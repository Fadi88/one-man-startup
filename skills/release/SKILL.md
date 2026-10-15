---
name: release
description: The release checklist - QA pass, reviews in, rollback written, backup tested, then merge, migrate, deploy and announce, each on the founder's go - and the watch after. Use for every release to users.
user_only: true
---

# Release

Run in order. Any line not met stops the release.

## Before

1. `docs/work/<id>/qa.md` says PASS or PASS WITH KNOWN ISSUES, and the founder has read the issues.
2. `security.md` has no open critical or high; `legal` has no RED on the launch path.
3. If the product has a free tier or trial, every cap row is `T`: a test proves each per-user,
   per-device and global limit holds.
4. `python tools/run_all.py` green on the release commit; CI green on the same commit.
5. Release notes written in `docs/work/<id>/release.md`: what users will notice, in their words.
6. **Rollback written down:** the exact steps and how long they take. If a migration cannot be
   reversed, say so and get the founder's explicit acceptance.
7. Backup taken and a restore of it tried, this session.

## Steps, each on its own go (`skills/ordered-steps/`)

1. Merge to main.
2. Run migrations.
3. Deploy.
4. Smoke test production: the main flow end to end, as a user.
5. Announce.

## After

Watch errors and the feature's success number for the window set in the spec. On a major
error, `qa` writes ROLLBACK and the orchestrator starts `rollback`: roll back first (on the
founder's go) and investigate second, with `debugger`. Write a short entry in `docs/HISTORY.md`.
