# UX: adding a receipt (RCPT-1)

Written by `product-designer`, 2026-10-28, from `spec.md`, `RCPT.md`, `contract.md`,
`research.md` and `project.toml`. Design system: `docs/design/brand.md` (one system; the only
platform is a web app in phone browsers). Mockups: `docs/design/mockups/receipt.html`, rendered
to `docs/design/mockups/shots/receipt-screen-1.png` to `-7.png`.

## Made for these people (`skills/human-design/`)

- **Who, and in what moment:** a working parent at the kitchen table in the evening, with a few
  receipts from the day, a phone in one hand and the receipt in the other.
- **What this screen must make easy:** checking one number against the paper in two seconds and
  saving with one thumb.

## The flow

1. **First time only: permission** (screen 1, LAUNCH-7, RCPT-23). "Yes, send my receipts" or "Not
   now", two buttons of the same size and weight (review S2, legal). Not now: the add button opens
   this screen again with the same choice; nothing is sent. There is no Settings screen in this
   feature (review D3).
2. **Add:** "Add a receipt" (screen 5) opens the phone's own picker with "Take photo" and "Photo
   library" (the browser's file input with `accept="image/*"`; the system draws that sheet).
3. **Reading** (not drawn): the photo, dimmed, with "Reading your receipt..." and the button
   "Cancel". Over 30 seconds: screen 4.
4. **Check before saving** (screen 2, RCPT-2, RCPT-22): the total large, shop, date, the six
   categories with the AI's one selected. Tapping the total, shop or date opens it for editing.
   A field the AI did not find shows "Add the shop" (or date, total) in the alert colour, and
   "Save receipt" stays off until the total, the date and the currency are there; the
   shop may stay empty (review F1). No currency found or "$" only: a currency
   picker above the total, "Which currency is this?" (RCPT-6).
5. **Saved:** back to the month screen (screen 5) of the receipt's printed month, the new receipt
   in its place by date and highlighted for 4 seconds, with "Saved. Tap it to change the
   category." (review D6).
6. **A saved receipt** (screen 8): tap a row on the month screen. Shows the fields, the six
   categories, "Delete receipt". Changing the category or a field saves at once; "Back to October" (the receipt's month)
   returns to the list; delete asks, in the browser's own confirmation box, "Delete this receipt?
   This can't be undone."; its buttons carry the browser's own words (RCPT-4, RCPT-20,
   RCPT-22; review D5).
7. **Months:** the month screen has "Previous month" and "Next month" buttons beside the month
   name; the list is by printed date, newest first; the app opens on the current month.

## Every state

| Screen | State | What the user sees |
|---|---|---|
| Permission | first visit | screen 1 |
| Reading | loading | photo dimmed, "Reading your receipt...", Cancel |
| Reading | unreadable (RCPT-5) | screen 3 |
| Reading | our failure (RCPT-21) | screen 4 |
| Reading | free allowance used up (RCPT-12) | "You've used your free receipts for now. They come back on {resets_at, in the phone's own date format}." with "See plans" and "Not now" (the period is the founder's, LAUNCH-1; review D14) |
| Reading | failed-read limit (RCPT-24) | "That's a lot of photos we couldn't read today. You can try again on {resets_at, in the phone's own time}." |
| Reading | photo too large (RCPT-13) | "This photo is too large. Try taking it again." |
| Reading | offline | "You're offline. Try again when you're connected." Nothing is kept or queued (review D4) |
| Check | normal | screen 2; Arabic screen 6; dark screen 7 |
| Check | field missing | the field in the alert colour with "Add the ..." |
| Check | currency unknown or "$" only | "Which currency is this?" with dirham and euro first, then a searchable list of every currency in the server's table (RCPT-6; review S3) |
| Check | thrown away | the read is discarded on the server at once (`POST /api/reads/discard`), back to the month screen |
| Check | saving failed | "We couldn't save it. Try again?"; the same save is sent with the same key |
| Month | empty | "No receipts in October yet." and "Add a receipt" |
| Month | normal | screen 5 (and screen 9 for a category with two currencies, one line per currency) |
| Saved receipt | normal, delete confirm | screen 8; the confirmation is the phone's own box |
| Saved receipt | change or delete failed | "We couldn't save that change. Try again?" (or "delete"); the screen keeps what was there |
| Month | loading more | the list grows at the bottom with "Loading more receipts..." |

Drawn after review round 4: screens 8 (saved receipt), 9 (two currencies), 10 (empty month), 11
(free receipts used up), 12 (reading); dark and Arabic versions of screens 1, 3, 4 and 5
(screens 13 to 20), screen 2 at 200 percent text (screen 21), and dark and Arabic versions of
screens 8 to 12 (22 to 31). Not drawn: limit, too large,
offline, loading more (one heading and one line on screen 3's layout), and field missing and
saving failed (the field in the alert colour, or one line above Save, on screen 2's layout).

## Interface copy

Final for English, as in the table and the mockups. Arabic: screens 6, 17 to 20 and 27 to 31, written as
an Arabic speaker would say it, not word for word (review D2: "تجاهل" meant "ignore"; now
"لا تحفظه", "don't save it"). Not confirmed by a native speaker: assumption A-14.

**Not decided: the app's own languages.** The founder chose receipt languages (English, Arabic,
German), not the languages of the app's screens. Mockups show English and Arabic; a German
interface is not drawn. Raised in `p1-open-questions.md`: blocks the German launch, not the build.

## Accessibility (WCAG 2.2 AA)

- Contrast: every pair in `docs/design/brand.md` "Contrast pairs", checked by
  `python tools/checks/contrast_check.py` ("PASS 10 colour pairs meet their contrast minimum").
- The fields show "Edit" at their end, the total included, so they read as editable (review S1).
- Touch targets at least 44 by 44 px on buttons; the category chips are 44 px tall.
- Focus order: total, shop, date, categories, Save, Throw away. Visible focus ring in the accent.
- Screen reader: the selected category announced as "Groceries, selected"; the total read with its
  currency name.
- Text grows to 200 percent without cutting the total: the total wraps under the label.
- Reduced motion: the saved line appears without sliding.
- Right to left: Arabic screens mirror the layout; numbers keep their own direction.

## Per platform

The only platform is the web in phone browsers (`project.toml [stack] platform`). Where the
phone's conventions win: the photo picker is the system sheet, not ours; the back gesture on the
check screen asks "Throw away this receipt?"; the installable app uses the system's share and
back behaviour. Not confirmed from a fetched guideline page: how iOS Safari and Android Chrome
label the picker; `qa` checks it on a real device (`skills/verified-claims/`).

## For `legal`

Consent and disclosure moments: screen 1 (AI provider named, explicit choice, no pre-ticked
box, "Not now" a button of the same size and weight as yes, after review round 4). The AI's role is shown in screen 1 only; whether every
check screen must say the category was chosen by AI is for `legal`.

## Compared with three real products (`research.md`)

The pages read for `research.md` (ReceiptStorm, Receipta, Spendee) describe what the apps do but
show none of their check screens, so no comparison of screens is claimed. What is ours by intent:
the receipt's own currency shown first and one category choice on the same screen as the
figures, so checking is one look; the founder and `reviewer` judge it from the screenshots.
