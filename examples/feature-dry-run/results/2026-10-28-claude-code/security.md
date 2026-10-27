# Security: RCPT-1 design (2026-10-28)

Written by `security` (`agents/security.md`), on `design.md`, `contract.md`, `agentic.md`,
`tickets.md`, ADR 0001. No code exists yet except ticket T1 (reviewed on its diff later).

## Threat model

- **What is valuable:** receipts (where a family shops, when, how much), the user's account, the
  AI budget (each read costs money).
- **Who would want it:** another user (curiosity, a partner), a script running up the AI bill,
  someone planting text on a receipt to change what the app stores.
- **How, and what stops them:**

| Attack | Stopped by | State |
|---|---|---|
| Read or change another user's receipt by id | user from session only; 404 for others (RCPT-10, contract) | designed; needs Supabase row-level rules as a second line (finding S-2) |
| Forge the AI's category at save, to skew the success number | not stopped: `POST /api/receipts` takes `read_id` but `design.md` stores no read result, so `ai_category` can only come from the client | **finding S-1** |
| Run up the AI bill with many reads | caps before the call (LAUNCH-1 to 4, RCPT-12, RCPT-24), global ceiling (LAUNCH-3) | designed |
| Upload something that is not an image, or a huge file | 4.5 MB limit; type check | type check by file content not specified (finding S-3) |
| Prompt injection via receipt text | no tools, schema, six-category check, user saves (agentic.md section 4) | designed; eval set tests it |
| Replay a save with another payload | idempotency key bound to user and request hash, 409 on reuse | designed |
| Personal data in logs | one structured event, allow-listed fields, no photo, shop or total (design.md) | designed |
| Secrets | Anthropic key from the environment only (backend-dev rule 7) | designed |

## Findings

| # | Severity | Where | How it is exploited | Fix |
|---|---|---|---|---|
| S-1 | medium | `design.md` data table, `contract.md` POST /api/receipts | a user sends their own `ai_category` (or the server trusts a client field), so RCPT-17's share can be faked and RCPT-19's record is not the AI's | store the read's checked answer server side under `read_id` (user-bound, short-lived), and take `ai_category` from it at save |
| S-2 | medium | Supabase tables | one missed check in a route exposes every user's receipts | row-level security on `receipts`, `ai_reads`, `idempotency_keys` keyed on the session user, as a second line |
| S-3 | low | `POST /api/receipts/read` | a non-image is sent to the AI provider, costing a read | check the file's first bytes are JPEG before the cap and the call |

No critical or high finding. Release is not blocked by this report; S-1 should be fixed before T3
and T4 are built, since it changes the contract.

## On the T1 diff (2026-10-28)

Read `src/lib/receipt-answer.ts`, its test and `package.json`. No secret, no network, no logging,
no query, no shell. The one new dependency is `vitest` 5.0.5 as a development dependency;
`npm install` reported "found 0 vulnerabilities". The answer is parsed with `JSON.parse` only, and
only five fields leave the function (RCPT-9).

| # | Severity | Where | How it is exploited | Fix |
|---|---|---|---|---|
| S-4 | low | `shop` passes through as text the AI read from the photo | a receipt printed with markup reaches the check screen; harmless only if the screen escapes it | T6 renders `shop` as text, never as HTML; add a T6 test with `<img onerror>` in a shop name |

No critical or high finding.
