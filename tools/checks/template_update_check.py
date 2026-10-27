"""TPL-77: template_update.py sorts each template file into the right group, takes only what it
is told to, and never touches a project file.

Builds a template folder and a project folder in a temporary directory, with one file in each
group (unchanged, changed in the template, changed in both, changed only in the project, new in
the template, removed in the template) and one project-only file, then runs the tool on them.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import template_update as tu

fails = 0


def check(ok: bool, what: str) -> None:
    global fails
    print(f"{'PASS' if ok else 'FAIL'}  {what}")
    fails += not ok


def put(root: Path, files: dict[str, str]) -> None:
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8", newline="")


def quiet(argv: list[str], root: Path) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = tu.run(argv, root)
    return code, out.getvalue()


START = {"AGENTS.md": "rules\n", "agents/qa.md": "qa\n", "skills/a/SKILL.md": "a\n",
         "tools/x.py": "x\n", "tools/gone.py": "gone\n", "tools/mine.py": "mine\n"}

with tempfile.TemporaryDirectory() as tmp:
    t, p = Path(tmp) / "template", Path(tmp) / "project"
    put(p, START)
    code, _ = quiet(["--init"], p)
    check(code == 0 and (p / tu.BASE).exists(), "TPL-77 --init records the starting fingerprint")
    put(p, {"skills/a/SKILL.md": "a, the project's edit\n", "tools/mine.py": "mine, edited\n",
            "docs/requirements/AREA.md": "project rows\n", "agents/qa.md": "qa\r\n"})
    put(t, {**START, "agents/qa.md": "qa v2\n", "skills/a/SKILL.md": "a v2\n",
            "tools/new.py": "new\n", "docs/requirements/AREA.md": "template rows\n"})
    (t / "tools/gone.py").unlink()

    found = dict(tu.changes(json.loads((p / tu.BASE).read_text())["files"], tu.owned(p), tu.owned(t)))
    check(found == {"agents/qa.md": "changed in the template", "skills/a/SKILL.md": "changed in both",
                    "tools/new.py": "new in the template", "tools/gone.py": "removed in the template"},
          "TPL-77 each file lands in its group; unchanged, project-only and non-template files are not listed")

    code, _ = quiet(["--from", str(t), "--apply", "docs/requirements/AREA.md"], p)
    check(code == 1 and (p / "docs/requirements/AREA.md").read_text() == "project rows\n",
          "TPL-77 a file not on the list is refused and left alone")
    code, _ = quiet(["--from", str(t), "--apply", "agents/qa.md", "tools/new.py", "tools/gone.py"], p)
    check(code == 0 and (p / "agents/qa.md").read_text() == "qa v2\n" and (p / "tools/new.py").exists()
          and not (p / "tools/gone.py").exists(), "TPL-77 --apply takes the named changes and deletions")
    check((p / "skills/a/SKILL.md").read_text() == "a, the project's edit\n",
          "TPL-77 a file not named is not touched")
    code, out = quiet(["--from", str(t)], p)
    check(code == 0 and "skills/a/SKILL.md" in out and "agents/qa.md" not in out,
          "TPL-77 after taking some, only the rest are offered")
    quiet(["--from", str(t), "--decline", "skills/a/SKILL.md"], p)
    code, out = quiet(["--from", str(t)], p)
    check("0 template files differ" in out and (p / "skills/a/SKILL.md").read_text() == "a, the project's edit\n",
          "TPL-77 a declined file keeps the project's version and is not offered again")

check(tu.TEMPLATE_URL.startswith("https://github.com/"), "TPL-77 the default source is the template's public repository")
sys.exit(1 if fails else 0)
