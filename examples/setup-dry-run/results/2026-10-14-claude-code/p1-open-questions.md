# Open questions

What is waiting on the founder. Each entry: the question, the options, the recommendation, what it
blocks, and the date it was raised. Remove an entry when it is answered and move the answer to
`p1-closed-decisions.md`.

- **How Receipt Buddy gets paid.** Options: the founder's own company with Stripe (supports
  businesses in the UAE and Germany per https://stripe.com/global, checked 2026-10-14; the
  founder then handles VAT in each country), or a merchant of record such as Paddle (pricing at
  https://www.paddle.com/pricing, checked 2026-10-14). Recommendation: decide with `legal` and
  an accountant, from each provider's dated terms. Blocks: the payment feature, not the
  prototype. Raised 2026-10-14 by setup.
- **The free version's numbers.** Receipts per signed-in user, per visitor without sign-up, and
  the global daily spend ceiling (rows LAUNCH-1 to LAUNCH-3). Recommendation: set them once the
  prototype has measured the cost of one receipt. Blocks: any free path going live. Raised
  2026-10-14.
- **For `legal`: cross-border transfer.** Receipt photos and figures of UAE and German users go
  to a database in Frankfurt and to Anthropic, whose processing is "global" or US only. On what
  basis may each region's data go there (UAE PDPL adequacy and exceptions, UNSETTLED; the EU-US
  Data Privacy Framework or standard contractual clauses for Germany; no EU adequacy decision
  for the UAE, where the founder is)? See both packs. Recommendation: `legal` answers, with
  counsel, before any real user's receipt is processed. Blocks: beta. Raised 2026-10-14.
- **For `legal`: an EU representative.** A controller outside the EU offering services to people
  in Germany must name one unless an exemption fits (DE pack). Recommendation: `legal` confirms
  and lists options. Blocks: German launch. Raised 2026-10-14.
- **For `legal`: UAE rules still unsettled.** PDPL executive regulations, Arabic-language and AED
  pricing duties, the Modern Technology Trade law's regulations, cookie consent, accessibility
  and the Central Bank's view of a receipt-only tracker (AE pack). The official UAE legislation
  site refused access on 2026-10-14. Blocks: UAE launch. Raised 2026-10-14.
- **For `legal`: special-category data in receipts.** Pharmacy items or donations on a receipt
  may reveal health or beliefs (DE pack). Recommendation: `legal` advises whether item-level
  categories need extra handling. Blocks: the categorisation feature's spec. Raised 2026-10-14.
- **For the founder, before deploying: Vercel's free plan for the prototype.** Vercel's Hobby
  plan is "for personal, non-commercial use" (https://vercel.com/pricing, checked 2026-10-14);
  whether an unpaid prototype of a business qualifies is assumption A-7. Options: ask Vercel,
  or start on Pro at US$20 a month. Blocks: the first deploy. Raised 2026-10-14.
