# QA report: RCPT-1, ticket T1 (`lib/receipt-answer`)

Written by `qa`, 2026-10-28. Scope: ticket T1 only. Nothing is released; T2 to T8 are not built.

## For Nadia

The first small piece works as planned: it checks the AI's answer before anyone sees it, keeps it
to the six categories, refuses a total that makes no sense, and drops a date that doesn't exist.
I found two ways a correct receipt could still be refused or mis-sorted, depending on how the
next piece asks the AI; they are written down for that piece. Nothing is live and nothing needs
you now.

**Verdict: PASS WITH KNOWN ISSUES** (two, both for T3, below).

## Rows

| Row | How verified | Result |
|---|---|---|
| RCPT-3 | named tests "keeps a category from the list", "stores an off-list category as other" | pass |
| RCPT-5 | named tests "treats readable false as unreadable", "...text that is not JSON...", "...JSON that is not an object...", "...a missing total..." | pass |
| RCPT-6 | named tests on fractional, negative and Eastern Arabic totals, currency case, "$" | pass (the save-side rules belong to T4) |
| RCPT-9 | named test "keeps only the five fields, whatever else the answer contains" | pass for the field allow-list; the prompt's resistance is T8's eval |

The rows stay `X` in `RCPT.md`: T1 covers their parsing part only, and each row also needs T3,
T4, T6 or T8 before a test asserts all of it (`skills/requirement-first/`).

## Runs (by qa, this turn)

- `npm test`: exit 0, "Test Files 1 passed (1)", "Tests 18 passed (18)".
- `python tools/run_all.py`: exit 0, "12 checks, 0 SKIP lines", GREEN.
- `python tools/checks/floor_check.py`: "PASS floor holds: 8 samples caught, 5 clean ones passed".
- Seen fail then pass (from the transcript, re-run by qa where marked): T1-B1's test red with the
  fix reverted ("2 failed | 16 passed (18)") and green restored; the "not an object" test red
  with its check removed, re-run by qa: exit 1, "1 failed | 17 passed (18)", then green.

## Edges tried (a probe script outside the suite, `node`, made-up answers)

| Input | Result | Judgement |
|---|---|---|
| total "99999999999999999999" | unreadable | right (not a safe integer) |
| total "143,75" | unreadable | right per RCPT-6 (minor units only) |
| total "" | unreadable | right |
| total 0 | accepted | allowed by the contract (0 to 100,000,000) |
| currency "aed " (trailing space) | currency null, the user picks | acceptable; one extra tap |
| date "2026-10-24T10:00" | date null, the user fills it | acceptable |
| shop 42 (a number) | shop null | right |
| readable "true" (a string) | unreadable | right per schema |
| category "Groceries" (capital G) | **other** | **known issue 1** |
| the whole answer wrapped in a ```json fence | **unreadable** | **known issue 2** |

## Known issues

1. **A category in other capitals is filed as "other".** Steps: answer with `"category":
   "Groceries"`. The AI's category is lost, the success share (RCPT-17) drops, and the user must
   fix it. For `agentic-workflow` and T3: ask the API for structured output that enforces the
   schema, or match the six case-insensitively in T1; the eval set (T8) counts it either way.
2. **An answer wrapped in a code fence is treated as an unreadable photo.** Steps: send
   "```json" + a correct answer + "```". The user is told the photo can't be read, and the read
   counts against their failed-read cap (RCPT-24), although the photo was fine. Models often
   wrap JSON this way unless the request forces structured output (not verified for the chosen
   model: no paid call was made). For T3: a test "fenced answer" with the chosen request shape;
   if T3 cannot rule it out, T1 strips one surrounding fence. Not a failing test in the suite now,
   because which side fixes it is T3's design choice and a deliberately failing or skipped test
   is refused by the floor check.

## Not verified, and why

- How the real model answers (fences, capitals, refusals): no API account, no paid call (founder:
  "Not yet").
- A type check: `typescript` is not installed and the stack has no type-check command yet.
- Anything on a phone or browser: T6 and T7 are not built.
- The performance scorecard (`skills/performance/`): no page exists yet.

## Known reds touched

None (`tools/known_red.json` unchanged).
