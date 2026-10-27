"""TPL-79: test the orchestrator's judgement on fixed requests (tools/evals/orchestrator.toml).

    python tools/run_evals.py              list the cases and what each costs to run, run nothing
    python tools/run_evals.py --run [ID]   ask the AI tool for each pick (or one case) and score it

Each case is one paid call to Claude Code (`claude -p --agent orchestrator`), read-only tools
only, told not to do the work. Run it when the founder asks, after editing an agent file or
AGENTS.md, and keep the scores beside the change. The sweep never runs it; it only checks the
cases are well formed (tools/checks/evals_check.py).
"""
from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tools" / "evals" / "orchestrator.toml"
TRACKS = {"fix", "feature", "bet"}
SCHEMA = {"type": "object", "required": ["track", "agents"], "properties": {
    "track": {"type": "string", "enum": sorted(TRACKS)},
    "agents": {"type": "array", "items": {"type": "string"}}}}


def load() -> dict:
    return tomllib.loads(CASES.read_text(encoding="utf-8"))


def score(case: dict, answer: dict) -> list[str]:
    """What is wrong with an answer, empty when it passes."""
    got = set(answer.get("agents", []))
    wrong = []
    if answer.get("track") != case["track"]:
        wrong.append(f"track {answer.get('track')!r}, wanted {case['track']!r}")
    wrong += [f"missing {a}" for a in case.get("must", []) if a not in got]
    wrong += [f"none of {', '.join(group)}" for group in case.get("one_of", []) if not got & set(group)]
    wrong += [f"named {a}, which it must not" for a in case.get("must_not", []) if a in got]
    return wrong


def prompt(assume: str, request: str) -> str:
    return (f"This is a test of your routing, not a request to work. {assume} Do not start any work, "
            "edit any file or ask the founder anything. Read agents/orchestrator.md and AGENTS.md if you "
            "need to. Your whole reply is one JSON object and nothing else, no prose and no code fence, "
            'shaped {"track": "fix" or "feature" or "bet", "agents": [every agent you would bring in, '
            f"by its name in agents/]}}, for this request from the founder:\n\n{request}")


def ask(text: str) -> dict:
    r = subprocess.run(["claude", "-p", text, "--agent", "orchestrator", "--tools", "Read,Grep,Glob",
                        "--output-format", "json", "--json-schema", json.dumps(SCHEMA)],
                       cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        raise RuntimeError((r.stderr or r.stdout).strip()[-300:])
    out = json.loads(r.stdout)
    if isinstance(out.get("structured_output"), dict):
        answer = out["structured_output"]
    else:  # the answer can come back as text, sometimes fenced; take its JSON object
        text = out.get("result", "")
        answer = json.loads(text[text.find("{"):text.rfind("}") + 1])
    answer["cost"] = out.get("total_cost_usd")
    return answer


def main(argv: list[str]) -> int:
    data = load()
    cases = data["case"]
    if "--run" not in argv:
        for c in cases:
            print(f"{c['id']:16} {c['track']:8} {c['request']}")
        print(f"\n{len(cases)} cases, one paid AI call each. Run with --run, or --run ID for one.")
        return 0
    only = argv[argv.index("--run") + 1:] or None
    passed, spent = 0, 0.0
    chosen = [c for c in cases if not only or c["id"] in only]
    for c in chosen:
        answer: dict = {}
        try:
            answer = ask(prompt(data["assume"], c["request"]))
            spent += answer.get("cost") or 0
            wrong = score(c, answer)
        except (RuntimeError, ValueError, OSError) as e:
            wrong = [f"no answer: {e}"]
        passed += not wrong
        picked = f" (picked {answer.get('track')}: {', '.join(answer.get('agents', []))})" if wrong and answer else ""
        print(f"{'PASS' if not wrong else 'FAIL'}  {c['id']}" + (f": {'; '.join(wrong)}{picked}" if wrong else ""))
    print(f"\n{passed} of {len(chosen)} passed, cost reported by the tool: {spent:.2f} USD")
    return 0 if passed == len(chosen) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
