---
name: verify-green
description: Use when about to say that tests pass, that a fix works or that work is done; before any commit or hand-back; and whenever a check goes red or a red is tempting to silence.
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

Say what you ran and what it said, with the command and the last lines of its output. A claim
of green rests on a run **in the same turn as the claim**: an earlier run, a partial run or
"should pass" is not evidence, and neither is another agent's report of success; read their diff
and run the checks yourself. A check that was skipped is reported as skipped, with why; one that
could not run (no network, no credentials) is reported as not run, never as passed.

A regression test is proven three ways before it counts: it passes with the fix, fails with the
fix reverted, and passes again with it restored (`git stash` makes this a minute's work).

## Never

- `--no-verify`, a skipped test, a commented-out assertion or a widened tolerance to get green.

## When you catch yourself saying

| The excuse | The answer |
|---|---|
| "It should work now." | Run it. "Should" is the word before every broken hand-off. |
| "I ran it a few minutes ago." | Something moved since. Run it again, in this turn. |
| "The linter passed." | A linter runs no tests and builds nothing. Run the thing the claim is about. |
| "The agent said it succeeded." | An agent's report is a claim. Its diff and your run are evidence. |
| "A partial run is enough for this change." | The full sweep is cheap. The check you skipped is the one that catches it. |
| "I'll register it as a known red for now." | Only the founder adds a known red. Propose the entry and wait. |

Red flags: "should", "probably", "seems to"; committing or handing back before the run;
satisfaction before the output is read.
