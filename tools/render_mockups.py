"""TPL-47: render each screen of the HTML mockups to its own PNG, so a designer can look at its
own work before anyone builds it.

    python tools/render_mockups.py [mockup.html ...]

With no arguments it renders every .html file in docs/design/mockups/. Each screen is a
`<section id="screen-N">` and is captured on its own into docs/design/mockups/shots/; capturing
the whole page cut off or repeated content when this was first used. Needs Playwright, which is
not part of the sweep: `pip install playwright` and `playwright install chromium`, on the
founder's go.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOCKUPS = ROOT / "docs" / "design" / "mockups"
SHOTS = MOCKUPS / "shots"


def main(argv: list[str]) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("render_mockups: Playwright is not installed; see this file's first lines")
        return 1
    files = [Path(a) for a in argv] or sorted(MOCKUPS.glob("*.html"))
    if not files:
        print(f"render_mockups: no .html files in {MOCKUPS.relative_to(ROOT).as_posix()}")
        return 1
    SHOTS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2000, "height": 1200})
        for html in files:
            page.goto(html.resolve().as_uri())
            page.wait_for_load_state("networkidle")
            sections = page.query_selector_all("section[id^=screen-]")
            for s in sections:
                s.screenshot(path=str(SHOTS / f"{html.stem}-{s.get_attribute('id')}.png"))
            print(f"{html.name}: {len(sections)} screens" if sections else f"{html.name}: no section#screen-N found")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
