# Open questions

What is waiting on the founder. Each entry: the question, the options, the recommendation, what it
blocks, and the date it was raised. Remove an entry when it is answered and move the answer to
`p1-closed-decisions.md`.

- **2026-10-14. Cross-border transfer of receipt data to third-country AI APIs.**
  Question: What legal transfer mechanism and vendor safeguards will govern transferring UAE
  and German receipt photos and text to US-hosted AI APIs (such as OpenAI)?
  Options: Rely on EU-U.S. Data Privacy Framework certification with standard data processing
  agreements; execute Standard Contractual Clauses (SCCs) with a Transfer Impact Assessment;
  or deploy self-hosted models within local EU/UAE infrastructure.
  Recommendation: Have legal counsel review AI vendor terms and verify Data Privacy Framework
  certification before processing live production user data.
  Blocks: Production launch of AI receipt scanning (`LAUNCH-12`).
- **2026-10-14. Free tier numerical caps and unit economics.**
  Question: What numerical limits should apply to monthly scans for registered free users and
  daily scans for guest devices?
  Options: Set arbitrary caps now vs measure cost per receipt scan in the working prototype
  and set limits that maintain safe margins under the $100 budget.
  Recommendation: Defer exact numbers until prototype testing measures token and storage costs.
  Blocks: Public release of free tier (`LAUNCH-13`, `LAUNCH-14`).
- **2026-10-14. Subscription pricing and merchant of record selection.**
  Question: What price points will be charged for paid subscriptions, and which payment processor
  or merchant of record (e.g. Stripe vs Paddle) will be used to handle UAE and EU sales tax and VAT?
  Options: Direct merchant account (Stripe) with local tax registrations vs Merchant of Record
  (Paddle) handling global VAT compliance automatically.
  Recommendation: Evaluate fee schedules and VAT filing obligations with legal and accounting
  counsel once prototype validation is complete.
  Blocks: Paid subscription checkout launch (`LAUNCH-6`, `LAUNCH-8`).
