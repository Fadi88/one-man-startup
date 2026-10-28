"""TPL-105, TPL-107: every review a founder reads opens with a plain list, and a diff review
looks past the diff.

Each `## Round` of a `docs/work/<id>/review.md` must carry a `### For the founder` list with one
line per finding of that round, `- <id>: <what a user would see go wrong> (blocks launch)` for a
blocking finding and `(can wait)` for a suggestion, and no line for a finding that is not there.
A finding is a paragraph starting `**<id>. Blocking.` or `**<id>. Suggestion.`. A round whose
heading names a diff must also carry a `**Older features:**` line: the rows of earlier features
the diff could break, and what was run to show they still hold.

The reader runs first on built-in samples, so a template with no work folders still proves the
check works.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUND = re.compile(r"^## (Round[^\n]*)\n", re.M)
FINDING = re.compile(r"^\*\*([A-Za-z0-9-]+)\. (Blocking|Suggestion)\.", re.M)
FOUNDER = re.compile(r"^### For the founder\s*\n(.*?)(?=^#{2,3} |\Z)", re.M | re.S)
LINE = re.compile(r"^- ([A-Za-z0-9-]+): (.+?) \((blocks launch|can wait)\)\s*$")
LABEL = {"Blocking": "blocks launch", "Suggestion": "can wait"}


def problems(text: str) -> list[str]:
    """Every way the review's rounds break the format, as sentences. Pure, so it can be sampled."""
    out = []
    parts = ROUND.split(text)
    for title, body in zip(parts[1::2], parts[2::2]):
        title = title.strip()
        found = {fid: LABEL[kind] for fid, kind in FINDING.findall(body)}
        block = FOUNDER.search(body)
        if block is None:
            if found:
                out.append(f"{title}: no '### For the founder' list")
        else:
            listed = {}
            for raw in block.group(1).splitlines():
                if not raw.strip():
                    continue
                m = LINE.match(raw.strip())
                if not m:
                    out.append(f"{title}: founder line not in the form '- <id>: <what a user sees> "
                               f"(blocks launch|can wait)': {raw.strip()!r}")
                    continue
                fid, _, label = m.groups()
                if fid in listed:
                    out.append(f"{title}: {fid} is on the founder list twice")
                listed[fid] = label
            for fid, label in found.items():
                if fid not in listed:
                    out.append(f"{title}: finding {fid} is missing from the founder list")
                elif listed[fid] != label:
                    out.append(f"{title}: {fid} says '{listed[fid]}' but the finding is "
                               f"{'blocking' if label == 'blocks launch' else 'a suggestion'}")
            for fid in listed:
                if fid not in found:
                    out.append(f"{title}: founder list names {fid}, which is not a finding here")
        if "diff" in title.lower() and "**Older features:**" not in body:
            out.append(f"{title}: a diff round with no '**Older features:**' line")
    return out


GOOD = [
    "## Round 1: spec (2026-11-01)\n\n### For the founder\n\n"
    "- B1: a user who changes the category loses the AI's first guess (blocks launch)\n"
    "- S1: the error message says 'invalid' with no next step (can wait)\n\n"
    "### Blocking\n\n**B1. Blocking. Where: RCPT-4.** text\n\n### Suggestions\n\n"
    "**S1. Suggestion. Where: ux.md.** text\n",
    "## Round 2: fix diff (2026-11-02)\n\n**Older features:** RCPT-1 to RCPT-6, their tests run, "
    "all pass.\n\nNo blocking findings.\n",
    "# Review\n\nNo rounds yet.\n",
]
BAD = [
    # no founder list
    "## Round 1: spec\n\n**B1. Blocking. Where: x.** text\n",
    # a finding left off the list
    "## Round 1: spec\n\n### For the founder\n\n- B1: totals are wrong (blocks launch)\n\n"
    "**B1. Blocking.** a\n\n**S1. Suggestion.** b\n",
    # a suggestion sold as blocking
    "## Round 1: spec\n\n### For the founder\n\n- S1: typo (blocks launch)\n\n**S1. Suggestion.** b\n",
    # a line with no label
    "## Round 1: spec\n\n### For the founder\n\n- B1: totals are wrong\n\n**B1. Blocking.** a\n",
    # a line for a finding that is not there
    "## Round 1: spec\n\n### For the founder\n\n- B1: a (blocks launch)\n- B2: b (blocks launch)\n\n"
    "**B1. Blocking.** a\n",
    # a diff round that only read the diff
    "## Round 3: T1 diff\n\nNo blocking findings.\n",
]


def selftest() -> list[str]:
    fails = []
    for t in GOOD:
        if problems(t):
            fails.append(f"FAIL  TPL-105 self-test: good sample refused: {problems(t)}")
    for t in BAD:
        if not problems(t):
            fails.append(f"FAIL  TPL-105 self-test: bad sample let through: {t[:60]!r}")
    return fails


def main() -> int:
    fails = selftest()
    reviews = sorted((ROOT / "docs" / "work").glob("*/review.md"))
    for f in reviews:
        for p in problems(f.read_text(encoding="utf-8")):
            ref = "TPL-107" if "Older features" in p else "TPL-105"
            fails.append(f"FAIL  {ref} {f.relative_to(ROOT).as_posix()}: {p}")
    for line in fails:
        print(line)
    if not fails:
        print(f"PASS  TPL-105 TPL-107 read {len(reviews)} review files and {len(GOOD) + len(BAD)} samples; "
              "every round has its founder list and every diff round its older features")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
