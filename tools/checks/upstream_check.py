"""TPL-17: text copied verbatim from upstream stays verbatim.

skills/karpathy-guidelines/SKILL.md carries forrestchang/andrej-karpathy-skills
CLAUDE.md unchanged from the line "# CLAUDE.md" on. The hash below was taken of
the upstream file fetched 2026-10-14. To take a newer upstream version, replace
the text and the hash in the same change, with the fetch date in the skill's note.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PINNED = {
    "skills/karpathy-guidelines/SKILL.md": (
        "# CLAUDE.md",
        "694a2d721e41c385f3db492838c23299826df5ba9809e3b0721aac70021e196a",
    ),
}

fails = 0
for rel, (marker, want) in PINNED.items():
    text = (ROOT / rel).read_bytes().decode("utf-8")
    at = text.find(marker + "\n")
    if at < 0:
        print(f"FAIL  TPL-17 {rel} has lost its {marker!r} line")
        fails += 1
        continue
    got = hashlib.sha256(text[at:].encode("utf-8")).hexdigest()
    if got != want:
        print(f"FAIL  TPL-17 {rel} differs from the pinned upstream text")
        fails += 1
if not fails:
    print(f"PASS  {len(PINNED)} verbatim upstream copy matches its pinned hash")
sys.exit(1 if fails else 0)
