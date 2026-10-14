"""Check that every URL cited in the given files answers.

    python tools/link_check.py docs/legal/regions/*.md

Not part of the sweep, because it needs the network and sites change. The
legal agent runs it before a launch review, and setup runs it on the packs it
writes. A cited page that does not exist is a claim with no source (rule 11).

Prints one line per URL: OK, BLOCKED (the site refuses scripts; open it by
hand) or DEAD (404, 410 or the domain does not resolve). Exits 1 if any URL is
DEAD.
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL = re.compile(r"https?://[^\s)>`\"'\]]+")


def status(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link check)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return "OK" if r.status < 400 else f"DEAD {r.status}"
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            return f"DEAD {e.code}"
        return f"BLOCKED {e.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return f"DEAD {type(e).__name__}"


def main(paths: list[str]) -> int:
    urls = sorted({u.rstrip(".,;:") for p in paths for u in URL.findall(Path(p).read_text(encoding="utf-8"))})
    if not urls:
        print("no URLs found")
        return 1
    dead = 0
    for u in urls:
        s = status(u)
        dead += s.startswith("DEAD")
        print(f"{s:<12} {u}")
    print(f"\n{len(urls)} URLs, {dead} dead")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
