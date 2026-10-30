"""TPL-105, TPL-107, TPL-119: every review a founder reads opens with a plain list, and a code
review looks past the change.

A review round is a `## Round <n>: <what> (<date>)` heading (`#`, `###`, and "Review" for
"Round" are read too, so a slip is still checked). Each round must open with a
`### For the founder` list, before its first finding, with one line per finding of that round:
`- <id>: <what a user would see go wrong> (blocks launch)` for a blocking finding and
`(can wait)` for a suggestion, and no line for a finding that is not there. A finding is a
paragraph starting `**<id>. Blocking.` or `**<id>. Suggestion.`; a near miss (`**B1 Blocking.**`,
`**B1: Blocking**`) is refused rather than skipped, and so is a finding outside any round.

A round about code (its heading names a diff, a code review or a ticket) must carry a non-empty
`**Older features:**` line: the rows of earlier features the change could break, and what was
run to show they still hold (TPL-107).

When project.toml [owner] level is non-technical, a founder line may not use a word from the
"Instead of" column of the table in skills/founder-voice/SKILL.md, except the words that also
name things users do (merge, secret, test, push, bug) (TPL-119).

The reader runs first on built-in samples, so a template with no work folders still proves the
check works.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUND = re.compile(r"^#{1,3} ((?:Round|Review) \d+[^\n]*)\n", re.M | re.I)
FINDING = re.compile(r"^\*\*([A-Za-z0-9-]+)\. (Blocking|Suggestion)\.", re.M)
NEAR = re.compile(r"^\*\*[A-Za-z0-9-]+[.:]?\s*\**\s*(Blocking|Suggestion)\b", re.M | re.I)
FOUNDER = re.compile(r"^### For the founder[ \t]*\n(.*?)(?=^#{1,6} |^\*\*|\Z)", re.M | re.S)
LINE = re.compile(r"^- ([A-Za-z0-9-]+): (.+?) \((blocks launch|can wait)\)\s*$")
OLDER = re.compile(r"^\*\*Older features:\*\*[ \t]*(\S.*)$", re.M)
CODE = re.compile(r"\b(diff|code review|ticket)\b", re.I)
# Words from the table that also name things users do, so a line about what users see may use them.
USER_WORDS = {"merge", "secret", "test", "push", "bug"}
LABEL = {"Blocking": "blocks launch", "Suggestion": "can wait"}
VOICE = ROOT / "skills" / "founder-voice" / "SKILL.md"


def jargon_words(voice: str) -> list[str]:
    """The words of the 'Instead of' column, one source for the skill and this check."""
    words = []
    in_table = False
    for line in voice.splitlines():
        if line.startswith("| Instead of |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cell = line.strip("|").split("|")[0].strip()
            if set(cell) <= set("-"):
                continue
            words += [w.strip() for w in cell.split(",") if w.strip() and w.strip().lower() not in USER_WORDS]
    return words


def problems(text: str, jargon: list[str] = ()) -> list[str]:
    """Every way the review breaks the format, as sentences. Pure, so it can be sampled."""
    out = []
    parts = ROUND.split(text)
    before = parts[0]
    if FINDING.search(before) or NEAR.search(before):
        out.append("a finding sits outside any '## Round <n>: ...' heading")
    for title, body in zip(parts[1::2], parts[2::2]):
        title = title.strip()
        found = {fid: LABEL[kind] for fid, kind in FINDING.findall(body)}
        exact = {m.start() for m in FINDING.finditer(body)}
        for m in NEAR.finditer(body):
            if m.start() not in exact:
                line = body[m.start():].splitlines()[0][:60]
                out.append(f"{title}: finding not in the form '**<id>. Blocking.' or '**<id>. Suggestion.': {line!r}")
        block = FOUNDER.search(body)
        first = min([m.start() for m in FINDING.finditer(body)] + [len(body)])
        if block is None:
            if found:
                out.append(f"{title}: no '### For the founder' list")
        else:
            if block.start() > first:
                out.append(f"{title}: the founder list comes after the findings; the round opens with it")
            listed = {}
            for raw in block.group(1).splitlines():
                if not raw.strip():
                    continue
                m = LINE.match(raw.strip())
                if not m:
                    out.append(f"{title}: founder line not in the form '- <id>: <what a user sees> "
                               f"(blocks launch|can wait)': {raw.strip()!r}")
                    continue
                fid, said, label = m.groups()
                if fid in listed:
                    out.append(f"{title}: {fid} is on the founder list twice")
                listed[fid] = label
                for word in jargon:
                    if re.search(rf"\b{re.escape(word)}\b", said, re.I):
                        out.append(f"{title}: {fid}'s founder line says {word!r}; say it the plain way "
                                   "(skills/founder-voice/)")
            for fid, label in found.items():
                if fid not in listed:
                    out.append(f"{title}: finding {fid} is missing from the founder list")
                elif listed[fid] != label:
                    out.append(f"{title}: {fid} says '{listed[fid]}' but the finding is "
                               f"{'blocking' if label == 'blocks launch' else 'a suggestion'}")
            for fid in listed:
                if fid not in found:
                    out.append(f"{title}: founder list names {fid}, which is not a finding here")
        if CODE.search(title) and not OLDER.search(body):
            out.append(f"{title}: a round about code with no filled '**Older features:**' line")
    return out


JARGON = ["API", "deploy", "regression"]  # what jargon_words gives minus the user words
GOOD = [
    "## Round 1: spec (2026-11-01)\n\n### For the founder\n\n"
    "- B1: a user who changes the category loses the AI's first guess (blocks launch)\n"
    "- S1: the error message says 'invalid' with no next step (can wait)\n\n"
    "### Blocking\n\n**B1. Blocking. Where: RCPT-4.** text\n\n### Suggestions\n\n"
    "**S1. Suggestion. Where: ux.md.** text\n",
    "## Round 2: fix diff (2026-11-02)\n\n**Older features:** RCPT-1 to RCPT-6, their tests run, "
    "all pass.\n\nNo blocking findings.\n",
    "# Review\n\nNo rounds yet.\n",
    # "code" in a spec's subject does not make it a code round; a user may "merge" lists
    "## Round 1: spec of the code of conduct page\n\n### For the founder\n\n"
    "- B1: users cannot merge two shopping lists (blocks launch)\n\n**B1. Blocking.** a\n",
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
    # "Review" instead of "Round"
    "## Review 1: spec\n\n**B1. Blocking.** a\n",
    # a level-three heading
    "### Round 1: spec\n\n**B1. Blocking.** a\n",
    # a near-miss finding form
    "## Round 1: spec\n\n### For the founder\n\n- B1: a (blocks launch)\n\n**B1. Blocking.** a\n\n"
    "**B2 Blocking.** b\n",
    # a code round whose title lacks "diff"
    "## Round 4: T1 code review\n\nNo blocking findings.\n",
    # a ticket round
    "## Round 5: ticket T2\n\nNo blocking findings.\n",
    # an empty older-features line
    "## Round 2: fix diff\n\n**Older features:**\n\nNo blocking findings.\n",
    # the founder list after the findings
    "## Round 1: spec\n\n**B1. Blocking.** a\n\n### For the founder\n\n- B1: totals wrong (blocks launch)\n",
    # findings with no round at all
    "# Review\n\n**B1. Blocking.** a\n",
    # jargon in a founder line
    "## Round 1: spec\n\n### For the founder\n\n- B1: the API returns the wrong total (blocks launch)\n\n"
    "**B1. Blocking.** a\n",
]


def selftest() -> list[str]:
    fails = []
    for t in GOOD:
        if problems(t, JARGON):
            fails.append(f"FAIL  TPL-105 self-test: good sample refused: {problems(t, JARGON)}")
    for t in BAD:
        if not problems(t, JARGON):
            fails.append(f"FAIL  TPL-105 self-test: bad sample let through: {t[:60]!r}")
    words = jargon_words(VOICE.read_text(encoding="utf-8")) if VOICE.exists() else []
    if "API" not in words or "Say" in words:
        fails.append(f"FAIL  TPL-119 self-test: founder-voice table read as {words[:6]}")
    return fails


def main() -> int:
    fails = selftest()
    owner = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("owner", {})
    jargon = jargon_words(VOICE.read_text(encoding="utf-8")) if owner.get("level") == "non-technical" else []
    reviews = sorted((ROOT / "docs" / "work").glob("*/review.md"))
    for f in reviews:
        for p in problems(f.read_text(encoding="utf-8"), jargon):
            ref = "TPL-107" if "Older features" in p else "TPL-119" if "plain way" in p else "TPL-105"
            fails.append(f"FAIL  {ref} {f.relative_to(ROOT).as_posix()}: {p}")
    for line in fails:
        print(line)
    if not fails:
        print(f"PASS  TPL-105 TPL-107 TPL-119 read {len(reviews)} review files and {len(GOOD) + len(BAD)} "
              "samples; every round opens with its founder list and every code round names older features")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
