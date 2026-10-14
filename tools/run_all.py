"""Run every check under tools/checks/ in parallel and report one verdict.

A check is any tools/checks/*.py that does not carry a `# NOT_A_CHECK, reason`
line. Each prints PASS / FAIL / SKIP lines and exits 0 when green.

Exit codes:
  0  every check green
  2  red, but every failing line is registered in tools/known_red.json
  1  anything else: a new red, an overdue recheck, or a broken check

Known reds are matched by the failing line, not the file, so a second,
different failure in the same check still shows up as NEW RED.
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKS = ROOT / "tools" / "checks"
KNOWN = ROOT / "tools" / "known_red.json"


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


def run(check: Path) -> tuple[Path, int, str, float]:
    start = dt.datetime.now()
    proc = subprocess.run(
        [sys.executable, str(check)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    secs = (dt.datetime.now() - start).total_seconds()
    return check, proc.returncode, proc.stdout + proc.stderr, secs


def main() -> int:
    known = json.loads(KNOWN.read_text(encoding="utf-8")) if KNOWN.exists() else []
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
