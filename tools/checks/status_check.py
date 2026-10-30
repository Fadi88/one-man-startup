"""TPL-127, TPL-78, TPL-80, TPL-101, TPL-104: the status page and the session reminder report what the files say.

Builds a small project in a temporary folder (an overdue assumption, a known red past its
recheck, an experiment due today, one settled assumption and one future date that must not
show, a work folder waiting on the founder with two rulings, an open question) and checks that
tools/lib/overdue.py, tools/status_report.py and tools/session_start.py each report exactly that.
Then runs the real report once, so a broken file in this repository fails here too.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
sys.path.insert(0, str(ROOT / "tools"))
import overdue
import session_start
import status_report

TODAY = dt.date(2026, 6, 15)
fails = 0


def check(ok: bool, what: str) -> None:
    global fails
    print(f"{'PASS' if ok else 'FAIL'}  {what}")
    fails += not ok


def write(root: Path, rel: str, text: str) -> None:
    (root / rel).parent.mkdir(parents=True, exist_ok=True)
    (root / rel).write_text(text, encoding="utf-8")


with tempfile.TemporaryDirectory() as tmp:
    t = Path(tmp)
    write(t, "docs/ASSUMPTIONS.md",
          "| ID | Claim | Used in | How | By | Status | Settled by |\n|---|---|---|---|---|---|---|\n"
          "| A-1 | Old claim | x | ask | 2026-06-01 | open | |\n"
          "| A-2 | Settled claim | x | ask | 2026-06-01 | confirmed | a test |\n"
          "| A-3 | Future claim | x | ask | 2026-07-01 | open | |\n")
    write(t, "tools/known_red.json", json.dumps([
        {"check": "x_check.py", "fails": "FAIL  thing", "recheck": "2026-06-10",
         "decided_by": "F", "decided_on": "2026-06-01"}]))
    write(t, "docs/EXPERIMENTS.md",
          "| # | Start | Experiment | Status | Read date |\n|---|---|---|---|---|\n"
          "| 1 | 2026-06-01 | Today's read | running | 2026-06-15 |\n"
          "| 2 | 2026-05-01 | Closed one | closed | 2026-06-01 |\n")
    write(t, "docs/work/receipts/status.md",
          "Track: feature\nNow: spec waits for approval\nNext: architect designs the data\nWaiting on: the founder\n\n"
          "## Rulings\n\n- named the field amount_minor\n- rounded half up\n")
    write(t, "docs/work/empty/notes.md", "nothing\n")
    write(t, "docs/requirements/p1-open-questions.md", "# Open questions\n\n- **Pick a price** (raised 2026-06-01).\n")
    write(t, "docs/requirements/AREA.md", "| ID | Requirement | Status |\n|---|---|---|\n"
          "| AR-1 | One. | T |\n| AR-2 | Two. | U |\n| AR-3 | Three. | U |\n")

    due = overdue.due(t, TODAY)
    check([(d["kind"], d["id"], d["overdue"]) for d in due]
          == [("assumption", "A-1", True), ("known red", "x_check.py", True), ("experiment", "1", False)],
          "TPL-80 overdue.due finds the overdue assumption and known red and today's read, and nothing settled, closed or future")

    status_report.ROOT = t
    s = status_report.gather(lambda: {"verdict": "RED", "reds": ["x_check.py   NEW RED  FAIL  thing"]})
    text = status_report.as_text(s)
    check(s["questions"] == ["Pick a price"], "TPL-78 the page lists the open question")
    check(len(s["waiting"]) == 1 and s["rulings"][0]["rulings"] == 2,
          "TPL-78 the page shows the work waiting on the founder and its two rulings")
    check("next: architect designs the data" in text, "TPL-127 the page shows where each work item goes next")
    check("## Waiting on you (4)" in text, "TPL-78 'waiting on you' counts the question, the work and the two rulings")
    check("## Checks: RED" in text and "NEW RED  FAIL  thing" in text,
          "TPL-101 the page shows the sweep verdict and each red line")
    check(s["coverage"] == [("AR", 3, 1)] and "- AR: 1 of 3 built rows guarded by a test, 2 not" in text,
          "TPL-104 the page counts, per area, the built rows a test guards and those nothing guards")
    check("- empty: no status.md yet" in text, "TPL-78 a work folder without status.md says so")
    check(s["rows"]["T"] == 1 and s["rows"]["U"] == 2, "TPL-78 rows are counted by status from the area files")
    page = status_report.as_html(s)
    check('name="viewport"' in page and "Pick a price" in page and "<script" not in page,
          "TPL-78 the html page has a viewport, the content and no script")

    session_start.ROOT = t
    msg = session_start.message("startup", TODAY)
    check("A-1" in msg and "x_check.py" in msg and "due today" in msg and "A-3" not in msg,
          "TPL-80 the session reminder names each due date and no future one")

status_report.ROOT = ROOT
try:
    status_report.as_html(status_report.gather(lambda: {"verdict": "GREEN", "reds": []}))
    check(True, "TPL-78 the report builds from this repository's own files")
except Exception as e:  # a parse error anywhere in the real files must show here
    check(False, f"TPL-78 the report fails on this repository's files: {e!r}")

sys.exit(1 if fails else 0)
