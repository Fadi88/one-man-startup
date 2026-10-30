"""TPL-11, TPL-111: every experiment was registered properly before it ran.

Each `### N. title` entry in docs/EXPERIMENTS.md must carry a Hypothesis, a Prediction, a
"Wrong if" and a Read date, each with text after it. Every entry has a row in the "At a glance"
table with the same number and read date, and every row an entry, since the reminders read the
table (tools/lib/overdue.py): an entry missing from it would never come due.

An A/B entry (one with **Arms:**) also carries its **Assignment:** and **Guardrails:**, and a
**Sample:** line in the form `<n> per arm (`tools/ab_size.py size --base <p> --target <p>`)`;
the check runs that calculation and refuses a typed figure that differs from it.

The reader runs first on built-in samples. An empty file passes and says so.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEEDED = ["Hypothesis", "Prediction", "Wrong if", "Read"]
AB = ["Assignment", "Sample", "Guardrails"]
TABLE = re.compile(r"^\| (\d+) \| [^|]+ \| [^|]+ \| [^|]+ \| ([^|]+?) \|$", re.M)
SAMPLE = re.compile(r"([\d,]+) per arm \(`(?:python )?tools/ab_size\.py size((?: --[a-z]+ [\d.]+)+)`\)")
FLAG = re.compile(r"--([a-z]+) ([\d.]+)")


def load_size():
    spec = importlib.util.spec_from_file_location("ab_size", ROOT / "tools" / "ab_size.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.size


def field(entry: str, name: str) -> str | None:
    m = re.search(rf"^- \*\*{re.escape(name)}:\*\*(.*)$", entry, re.M)
    return None if m is None else m.group(1).strip()


def problems(text: str, size) -> list[str]:
    """Every way the file breaks registration, as sentences. Pure, so it can be sampled."""
    out = []
    entries = re.split(r"^### ", text, flags=re.M)[1:]
    table = {n: d.strip() for n, d in TABLE.findall(text.split("## The entries")[0])}
    seen = set()
    for e in entries:
        title = e.splitlines()[0].strip()
        num = title.split(".")[0]
        seen.add(num)
        for name in NEEDED:
            value = field(e, name)
            if not value:
                out.append(f"TPL-11 experiment {title!r} has no {name}" + ("" if value is None else " text"))
        read = re.match(r"\d{4}-\d{2}-\d{2}", field(e, "Read") or "")
        if field(e, "Read") and not read:
            out.append(f"TPL-11 experiment {title!r}: Read does not start with a date like 2026-12-01")
        if num not in table:
            out.append(f"TPL-11 experiment {title!r} has no row in the 'At a glance' table, so it never comes due")
        elif read and table[num] != read.group(0):
            out.append(f"TPL-11 experiment {num} reads on {read.group(0)} but the table says {table[num]}")
        if field(e, "Arms") is not None:
            for name in AB:
                if not field(e, name):
                    out.append(f"TPL-111 A/B experiment {title!r} has no {name}")
            m = SAMPLE.search(field(e, "Sample") or "")
            if field(e, "Sample") and not m:
                out.append(f"TPL-111 A/B experiment {title!r}: Sample is not '<n> per arm "
                           "(`tools/ab_size.py size --base <p> --target <p>`)'")
            elif m:
                typed = int(m[1].replace(",", ""))
                flags = {k: float(v) for k, v in FLAG.findall(m[2])}
                if not {"base", "target"} <= flags.keys() or not flags.keys() <= {"base", "target", "alpha", "power"}:
                    out.append(f"TPL-111 A/B experiment {title!r}: the size command needs --base and --target only, "
                               "with --alpha and --power optional")
                    continue
                want = size(flags["base"], flags["target"], flags.get("alpha", 0.05), flags.get("power", 0.8))
                if typed != want:
                    out.append(f"TPL-111 A/B experiment {title!r} says {typed} per arm; ab_size.py gives {want}")
    for num in table:
        if num not in seen:
            out.append(f"TPL-11 the 'At a glance' table has experiment {num} with no entry")
    return out


HEAD = "| # | Start | Experiment | Status | Read date |\n|---|---|---|---|---|\n"
ENTRY = ("### 1. Welcome screen, from 2026-11-01\n- **Hypothesis:** h\n- **Prediction:** p\n"
         "- **Wrong if:** w\n- **Read:** 2026-12-01.\n")
AB_LINES = ("- **Arms:** A old, B new.\n- **Assignment:** hash of user id.\n"
            "- **Sample:** 3,839 per arm (`tools/ab_size.py size --base 0.10 --target 0.12`).\n"
            "- **Guardrails:** crash rate.\n")
ROW1 = "| 1 | 2026-11-01 | Welcome screen | running | 2026-12-01 |\n"
GOOD = [
    "# Experiments\n",
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY + AB_LINES.replace(
        "3,839 per arm (`tools/ab_size.py size --base 0.10 --target 0.12`)",
        "3,839 per arm (`tools/ab_size.py size --target 0.12 --base 0.10 --power 0.8`)"),  # any order
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY,
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY + AB_LINES,
]
BAD = [
    HEAD + "\n## The entries\n\n" + ENTRY,                                          # not in the table
    HEAD + ROW1.replace("2026-12-01", "2026-12-09") + "\n## The entries\n\n" + ENTRY,  # dates differ
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY.replace("- **Prediction:** p\n", ""),  # field missing
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY.replace("**Wrong if:** w", "**Wrong if:**"),  # empty
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY + AB_LINES.replace("3,839", "12"),  # wrong sample
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY + AB_LINES.replace("- **Guardrails:** crash rate.\n", ""),
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY + AB_LINES.replace(
        "3,839 per arm (`tools/ab_size.py size --base 0.10 --target 0.12`)", "about 4,000"),  # free text
    HEAD + ROW1 + "| 2 | 2026-11-01 | Ghost | planned | 2026-12-01 |\n\n## The entries\n\n" + ENTRY,
    HEAD + ROW1 + "\n## The entries\n\n" + ENTRY.replace("**Read:** 2026-12-01.", "**Read:** first of December"),
]


def main() -> int:
    size = load_size()
    fails = []
    for t in GOOD:
        if problems(t, size):
            fails.append(f"self-test: good sample refused: {problems(t, size)}")
    for t in BAD:
        if not problems(t, size):
            fails.append(f"self-test: bad sample let through: {t[-80:]!r}")
    f = ROOT / "docs" / "EXPERIMENTS.md"
    if not f.exists():
        print("FAIL  TPL-11 docs/EXPERIMENTS.md is missing")
        return 1
    text = f.read_text(encoding="utf-8")
    fails += problems(text, size)
    for line in fails:
        print(f"FAIL  {line}" if line.startswith("TPL-") else f"FAIL  TPL-11 {line}")
    if not fails:
        n = len(re.split(r"^### ", text, flags=re.M)) - 1
        print(f"PASS  TPL-11 TPL-111 read {n} experiment entries and {len(GOOD) + len(BAD)} samples, "
              "each registered and in the table")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
