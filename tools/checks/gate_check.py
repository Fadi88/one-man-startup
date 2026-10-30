"""TPL-82: product code does not change while no feature's build pass is open.

The readiness gate (skills/readiness-gate/) has a design pass and a build pass; only the build
pass opens the developers. A sentence asking them to wait is a wish, so this reads the files
that differ from HEAD (in CI, from the base commit, TPL-121) and, if any of them is product code,
passes only when some docs/work/<id>/readiness.md is open: its last pass line is
`Build pass: open`, or `Fix: open <row id>` on the fix track. The release writes
`Build pass: closed` and qa writes `Fix: closed`, so a shipped feature stops opening the gate
(TPL-120). At [gates] level light there is no readiness gate, so the check SKIPs.

Product code is any changed path outside the template's own folders (docs/, agents/, skills/,
tools/, examples/, site/, .claude/, .cursor/, .github/), or a code file at the top level.
Outside a git repository there is no diff to read, so the check SKIPs.

The classifier and the readiness reading run first on built-in samples, so a clean tree still
proves the check works.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lib"))
from diff_base import base

ROOT = Path(__file__).resolve().parents[2]
NOT_PRODUCT = {"docs", "agents", "skills", "tools", "examples", "site", ".claude", ".cursor", ".github"}
PASS_LINE = re.compile(r"^(Build pass|Fix): (open|closed)(?![A-Za-z])", re.M)
CODE_SUFFIX = {".py", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs", ".kt", ".swift", ".java", ".go",
               ".rb", ".php", ".rs", ".cs", ".dart", ".vue", ".svelte", ".html", ".css", ".sql"}
TODO = ("open the build pass (`Build pass: open`, skills/readiness-gate/) or, on the fix track, "
        "`Fix: open <row id>` in docs/work/<id>/readiness.md before product code changes")


def is_product(path: str) -> bool:
    """True for a path that is product code. Pure, so it can be sampled."""
    parts = path.replace("\\", "/").strip("/").split("/")
    if len(parts) == 1:
        return Path(parts[0]).suffix in CODE_SUFFIX
    return parts[0] not in NOT_PRODUCT


def build_open(readiness: str) -> bool:
    """TPL-120: open when the last pass line says open. The release closes the build pass and qa
    the fix line, so a feature that shipped no longer opens the gate for every later change."""
    lines = PASS_LINE.findall(readiness)
    return bool(lines) and lines[-1][1] == "open"


PRODUCT = ["src/app.py", "app/main.ts", "web/index.html", "android/app/build.gradle", "lib/x/y.rb",
           "main.py", "server.js"]
NOT_CODE = ["AGENTS.md", "project.toml", ".gitignore", "LICENSE", "package.json", "docs/work/a/spec.md",
            "tools/checks/gate_check.py", "skills/x/SKILL.md", ".claude/settings.json", ".github/workflows/ci.yml",
            "examples/demo/app.py", "site/index.html", "agents/qa.md", ".cursor/rules/a.mdc"]
OPEN_SAMPLES = ["# Readiness\n\nDesign pass: open 2026-10-01\nBuild pass: open 2026-10-02\n",
                "Build pass: open\n",
                "Fix: open RCPT-4 2026-11-02\n",
                "Build pass: open 2026-10-02\nBuild pass: closed 2026-11-01\nFix: open RCPT-6\n"]
SHUT_SAMPLES = ["Design pass: open\nBuild pass: not yet\n",
                "  Build pass: open\n",
                "The build pass: open when every line holds\n",
                "",
                "Build pass: opened by mistake\n",
                "Build pass: open 2026-10-02\nBuild pass: closed 2026-11-01 (released)\n",
                "Fix: open RCPT-4\nFix: closed RCPT-4 2026-11-03\n"]


def no_gate(cfg: dict) -> bool:
    """TPL-120: the light level has no readiness gate (skills/gates/)."""
    return cfg.get("gates", {}).get("level") == "light"


def selftest() -> list[str]:
    fails = []
    if not no_gate({"gates": {"level": "light"}}) or no_gate({"gates": {"level": "strict"}}) or no_gate({}):
        fails.append("FAIL  TPL-120 self-test: the light level read wrongly")
    # TPL-121: no CHECK_BASE, or the all-zero one GitHub sends for a new branch, reads against
    # HEAD; a real commit reads against it.
    saved = os.environ.pop("CHECK_BASE", None)
    try:
        if base() != "HEAD":
            fails.append("FAIL  TPL-121 self-test: no CHECK_BASE did not read against HEAD")
        os.environ["CHECK_BASE"] = "0" * 40
        if base() != "HEAD":
            fails.append("FAIL  TPL-121 self-test: the all-zero CHECK_BASE did not fall back to HEAD")
        head = git("rev-parse", "HEAD").stdout.strip()
        if head:
            os.environ["CHECK_BASE"] = head
            if base() != head:
                fails.append("FAIL  TPL-121 self-test: CHECK_BASE set to a commit was not used")
    finally:
        os.environ.pop("CHECK_BASE", None)
        if saved is not None:
            os.environ["CHECK_BASE"] = saved
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
    """Paths differing from the base (HEAD, or in CI the base commit, TPL-121), staged, unstaged
    or untracked; None outside a git repository."""
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        return None
    has_head = git("rev-parse", "--verify", "-q", "HEAD").returncode == 0
    diff = git("diff", base(), "--name-only") if has_head else git("diff", "--cached", "--name-only")
    untracked = git("ls-files", "--others", "--exclude-standard")
    return sorted({p for p in (diff.stdout + untracked.stdout).splitlines() if p.strip()})


def main() -> int:
    fails = selftest()
    for f in fails:
        print(f)
    if fails:
        return 1
    if no_gate(tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8"))):
        print("SKIP  TPL-120 [gates] level is light, which has no readiness gate (skills/gates/)")
        return 0
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
