"""Minimal frontmatter reader, no dependencies.

Supports the subset the template uses: `key: value`, quoted strings, and
inline lists `[a, b, c]`. Anything richer is refused loudly rather than
half-parsed, because a parser that guesses looks exactly like one that works.
"""
from __future__ import annotations

from pathlib import Path


class FrontmatterError(ValueError):
    pass


def _scalar(raw: str):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [] if not inner else [_scalar(p) for p in inner.split(",")]
    if raw in ("true", "false"):
        return raw == "true"
    return raw


def parse(text: str, source: str = "<text>") -> tuple[dict, str]:
    """Return (fields, body). Raises FrontmatterError on anything unexpected."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError(f"{source}: no frontmatter, the first line must be ---")
    fields: dict = {}
    for i, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            return fields, "\n".join(lines[i:]).lstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            raise FrontmatterError(f"{source}:{i}: unsupported frontmatter line: {line!r}")
        key, _, value = line.partition(":")
        key = key.strip()
        if key in fields:
            raise FrontmatterError(f"{source}:{i}: duplicate key {key!r}")
        fields[key] = _scalar(value)
    raise FrontmatterError(f"{source}: frontmatter never closed with ---")


def read(path: Path) -> tuple[dict, str]:
    return parse(path.read_text(encoding="utf-8"), str(path))
