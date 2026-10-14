# Result: setup dry run, 2026-10-14, Claude Code

**Verdict: PASS.** Every "Must" item passed except M9, which is partial (one unsourced line in
the transcript). The run's files are in `2026-10-14-claude-code/`.

## How it was run

- A fresh copy of the template (main at commit 1757c41 plus the uncommitted playbook changes of
  the same day), with one baseline commit and nothing else.
- One Claude Code agent, started with no memory of the template's design discussion, given
  `prompt.md`. It played the setup agent and answered for the founder only from `founder.md`.
- Limitation: one agent played both roles, so the founder's answers are not independent of the
  interviewer. A run with a real person is still needed (`docs/ASSUMPTIONS.md` A-7).

## Score

| # | Item | Result | Evidence |
|---|---|---|---|
| M1 | Rounds, recommendation and reason, waits | PASS | 5 rounds, 26 questions, each numbered with a recommendation and reason (`transcript.md`) |
| M2 | No facts asked of the founder | PASS | Region law and stack prices researched by the agent; the founder was asked for decisions only |
| M3 | `project.toml` filled and matching | PASS | No `unset` outside comments; values match `founder.md` |
| M4 | Strict recommended, standard recorded with reason | PASS | Recommended in rounds 1 and 2 with what it buys; `p1-closed-decisions.md` and `p1-rejected.md` quote the founder |
| M5 | Social media off, the "not yet" recorded (rule 13) | PASS | `[team] enabled`; `p1-rejected.md` |
| M6 | AE and DE packs complete | PASS | Disclaimer, "As of: 2026-10-14", sources, 13 and 8 UNSETTLED points |
| M7 | Financial data sensitive; transfer question raised | PASS | `sensitive` in `project.toml`; `p1-open-questions.md` "For legal: cross-border transfer" |
| M8 | Strict free tier as rows | PASS | LAUNCH-1 to LAUNCH-4, numbers left to the founder, "never on network address alone" |
| M9 | No unsourced claim as fact | PARTIAL | One line in the transcript's round 4 ("the agents build it well") is unsourced; not repeated in any output. Unreachable primary sources were labelled secondary or UNSETTLED rather than stated |
| M10 | Sweep green, adapters regenerated | PASS | `run_all.py`: 10 checks, GREEN |
| M11 | Nothing committed, pushed or sent | PASS | Only the baseline commit; changes uncommitted |
| S1 | Plain language | PASS | Terms explained in passing (what hosting, a database, a gate is) |
| S2 | Simple hosted stack with sourced start cost | PASS | Free-plan limits quoted from provider pages, dated; the "free while a prototype" point registered as an assumption |
| S3 | Few rounds | PARTIAL | 26 questions is a lot for a non-technical founder |
| S4 | Clear closing summary | PASS | Decided, open, next |

## Process note

The agent read the global git configuration of the machine once, outside the copy it was told
to stay in. It did not use the value. `prompt.md` now says not to read anything outside the copy.

## Findings and fixes

| # | Finding | Fix |
|---|---|---|
| F1 | The setup tree made Data wait for Market, though what data is held depends on the product. It cost a round. | Data now unlocks from Product and is asked with Market (`skills/setup/SKILL.md`). |
| F2 | Setup asked to quote each agent's "cost in time per feature", which nobody has measured (rule 11). | Setup now says what each agent does and when it is first needed, and quotes no time. |
| F3 | `project.toml` pointed to `docs/DECISIONS.md`, which does not exist. | Points to `docs/requirements/p1-closed-decisions.md`. |
| F4 | Dropping a tool target removed its generated folder but left `GEMINI.md` (and would leave `CLAUDE.md`). | `tools/sync_adapters.py` now removes generated pointer files for dropped targets. Tested in a scratch copy. |
| F5 | Test and build commands were required at the idea stage, before any code exists. | `"none yet"` is allowed until code exists. |
| F6 | The setup skill did not say where its requirement rows go. | `docs/requirements/LAUNCH.md`, prefix `LAUNCH`. |
| F7 | 26 questions for a non-technical founder. | Setup now asks for as few rounds as the dependencies allow, combines branches, and defers what the first feature does not need to `p1-open-questions.md`. To be measured on the next run. |
| F8 | `founder.md` had no answer for confirming the summary. | Added. |
