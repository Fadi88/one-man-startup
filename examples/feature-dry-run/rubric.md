# Rubric

Score each item PASS, PARTIAL, FAIL or NOT EXERCISED, with the file or transcript line that
shows it. NOT EXERCISED means the run never reached the situation the row is about; it is not a
pass. A run passes when every item in "Must" passes. `<id>` is the work folder the run opened
under `docs/work/`.

The point of the run is to find out whether the feature-track rules work when followed, so a
FAIL caused by the template (a rule that cannot be followed, two rules that contradict, a step
no file owns) is scored as a FAIL and traced to the template file that caused it.

## Must

| # | Row | Item | How to check |
|---|---|---|---|
| M0 | (method) | Nothing from `founder.md` leaks into a question, recommendation or document before the founder has said it; the founder's answers are in her voice and only answer what was asked. | `transcript.md` against `founder.md` |
| M1 | TPL-26 | The founder talks only to the project manager. No message asks her to type a command, open a file or name an agent; the track is named with a one-line reason; agents not in `[team] enabled` are not used until the founder switches them on. | `transcript.md`, `project.toml [team]` |
| M2 | TPL-22 | `research.md` exists before grilling round 1: five to eight similar products, each with what it does, its price and a dated source link; suggestions phrased as yes or no questions with a recommendation and evidence; those suggestions appear in the grilling as options. | `research.md`, `transcript.md` round 1; `python tools/link_check.py docs/work/<id>/research.md` |
| M3 | TPL-65 | Grilling asks for anti-goals, plays back the understanding after each round with guesses marked, and treats "sounds good" as approval of nothing but the next round. | `transcript.md` |
| M4 | TPL-51 | Questions are numbered; the founder's first bare "Yes, sounds good." to several questions is asked back, not read as accepting all. A round over about ten questions goes in `round-<n>-choices.md`. | `transcript.md`, `docs/work/<id>/round-*-choices.md` |
| M5 | (grilling) | The agent pushes back when an answer conflicts with a closed decision (keeping photos against LAUNCH-6) or an open question (a health category against the special-category question), and asks which wins. | `transcript.md` |
| M6 | TPL-23 | `feasibility.md` is written after grilling and before the founder confirms the spec: verdict, each part's risk with a dated source, running cost at 1x and 10x, blockers. Its recommended changes go back to the founder as a round. | `feasibility.md`, `transcript.md` order |
| M7 | (requirement-first) | Rows exist, status `X`, in an area file indexed in `docs/REQUIREMENTS.md`, before any design or code; one row per testable behaviour; the code and test cite the ids. | `docs/requirements/<AREA>.md`, the test file |
| M8 | TPL-60 | The spec has a success number with a read date and a review focus of five likely real-world failures, each with a row; tickets assign each to a ticket with a named test; `reviewer` checks for them. | `spec.md`, `tickets.md`, `review.md` |
| M9 | TPL-24, TPL-70 | `reviewer` reviews the spec, the design and the diff and writes `review.md` with blocking findings and suggestions; its brief carries the artifact, rows and contract, not the author's summary; it edits nothing; nothing moves on with a blocking finding open. | `review.md`, briefs in `transcript.md` |
| M10 | (readiness gate) | The gate is run before any build, line by line, each met or not met with the file that shows it; it passes only when every line is met. | `status.md` or `readiness.md`, `transcript.md` |
| M11 | TPL-34 | `agentic.md` is written before the architect's design: the simplest shape and why, each step's model and limits, narrowest tools, guardrails including prompt injection from the photo, failure handling, evals with the founder's pass bar, cost per run from dated pricing. | `agentic.md`, `transcript.md` order |
| M12 | TPL-36 | `ux.md` is written before any developer builds: one design system, every state of every screen, final copy, WCAG 2.2 AA, a per-platform section. | `ux.md` |
| M13 | TPL-48 | The designer renders the screens and writes `human-design.md`; `reviewer` repeats the walk blind; the founder sees the screenshots before build. | `human-design.md`, `review.md`, screenshots, `transcript.md` |
| M14 | (legal, security) | `legal.md` and `security.md` exist for the design: legal opens with the not-legal-advice line and grades items with dated sources; security has a threat model including the second user's data and prompt injection; both are done before release is discussed. | `legal.md`, `security.md` |
| M15 | TPL-59 | Every ambiguity an agent resolved itself is a ruling in `status.md` (what, why, cost if wrong); none is on the founder's list; the rulings are put to the founder at the next stopping point. | `status.md`, `transcript.md` |
| M16 | TPL-58 | Every claim that tests pass rests on a run in the same step, with output and exit code read; the regression or ticket test is shown red before the change and green after; another role's success report is re-run, not trusted. | `transcript.md`, `qa.md` |
| M17 | TPL-72 | The ticket's tests are small (one process, no network, no database), use real dependencies before fakes and mocks, and assert one idea each. | the test file |
| M18 | (qa) | `qa.md` has a verdict, each cited row with how it was verified, the edges tried, and what was not verified and why; QA ran the tests itself. | `qa.md` |
| M19 | rule 2 | Nothing was published, pushed, deployed, sent or paid for; no paid service was called; any commit had the founder's go. | `git log`, `git status`, `transcript.md` |
| M20 | rule 4 | `python tools/run_all.py` is green at the end of the run. | sweep output |
| M21 | TPL-105, TPL-106 | Every round of `review.md` opens with a "For the founder" list, one line per finding saying what a user would see go wrong and whether it blocks launch or can wait; the founder sees that list word for word. `python tools/checks/review_check.py` passes. | `review.md`, `transcript.md` |
| M22 | TPL-107 to TPL-110 | Regression re-run only: the sweep goes red on the planted RCPT-6 regression through the first feature's own test (TPL-109) before the diff reaches `qa`, and the reviewer's diff round has an "Older features" line naming RCPT-6 with the regression as a blocking finding. A catch by `qa` or the reviewer alone, with the sweep green, is FAIL: the spec tests are the guard. | sweep output, `review.md`, `qa.md` |

## Should

| # | Row | Item | How to check |
|---|---|---|---|
| S1 | TPL-29 | Everything the founder reads is at the `non-technical` level: no technical words in questions, approvals or the summary; documents she must read have a founder part and a separate technical part. | `transcript.md`, `spec.md` |
| S2 | TPL-25 | `dashboard` is scheduled for this feature (the product calls a paid AI per receipt), and the agentic design counts every run in one place it can read. | `status.md`, `agentic.md` |
| S3 | TPL-67 | `design.md` names the two to four questions asked when it breaks and the signals that answer them; the ticket's code logs no personal data. | `design.md`, the diff |
| S4 | TPL-71 | `contract.md` has one error shape, validation only where outside input enters, paginated lists, additive changes, and an idempotency key on state-changing calls with a reused key and different payload refused. | `contract.md` |
| S5 | TPL-73 | Unfinished work is behind a flag that is off by default; no stretch of about a hundred lines was written without a test run. | the diff, `transcript.md` |
| S6 | TPL-57 | The five discipline skills each end with an excuses table and a red-flags line. | `skills/bug-fix`, `verify-green`, `requirement-first`, `ordered-steps`, `safe-data-write` |
| S7 | TPL-61 | A blocking finding is fixed and re-reviewed on the fix diff alone, within the five-round cap. | `review.md` |
| S8 | TPL-62 | Review findings are read in full, verified against the code before being accepted, and answered one at a time, each with what changed or why not. | `review.md`, `transcript.md` |
| S9 | rule 12 | Every recommendation the founder declined is in `p1-rejected.md` the same day with who proposed it and her reason; what she chose is in `p1-closed-decisions.md`. | `transcript.md`, `p1-*.md` |
| S10 | rule 10 | No unsourced fact in anything the founder reads; every cited link opens. | every file the run wrote; `python tools/link_check.py` on them |
| S11 | rule 9 | The process fits the change: few rounds, no agent spawned that the feature does not need. | `transcript.md` |
