"""TPL-92, TPL-94: the tools' own options and exceptions work, proven on samples.

TPL-92: tools/render_mockups.py turns --dark, --rtl and --text-scale into the extra variants it
renders, with the file suffixes the designer looks for. Only the argument parsing is checked
here, so the sweep needs no browser.

TPL-94: tools/link_check.py lets through a URL whose line notes "(returned 404 on YYYY-MM-DD)",
and still checks a URL that is cited elsewhere without the note. No network is used.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fails: list[str] = []

# TPL-92
render = load("render_mockups")
cases = [
    ([], [], []),
    (["--dark"], [], ["", "-dark"]),
    (["--rtl", "docs/design/mockups/a.html"], ["docs/design/mockups/a.html"], ["", "-rtl"]),
    (["--text-scale", "1.5"], [], ["", "-text150"]),
    (["--dark", "--rtl", "--text-scale", "2"], [], ["", "-dark", "-rtl", "-text200"]),
]
for argv, want_files, want_suffixes in cases:
    files, variants = render.parse(argv)
    suffixes = [s for s, _ in variants]
    if [f.as_posix() for f in files] != want_files or suffixes != (want_suffixes or [""]):
        fails.append(f"FAIL  TPL-92 render_mockups {argv!r} gave {files!r}, {suffixes!r}")
_, variants = render.parse(["--dark", "--rtl", "--text-scale", "1.5"])
opts = dict(variants)
if opts.get("-dark") != {"color_scheme": "dark"} or opts.get("-rtl") != {"dir": "rtl"} \
        or opts.get("-text150") != {"text_scale": 1.5} or opts.get("") != {}:
    fails.append(f"FAIL  TPL-92 render_mockups variant options are wrong: {variants!r}")


def refused(argv: list[str]) -> bool:
    try:
        with contextlib.redirect_stderr(io.StringIO()):
            render.parse(argv)
    except SystemExit:
        return True
    return False


for bad in (["--text-scale", "0"], ["--text-scale", "big"], ["--text-scale"], ["--out", "x"]):
    if not refused(bad):
        fails.append(f"FAIL  TPL-92 render_mockups accepted {bad!r}")

# TPL-94
link = load("link_check")
sample = "\n".join([
    "- Old rule page https://gone.example.org/rule (returned 404 on 2026-10-01)",
    "- Live page https://live.example.org/page",
    "- Cited twice https://twice.example.org/a (returned 404 on 2026-10-01)",
    "- and again https://twice.example.org/a",
    "- Not a note https://bad.example.org/x (returned 404 sometime)",
])
to_check, noted = link.cited(sample)
if noted != ["https://gone.example.org/rule"]:
    fails.append(f"FAIL  TPL-94 link_check noted {noted!r}, wanted only the gone page")
if to_check != ["https://bad.example.org/x", "https://live.example.org/page", "https://twice.example.org/a"]:
    fails.append(f"FAIL  TPL-94 link_check would check {to_check!r}")

for f in fails:
    print(f)
if not fails:
    print(f"PASS  TPL-92 render flags parse ({len(cases)} cases, 4 refused), "
          "TPL-94 a noted 404 is let through and an un-noted one is still checked")
sys.exit(1 if fails else 0)
