"""TPL-16: every open assumption can be confirmed and is not overdue.

Reads the table in docs/ASSUMPTIONS.md. Each row needs a unique A-n id, a way
to confirm it, a YYYY-MM-DD confirm-by date and a status of open, confirmed or
disproved. An open row past its date fails; a settled row must say what
settled it.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
f = ROOT / "docs" / "ASSUMPTIONS.md"
if not f.exists():
    print("FAIL  TPL-16 docs/ASSUMPTIONS.md is missing")
    sys.exit(1)

today = dt.date.today()
rows = [l for l in f.read_text(encoding="utf-8").splitlines() if re.match(r"^\| A-\d+ \|", l)]
fails = 0
seen = set()
for line in rows:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 7:
        print(f"FAIL  TPL-16 malformed row: {line[:60]}")
        fails += 1
        continue
    aid, claim, used, how, by, status, settled = cells
    if aid in seen:
        print(f"FAIL  TPL-16 {aid} appears twice")
        fails += 1
    seen.add(aid)
    if not how:
        print(f"FAIL  TPL-16 {aid} has no way to confirm it")
        fails += 1
    try:
        due = dt.date.fromisoformat(by)
    except ValueError:
        print(f"FAIL  TPL-16 {aid} confirm-by {by!r} is not a YYYY-MM-DD date")
        fails += 1
        continue
    if status not in {"open", "confirmed", "disproved"}:
        print(f"FAIL  TPL-16 {aid} status {status!r} is not open, confirmed or disproved")
        fails += 1
    elif status == "open" and due < today:
        print(f"FAIL  TPL-16 {aid} is still open and was due {by}: confirm it, disprove it, or ask the founder for a new date")
        fails += 1
    elif status != "open" and not settled:
        print(f"FAIL  TPL-16 {aid} is {status} but does not say what settled it")
        fails += 1

if not fails:
    open_n = sum(1 for l in rows if "| open |" in l)
    print(f"PASS  read {len(rows)} assumptions, {open_n} open, none overdue")
sys.exit(1 if fails else 0)
