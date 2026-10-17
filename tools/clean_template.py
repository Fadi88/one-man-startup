"""TPL-30: remove what belongs to the template itself from a new project made from it.

The template's repository carries its own history: decisions and rejected ideas about the
template, its launch experiments and assumptions, its landing page, its README, example runs and
marketing diagrams. A project made from the template starts without them. Setup runs this once,
after the founder confirms the setup summary and says go.

    python tools/clean_template.py           # show what would change, change nothing
    python tools/clean_template.py --yes     # do it

It is safe to run twice. It removes itself and its check when done, since a project never needs
them again. Everything it removes stays in the template's own repository and in git history.
"""
from __future__ import annotations

import re
import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Whole files and folders that only describe or publish the template.
PATHS = [
    "examples",
    "docs/growth/readme-survey.md",
    "site",
    ".github/workflows/pages.yml",
    "docs/images/hero.svg",
    "docs/images/journey.svg",
    "docs/images/team.svg",
    "docs/images/your-call.svg",
    "docs/images/demo.svg",
    "docs/images/social-preview.svg",
    "docs/images/social-preview.png",
    "tools/checks/clean_check.py",
    "tools/clean_template.py",
]

# Requirement rows about the template's README, diagrams, landing page, guide and this script.
TPL_ROWS = ["TPL-18", "TPL-19", "TPL-20", "TPL-21", "TPL-27", "TPL-30", "TPL-38"]

TEMPLATE_SECTION = "## About the template itself"

PROJECT_README = """# {name}

{one_liner}

## How this project works

You talk to one agent, the project manager, in your own words. It runs the rest of the team,
keeps a written record of every step in `docs/`, and waits for your yes before anything goes
live, costs money, deletes something or sends a message.

- New here: [docs/START-HERE.md](docs/START-HERE.md).
- The rules the agents follow: [AGENTS.md](AGENTS.md).
- How the files fit together: [docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md).

Made from the [one-man startup template](https://github.com/Fadi88/one-man-startup).
"""


def drop_section(text: str) -> str:
    """Remove the template's own section from a p1 decision file (it runs to the end)."""
    i = text.find(TEMPLATE_SECTION)
    return text if i < 0 else text[:i].rstrip() + "\n"


def drop_rows(text: str, pattern: str) -> str:
    return "".join(l for l in text.splitlines(keepends=True) if not re.match(pattern, l))


def drop_experiments(text: str) -> str:
    text = drop_rows(text, r"^\| \d+ \|")
    head, sep, _ = text.partition("## The entries")
    return head + sep + "\n\n(none yet)\n" if sep else text


def drop_worked_example(text: str) -> str:
    return re.sub(r" If you're stuck\nbefore you get that far, the \[worked example\][^.]*\.", "", text)


def publish_off(text: str) -> str:
    """TPL-43: a new project publishes nothing until the founder asks for it."""
    return re.sub(r"(^\[publish\]\n(?:#.*\n)*enabled = )true$", r"\1false", text, count=1, flags=re.M)


EDITS = {
    "docs/requirements/p1-closed-decisions.md": ("remove decisions about the template", drop_section),
    "docs/requirements/p1-rejected.md": ("remove ideas rejected for the template", drop_section),
    "docs/EXPERIMENTS.md": ("remove the template's launch experiments", drop_experiments),
    "docs/ASSUMPTIONS.md": ("remove the template's assumptions", lambda t: drop_rows(t, r"^\| A-\d+ \|")),
    "docs/requirements/TPL.md": ("remove rows about the template's own pages",
                                 lambda t: drop_rows(t, r"^\| (%s) \|" % "|".join(TPL_ROWS))),
    "docs/START-HERE.md": ("remove the link to the template's example run", drop_worked_example),
    "project.toml": ("switch publishing off until the founder asks for it", publish_off),
}


TEMPLATE_NOTICE = "docs/licenses/one-man-startup.txt"


def template_licence_left() -> bool:
    """The template's own MIT licence still sits in LICENSE, not yet moved to its notice file."""
    f = ROOT / "LICENSE"
    return f.exists() and f.read_text(encoding="utf-8").startswith("MIT License") and not (ROOT / TEMPLATE_NOTICE).exists()


def plan() -> list[tuple[str, str]]:
    """Every change as (path, what), only for what is still there to change."""
    out = [(p, "delete") for p in PATHS if (ROOT / p).exists()]
    if template_licence_left():
        out.append(("LICENSE", f"move the template's licence notice to {TEMPLATE_NOTICE}"))
    for rel, (what, fn) in EDITS.items():
        f = ROOT / rel
        if f.exists() and fn(t := f.read_text(encoding="utf-8")) != t:
            out.append((rel, what))
    readme = ROOT / "README.md"
    if readme.exists() and "# One-man startup" in readme.read_text(encoding="utf-8"):
        out.append(("README.md", "replace the template's README with one for this project"))
    return out


def apply() -> None:
    product = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8")).get("product", {})
    if product.get("name", "unset") == "unset":
        sys.exit("clean_template: run setup first; project.toml [product] name is unset")
    for rel, what in plan():
        f = ROOT / rel
        if what == "delete":
            shutil.rmtree(f) if f.is_dir() else f.unlink()
        elif rel == "LICENSE":
            (ROOT / TEMPLATE_NOTICE).parent.mkdir(parents=True, exist_ok=True)
            f.replace(ROOT / TEMPLATE_NOTICE)
        elif rel == "README.md":
            f.write_text(PROJECT_README.format(name=product["name"], one_liner=product.get("one_liner", "")),
                         encoding="utf-8")
        else:
            f.write_text(EDITS[rel][1](f.read_text(encoding="utf-8")), encoding="utf-8")


def main(argv: list[str]) -> int:
    changes = plan()
    if not changes:
        print("Nothing of the template's own left to remove.")
        return 0
    for rel, what in changes:
        print(f"{what:60}  {rel}")
    if "--yes" not in argv:
        print(f"\n{len(changes)} changes shown, none made. Run again with --yes to make them.")
        return 0
    apply()
    print(f"\nDone. Now run: python tools/checks/req_check.py --fix, then python tools/run_all.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
