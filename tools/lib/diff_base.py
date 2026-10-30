"""TPL-121: what the diff-reading checks compare against.

Locally that is HEAD: the change not yet committed. In CI the checkout is clean, so a diff
against HEAD is empty and every diff-reading check would pass whatever was pushed. CI sets
CHECK_BASE to the commit the change started from (the pull request's base branch, or the commit
before a push), and the checks then read everything since it, committed or not. A commit or a
tool that skips the git hook (`--no-verify`, a tool without hooks) is caught there.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EMPTY = "0" * 40


def base() -> str:
    """The commit to diff against: CHECK_BASE when CI sets a usable one, else HEAD."""
    want = os.environ.get("CHECK_BASE", "").strip()
    if not want or want == EMPTY:
        return "HEAD"
    ok = subprocess.run(["git", "rev-parse", "--verify", "-q", f"{want}^{{commit}}"], cwd=ROOT,
                        capture_output=True, text=True)
    if ok.returncode != 0:
        # In CI a base that cannot be read would leave an empty diff and a quiet green.
        tag = "FAIL  TPL-121" if os.environ.get("GITHUB_ACTIONS") else "     "
        print(f"{tag} CHECK_BASE {want!r} is not a commit here; reading the diff against HEAD")
        return "HEAD"
    merge = subprocess.run(["git", "merge-base", want, "HEAD"], cwd=ROOT, capture_output=True, text=True)
    return merge.stdout.strip() or want
