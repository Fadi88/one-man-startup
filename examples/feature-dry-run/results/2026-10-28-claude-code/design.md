# Design: RCPT-1, a receipt photo sorted into a spending category

Written by `architect`, 2026-10-28, from `spec.md`, `RCPT.md`, `agentic.md`, `feasibility.md`.
System map: `docs/architecture.md`. ADR: `docs/adr/0001-photo-read-without-keeping.md`.

## For Nadia

Your phone makes the photo smaller and sends it to our server. The server checks the free limits,
asks the AI to read it, and sends back the five boxes for you to check. Nothing is saved as a receipt
until you save. The photo itself is never kept after the read: it lives only in the server's memory for
the few seconds of the read. The figures it read are kept for at most a day so a dropped connection does not
lose them, and go at once if you throw the receipt away.

## Components touched

| Component | Responsibility in this feature |
|---|---|
| Web app | take or pick a photo, shrink it (RCPT-13), show the five fields for checking and correction (RCPT-2, RCPT-22), the month list (RCPT-18) |
| `POST /api/receipts/read` | caps (RCPT-12, RCPT-24), one AI read (`agentic.md`), validate, count (RCPT-11), return fields; stores no receipt |
| `POST /api/reads/discard` | forget a read the user threw away (RCPT-20) |
| `POST /api/receipts` | save a checked receipt once per idempotency key (RCPT-14) and once per read; `ai_category` from the signed token (RCPT-19, review D8, security S-1) |
| `PATCH /api/receipts/{id}`, `DELETE /api/receipts/{id}` | change category (RCPT-4) and fields; delete (RCPT-20); own receipts only (RCPT-10) |
| `GET /api/months/{yyyy-mm}` | the list and the totals per category and currency (RCPT-18), paginated |
| `lib/receipt-answer` (ticket T1) | turn the AI's raw answer into a checked result: schema, six categories, minor units, currency |

## Data

| Table.field | Owner | Notes |
|---|---|---|
| receipts.id, user_id | server | user_id from the session, never from the request (RCPT-10) |
| receipts.shop, spent_on, total_minor, currency | user (after checking) | currency ISO 4217; total integer minor units (RCPT-6) |
| receipts.category | user | one of six (RCPT-3, RCPT-4) |
| receipts.ai_category | server, written once | never shown (RCPT-19) |
| receipts.saved_at | server | RCPT-2 |
| ai_reads.user_id, feature, at, model, input_tokens, output_tokens, cost_micro_usd, outcome | server | one row per read, the single source for RCPT-11, RCPT-16 and RCPT-24; `feature` from a fixed set, today `receipt_read` (review D12) |
| idempotency_keys.key, user_id, request_hash, response, created_at | server | RCPT-14; 48 hours, but a read's record (it holds figures) goes on save, on discard, or after 24 hours (review D7) |
| receipts.read_nonce | server | unique; one save per read (review D8) |
| currencies.code, exponent | server | the one ISO 4217 table (review S5) |

**Retention and deletion.** The photo is not stored (ADR 0001): it is held in memory for the read
and dropped, which meets LAUNCH-6, RCPT-15 and RCPT-20 for photos. The read's figures live only in
its idempotency record and its signed `read_token` (held by the phone): deleted on save, on discard
(`POST /api/reads/discard`), or by the hourly cleanup job after 24 hours (RCPT-15). Every
idempotency record is deleted with the account (LAUNCH-9). Receipt figures are deleted on
the user's delete (RCPT-20) or with the account (LAUNCH-9). ai_reads keep no receipt content, only
counts and cost; they are kept with the account and deleted with it.

## Main flow

1. Permission given (LAUNCH-7, RCPT-23), else the read call is refused.
2. Phone shrinks the photo, sends it with an idempotency key.
3. Server: session, caps, then the AI call with a 30 s timeout; `lib/receipt-answer` checks the
   answer; one ai_reads row with the outcome.
4. The fields go back; the user corrects and saves; `POST /api/receipts` writes one row.

## Failure modes

As in `agentic.md` section 5, plus: database write fails on save: "We couldn't save it. Try
again?", nothing half written, the idempotency key lets the retry succeed once.

## When it breaks: the questions and the signals (`skills/observability/`)

1. **Is reading failing, and is it the provider or us?** Metric: reads per minute by outcome
   (ok, unreadable, provider_error, timeout, cap) and read duration p50, p95, p99, labelled by model.
2. **Is it costing more than planned?** Metric: cost per read from ai_reads, daily total against
   the LAUNCH-3 ceiling.
3. **Is saving or the month page failing?** Metric: rate, errors and duration p50, p95, p99 for
   save, change, delete, discard and month, by route; a counter of idempotent replays and of 409s.
4. **Why did this user's read fail?** Log: one structured event `receipt_read` with request_id,
   outcome, model, duration_ms, error_code; never the photo, shop, total or email.

## Access

Row-level security in Supabase on `receipts`, `ai_reads` and `idempotency_keys`, keyed on the
session user, as a second line behind the routes (security S-2).

## Not set yet

- **Speed targets** (`skills/performance/`: "Targets are the founder's rows"): no row sets how fast
  a read or the month page must be. The grilling did not ask. Raised in `p1-open-questions.md`;
  blocks release, not build.
