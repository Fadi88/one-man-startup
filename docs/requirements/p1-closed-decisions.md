# Closed decisions

What was decided, so nobody argues it again without a new fact. Newest first. Each entry: date,
decision, reason, who decided, what would make it worth reopening.

## This project

- (setup writes the first entries)

## About the template itself

Decisions taken while building the template. They explain why the template's files say what
they say. Setup removes this section from a new project (`tools/clean_template.py`).

- **2026-10-21. Eight practices from addyosmani/agent-skills are taken** (TPL-66 to TPL-73), from
  the orchestrator's comparison of its 25 skills, 4 reviewer personas and 7 checklists with this
  template (read 2026-10-21): a performance skill (targets as the founder's rows, measure before
  and after, keep or revert, a sourced scorecard), an observability skill (questions first,
  structured logs with a request id, RED metrics as percentiles, symptom alerts with runbooks,
  the staging proof), schema expand-then-contract and deprecation rules, the floor as a check
  (`tools/checks/floor_check.py`), reviews briefed without the author's reasoning, contract
  rules with idempotency keys, test shape, and flags for incomplete work. No new agent: their
  web-performance-auditor is `qa`'s pre-release scorecard, their code-reviewer, test-engineer and
  security-auditor are `reviewer`, `qa` and `security`. Decided by Fadi ("do as recommended").
- **2026-10-18. Nine practices from obra/superpowers are taken** (TPL-57 to TPL-65), from the
  orchestrator's comparison of its fifteen skills with this template (read 2026-10-18): excuse
  tables and red flags in the discipline skills, fresh evidence for every green claim, rulings
  in `status.md`, a review focus in every spec, a capped review fix loop, a method for answering
  reviews, a session-start and post-compaction hook, typed confirmation for discards, and
  anti-goals, playback and the spike rule in grilling. One deviation: superpowers asks one
  question per message, and grilling keeps its numbered rounds, which cost the founder fewer
  minutes (TPL-51). Its trigger-only skill descriptions run as experiment 3 on three skills
  before any wider change. Decided by Fadi ("do as recommended").
- **2026-10-17. The Fuel & Train lessons are taken** (TPL-41, TPL-41a, TPL-44 to TPL-56), from pull
  request 2, all as proposed except: the per-platform agents are one `platform-architect` and
  one `platform-designer` for any platform, not one per platform; lesson 4's helper that mines
  the old app's rows is written as steps (TPL-41a), not built as a tool, since its input depends
  on how the old app keeps its requirements; and lesson 14 changes nothing, because
  `.gitattributes` already sets `* text=auto eol=lf`. Decided by Fadi ("fix everything").
- **2026-10-17. Publishing is off in a new project until the founder asks** (TPL-43). Setup's
  clean-out switches `[publish] enabled` to false and the checks refuse any publishing or
  deploying workflow while it is. Reason: tracker_app's first push ran the template's landing
  page job and failed; nothing should go public by default. Decided by Fadi.
- **2026-10-17. A narrow "check" access for agents told to run checkers** (TPL-42). Legal,
  the orchestrator, researcher, growth, social-media, architect, product-designer and security
  were told by their own skills to run `python tools/...` checkers but had no way to. They get
  `check` access, which runs only the read-only checkers; in Claude Code a hook generated into
  each agent blocks every other command (A-12). Other tools read it as an instruction only.
  Chosen over full run access, which would let them run anything. Decided by Fadi.
- **2026-10-17. The team table lives in `docs/TEAM.md`** (TPL-4). `AGENTS.md` was a few characters
  under its budget, so each new agent forced cuts to the rules. The check now reads the
  table from `docs/TEAM.md` and `AGENTS.md` keeps a pointer. Declined: raising the budget (every
  tool loads `AGENTS.md` every session) and tightening the wording (little room, blurrier rules).
  Decided by Fadi. Reopen: if tools stop finding the team without the table in `AGENTS.md`.
- **2026-10-17. A rebuild of an existing app is its own setup answer** (TPL-41). Setup asks new
  idea or rebuild; a rebuild starts from the original's public features and adds a legal check
  that nothing of the original's own is copied. Declined: only a fifth stage value, which would
  not make the legal check happen. Decided by Fadi.
- **2026-10-17. Setup checks the repository is private, and the founder decides** (TPL-39,
  TPL-40, TPL-42, with the budget wording and legal running the link checker). Lessons from the
  first runs, all fixed as proposed. Decided by Fadi.
- **2026-10-16. The README is a calm document in ink and one accent** (TPL-38). The promise, a
  start link and the recorded demo come first, then the journey, team and approval diagrams,
  then getting started; the practice table, limits and glossary follow. Every README image is
  flat: white or dark grey, near-black or near-white text, one deep blue accent, no gradients,
  glows or shadows. Reason: the survey of 14 similar projects (`docs/growth/readme-survey.md`)
  found restraint, plain language and honest limits are where this template stands apart, and
  the reader is a non-coder who has to trust it. Decided by Fadi. Reopen: if the landing page's
  numbers show readers leave before the start link. **Image style reversed by Fadi on
  2026-10-17**: the six README images are back in the original warm paper style, with the same
  words and diagrams; the README's order and start link stay.

- **2026-10-16. The reviewer suggests new agents as the project changes** (TPL-37). Setup
  picks the team once; after that, each review checks whether the work needs an agent that is
  switched off or does not exist yet, and suggests it, never as a blocking finding. The founder
  decides, through the orchestrator; a yes reruns setup's team question, a no goes to
  `p1-rejected.md`. Reason: the founder wanted the team to grow with the project instead of
  staying as setup left it. Decided by Fadi. Reopen: if the suggestions are mostly declined.

- **2026-10-15. Six more agents: rollback, debugger, agentic workflow, Android, iOS and desktop**
  (TPL-32 to TPL-35). `rollback` is called by `qa` on a major error live; since only the
  orchestrator starts agents, QA writes the verdict ROLLBACK and the orchestrator starts
  `rollback` before anything else. The rollback itself still waits for the founder's go
  (constitution rule 2). `debugger` finds the cause of hard bugs and incidents. `agentic-workflow`
  designs the AI workflows inside the product, not the template's own agent team (that stays
  with `optimizer`). All six are on by default, and setup recommends each only when the project
  needs it. Decided by Fadi. Reopen: if the optimizer shows an agent is never used or costs more
  than it saves.

- **2026-10-15. A product designer, and one developer per platform** (TPL-35, TPL-36).
  `product-designer` designs what users see for every platform the product has, in one
  `ux.md` with one design system and a section per platform; `web-dev`, `android-dev`,
  `ios-dev` and `desktop-dev` build it and never redesign it. `frontend-dev` is split into
  `product-designer` and `web-dev`. This reverses "No separate designer" (14 October). The new
  fact: with four platforms, one agent designing and building all of them would make the
  design differ from platform to platform. Decided by Fadi. Reopen: if the hand-off between
  designer and developers costs more rework than it saves, shown by review and QA findings.

- **2026-10-15. Setup removes the template's own content from a new project** (TPL-30): its
  decisions and rejected ideas, experiments, assumptions, landing page, examples, marketing
  diagrams and README, on the founder's go, by a script whose result the sweep rehearses on a
  scratch copy every run. Reason: a test project began deleting the template's history on its
  own, and a founder should start from clean files. Decided by Fadi. Also decided: Claude Code
  showing each file change in the terminal is fine for founders, so nothing hides it.
- **2026-10-15. Setup asks for the product's licence, and is split into one file per step**
  (TPL-31). The licence question explains all rights reserved, MIT, Apache 2.0, GPLv3 and
  AGPLv3 with what each means for the business, recommends all rights reserved unless open
  source is part of the plan, and is flagged as not legal advice. The template's own MIT notice
  stays in every project (`docs/licenses/one-man-startup.txt`), as MIT requires. Setup's
  sections are now `skills/setup/1-check-tools.md` to `4-finish.md` and `licences.md`, linked
  from `skills/setup/SKILL.md`. Decided by Fadi.

- **2026-10-15. Three technical levels for the founder, and every agent words to it** (TPL-28,
  TPL-29). `project.toml [owner] level` is non-technical, basics or technical; setup asks, the
  grilling asks first when it is unset, and `skills/founder-voice/` sets the wording of every
  question, approval and report, with no technical terms for a non-technical founder. Reason:
  the template is mainly for founders who do not code. Seen working on 2026-10-15 in Claude
  Code on a set-up copy at the non-technical level: a subscription request gave a plain status
  update and a multiple-choice round with a recommendation and no technical terms; the tool's
  own display of file changes still showed. Decided by Fadi. Reopen: if founders at
  one level keep asking for more or less detail.

- **2026-10-15. One entry point and a start guide for non-coders** (TPL-26, TPL-27). The
  founder talks only to the project manager, which starts setup by itself; the guide never asks
  for a command. The guide follows one path: GitHub, GitHub Desktop, then Claude Code in a
  terminal, where the founder types only the install line and `claude` (changed the same day
  from the Claude desktop app, at Fadi's request, so the screenshots could be taken of a real
  session). It lives in `docs/START-HERE.md` linked first from the README and the landing page,
  and uses real screenshots. The single entry is set in `AGENTS.md`, not with Claude Code's
  `agent` setting: that setting is documented for the terminal only, and it would give the main
  session the project manager's tools, which cannot run the checks. Decided by Fadi. Reopen: if a
  tool does not follow the instruction (A-9, A-10).

- **2026-10-15. A dashboard agent** (TPL-25). The template gets a `dashboard` agent that builds
  the founder's private dashboard; for a product that uses AI, it shows usage and spend and
  gives the founder controls (caps, pause, model choice) with an audit log. On by default, and
  setup recommends it from the start for any product that pays per action. Reason: an AI
  product needs its usage watched and controllable. Prompted by a comment on r/nocode:
  https://www.reddit.com/r/nocode/comments/1x5u68s/comment/pgu1yl2/ which reads, as pasted by
  Fadi: "Pregunto, hiciste métrica de tokens? Cuánto gastaste en lo que hiciste? Tenés tu propio
  sistema de control? Está buenísima la idea" (in English: did you measure tokens? How much did
  you spend on what you built? Do you have your own control system? Great idea). Decided by Fadi. Reopen: if the optimizer finds the dashboard
  costs more to keep than it saves.

- **2026-10-15. The "one author" rule is removed** from the constitution (it was rule 10;
  rules 11 to 13 are now 10 to 12). Commits may credit a tool or model and may come from any
  author; the commit-msg hook now refuses only banned characters (TPL-7). Decided by Fadi, no
  reason given. The settings that switch off Claude Code's credit lines moved from the shared
  `.claude/settings.json` to this repository's untracked `.claude/settings.local.json`, so they
  apply only to the template's own repository and not to projects made from it. Reopen: if
  the founder wants the history to carry one name again.

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
  outgrows one agent, shown by QA findings. **Reversed by Fadi on 2026-10-15** (a product
  designer and one developer per platform, above).
- **2026-10-14. Every rejected idea is recorded** (constitution rule 12), in
  `p1-rejected.md` the same day, whoever proposed it. Reason: without it, settled proposals come
  back as if new. Decided by Fadi, 14 October 2026.
- **2026-10-14. No unconfirmed assumptions** (constitution rule 10). Facts in anything the
  founder or a user reads are sourced, tested or measured, registered as assumptions, or cut.
  Decided by Fadi, 14 October 2026.
