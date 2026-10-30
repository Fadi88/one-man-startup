"""Run every check under tools/checks/ in parallel and report one verdict.

A check is any tools/checks/*.py that does not carry a `# NOT_A_CHECK, reason`
line. Each prints PASS / FAIL / SKIP lines and exits 0 when green.

Exit codes:
  0  every check green
  2  red, but every failing line is registered in tools/known_red.json
  1  anything else: a new red, an overdue recheck, or a broken check

Known reds are matched by the failing line, not the file, so a second,
different failure in the same check still shows up as NEW RED. A register entry that is
malformed (a missing key, a `fails` that is not a whole FAIL line, a date that is not a date)
makes the sweep BROKEN, since an empty `fails` would silence every red in its check (TPL-13).

Checks run with UTF-8 output whatever the system code page, so a FAIL line in Arabic or with an
accent cannot crash the sweep, and each check has a time limit, so a hung one cannot hang it.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKS = ROOT / "tools" / "checks"
KNOWN = ROOT / "tools" / "known_red.json"
# Longer than the product suite's own limit in regression_check.py.
TIMEOUT = 2400
KEYS = ("check", "fails", "reason", "decided_by", "decided_on", "recheck")


def discover() -> list[Path]:
    found = []
    for p in sorted(CHECKS.glob("*.py")):
        head = p.read_text(encoding="utf-8").splitlines()[:5]
        marker = [l for l in head if l.startswith("# NOT_A_CHECK")]
        if marker:
            if "," not in marker[0]:
                print(f"BROKEN  {p.name}: NOT_A_CHECK needs a reason after a comma")
                sys.exit(1)
            continue
        found.append(p)
    return found


def register_problems(known: object) -> list[str]:
    """Every way the known-red register is malformed. Pure, so runall_check can sample it."""
    if not isinstance(known, list):
        return ["tools/known_red.json is not a list"]
    out = []
    for i, k in enumerate(known):
        if not isinstance(k, dict):
            out.append(f"entry {i} is not an object")
            continue
        missing = [key for key in KEYS if key not in k]
        if missing:
            out.append(f"entry {i} has no {', '.join(missing)}")
            continue
        if not isinstance(k["fails"], str) or not k["fails"].startswith("FAIL") or len(k["fails"].strip()) < 10:
            out.append(f"entry {i}: fails must be a whole FAIL line, not {k['fails']!r}")
        for key in ("decided_on", "recheck"):
            if key == "recheck" and k[key] is None:
                continue
            try:
                dt.date.fromisoformat(str(k[key]))
            except ValueError:
                out.append(f"entry {i}: {key} {k[key]!r} is not a date like 2026-04-01")
    return out


def run(check: Path) -> tuple[Path, int, str, float]:
    start = dt.datetime.now()
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    try:
        proc = subprocess.run([sys.executable, str(check)], cwd=ROOT, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", env=env, timeout=TIMEOUT)
        code, out = proc.returncode, proc.stdout + proc.stderr
    except subprocess.TimeoutExpired:
        code, out = 1, f"FAIL  {check.name} ran past {TIMEOUT} seconds and was stopped"
    secs = (dt.datetime.now() - start).total_seconds()
    return check, code, out, secs


def main() -> int:
    # A terminal on a narrow code page shows '?' for what it cannot draw rather than crashing.
    sys.stdout.reconfigure(errors="replace")
    known = json.loads(KNOWN.read_text(encoding="utf-8")) if KNOWN.exists() else []
    bad = register_problems(known)
    if bad:
        for b in bad:
            print(f"BROKEN  TPL-13 tools/known_red.json {b}")
        return 1
    checks = discover()
    if not checks:
        print("BROKEN  no checks found under tools/checks/, a sweep that runs nothing is not green")
        return 1
    with ThreadPoolExecutor() as pool:
        results = list(pool.map(run, checks))

    today = dt.date.today().isoformat()
    verdict = 0
    skips = 0
    for check, code, out, secs in results:
        name = check.name
        fails = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL")]
        skips += sum(1 for l in out.splitlines() if l.strip().startswith("SKIP"))
        for l in out.splitlines():
            if l.strip().startswith("SKIP"):
                print(f"  {name}: {l.strip()}")
        if code == 0 and not fails:
            print(f"{name:<32} ok     {secs:5.1f}s")
            stale = [k for k in known if k["check"] == name]
            for k in stale:
                print(f"  {name}: now passes, prune its known_red entry ({k['fails']!r})")
            continue
        if code != 0 and not fails:
            print(f"{name:<32} BROKEN exit {code} with no FAIL line:\n{out}")
            verdict = 1
            continue
        mine = [k for k in known if k["check"] == name]
        for line in fails:
            match = next((k for k in mine if k["fails"] in line), None)
            if match is None:
                print(f"{name:<32} NEW RED  {line}")
                verdict = 1
            elif match.get("recheck") and match["recheck"] < today:
                print(f"{name:<32} RECHECK OVERDUE ({match['recheck']})  {line}")
                verdict = 1
            else:
                print(f"{name:<32} KNOWN RED  {line}  [{match['decided_by']}, {match['decided_on']}]")
                verdict = verdict or 2

    print(f"\n{len(checks)} checks, {skips} SKIP lines")
    print({0: "GREEN", 2: "RED, every red is registered as known", 1: "RED"}[verdict])
    return verdict


if __name__ == "__main__":
    sys.exit(main())
