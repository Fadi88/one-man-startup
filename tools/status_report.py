"""TPL-78: the founder's status page, built from the files alone.

    python tools/status_report.py                 print it
    python tools/status_report.py --html [PATH]   also write it as a page (default: status.html
                                                  in the system temp folder) and print the path

What it reads, and nothing else: the open questions (docs/requirements/p1-open-questions.md),
each docs/work/<id>/status.md (its Track:, Now: and Waiting on: lines and its rulings,
skills/handoff/), the dates that have come due (tools/lib/overdue.py), the known reds
(tools/known_red.json), the requirement rows by status and the newest entries of
docs/HISTORY.md. Every figure is counted here when it runs; nothing on the page is typed.
"""
from __future__ import annotations

import html
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
import overdue

ROW = re.compile(r"^\| ([A-Z][A-Z0-9]*-\d+[a-z]?) \| (.+) \| ([A-Za-z/]+) \|$")
STATUSES = {"T": "a test guards it", "M": "seen working", "U": "built, never run",
            "X": "decided, not built", "n/a": "not to be built"}

# The template's visual style (docs/images/STYLE.md); tools/checks/contrast_check.py keeps
# these values equal to that file's, so the page cannot drift from the README and the site.
CSS = """
:root {
  --page: #ffffff; --surface: #f7f5fa; --line: #e4e0eb;
  --ink: #14121f; --soft: #55505f;
  --brand: #d6246e; --brand-ink: #b0124f; --brand-hover: #b0124f; --tint: #fdebf3; --on-brand: #ffffff;
  --ok: #1b7a4b;
  --font: -apple-system, "Segoe UI Variable", "Segoe UI", system-ui, Roboto, "Helvetica Neue", Arial, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --r-s: 10px; --r-m: 20px; --r-l: 28px; --r-pill: 999px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --page: #0f0d14; --surface: #1a1722; --line: #2c2837;
    --ink: #f4f2f8; --soft: #b5afc2;
    --brand-ink: #ff6fa6; --tint: #2a1420; --ok: #5fd3a0;
  }
}
"""

PAGE_CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--ink); font: 17px/1.65 var(--font); }
main { max-width: 860px; margin: 0 auto; padding: 40px 16px 64px; }
h1 { font-size: 2.6rem; font-weight: 800; letter-spacing: -1px; line-height: 1.1; margin: 0 0 8px; }
.sub { color: var(--soft); margin: 0 0 32px; }
section { background: var(--surface); border-radius: var(--r-m);
  padding: 20px 24px; margin: 0 0 20px; }
h2 { font-size: 1.15rem; font-weight: 800; margin: 0 0 12px; display: flex; align-items: center; gap: 10px; }
.count { background: var(--tint); color: var(--brand-ink); border-radius: var(--r-pill);
  padding: 1px 10px; font-size: 0.85rem; font-weight: 800; }
.count.warn { background: var(--brand); color: var(--on-brand); }
ul { margin: 0; padding-left: 20px; }
li { margin: 4px 0; }
.empty { color: var(--soft); margin: 0; }
code { font: 0.9em var(--mono); }
table { border-collapse: collapse; width: 100%; }
td { padding: 6px 0; border-top: 1px solid var(--line); }
td.n { text-align: right; font-weight: 600; width: 4em; }
"""


def read(rel: str) -> str:
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def open_questions() -> list[str]:
    text = read("docs/requirements/p1-open-questions.md")
    return re.findall(r"^- \*\*(.+?)\*\*", text, flags=re.M)


def work() -> list[dict]:
    out = []
    base = ROOT / "docs" / "work"
    for d in sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []:
        text = (d / "status.md").read_text(encoding="utf-8") if (d / "status.md").exists() else ""
        field = {k: (m[1].strip() if (m := re.search(rf"^{k}:\s*(.*)$", text, flags=re.M)) else "")
                 for k in ("Track", "Now", "Waiting on")}
        rulings = re.search(r"^## Rulings\s*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
        field["rulings"] = len(re.findall(r"^- ", rulings[1], flags=re.M)) if rulings else 0
        field["id"] = d.name
        field["has_status"] = bool(text)
        out.append(field)
    return out


def rows_by_status() -> dict[str, int]:
    counts = {s: 0 for s in STATUSES}
    for f in (ROOT / "docs" / "requirements").glob("*.md"):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if m and m[3] in counts:
                counts[m[3]] += 1
    return counts


def history(n: int = 5) -> list[tuple[str, str]]:
    out = []
    for date, text in re.findall(r"^- \*\*(\d{4}-\d{2}-\d{2})\.\*\* (.+?)(?=^- |^#|\Z)", read("docs/HISTORY.md"),
                                 flags=re.M | re.S)[:n]:
        text = " ".join(text.split())
        out.append((date, text if len(text) <= 140 else text[:137].rsplit(" ", 1)[0] + "..."))
    return out


def gather() -> dict:
    known = json.loads(read("tools/known_red.json") or "[]")
    w = work()
    return {
        "questions": open_questions(),
        "waiting": [x for x in w if x["Waiting on"].lower().startswith(("the founder", "founder"))],
        "rulings": [x for x in w if x["rulings"]],
        "due": overdue.due(ROOT),
        "work": w,
        "known": known,
        "rows": rows_by_status(),
        "history": history(),
    }


def as_text(s: dict) -> str:
    out = ["# Status", ""]
    waiting = len(s["questions"]) + len(s["waiting"]) + sum(x["rulings"] for x in s["rulings"])
    out.append(f"## Waiting on you ({waiting})")
    out += [f"- Question: {q}" for q in s["questions"]]
    out += [f"- {x['id']}: {x['Now'] or 'waiting on you'}" for x in s["waiting"]]
    out += [f"- {x['id']}: {x['rulings']} ruling(s) to look over in docs/work/{x['id']}/status.md" for x in s["rulings"]]
    if not waiting:
        out.append("- Nothing.")
    out += ["", f"## Dates that have come due ({len(s['due'])})"]
    out += [f"- {overdue.line(d)}" for d in s["due"]] or ["- None."]
    out += ["", f"## Work in progress ({len(s['work'])})"]
    for x in s["work"]:
        if not x["has_status"]:
            out.append(f"- {x['id']}: no status.md yet")
        else:
            out.append(f"- {x['id']}: {x['Track'] or 'track not set'}; now: {x['Now'] or 'not set'}; "
                       f"waiting on: {x['Waiting on'] or 'nothing'}")
    if not s["work"]:
        out.append("- None.")
    out += ["", f"## Failing checks you accepted ({len(s['known'])})"]
    out += [f"- {k['check']}: {k['fails']} (recheck {k.get('recheck', 'not set')})" for k in s["known"]] or ["- None."]
    out += ["", f"## Requirement rows ({sum(s['rows'].values())})"]
    out += [f"- {s['rows'][k]} {k}: {v}" for k, v in STATUSES.items()]
    out += ["", "## Recently changed"]
    out += [f"- {d}: {t}" for d, t in s["history"]] or ["- Nothing recorded."]
    return "\n".join(out) + "\n"


def as_html(s: dict) -> str:
    e = html.escape

    def block(title: str, items: list[str], n: int | None = None, warn: bool = False) -> str:
        badge = f'<span class="count{" warn" if warn and n else ""}">{n}</span>' if n is not None else ""
        body = "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>" if items else '<p class="empty">Nothing here.</p>'
        return f"<section><h2>{e(title)} {badge}</h2>{body}</section>"

    wait = ([f"Question: {e(q)}" for q in s["questions"]]
            + [f"<code>{e(x['id'])}</code>: {e(x['Now'] or 'waiting on you')}" for x in s["waiting"]]
            + [f"<code>{e(x['id'])}</code>: {x['rulings']} ruling(s) to look over" for x in s["rulings"]])
    work_items = [f"<code>{e(x['id'])}</code>: " + (e(f"{x['Track'] or 'track not set'}; now: {x['Now'] or 'not set'}; "
                  f"waiting on: {x['Waiting on'] or 'nothing'}") if x["has_status"] else "no status.md yet")
                  for x in s["work"]]
    rows = "".join(f'<tr><td>{e(v)} <code>{e(k)}</code></td><td class="n">{s["rows"][k]}</td></tr>'
                   for k, v in STATUSES.items())
    parts = [
        block("Waiting on you", wait, len(wait), warn=True),
        block("Dates that have come due", [e(overdue.line(d)) for d in s["due"]], len(s["due"]), warn=True),
        block("Work in progress", work_items, len(s["work"])),
        block("Failing checks you accepted", [e(f"{k['check']}: {k['fails']}") for k in s["known"]], len(s["known"])),
        f"<section><h2>Requirement rows <span class=\"count\">{sum(s['rows'].values())}</span></h2><table>{rows}</table></section>",
        block("Recently changed", [f"<strong>{e(d)}</strong> {e(t)}" for d, t in s["history"]]),
    ]
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>Project status</title><style>{CSS}{PAGE_CSS}</style></head><body><main>"
            "<h1>Project status</h1><p class=\"sub\">Built from the project's files by "
            "<code>tools/status_report.py</code>. Run it again for the latest.</p>"
            + "".join(parts) + "</main></body></html>\n")


def main(argv: list[str]) -> int:
    s = gather()
    sys.stdout.write(as_text(s))
    if "--html" in argv:
        i = argv.index("--html")
        path = Path(argv[i + 1]) if len(argv) > i + 1 else Path(tempfile.gettempdir()) / "status.html"
        path.write_text(as_html(s), encoding="utf-8")
        print(f"\nWrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
