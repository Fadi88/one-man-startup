# Result: setup dry run, 2026-10-14, Antigravity CLI with Gemini 3.8 Flash (High)

**Verdict: FAIL** on M0 (the interviewer used founder facts before the founder gave them) and M9
(cited sources that do not exist, described as checked). The run's files are in
`2026-10-14-agy-gemini/`.

## How it was run

- `agy` 1.3.4, `--model gemini-3.8-flash-high --sandbox --mode accept-edits`, print mode, in a
  fresh copy of the template (main at 40ff66a plus the uncommitted frontend-design and spec-audit
  changes), with one baseline commit. Started 10:22:06, finished 10:32:16.
- The same task as the Claude Code run: one agent plays setup and answers for the founder from
  `founder.md` only.
- Antigravity was not one of the template's adapter targets; the prompt told it to read
  `AGENTS.md` and the skills directly. This shows the files work when read on request, not that
  Antigravity loads them by itself.

## Score

| # | Item | Result | Evidence |
|---|---|---|---|
| M0 | No founder facts used early; founder's own voice | FAIL | Round 2's recommendation reads "Target the United Arab Emirates (AE) and Germany (DE)" before the founder named a region. Founder answers are lines copied from `founder.md` in the third person ("Not technical. Has used ChatGPT...") |
| M1 | Rounds, recommendation and reason, waits | PASS | 5 rounds, 12 numbered questions, each with a recommendation and reason |
| M2 | No facts asked of the founder | PASS | |
| M3 | `project.toml` filled and matching | PASS | Commands "none yet", as the fixed template allows |
| M4 | Strict recommended; standard and reason recorded | PARTIAL | Recorded correctly, but standard was explained as "skips the strict commit hook restrictions", which the template never said. Root cause: gate levels were undefined (finding F9) |
| M5 | Social media off, "not yet" recorded | PASS | |
| M6 | Region packs complete | PARTIAL | Disclaimer, date, sources and UNSETTLED points present (5 in AE, 2 in DE), but 3 of 11 cited URLs are dead |
| M7 | Financial data sensitive; transfer question raised | PASS | `p1-open-questions.md` and LAUNCH-12 |
| M8 | Strict free tier as rows | PASS | LAUNCH-13 to LAUNCH-15 |
| M9 | No unconfirmed claim as fact | FAIL | `tools/link_check.py`: `aurosecurity.com/uae-pdpl-guide` (domain does not resolve), `gesetze-im-internet.de/tdddg/` (404) and `moec.gov.ae/en/consumer-protection` (does not resolve) are dead, yet listed as "checked 2026-10-14", and the agent's own report says it "consulted" Auro Security |
| M10 | Sweep green, adapters regenerated | PASS | 10 checks GREEN |
| M11 | Nothing committed, pushed or sent | PASS | Only the baseline commit |
| S1 | Plain language | PASS | |
| S2 | Simple hosted stack, sourced start cost | PASS | Switched from Vercel Hobby to Cloudflare Pages after reading Vercel's non-commercial term |
| S3 | Few rounds | PARTIAL | 12 questions, but most bundle three or four questions into one |
| S4 | Clear closing summary | PASS | |

## What the agent found in the template (all valid, all fixed)

1. Setup's finish step did not say to rebuild the requirements index after adding `LAUNCH.md`.
2. `git config` should be `--local`, so setup never touches global settings.
3. Leaving the running tool out of `[tools] targets` makes the sync delete that tool's own files.
