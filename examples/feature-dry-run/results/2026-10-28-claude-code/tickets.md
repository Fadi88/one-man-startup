# Tickets: RCPT-1

Written by `architect`, 2026-10-28. Each ticket is buildable and testable alone. Builders:
`backend-dev`, `web-dev` (the stack has no phone or desktop app).

| Ticket | Builder | What | Rows | Blocked by | Named tests |
|---|---|---|---|---|---|
| T1 | backend-dev | `lib/receipt-answer`: turn the AI's raw text answer into a checked result or a typed failure; no network | RCPT-3, RCPT-5, RCPT-6, RCPT-9 | none | `receipt-answer.test.ts` (each review focus test named below, plus "drops a date more than a day in the future") |
| T2 | backend-dev | ai_reads table (with `feature`) and the one function that records a read and its cost; its rate, error and duration metrics | RCPT-11, RCPT-16 | none | `ai-reads.test.ts` "cost per user, per feature, in total" |
| T3 | backend-dev | `POST /api/receipts/read` and `POST /api/reads/discard`: caps, the AI call (behind the flag `receipt_ai_read`, off by default), T1, T2, the signed read token, the hourly cleanup, metrics | RCPT-12, RCPT-13, RCPT-14, RCPT-15, RCPT-20, RCPT-21, RCPT-23, RCPT-24, LAUNCH-4, LAUNCH-7 | T1, T2, LAUNCH-1 to 3 numbers for live use | `read.contract.test.ts` "same key read once, counted once", "stores nothing", "discard deletes the record", "record gone after 24 hours", "timeout", "provider error", "refusal", "cut answer is ours", "not a photo", "too large" |
| T4 | backend-dev | receipts table, save (AI category from the token, once per read), change, delete with idempotency; field rules; row-level security; metrics | RCPT-2, RCPT-4, RCPT-6, RCPT-10, RCPT-14, RCPT-19, RCPT-20 | none | `receipts.contract.test.ts` "same key twice", "reused key other payload", "other user's receipt is not found", "token saves once", "forged category ignored", "null total refused" |
| T5 | backend-dev | `GET /api/months/{yyyy-mm}`, totals per currency and category, and the RCPT-17 share | RCPT-17, RCPT-18 | T4 | `months.contract.test.ts` "count covers the whole month", `success-share.test.ts` |
| T6 | web-dev | add a receipt: permission, take or pick, shrink, check and correct, save or throw away; every state in `ux.md` | RCPT-1, RCPT-2, RCPT-5, RCPT-6, RCPT-13, RCPT-20, RCPT-21, RCPT-22, RCPT-23 | contract only | `add-receipt.spec.ts` "permission declined sends nothing", "photo shrunk to 2,576 px", "unreadable message", "our failure message", "currency picker", "fix the total", "throw away calls discard", "try-again sends a new key, automatic retry the same" |
| T7 | web-dev | the month screen and a saved receipt (change category, edit, delete) | RCPT-4, RCPT-18, RCPT-20, RCPT-22 | contract only | `month.spec.ts` "previous and next month", "two currencies in one category", "empty month"; `saved-receipt.spec.ts` "change category", "delete asks first" |
| T8 | agentic-workflow, qa | the eval set and its runner (experiment 1 first) | RCPT-7, RCPT-8, RCPT-9 | founder's API account and go | `evals/read-receipt.eval.ts` |

## Review focus, by ticket

| Item (spec "Review focus") | Ticket | Test |
|---|---|---|
| 1. The bad photo | T1 (unreadable answer), T3 (413, not a photo), T8 | `receipt-answer.test.ts` "treats readable false as unreadable", `read.contract.test.ts` "too large" |
| 2. Double tap and retry | T3, T4 | `receipts.contract.test.ts` "same key twice", "reused key other payload" |
| 3. Leaves halfway | T3 | `read.contract.test.ts` "stores nothing", "record gone after 24 hours" |
| 4. The Arabic receipt | T1 (Eastern Arabic digits in the total), T8 | `receipt-answer.test.ts` "reads a total written in Eastern Arabic digits" |
| 5. The receipt that gives orders | T1 (extra fields and off-list categories ignored), T4 (forged category), T8 | `receipt-answer.test.ts` "keeps only the five fields, whatever else the answer contains" |
| 6. The AI company down | T3 | `read.contract.test.ts` "timeout", "provider error", "refusal" |
| The second user | T4 | `receipts.contract.test.ts` "other user's receipt is not found" |
