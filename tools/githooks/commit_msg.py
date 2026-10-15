"""The commit-msg rules, enforced rather than asked for.

Style bans from project.toml [style] (by default em and en dashes).

Exit 0 to accept, 1 to refuse with the reason on stderr.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def config() -> dict:
    path = ROOT / "project.toml"
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def problems(message: str, cfg: dict) -> list[str]:
    out = []
    body = "\n".join(l for l in message.splitlines() if not l.startswith("#"))
    style = cfg.get("style", {})
    for ch in style.get("banned_chars", ["\u2014", "\u2013"]):
        if ch in body:
            out.append(f"a banned character U+{ord(ch):04X} (project.toml [style] banned_chars)")
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
