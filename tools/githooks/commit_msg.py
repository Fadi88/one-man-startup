"""The commit-msg rules, enforced rather than asked for.

1. The author is the founder named in project.toml [owner]. Agents work for
   the founder; the history carries one name.
2. No attribution trailers or bylines for tools or models: Co-authored-by,
   "Generated with", session links.
3. Style bans from project.toml [style] (by default em and en dashes).

Exit 0 to accept, 1 to refuse with the reason on stderr.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ATTRIBUTION = re.compile(
    r"^\s*(co-authored-by:|generated (with|by)\b|session:|https?://\S*(claude\.ai|chatgpt\.com|gemini\.google)\S*)",
    re.IGNORECASE | re.MULTILINE,
)
BOT_NAMES = re.compile(r"\b(claude|chatgpt|gpt-\d|codex|gemini|copilot|cursor)\b", re.IGNORECASE)


def config() -> dict:
    path = ROOT / "project.toml"
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def problems(message: str, cfg: dict, author: str | None) -> list[str]:
    out = []
    body = "\n".join(l for l in message.splitlines() if not l.startswith("#"))
    if ATTRIBUTION.search(body):
        out.append("an attribution trailer or byline (Co-authored-by, Generated with, a session link)")
    for line in body.splitlines():
        if line.lower().startswith(("co-authored", "signed-off-by")) and BOT_NAMES.search(line):
            out.append(f"a tool or model credited: {line.strip()}")
    style = cfg.get("style", {})
    for ch in style.get("banned_chars", ["\u2014", "\u2013"]):
        if ch in body:
            out.append(f"a banned character U+{ord(ch):04X} (project.toml [style] banned_chars)")
    owner = cfg.get("owner", {})
    want = owner.get("email")
    if want and want != "unset" and author and want.lower() not in author.lower():
        out.append(f"author {author!r} is not the founder {owner.get('name')} <{want}>")
    return out


def current_author() -> str | None:
    env = os.environ.get("GIT_AUTHOR_EMAIL")
    if env:
        return env
    r = subprocess.run(["git", "var", "GIT_AUTHOR_IDENT"], capture_output=True, text=True, cwd=ROOT)
    return r.stdout.strip() or None


def main(argv: list[str]) -> int:
    message = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    found = problems(message, config(), current_author())
    if found:
        print("commit-msg: refused, the message carries:", file=sys.stderr)
        for p in found:
            print(f"  - {p}", file=sys.stderr)
        print("Remove those lines. Never bypass this hook with --no-verify.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
