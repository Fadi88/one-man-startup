"""TPL-109, TPL-110: older features are guarded by their spec tests, not by anyone's reading.

TPL-109: the sweep runs the product's whole test suite, project.toml [stack] test_command, so
every earlier feature's tests run on every round, not only the tests of the change. It SKIPs
while there is no product suite (the command is empty, "unset" or "none yet", as setup writes
before code exists, and no test folder or release exists either); once tests or a release exist,
a command still unset is red. A non-zero exit FAILs with one FAIL line per failing line of the
suite's output, numbers and timings blanked, so a known red accepted for one failing test does
not hide a second test that breaks later (skills/known-reds/). A suite past its time limit is
stopped with every process it started.

TPL-110: a row a release shipped stays guarded. The `Rows shipped:` line of each
docs/work/<id>/release.md (with any indented lines that continue it) names the rows; ranges
("RCPT-1 to RCPT-4", "RCPT-1 to 4", "RCPT-1 through RCPT-4", "RCPT-1..RCPT-4",
"RCPT-1 - RCPT-4") count every row between. Every one must be T or n/a; a shipped row that is
M, U or X, or no row at all, is red until a test names it or the founder accepts it as a known
red. A release.md with no `Rows shipped:` line is red too.

Both readers run first on built-in samples, so a template with no product still proves the check
works.
"""
from __future__ import annotations

import os
import re
import signal
import subprocess
import sys
import time
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROW = re.compile(r"^\| ([A-Z][A-Z0-9]*-\d+[a-z]?) \| .+ \| ([A-Za-z/]+) \|$", re.M)
ID = re.compile(r"\b([A-Z][A-Z0-9]*-\d+[a-z]?)\b")
# "to" and "through" may drop the area on the right ("RCPT-1 to 4"); a dash or ".." must repeat
# it ("RCPT-1 - RCPT-4"), so a date after a dash is never read as the end of a range.
RANGE = re.compile(r"\b([A-Z][A-Z0-9]*)-(\d+)\s*(?:(?:to|through)\s+(?:\1-)?|(?:\.\.|-|\u2013)\s*\1-)(\d+)\b")
MAX_RANGE = 200
# The line and any indented lines that continue it, as a wrapped document writes them.
SHIPPED = re.compile(r"^Rows shipped:(.*(?:\n[ \t]+\S.*)*)", re.M)
NO_SUITE = {"", "unset", "none yet", "none"}
FAILING = re.compile(r"\b(fail|failed|failure|failing|error|errors)\b|\u2717|\u2715", re.I)
PASSING = re.compile(r"^\s*(PASS|ok)\b|\bPASSED\b")
NUMBERS = re.compile(r"\d+(\.\d+)?\s*(ms|s|sec|seconds)?\b")
GUARDED = {"T", "n/a"}
TIMEOUT = 1800


def shipped(text: str) -> set[str] | None:
    """Every row id on the release's `Rows shipped:` lines, ranges expanded; None when there is
    no such line. Pure, so it can be sampled."""
    lines = SHIPPED.findall(text)
    if not lines:
        return None
    ids = set()
    for line in lines:
        ids |= set(ID.findall(line))
        for area, lo, hi in RANGE.findall(line):
            lo, hi = int(lo), int(hi)
            if not 0 < hi - lo <= MAX_RANGE:
                ids.add(f"{area}-{lo}..{hi} (not a range of rows)")
                continue
            ids |= {f"{area}-{n}" for n in range(lo, hi + 1)}
    return ids


def unguarded(ids: set[str], status: dict[str, str]) -> list[str]:
    """The shipped ids that no test guards, sorted; an id that is no row at all counts too."""
    return sorted(i for i in ids if status.get(i) not in GUARDED)


def failing_lines(output: str) -> list[str]:
    """The suite's failing lines, numbers blanked so the same failure matches run after run."""
    out = []
    for raw in output.splitlines():
        if FAILING.search(raw) and not PASSING.search(raw):
            line = NUMBERS.sub("N", raw.strip())[:160]
            if line not in out:
                out.append(line)
    return out[:20]


def suite_state(command: str, test_paths: list, released: bool) -> str:
    """run, skip (no product suite yet) or fail (tests or a release exist, yet no command runs them)."""
    if command.lower() not in NO_SUITE:
        return "run"
    return "fail" if test_paths or released else "skip"


SAMPLE_STATUS = {"RCPT-1": "T", "RCPT-2": "T", "RCPT-3": "M", "RCPT-4": "n/a", "LAUNCH-1": "U",
                 "TPL-41a": "M"}
SAMPLES = [
    ("Rows shipped: RCPT-1, RCPT-2.", []),
    ("Rows shipped: RCPT-1 to RCPT-4.", ["RCPT-3"]),
    ("Rows shipped: RCPT-1 to 4.", ["RCPT-3"]),
    ("Rows shipped: RCPT-1 through RCPT-4", ["RCPT-3"]),
    ("Rows shipped: RCPT-1..RCPT-4", ["RCPT-3"]),
    ("Rows shipped: RCPT-1 - RCPT-4", ["RCPT-3"]),
    ("Rows shipped: RCPT-2, LAUNCH-1\nNot shipped: RCPT-3, see HTTP-200.", ["LAUNCH-1"]),
    ("Rows shipped: TPL-41a", ["TPL-41a"]),
    ("Rows shipped: RCPT-9", ["RCPT-9"]),
    ("Rows shipped: RCPT-1, RCPT-2,\n  RCPT-3.", ["RCPT-3"]),
    ("Rows shipped: RCPT-2 - 2026-11-01 release", []),
    ("Rows shipped: RCPT-1 to 900", ["RCPT-1..900 (not a range of rows)"]),
]
SUITE_SAMPLES = [
    ("exit 0", f'"{sys.executable}" -c "print(1)"', 0),
    ("exit 1", f'"{sys.executable}" -c "print(\'FAILED test_total - 0.31s\'); raise SystemExit(1)"', 1),
]
# A child that starts its own child and outlives the time limit is stopped, tree and all.
HANG = (f'"{sys.executable}" -c "import subprocess,sys,time; '
        f'subprocess.Popen([sys.executable, \'-c\', \'import time; time.sleep(60)\']); time.sleep(60)"')


def selftest() -> list[str]:
    fails = []
    for text, want in SAMPLES:
        got = shipped(text)
        got = None if got is None else unguarded(got, SAMPLE_STATUS)
        if got != want:
            fails.append(f"FAIL  TPL-110 self-test: {text!r} gave {got}, wanted {want}")
    if shipped("Release notes with no rows line. RCPT-3") is not None:
        fails.append("FAIL  TPL-110 self-test: a release with no 'Rows shipped:' line was read as shipping rows")
    for label, command, want in SUITE_SAMPLES:
        got = len(suite(command)) > 0
        if got != bool(want):
            fails.append(f"FAIL  TPL-109 self-test: suite sample {label!r} read wrongly")
    started = time.monotonic()
    code, _ = run_tree(HANG, 2)
    if code is not None or time.monotonic() - started > 20:
        fails.append("FAIL  TPL-109 self-test: a hung suite and its child were not stopped at the time limit")
    a = failing_lines("FAILED test_total - 0.31s\nok test_x\n2 failed in 1.2s\nPASS src/error.test.ts")
    b = failing_lines("FAILED test_total - 0.29s\nok test_x\n2 failed in 1.4s\nt/errors.py::test_ok PASSED")
    if a != b or len(a) != 2:
        fails.append(f"FAIL  TPL-109 self-test: failing lines not stable across runs: {a} {b}")
    for cmd, paths, released, want in [("none yet", [], False, "skip"), ("unset", ["tests"], False, "fail"),
                                       ("none yet", [], True, "fail"), ("pytest", [], False, "run")]:
        if suite_state(cmd, paths, released) != want:
            fails.append(f"FAIL  TPL-109 self-test: test_command {cmd!r} with tests {paths} gave "
                         f"{suite_state(cmd, paths, released)!r}, wanted {want!r}")
    return fails


def run_tree(command: str, timeout: float) -> tuple[int | None, str]:
    """Run a shell command; on timeout stop it and every process it started (a test runner's
    workers would otherwise keep the output open and hang the sweep). None for a timeout."""
    proc = subprocess.Popen(command, shell=True, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", errors="replace", start_new_session=os.name != "nt")
    try:
        out, _ = proc.communicate(timeout=timeout)
        return proc.returncode, out
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)
        else:
            os.killpg(proc.pid, signal.SIGKILL)
        try:
            proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        return None, ""


def statuses() -> dict[str, str]:
    out = {}
    for f in (ROOT / "docs" / "requirements").glob("*.md"):
        if not f.name.startswith("p1-"):
            out.update(dict(ROW.findall(f.read_text(encoding="utf-8"))))
    return out


def suite(command: str) -> list[str]:
    """TPL-109: run the whole product suite; its failing lines, or none."""
    code, output = run_tree(command, TIMEOUT)
    if code is None:
        return [f"FAIL  TPL-109 the test suite ({command}) ran past {TIMEOUT} seconds and was stopped"]
    if code == 0:
        return []
    lines = failing_lines(output) or [f"exit {code}, no failing line found; last line: "
                                      f"{(output.strip().splitlines() or [''])[-1][:120]}"]
    return [f"FAIL  TPL-109 test suite: {l}" for l in lines]


def main() -> int:
    fails = selftest()
    stack = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("stack", {})
    command = str(stack.get("test_command", "unset")).strip()
    releases = sorted((ROOT / "docs" / "work").glob("*/release.md"))
    state = suite_state(command, stack.get("test_paths", []), bool(releases))
    if state == "skip":
        print(f"SKIP  TPL-109 [stack] test_command is {command!r}, so there is no product suite to run yet")
    elif state == "fail":
        fails.append(f"FAIL  TPL-109 [stack] test_command is {command!r} but the product has tests or a release; "
                     "the developer who wrote the first test fills it in (skills/verify-green/)")
    else:
        print(f"      TPL-109 running the whole product suite: {command}", flush=True)
        fails += suite(command)
    status = statuses()
    for f in releases:
        rel = f.relative_to(ROOT).as_posix()
        ids = shipped(f.read_text(encoding="utf-8"))
        if ids is None:
            fails.append(f"FAIL  TPL-110 {rel} has no 'Rows shipped:' line naming the rows it ships")
            continue
        for rid in unguarded(ids, status):
            what = status.get(rid, "not a row")
            fails.append(f"FAIL  TPL-110 {rid} shipped in {rel} but is {what}: no test guards it "
                         "against later changes")
    for line in fails:
        print(line)
    if not fails:
        print(f"PASS  TPL-109 TPL-110 read {len(releases)} releases, {len(SAMPLES)} release samples and "
              f"{len(SUITE_SAMPLES) + 1} suite samples; every shipped row is guarded by a test")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
