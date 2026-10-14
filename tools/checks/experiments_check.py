"""TPL-11: every open experiment was registered properly before it ran.

Each `### N. title` entry in docs/EXPERIMENTS.md must carry a Hypothesis, a
Prediction, a "Wrong if" and a Read date. An empty file passes and says so.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
f = ROOT / "docs" / "EXPERIMENTS.md"
if not f.exists():
    print("FAIL  TPL-11 docs/EXPERIMENTS.md is missing")
    sys.exit(1)
text = f.read_text(encoding="utf-8")
entries = re.split(r"^### ", text, flags=re.M)[1:]
NEEDED = ["**Hypothesis:**", "**Prediction:**", "**Wrong if:**", "**Read:**"]
fails = 0
for e in entries:
    title = e.splitlines()[0].strip()
    for field in NEEDED:
        if field not in e:
            print(f"FAIL  TPL-11 experiment {title!r} has no {field}")
            fails += 1
print(f"PASS  read {len(entries)} experiment entries, each fully registered" if not fails else "")
sys.exit(1 if fails else 0)
