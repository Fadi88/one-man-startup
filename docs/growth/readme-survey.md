# README survey: projects similar to One-man startup

Read on 2026-10-16. Purpose: input for redesigning our README's visual style and for positioning.

## How this was done, and its limit

I opened the GitHub page of each project below on 2026-10-16 and read the README as the page returned it. The fetch tool passes the page through a small summarising model, so what I recorded is that tool's description of the page, not my own look at the rendered page. Two consequences:

- Star counts are exactly as the page showed them that day. They are a snapshot.
- Visual details (banner, GIF, dark-mode image pairs, collapsible blocks) are as reported. Where the report said it could not tell, I say "not confirmed". Before copying any style, open the page in a browser to check.
- gstack's page was longer than the tool read; the last 12,962 characters were not read.

Our own README (README.md, read the same day) has: an SVG hero, a recorded-dry-run SVG, a journey SVG, a team SVG, a "your call" SVG, an architecture SVG, a "not vibe coding" table, a glossary table, no badges, no emoji, about 208 lines. I did not check whether our SVGs adapt to dark mode.

## The job

Give a person a ready-made structure so an AI coding tool builds software in a disciplined way, not by guesswork. Search basis: our Credits list, plus the names the founder suggested, plus ChatDev, MetaGPT and OpenHands as the multi-agent "software company" family.

## Summary table

| Project | Stars (read 2026-10-16) | For whom | Hero | Badges | Length | Demo |
|---|---|---|---|---|---|---|
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 54.2k | Developers and small teams | Wide banner plus delivery-loop SVG | 3 | Medium | None |
| [spec-kit](https://github.com/github/spec-kit) | 141.5k | Developers | Logo | 4 | Long | Video linked, not embedded |
| [gstack](https://github.com/garrytan/gstack) | about 136.6k | Developers and technical founders | None | None | Very long (8,000+ words) | Text transcript |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 293.4k | Working engineers | Banner linked to newsletter | 1 | About 2,000 words | None |
| [obra/superpowers](https://github.com/obra/superpowers) | about 300.3k | Developers | None | None | Long (1,300 to 1,500 words) | None |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 23.9k | Claude Code developers | None | Many | Long | None |
| [wshobson/agents](https://github.com/wshobson/agents) | 40.9k | Developers | None | None | About 1,000 words | None |
| [contains-studio/agents](https://github.com/contains-studio/agents) | 12.4k | Developers, small studios | None | None | About 1,000 words | None |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | 5.5k | Developers | One image | None | About 250 words | None |
| [claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 28.2k | Developers in AI editors | Logo | About 7 | Long | None |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.9k | Developers, researchers | Logo plus schematic | 3 | About 800 to 1,000 words | Hugging Face Space, video |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | 34.5k | Non-coders and developers | Centered logo | None | 2,000+ words | Many GIFs, workflow gallery |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | about 91k | Engineering teams | Logo plus screenshot | 5 | About 1,000 words | One screenshot |
| [Ruflo (was claude-flow)](https://github.com/ruvnet/claude-flow) | 75.3k | Claude Code and Codex developers | Animated GIF, terminal recording, video | 6 | Very long | Recording, console tour |

Not in our Credits: superpowers, SuperClaude, wshobson/agents, contains-studio/agents, agent-os, claude-task-master, MetaGPT, ChatDev, OpenHands, Ruflo. That is ten, above the required five.

Two repo notes: the OpenHands URL now describes "Agent Canvas", a self-hosted control center for coding agents, so it is a different pitch from the older OpenHands coding agent. The claude-flow URL now presents the project as "Ruflo".

## Project by project

Each entry: what it is, visual style, what works and what does not for a non-technical reader, positioning, and where we differ. Source for every entry is the URL in its heading, read 2026-10-16.

### 1. BMAD-METHOD (https://github.com/bmad-code-org/BMAD-METHOD, 54.2k stars)

- **What it is:** An agile framework for AI-driven development. Opens with "Agile Ai Driven Development: turn an idea or change request into working software without giving up the thinking." For developers and small teams.
- **Visual style:** Wide banner, then three badges (version, MIT, Discord), then a delivery-loop SVG diagram. One table (six modules). Bulleted "Why BMad?". No emoji, no collapsibles, no screenshots, no demo. Medium length. "What is this" is right after the banner; "Start Building" follows the diagram, within one or two screens.
- **Works:** The tagline and "Why BMad?" bullets state the value plainly. The loop diagram gives a fast picture. Links to tutorials.
- **Does not:** Dense unexplained jargon (spec-driven, context engineering, skills, `npx`, `uv`). Two install tracks (stable and a V7 alpha) confuse the choice. Odd title casing. No screenshot or demo.
- **Positioning:** A counterweight to raw coding assistants that "turn unstated assumptions into code". Free, open source, covers planning, specs, architecture and review.
- **Where we differ:** We write for someone who never opens a terminal, define every term, and show a real recorded session.

### 2. spec-kit (https://github.com/github/spec-kit, 141.5k stars)

- **What it is:** "An open source toolkit that gives AI coding agents structured processes." Tagline: "Build with a spec, fix a bug, or assess an idea." For developers comfortable in a terminal.
- **Visual style:** Logo, four badges, language switcher (English, Chinese, Japanese, Korean). No diagrams or screenshots. A video is linked, not embedded. A star-history chart near the bottom. Two tables ("Choose your process", a dozen-row "Capabilities"). Light emoji. Long. "How to start" is the third block, after the two tables.
- **Works:** "Choose your process" is a table of plain questions mapped to outcomes. Entry points are independent, not a forced sequence.
- **Does not:** Jargon (SDD, primitives, integration keys, bundles). Capabilities table is dense. Setup needs Python tooling and slash commands.
- **Positioning:** Process-agnostic, extensible, works with many agents. Names no rivals.
- **Where we differ:** Ours is a complete team and a guided story, not a toolkit of parts.

### 3. gstack (https://github.com/garrytan/gstack, about 136.6k stars)

- **What it is:** About 23 role-based slash-command skills for Claude Code (CEO, designer, reviewer, QA, security, release). "Use Garry Tan's exact Claude Code setup." Aimed at developers and technical founders, though it lists "Founders and CEOs" and first-time Claude Code users.
- **Visual style:** No banner, no badges, almost no emoji. Opens with a Karpathy quote and the author's story ("I'm Garry Tan, President & CEO of Y Combinator"). Only two images: GitHub contribution-graph screenshots. Heavy tables. The sprint is a text arrow chain (Think, Plan, Build, Review, Test, Ship, Reflect). A text example session stands in for a demo. Very long. Quick start after roughly 700 to 1,000 words.
- **Works:** The "virtual engineering team" metaphor lands at once. The worked example (a daily briefing app) shows the flow in plain steps. The author's credibility does the selling.
- **Does not:** Jargon (Bun, CSO, OWASP, STRIDE, MCP, ACP). Long install caveats. Bold productivity claims ("about 810x my 2013 pace") that the README itself says are contested. A hiring aside interrupts.
- **Positioning:** An opinionated workflow layer on Claude Code, complementary to CLAUDE.md rule sets. Leans on the author's name and breadth.
- **Where we differ:** We do not rely on a famous author; we rely on a visible process, and we address a founder who does not code.

### 4. mattpocock/skills (https://github.com/mattpocock/skills, 293.4k stars)

- **What it is:** "My agent skills that I use every day to do real engineering - not vibe coding." Skills for Claude Code, Codex, Copilot. For working engineers.
- **Visual style:** A banner linked to a newsletter, one badge (skills.sh). No tables, diagrams, screenshots, collapsibles or emoji. About 2,000 words. "Installation (30-second setup)" comes before the long "Why These Skills Exist". No demo.
- **Works:** Fastest path to "how to start" of the set. "Why These Skills Exist" frames the problem as relatable failures (the agent misunderstood you, the code broke). Candid tone; admits what a skill will not fix.
- **Does not:** Jargon (tracer-bullet, deep modules, ADRs, red-green-refactor). Per-agent install commands. Dense reference list. No visuals of the tool in use.
- **Positioning:** Directly against process frameworks (GSD, BMAD, Spec-Kit) that "take away your control"; small, editable, composable skills.
- **Where we differ:** Same "not vibe coding" phrase. We are the opposite bet: a whole owned process for people who cannot steer small pieces themselves.

### 5. obra/superpowers (https://github.com/obra/superpowers, about 300.3k stars)

- **What it is:** "A complete software development methodology for your coding agents, built on top of a set of composable skills." For developers across Claude Code, Cursor, Codex, Gemini CLI.
- **Visual style:** No hero, no badges, no tables, diagrams, screenshots or emoji. Plain text with a table of contents. A numbered list of seven skills is the workflow. Install is the third section, with 17-plus per-tool install blocks. About 1,300 to 1,500 words.
- **Works:** "How it works" is plain: it does not jump into code when you say you are building something. Honest "When Something Goes Wrong" and telemetry disclosure.
- **Does not:** Jargon (subagent-driven-development, RED-GREEN-REFACTOR, YAGNI). Install blocks dominate. Nothing visual.
- **Positioning:** "Mandatory workflows, not suggestions"; names no rivals; social proof is the star count.
- **Where we differ:** We have pictures and a story; they prove that a plain text page can still win with a strong idea and a clear first paragraph.

### 6. SuperClaude (https://github.com/SuperClaude-Org/SuperClaude_Framework, 23.9k stars)

- **What it is:** A configuration framework adding slash commands, agents and modes to Claude Code. "Transform Claude Code into a Structured Development Platform." For existing Claude Code developers. States it is not affiliated with Anthropic.
- **Visual style:** No hero image. A wall of badges (Smithery, Awesome Claude Code, sibling frameworks, version, tests, MIT, PyPI, npm, languages). Bold statistics (30 commands, 20 agents, 7 modes, 8 MCP servers). Several tables, one collapsible (the full command list), heavy emoji in headings. Long and repetitive.
- **Works:** Statistics up front, clear non-affiliation note, scannable tables.
- **Does not:** Badge clutter. Undefined jargon (meta-programming, MCP). Version mismatch between heading (v4.1) and badge (4.3.0). Describes features not yet available (v5.0 plugins). Unsupported speed and token claims. Donation ask.
- **Positioning:** A layer on top of Claude Code that adds breadth; reads as a catalogue.
- **Where we differ:** We show no counts as proof and we keep claims checkable. (Their version mismatch is a reminder to keep our README's claims in step with the repo.)

### 7. wshobson/agents (https://github.com/wshobson/agents, 40.9k stars)

- **What it is:** "Plugins, agents, and skills for AI coding tools." A catalogue (94 plugins, 202 agents, 185 skills, 105 commands as shown that day) usable from seven tools. For developers.
- **Visual style:** No hero, badges, diagrams, emoji or screenshots. Four tables (harness support, quick-start plugins, component counts, docs map). One image only: a star-history chart at the bottom. About 1,000 words. First paragraph answers "what"; "Quick start" follows the harness table.
- **Works:** The "Use it for" table maps tasks to plugins. Headline counts show scale. Honest caveat that its evaluation scores are not validated against human labels.
- **Does not:** Jargon (harness, agentic, adapter, TOML), defined only once. Nothing shows output. Install varies by tool.
- **Positioning:** Breadth and one Markdown source for seven tools. Names no rivals.
- **Where we differ:** A catalogue is a shelf; we are a guided route.

### 8. contains-studio/agents (https://github.com/contains-studio/agents, 12.4k stars)

- **What it is:** Specialised agents for Claude Code in departments (engineering, product, marketing, design, testing), for fast "6-day sprints". For developers and small studios.
- **Visual style:** No hero, badges or tables. Bulleted lists. One text directory tree. Heavy emoji in headers and checklists. "What is this" under the title, then install, then quick start. About 1,000 words.
- **Works:** "Example Usage" maps everyday requests to agent names ("Make this loading screen more fun" goes to `whimsy-injector`). Each agent has a punchy tagline. The department structure is easy to grasp.
- **Does not:** Install assumes git, terminal and `~/.claude/`. Unexplained jargon (YAML frontmatter, MultiEdit). Nothing shows an output.
- **Positioning:** "Sharing current agents in use"; department structure and personality.
- **Where we differ:** The department idea is close to our team chart. We add the gates, the decision log and the founder-level voice.

### 9. Agent OS (https://github.com/buildermethods/agent-os, 5.5k stars)

- **What it is:** "Agents that build the way you would." A system for injecting your codebase standards and writing better specs. Works with Claude Code, Cursor and others. For developers.
- **Visual style:** One title image, horizontal rules, four "Core capabilities" bullets, one emoji. About 250 words. "How to start" is not in the README; it points to buildermethods.com/agent-os.
- **Works:** Shortest of the set. The tagline is plain English. The promise is clear.
- **Does not:** "Spec-driven development", "codebase standards", "injecting" unexplained. No example or demo. Install lives elsewhere.
- **Positioning:** A complementary layer, language and framework agnostic.
- **Where we differ:** Ours answers "how do I start" on the page and links a step-by-step guide.

### 10. claude-task-master (https://github.com/eyaltoledano/claude-task-master, 28.2k stars)

- **What it is:** "A task management system for AI-driven development, designed to work seamlessly with any AI chat." For developers in Cursor, Windsurf, Roo, Claude Code.
- **Visual style:** Logo linked to the site; about seven badges (CI, stars, npm, license, three download counters, Discord, Trendshift). A one-click Cursor install badge in a dark-theme version (the only dark-mode-aware image in the set). Two tables (config paths, tool-loading modes). Light emoji. Long. Images are only the logo, a hiring banner, a contributors graph, a star-history chart.
- **Works:** One-sentence summary near the top. One-click install is the most friendly start of the set. Community links as social proof.
- **Does not:** MCP, CLI, npm, JSON, environment variables with no glossary. JSON config blocks and API-key steps. No visual of the tool in use.
- **Positioning:** Editor-agnostic, multi-provider, bring your own keys.
- **Where we differ:** We never ask the reader to edit a config file.

### 11. MetaGPT (https://github.com/FoundationAgents/MetaGPT, 70.9k stars)

- **What it is:** "The Multi-Agent Framework: assign different roles to GPTs to form a collaborative entity for complex tasks." Product manager, architect, project manager, engineer. For developers and researchers.
- **Visual style:** Logo, a role schematic, three badges (MIT, Discord, X). Emoji throughout. No tables. News section sits before the explanation, delaying "what is this". Demo: a Hugging Face Space to try without installing, an embedded video, a YouTube link. About 800 to 1,000 words.
- **Works:** "One line requirement in, software artifacts out" is easy to grasp. A try-it-without-installing link is the strongest low-friction demo in the set.
- **Does not:** SOP, LLM, "Code = SOP(Team)" unexplained. Install needs Python versions, Node, pnpm, config editing. News first.
- **Positioning:** The "AI software company" as a multi-agent system, with academic credibility (ICLR, paper) and a commercial product link.
- **Where we differ:** Same "software company of agents" idea, but they simulate it in a framework for builders; we hand it to a founder who stays in charge.

### 12. ChatDev (https://github.com/OpenBMB/ChatDev, 34.5k stars)

- **What it is:** "ChatDev 2.0 - DevAll: a Zero-Code Multi-Agent Platform for Developing Everything." For non-coders who want to orchestrate agents, and developers who extend it.
- **Visual style:** Centered logo, no badges. Many GIFs (web console tutorial, workflow, launch), a Featured Workflows table pairing demo GIFs with example prompts, heavy emoji in headers, a language link. Long (2,000+ words) and News-first, so Quick Start is a screen or more down.
- **Works:** Plain-language overview. The workflow gallery shows concrete outputs with the prompt that made them, which is the clearest "see it" in the set for a lay reader.
- **Does not:** "Zero-code" clashes with a setup needing uv, Node, Vite, Docker and YAML. Long News and ChatDev 1.0 history dilute the message.
- **Positioning:** Successor to the software-company simulation, widened to "everything", backed by arXiv and NeurIPS 2025.
- **Where we differ:** The only other project here that names non-coders as an audience. We do it with a process and a guided start; they do it with a visual platform.

### 13. OpenHands (https://github.com/All-Hands-AI/OpenHands, about 91k stars)

- **What it is:** Now presented as "Agent Canvas": "The self-hosted developer control center for coding agents and automations." Runs OpenHands, Claude Code, Codex, Gemini. For developers and engineering teams.
- **Visual style:** Logo, five badges (beta, CI, npm, docs, Slack), a quick-nav link row, one automation screenshot, six bold feature blurbs, an architecture image, one table, two clear warning callouts about full file access. No emoji in the body. About 1,000 words. Install paths ordered from simplest to most advanced.
- **Works:** Feature blurbs are skimmable. Safety warnings are prominent and plain. Simplest-first install order.
- **Does not:** ACP, uv, Docker sandbox, environment variables unexplained. Four install paths. Assumes you know what a coding agent is.
- **Positioning:** A hub that hosts any agent, flexible hosting, Slack and GitHub integrations.
- **Where we differ:** They run agents; we decide what agents may do and who approves it.

### 14. Ruflo, formerly claude-flow (https://github.com/ruvnet/claude-flow, 75.3k stars)

- **What it is:** "An agent meta-harness for Claude Code and Codex": multiple agents, shared memory, coordination. For developers.
- **Visual style:** The most media-rich README: an animated neon-sign GIF, a looping terminal recording, a console demo video, SVG diagrams (learning loop, federation), a text architecture flow, about six badges (one links to the old repo name), moderate emoji, many tables including "Claude Code Alone vs. + Ruflo". Very long. Install appears before the explanation.
- **Works:** Analogies ("Slack for Agents"; Agent = Model + Harness). Reassurance: "You don't need to learn 314 MCP tools or 26 CLI commands." Honest note that the workflow animation uses sample data.
- **Does not:** Dense jargon (HNSW, Raft, Byzantine, mTLS). Name confusion between Ruflo and claude-flow. Self-reported benchmarks (for example "89% accuracy") linking to an external gist. Too many paths before a first step.
- **Positioning:** A layer over Claude Code and Codex, compared against LangGraph, AutoGen and CrewAI.
- **Where we differ:** We make no benchmark claims and we have no marketplace; we sell a way of working.

## Synthesis

### Visual patterns the better READMEs share

1. **A one-sentence promise right under the title, before any install.** BMAD, spec-kit, mattpocock/skills, superpowers, wshobson/agents, contains-studio, Agent OS, task-master, ChatDev, OpenHands. (The ones that bury it: MetaGPT and ChatDev put News first; gstack and Ruflo put a story or install first.) Ours already does this.
2. **A single process picture early.** BMAD (delivery-loop SVG), MetaGPT (role schematic), Ruflo (flow and SVGs), OpenHands (architecture image), gstack (text arrow chain). Ours has journey and team SVGs.
3. **A table that turns a menu into a choice.** spec-kit "Choose your process", wshobson "Use it for", gstack sprint-role table, BMAD module table. Tables work when the left column is a question or a task, not a product term.
4. **Showing a real result, not describing one.** ChatDev (GIF gallery with the prompt beside each), MetaGPT (try-it Space), Ruflo (recorded console), gstack (example session), contains-studio (request-to-agent examples). Ours has the word-for-word dry-run SVG, which is rare.
5. **Install in one short block, early, simplest first.** mattpocock/skills (30-second setup), task-master (one-click Cursor), OpenHands (simplest to hardest). Counterexamples: superpowers (17 blocks), Agent OS (none on the page).
6. **Restraint with badges.** The cleanest pages have none to four (BMAD 3, spec-kit 4, MetaGPT 3); the most cluttered have six or more (SuperClaude, task-master, Ruflo). Social proof is a star count or a Discord link, not a wall.
7. **Plain, candid limits.** mattpocock/skills (admits what it will not fix), superpowers (when something goes wrong, telemetry), OpenHands (full file access warnings), wshobson (scores not validated). Honesty reads as trust.
8. **A clear named enemy or contrast.** mattpocock/skills (process frameworks), BMAD (raw assistants), our own "not vibe coding". A one-line contrast sells faster than a feature list.

Gap across the whole set: almost none show a screenshot or picture of what a user sees. Emoji are split between none (gstack, superpowers, wshobson, BMAD) and heavy (SuperClaude, contains-studio, ChatDev, MetaGPT). Dark-mode-aware images were confirmed in only one place (task-master's install badge); this is a gap an SVG hero could close if ours does not already.

### Three style directions for our README

**A. Product landing page.**
- Change: a stronger hero with one sentence and one button ("Start here"), a three-step strip, a short testimonial-style demo (the dry run), a features grid of six blurbs, a comparison row "vibe coding vs this". Cut the "not vibe coding" table down to five rows and move the rest to a docs page. Keep SVG art.
- Borrows from: OpenHands (feature blurbs, warnings), ChatDev (demo gallery), Ruflo (hero, comparison table), task-master (one-click start).
- Risk for a non-technical reader: low on comprehension, medium on trust. It can feel like marketing and the founder base is wary of hype; a long features grid also hides the honest limits that are part of our appeal.

**B. Calm document with diagrams.**
- Change: keep the current order and voice, tighten to one screen of promise, then the journey diagram, the team diagram, a short "what stays in your hands" box, the start link. Move the long practice table and "good to know" detail below or into docs. Consistent diagram style, no badges, no emoji.
- Borrows from: BMAD (tagline then loop diagram), superpowers (plain "how it works"), mattpocock/skills (candid tone), wshobson (task table).
- Risk: lowest. The main risk is looking like every other plain README, which means we lose the pull of the demo; and a text-heavy page can still feel long to someone who just wants to know if it is for them.

**C. Terminal and demo first.**
- Change: open with a recorded session (GIF or video) of the setup interview, then a three-line start, then the explanation.
- Borrows from: Ruflo (recording), MetaGPT (try without installing), ChatDev (GIF gallery).
- Risk: highest for our reader. A terminal view signals "for developers" to someone who has never used one, which is the opposite of our message. A video also dates quickly as the tool changes and cannot be checked by our sweep.

### Recommendation

Direction B, with one borrowed piece from A: a calm document with diagrams, plus a single short "see it" block near the top (the dry-run demo we already have) and a clearly marked start button. Reason: our reader is a non-coder who must trust us with real decisions, and the near-total absence of restraint, plain language and honest limits among competitors is where we are strongest. A is a fallback if the founder wants more conversion; C works against the audience. Evidence for B being a gap worth owning: of the 14, only ChatDev names non-coders, and none pairs plain language with a visible process picture and a recorded real session.

### What in our README none of them does, worth keeping

1. **The "not vibe coding" table that maps each step to a standard practice name** (requirements traceability, definition of ready, rollback). None of the 14 gives a lay reader a lookup name for each step. I found no equivalent in any README read.
2. **The word-for-word recorded dry run** with a fictional founder, linked to the full transcript. Others show a text session (gstack) or GIFs (ChatDev), but not an unedited run plus every file produced.
3. **The "What stays in your hands" picture and list:** agents act on their own, a defined set waits for the founder's yes. OpenHands warns about file access; nobody frames the approval boundary as a feature.
4. **A glossary in the README itself** ("Words you'll see"). No other README read has one; several are called out above for unexplained jargon.
5. **Founder-level voice** (no jargon at all for a non-technical founder). Unique among the set as a stated design rule.
6. **Plain "Good to know" limits:** not magic, not legal advice, free-tier caps, spend visibility, you can stop any time. Closest are superpowers and OpenHands, but neither covers money and legal exposure.
7. **No badges, no emoji, no benchmark claims.** This is a quiet advantage given how many competitors lean on counts and self-reported numbers (SuperClaude, Ruflo, gstack).

## Not found or not confirmed

- Whether any of these READMEs serves dark-mode-specific images (the `<picture>` tag): confirmed only for task-master's install badge. All other cases are "not confirmed".
- Collapsible sections: confirmed for SuperClaude; ChatDev's "Old News" seems folded but is not confirmed; Ruflo not confirmed.
- No project found that is aimed at non-technical founders and uses a full agent team with approval gates, other than ChatDev's "non-coders" audience. A wider search (Lovable, Bolt and similar hosted builders) was out of scope: those are products, not templates in a repository.
- Whether ours has dark-mode-safe SVGs: not checked.
