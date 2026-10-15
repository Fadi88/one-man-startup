# Closed decisions

What was decided, so nobody argues it again without a new fact. Newest first. Each entry: date,
decision, reason, who decided, what would make it worth reopening.

## This project

- (setup writes the first entries)

## About the template itself

Decisions taken while building the template. They explain why the template's files say what
they say. A project made from the template keeps them as background and adds its own above.

- **2026-10-15. Three more agents: researcher, feasibility and reviewer** (TPL-22 to TPL-24).
  The researcher runs before the first grilling round and its findings become options in it. The
  feasibility agent judges whether the idea can be built and run (stack, limits, cost, effort,
  blockers), not whether it will sell, which stays with `growth`. The reviewer reads both
  documents (spec, design, contract, tickets) and code diffs. All three are on by default.
  Reason: the founder wanted grilling to start from what similar products do, a build check
  before spending, and a second reader on every artifact. Decided by Fadi. Reopen: if the
  optimizer shows the extra runs cost more than the rework they prevent.

- **2026-10-14. The premise is building a software startup without writing code, and it is not
  vibe coding.** The README leads with that line and shows each step of the workflow beside the
  established practice it follows (TPL-18). Reason: the old line, "build real software without
  a tech team", did not say why the result can be trusted; the answer is that the agents follow
  the traditional, well-structured software workflow rather than prompting until it seems to
  work. Decided by Fadi. Reopen: if founders read "without writing code" as a promise that no
  technical judgement is ever needed.
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
  by `legal`. Reason: fake urgency is a dark pattern and a consumer law risk; the frontend
  developer's design rules already rule it out. Decided by Fadi, from review cycle 3.
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
- **2026-10-14. From the repository audit of 14 October, kept as methods:** carrying web work
  into the app after install; app attestation for free-tier endpoints; caching savings counted
  only once measured; a managed service before custom infrastructure; the paywall as an
  experiment; special categories of data in the region packs; data kept on the device as an
  option. Decided by Fadi.
- **2026-10-14. No separate designer.** The frontend developer designs and builds the user's
  side, using the frontend-design skill; the architect is the software architect for the whole
  system; the backend developer builds the server side. Decided by Fadi. Reopen: if design work
  outgrows one agent, shown by QA findings.
- **2026-10-14. Every rejected idea is recorded** (constitution rule 13), in
  `p1-rejected.md` the same day, whoever proposed it. Reason: without it, settled proposals come
  back as if new. Decided by Fadi, 14 October 2026.
- **2026-10-14. No unconfirmed assumptions** (constitution rule 11). Facts in anything the
  founder or a user reads are sourced, tested or measured, registered as assumptions, or cut.
  Decided by Fadi, 14 October 2026.
