"""TPL-9 and TPL-10: requirement rows are well formed and the index is computed.

    python tools/checks/req_check.py         check
    python tools/checks/req_check.py --fix   rewrite the index table in docs/REQUIREMENTS.md

A T row must be named by a check under tools/checks/ (its id appears in the
check's text). Every id a check cites must exist. Area files are every
docs/requirements/*.md that is not a p1-* file.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQ = ROOT / "docs" / "requirements"
INDEX = ROOT / "docs" / "REQUIREMENTS.md"
ROW = re.compile(r"^\| ([A-Z][A-Z0-9]*-\d+[a-z]?) \| (.+) \| ([A-Za-z/]+) \|$")
ID = re.compile(r"\b([A-Z][A-Z0-9]*-\d+[a-z]?)\b")
STATUSES = ["T", "M", "U", "X", "n/a"]
START, END = "<!-- req-index:start -->", "<!-- req-index:end -->"

fails: list[str] = []


def fail(msg: str) -> None:
    fails.append(msg)
    print(f"FAIL  {msg}")


areas = sorted(p for p in REQ.glob("*.md") if not p.name.startswith("p1-"))
if not areas:
    fail("TPL-9 no area files under docs/requirements/, a check over nothing is not a pass")
    sys.exit(1)

rows: dict[str, tuple[str, str]] = {}
per_file: dict[str, tuple[str, Counter]] = {}
for f in areas:
    counts: Counter = Counter()
    prefixes = set()
    for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| ") or line.startswith(("| ID ", "|---")):
            continue
        m = ROW.match(line)
        if not m:
            fail(f"TPL-9 {f.name}:{n} is not a well formed row")
            continue
        rid, _, status = m.groups()
        if status not in STATUSES:
            fail(f"TPL-9 {f.name}:{n} {rid} has status {status!r}, not one of {STATUSES}")
        if rid in rows:
            fail(f"TPL-9 {rid} appears twice ({rows[rid][0]} and {f.name})")
        rows[rid] = (f.name, status)
        counts[status] += 1
        prefixes.add(rid.split("-")[0])
    if len(prefixes) > 1:
        fail(f"TPL-9 {f.name} mixes prefixes {sorted(prefixes)}; one area per file")
    per_file[f.name] = (next(iter(prefixes), "?"), counts)

checks_text = {p.name: p.read_text(encoding="utf-8") for p in (ROOT / "tools" / "checks").glob("*.py")}
named = {rid for text in checks_text.values() for rid in ID.findall(text)}
for rid, (fname, status) in sorted(rows.items()):
    if status == "T" and rid not in named:
        fail(f"TPL-9 {rid} is T but no check under tools/checks/ names it")
for name, text in checks_text.items():
    for rid in set(ID.findall(text)):
        if rid.split("-")[0] in {p for p, _ in per_file.values()} and rid not in rows:
            fail(f"TPL-9 {name} cites {rid}, which has no row")

table = ["| File | Prefix | Rows | T | M | U | X | n/a |", "|---|---|---|---|---|---|---|---|"]
for fname, (prefix, c) in per_file.items():
    table.append(f"| `requirements/{fname}` | {prefix} | {sum(c.values())} | "
                 + " | ".join(str(c[s]) for s in STATUSES) + " |")
index = INDEX.read_text(encoding="utf-8")
if START not in index or END not in index:
    fail("TPL-10 docs/REQUIREMENTS.md has lost its req-index markers")
    sys.exit(1)
head, rest = index.split(START, 1)
_, tail = rest.split(END, 1)
want = f"{head}{START}\n" + "\n".join(table) + f"\n{END}{tail}"
if want != index:
    if "--fix" in sys.argv:
        INDEX.write_text(want, encoding="utf-8", newline="\n")
        print("fixed  docs/REQUIREMENTS.md index table rewritten")
    else:
        fail("TPL-10 the index table in docs/REQUIREMENTS.md is stale, run python tools/checks/req_check.py --fix")

if not fails:
    print(f"PASS  {len(rows)} rows in {len(areas)} area files, index current, every T row named by a check")
sys.exit(1 if fails else 0)
