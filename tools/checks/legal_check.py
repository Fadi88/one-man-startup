"""TPL-12, TPL-95: region packs say they are not legal advice, carry a date and cite sources,
and a set-up project has no "(setup fills)" line left in docs/legal/playbook.md.

Also warns (SKIP, not FAIL) when a pack is older than 90 days, because the
legal-review skill requires a re-check before launch, not before every commit.

TPL-95: the template itself (project.toml [product] name still "unset") keeps its "(setup fills)"
lines; once setup has named the product, any one left is a playbook position nobody took. The
rule runs first on samples.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLACEHOLDER = "(setup fills)"


def unfilled(product_name: str, playbook: str) -> list[str]:
    """TPL-95: the playbook lines setup should have filled. Empty for the template itself."""
    if product_name.strip().lower() == "unset":
        return []
    return [line.strip() for line in playbook.splitlines() if PLACEHOLDER in line]


for name, text, want in [("unset", "| Retention | after (setup fills) |", 0),
                         ("Acme", "| Retention | after (setup fills) |\n| Ads | (setup fills) |", 2),
                         ("Acme", "| Retention | after 30 days |", 0)]:
    if len(unfilled(name, text)) != want:
        print(f"FAIL  TPL-95 self-test: {name!r} with {text!r} did not give {want} unfilled lines")
        sys.exit(1)

product = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("product", {}).get("name", "unset")
playbook = ROOT / "docs" / "legal" / "playbook.md"
left = unfilled(product, playbook.read_text(encoding="utf-8")) if playbook.exists() else []
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
for line in left:
    print(f"FAIL  TPL-95 docs/legal/playbook.md still has a line for setup to fill: {line[:80]}")
    fails += 1
print(f"PASS  {len(packs)} region packs carry the disclaimer, a date and sources; "
      f"playbook {'filled' if product != 'unset' else 'left for setup (template)'}" if not fails else "")
sys.exit(1 if fails else 0)
