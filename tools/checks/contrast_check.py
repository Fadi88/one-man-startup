"""TPL-46: every text and background pair in the brand passes its contrast minimum.

Reads the "Contrast pairs" table in docs/design/brand.md, which product-designer keeps:

    | Pair | Text | Background | Minimum |
    |---|---|---|---|
    | Body on page | #1A1A1A | #FFFFFF | 4.5 |

Minimum is 4.5 for normal text and 3 for large text and interface parts (WCAG 2.2, 1.4.3 and
1.4.11). The ratio is the WCAG formula from relative luminance, computed here, never by hand.
A row that cannot be read fails, so a typo cannot hide a failing pair.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BRAND = ROOT / "docs" / "design" / "brand.md"
HEX = re.compile(r"^#?([0-9a-fA-F]{6})$")
NUMBER = re.compile(r"^(\d+(?:\.\d+)?)")


def luminance(hex_colour: str) -> float:
    rgb = [int(hex_colour[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check(text: str) -> tuple[list[str], int]:
    """Every row of the Contrast pairs table must read, and meet its minimum."""
    parts = text.split("## Contrast pairs", 1)
    if len(parts) < 2:
        return ['TPL-46 docs/design/brand.md has no "## Contrast pairs" table'], 0
    lines = [l.strip() for l in parts[1].split("\n## ", 1)[0].splitlines() if l.strip().startswith("|")]
    out: list[str] = []
    pairs = 0
    for line in lines[2:]:  # past the header and the separator
        cells = [c.strip() for c in line.strip("|").split("|")]
        ok = len(cells) == 4
        fg, bg, minimum = (HEX.match(cells[1]), HEX.match(cells[2]), NUMBER.match(cells[3])) if ok else (None,) * 3
        if not (fg and bg and minimum):
            out.append(f"TPL-46 cannot read this pair (colours as #RRGGBB, the minimum as a number): {line}")
            continue
        pairs += 1
        r = ratio(fg.group(1), bg.group(1))
        if r < float(minimum.group(1)):
            out.append(f"TPL-46 {cells[0]}: {cells[1]} on {cells[2]} is {r:.2f} to 1, under {minimum.group(1)}")
    if not pairs and not out:
        out.append("TPL-46 the Contrast pairs table in docs/design/brand.md has no rows")
    return out, pairs


fails: list[str] = []
# The formula: black on white is 21 and a colour on itself is 1 by definition; #767676 on white
# works out at 4.54, the usual example of the lightest grey that passes 4.5.
for a, b, want in [("000000", "FFFFFF", 21.0), ("FFFFFF", "FFFFFF", 1.0), ("767676", "FFFFFF", 4.54)]:
    if abs(round(ratio(a, b), 2) - want) > 0.01:
        fails.append(f"TPL-46 the formula gives {ratio(a, b):.2f} for #{a} on #{b}, not {want}")

# The reading: a failing pair, an unreadable colour and an empty table fail; "4.5:1" reads.
SAMPLE = "## Contrast pairs\n\n| Pair | Text | Background | Minimum |\n|---|---|---|---|\n"
for rows, want in [("| Body | #1A1A1A | #FFFFFF | 4.5 |\n", 0), ("| Muted | #777777 | #FFFFFF | 4.5 |\n", 1),
                   ("| Short | #FFF | #000000 | 4.5 |\n", 1), ("| Ratio | #000000 | #FFFFFF | 4.5:1 |\n", 0),
                   ("| Word | white | #000000 | 3 |\n", 1), ("", 1)]:
    if len(check(SAMPLE + rows)[0]) != want:
        fails.append(f"TPL-46 the check reads {rows.strip() or 'an empty table'!r} wrongly")

if not BRAND.exists():
    print("SKIP  no docs/design/brand.md yet, so no colour pairs to check")
else:
    found, n = check(BRAND.read_text(encoding="utf-8"))
    fails += found
    if not found:
        print(f"PASS  {n} colour pairs meet their contrast minimum")

for f in fails:
    print(f"FAIL  {f}")
sys.exit(1 if fails else 0)
