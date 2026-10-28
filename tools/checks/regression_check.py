"""TPL-109, TPL-110: older features are guarded by their spec tests, not by anyone's reading.

TPL-109: the sweep runs the product's whole test suite, project.toml [stack] test_command, so
every earlier feature's tests run on every round, not only the tests of the change. It SKIPs
while the command is unset (no product yet) and FAILs on a non-zero exit with the last lines.

TPL-110: a row a release shipped stays guarded. Every row id named in a
docs/work/<id>/release.md (ranges written "RCPT-1 to RCPT-17" count every row between) must be
T, or n/a; a shipped row that is M, U or X is red until a test names it or the founder accepts
it as a known red (skills/known-reds/).

The release reader runs first on built-in samples, so a template with no releases still proves
the check works.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROW = re.compile(r"^\| ([A-Z][A-Z0-9]*-\d+[a-z]?) \| .+ \| ([A-Za-z/]+) \|$", re.M)
ID = re.compile(r"\b([A-Z][A-Z0-9]*)-(\d+)\b")
RANGE = re.compile(r"\b([A-Z][A-Z0-9]*)-(\d+) to \1-(\d+)\b")
GUARDED = {"T", "n/a"}
TIMEOUT = 1800


def shipped(text: str) -> set[str]:
    """Every row id a release names, ranges expanded. Pure, so it can be sampled."""
    ids = {f"{a}-{n}" for a, n in ID.findall(text)}
    for area, lo, hi in RANGE.findall(text):
        ids |= {f"{area}-{n}" for n in range(int(lo), int(hi) + 1)}
    return ids


def unguarded(ids: set[str], status: dict[str, str]) -> list[str]:
    """The shipped ids that are rows and that no test guards, sorted."""
    return sorted(i for i in ids if i in status and status[i] not in GUARDED)


SAMPLE_STATUS = {"RCPT-1": "T", "RCPT-2": "T", "RCPT-3": "M", "RCPT-4": "n/a", "LAUNCH-1": "U"}
SAMPLES = [
    ("Rows shipped: RCPT-1, RCPT-2.", []),
    ("Rows shipped: RCPT-1 to RCPT-4.", ["RCPT-3"]),
    ("Ships RCPT-2 and LAUNCH-1; see HTTP-200 in the notes.", ["LAUNCH-1"]),
    ("Nothing shipped.", []),
]


def selftest() -> list[str]:
    fails = []
    for text, want in SAMPLES:
        got = unguarded(shipped(text), SAMPLE_STATUS)
        if got != want:
            fails.append(f"FAIL  TPL-110 self-test: {text!r} gave {got}, wanted {want}")
    return fails


def statuses() -> dict[str, str]:
    out = {}
    for f in (ROOT / "docs" / "requirements").glob("*.md"):
        if not f.name.startswith("p1-"):
            out.update(dict(ROW.findall(f.read_text(encoding="utf-8"))))
    return out


def suite(command: str) -> list[str]:
    """TPL-109: run the whole product suite; the failing lines, or none."""
    try:
        r = subprocess.run(command, shell=True, cwd=ROOT, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return [f"FAIL  TPL-109 the test suite ({command}) ran past {TIMEOUT} seconds"]
    if r.returncode == 0:
        return []
    tail = (r.stdout + r.stderr).strip().splitlines()[-15:]
    return [f"FAIL  TPL-109 the test suite ({command}) exited {r.returncode}; an earlier feature "
            "or this change is broken. Last lines:"] + [f"      {l}" for l in tail]


def main() -> int:
    fails = selftest()
    stack = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("stack", {})
    command = str(stack.get("test_command", "unset")).strip()
    if command in ("", "unset"):
        print("SKIP  TPL-109 [stack] test_command is unset, so there is no product suite to run yet")
    else:
        fails += suite(command)
    status = statuses()
    releases = sorted((ROOT / "docs" / "work").glob("*/release.md"))
    for f in releases:
        for rid in unguarded(shipped(f.read_text(encoding="utf-8")), status):
            fails.append(f"FAIL  TPL-110 {rid} shipped in {f.relative_to(ROOT).as_posix()} but is "
                         f"{status[rid]}: no test guards it against later changes")
    for line in fails:
        print(line)
    if not fails:
        print(f"PASS  TPL-110 read {len(releases)} releases and {len(SAMPLES)} samples; every shipped "
              "row is guarded by a test")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
