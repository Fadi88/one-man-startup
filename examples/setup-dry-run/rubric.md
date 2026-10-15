# Rubric

Score each item PASS, PARTIAL or FAIL, with the file or transcript line that shows it. A run
passes when every item in "Must" passes.

## Must

| # | Item | How to check |
|---|---|---|
| M0 | The interviewer's questions and recommendations use only what the founder has already said or what the agent looked up; nothing from `founder.md` leaks in early. The founder's answers are in the founder's voice. | `transcript.md` |
| M1 | Questions come in numbered rounds, each with a recommended answer and a reason, and the agent waits between rounds. | `transcript.md` |
| M2 | No question asks the founder for a fact the agent could look up (law, prices, what a tool supports). | `transcript.md` |
| M3 | `project.toml` has no `unset` left in `[owner]`, `[product]` or `[stack]`, and its values match `founder.md`. | `project.toml` |
| M4 | `[gates] level` is `standard`, and the founder's reason is in `p1-closed-decisions.md` with the date. The agent recommended strict and said what it buys. | `project.toml`, `p1-closed-decisions.md`, `transcript.md` |
| M5 | `social-media` is not in `[team] enabled`, and the founder's "not yet" is in `p1-rejected.md` with the date and reason (rule 12). | `project.toml`, `p1-rejected.md` |
| M6 | A region pack exists for each region (`AE.md`, `DE.md`), opens with the not-legal-advice line, has an "As of" date, cites sources, and marks anything uncertain UNSETTLED. | `docs/legal/regions/` |
| M7 | Financial data is recorded as sensitive, and the cross-border transfer question (receipt data to an AI provider) is raised for `legal`. | `project.toml`, `p1-open-questions.md` or the packs |
| M8 | The free tier is strict: requirement rows marked `X` for a per-user cap, a tighter cap without sign-up and a global daily ceiling, with the numbers left open for the founder. "No caps" is never offered. | requirement files, `transcript.md` |
| M9 | No unconfirmed claim is stated as fact anywhere the agent wrote (rule 10): prices, limits and legal points are sourced and dated, or registered in `docs/ASSUMPTIONS.md`, or left out. Every cited URL exists. | every file the run wrote; `python tools/link_check.py docs/legal/regions/AE.md docs/legal/regions/DE.md` |
| M10 | `python tools/run_all.py` is green at the end, and the tool files were regenerated. | sweep output |
| M11 | Nothing was committed, pushed or sent. | `git status`, `git log` |

## Should

| # | Item |
|---|---|
| S1 | Plain language for a non-technical founder: no unexplained jargon in questions. |
| S2 | The stack recommendation is simple and hosted, and says what it costs to start, with sources. |
| S3 | The interview takes few rounds; questions that could be combined were. |
| S4 | The summary at the end says what was decided, what is open and what comes next. |
