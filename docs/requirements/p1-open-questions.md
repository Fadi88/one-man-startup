# Open questions

What is waiting on the founder. Each entry is the question and the date raised, then its decision
card (`skills/founder-voice/`) as indented lines: Recommendation, Could go wrong, Undo, Blocks,
and two `Reply:` lines the founder can copy, the recommended one first. Remove an entry when it is
answered and move the answer to `p1-closed-decisions.md`. `tools/checks/card_check.py` checks
every entry (TPL-114).

- **Three improvements kept for later** (raised 2026-10-28). Offered by the orchestrator with
  the round that became TPL-74 to TPL-81; Fadi chose "later", not rejected: (3) run the setup
  dry run in Codex, Gemini CLI and Cursor to move TPL-15 off `U`; (4) repeat the setup dry run
  after TPL-39 to TPL-55 changed setup; (5) a check that a turned-down idea is recorded in
  `p1-rejected.md` the same day (rule 12).
  - Recommendation: 4 first, it is cheapest.
  - Could go wrong: while none is run, the setup changes since TPL-39 are untested end to end.
  - Undo: nothing to undo; a dry run works in a throwaway copy.
  - Blocks: nothing.
  - Reply: `run 4 now`
  - Reply: `keep all three for later`
- **A check that flags a stale ticket** (raised 2026-10-28). From the repository review Fadi
  pasted (its Proposal 2): a ticket records which rows and contract sections it was written
  from, and a check flags it when one changes later. Kept for later by Fadi.
  - Recommendation: build it once a project has run two features in parallel.
  - Could go wrong: until then, a ticket written before a row changed can be built as it was.
  - Undo: the check is one file; deleting it removes it.
  - Blocks: nothing.
  - Reply: `wait for two features in parallel`
  - Reply: `build it now`
