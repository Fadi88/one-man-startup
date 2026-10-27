"""TPL-77: bring the template's later fixes into a project made from it, file by file, only
the ones the founder says yes to.

A project made with "Use this template" has none of the template's history, so the starting
point is kept as a fingerprint instead: tools/template_base.json holds, for every
template-owned file (AGENTS.md, agents/, skills/, tools/), the hash it had when setup ran
(tools/clean_template.py writes it). Each file then falls in one of these groups:

    new in the template       the template added it, the project has no such file
    changed in the template   the template changed it, the project never did: safe to take
    changed in both           the project changed it too: taking it overwrites that change
    removed in the template   the template deleted it, the project never changed it

    python tools/template_update.py                      list what changed, change nothing
    python tools/template_update.py --apply PATH ...     take those files (or deletions)
    python tools/template_update.py --decline PATH ...   say no; they are not offered again
    python tools/template_update.py --init               record today's files as the start,
                                                         for a project made before this tool
    --from URL_OR_FOLDER                                 the template (default: TEMPLATE_URL)

It never touches a file outside the template-owned set, refuses a file with uncommitted
changes, and every file it writes is tracked by git, so `git checkout -- PATH` undoes it.
Afterwards: python tools/sync_adapters.py, then python tools/run_all.py.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_URL = "https://github.com/Fadi88/one-man-startup"
BASE = "tools/template_base.json"
OWNED = ["AGENTS.md", "agents", "skills", "tools"]
# Inside tools/ but the project's own, or gone after setup.
NOT_OWNED = {BASE, "tools/known_red.json", "tools/clean_template.py", "tools/checks/clean_check.py"}


def digest(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def owned(root: Path) -> dict[str, str]:
    """Every template-owned file under root, as {posix path: hash}."""
    out = {}
    for top in OWNED:
        p = root / top
        files = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else []
        for f in files:
            rel = f.relative_to(root).as_posix()
            if "__pycache__" not in rel and rel not in NOT_OWNED:
                out[rel] = digest(f)
    return out


def changes(base: dict[str, str], project: dict[str, str], template: dict[str, str]) -> list[tuple[str, str]]:
    out = []
    for rel in sorted(set(base) | set(template)):
        b, p, t = base.get(rel), project.get(rel), template.get(rel)
        if t == p or t == b:
            continue  # already the same, or only the project changed it
        if t is None:
            out.append((rel, "removed in the template"))
        elif b is None and p is None:
            out.append((rel, "new in the template"))
        elif p == b:
            out.append((rel, "changed in the template"))
        else:
            out.append((rel, "changed in both"))
    return out


def fetch(source: str) -> tuple[Path, tempfile.TemporaryDirectory | None]:
    if Path(source).is_dir():
        return Path(source), None
    tmp = tempfile.TemporaryDirectory()
    subprocess.run(["git", "clone", "--quiet", "--depth", "1", source, tmp.name], check=True)
    return Path(tmp.name), tmp


def uncommitted(root: Path, paths: list[str]) -> list[str]:
    r = subprocess.run(["git", "status", "--porcelain", "--", *paths], cwd=root, capture_output=True, text=True)
    return [l[3:] for l in r.stdout.splitlines()] if r.returncode == 0 else []


def run(argv: list[str], root: Path = ROOT) -> int:
    base_file = root / BASE
    source = argv[argv.index("--from") + 1] if "--from" in argv else TEMPLATE_URL
    named = [a for a in argv if not a.startswith("--") and a != source]

    if "--init" in argv:
        if base_file.exists():
            print(f"{BASE} already exists; nothing recorded.")
            return 1
        base_file.write_text(json.dumps({"files": owned(root)}, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Recorded {BASE}. A change the project made before today now counts as the template's.")
        return 0
    if not base_file.exists():
        print(f"No {BASE}: this is the template itself, or a project made before this tool. "
              "In a project, run with --init once.")
        return 1

    base = json.loads(base_file.read_text(encoding="utf-8"))
    template_root, tmp = fetch(source)
    try:
        template = owned(template_root)
        found = dict(changes(base["files"], owned(root), template))
        if "--apply" not in argv and "--decline" not in argv:
            for rel, what in found.items():
                print(f"{what:26}  {rel}")
            print(f"\n{len(found)} template files differ; nothing changed. "
                  "Take some with --apply PATH ..., say no with --decline PATH ...")
            return 0
        unknown = [n for n in named if n not in found]
        if unknown or not named:
            print("Refused: name files from the list. Not on it: " + (", ".join(unknown) or "none named"))
            return 1
        dirty = uncommitted(root, named)
        if dirty:
            print("Refused: these have uncommitted changes, commit or set them aside first: " + ", ".join(dirty))
            return 1
        for rel in named:
            if "--apply" in argv:
                target = root / rel
                if found[rel] == "removed in the template":
                    target.unlink(missing_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(template_root / rel, target)
                print(f"took      {rel}")
            else:
                print(f"declined  {rel}")
            if rel in template:
                base["files"][rel] = template[rel]
            else:
                base["files"].pop(rel, None)
        base_file.write_text(json.dumps(base, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("\nNow run: python tools/sync_adapters.py, then python tools/run_all.py")
        return 0
    finally:
        if tmp:
            tmp.cleanup()


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
