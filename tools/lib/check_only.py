"""TPL-42: the Claude Code hook for agents with `check` access. It lets through only the
template's checkers (and the mockup renderer, which writes only screenshots) and blocks every
other command.

Claude Code runs it before each Bash call of such an agent, with the call as JSON on stdin
(https://code.claude.com/docs/en/hooks-guide.md). Exit 2 blocks the call and shows the
message to the agent; exit 0 lets it run.
"""
from __future__ import annotations

import json
import re
import sys

# A checker, then plain arguments only: no ;, &, |, >, <, $, backticks or quotes to chain or redirect.
ALLOWED = re.compile(
    r"^(python3?|py)( -I)? tools/(link_check|run_all|repo_visibility|checks/[a-z_]+_check)\.py"
    r"( [A-Za-z0-9_./*:=-]+)*$"
)
# The mockup renderer writes screenshots and opens pages in a browser, so it may open only the
# project's own mockups, with only its TPL-92 flags (--dark, --rtl, --text-scale N).
RENDER = re.compile(r"^(python3?|py)( -I)? tools/render_mockups\.py"
                    r"( docs/design/mockups/[A-Za-z0-9_-]+\.html| --dark| --rtl| --text-scale [0-9]+(\.[0-9]+)?)*$")


def allowed(command: str) -> bool:
    command = command.strip()
    return bool(ALLOWED.match(command) or RENDER.match(command)) and ".." not in command


def main() -> int:
    try:
        command = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except (json.JSONDecodeError, AttributeError):
        command = ""
    if allowed(command):
        return 0
    print("Blocked: this agent may run only the template's checkers, such as "
          "`python tools/link_check.py <files>` or `python tools/run_all.py`.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
