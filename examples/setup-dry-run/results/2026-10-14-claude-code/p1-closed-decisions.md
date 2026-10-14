# Closed decisions

What was decided, so nobody argues it again without a new fact. Newest first. Each entry: date,
decision, reason, who decided, what would make it worth reopening.

## This project

All from the setup interview of 2026-10-14 (`examples/setup-dry-run/transcript.md`), decided by
Nadia Example. Reopen any of them when the fact behind it changes.

- **2026-10-14. Founder: Nadia Example <nadia@example.com>, not technical.** Agents explain in
  plain words. Git identity and `core.hooksPath tools/githooks` set to match.
- **2026-10-14. Product: Receipt Buddy, at the idea stage.** "Snap a photo of a receipt and it
  sorts your household spending for you, so you can see where the money goes each month."
- **2026-10-14. Regions AE and DE.** Reason: "I live in Dubai and my sister in Berlin wants it
  too." Turned on: region packs `docs/legal/regions/AE.md` and `DE.md`, to be reviewed by
  `legal` before any launch. Reopen: a new country.
- **2026-10-14. Domain: personal finance** (setup's recommendation, accepted). Turned on: money
  data is sensitive, so `legal` and `security` review every feature that touches receipts,
  spending or payments.
- **2026-10-14. Audience: "Busy expat families who never get round to tracking spending."**
  Turned on: plain, low-effort flows for `designer` and `growth`; the language of terms and
  notices follows the region packs.
- **2026-10-14. Customer size: consumers.** Turned on: self-serve sign-up, cancellation and
  deletion, consumer law in each pack, and the rows in `docs/requirements/LAUNCH.md`.
- **2026-10-14. Data: receipt photos, the amounts and shop names on them, the user's email.**
  Sensitive: personal data, financial data, payments, AI processing of user content. No
  children (adults only, 18 and over), no health data, no biometrics (recommendations accepted).
- **2026-10-14. The AI suggests a category and the user can change it; it decides nothing about
  a person** (recommendation accepted). Reason: keeps the totals trustworthy and keeps the
  product away from decisions about people.
- **2026-10-14. Receipt photos are deleted once read and checked; the figures are kept until the
  account is deleted** (recommendation accepted). Reason: the photo is the riskiest thing to
  store. This fills the retention line of `docs/legal/playbook.md` for this project.
- **2026-10-14. A paid plan; a free version only with strict caps** (per signed-in user, tighter
  without sign-up, a global daily ceiling), numbers set by the founder once the prototype has
  measured the cost of one receipt. Founder: "I don't know the costs yet. Do what you recommend
  and I'll set the numbers when we know them."
- **2026-10-14. Stack: web app for phone browsers; Next.js, Supabase (Frankfurt), Vercel,
  Anthropic API, Vitest and Playwright.** Founder: "No idea. Whatever is simplest and cheap to
  start." The prices behind it are in the transcript, round 4, each with its source and date.
- **2026-10-14. Gates: standard, not strict.** Setup recommended strict twice and said what it
  buys. Founder's reason: "Can we go lighter? I want to move fast, it's just an idea." then
  "Fine, standard then, not light. I'll go strict before real users." Reopen: before the first
  real user, by the founder's own word.
- **2026-10-14. Team: orchestrator, setup, architect, designer, frontend-dev, backend-dev, qa,
  security, legal, growth, optimizer.** devops is off until the first deploy (setup's
  recommendation); social-media declined for now (see `p1-rejected.md`).
- **2026-10-14. AI budget: US$100 a month** ("About 100 dollars a month for the AI stuff").
- **2026-10-14. Tools: Claude Code only** ("I'm using Claude Code"). Adapters are generated for
  Claude Code alone.

## About the template itself

Decisions taken while building the template. They explain why the template's files say what
they say. A project made from the template keeps them as background and adds its own above.

- **2026-10-14. The B2C playbook names no product, market, platform or price.** It is a method
  for any consumer product; the founder fills those in at setup and in each grilling. Reason:
  the template is meant for any project. Decided by Fadi, answering the grilling on strategy
  v2 (product, customer, first market and platform are the founder's; the template must not
  start a startup). Reopen: never for the template; each project decides its own.
- **2026-10-14. The free tier is strict.** Every free action that costs money is capped per
  user, use without sign-up is capped harder, and a global daily ceiling pauses the free tier.
  The caps are requirement rows that must be tested before release. Reason: an uncapped free
  path lets anyone, including scripts, run up the founder's AI bill. Decided by Fadi. Enforced
  in the playbook (section 2), setup, architect, backend developer, security and the release
  checklist. Reopen: only with a mechanism that bounds spend another way, shown working.
- **2026-10-14. Whether a cookie or consent banner is needed is decided by `legal`, per region.**
  "Cookieless analytics means no banner" is not taken as given. Reason: it depends on what is
  stored on or read from the device and on each region's rules, not on the analytics vendor's
  description. Decided by Fadi, from review cycle 3 of the B2C strategy. Reopen: a region pack
  that cites the rule for that region.
- **2026-10-14. Deadline discounts only when the deadline is real**, with the wording checked
  by `legal`. Reason: fake urgency is a dark pattern and a consumer law risk; the designer
  agent already rules it out. Decided by Fadi, from review cycle 3.
- **2026-10-14. Choosing between selling through the founder's own company and through a
  merchant of record is a founder decision**, made with `legal` and an accountant, from fees and
  terms read off each provider's own pages and dated. Neither is mandated by the template.
  Reason: the right answer depends on the founder's company, markets and volume. Decided by
  Fadi, from review cycle 3.
- **2026-10-14. Growth ideas run as experiments** with a prediction, a "wrong if" and a read
  date, and the roadmap validates (smoke test, prototype) before it builds. Reason: a plan with
  no number that can fail teaches nothing. Decided by Fadi, from the review of strategy v2.
- **2026-10-14. From strategy review cycle 7, kept as methods in the playbook:** caps counted on
  combined signals, never network address alone; cost reserved before a paid call and returned on
  failure; an optional lower allowance for new paying users during a refund window; abuse checks
  on public share pages; a cold-start section (open-source pieces, listings, genuine community
  answers); store rules on thin web wrappers and outside payment links; a retention section built
  on value and one-click export; AI transparency and self-serve deletion, export and invoices.
  The region pack template gains withdrawal waivers, exit offers, pre-selection, AI content
  marking and device identifiers. Decided by Fadi. Reopen: a project's own evidence.
- **2026-10-14. Every rejected idea is recorded** (constitution rule 13), in
  `p1-rejected.md` the same day, whoever proposed it. Reason: without it, settled proposals come
  back as if new. Decided by Fadi, 14 October 2026.
- **2026-10-14. No unconfirmed assumptions** (constitution rule 11). Facts in anything the
  founder or a user reads are sourced, tested or measured, registered as assumptions, or cut.
  Decided by Fadi, 14 October 2026.
