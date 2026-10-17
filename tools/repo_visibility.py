"""TPL-39: say whether this repository is public on GitHub.

    python tools/repo_visibility.py

Setup runs it in step 1. It asks GitHub about the `origin` remote without signing in. A public
repository answers, so an answer means anyone can read it. A private one is assumed to answer
404 like a missing one (A-11 in docs/ASSUMPTIONS.md).

Prints one line: PUBLIC, NOT PUBLIC (GitHub does not show it to strangers), NO REMOTE (not on
GitHub yet), OTHER HOST (not GitHub; check by hand) or UNKNOWN (GitHub could not be reached).
Exits 1 on PUBLIC, so a script can stop on it, and 0 otherwise.
"""
from __future__ import annotations

import re
import subprocess
import sys
import urllib.error
import urllib.request

GITHUB = re.compile(r"github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$")


def origin() -> str:
    r = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def visibility(url: str) -> str:
    if not url:
        return "NO REMOTE"
    m = GITHUB.search(url)
    if not m:
        return f"OTHER HOST {url}"
    owner, repo = m.groups()
    req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}",
                                 headers={"User-Agent": "one-man-startup visibility check"})
    try:
        with urllib.request.urlopen(req, timeout=20):
            return f"PUBLIC {owner}/{repo}"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"NOT PUBLIC {owner}/{repo}"
        return f"UNKNOWN {owner}/{repo} (GitHub answered {e.code})"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return f"UNKNOWN {owner}/{repo} ({type(e).__name__})"


def main() -> int:
    result = visibility(origin())
    print(result)
    return 1 if result.startswith("PUBLIC") else 0


if __name__ == "__main__":
    sys.exit(main())
