---
name: commit
description: Commit discipline - one change per commit, the founder as the only author, requirement ids in the subject, no tool or model credited, hooks never bypassed. Use whenever a commit is made.
---

# Commit

- **When:** each change as it finishes and the sweep is green, on the founder's go where they
  asked to see the change first (`skills/ordered-steps/`).
- **Author:** the founder from `project.toml [owner]`. Agents work for the founder; the history
  carries one name.
- **Subject:** the requirement ids, a colon, what changed: `AUTH-12, AUTH-13: email login with
  a magic link`. One subject, one change. If it needs "and", it may be two commits.
- **Body:** why, and what a reviewer should know. Nothing about the session, the tool or the
  model: no Co-authored-by, no "Generated with", no links to a chat.
- **Hooks:** `tools/githooks/commit-msg` refuses attribution lines, banned characters and the
  wrong author; `pre-commit` runs the sweep. If a hook refuses, fix the message or the code.
  Never `--no-verify`.
- **Push and merge** are outward steps: the founder's go each time.
