# Rejected proposals

Ideas the founder turned down, and why. Reopening one needs a new fact, not a fresh opinion.
Newest first. Each entry: date, the proposal, who proposed it, the reason it was rejected.

## This project

- **2026-10-14. Enforcing strict gates during the idea stage.** Proposed by the setup agent.
  Declined by Nadia: "Can we go lighter? I want to move fast, it's just an idea." The setup
  agent explained the protection strict gates provide; Nadia settled on standard gates during
  development, committing to strict gates before onboarding real users.
- **2026-10-14. Enabling the social-media agent in the initial team roster.** Proposed by the
  setup agent. Declined by Nadia: "I don't need the social media one yet, I'll do that myself later."
- **2026-10-14. Uncapped free tier scans.** Evaluated during free tier discussion. Rejected by
  Nadia and barred by template rules: an open, uncapped free tier risks runaway AI inference
  costs. Nadia accepted strict caps, leaving specific numerical thresholds to be calibrated
  once unit costs are measured in the prototype ("I don't know the costs yet. Do what you
  recommend and I'll set the numbers when we know them.").

## About the template itself

### From the grilling that shaped the template, 14 October 2026

Options proposed by the assistant building the template and declined by Fadi.

- **Building the template inside the NutritionTracker repository.** Declined: the template is a
  separate public project (`Fadi88/one-man-startup`).
- **Claude Code only, or one plan tier only.** Declined: the template works with any AI coding
  tool. One source in plain Markdown, with generated adapters per tool.
- **Lighter gates for the template itself.** Declined: the template is strict. Projects made
  from it are asked at setup and recommended strict; the founder decides.
- **A default tech stack baked in.** Declined: the setup agent picks the stack with the founder.
- **An optimizer that applies its own changes**, even safe ones. Declined: it proposes; the
  founder decides each change.
- **A legal agent that writes final, publish-ready documents, or only checklists.** Declined
  both: checklists and drafts, always flagged as not legal advice.
- **Private or commercial licence.** Declined: public on GitHub under MIT.
- **Technical founders as the primary audience.** Chosen at first, then reversed by Fadi the
  same day: the template is positioned for non-technical founders first; developers can use it
  too.
- **Filling the B2C strategy with a real product** (one of the founder's own apps was offered
  as a candidate), **a first market, a platform, and keeping the strategy in a product
  repository.** Declined: the template starts no startup; these are each founder's to decide.

- **A brand kit in the template**, either the founder's own design system (steerai-design) or a
  generic brand-kit slot that setup fills. Declined by Fadi, 14 October 2026: left out for now;
  the template ships Anthropic's frontend-design skill only.
- **Plain-writing (humanizer) and Claude Code setup audit (cc-setup-audit) skills for the
  agents.** Offered with spec-completeness-audit; declined by Fadi, 14 October 2026. Only the
  spec audit was taken, rewritten in the template's own words.

### From the B2C strategy drafts

Proposals from the B2C strategy drafts (v1, v2 and review cycle 3, all 14 October 2026) that
were reviewed and left out of `docs/playbooks/b2c-organic-growth.md`. Proposed in the drafts;
rejected by Fadi on review. The useful parts of each draft went into the playbook.

- **"AI inference cost is a rounding error; gross margins of 75 percent or more are given."**
  Rejected as a premise: margin depends on the product, the price and above all the free tier.
  The playbook keeps margin as a target the founder sets and checks against a measured unit
  economics table.
- **A no-login trial calling premium models without caps** (v2). Rejected: an open path to the
  founder's AI bill. Replaced by the strict free tier and its tiers of access.
- **Keyword-swapped landing pages generated in bulk** (v2). Rejected: the kind of thin content
  search engines' spam policies target. Replaced by working tools behind a quality gate.
- **Market statistics stated without sources** (review cycle 3): UAE smartphone ownership and
  iOS share, WhatsApp as the main channel, German and French as the highest-paying European
  segments, "over 35 percent of software discovery happens in AI search", "high disposable
  income" and similar. Rejected under constitution rule 11. A project may use any of them once
  it has a dated source.
- **Fixed prices and rates in a template** (review cycle 3): AED 49 a month, 12 euros a month,
  0.00015 and 0.008 dollars per request, merchant of record and app store fee percentages, 15
  percent visitor to trial and 4 percent trial to paid. Rejected: prices are founder decisions,
  fees come from each provider's page with a date, and rates are assumptions until measured.
- **"No consent banner is needed with cookieless analytics."** Rejected as a blanket claim; see
  the closed decision of the same date.
- **A 30 percent discount if upgraded within 24 hours**, as a default. Rejected as a default;
  allowed only with a real deadline and `legal` checking the wording.
- **"Pages publish only with at least 40 percent unique data"** and **"failover within 2000
  ms"**. Rejected: precise numbers with nothing behind them. The playbook keeps the quality gate
  and the fallback provider, with the founder setting the bar.
- **"Mandate a merchant of record."** Rejected as a mandate; kept as one of two options the
  founder chooses between.
- **Tying the strategy to Europe and the UAE.** Rejected for the template; markets come from
  each project's `project.toml`.

### From strategy review cycle 7 (14 October 2026)

Proposed in the v7 draft; rejected by Fadi on review. The useful methods went into the playbook.

- **Production code and a database schema in the strategy** (an edge gateway, Redis keys, SQL
  tables). Rejected for the template: the stack and the code are each project's, built through
  the feature track. The principles behind them are in the playbook. The draft's gateway also
  checked its limits before counting, so two requests at once could both pass.
- **A named stack** (Cloudflare, Hono, Next.js, Supabase in Frankfurt, Upstash, Paddle,
  RevenueCat, Expo). Rejected: setup picks the stack with the founder.
- **Fixed figures** again: a 15 dollar an hour circuit breaker, 0.80 dollars a day for new
  subscribers, prices in euros and dirhams, 60 percent annual mix, churn of 4.5 to 15 percent,
  "90 percent input cost reduction", "3 times higher click-through", "DR 0 to DR 28", "Google's
  sandbox for 3 to 6 months", "LLMs index GitHub within hours", 400 characters before indexing,
  and the four-stage financial table. Rejected under rule 11: unsourced, or founder decisions.
- **"Parasite SEO" and seeding 30 to 50 high-ranking threads** with links to the product.
  Rejected: it breaks most communities' rules and the social media agent's rules. Kept instead:
  genuine answers, rules read first, the connection disclosed.
- **"Three mandatory native features" to pass app review.** Rejected as a rule nobody published;
  kept as "read the current store guidelines before designing a store app".
- **Copy-paste legal text** (a withdrawal waiver checkbox citing a directive article, an AI Act
  footer). Rejected: legal wording is drafted by `legal` for the project's regions and flagged
  for counsel. The topics went into the region pack template.
- **A "Personal Context Vault" as a switching-cost moat.** Rejected as framing: retention comes
  from value, and export is always one click. Saved history as a feature is kept.
- **A cancellation "salvage flow" with a discount before cancelling**, as a default. Rejected as
  a default; allowed only if cancelling stays one clear path and `legal` approves it per region.
- **Annual plan pre-selected by default.** Rejected as a default; `legal` decides per region.
- **A niche list of expat, tenancy, employment, tax and visa tools** for Europe and the UAE.
  Rejected for the template: the product is the founder's. Noted for any project choosing such
  tools: legal, tax and employment answers are a high-risk category for `legal` to review.
- **Publishing open-source modules under a named personal GitHub account.** Rejected: where code
  is published is each founder's choice.
