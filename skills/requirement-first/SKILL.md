---
name: requirement-first
description: How requirement rows are written, numbered, statused and cited - the row comes before the code. Use before any change to code, copy or config, and whenever a requirement id is mentioned.
---

# Requirement first

A row written before the code decides the design. A row written after only records whatever the
design drifted into. So the row comes first, even for a two-line fix.

## The row

`| ID | What must be true, in one or two sentences a tester can check | STATUS |`

- **ID** is `AREA-N`: a short area prefix and a number. Ids are never reused or renumbered. To
  slot a row between two others, add a letter: `AUTH-12a`.
- One file per area under `docs/requirements/`, listed in `docs/REQUIREMENTS.md` with its prefix.
- A new area needs a new file and an index line; run `python tools/run_all.py` to check both.

## Status letters

| Letter | Means |
|---|---|
| T | A named test asserts it. The test file names the id. |
| M | Seen working by a person, nothing automatic guards it. |
| U | Built, never run. |
| X | Decided, not built yet. |
| n/a | A standing decision not to build, or `Covered by <ID>.`, a duplicate of another row. |

Rows move X, U, M, T. A row only goes backwards by being rewritten, with the reason in
`docs/HISTORY.md`. `X` and `n/a` look alike; `p1-closed-decisions.md` says which, unless the row reads
"Covered by <ID>."

## Duplicates

When two rows specify the same behaviour, the one in the area that owns it stays. The other is
rewritten as "Covered by <ID>." with status `n/a`, never deleted, so its id still resolves.

## Citing

Code, tests and commits cite the ids they satisfy (`AUTH-12` in a test name or comment, in the
commit subject). The sweep fails on a cited id with no row.

## Not a requirement

An answer to a question is not a requirement. Do not turn a chat answer into a row unless it
shows an existing row is wrong; then fix that row in the same change.
