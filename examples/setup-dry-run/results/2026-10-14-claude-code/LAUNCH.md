# LAUNCH: what must hold before Receipt Buddy has real users

Rows implied by the setup answers of 2026-10-14 (`p1-closed-decisions.md`): consumers in the
UAE and Germany, personal finance, receipt photos read by an AI provider, a paid plan and a
possible free version. All `X`: decided, not built. Legal rows follow the region packs in
`docs/legal/regions/`; `legal` refines them per feature.

| ID | Requirement | Status |
|---|---|---|
| LAUNCH-1 | A signed-in free user can have at most N receipts read by the AI per period; N and the period are set by the founder after the prototype measures the cost of one receipt. | X |
| LAUNCH-2 | Use without sign-up, if offered, has a lower cap than LAUNCH-1, counted per device on combined signals and never on network address alone; the number is set by the founder. | X |
| LAUNCH-3 | A global daily ceiling on what all free use may spend pauses the free version until the next day when it is reached; the amount is set by the founder. | X |
| LAUNCH-4 | No free path calls the AI provider or another paid service without passing the cap checks of LAUNCH-1 to LAUNCH-3 first. | X |
| LAUNCH-5 | The AI only suggests a spending category, and the user can change the category of any receipt. | X |
| LAUNCH-6 | A receipt photo is deleted once its figures are read and the user has checked them; the figures are kept until the account is deleted. | X |
| LAUNCH-7 | Before a user's first receipt is read, the app says that a named AI provider reads it and asks for explicit permission. | X |
| LAUNCH-8 | Sign-up asks the user to confirm they are 18 or over, and the service is not offered to anyone who does not. | X |
| LAUNCH-9 | A user can delete their account and all their data themselves, in the app. | X |
| LAUNCH-10 | A user can export all their figures in one step, in a common file format. | X |
| LAUNCH-11 | Nothing that is not strictly necessary is stored on or read from the user's device before consent, where the region pack requires consent. | X |
| LAUNCH-12 | Prices are shown to consumers including VAT, and checkout follows the region packs (in Germany, the order button wording). | X |
| LAUNCH-13 | Cancelling the paid plan is self-serve and no longer than signing up, and follows the region packs (in Germany, a permanent cancellation button). | X |
| LAUNCH-14 | The privacy notice names each processor (database, hosting, AI provider, payment provider) and where it processes data. | X |
| LAUNCH-15 | The service shows the business information each region pack requires (in Germany, an Impressum). | X |
