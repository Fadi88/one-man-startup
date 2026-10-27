"""TPL-63, TPL-80: the Claude Code SessionStart hook. Prints the standing reminder at the start of a
session and again after compaction, when a long session has lost its first instructions.

Claude Code runs it with JSON on stdin whose `source` is startup, resume, clear or compact
(https://code.claude.com/docs/en/hooks.md); what it prints is added to the session's context.
Other tools have no equivalent hook and rely on AGENTS.md being read at the start.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
import overdue


def message(source: str, today=None) -> str:
    lines = [
        "Session reminder (tools/session_start.py):",
        "- Read project.toml first. If [owner] or [product] is unset, run skills/setup/ before anything else.",
        "- You answer the founder as orchestrator (agents/orchestrator.md); the constitution is AGENTS.md.",
        "- Every change cites a requirement row; the round ends green (python tools/run_all.py).",
    ]
    if source == "compact":
        lines.append(
            "- Context was just compacted: re-open docs/work/<id>/status.md for the work in progress, "
            "and re-read the skill you are following rather than working from memory of it."
        )
    work = ROOT / "docs" / "work"
    if work.is_dir():
        recent = sorted((p for p in work.iterdir() if p.is_dir()), key=lambda p: p.stat().st_mtime, reverse=True)[:3]
        if recent:
            lines.append("- Recent work folders: " + ", ".join(p.name for p in recent))
    due = overdue.due(ROOT, today)
    if due:
        lines.append("- Dates that have come due; tell the founder before other work:")
        lines += [f"  - {overdue.line(d)}" for d in due]
    return "\n".join(lines)


def main() -> int:
    try:
        source = json.load(sys.stdin).get("source", "startup")
    except (json.JSONDecodeError, ValueError, OSError):
        source = "startup"
    print(message(source))
    return 0


if __name__ == "__main__":
    sys.exit(main())
