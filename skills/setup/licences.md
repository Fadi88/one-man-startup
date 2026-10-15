# Setup: choosing a licence

Part of `skills/setup/SKILL.md`, interview branch 10.

This is not legal advice. It explains the common choices so the founder can decide; `legal` can
review the choice before launch, and a lawyer should look at anything unusual.

As of: 2026-10-15.

## What a licence decides

Who may use, copy, change, share or sell the product's code, and on what conditions. It covers
the code, not the product's name or brand.

## The options

Put these to the founder at their level (`skills/founder-voice/`), each with what it means for
the business.

| Choice | What others may do | What it means for the business |
|---|---|---|
| **All rights reserved** (no open licence) | Nothing without your permission. Code without a licence stays under exclusive copyright. If the repository is public, GitHub's terms still let people view and fork it, but not use it. | Competitors cannot legally copy the product. Nobody outside can build on it. The usual choice for a product you sell. |
| **MIT** | Use, copy, change and sell it, for any purpose, including in their own closed products. The only condition: keep your copyright and licence notice. | Free marketing and outside contributions; no protection from a competitor running a copy. |
| **Apache 2.0** | The same as MIT, plus an explicit permission to use any patents you hold that the code uses. They must keep the notices and say what they changed; it gives no right to your trademarks. | As MIT, with clearer terms on patents. Common for company-backed open source. |
| **GPLv3** | Use, change and sell it, but whoever distributes it, changed or not, must make the full source available under the same licence. | Keeps shared versions open. On choosealicense.com, the "network use is distribution" condition is listed for AGPL and not for GPL, so a competitor could offer a changed copy as an online service without sharing its changes. |
| **AGPLv3** | As GPLv3, and offering it to users over a network counts as distributing it, so a hosted copy must share its full source too. | The strongest of these at keeping copies open, including copies run as a service. |

## Recommend

**All rights reserved**, unless open source is part of how the product grows (a developer tool,
a library, a community project). If it is, ask what matters more: the most people using it
(MIT or Apache 2.0) or that copies stay open (AGPLv3, or GPLv3 if the product is not offered as
an online service).

Say also: ask `legal` before changing the licence of code that has already been published.

## The template's own notice

This project started from the one-man startup template, which is under the MIT licence. MIT asks
that its copyright and permission notice stay with copies or substantial portions of the
template, so `tools/clean_template.py` keeps it in `docs/licenses/one-man-startup.txt`, whatever
the founder chooses for their own code. Files copied from other projects keep their own licence
files (for example `skills/frontend-design/LICENSE.txt`).

## Writing the file

Record the choice in `project.toml [product] licence` as `proprietary` or its SPDX id (`MIT`,
`Apache-2.0`, `GPL-3.0-only`, `AGPL-3.0-only`), then write `LICENSE`:

- **All rights reserved:** `Copyright (c) <year> <founder or company name>. All rights
  reserved.` and a line pointing to `docs/licenses/` for the notices of the code it includes.
- **An open licence:** the official text, word for word, from its page on choosealicense.com,
  with only the year and the name filled in. Never write a licence text from memory.

## Sources

- choosealicense.com, the licence list with each licence's permissions, conditions and
  limitations: https://choosealicense.com/licenses/ (read 2026-10-15).
- choosealicense.com, "No License": https://choosealicense.com/no-permission/ (read 2026-10-15).
- The MIT licence text in this repository's `LICENSE` ("The above copyright notice and this
  permission notice shall be included in all copies or substantial portions of the Software").
