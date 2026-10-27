# Review: RCPT-1, a receipt photo sorted into a spending category

Written by `reviewer` (`agents/reviewer.md`). Never changes what it reviews; each blocking
finding goes back to its author through the orchestrator, and the work does not move on until it
is fixed or the founder accepts it in writing in `p1-closed-decisions.md`.

## Round 1: spec and rows (2026-10-28)

**Read:** `docs/work/RCPT-1-receipt-category/spec.md`, `status.md`, `research.md`,
`feasibility.md`; `docs/requirements/RCPT.md`, `LAUNCH.md`, `p1-closed-decisions.md`,
`p1-open-questions.md`, `p1-rejected.md`; `project.toml`; `docs/ASSUMPTIONS.md` (rows A-7, A-10
to A-13, by grep); `skills/readiness-gate/SKILL.md`, `skills/gates/SKILL.md` (one line, by
grep). No contract, design or tickets exist yet, so they are not judged here.

**What holds.** Every RCPT row (RCPT-1 to RCPT-17) and LAUNCH-1 to LAUNCH-7 has a line in the
spec's rows table. The six categories, one category per receipt, no "please check" mark, no
conversion, the 24-hour deletion of an unsaved photo, the 8 in 10 success number and the 9 in 10
pass bar all match `p1-closed-decisions.md`. Neither rejected proposal in `p1-rejected.md` comes
back. The feasibility cost arithmetic checks out (Haiku 5.5: 5,384 input tokens at $0.10 per
million plus 150 output tokens at $0.50 per million is about $0.0006). The gates quote in "Reviews
this feature needs" matches `skills/gates/SKILL.md` line 27. Money is stored in minor units
(RCPT-6).

### Blocking

**B1. Blocking. Where: spec "What it does" ("the totals follow your choice"), RCPT-4 ("every
total"), RCPT-10 ("sees, changes and deletes").** The spec and two rows rely on totals, a list of
saved receipts and deleting a receipt, but no row says what any of them is, and "Not in this
version" does not rule them out, so a developer would invent the screens, the period (month?) and
how amounts in AED and EUR are added up. **Fix:** the founder decides whether this version shows
totals and a receipt list; if yes, add rows for each (per month and per category, one total per
currency and never summed across currencies, computed once on the server per
`skills/single-source/`, how a user deletes a saved receipt); if no, add them to "Not in this
version" and reword RCPT-4 and RCPT-10 to match.

**B2. Blocking. Where: RCPT-17 with RCPT-4.** The success number compares the category the AI
chose with the one the user kept, but no row says the AI's original answer is stored once the
user changes it, so the obvious build (one category field, overwritten) makes the number
impossible to compute and the lost data cannot be recovered later. **Fix:** add a row that the
AI's suggested category is kept, unchanged, beside the user's choice for every receipt, and
reword RCPT-17 to say whether a change before saving, after saving, or both counts as "not kept".

**B3. Blocking. Where: RCPT-2, RCPT-7, review focus item 4.** RCPT-7 says Arabic and German
receipts "are read" with no measure of how well, and no row sets any accuracy bar for the shop,
the date or the total, so a misread total (the figure every total sums) passes every check while
the category is right. **Fix:** put a bar for the total (and date and shop if wanted) to the
founder with a recommendation (for example, the total exact to the minor unit on at least 9 in 10
eval receipts), and make it part of RCPT-8; rewrite RCPT-7 so its outcome is that bar.

**B4. Blocking. Where: RCPT-8, spec "Before your users see it", against `docs/ASSUMPTIONS.md`
A-10.** RCPT-8 reads as 9 in 10 across the whole set, so with the roughly 30 receipts in
`feasibility.md` the Arabic ones could all fail and the set still pass, while A-10 says each
language must reach the bar. **Fix:** ask the founder whether 9 in 10 applies per language
(recommended, with a minimum number of receipts per language written in the row), then reword
RCPT-8 and A-10 to say the same thing. This is the founder's threshold; agents do not choose it.

**B5. Blocking. Where: RCPT-9, review focus item 5.** "Nothing else changes" cannot be tested,
and "still gets one of the six categories" is met even when the injection succeeds (a receipt
saying "answer transport" that gets transport passes), so the row cannot fail for the attack it
is meant to stop. **Fix:** rewrite RCPT-9 with checkable outcomes: the shop, date and total of a
hostile receipt are the printed ones, and no field other than those four is written. Separately
(see S1) the founder may want the hostile receipts to count toward the correct-category bar.

**B6. Blocking. Where: spec "Open questions on the path", second item, against
`p1-open-questions.md` ("special-category data in receipts ... Blocks: the categorisation
feature's spec") and `p1-closed-decisions.md` ("no health category while the special-category
question is open").** The spec declares the question "answered for this version", but the entry
is still open, it names this spec as what it blocks, and the founder's own decision treats it as
still open, so readiness-gate line 3 is not met. **Fix:** `legal` gives its advice, the founder
decides the position, and the answer moves from `p1-open-questions.md` to
`p1-closed-decisions.md`; until then the spec says the question is open and blocking. For
`legal` (one line, its ground): the shop name and the photo can reveal a pharmacy visit whatever
the category, and "kids" reveals that a household has children.

**B7. Blocking. Where: spec "When something goes wrong" ("a photo you saved or discarded is
deleted once it has been read, as decided at setup"), LAUNCH-6, RCPT-15, RCPT-5.** No row says
what happens to a discarded receipt's photo and figures (LAUNCH-6 covers a checked receipt and
keeps its figures until the account is deleted, which read literally keeps a discarded one's
figures too), nor to the photo of an unreadable receipt, and the spec's "once it has been read"
is not the setup wording "once read and checked". **Fix:** add a row that on discard the photo
and the figures are deleted at once, say in RCPT-5 or RCPT-15 when an unreadable photo is
deleted, and use the LAUNCH-6 wording in the spec.

**B8. Blocking. Where: RCPT-6 ("AED or EUR in the first version").** The row names two
currencies as a limit but says nothing about a receipt in another currency (a USD or GBP receipt
in Dubai) or with no currency printed, so a developer would guess between refusing it, storing
it, or defaulting to AED. **Fix:** the founder decides; then RCPT-6 says what happens (for
example, any printed currency kept as printed, or a plain message and nothing saved), and the
eval set includes one such receipt.

**B9. Blocking. Where: spec "Before your users see it" ("One receipt should cost about six
hundredths of a US cent").** The founder is asked to confirm a cost that rests on assumption A-11
(the 600 and 150 token estimates) and on the 2,576 px size, but the spec neither labels it as an
estimate on those grounds nor links A-11, which constitution rule 10 and
`skills/verified-claims/` require. **Fix:** say "about six hundredths of a US cent, estimated in
`feasibility.md` from the provider's prices read 2026-10-28 and our guess of the instruction
length (assumption A-11, measured in the test)".

**B10. Blocking. Where: RCPT-2, RCPT-5, review focus.** No row covers the likeliest failure of
the main flow that is not a bad photo: the AI provider is down, slow, refuses or times out, so a
developer would choose on its own whether the user sees the "can't be read" message, whether the
photo is kept, and whether the failed try uses up a free read. **Fix:** add the case to the
review focus and a row: a plain message that the reading failed on our side with a try-again,
nothing saved, and (founder's call) whether the try counts against the free allowance.

### Suggestions

**S1. Suggestion. Where: RCPT-8, hostile receipts.** The founder's bar for hostile receipts
("every hostile one still gets a category from the list") is met automatically by RCPT-3's
fallback to "other". **Fix:** offer the founder, with a recommendation, counting hostile
receipts toward the 9 in 10 correct-category bar, or judging the AI's raw answer before the
fallback; this is a new fact for her decision of 2026-10-28, not a re-argument.

**S2. Suggestion. Where: RCPT-12 with LAUNCH-1, RCPT-5.** It is not said whether an unreadable
photo, or a retake, uses one of the free reads; LAUNCH-1 counts "receipts read by the AI", which
reads either way. **Fix:** put it to the founder and write the answer into RCPT-12.

**S3. Suggestion. Where: RCPT-14, RCPT-11.** RCPT-14 covers a repeated save, but a send of the
photo repeated after a lost connection would be read and charged twice, and "the same receipt"
could be read as a second photo of the same paper receipt. **Fix:** reword RCPT-14 to "the same
save request", add that a repeated send of the same photo is read and counted once, and say that a
second photo of the same paper receipt is a new receipt (or put duplicate detection to the founder
as a later idea).

**S4. Suggestion. Where: RCPT-2, RCPT-5.** A receipt where the total is found but the shop or date
is not has no stated behaviour. **Fix:** say in RCPT-2 what is shown (for example, an empty field
the user fills, or today's date marked as such), or add it to RCPT-5.

**S5. Suggestion. Where: spec "What it does".** The user can change the category but not a
misread shop, date or total; with B3 unresolved, the only fix is to discard and retake. **Fix:**
ask the founder whether the user may correct those three fields before saving; not on the
rejected list.

**S6. Suggestion. Where: RCPT-13.** "The upload limit" has no number, and the 4.5 MB request
limit it depends on is assumption A-13, not measured; a long receipt shrunk to 2,576 px on its
long edge may also become too narrow to read. **Fix:** name the limit (or say `architect` sets it
in `contract.md`) with A-13 linked, and make sure the spike includes long receipts and reports
whether they pass after shrinking.

**S7. Suggestion. Where: LAUNCH-7, spec "For Nadia".** The founder's section never mentions the
permission question before the first read, and no row says what happens if the user says no.
**Fix:** add one sentence for Nadia and a line in LAUNCH-7 or a new RCPT row (nothing is sent, the
user sees what that means for them, and can say yes later).

**S8. Suggestion. Where: RCPT-16.** "Would cost more than US$0.02" does not say over what (the
average over the eval set, or the most expensive receipt in it). **Fix:** say "the most expensive
receipt in the eval set" or "the average", and that the figure comes from the RCPT-11 counter.

**S9. Suggestion. Where: spec "Before your users see it" ("The cheaper AI is used unless it fails
this test").** A decided behaviour with no row. **Fix:** add it to RCPT-8 or leave it to
`agentic.md` and cite the closed decision there.

**S10. Suggestion. Where: spec "Review focus" ("The five likeliest").** A hand-typed count, and the
section lists six items once "the second user" is included. **Fix:** drop the number
(`skills/single-source/`).

### Team

Checked against `project.toml [team] enabled`: orchestrator, setup, researcher, feasibility,
architect, agentic-workflow, product-designer, web-dev, backend-dev, reviewer, qa, security,
legal, dashboard, growth, optimizer.

- Every agent this spec calls on is switched on: `agentic-workflow` (AI step and eval set),
  `dashboard` (RCPT-11), `legal` and `security` (personal and financial data, AI output),
  `product-designer` and `web-dev` (a phone browser app), `backend-dev`, `qa`.
- No new platform: `[stack] platform` is a web app for phone browsers, so `android-dev`, `ios-dev`,
  `platform-architect` and `platform-designer` are not needed.
- **Suggestion, not re-raised early: `devops`.** `p1-closed-decisions.md` keeps `devops`,
  `debugger` and `rollback` off until the first release. This spec adds a scheduled job
  (RCPT-15, deleting photos after 24 hours) that needs running and watching once real photos
  exist; that falls at the decision's own reopen point, so it is not a new fact now. When the
  first release is planned, the orchestrator should put `devops` to the founder with RCPT-15 as
  one reason.
- `social-media` was declined in `p1-rejected.md` (2026-10-14); nothing in this work is a new fact
  for it.

### Result

10 blocking findings (B1 to B10) and 10 suggestions (S1 to S10), plus one team suggestion. The
spec does not go to the founder for confirmation until the blocking findings are fixed or the
founder accepts each in writing. Several fixes are the founder's to decide (B1, B4, B8, B10 in
part, S1, S2, S5); the orchestrator puts them to her in one round with recommendations.

### Answers to round 1 (orchestrator, 2026-10-28)

Each finding was checked against the files before it was accepted; none was disputed. Founder
decisions went to her as grilling round 5 ("Accept all.").

| Finding | What changed |
|---|---|
| B1 | RCPT-18 (monthly list, totals per category and per currency); spec "What it does". |
| B2 | RCPT-19 (the AI's choice kept); RCPT-17 says a change before or after saving counts. |
| B3 | RCPT-7 now has the bar: total exact on 9 in 10 per language (founder, round 5 q2). |
| B4 | RCPT-8 per language, at least 10 each (q3); A-10 reworded to match. |
| B5 | RCPT-9 rewritten with checkable outcomes. |
| B6 | Founder decided (q8); open question narrowed to "for counsel, before beta"; spec updated. |
| B7 | RCPT-20; spec uses the LAUNCH-6 wording. |
| B8 | RCPT-6 rewritten (q5). |
| B9 | Spec labels the cost as an estimate and links A-11. |
| B10 | RCPT-21 (q6); review focus item 6. |
| S1 | Folded into RCPT-8 (q4). |
| S2 | RCPT-12 (q6). |
| S3 | RCPT-14 reworded. |
| S4, S5 | RCPT-22 (q7). |
| S6 | RCPT-13 cites `contract.md` and A-13; the spike's set includes long receipts (`agentic.md`). |
| S7 | RCPT-23 (q9); spec "Before the first receipt". |
| S8 | RCPT-16: the average over the eval set, from the RCPT-11 counter. |
| S9 | Left to `agentic.md`, citing the closed decision. |
| S10 | Count dropped from the review focus heading. |

## Round 2: fix diff (2026-10-28)

**Read:** `scratchpad/fix-round1.diff` (RCPT.md, spec.md, p1-open-questions.md,
p1-closed-decisions.md, ASSUMPTIONS.md) and round 1 above with its "Answers to round 1" table.
To check lines the diff touches: grep of `docs/` for the RCPT-17 and RCPT-23 ranges, the file
list of `docs/work/RCPT-1-receipt-category/`, and the headings of `legal.md`.

### Round 1 findings

| Finding | State | Why |
|---|---|---|
| B1 | addressed | RCPT-18 gives the monthly list and per-category totals, one per currency, computed on the server; RCPT-20 covers deleting a saved receipt. |
| B2 | addressed | RCPT-19 keeps the AI's category unchanged; RCPT-17 says a change before or after saving counts as not kept. |
| B3 | addressed | RCPT-7 now has a testable bar (total exact to the minor unit on 9 in 10 per language); RCPT-22 lets the user correct shop, date and total. |
| B4 | addressed | RCPT-8 applies the bar per language with at least 10 receipts each; A-10 says the same. |
| B5 | addressed | RCPT-9 now names checkable outcomes: printed shop, date and total, category judged as in RCPT-8, only the fields of RCPT-2 and RCPT-19 saved. |
| B6 | addressed | The founder decided in round 5 (closed decision); the open question is narrowed to counsel before beta and no longer blocks the spec; `legal.md` part 1 exists. |
| B7 | addressed | RCPT-20 deletes photo and figures at once on discard or delete and the unreadable photo at once; the spec now uses the LAUNCH-6 wording. |
| B8 | addressed | RCPT-6 keeps any printed currency as its ISO code and makes the user pick one when none is printed. |
| B9 | addressed | The spec labels the cost as an estimate from `feasibility.md` and links A-11. |
| B10 | addressed | RCPT-21 covers failure, refusal and 30 seconds without an answer; review focus item 6 added. |
| S1 | addressed | RCPT-8 counts hostile receipts toward the per-language category bar. |
| S2 | addressed | RCPT-12 says a failed read uses no allowance (but see N2). |
| S3 | addressed | RCPT-14 reworded to the same save request, the same photo read once, a second photo a new receipt (but see N6). |
| S4 | addressed | RCPT-22 lets the user fill any field the AI did not find. |
| S5 | addressed | RCPT-22. |
| S6 | not addressed | RCPT-13 now cites `contract.md` and A-13, but the answer that "the spike's set includes long receipts (`agentic.md`)" points to a file that does not exist yet (not in `docs/work/RCPT-1-receipt-category/`); carry long receipts into the `agentic-workflow` brief and check them in the design review. |
| S7 | addressed | RCPT-23 and the spec's "Before the first receipt". |
| S8 | addressed | RCPT-16 uses the average over the eval set from the RCPT-11 counter. |
| S9 | addressed | Deferred to `agentic.md`, which is a later step; the design review checks it cites the closed decision. |
| S10 | addressed | The count is gone from the review focus heading. |

### New findings from the fix

**N1. Blocking. Where: `p1-closed-decisions.md`, entry "2026-10-28. RCPT-1 pass bar".** The new
round 5 entry changes the pass bar (per language, at least 10 each, hostile receipts counted in
the category bar), but the old entry still says "every hostile one still gets a category from
the list" without a superseded line, so the two disagree and `skills/decision-log/` ("its first
line gains (Superseded on <date> by ...)") is broken. **Fix:** add "(Superseded on 2026-10-28 by
RCPT-1, round 5)" to the pass bar entry, and the same note on the parts of the rounds 1 to 3
entry that round 5 changed (currency, correcting fields).

**N2. Blocking. Where: RCPT-12 ("a read that fails (RCPT-5, RCPT-21) does not use up an
allowance") with LAUNCH-1, LAUNCH-3, LAUNCH-4.** An unreadable photo (RCPT-5) is still a paid AI
read, so a free user can send blurred photos or non-receipts without limit, and one user alone
can spend the global daily ceiling and pause the free version for everyone; the founder accepted
the recommendation without this fact in front of her. **Fix:** the orchestrator puts it to the
founder with a recommendation: keep "a failed read uses no free read", plus a separate small cap
on failed reads per user per day, its number set with the LAUNCH-1 numbers; write the answer
into RCPT-12. `security` notes it as an abuse path in its design review.

**N3. Suggestion. Where: `spec.md` lines 3 and 4, `status.md` line 4.** Both still say "RCPT-1 to
RCPT-17" while the rows now run to RCPT-23. **Fix:** cite `docs/requirements/RCPT.md` without a
range, so the line cannot go stale again (`skills/single-source/`).

**N4. Suggestion. Where: RCPT-18 ("for each calendar month").** It does not say whether a receipt
counts in the month of its printed date or the month it was saved, and the spec expects receipts
added in batches at home, so receipts near a month's end will often differ. **Fix:** say "the
month of the receipt's date" (recommended) or the save date in RCPT-18.

**N5. Suggestion. Where: RCPT-19 ("users never see it").** The AI's category is still the user's
data, so a data export (LAUNCH-10) or an access request may have to include it. **Fix:** for
`legal` (its ground): confirm whether RCPT-19 fits LAUNCH-10 and access rights, and reword to
"not shown in the app" if so.

**N6. Suggestion. Where: RCPT-14 with RCPT-21.** "The same photo sent twice is read and counted
once" could stop the try-again of RCPT-21 from reading the photo after a failed first try.
**Fix:** add to RCPT-14 that a try-again after a failed read is a new read.

**N7. Suggestion. Where: `p1-open-questions.md`, "For counsel, before beta: special-category
data".** The narrowed entry has no options and no recommendation, which `skills/decision-log/`
asks of each open question. **Fix:** add the options counsel may give and the team's
recommendation.

**N8. Suggestion. Where: RCPT-6.** A receipt that prints only a symbol ("$", "Dhs") does not map to
one ISO code, and the eval set is not required to hold a receipt in another currency or with none.
**Fix:** say that an unclear symbol is treated like no currency (the user picks), and add both
cases to the eval set in RCPT-8 or `agentic.md`.

### Result

B1 to B10: 10 addressed, 0 open. S1 to S10: 9 addressed, 1 not addressed (S6, a suggestion). New:
2 blocking (N1, N2) and 6 suggestions (N3 to N8). N2 is the founder's to decide. The spec does not
go to the founder for confirmation until N1 is fixed and N2 is decided or accepted in writing.

## Round 3: fix diff (2026-10-28)

**Read:** `scratchpad/fix-round2.diff` (p1-closed-decisions.md, RCPT.md, spec.md,
p1-open-questions.md, status.md) and the "Rulings" section of `skills/handoff/SKILL.md` (by grep).

### Round 2 findings

| Finding | State | Why |
|---|---|---|
| N1 | addressed | The pass bar entry now opens "(Superseded on 2026-10-28 by "RCPT-1, round 5".)", and the rounds 1 to 3 entry is marked partly superseded. |
| N2 | addressed | The founder decided in round 6 (closed decision); RCPT-24 adds a separate daily cap on failed reads, checked before the read, with RCPT-12 and the spec matching. |
| N3 | addressed | `spec.md` and `status.md` cite every row in `RCPT.md` without a range. |
| N4 | addressed | RCPT-18 counts a receipt in the month of its printed date (or the date the user set); ruling 3. |
| N5 | open, passed on | Passed to `legal` for the design review; a suggestion, it does not block. |
| N6 | addressed | RCPT-14 separates the phone's own retry (read once) from a try-again the user asks for (a new read). |
| N7 | addressed | The open question now has options (a) and (b) and a recommendation. |
| N8 | addressed | RCPT-6 treats a symbol naming more than one currency like no currency; ruling 4. Adding such receipts to the eval set waits for `agentic.md`, with S6. |

S6 still waits for `agentic.md`, as round 2 said.

### Rulings 3 and 4

`skills/handoff/` says anything on the founder's list (targets, thresholds, prices, scope, legal,
permissions, outward steps) is never ruled, and a ruling that crosses a module boundary or cannot
be undone cheaply goes to `reviewer`.

- **Ruling 3 (month by printed date).** Not on the founder's list: it settles an edge case of
  RCPT-18, not a target, scope or price, and it is written into a row the founder confirms with
  the spec. It touches only the server's total, so no module boundary. One claim needs a row (R2
  below): "both dates are kept" is not true of any row yet.
- **Ruling 4 ("$" treated as no currency).** Not on the founder's list: a default for an edge case
  RCPT-6 did not reach, cheap to undo (one extra tap). It sits within the read and save path of
  RCPT-6, so no new module boundary.

Both go in front of the founder at the next stopping point, as the handoff skill says.

### New findings from the fix

**N9. Blocking. Where: `p1-closed-decisions.md`, entry "2026-10-28. RCPT-1, round 5".** The new
round 6 entry says it "Supersedes the failed-read part of round 5 question 6", but the round 5
entry's first line has no "(Partly superseded on 2026-10-28 by "RCPT-1, round 6".)", which is
the same `skills/decision-log/` rule N1 enforced. **Fix:** add that note to the start of the
round 5 entry.

**R1. Suggestion. Where: RCPT-24 with RCPT-21.** A provider failure is our fault, yet it counts
against the user's failed-read cap, so an outage could lock a user out for the day, and no row
says what the user sees when this cap is reached. **Fix:** put to the founder whether provider
failures count (recommended: only RCPT-5 reads, which cost money), and say in RCPT-24 that a
plain message with what the user can do is shown, as in RCPT-12.

**R2. Suggestion. Where: ruling 3 ("both dates are kept"), RCPT-18.** No row says the save date is
stored, so the "cost if wrong" in ruling 3 rests on a guess. **Fix:** add the save date to the
fields a saved receipt holds (RCPT-2 or RCPT-18), or drop the claim from the ruling.

**R3. Suggestion. Where: `spec.md` line 3 ("from grilling rounds 1 to 4").** Rounds 5 and 6 now
shape the spec too. **Fix:** say "grilling rounds 1 to 6" or cite the closed decisions.

### Result

N1 to N8: 7 addressed, 1 open and passed to `legal` (N5, a suggestion). New: 1 blocking (N9) and 3
suggestions (R1 to R3). Rulings 3 and 4 are not on the founder's list and cross no module
boundary. The spec does not go to the founder for confirmation until N9 is fixed.

## Round 4: design, contract, tickets (2026-10-28)

Reviewer, separate agent. Read: `ux.md`, `design.md`, `contract.md`, `tickets.md`, `agentic.md`,
`spec.md`, `readiness.md`, `status.md`, `RCPT.md`, `LAUNCH.md`, `docs/design/brand.md`,
`docs/design/mockups/receipt.html`, `docs/architecture.md`, `docs/adr/0001-photo-read-without-keeping.md`,
`project.toml`, the seven screenshots `docs/design/mockups/shots/receipt-screen-1.png` to `-7.png`,
and by grep `p1-closed-decisions.md`, `ASSUMPTIONS.md`, `p1-open-questions.md`,
`skills/new-feature/SKILL.md`, `agents/architect.md`, `agents/orchestrator.md`. `human-design.md`
was opened only after the walk below was written.

### Human-design walk (reviewer, blind)

Screens as rendered: 1 to 6 light, 7 dark, 6 Arabic right to left. No screen at the largest text
size; no dark or Arabic render of screens 1, 3, 4 and 5.

| Screen | Result | Notes |
|---|---|---|
| 1 Permission | pass | Brand paper, ink and one accent on the one main action; no image or icon; plain copy that names the provider. Not a tell, but see D3 (copy promises a Settings screen) and S2 (the choice leans to yes). |
| 2 Check, English, light | pass | Total at 40 px weight 600 against 16 px fields: real contrast in size and weight; chips, fields and total differ in shape; real-looking sample data (AED 143.75, "Carrefour, Mall of the Emirates"). See S1 (the total gives no sign it can be edited). |
| 3 Unreadable | pass | Plain words, says nothing was saved, says what to do next; no mascot. |
| 4 Our failure | pass | Plain words; the claim "doesn't count against your free receipts" matches RCPT-12 and RCPT-24. |
| 5 Month | pass | Totals at 20 px bold over a 16 px list with hairline dividers: a list where a list is clearer. See S4 (the visible receipts do not add up to the totals). |
| 6 Check, Arabic | **tell** | Copy the audience would not use: the discard button reads "تجاهل" ("ignore"), not "throw away", and "الأكل في الخارج" is a word-for-word "eating out"; the hint "Tap any line to fix it." of screens 2 and 7 is missing. The layout mirrors correctly and the Arabic face sits at the same steps and weights as the Latin one. |
| 7 Check, dark | pass | Dark tokens from `brand.md`; selected chip in ink on paper, accent kept for Save only. |

Not walkable: the largest text size (no render anywhere) and dark or Arabic for four of seven
screens. That is step 2 of the gate not done (D1), not a pass.

### Compared with the designer's walk (`human-design.md`)

| Point | Designer | Reviewer | Settled |
|---|---|---|---|
| Largest text size | not rendered, not verified | not rendered | agree: gate step 2 incomplete (D1) |
| Typeface, Arabic | partial: chosen, not compared side by side | pass from screen 6: same steps, 600 on the total, regular body | designer re-marks after the D1 renders put Latin and Arabic side by side |
| Arabic copy | not raised | tell (D2) | new from this review; under the gate it blocks |
| "Not now" weaker than "Yes" (screen 1) | found, for `legal` | agree (S2) | same finding |
| Fields look read-only (screens 2, 7) | shop and date look read-only | shop and date are boxed like inputs; the total is the one with no sign of editing | partly agree (S1) |
| Nine states described, not drawn | found | agree; and two of them are wrongly said to follow screen 3 (S3) | same finding |
| Placeholder data | pass | pass, with the screen 5 sums (S4) | close |

Neither walk found a tell in the palette, icon, image, motion or card rows of the table.

### Blocking

**D1. Blocking. Where: `human-design.md` header; `ux.md` "Accessibility".** Gate step 2 is not
done: nothing is rendered at the largest text size, and only the check screen is rendered dark
and in Arabic, so "the total wraps under the label" at 200 percent is unchecked and long Arabic
chips are unseen. **Fix:** render all seven screens light and dark, English and Arabic, and at
200 percent text (for example a second pass with `html { font-size: 200% }` or the renderer's
zoom), then repeat the walk on the new shots.

**D2. Blocking. Where: screen 6, `receipt.html` lines 99 to 104.** The Arabic copy reads as a
word-for-word translation ("تجاهل" means "ignore", not "throw away") and drops the "Tap any line
to fix it." hint, a tell under the human-design table. **Fix:** have the Arabic strings checked
by a native speaker (for example "احذف" for throw away, "مطاعم" for eating out), and add the hint
line.

**D3. Blocking. Where: screen 1, second paragraph; `ux.md` "The flow" step 1.** The screen tells
the user "You can say yes later in Settings", but no Settings screen exists in this feature and
`ux.md` says the add button reopens screen 1, so a user-facing statement is false
(`skills/verified-claims/`). **Fix:** say "You can say yes the next time you add a receipt", or
add a settings place to `ux.md` with a ticket; how a user later withdraws permission goes to
`legal`.

**D4. Blocking. Where: `ux.md` "Every state", Reading, offline.** "The photo will be read when
you're back online" promises a queued read that no design, contract line or ticket covers, and it
keeps the photo on the phone with no deletion rule, against RCPT-15, ADR 0001 and screen 1's "we
don't keep the photo afterwards". **Fix (recommended):** "You're offline. Try again when you're
back online." with nothing kept; or, if a queue is wanted, a design for it with a retention rule,
a row and a ticket.

**D5. Blocking. Where: `ux.md` (no state), `tickets.md` T7.** There is no screen or state for a
saved receipt: changing its category (RCPT-4; the saved line even says "Tap it to change the
category"), correcting its fields (PATCH), or deleting it (RCPT-20); no web ticket cites RCPT-20.
**Fix:** add the saved-receipt states to `ux.md` (change category, edit, delete with a
confirmation, delete failed), add RCPT-20 to T7, and name the tests in `month.spec.ts`.

**D6. Blocking. Where: `ux.md` step 5 and "Month"; `contract.md` GET months.** Nothing says how
the user reaches another month (RCPT-18 "for each calendar month"), which month opens after
saving a receipt printed in an earlier month, or the list order; "the new receipt at the top"
contradicts a list by printed date (ruling 3). **Fix:** specify month navigation, that the app
opens the month of the saved receipt's date, and the order (for example `spent_on` newest first,
then `saved_at`), and say the app fetches the totals again after a save instead of adding them
up itself (`skills/single-source/`).

**D7. Blocking. Where: `design.md` "Data" (idempotency_keys) and "Retention and deletion";
`contract.md` "Idempotency".** For the read call, the stored first answer is the shop, date and
total of a receipt nobody has saved, kept 48 hours, which contradicts "stores no receipt" and
"Nothing is stored until you save"; and RCPT-20 (discard deletes the figures at once) cannot hold,
because no call tells the server about a discard. idempotency_keys are also missing from the
retention paragraph and from account deletion (LAUNCH-9). **Fix:** keep the read's replay answer
only until save or discard, with a short expiry the architect states; add a discard call (or a
stated expiry the founder accepts as "at once"); list idempotency_keys in retention and account
deletion.

**D8. Blocking. Where: `contract.md` POST /api/receipts (`read_id`); `design.md` "Data".** The
contract does not say what `read_id` points to on the server, where the AI's category waits
between read and save, how long it lives, or that one read can be saved only once; and ai_reads
"keep no receipt content". A developer will guess, and if the app sends the AI's category back,
RCPT-17 and RCPT-19 can be forged or skewed. **Fix:** name the server record that holds the AI's
category for a read (and its lifetime, joined with D7), state that the server copies
`ai_category` from it and never from the body, and make `read_id` single use
(`409 read_already_saved`).

**D9. Blocking. Where: `contract.md`, every call.** The error lists are incomplete: no code for a
missing or expired session although every call needs one; PATCH and DELETE require an
Idempotency-Key but do not list `409 idempotency_key_reused`; no call lists a code for a missing
key; GET months has no code for a bad `yyyy-mm` or a bad cursor. **Fix:** add `401 not_signed_in`
to every call, `400 idempotency_key_missing` and `409 idempotency_key_reused` to every state
change, and `400 invalid_month` and `400 invalid_cursor` to GET months.

**D10. Blocking. Where: `contract.md` POST and PATCH /api/receipts.** "Validation only here, at
the boundary" names no rules, so `invalid_field` has no definition: shop length, `spent_on` format
and how far in the future, `total_minor` range (zero, negative, maximum), `currency` checked
against which ISO 4217 list, and that a null total or currency is refused at save (RCPT-6;
`ux.md` "Save receipt stays off until the total is there"); nor whether PATCH may set a field to
null. **Fix:** a field table in the contract with each rule and its `details.field` value.

**D11. Blocking. Where: `tickets.md` T3 and "Review focus".** T3 builds the read call but does not
cite RCPT-14, and no named test covers "the same photo sent twice by the phone's own retry is read
and counted once" or "a try-again the user asks for is a new read"; focus item 3 maps to an ADR,
not a ticket. **Fix:** add RCPT-14, RCPT-15 and RCPT-20 to T3 with tests `read.contract.test.ts`
"same key read once, counted once" and "stores nothing" (owned by T3), and in T6 a test that a
user's try-again sends a new key and an automatic retry sends the same one.

**D12. Blocking. Where: `design.md` "Data", ai_reads.** RCPT-11 asks for cost "per user, per
feature and in total", and ai_reads has no feature field, so the row has no home. **Fix:** add
`feature` (a fixed set, today `receipt_read`) to ai_reads and to T2's test.

**D13. Blocking. Where: `docs/architecture.md` lines 3, 9 and 11.** The system map still lists
Supabase "photo storage" and a "Cleanup job (scheduled) deleting photos after 24 hours", which
ADR 0001 rejected, and it says "No code is built yet beyond ticket T1" while `src/` holds no files
and readiness pass 2 has not run (ruling 6). **Fix:** remove photo storage and the cleanup job
(cite ADR 0001), and say "No code is built yet".

**D14. Blocking. Where: `ux.md` "Every state", free allowance used up.** "You've used this
month's free receipts." fixes the allowance period, which LAUNCH-1 leaves to the founder, in copy
marked final. **Fix:** word it without a period ("You've used your free receipts. They come back
on <date from `details.resets_at`>.") until the founder sets N and the period.

### Suggestions

**S1. Where: screens 2 and 7, the total.** The total, the field most likely to need fixing, has
no box or mark, while shop and date are boxed like inputs. **Fix:** give the total the same
editable cue (an outline or an "Edit" label) and check it in the D1 renders.

**S2. Where: screen 1; `ux.md` "For legal".** `ux.md` says "'Not now' as visible as yes", but the
screen has a filled button against an underlined link (the designer found the same). **Fix:**
make "Not now" an outlined button of the same size, or correct the sentence; `legal` decides
whether it matters for consent.

**S3. Where: `ux.md` "Every state".** The currency picker (RCPT-6, "Which currency is this?") is
in the flow but not in the state table, and what it lists is not said; "field missing" and
"saving failed" are check-screen states, not screen 3's layout as the note says. **Fix:** add the
picker as a state (which currencies first, how to find others) and correct the layout note;
drawing the nine states stays a suggestion.

**S4. Where: screen 5.** The four visible receipts do not add up to the totals above them (Kids
AED 239.95 has no receipt shown) and nothing signals more rows, so the founder may read the
totals as wrong at gate step 5; the two-currency category state is not drawn. **Fix:** show a
cut-off cue or consistent sample rows, and draw one category with two currency lines.

**S5. Where: `contract.md` amounts.** Showing `total_minor` needs each currency's minor-unit
exponent (two for AED and EUR, not for every ISO 4217 code), and nothing says where that table
lives, so the app and the server may each keep one (`skills/single-source/`). **Fix:** one table
on the server; the contract returns the exponent (or the formatted amount) with each amount.

**S6. Where: `contract.md` GET months.** It does not say whether `totals` cover the whole month,
or whether they come on every page or on the first only. **Fix:** one sentence.

**S7. Where: `design.md` "When it breaks".** Section 3 of `skills/observability/` asks for rate,
errors and duration on every endpoint; only the read call has them, nothing counts idempotent
replays or 409s, and no ticket carries the instrumentation. The "day" of RCPT-24 and the time
zone of `resets_at` are not stated either. **Fix:** add rate, errors and duration for save,
change, delete and month, a replay counter, put the signals in T3 to T5, and state the day
boundary (the user's local midnight, or UTC said plainly in the copy).

**S8. Where: ruling 7; `agentic.md` sections 2 and 4; T1.** Ruling 7 is sound (300 tokens is twice
the A-11 answer estimate, and the evals will show a cut), but an answer cut at the token limit
would fail to parse and be treated as unreadable (RCPT-5), counting against the user's RCPT-24 cap
though the cut is ours; "a future date is treated as not found" is in the ruling, not in
`agentic.md` or a test; and RCPT-21's "refuses" has no named test. **Fix:** treat a stop at the
token limit as our failure (`provider_failed`), write the date consequence into `agentic.md`
section 4, and add `receipt-answer.test.ts` "future date is null", "cut answer is ours" and
`read.contract.test.ts` "refusal".

**S9. Where: ruling 6; `readiness.md`; `status.md` steps.** Ruling 6 is sound: the quotes hold
(`skills/new-feature/SKILL.md` line 61 "When it passes", `agents/architect.md` "Use after the
readiness gate", `agents/orchestrator.md` line 47), the deadlock is real, and pass 1 opens design
only. But rulings 6 and 7 sit after the sentence that says which rulings go to the founder, so
nothing sends them; the steps table still shows the readiness gate, AI design, design and UX as
"waiting"; and a process rule bent on every feature that stores data is a wish, not an
enforcement (constitution rule 5). **Fix:** add 6 and 7 to the next stopping point, update the
steps table, and propose a template row that splits the readiness gate into a design pass and a
build pass.

**S10. Where: `status.md` ruling 1.** "a rename of 17 ids" is a hand-typed count and is stale:
`RCPT.md` now has 24 rows. **Fix:** drop the number.

**S11. Where: `tickets.md` T6.** `add-receipt.spec.ts` is one name for seven rows. **Fix:** name
the cases, at least "shrinks to 2,576 px", "declined permission sends nothing", "currency picker
when no currency", "Arabic screen mirrors".

### For other agents (their ground, one line each)

- `legal`: consent prominence (S2), how permission is withdrawn (D3), AI disclosure on the check
  screen (`ux.md` "For legal"), retention of read results (D7).
- `security`: a forged `ai_category` and `read_id` reuse (D8), idempotency keys scoped to the
  user, upload type and size checks on the read call.

### Team

- **`devops`, before T3 is built.** The closed decision of 2026-10-28 ("Team for the first
  feature") keeps it off until the first release. New fact: T3 ships behind the flag
  `receipt_ai_read`, and `design.md` names metrics and a daily cost total against LAUNCH-3, so a
  flag mechanism and a place for metrics are needed at build time, not at release. What it adds
  each round: environments, the flag, the metrics sink and the alert on the LAUNCH-3 ceiling.
  It never blocks.
- `debugger` and `rollback`: no new fact; they stay off until the first release, as decided.

### Result

New: 14 blocking (D1 to D14), 11 suggestions (S1 to S11). Rulings 6 and 7 checked: both sound,
with S8 and S9. The design does not go to the developers, and readiness pass 2 does not run,
until D1 to D14 are fixed or the founder accepts them in writing in `p1-closed-decisions.md`.

## Round 5: design fix diff (2026-10-28)

Reviewer, same agent as round 4, second round. Read: `scratchpad/fix-round4.diff` (ux.md,
design.md, contract.md, tickets.md, status.md, architecture.md, ADR 0001, brand.md), screenshots
1, 2, 5, 6, 8, 9, 11, 17 and 21, `human-design.md` "Revision after review round 4", `agentic.md`
section 4, and by grep `brand.md` palette, `ASSUMPTIONS.md` (A-14), `ux.md`. Ran
`python tools/checks/contrast_check.py`: "PASS 12 colour pairs meet their contrast minimum".

### Round 4 findings

| Finding | State | Note |
|---|---|---|
| D1 | **partly addressed, still blocking** | Screens 1 to 7 now have dark (7, 13 to 16), Arabic (6, 17 to 20) and 200 percent text (21, total wraps, nothing cut). The new screens 8 to 12 have no dark or Arabic render, the same gap D1 named. |
| D2 | addressed | "لا تحفظه" on screen 6; hint line back; native reading registered as A-14 and labelled in `ux.md`. |
| D3 | addressed | Screen 1 and 17: "You can say yes later: tap "Add a receipt" again." |
| D4 | addressed | Offline: "Try again when you're connected." Nothing kept or queued. |
| D5 | addressed | Screen 8, flow step 6, T7 with RCPT-20 and `saved-receipt.spec.ts`. Leftovers in S12. |
| D6 | addressed | Previous and next month, opens the printed month, order newest first then saved time (ux step 7, contract GET months). |
| D7 | addressed | A read's record goes on save, discard (`POST /api/reads/discard`) or by the cleanup; listed in retention and account deletion. Leftover in S13. |
| D8 | addressed | Signed `read_token` with the AI's category and a single-use nonce; `receipts.read_nonce` unique; `ai_category` never from the body; tests "token saves once", "forged category ignored". |
| D9 | addressed | `401 not_signed_in` on every call, idempotency errors on every state change, `invalid_month`, `invalid_cursor`. |
| D10 | addressed | Field table with rules and `details.field`; PATCH may not set null. New contradiction in F1. |
| D11 | addressed | T3 cites RCPT-14, RCPT-15, RCPT-20 with the named tests; T6 test on new key versus same key. |
| D12 | addressed | `ai_reads.feature`; T2 test "cost per user, per feature, in total". |
| D13 | addressed | Photo storage removed; cleanup job now deletes read records only; "No code is built yet". |
| D14 | addressed | "You've used your free receipts for now. They come back on {resets_at}." (screen 11). |
| S1 | addressed | "Edit" at the end of every field, the total included (screens 2, 8, 21). |
| S2 | addressed | "Not now" is a full-width outlined button (screens 1, 11, 17). |
| S3 | partly addressed | Picker state added; still open: how to find a currency outside the first ones, the "user's region" has no field in the data, and the note still puts "field missing" and "saving failed" on screen 3's layout. |
| S4 | addressed | Screen 5 totals now match its rows (AED 204.95 = 143.75 + 61.20); screen 9 draws two currencies. New count in F2. |
| S5 | addressed | `currencies` table on the server; amounts carry `exponent`. Leftover in S14. |
| S6 | addressed | Totals cover the whole month and come on every page. |
| S7 | partly addressed | Rate, errors and duration for every route, replay and 409 counters, day ends at midnight UTC. Still open: the failed-read copy says "Try again tomorrow", which is 04:00 in the UAE; use `resets_at` as screen 11 does. |
| S8 | addressed | `agentic.md` section 4: cut answer is `provider_failed`, future date dropped; tests named in T1 and T3. |
| S9 | partly addressed | Steps table updated; rulings 5 to 7 go to the founder. No template row proposed for the two-pass gate. |
| S10 | addressed | "a rename of the area's ids". |
| S11 | addressed | Cases named in `add-receipt.spec.ts`. |

### New findings from the fix

**F1. Blocking. Where: `contract.md` "Fields" (shop and spent_on "required at save") against `ux.md`
flow step 4 ("Save receipt" stays off until the total is there).** The contract now refuses a save
without a shop or a date, while the screen lets the user save with only the total, so a receipt
whose shop was not found ends in `400 invalid_field`; making the shop required is also a new rule
no row or founder answer set (RCPT-2, RCPT-22 do not). **Fix:** align both: recommended, date
required (the month depends on it, ruling 3) and shop optional; or put "shop required" to the
founder and make `ux.md` keep Save off until it is filled.

**F2. Blocking. Where: screens 5 and 9 ("4 receipts", "2 receipts"); `contract.md` GET months.**
The month screen now shows a count of receipts, but the month answer has no count, so the app
would count the items it has loaded, which is wrong past the first page of 50
(`skills/single-source/`). **Fix:** add `count` to the GET months answer, computed on the server
with the totals, and a test in `months.contract.test.ts`.

**F3. Blocking. Where: `design.md` "For Nadia".** The paragraph still says "Nothing is stored
until you save" two sentences before "The figures it read wait for you for at most 24 hours", so
the founder reads a false statement about her users' data (`skills/verified-claims/`). **Fix:**
"Nothing is saved as a receipt until you save. The figures it read are kept for at most a day so a
dropped connection does not lose them, and go at once if you throw the receipt away."

### Suggestions from the fix

**S12. Where: screen 8, `ux.md` step 6.** The saved receipt has no way back drawn, the delete
confirmation is listed as screen 8 but not drawn, and no state says what the user sees when a
change or a delete fails. **Fix:** say how the user leaves screen 8, and add "change failed" and
"delete failed" to the state table.

**S13. Where: `contract.md` "Idempotency", `design.md` retention.** An hourly job that deletes
records older than 24 hours leaves some for up to 25, against "after 24 hours at most"; and a
discarded read's token stays valid for a save until it expires. **Fix:** delete records older
than 23 hours (or say "within 25 hours"), and have the save refuse a token whose read record is
gone.

**S14. Where: `contract.md` POST /api/receipts/read.** `total` is an amount whose currency is
never null, yet `currency` may be null ("$" or none, RCPT-6), so the answer for a total without a
currency is undefined, and its exponent is unknown. **Fix:** say that `total` then comes with
`currency` and `exponent` null and the app asks for the currency first.

**S15. Where: `docs/design/brand.md`.** The highlight colours (#DCE4DB, #23312D) are in the
contrast pairs but not in the palette table, so the token has no job written down. **Fix:** add a
`highlight` row ("the receipt just saved").

**S16. Where: `ux.md` "Interface copy".** "Arabic: screens 6 and 14 to 20" disagrees with
`human-design.md` (Arabic 17 to 20; 13 to 16 are dark), and screen 6 keeps the hint line that the
English screens 2 and 7 have dropped for "Edit". **Fix:** correct the screen numbers and use the
same hint in both languages.

### Result

Round 4: 13 of 14 blocking addressed, D1 partly (screens 8 to 12); 8 of 11 suggestions
addressed, S3, S7 and S9 partly. New: 3 blocking (F1 to F3) and 5 suggestions (S12 to S16).
Open blocking: D1, F1, F2, F3. The design does not go to the developers, and readiness pass 2
does not run, until they are fixed or the founder accepts them in writing in
`p1-closed-decisions.md`.

## Round 6: design fix diff (2026-10-28)

Reviewer, same agent, third round. Read: `scratchpad/fix-round5.diff` (ux.md, design.md,
contract.md, tickets.md, brand.md), screenshots 8, 22, 27 and 31, `human-design.md` "Second
revision after review round 5", and `ux.md` flow step 4 (lines 25 to 29) to check F1.

### Round 5 findings

| Finding | State | Note |
|---|---|---|
| D1 | addressed | Dark (22 to 26) and Arabic (27 to 31) of screens 8 to 12 rendered; 22, 27 and 31 looked at: no tell, layout mirrors, dark tokens right. |
| F1 | **partly addressed, still blocking** | The contract now lets the shop be empty, but still requires `spent_on` and `currency` at save, while `ux.md` step 4 is unchanged: "Save receipt" stays off only "until the total is there". A receipt whose date was not found can still be sent and refused with `400 invalid_field`. |
| F2 | addressed | `count` in GET months, whole month, on every page; test "count covers the whole month" in T5. |
| F3 | addressed | "Nothing is saved as a receipt until you save ... kept for at most a day". |
| S3 | addressed | Dirham and euro first, then a searchable list from the server's table; layout note corrected. |
| S7 | addressed | Failed-read copy uses `resets_at` in the phone's own time. |
| S12 | addressed | "Back to October" on screens 8, 22, 27; "change or delete failed" state added. New detail in S17. |
| S13 | addressed | Records older than 23 hours deleted; a save whose read record is gone is `400 invalid_read_token`. |
| S14 | addressed | Unknown currency: `total` carries `minor` with `currency` and `exponent` null; the app asks first. |
| S15 | addressed | `highlight` row in the palette. |
| S16 | addressed | Arabic screens listed as 6, 17 to 20, 27 to 31; Arabic hint dropped to match "Edit". |

### Open blocking

**F1. Blocking. Where: `ux.md` flow step 4 against `contract.md` "Fields".** The screen still
enables Save on the total alone, while the server refuses a save without a date or a currency, so
a receipt whose date was not found fails on save. **Fix:** one sentence in step 4: "Save receipt"
stays off until the total, the date and the currency are there; the shop may stay empty.

### Suggestions

**S17. Where: `ux.md` flow step 6, "Saved receipt" state.** The delete confirmation is "the
phone's own confirmation box" with the buttons "Delete" and "Keep it", but the browser's own
confirmation box sets its own button words, so the build cannot show "Delete" and "Keep it" there.
**Fix:** draw our own confirmation (one heading, two buttons, as screen 1), or accept the
browser's words and drop the button labels from `ux.md`.

### Result

Round 5: 1 of 4 blocking still open (F1, partly addressed); D1, F2, F3 and all 8 suggestions
(S3, S7, S12 to S16) addressed. New: 0 blocking, 1 suggestion (S17). Open blocking: F1, a
one-sentence fix. This was the third review round of the design; the fix loop cap in
`agents/orchestrator.md` applies to the next one. Not "No blocking findings" while F1 is open.

## Round 7: T1 diff (2026-10-28)

Reviewer, 2026-10-28. Ticket T1 (`lib/receipt-answer`; RCPT-3, RCPT-5, RCPT-6, RCPT-9), read
against `tickets.md` (T1, "Review focus, by ticket"), `contract.md` ("Rules for every call",
"Fields"), `agentic.md` sections 2 and 4 and `docs/requirements/RCPT.md`. Diff read in full:
`package.json`, `src/lib/receipt-answer.ts` (63 lines), `src/lib/receipt-answer.test.ts`
(70 lines). No author summary was given. Line numbers below are file lines, not diff lines.

Ran `npm test` in the project root: vitest 5.0.5, 1 file, 11 tests, all passed. Ran
`node -e` on `Date.parse` to check the date rule (below).

### Correct

- RCPT-3: a category outside the six becomes `other`, case-sensitively, as the schema says.
- RCPT-5: `readable` other than `true`, text that is not JSON, JSON that is not an object, and a
  missing or non-integer total all give `{ ok: false, reason: "unreadable" }` with no value, so
  no category can be shown.
- RCPT-6: the total is a safe non-negative integer or a string of Western or Eastern Arabic
  digits (U+0660 to U+0669); a fractional number is refused; a currency that is not three letters
  ("$") becomes null for the user to pick (ruling 4).
- The future-date rule (ruling 7, `agentic.md` section 4) matches the contract's "not more than one
  day after today in UTC": a date's midnight at or before `now + 24 h` is the same set of dates as
  "today plus one day or earlier", for any time of day. Checked by hand at 00:00, 12:00 and 23:59 UTC.
- One defect, T1-B1 below: an impossible calendar date passes the date check.

### Fits

- The five output fields match RCPT-2's shop, date, total, currency and category; nothing outside
  T1's scope (no network, no storage, no prompt, no metrics). `package.json` is the minimum needed
  to run the tests.
- Leaving the ISO 4217 table check and the 0 to 100,000,000 total range to the save boundary
  agrees with "Validation only at this boundary" in `contract.md`; see T1-S2.

### Simple

- Small, no dead code, no speculative abstraction; names a newcomer can follow. Comments cite
  the rows they serve.

### Tested

- Each test fails without the change (the module is new). Each of RCPT-3, RCPT-5, RCPT-6 and
  RCPT-9 has at least one asserting test.
- Review-focus tests T1 owns, by the names in `tickets.md`:

| Item | Name in `tickets.md` | In `receipt-answer.test.ts` |
|---|---|---|
| 1. The bad photo | "treats readable false as unreadable" | yes, line 30 |
| 4. The Arabic receipt | "reads a total written in Eastern Arabic digits" | yes, line 45 |
| 5. The receipt that gives orders | "keeps only the five fields, whatever else the answer contains" | yes, line 64 |
| T1 extra | "drops a date more than a day in the future" | yes, line 57, with " (ruling 7)" added to the name (T1-S5) |

### Blocking

**T1-B1. Where: `src/lib/receipt-answer.ts` line 35 (`spentOn`).** `Date.parse` rolls an impossible
day over instead of refusing it (`Date.parse("2026-02-30T00:00:00Z")` is 2 March 2026, and
`2026-04-31` is 1 May), so a misread date such as `2026-02-30` reaches the user as a checked
`spentOn`, and the month it is filed under (ruling 3) depends on what the save layer does with a
date that does not exist. **Fix:** after parsing, keep the value only if
`new Date(t).toISOString().slice(0, 10) === value`, else return null so the user fills it
(RCPT-22), and add a test "drops a date that does not exist" with `2026-02-30`.

### Suggestions

**T1-S1. Where: `src/lib/receipt-answer.ts` line 44.** The comment says an answer that is not JSON is
an unreadable photo, which holds only if the caller has already turned a stop at the 300-token
limit and a provider refusal into `provider_failed` (`agentic.md` section 4, RCPT-21); otherwise a
cut answer fails to parse here and counts against the user's RCPT-24 cap. **Fix:** say in the
function's comment that the caller must hand over only complete, non-refused answers, so T3's
builder does not rely on a parse failure; T3's "cut answer is ours" and "refusal" tests are where
it is proved.

**T1-S2. Where: `src/lib/receipt-answer.ts` lines 19 and 23.** A total above the contract's
100,000,000 is accepted here and refused only at save (`400 invalid_field`), so a misread total
can be shown as read and then fail on the tap. **Fix:** keep the range in one shared place that
both this parser and the save check read (`skills/single-source/`), and treat an out-of-range
total like a missing one; or leave it and let the user correct it (RCPT-22). Either way, no
second hand-typed copy of the number.

**T1-S3. Where: `src/lib/receipt-answer.ts` line 51.** An off-list category becomes `other` with no
sign that it happened, but `agentic.md` section 2 counts it as a schema miss in the evals, so T8
would have to repeat the category check to count it. **Fix:** return the miss (for example a
`categoryWasOffList` flag beside the result, outside the five fields) so the eval runner reads it
from this one function.

**T1-S4. Where: `src/lib/receipt-answer.test.ts`.** No test covers a negative total, a JSON answer
that is not an object (`null`, `[]`, `"text"`), shop trimming and the 120-character cut, or the
date boundary (with `NOW` at 12:00 UTC on 28 October, 29 October kept and 30 October dropped);
the future-date test uses 15 November, far from the edge where an off-by-one would hide.
**Fix:** add those four cases.

**T1-S5. Where: `src/lib/receipt-answer.test.ts` line 57.** The test is named "drops a date more than
a day in the future (ruling 7)", while `tickets.md` names it without " (ruling 7)"; a check that
matches names exactly would miss it. **Fix:** use the name `tickets.md` gives.

**T1-S6. Where: `package.json` line 15 and the root `package-lock.json`.** The diff has a caret range
(`^5.0.5`) and no lock file, so the vitest version that runs is not pinned by this change, though
a `package-lock.json` exists in the working tree. **Fix:** commit `package-lock.json` with the
change.

**T1-S7. Where: `src/lib/receipt-answer.ts` line 56.** `slice(0, 120)` counts UTF-16 units, so a shop
name ending in an emoji at the cut can be split; the contract says "characters". **Fix:** cut by
code points (`Array.from(s).slice(0, 120).join("")`), or note that the save check counts the same
way.

### For other agents (their ground, one line each)

- `security`: RCPT-9 here is a field allow-list only; whether the prompt holds against a hostile
  receipt is T8's eval ground.
- `agentic-workflow`: the parser cannot tell a model that turned "$" into "USD" from a printed
  "USD"; ruling 4 then depends on the prompt and the eval set.

### Team

Nothing in this diff calls for an agent that is not switched on.

### Result

Round 7: 1 blocking (T1-B1), 7 suggestions (T1-S1 to T1-S7). T1 does not go to qa until T1-B1 is fixed or
the founder accepts it in writing in `p1-closed-decisions.md`.

### Answers to round 7 (backend-dev, 2026-10-28)

Each finding checked before it was accepted: T1-B1 reproduced by the new test "drops a date that
does not exist" (red: "Tests 2 failed | 16 passed (18)", with T1-S7's test); T1-S7 likewise.

| Finding | What changed, or why not |
|---|---|
| T1-B1 | Fixed: the date must round-trip through `toISOString`; test "drops a date that does not exist". Red with the fix reverted, green restored. |
| T1-S1 | Fixed: the caller's duty stated above `parseReceiptAnswer`; T3's tests prove it. |
| T1-S2 | Not changed: the reviewer's second option. An out-of-range total reaches the check screen and the user corrects it (RCPT-22); no second copy of the number. |
| T1-S3 | Not changed now: no caller needs the flag until T8; added to T8's notes when T8 starts, so nothing unused is built (`skills/karpathy-guidelines/`). |
| T1-S4 | Fixed: tests for a negative total, JSON that is not an object, trimming, the 29 and 30 October boundary. |
| T1-S5 | Fixed: the test name now matches `tickets.md`. |
| T1-S6 | Not changed: nothing is committed in this round (no founder go to commit); `package-lock.json` goes in with the first commit. |
| T1-S7 | Fixed: cut by code points; test "cuts the shop name at 120 characters without splitting one". |

## Round 8: T1 fix diff (2026-10-28)

Reviewer, 2026-10-28. Read only the fix diff (`src/lib/receipt-answer.ts`,
`src/lib/receipt-answer.test.ts`) and "Answers to round 7". Ran `npm test` in the project root:
1 file, 18 tests, all passed.

### Round 7 findings

| Finding | Status | Why |
|---|---|---|
| T1-B1 | addressed | `spentOn` now refuses a date that does not round-trip through `toISOString` (`receipt-answer.ts` line 37); "drops a date that does not exist" asserts `2026-02-30` is null. |
| T1-S1 | addressed | The caller's duty (a cut or refused answer is `provider_failed` before the parser runs) is stated above `parseReceiptAnswer`; T3's "cut answer is ours" and "refusal" still prove it. |
| T1-S2 | answered | The second option offered in round 7: the user corrects an out-of-range total (RCPT-22) and the save check is the only copy of the range. Accepted. |
| T1-S3 | answered | Accepted as not needed until T8 (nothing unused is built). The note is promised for when T8 starts and is not written anywhere yet, so the reviewer of T8 will look for the schema-miss count there. |
| T1-S4 | addressed, one gap | Negative total, the 29 and 30 October boundary and trimming are tested. "Not an object" is tested with `[]`, which is an object to `typeof` and fails on `readable` instead, so the `typeof answer !== "object" \|\| answer === null` check (line 56) is still not exercised; see T1-S8. |
| T1-S5 | addressed | The test is now "drops a date more than a day in the future" (test line 66), the name in `tickets.md`. |
| T1-S6 | answered | Nothing is committed this round; accepted, on the condition that `package-lock.json` goes in with the first commit of `package.json`. |
| T1-S7 | addressed | `shop()` cuts by code points; the test with 119 letters, an emoji and one more letter keeps the emoji whole. |

### New findings from the fix

**T1-S8. Suggestion. Where: `src/lib/receipt-answer.test.ts`, "treats JSON that is not an object
as unreadable".** The input `[]` passes the object check and is caught by `readable !== true`, so
removing the check on line 56 would not turn the test red. **Fix:** use `null` (or `"text"`) as
the input, which only that check catches.

No new blocking finding. The new `shop()` and date code is small, cites its rule, and stays in T1's
scope.

### Result

Round 8: T1-B1 addressed; T1-S1, T1-S5, T1-S7 addressed; T1-S4 addressed with one gap (T1-S8);
T1-S2, T1-S3, T1-S6 answered and accepted. New: 0 blocking, 1 suggestion (T1-S8).

No blocking findings.
