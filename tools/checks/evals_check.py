"""TPL-79: the orchestrator's eval cases are well formed and the scorer scores them right.

Runs no AI call. Each case needs an id, a request, a track of fix, feature or bet, and agent
names that exist in agents/, with no agent both required and forbidden. The scorer is checked
on a right answer and on each kind of wrong one, so a scorer that passes everything fails here.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import run_evals

fails = 0


def fail(msg: str) -> None:
    global fails
    print(f"FAIL  {msg}")
    fails += 1


data = run_evals.load()
agents = {p.stem for p in (ROOT / "agents").glob("*.md")}
cases = data.get("case", [])
if not cases or not data.get("assume"):
    fail("TPL-79 tools/evals/orchestrator.toml has no cases or no 'assume' line")
seen = set()
for c in cases:
    cid = c.get("id", "?")
    if cid in seen:
        fail(f"TPL-79 case {cid} appears twice")
    seen.add(cid)
    if not c.get("request") or c.get("track") not in run_evals.TRACKS:
        fail(f"TPL-79 case {cid} needs a request and a track of fix, feature or bet")
    named = set(c.get("must", [])) | set(c.get("must_not", [])) | {a for g in c.get("one_of", []) for a in g}
    for a in sorted(named - agents):
        fail(f"TPL-79 case {cid} names {a!r}, which is not in agents/")
    if set(c.get("must", [])) & set(c.get("must_not", [])):
        fail(f"TPL-79 case {cid} both requires and forbids {set(c['must']) & set(c['must_not'])}")

case = {"track": "fix", "must": ["qa"], "one_of": [["web-dev", "backend-dev"]], "must_not": ["legal"]}
for answer, want in [({"track": "fix", "agents": ["qa", "web-dev"]}, 0),
                     ({"track": "bet", "agents": ["qa", "web-dev"]}, 1),
                     ({"track": "fix", "agents": ["web-dev"]}, 1),
                     ({"track": "fix", "agents": ["qa"]}, 1),
                     ({"track": "fix", "agents": ["qa", "web-dev", "legal"]}, 1),
                     ({}, 3)]:
    if len(run_evals.score(case, answer)) != want:
        fail(f"TPL-79 the scorer gives {run_evals.score(case, answer)} for {answer}, wanted {want} problem(s)")

if not fails:
    print(f"PASS  TPL-79 {len(cases)} eval cases well formed, the scorer catches each kind of wrong answer")
sys.exit(1 if fails else 0)
