"""TPL-80: every date that has come due, found once and read by the session reminder, the status
page and its own check.

Three kinds of date: an open assumption's confirm-by (docs/ASSUMPTIONS.md), a known red's recheck
(tools/known_red.json) and a running or planned experiment's read date (the "At a glance" table
of docs/EXPERIMENTS.md). A date on or before today is due; one before today is overdue.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSUMPTION = re.compile(r"^\| (A-\d+) \|")
EXPERIMENT = re.compile(r"^\| (\d+) \| [^|]+ \| ([^|]+?) \| (running|planned) \| (\d{4}-\d{2}-\d{2}) \|$")


def _date(text: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(text.strip())
    except ValueError:
        return None


def due(root: Path = ROOT, today: dt.date | None = None) -> list[dict]:
    """Every date on or before today, oldest first: {kind, id, what, date, overdue}."""
    today = today or dt.date.today()
    found = []

    assumptions = root / "docs" / "ASSUMPTIONS.md"
    if assumptions.exists():
        for line in assumptions.read_text(encoding="utf-8").splitlines():
            if not ASSUMPTION.match(line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 7 and cells[5] == "open":
                found.append({"kind": "assumption", "id": cells[0], "what": cells[1],
                              "date": _date(cells[4]), "file": "docs/ASSUMPTIONS.md"})

    known = root / "tools" / "known_red.json"
    if known.exists():
        for k in json.loads(known.read_text(encoding="utf-8")):
            if k.get("recheck"):
                found.append({"kind": "known red", "id": k["check"], "what": k["fails"],
                              "date": _date(k["recheck"]), "file": "tools/known_red.json"})

    experiments = root / "docs" / "EXPERIMENTS.md"
    if experiments.exists():
        for line in experiments.read_text(encoding="utf-8").splitlines():
            m = EXPERIMENT.match(line.strip())
            if m:
                found.append({"kind": "experiment", "id": m[1], "what": m[2],
                              "date": _date(m[4]), "file": "docs/EXPERIMENTS.md"})

    out = [f for f in found if f["date"] is not None and f["date"] <= today]
    for f in out:
        f["overdue"] = f["date"] < today
    return sorted(out, key=lambda f: f["date"])


def line(item: dict) -> str:
    when = f"overdue since {item['date']}" if item["overdue"] else "due today"
    what = item["what"] if len(item["what"]) <= 70 else item["what"][:67] + "..."
    return f"{item['kind']} {item['id']} ({item['file']}), {when}: {what}"
