---
name: commit
description: Commit discipline - one change per commit, requirement ids in the subject, hooks never bypassed. Use whenever a commit is made.
---

# Commit

- **When:** each change as it finishes and the sweep is green, on the founder's go where they
  asked to see the change first (`skills/ordered-steps/`).
- **Subject:** the requirement ids, a colon, what changed: `AUTH-12, AUTH-13: email login with
  a magic link`. One subject, one change. If it needs "and", it may be two commits.
- **Body:** why, and what a reviewer should know.
- **Incomplete work** ships off by default behind a flag, so main stays releasable; turning the
  flag on, and later removing it, are their own commits.
- **Remove and replace** are two commits, never one.
- **Size:** about a hundred lines without a test run is a red flag. Stop and run.
- **Hooks:** `tools/githooks/commit-msg` refuses banned characters; `pre-commit` runs the
  sweep. If a hook refuses, fix the message or the code.
  Never `--no-verify`.
- **Push and merge** are outward steps: the founder's go each time.
