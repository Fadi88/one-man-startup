# Contract: RCPT-1

Written by `architect`, 2026-10-28; revised the same day after review round 4 (D7 to D11, S5,
S6). The web app and the server build against this file in parallel; a change after they start is
a new hand-off. The user is always taken from the session, never from the request (RCPT-10).

## Rules for every call

- **One error shape:** `{ "error": { "code": string, "message": string, "details": object } }`,
  `message` in plain words the app may show. Every call can answer `401 not_signed_in`.
- **Validation only at this boundary**, by the field table below; inner code trusts checked values.
- **Lists are paginated:** `?cursor=<opaque>&limit=<1..100, default 50>`, answer
  `{ "items": [...], "next_cursor": string | null }`; a bad cursor is `400 invalid_cursor`.
- **Changes are additive:** a field is never removed or retyped; new fields are optional.
- **Idempotency:** every call that changes state (`POST`, `PATCH`, `DELETE`) needs
  `Idempotency-Key: <uuid>`, else `400 idempotency_key_missing`. The key is claimed atomically
  with the user id and a hash of the request; the same key and payload returns the first answer
  and changes nothing; the same key with a different payload is `409 idempotency_key_reused`.
  Keys are kept 48 hours, except a read's key, which holds receipt figures: it is deleted when its
  read is saved or discarded, and within 24 hours (the hourly job deletes records older than
  23 hours; RCPT-15, RCPT-20). A save whose read record is gone is refused
  (`400 invalid_read_token`).
- **Amounts:** every amount is `{ "minor": int, "currency": "ISO 4217", "exponent": int }`; the
  exponent comes from one table on the server (`skills/single-source/`); the app keeps none.

## Fields (validated on POST /api/receipts and PATCH)

| Field | Rule | `details.field` |
|---|---|---|
| shop | text, up to 120 characters after trimming; may be empty (a shop the AI did not find, RCPT-22) | `shop` |
| spent_on | `YYYY-MM-DD`, not more than one day after today in UTC; required at save (the month depends on it, ruling 3) | `spent_on` |
| total_minor | integer, 0 to 100,000,000; required at save; never null | `total_minor` |
| currency | a code in the server's ISO 4217 table; required at save; never null | `currency` |
| category | one of `groceries`, `eating_out`, `transport`, `household`, `kids`, `other` | `category` |

PATCH may change any field but may not set one to null. A failed rule is `400 invalid_field`.

## POST /api/receipts/read

Body: `multipart/form-data`, field `photo`; its first bytes must be JPEG (`400 not_a_photo`), at
most 4.5 MB (A-13). Reads, stores no receipt. The phone's own retry reuses the key and gets the
first answer without a second read (RCPT-14); a try-again the user asks for sends a new key.

200: `{ "read_token": string, "shop": string|null, "spent_on": string|null, "total": amount|null,
"currency": string|null, "category": string }`. When the currency is unknown, `total` carries
`minor` with `currency` and `exponent` null, and the app asks for the currency first (RCPT-6). `read_token` is signed by the server and holds the
user id, the AI's category, a single-use nonce and an expiry 24 hours ahead; the app cannot change
it without the signature failing.

Errors: `400 photo_missing`, `400 not_a_photo`, `413 photo_too_large` (RCPT-13), `403
ai_permission_missing` (RCPT-23), `422 unreadable` (RCPT-5), `429 allowance_used_up` and `429
failed_reads_used_up` (RCPT-12, RCPT-24; `details.resets_at`, an ISO time in UTC; the day ends at
midnight UTC), `502 provider_failed` (also an answer cut at the token limit) and `504
provider_timeout` (RCPT-21), and the idempotency errors.

## POST /api/reads/discard

Body: `{ "read_token" }`. 204. Deletes the read's idempotency record at once (RCPT-20). Errors:
`400 invalid_read_token`, the idempotency errors.

## POST /api/receipts

Body: `{ "read_token", "shop", "spent_on", "total_minor", "currency", "category" }` as checked and
corrected by the user (RCPT-22). The server takes `ai_category` from the verified token, never from
the body (RCPT-19); each token saves once (`409 read_already_saved`, by its nonce). 201: the
receipt. Errors: `400 invalid_field`, `400 invalid_read_token` (bad signature, another user,
expired), `409 read_already_saved`, the idempotency errors.

## PATCH /api/receipts/{id}

Body: any of the fields. 200: the receipt. Errors: `404 not_found` (also another user's receipt,
RCPT-10), `400 invalid_field`, the idempotency errors.

## DELETE /api/receipts/{id}

204; the figures are deleted at once (RCPT-20). Errors: `404 not_found`, the idempotency errors.

## GET /api/months/{yyyy-mm}

`{ "items": [receipt...], "next_cursor", "count": int, "totals": [ { "category", "total": amount } ] }`. Items by
printed date, newest first, then by saved time (ruling 3). `totals` and `count` cover the whole month, one
line per category and currency, and come on every page, computed on the server only (RCPT-18).
Errors: `400 invalid_month`, `400 invalid_cursor`.
