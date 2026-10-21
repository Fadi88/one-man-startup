"""TPL-69: the floor. The diff against HEAD adds no suppression, no empty catch, no skipped or
deleted test, and no secret.

A rule that "the reviewer watches for" is a wish; this makes the four floor rules a check. It
reads only added and removed lines (staged, unstaged and untracked), so it is fast and never
blames old code. A hit is accepted only the way any red is: registered in tools/known_red.json
with the founder's decision (skills/known-reds/).

The rules run first on built-in samples, so a clean tree still proves the check works.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SELF = Path(__file__).resolve()
CODE = {".py", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs", ".kt", ".kts", ".swift", ".java",
        ".go", ".rs", ".rb", ".php", ".cs", ".dart", ".vue", ".svelte"}
TEXT = CODE | {".md", ".toml", ".json", ".yml", ".yaml", ".txt", ".env", ".ini", ".cfg", ".sh",
               ".html", ".css", ".sql", ".mdc", ""}

SUPPRESSIONS = re.compile(r"@ts-ignore|eslint-disable|#\s*noqa|#\s*type:\s*ignore|#\s*pragma:\s*no cover|@SuppressWarnings|@Suppress\(|// nolint|#\[allow\(")
EMPTY_CATCH = re.compile(r"\bcatch\b[^{]*\{\s*\}|\brescue\b\s*(?:=>\s*\w+\s*)?$")
EXCEPT_LINE = re.compile(r"^\s*except\b[^:]*:\s*(?:pass\s*)?(?:#.*)?$")
PASS_LINE = re.compile(r"^\s*pass\s*(?:#.*)?$")
SKIPS = re.compile(r"\b(?:it|test|describe)\.skip\(|\b(?:xit|xtest|xdescribe)\(|@pytest\.mark\.skip|@unittest\.skip|\bpytest\.skip\(|@Ignore\b|@Disabled\b|\bXCTSkip|\bt\.Skip\(")
TEST_DEF = re.compile(r"^\s*(?:async\s+)?def\s+(test_\w+)|^\s*(?:it|test)\(\s*['\"`]([^'\"`]+)|^\s*@Test\b.*\n?\s*(?:fun|void|public)\s+(\w+)|^\s*func\s+(test\w+)\(")
SECRETS = [
    ("live Stripe key", re.compile(r"\bsk_live_[0-9a-zA-Z]{16,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}")),
    ("hard-coded credential", re.compile(r"(?i)\b(?:api[_-]?key|secret|password|passwd|token)\s*[:=]\s*[\"'][^\"'\s]{12,}[\"']")),
]
PLACEHOLDER = re.compile(r"(?i)example|placeholder|your[_-]|<[^>]+>|xxx|dummy|changeme|\$\{|\{\{|os\.environ|process\.env|getenv")


def test_names(lines: list[str]) -> set[str]:
    names: set[str] = set()
    for i, line in enumerate(lines):
        m = TEST_DEF.match(line)
        if m:
            names.add(next(g for g in m.groups() if g))
        elif re.match(r"^\s*@Test\b", line) and i + 1 < len(lines):
            m2 = re.match(r"^\s*(?:public\s+)?(?:fun|void)\s+(\w+)", lines[i + 1])
            if m2:
                names.add(m2.group(1))
    return names


def problems(path: str, added: list[str], removed: list[str]) -> list[str]:
    """The floor rules over one file's added and removed lines. Pure, so it can be sampled."""
    out: list[str] = []
    suffix = Path(path).suffix
    is_code = suffix in CODE
    for i, line in enumerate(added):
        if is_code and SUPPRESSIONS.search(line):
            out.append(f"{path}: new suppression: {line.strip()[:80]}")
        if is_code and EMPTY_CATCH.search(line):
            out.append(f"{path}: empty catch: {line.strip()[:80]}")
        if suffix == ".py" and EXCEPT_LINE.match(line):
            nxt = added[i + 1] if i + 1 < len(added) else ""
            if line.rstrip().endswith("pass") or PASS_LINE.match(nxt):
                out.append(f"{path}: except that swallows: {line.strip()[:80]}")
        if is_code and SKIPS.search(line):
            out.append(f"{path}: skipped test: {line.strip()[:80]}")
        for label, rx in SECRETS:
            if rx.search(line) and not PLACEHOLDER.search(line):
                out.append(f"{path}: looks like a {label} (value not shown)")
                break
    if is_code:
        for name in sorted(test_names(removed) - test_names(added)):
            out.append(f"{path}: deleted test {name}")
    return out


SAMPLES = [
    ("a.ts", ["// @ts-ignore", "x()"], [], "new suppression"),
    ("a.py", ["import os  # noqa: F401"], [], "new suppression"),
    ("a.js", ["try { f() } catch (e) {}"], [], "empty catch"),
    ("a.py", ["try:", "    f()", "except Exception:", "    pass"], [], "except that swallows"),
    ("a.test.ts", ["it.skip('adds', () => {})"], [], "skipped test"),
    ("test_a.py", ["def test_other():"], ["def test_adds():"], "deleted test test_adds"),
    ("cfg.py", ["STRIPE = 'sk_live_" + "4eC39HqLyjWDarjtT1zdp7dc'"], [], "live Stripe key"),
    ("cfg.py", ["password = 'correct-horse-battery-staple'"], [], "hard-coded credential"),
]
CLEAN = [
    ("a.ts", ["// @ts-expect-error: upstream types lag the runtime"], []),
    ("test_a.py", ["def test_adds_renamed():", "def test_adds():"], ["def test_adds():"]),
    ("cfg.py", ["STRIPE = os.environ['STRIPE_KEY']", "password = '<your password here>'"], []),
    ("a.py", ["except ValueError:", "    raise"], []),
    ("notes.md", ["eslint-disable is banned; see the floor"], []),
]


def selftest() -> list[str]:
    fails = []
    for path, added, removed, expect in SAMPLES:
        got = problems(path, added, removed)
        if not any(expect in g for g in got):
            fails.append(f"FAIL  self-test: {expect!r} not caught in {added!r}")
    for path, added, removed in CLEAN:
        if problems(path, added, removed):
            fails.append(f"FAIL  self-test: false alarm on {added!r}: {problems(path, added, removed)}")
    return fails


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                          errors="replace").stdout


def changed() -> dict[str, tuple[list[str], list[str]]]:
    """Added and removed lines per file: the diff against HEAD plus every untracked file."""
    files: dict[str, tuple[list[str], list[str]]] = {}
    cur = None
    for line in git("diff", "HEAD", "-U0", "--no-color", "--").splitlines():
        if line.startswith("+++ b/"):
            cur = line[6:]
            files.setdefault(cur, ([], []))
        elif line.startswith("+++ /dev/null"):
            cur = None
        elif cur and line.startswith("+") and not line.startswith("+++"):
            files[cur][0].append(line[1:])
        elif cur and line.startswith("-") and not line.startswith("---"):
            files[cur][1].append(line[1:])
    for f in git("ls-files", "--others", "--exclude-standard").splitlines():
        p = ROOT / f
        if p.is_file() and p.suffix in TEXT:
            try:
                files.setdefault(f, ([], []))[0].extend(p.read_text(encoding="utf-8").splitlines())
            except UnicodeDecodeError:
                pass
    return {f: v for f, v in files.items() if Path(f).suffix in TEXT and (ROOT / f).resolve() != SELF}


def main() -> int:
    fails = selftest()
    seen = 0
    if not fails:
        for path, (added, removed) in changed().items():
            seen += 1
            fails.extend(f"FAIL  {p}" for p in problems(path, added, removed))
    for f in fails:
        print(f)
    if not fails:
        print(f"PASS  floor holds: {len(SAMPLES)} samples caught, {len(CLEAN)} clean ones passed, {seen} changed files read")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
