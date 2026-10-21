# Rejected proposals

Ideas the founder turned down, and why. Reopening one needs a new fact, not a fresh opinion.
Newest first. Each entry: date, the proposal, who proposed it, the reason it was rejected.

## This project

- (none yet)

## About the template itself

Setup removes this section from a new project (`tools/clean_template.py`).

### From the addyosmani/agent-skills comparison, 21 October 2026

Proposed by the orchestrator as the part of addyosmani/agent-skills not to take; Fadi agreed
("do as recommended"). Each comes back only with a new fact.

- **Slash commands (`/spec`, `/plan`, `/build`, `/ship`) and `/build auto`.** Declined: the
  founder never names a command here; the orchestrator routes.
- **A separate `CONSTRAINTS.md`.** Declined: the requirement rows, `skills/gates/` and
  `tools/known_red.json` are that file, and `floor_check.py` enforces its floor.
- **A mutation-score bar.** Declined for cost; coverage of changed lines is the bar offered.
- **The code-simplification skill.** Declined: `karpathy-guidelines` and the reviewer's "Simple"
  check cover it.
- **A second model's review through another vendor's CLI.** Declined as a rule; worth an
  experiment when a review misses something a second model would have caught.

### From the superpowers comparison, 18 October 2026

Proposed by the orchestrator as the part of obra/superpowers not to take; Fadi agreed ("do as
recommended"). Each comes back only with a new fact.

- **Delete any code written before its test** (the TDD iron law). Declined: test-first in
  `bug-fix` and the reviewer's "a test that would fail without the change" cover the same ground
  without discarding work.
- **Continuous execution without check-ins between tasks.** Declined: the founder's gates are
  the design, not an overhead.
- **A git worktree per task or agent.** Declined until parallel developers collide; the hand-off
  rule that nobody edits a shared file already prevents it.
- **A session-diagnosis skill** (why the process failed, with a scrubbed bundle). Declined:
  `p1-traps.md` and `optimizer` do this job.
- **The browser visual companion and its telemetry.** Declined: mockups are rendered with
  `tools/render_mockups.py`, and nothing in the template phones home.
- **One question per message in grilling.** Declined in favour of numbered rounds (TPL-51),
  which cost the founder fewer minutes.

### README style, 16 October 2026

Proposed by the orchestrator from the researcher's survey (`docs/growth/readme-survey.md`);
Fadi chose the calm document in ink and one accent.

- **README as a product landing page** (feature grid, "vibe coding vs this" row, practice table
  cut to five rows). Declined by Fadi, 16 October 2026: the calm document was chosen; the survey
  found it reads as marketing and gives the honest limits less room.
- **README opening with a terminal recording.** Declined by Fadi, 16 October 2026: a terminal
  tells a non-coder the project is for developers, and a video dates as the tool changes.
- **Images in the old warm paper style, only flattened.** Declined by Fadi, 16 October 2026, for
  ink and one accent. Superseded 17 October 2026: Fadi asked for the original style back, as it
  was (not flattened).
- **Hand-drawn, whiteboard-style images.** Declined by Fadi, 16 October 2026, for ink and one
  accent; handwriting is harder to read and can look less serious.

### Founder's technical level, 15 October 2026

- **Two levels only (non-technical or technical)**, offered by the assistant as the simpler
  option. Declined by Fadi in favour of three levels; no reason given.

### Start guide and single entry point, 15 October 2026

Offered by the assistant as the alternatives to the recommended options; declined by Fadi, no
reason given beyond choosing the recommendation.

- **Writing the guide for all four tools equally** (Claude, Codex, Gemini CLI, Cursor).
- **Keeping `/setup` as one command the founder types** before handing over to the project
  manager.
- **Drawn illustrations instead of real screenshots.**
- **Putting the whole guide inside the README.**

### Dashboard agent, 15 October 2026

- **Tracking the agents' own token spend** (the optimizer recording usage from the AI tool and
  the dashboard showing it), proposed by the assistant as an answer to the r/nocode comment.
  Declined by Fadi: the dashboard is for the project built from the template, not for the
  template itself.

### Researcher, feasibility and reviewer agents, 15 October 2026

- **A reviewer for code diffs only**, leaving documents to the readiness gate and spec-audit,
  proposed by the assistant as the recommended option. Declined by Fadi, who chose a reviewer
  for both documents and code; no reason given.
- **Business viability in the feasibility check** (market size, willingness to pay), offered by
  the assistant as an option. Declined by Fadi: feasibility judges building and running only.
- **Research only when the founder asks**, offered by the assistant as the cheaper option.
  Declined by Fadi: research runs before every first grilling round.

### Launch of the template, 14 October 2026

- **A launch article** (on a blog, dev.to or LinkedIn) built around the practice table, proposed
  by the assistant among ideas for bringing traffic to the repository. Declined by Fadi, who
  asked for everything else on the list; no reason given. The launch uses posts only
  (`examples/template-launch/`).

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

- **A separate designer agent**, and giving the designer the frontend-design skill. Declined by
  Fadi, 14 October 2026: design belongs to the frontend developer, with a software architect
  over the whole system. Brought back by Fadi on 15 October 2026 with a new fact (four
  platforms to design for) and taken; see closed decisions.

### From the repository audit (14 October 2026)

Proposed in an audit of the strategy drafts that read them as the repository; rejected by Fadi
on review. The useful methods went into the playbook, the architect and the region template.

- **Unsourced figures:** 60 to 80 percent drop-off from web to app, viral K-factors of 0.05 to
  0.15, a 22 percent payment haircut, 3.2 months of average subscription life, 85 percent
  bounce on calculator searches, 0 to 15 percent cache hits, refunds of 3 to 5 percent. Rule 10.
- **Competitor claims without sources:** Cal AI's revenue and its 424 paywall variants,
  MacroFactor's and Hevy's growth, Pieter Levels keeping 97 percent of revenue. Rule 10.
- **Programmatic pages on a separate domain to protect the main one.** An SEO claim with no
  source.
- **"Web checkout before install bypasses store commission legally."** Store payment rules
  differ by region; the playbook sends this to `legal`.
- **A 12 to 15 screen questionnaire to build sunk cost before the paywall, with an annual trial
  by default.** Onboarding used as pressure; ruled out by the no-dark-patterns rule.
- **Storing all user data on the device as the default architecture.** Kept only as an option.
- **The audit's citation of the UAE data protection law as Decree-Law No. 44 of 2021.** The
  packs cite No. 45 of 2021.

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
  income" and similar. Rejected under constitution rule 10. A project may use any of them once
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
  and the four-stage financial table. Rejected under rule 10: unsourced, or founder decisions.
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
