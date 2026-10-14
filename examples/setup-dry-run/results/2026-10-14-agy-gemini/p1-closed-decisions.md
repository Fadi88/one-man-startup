# Closed decisions

What was decided, so nobody argues it again without a new fact. Newest first. Each entry: date,
decision, reason, who decided, what would make it worth reopening.

## This project

- **2026-10-14. Founder identity: Nadia Example (nadia@example.com), level non-technical.**
  Decided by Nadia. Reason: founder preferences; agents will communicate in plain language
  without unexplained jargon. Reopen: if ownership or technical preferences change.
- **2026-10-14. Product definition: Receipt Buddy, stage idea.** One sentence: "Snap a photo of a
  receipt and it sorts your household spending for you, so you can see where the money goes each month."
  Decided by Nadia. Reason: initial concept definition. Reopen: when prototype validation finishes.
- **2026-10-14. Target markets UAE (AE) and Germany (DE), customer size consumers, domain fintech.**
  Audience: "Busy expat families who never get round to tracking spending." Decided by Nadia. Reason:
  founder lives in Dubai with family in Berlin, consumer self-serve model. Reopen: when expanding to
  additional jurisdictions or business customer tiers.
- **2026-10-14. Financial data and payment processing classified as sensitive.** User emails, receipt
  photos, vendor names, and itemized amounts stored securely. Decided by Nadia. Reason: receipts contain
  confidential household financial data requiring encryption and clear privacy disclosures. Reopen: if
  data collection scope changes.
- **2026-10-14. Process gates set to standard during the idea phase.** Decided by Nadia. Reason: founder
  asked "Can we go lighter? I want to move fast, it's just an idea." The setup agent explained what strict
  buys (requirement rows before code, green test sweep before every hand-off, commit hooks, prevented
  regressions). Nadia settled on: "Fine, standard then, not light. I'll go strict before real users."
  Reopen: upgrade to strict before onboarding real users.
- **2026-10-14. Agent roster excludes social-media agent.** Decided by Nadia. Reason: founder stated "I don't
  need the social media one yet, I'll do that myself later." Reopen: when preparing for marketing launch.
- **2026-10-14. AI spend ceiling set to $100 per month.** Decided by Nadia. Reason: founder budget constraint
  ("About 100 dollars a month for the AI stuff"). Reopen: when prototype measurements or user growth require it.
- **2026-10-14. Primary AI coding tool set to Claude Code (`targets = ["claude"]`).** Decided by Nadia.
  Reason: founder uses Claude Code. Reopen: if developer tooling changes.
- **2026-10-14. Technical stack: Web platform, Next.js, Cloudflare Pages, Supabase PostgreSQL, OpenAI API.**
  Test and build commands set to "none yet". Decided by Nadia accepting agent recommendation. Reason: hosted,
  standard, zero-cost start on free tiers (Supabase 500 MB database, Cloudflare Pages 500 builds/month).
  Reopen: if performance or compliance requires self-hosting.
- **2026-10-14. Strict caps required for free tier.** Requirement rows marked X created in `LAUNCH.md` for
  a per-user cap, a tighter guest cap, and a global daily AI inference circuit breaker. Decided by Nadia
  accepting agent recommendation. Reason: prevents runaway AI costs while allowing product trials; numerical
  limits left open until unit cost per scan is measured in prototype. Reopen: never without alternative spend bound.

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
