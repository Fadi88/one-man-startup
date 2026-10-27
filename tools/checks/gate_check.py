"""TPL-82: product code does not change while no feature's build pass is open.

The readiness gate (skills/readiness-gate/) has a design pass and a build pass; only the build
pass opens the developers. A sentence asking them to wait is a wish, so this reads the files
that differ from HEAD (staged, unstaged and untracked) and, if any of them is product code,
passes only when some docs/work/<id>/readiness.md has a line starting `Build pass: open`.

Product code is any changed path outside the template's own folders (docs/, agents/, skills/,
tools/, examples/, site/, .claude/, .cursor/, .github/) that is not a file at the top level.
Outside a git repository there is no diff to read, so the check SKIPs.

The classifier and the readiness reading run first on built-in samples, so a clean tree still
proves the check works.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOT_PRODUCT = {"docs", "agents", "skills", "tools", "examples", "site", ".claude", ".cursor", ".github"}
OPEN = re.compile(r"^Build pass: open", re.M)
TODO = ("the build pass in skills/readiness-gate/ must be open in docs/work/<id>/readiness.md "
        "before product code changes")


def is_product(path: str) -> bool:
    """True for a path that is product code. Pure, so it can be sampled."""
    parts = path.replace("\\", "/").strip("/").split("/")
    return len(parts) > 1 and parts[0] not in NOT_PRODUCT


def build_open(readiness: str) -> bool:
    return bool(OPEN.search(readiness))


PRODUCT = ["src/app.py", "app/main.ts", "web/index.html", "android/app/build.gradle", "lib/x/y.rb"]
NOT_CODE = ["AGENTS.md", "project.toml", ".gitignore", "LICENSE", "package.json", "docs/work/a/spec.md",
            "tools/checks/gate_check.py", "skills/x/SKILL.md", ".claude/settings.json", ".github/workflows/ci.yml",
            "examples/demo/app.py", "site/index.html", "agents/qa.md", ".cursor/rules/a.mdc"]
OPEN_SAMPLES = ["# Readiness\n\nDesign pass: open 2026-10-01\nBuild pass: open 2026-10-02\n",
                "Build pass: open\n"]
SHUT_SAMPLES = ["Design pass: open\nBuild pass: not yet\n", "  Build pass: open\n",
                "The build pass: open when every line holds\n", ""]


def selftest() -> list[str]:
    fails = []
    for p in PRODUCT:
        if not is_product(p):
            fails.append(f"FAIL  TPL-82 self-test: {p} not seen as product code")
    for p in NOT_CODE:
        if is_product(p):
            fails.append(f"FAIL  TPL-82 self-test: {p} wrongly seen as product code")
    for t in OPEN_SAMPLES:
        if not build_open(t):
            fails.append(f"FAIL  TPL-82 self-test: open build pass not read in {t!r}")
    for t in SHUT_SAMPLES:
        if build_open(t):
            fails.append(f"FAIL  TPL-82 self-test: build pass wrongly read as open in {t!r}")
    return fails


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def changed() -> list[str] | None:
    """Paths differing from HEAD, staged, unstaged or untracked; None outside a git repository."""
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        return None
    has_head = git("rev-parse", "--verify", "-q", "HEAD").returncode == 0
    diff = git("diff", "HEAD", "--name-only") if has_head else git("diff", "--cached", "--name-only")
    untracked = git("ls-files", "--others", "--exclude-standard")
    return sorted({p for p in (diff.stdout + untracked.stdout).splitlines() if p.strip()})


def main() -> int:
    fails = selftest()
    for f in fails:
        print(f)
    if fails:
        return 1
    paths = changed()
    if paths is None:
        print("SKIP  TPL-82 not a git repository, no diff to read")
        return 0
    product = [p for p in paths if is_product(p)]
    if not product:
        print(f"PASS  TPL-82 no product code changed ({len(paths)} changed files, "
              f"{len(PRODUCT) + len(NOT_CODE)} paths and {len(OPEN_SAMPLES) + len(SHUT_SAMPLES)} readiness samples self-tested)")
        return 0
    opened = [r.parent.name for r in sorted((ROOT / "docs" / "work").glob("*/readiness.md"))
              if build_open(r.read_text(encoding="utf-8"))]
    if opened:
        print(f"PASS  TPL-82 {len(product)} product files changed with the build pass open for {', '.join(opened)}")
        return 0
    shown = ", ".join(product[:5]) + (f" and {len(product) - 5} more" if len(product) > 5 else "")
    print(f"FAIL  TPL-82 product code changed ({shown}) but no build pass is open: {TODO}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
