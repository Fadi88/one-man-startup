"""TPL-13: run_all.py exits 0, 2 and 1 when it should.

Builds a throwaway repo with one fake check and drives run_all through each
case: green, a red registered as known, the same red past its recheck date,
a second unregistered red in the same check, and a check that crashes. Also: a FAIL line in
Arabic with an accent is matched, not a crash, and a malformed register (an empty `fails`, a
date that is not a date) makes the sweep BROKEN instead of silencing every red.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FAKE = """import sys
mode = open("mode.txt").read().strip()
if mode == "green":
    print("PASS  fine")
elif mode == "crash":
    raise SystemExit(3)
elif mode == "accent":
    print("FAIL  café العربية ✓")
    sys.exit(1)
else:
    print("FAIL  first problem")
    if mode == "two":
        print("FAIL  second problem")
    sys.exit(1)
"""


def run(tmp: Path, mode: str, known: list) -> int:
    (tmp / "mode.txt").write_text(mode, encoding="utf-8")
    (tmp / "tools" / "known_red.json").write_text(json.dumps(known))
    return subprocess.run([sys.executable, "tools/run_all.py"], cwd=tmp, capture_output=True).returncode


entry = {"check": "fake.py", "fails": "FAIL  first problem", "reason": "test", "decided_by": "founder",
         "decided_on": "2026-01-01", "recheck": "2999-01-01"}
cases = [
    ("green", "green", [], 0),
    ("known red", "one", [entry], 2),
    ("overdue recheck", "one", [{**entry, "recheck": "2000-01-01"}], 1),
    ("standing known red", "one", [{**entry, "recheck": None}], 2),
    ("second red in the same check", "two", [entry], 1),
    ("unregistered red", "one", [], 1),
    ("crashing check", "crash", [], 1),
    ("accented Arabic red registered as known", "accent",
     [{**entry, "fails": "FAIL  café العربية"}], 2),
    ("empty fails silences nothing", "one", [{**entry, "fails": ""}], 1),
    ("recheck that is not a date", "one", [{**entry, "recheck": "next month"}], 1),
    ("entry with a key missing", "one", [{k: v for k, v in entry.items() if k != "reason"}], 1),
]

failed = 0
with tempfile.TemporaryDirectory() as d:
    tmp = Path(d)
    (tmp / "tools" / "checks").mkdir(parents=True)
    shutil.copy(ROOT / "tools" / "run_all.py", tmp / "tools" / "run_all.py")
    (tmp / "tools" / "checks" / "fake.py").write_text(FAKE, encoding="utf-8")
    for label, mode, known, want in cases:
        got = run(tmp, mode, known)
        if got == want:
            print(f"PASS  {label}: exit {got}")
        else:
            print(f"FAIL  {label}: exit {got}, expected {want}")
            failed += 1
sys.exit(1 if failed else 0)
