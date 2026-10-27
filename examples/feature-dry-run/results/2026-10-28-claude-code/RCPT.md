# RCPT: a receipt photo sorted into a spending category

Rows for the first feature, from the grilling of 2026-10-28
(`docs/work/RCPT-1-receipt-category/spec.md`). All `X`: decided, not built. The free allowance
(LAUNCH-1 to LAUNCH-4), the AI only suggesting (LAUNCH-5), photo deletion (LAUNCH-6) and the
permission before the first read (LAUNCH-7) stay in `LAUNCH.md`; rows here cite them.

| ID | Requirement | Status |
|---|---|---|
| RCPT-1 | A signed-in user adds one receipt per photo, by taking a photo or choosing one from the phone's photos. | X |
| RCPT-2 | After a photo is read, the app shows the shop, the date, the total with the currency printed on the receipt, and one category, before anything is saved; the user saves or discards it. A saved receipt also keeps the date it was saved. | X |
| RCPT-3 | The category is one of exactly six: groceries, eating out, transport, household, kids, other. An answer from the AI that is not one of the six is stored as "other". | X |
| RCPT-4 | The user can change a receipt's category before saving and at any time after; the user's choice is the one every total counts (refines LAUNCH-5). | X |
| RCPT-5 | When a photo cannot be read (blurred, too dark, not a receipt, no total found), the app says so in plain words and offers a retake; nothing is saved and no category is shown. | X |
| RCPT-6 | Each amount keeps the currency printed on the receipt, as its ISO code, and is never converted; totals are per currency. A receipt with no currency printed, or only a symbol that names more than one currency ("$"), is saved only after the user picks one. Amounts are stored as whole minor units (fils, cents), never as fractional numbers. | X |
| RCPT-7 | Receipts printed in English, Arabic or German are read, including Arabic text written right to left and Eastern Arabic digits: on the eval set, the total is exact to the minor unit on at least 9 in 10 receipts in each language. | X |
| RCPT-8 | Before any user sees it, the AI step passes the eval set: at least 10 made-up receipts in each language of RCPT-7, and in each language at least 9 in 10 get the category that fits what was bought, hostile receipts included. | X |
| RCPT-9 | Text printed on a receipt is treated as data, never as instructions: for a hostile receipt, the shop, date and total read are the printed ones, the category is judged as in RCPT-8, and the saved receipt holds only the fields of RCPT-2 and RCPT-19. | X |
| RCPT-10 | A user sees, changes and deletes only their own receipts; a request for another user's receipt is answered as not found. | X |
| RCPT-11 | Every AI read is counted once, with its cost, per user, per feature and in total, in one place the founder's dashboard reads. | X |
| RCPT-12 | A free user's AI read passes the cap checks of LAUNCH-1 to LAUNCH-4 first; a read that fails (RCPT-5, RCPT-21) does not use up an allowance but counts against RCPT-24 when it is an unreadable photo (RCPT-5); when an allowance is used up, the user sees a plain message with what they can do, not an error. | X |
| RCPT-13 | The photo is shrunk on the phone to at most 2,576 pixels on its long edge before it is sent; a photo still over the upload limit set in `contract.md` (assumption A-13) is refused with a plain message. | X |
| RCPT-14 | The same save request sent twice (a double tap, a retry after a lost connection) stores one receipt, and the same photo sent twice by the phone's own retry is read and counted once, while a try-again the user asks for (RCPT-21) is a new read; a second photo of the same paper receipt is a new receipt. | X |
| RCPT-15 | A photo whose receipt was not saved or discarded is deleted 24 hours after it was sent. | X |
| RCPT-16 | If the average cost of one AI read over the eval set, from the RCPT-11 counter, is more than US$0.02, the founder is told before it ships. | X |
| RCPT-17 | Success: at least 8 in 10 receipts saved by real users keep the category the AI chose (RCPT-19; a change before or after saving counts as not kept), read four weeks after the first real user; the share is computed in one place. | X |
| RCPT-18 | For each calendar month, by the date printed on the receipt (or the date the user set, RCPT-22), the user sees the list of their saved receipts and a total per category, one total per currency and never summed across currencies, computed in one place on the server. | X |
| RCPT-19 | The category the AI chose is stored unchanged beside the user's category for every receipt; users never see it; only RCPT-17 reads it. | X |
| RCPT-20 | Discarding a receipt before saving, or deleting a saved one, deletes its photo and figures at once; the photo of an unreadable receipt (RCPT-5) is deleted at once. | X |
| RCPT-21 | When the AI provider fails, refuses or has not answered within 30 seconds, the user sees a plain message that the reading failed on our side, with a try-again; nothing is saved. | X |
| RCPT-22 | Before saving, the user can correct the shop, the date and the total, and fill any of them the AI did not find. | X |
| RCPT-23 | If the user declines the permission of LAUNCH-7, nothing is sent to the AI provider, the app says it cannot sort receipts without it, and the user can give permission later. | X |
| RCPT-24 | Each user has a daily cap on unreadable-photo reads (RCPT-5), separate from LAUNCH-1, checked before the read like LAUNCH-4; a provider failure (RCPT-21) does not count against it; when the cap is reached the user sees a plain message with what they can do; its number is set by the founder with the LAUNCH-1 to LAUNCH-3 numbers. | X |
| RCPT-25 | The month page's Largest Contentful Paint is 2.5 s or less on a phone, measured as `skills/performance/` describes. | X |
| RCPT-26 | The month page's Interaction to Next Paint is 200 ms or less, and its Cumulative Layout Shift 0.1 or less. | X |
| RCPT-27 | 95 in 100 receipt reads answer within 15 seconds, from the RCPT-11 duration metric. | X |
| RCPT-28 | Every screen of the feature is available in English, Arabic (right to left) and German, chosen from the phone's language. | X |
