"""Check that every URL cited in the given files answers.

    python tools/link_check.py docs/legal/regions/*.md

Not part of the sweep, because it needs the network and sites change. The
legal agent runs it before a launch review, and setup runs it on the packs it
writes. A cited page that does not exist is a claim with no source (rule 10).

Prints one line per URL: OK, BLOCKED (the site refuses scripts; open it by
hand), BY HAND (a site known to answer scripts with 404 while browsers load the page; open it
in a browser) or DEAD (404, 410 or the domain does not resolve). Exits 1 if any URL is DEAD.

TPL-94: a URL whose line says "(returned 404 on YYYY-MM-DD)" is a page known to be gone, cited
on purpose (a brief may record what a page said before it went). It is not fetched and is
reported as NOTED. The same URL cited on another line without the note is still checked.
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

URL = re.compile(r"https?://[^\s)>`\"'\]]+")
NOTED = re.compile(r"\(returned 404 on \d{4}-\d{2}-\d{2}\)")

# TPL-44: hosts that answer a script's request with 404 while a browser loads the same page.
# Each was seen doing it, with the date. A 404 from them, or a subdomain, is reported as BY HAND,
# not DEAD; the cost is that a page there that is really gone shows only when opened by hand.
BY_HAND = {
    # The COPPA rule page answered 404 to Python with browser headers and loaded in a fetch tool.
    "ftc.gov": "2026-10-17",
}


def status(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link check)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return "OK" if r.status < 400 else f"DEAD {r.status}"
    except urllib.error.HTTPError as e:
        host = urllib.parse.urlsplit(url).hostname or ""
        if e.code == 404 and any(host == h or host.endswith("." + h) for h in BY_HAND):
            return "BY HAND"
        if e.code in (404, 410):
            return f"DEAD {e.code}"
        return f"BLOCKED {e.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return f"DEAD {type(e).__name__}"


def cited(text: str) -> tuple[list[str], list[str]]:
    """The URLs to fetch, and the ones only ever cited on a line noting their 404 (TPL-94)."""
    plain: set[str] = set()
    noted: set[str] = set()
    for line in text.splitlines():
        found = {u.rstrip(".,;:") for u in URL.findall(line)}
        (noted if NOTED.search(line) else plain).update(found)
    return sorted(plain), sorted(noted - plain)


def main(paths: list[str]) -> int:
    plain: set[str] = set()
    noted: set[str] = set()
    for p in paths:
        to_check, gone = cited(Path(p).read_text(encoding="utf-8"))
        plain.update(to_check)
        noted.update(gone)
    noted -= plain
    urls = sorted(plain)
    if not urls and not noted:
        print("no URLs found")
        return 1
    for u in sorted(noted):
        print(f"{'NOTED':<12} {u}")
    dead = by_hand = 0
    for u in urls:
        s = status(u)
        dead += s.startswith("DEAD")
        by_hand += s.startswith("BY HAND")
        print(f"{s:<12} {u}")
    print(f"\n{len(urls)} URLs, {dead} dead, {by_hand} to open by hand, {len(noted)} noted as gone")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
