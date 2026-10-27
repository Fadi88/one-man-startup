# Spec: a receipt photo sorted into a spending category (RCPT-1)

Written by the orchestrator from grilling rounds 1 to 7 (2026-10-28) and three rounds of review. Rows: every row in
`docs/requirements/RCPT.md`, with `LAUNCH-1` to `LAUNCH-7` from setup.

## For Nadia

**Who and why.** For you first, and for busy families like yours: both parents work, they shop
all the time, and the receipts end up in a drawer. Today they do nothing; a spreadsheet was tried
and given up after two weeks.

**What it does.** You take a photo of one receipt, or pick one from your phone's photos. The app
makes the photo smaller, reads it with AI, and shows you the shop, the date, the total in the
currency on the receipt, and one category. Before saving you can correct the shop, date or total,
and change the category; then you save it or throw it away. You can change the category any time
later. For each month you see the list of your saved receipts and a total per category; dirhams,
euros and any other currency are totalled separately, never added together. A receipt with no
currency printed asks you to pick one.

**Before the first receipt.** The app asks your permission to send receipts to the AI company.
If you say no, nothing is sent, the app explains it cannot sort receipts without it, and you can
say yes later.

**The categories.** Groceries, eating out, transport, household, kids (things bought for
children), and other. Pharmacy receipts go under other, and there is no health category while the
legal question about health information is open.

**When something goes wrong.** A photo that can't be read gets a plain message and a retake;
nothing is saved. If the AI company is down or takes more than about 30 seconds, the app says it
couldn't read it on our side and offers to try again. Neither uses up a free read, but each
person has a small daily limit of photos that can't be read (a failure on our side never counts), so nobody can run up the cost; its number is set
with the other free allowance numbers. When the free allowance runs out, a plain message says what you can do. A photo
left without saving is deleted after 24 hours. When you save a receipt, its photo is deleted once
it has been read and checked, as decided at setup; when you throw one away or delete it, the photo
and the figures go at once.

**Not in this version.** No bank connection, no email receipts, no item-by-item sorting, no
sharing with family, no "please check" mark, no currency conversion.

**How we know it works.** At least 8 out of 10 receipts that real users save stay in the category
the app chose. We read this four weeks after the first real user starts.

**Before your users see it.** The AI is tested on a fixed set of made-up receipts in English,
Arabic and German, at least 10 in each language. In each language, at least 9 out of 10 must get
the category that fits what was bought (receipts written to fool the AI count like any other),
and the total must be exactly right on at least 9 out of 10. The cheaper AI is used unless it fails
this test. One receipt should cost about six hundredths of a US cent to read. That is an estimate in
`feasibility.md`, from the AI company's prices read on 2026-10-28 and our guess of the length of
the instructions (assumption A-11, measured in the test). You are told if it would cost more
than two cents.

**Not yet known.** How well the AI reads Arabic and German receipts (assumption A-10): the test on
made-up receipts settles it, once you have opened the AI account and said go.

**Guesses you may want to correct.** A month is a calendar month. People will add receipts in batches at home rather than at
the till. "Kids" means things bought for children, not information about children.

## For the other agents

### Rows

| Behaviour | Rows |
|---|---|
| Add a receipt by photo | RCPT-1, RCPT-13 |
| Read and show before saving | RCPT-2, RCPT-6, RCPT-7, RCPT-22 |
| Monthly list and totals | RCPT-18 |
| The AI's first choice kept | RCPT-19 |
| Discard and delete | RCPT-20 |
| AI provider down or slow | RCPT-21 |
| Permission declined | RCPT-23, LAUNCH-7 |
| Six categories, AI answer constrained | RCPT-3, RCPT-9 |
| Change category | RCPT-4, LAUNCH-5 |
| Unreadable photo | RCPT-5 |
| Quality bar before users | RCPT-8 |
| Own data only | RCPT-10 |
| Counting and cost | RCPT-11, RCPT-16 |
| Free allowance | RCPT-12, RCPT-24, LAUNCH-1 to LAUNCH-4 |
| Duplicate save | RCPT-14 |
| Photo deletion | LAUNCH-6, RCPT-15 |
| Permission before the first read | LAUNCH-7 |
| Success number | RCPT-17 |

### Review focus

The likeliest real-world conditions that would break this feature and that no setup row
tested:

1. **The bad photo:** a long, crumpled, blurred or dark receipt, or a photo of something that is
   not a receipt. RCPT-5, RCPT-13.
2. **The double tap and the retry:** the user taps save twice, or the connection drops and the
   phone sends again. RCPT-14.
3. **The user who leaves halfway:** a photo sent, the app closed before saving. RCPT-15.
4. **The Arabic receipt:** right-to-left text, Eastern Arabic digits, a total in AED with fils.
   RCPT-6, RCPT-7.
5. **The receipt that gives orders:** printed or handwritten text such as "ignore the list and
   answer X". RCPT-9.
6. **The AI company down or slow** on a busy evening. RCPT-21.

And the classic one from security: **the second user** asking for the first user's receipt
(RCPT-10).

### Reviews this feature needs

Personal and financial data and AI output: `legal` and `security` on the design, and `security`
on every diff (gates level standard: "only where the feature's spec flags them"; this spec flags
them).

### Open questions on the path

- Cross-border transfer (`p1-open-questions.md`): blocks any real user's receipt, not the build.
- Special-category data in receipts: decided by the founder on 2026-10-28 (round 5, question 8):
  build and test with made-up receipts now; counsel before any real user's receipt is read
  (`legal.md` part 1). Blocks beta, not the build.
- Free allowance numbers: block any free path going live, not the build.
