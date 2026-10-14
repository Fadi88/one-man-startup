---
name: verify-green
description: Run what covers a change, then the full sweep, and end every round green - and who owns a red. Use before handing any work back, before any commit, and whenever a check fails.
---

# Verify, and end the round green

## Run

1. The narrow check for what you touched: the stack's test command (`project.toml [stack]
   test_command`) on the files you changed.
2. Before handing anything back: `python tools/run_all.py` and the full test command. Every time,
   whatever moved. A sweep is cheap next to a broken hand-off.

Exit codes of the sweep: `0` green, `2` red but every red is registered as known, `1` red.

## Who owns a red

- **A red your edit caused is yours.** Fix it before handing back. Never hand back red with a
  note promising to fix it later.
- **A red where real data disagrees with a document** (a metric under a target, a limit
  exceeded) is a decision about the business. Bring the founder the numbers and ask. Never move
  the threshold, loosen the check or rewrite the document on your own.
- **A red the founder decides to live with** goes in `tools/known_red.json`
  (`skills/known-reds/`), with their name, the date and a recheck date.

## Report

Say what you ran and what it said. "Tests pass" without the command and its output is not a
report. A check that was skipped is reported as skipped, with why.

## Never

- `--no-verify`, a skipped test, a commented-out assertion or a widened tolerance to get green.
