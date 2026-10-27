"""The commit-msg rules, enforced rather than asked for.

Style bans from project.toml [style] (by default em and en dashes), and the subject's
requirement ids (TPL-75): the subject opens with the ids it satisfies, a colon, then what changed,
and every id is a row in docs/requirements/. Merge, revert, fixup and squash subjects pass.

Exit 0 to accept, 1 to refuse with the reason on stderr.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROW = re.compile(r"^\| ([A-Z][A-Z0-9]*-\d+[a-z]?) \|", re.M)
ID = re.compile(r"\b([A-Z][A-Z0-9]*-\d+[a-z]?)\b")
GIT_MADE = ("Merge ", "Revert ", "fixup! ", "squash! ", "amend! ")


def config() -> dict:
    path = ROOT / "project.toml"
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def row_ids() -> set[str]:
    found = set()
    for path in (ROOT / "docs" / "requirements").glob("*.md"):
        found.update(ROW.findall(path.read_text(encoding="utf-8")))
    return found


def problems(message: str, cfg: dict, rows: set[str] | None = None) -> list[str]:
    out = []
    lines = [l for l in message.splitlines() if not l.startswith("#")]
    body = "\n".join(lines)
    style = cfg.get("style", {})
    for ch in style.get("banned_chars", ["\u2014", "\u2013"]):
        if ch in body:
            out.append(f"a banned character U+{ord(ch):04X} (project.toml [style] banned_chars)")
    subject = next((l.strip() for l in lines if l.strip()), "")
    if subject and not subject.startswith(GIT_MADE):
        ids = ID.findall(subject.split(":", 1)[0]) if ":" in subject else []
        if not ids:
            out.append("no requirement id: the subject opens with the ids it satisfies and a colon, "
                       "e.g. 'AUTH-12, AUTH-13: email login' (skills/commit/)")
        else:
            rows = row_ids() if rows is None else rows
            missing = sorted(set(ids) - rows)
            if missing:
                out.append(f"ids that are not rows in docs/requirements/: {', '.join(missing)}")
    return out


def main(argv: list[str]) -> int:
    message = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    found = problems(message, config())
    if found:
        print("commit-msg: refused, the message carries:", file=sys.stderr)
        for p in found:
            print(f"  - {p}", file=sys.stderr)
        print("Remove them. Never bypass this hook with --no-verify.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
