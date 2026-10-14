"""TPL-12: region packs say they are not legal advice, carry a date and cite sources.

Also warns (SKIP, not FAIL) when a pack is older than 90 days, because the
legal-review skill requires a re-check before launch, not before every commit.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
packs = sorted((ROOT / "docs" / "legal" / "regions").glob("*.md"))
if not packs:
    print("FAIL  TPL-12 no region packs, not even _TEMPLATE.md")
    sys.exit(1)

fails = 0
for p in packs:
    text = p.read_text(encoding="utf-8")
    name = p.relative_to(ROOT).as_posix()
    if not text.startswith("**Not legal advice.**"):
        print(f"FAIL  TPL-12 {name} does not open with the not-legal-advice line")
        fails += 1
    m = re.search(r"^As of: (\S+)", text, flags=re.M)
    if not m:
        print(f"FAIL  TPL-12 {name} has no 'As of:' line")
        fails += 1
    elif p.name != "_TEMPLATE.md":
        try:
            age = (dt.date.today() - dt.date.fromisoformat(m.group(1))).days
            if age > 90:
                print(f"SKIP  {name} is {age} days old; re-check it before the next launch")
        except ValueError:
            print(f"FAIL  TPL-12 {name} 'As of' is not a YYYY-MM-DD date")
            fails += 1
    if "## Sources" not in text:
        print(f"FAIL  TPL-12 {name} has no Sources section")
        fails += 1
print(f"PASS  {len(packs)} region packs carry the disclaimer, a date and sources" if not fails else "")
sys.exit(1 if fails else 0)
