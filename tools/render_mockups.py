"""TPL-47, TPL-92: render each screen of the HTML mockups to its own PNG, so a designer can look
at its own work before anyone builds it.

    python tools/render_mockups.py [--dark] [--rtl] [--text-scale N] [mockup.html ...]

With no files it renders every .html file in docs/design/mockups/. Each screen is a
`<section id="screen-N">` and is captured on its own into docs/design/mockups/shots/; capturing
the whole page cut off or repeated content when this was first used. Needs Playwright, which is
not part of the sweep: `pip install playwright` and `playwright install chromium`, on the
founder's go.

TPL-92: each flag adds one more PNG per screen next to the normal one, so the states a design
most often breaks in are seen before anyone builds it: --dark renders with the dark color
scheme (suffix -dark), --rtl sets dir="rtl" on <html> (suffix -rtl), and --text-scale N
multiplies the root font size by N (suffix -text150 for 1.5). Without flags the output is as
before.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOCKUPS = ROOT / "docs" / "design" / "mockups"
SHOTS = MOCKUPS / "shots"


def scale(text: str) -> float:
    value = float(text)
    if not 0 < value <= 4:
        raise argparse.ArgumentTypeError("must be above 0 and at most 4")
    return value


def parse(argv: list[str]) -> tuple[list[Path], list[tuple[str, dict]]]:
    """The files to render and the variants, as (file suffix, options). Pure, so it can be checked."""
    ap = argparse.ArgumentParser(prog="render_mockups")
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--dark", action="store_true", help="also render in the dark color scheme")
    ap.add_argument("--rtl", action="store_true", help='also render with dir="rtl" on <html>')
    ap.add_argument("--text-scale", type=scale, metavar="N", help="also render with the root font size times N")
    args = ap.parse_args(argv)
    variants: list[tuple[str, dict]] = [("", {})]
    if args.dark:
        variants.append(("-dark", {"color_scheme": "dark"}))
    if args.rtl:
        variants.append(("-rtl", {"dir": "rtl"}))
    if args.text_scale:
        variants.append((f"-text{round(args.text_scale * 100)}", {"text_scale": args.text_scale}))
    return args.files, variants


def main(argv: list[str]) -> int:
    files, variants = parse(argv)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("render_mockups: Playwright is not installed; see this file's first lines")
        return 1
    files = files or sorted(MOCKUPS.glob("*.html"))
    if not files:
        print(f"render_mockups: no .html files in {MOCKUPS.relative_to(ROOT).as_posix()}")
        return 1
    SHOTS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2000, "height": 1200})
        for html in files:
            for suffix, opts in variants:
                page.emulate_media(color_scheme=opts.get("color_scheme", "light"))
                page.goto(html.resolve().as_uri())
                page.wait_for_load_state("networkidle")
                if "dir" in opts:
                    page.evaluate("d => { document.documentElement.dir = d; }", opts["dir"])
                if "text_scale" in opts:
                    page.evaluate("s => { const r = document.documentElement;"
                                  " r.style.fontSize = (parseFloat(getComputedStyle(r).fontSize) * s) + 'px'; }",
                                  opts["text_scale"])
                sections = page.query_selector_all("section[id^=screen-]")
                for s in sections:
                    s.screenshot(path=str(SHOTS / f"{html.stem}-{s.get_attribute('id')}{suffix}.png"))
                label = f"{html.name}{' ' + suffix[1:] if suffix else ''}"
                print(f"{label}: {len(sections)} screens" if sections else f"{label}: no section#screen-N found")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
