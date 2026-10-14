"""TPL-17: text copied verbatim from upstream stays verbatim.

The pinned files and their hashes live in tools/lib/verbatim.py. To take a
newer upstream version, replace the text and the hash in the same change, with
the fetch date beside the entry.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from verbatim import PINNED  # noqa: E402

fails = 0
for rel, (marker, want) in PINNED.items():
    path = ROOT / rel
    if not path.exists():
        print(f"FAIL  TPL-17 {rel} is missing")
        fails += 1
        continue
    data = path.read_bytes()
    if marker:
        at = data.find((marker + "\n").encode("utf-8"))
        if at < 0:
            print(f"FAIL  TPL-17 {rel} has lost its {marker!r} line")
            fails += 1
            continue
        data = data[at:]
    if hashlib.sha256(data).hexdigest() != want:
        print(f"FAIL  TPL-17 {rel} differs from the pinned upstream text")
        fails += 1
if not fails:
    print(f"PASS  {len(PINNED)} verbatim upstream copies match their pinned hashes")
sys.exit(1 if fails else 0)
