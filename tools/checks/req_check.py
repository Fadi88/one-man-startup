"""TPL-9 and TPL-10: requirement rows are well formed and the index is computed.

    python tools/checks/req_check.py         check
    python tools/checks/req_check.py --fix   rewrite the index table in docs/REQUIREMENTS.md

A T row must be named by a check under tools/checks/ or by a test in a folder listed in
project.toml [stack] test_paths (its id appears in the file's text, TPL-102). Every id a check cites must exist. Area files are every
docs/requirements/*.md that is not a p1-* file.
"""
from __future__ import annotations

import re
import sys
import tomllib
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


def test_ids(root: Path, paths: list[str]) -> tuple[set[str], list[str]]:
    """TPL-102: every row id named in a file under the product's test folders, and the paths
    that are not folders inside the repository."""
    found: set[str] = set()
    bad: list[str] = []
    for rel in paths:
        base = (root / rel).resolve()
        if not base.is_relative_to(root.resolve()) or not base.exists():
            bad.append(rel)
            continue
        for f in [base] if base.is_file() else base.rglob("*"):
            if f.is_file() and "node_modules" not in f.parts and f.stat().st_size < 2_000_000:
                found.update(ID.findall(f.read_text(encoding="utf-8", errors="ignore")))
    return found, bad


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
stack = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("stack", {})
in_tests, bad_paths = test_ids(ROOT, stack.get("test_paths", []))
named |= in_tests
for rel in bad_paths:
    fail(f"TPL-102 project.toml [stack] test_paths names {rel!r}, which is not a folder in this repository")
for rid, (fname, status) in sorted(rows.items()):
    if status == "T" and rid not in named:
        fail(f"TPL-9 {rid} is T but no check under tools/checks/ and no test in [stack] test_paths names it")

# TPL-102: the test folders are read, recursively, and a path outside the repository is refused.
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    t = Path(tmp)
    (t / "tests" / "auth").mkdir(parents=True)
    (t / "tests" / "auth" / "test_login.py").write_text("def test_lockout():  # AUTH-12\n", encoding="utf-8")
    got, _ = test_ids(t, ["tests"])
    _, bad = test_ids(t, ["../outside", "missing"])
    if "AUTH-12" not in got or bad != ["../outside", "missing"]:
        fail("TPL-102 test_ids does not read a nested test file, or lets a path outside the repository through")
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
