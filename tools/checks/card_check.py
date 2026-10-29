"""TPL-114: every question waiting on the founder is a decision card they can answer by copying.

Each `- **<question>**` entry in docs/requirements/p1-open-questions.md must carry, as indented
`  - <field>:` lines, a Recommendation, Could go wrong, Undo and Blocks, and exactly two
`Reply:` lines, each one reply in backticks, the two different.

The reader runs first on built-in samples, so the check proves itself even with no open
questions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "docs" / "requirements" / "p1-open-questions.md"
ENTRY = re.compile(r"^- \*\*(.+?)\*\*(.*?)(?=^- \*\*|\Z)", re.M | re.S)
FIELD = re.compile(r"^  - ([A-Za-z ]+): (.*)$", re.M)
NEEDED = ("Recommendation", "Could go wrong", "Undo", "Blocks")
REPLY = re.compile(r"^`[^`]+`$")


def problems(text: str) -> list[str]:
    """Every way the entries break the card, as sentences. Pure, so it can be sampled."""
    out = []
    for title, body in ENTRY.findall(text):
        fields = FIELD.findall(body)
        names = [n for n, _ in fields]
        for need in NEEDED:
            if need not in names:
                out.append(f"'{title}': no '{need}:' line")
        replies = [v.strip() for n, v in fields if n == "Reply"]
        if len(replies) != 2:
            out.append(f"'{title}': {len(replies)} 'Reply:' lines, the card needs two")
        for r in replies:
            if not REPLY.match(r):
                out.append(f"'{title}': reply {r!r} is not one reply in backticks")
        if len(replies) == 2 and replies[0] == replies[1]:
            out.append(f"'{title}': both replies say the same")
    return out


CARD = ("  - Recommendation: yes.\n  - Could go wrong: x.\n  - Undo: y.\n  - Blocks: nothing.\n"
        "  - Reply: `yes`\n  - Reply: `not now`\n")
GOOD = [
    "# Open questions\n\nNothing waiting.\n",
    "# Open questions\n\n- **Pick a price** (raised 2026-06-01). Context.\n" + CARD,
    "- **A** (raised 2026-06-01).\n" + CARD + "- **B** (raised 2026-06-02).\n" + CARD,
]
BAD = [
    # an entry with no card at all
    "- **Pick a price** (raised 2026-06-01).\n",
    # no undo line
    "- **A** (raised 2026-06-01).\n" + CARD.replace("  - Undo: y.\n", ""),
    # one reply only
    "- **A** (raised 2026-06-01).\n" + CARD.replace("  - Reply: `not now`\n", ""),
    # a reply that is not copyable as it is
    "- **A** (raised 2026-06-01).\n" + CARD.replace("`not now`", "not now, or later"),
    # the same reply twice
    "- **A** (raised 2026-06-01).\n" + CARD.replace("`not now`", "`yes`"),
    # the second entry breaks while the first is fine
    "- **A** (raised 2026-06-01).\n" + CARD + "- **B** (raised 2026-06-02).\n  - Blocks: x.\n",
]


def main() -> int:
    fails = []
    for t in GOOD:
        if problems(t):
            fails.append(f"FAIL  TPL-114 self-test: good sample refused: {problems(t)}")
    for t in BAD:
        if not problems(t):
            fails.append(f"FAIL  TPL-114 self-test: bad sample let through: {t[:60]!r}")
    text = FILE.read_text(encoding="utf-8") if FILE.exists() else ""
    for p in problems(text):
        fails.append(f"FAIL  TPL-114 docs/requirements/p1-open-questions.md: {p}")
    for line in fails:
        print(line)
    if not fails:
        print(f"PASS  TPL-114 read {len(ENTRY.findall(text))} open questions and "
              f"{len(GOOD) + len(BAD)} samples; every question is a card with two replies")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
