# Research: sorting a receipt photo into a spending category

Written by `researcher` for RCPT-1, 2026-10-28, before the first grilling round.

**The job:** "I have a paper receipt; I want it counted in the right part of my household
spending without typing it in."

**Search terms used:** "receipt scanning app household budget automatic category AI consumer
pricing 2026"; then each product's own pricing page or store listing.

## What similar products do

Every price and feature below is quoted from the product's own page, read on 2026-10-28.
Store listings showed no reviews ("This app hasn't received enough ratings or reviews to display
an overview"), so the complaint column says so rather than guess.

| Product | What it does for this job | Price | Standout strength | Common complaint | Source (read 2026-10-28) |
|---|---|---|---|---|---|
| ReceiptStorm | Photo of a paper receipt; "Our AI extracts items, prices, and categorizes them automatically in about 10 seconds." | Free: "5 AI scans per month, unlimited typing"; Pro "€3/month" for the household (the listing's in-app purchases say "Receipt Storm Pro $4.99"; the listing does not explain the difference) | One plan covers the whole household; a clear message when free scans run out | No reviews shown | https://apps.apple.com/au/app/id6755887696 |
| Receipta | Camera, photo, PDF or forwarded email; reads "item by item" and "assigns categories"; translates receipts and converts currencies | "Receipta Monthly $6.99", "Receipta Yearly $49.99", trial without payment | Many ways in (photo, PDF, email) | No reviews shown | https://apps.apple.com/app/id6759993760 |
| Shoeboxed | Receipt scanning service, digital scans and posted paper receipts | Starter "$9 /mo" with "50 digital scans per month"; Pro "$29 /mo"; Plus "$79 /mo" | Large scan allowances, paper receipts posted in | Not found on the page; the page does not describe automatic categories as a feature | https://www.shoeboxed.com/pricing/ |
| Spendee | Budget app; "we categorize all your new transactions for you"; "Connect Spendee with all your bank accounts"; "Shared wallets" on paid plans | Basic "Free"; Plus "$1.99/Month"; Premium "$5.99/Month" | Shared wallets for more than one person | Not found; the page does not say whether receipts can be photographed | https://www.spendee.com/pricing |
| Finanzguru (Germany) | Bank-connected; "Deine Buchungen werden automatisch kategorisiert"; links "über 4.000 Banken und Anbieter" | Plus "0,99 € pro Woche" | Automatic categories from bank data, popular in Germany | Not found; the page does not mention receipt scanning | https://finanzguru.de/ |

## Patterns

- **Almost everyone sorts into categories automatically**, from the photo (ReceiptStorm,
  Receipta) or from bank data (Spendee, Finanzguru). Users will expect it.
- **The receipt-photo apps sort item by item**; the bank apps sort the whole payment.
- **A free allowance of AI scans is common** (ReceiptStorm: 5 a month), with a paid plan for
  more.
- **Nobody shown here is built for the UAE or for Arabic receipts.** None of the pages read
  mentions Arabic. A possible opening, not a proven one.

## Suggestions for the grilling

1. **One category per receipt in the first version, not item by item?** Recommended yes: it is
   the smallest version that answers "where does the money go", and item by item raises the
   pharmacy-items question already open for `legal`. Evidence: ReceiptStorm and Receipta go
   item by item; the bank apps sort whole payments and are popular.
2. **No bank connection in the first version?** Recommended yes (no bank connection): the
   product is about receipts, and connecting banks brings in the open question about the UAE
   Central Bank. Evidence: Spendee and Finanzguru connect banks; the receipt apps do not.
3. **Photo only, not email or PDF, in the first version?** Recommended yes: one way in keeps the
   first version small. Evidence: Receipta also takes PDFs and forwarded email.
4. **One account for the household later, not now?** Recommended: later. Evidence: ReceiptStorm
   and Spendee sell household or shared use as a paid feature.
5. **A clear message, not an error, when the free allowance runs out?** Recommended yes.
   Evidence: ReceiptStorm's listing promises "a clear message with your options instead of an
   error". The allowance itself is already an open decision (LAUNCH-1 to LAUNCH-3).

## Not found

- Expensify's pricing: https://www.expensify.com/pricing opened an unrelated settings page and
  https://www.expensify.com/pricing-details returned 404, so it is left out.
- Finanzguru's prices page (https://finanzguru.de/preise) returned 404; the price is from its
  home page.
- User complaints: no store listing read showed reviews. Not confirmed.
- Any receipt app built for the UAE or Arabic receipts: none found in this short search.
