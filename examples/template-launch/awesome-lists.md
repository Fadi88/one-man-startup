# Awesome lists

## Recheck 2026-10-16

Nothing was submitted, starred, posted or opened as a PR or issue. Every page below was opened on
2026-10-16 (GitHub pages, `raw.githubusercontent.com` files and `api.github.com/repos/<repo>/commits`).
Star counts are what the GitHub page showed that day. The tool I used to read pages sometimes
returned a summary, so quotes are short and a few details are marked "not seen".

What changed since 2026-10-14:
- `docs/ASSUMPTIONS.md` still shows A-2 to A-5 (Claude Code loading `.claude/`, Codex, Gemini CLI,
  Cursor) as open, confirm by 2026-10-31. So A-4 has not changed: the Gemini CLI list still waits.
- The repository is 2 days old. Any rule of the form "14 days" or "traction" is not met before
  2026-10-28 at the earliest.
- The README's claim of four supported tools is still partly unconfirmed. Every line below
  therefore says "AI coding agents" and names no tool.

### Ranked: submit now

How I judged traffic: stars first (people browse big lists), then whether a human or bot merged an
outside submission in the last week (a list that merges is read and kept alive), then fit (a
rejected or auto-closed submission gives no traffic). Only one list passes all three today.

| Rank | List | Stars (2026-10-16) | Last commit | Verdict |
|---|---|---|---|---|
| 1 | engineering4ai/awesome-spec-driven-development | 298 | 2026-10-12, merged outside PR #47 | Submit now |

### Not "now", ordered by what could come next

| List | Stars | Last commit | Verdict | Blocker |
|---|---|---|---|---|
| filipecalegario/awesome-vibe-coding | 5.3k | 2026-04-16 (6 months) | Wait | Its CONTRIBUTING.md is linked from the README but returned 404 at `main/CONTRIBUTING.md`, `master/CONTRIBUTING.md` and `.github/CONTRIBUTING.md`; I have not seen its rules. Open the link from the README page in a browser first. A merged PR (#95) was seen dated 2026-04-11. |
| kyrolabs/awesome-agents | 2.9k | 2026-10-14 | Wait | Its rules exclude "brand new repo without demonstrated traction" and say PRs not following them "will be automatically closed". No number is given for traction. Revisit after outside stars or users exist. |
| Piebald-AI/awesome-gemini-cli | 517 | 2026-10-16 (maintainer commits about a star check) | Wait for A-4 | A-4 open. New: its AGENTS.md asks for a star on that repository in return for a listing. Starring is the founder's own choice and is outward; I did not do it. |
| milisp/awesome-codex-cli | 122 | 2026-10-16 | Wait | A-3 open, and it wants "proven external usage". |
| bradAGI/awesome-cli-coding-agents | 1.4k | 2026-10-12 (bot) | Not a fit | The template is not a CLI agent; list is sorted by stars. |
| hesreallyhim/awesome-claude-code | 55.8k | 2026-10-16 (bot) | Not a fit | Form requires "specific to Claude Code"; the repo is 14 days old only on 2026-10-28. |
| VoltAgent/awesome-claude-code-subagents | 25.8k | 2026-10-11 | Not a fit | Lists subagent definitions; "We don't accept PRs whose primary purpose is to promote a product, company, or personal project." |
| VoltAgent/awesome-agent-skills | 35.8k | 2026-10-15 | Not a fit | Lists single skills, one per repository; "Brand new skills that were just created are not accepted." |
| ComposioHQ/awesome-claude-skills | 77.2k | 2026-07-24 | Not a fit | Lists skills; no human commit for almost 3 months. |
| travisvn/awesome-claude-skills | 15.4k | 2026-04-28 | Not a fit | Skills only; 5.5 months without a commit. |
| PatrickJS/awesome-cursorrules | 40.9k | 2026-05-30 | Not a fit | A submission is a `.mdc` rule file; Cursor support is A-5, open. |
| youxufkhan/awesome-ai-coding | 0 shown | 2026-10-09 | Skip | 0 stars, so no traffic; entries are table rows with maturity badges and I could not read its Contributing text. |
| hesreallyhim/awesome-claude-code-agents | not read | 2025-11-10 | Not a fit | Stale. |
| rahulvrane/awesome-claude-agents | not read | 2025-08-01 | Not a fit | Stale. |

### 1. engineering4ai/awesome-spec-driven-development: submit now

- URL: https://github.com/engineering4ai/awesome-spec-driven-development (opened 2026-10-16).
- Stars: 298 (page, 2026-10-16). Last commit: 2026-10-12 14:46 UTC, "Merge pull request #47 from dwkerwin/patch-1", which added an outside author's own project, The Enso Method, to Development Frameworks (API commits, opened 2026-10-16). So own-project submissions are accepted.
- Rules: the only text is "Contributions are welcome! Please feel free to submit a pull request to add more tools to this awesome list." (README, opened). No CONTRIBUTING file, no minimum stars, no age rule, no AI-content rule, no disclosure rule found. A pull request, not an issue.
- Section: "Development Frameworks". Alphabetical, ignoring case. I read the first 12 entries (agent-skills to ouroboros); the new line goes after MoAI-ADK and before ouroboros, but check the neighbours at submission time because I did not read the whole section.
- Format seen: `- [Name](repo URL) ![stars badge](...) - Description`. The badge is optional (MySpec and Reqode have none), so I leave it out.
- Fit: close neighbours are Cosmosmith (generates AGENTS.md and design templates) and Consort (spec-first, test-driven, human-approval gates). Our description sticks to what the README table states.
- Exact line:

```
- [one-man-startup](https://github.com/Fadi88/one-man-startup) - GitHub template that gives AI coding agents the roles of a software team: numbered requirements written before building, a Definition of Ready gate, test-first development, independent QA and approval before release.
```

- PR description (the list does not ask for it, but Fadi is the author): "Adds one-man-startup under Development Frameworks. Disclosure: I (Fadi) am the author."
- Rule risk: none found. Risk of rejection: the maintainer may see a template with a 2-day-old history as thin; no rule says so.
- Honest limit: the "stars" there are few, so expect modest traffic. It is the only list that passes today.

### 2. filipecalegario/awesome-vibe-coding: wait (read its rules first)

- URL: https://github.com/filipecalegario/awesome-vibe-coding (opened 2026-10-16). 5.3k stars, 754 forks, CC0-1.0.
- Last commit 2026-04-16, "Add getdesign.md link to various README files and settings". Six months old, so submissions may not be merged quickly.
- Why it matters: the README is the contrast entry. The listed sections include "Documentation for AI Coding" (AGENTS.md, awesome-cursorrules, llms.txt) and "Task Management for AI Coding" (Claude Task Master, CCPM, AWS Labs AI-DLC Workflows). "Task Management for AI Coding" or "Documentation for AI Coding" is the likely section, and AI-DLC Workflows is the closest neighbour.
- Rules: "Contributions welcome! Read the contribution guidelines (CONTRIBUTING.md) first." I could not open that file (404 on three paths). Verdict: wait until Fadi opens the link from the README in a browser and reads it.
- Format seen: `- [Name](URL) - Short description.`
- Candidate line, to be adjusted to the rules once read:

```
- [one-man-startup](https://github.com/Fadi88/one-man-startup) - GitHub template that gives AI coding agents the roles and checks of a software team (requirements first, test-first, independent QA, approvals), as a structured alternative to prompting and accepting.
```

### 3. kyrolabs/awesome-agents: wait until there is traction

- URL: https://github.com/kyrolabs/awesome-agents (opened 2026-10-16). 2.9k stars. Last commit 2026-10-14, "Add CUGA to Frameworks (#843)".
- Rules: https://raw.githubusercontent.com/kyrolabs/awesome-agents/main/CONTRIBUTING.md (opened). "The contribution needs to be open source." "Submit a PR, not an issue." Excluded: "brand new repo without demonstrated traction", "not related to Agentic frameworks". "those criteria are non-negotiable, managed and applied automatically."
- Sections seen: Frameworks, Software Development, and others. Entry format: `- [Name](URL): one-line description`, many with a stars badge. New items go at the bottom.
- Verdict: a 2-day-old repo with no outside stars is the exact case it closes. Wait; no date can be given because "traction" has no number. Reread the rules then.

### Lists that cannot take it, and why (all opened 2026-10-16)

- VoltAgent/awesome-claude-code-subagents (https://github.com/VoltAgent/awesome-claude-code-subagents): 25.8k stars, last commit 2026-10-11. CONTRIBUTING (https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/CONTRIBUTING.md) is about adding a subagent file and its README line `- [**agent-name**](path/to/agent.md) - Brief description`, and the README says it does not take promotion PRs. A separate option for the founder: contribute a real, vendor-neutral subagent (for example the rollback or debugger role) in the list's template. That is a different job with its own review, and I have not drafted it.
- VoltAgent/awesome-agent-skills: format `- **[author/skill-name](URL)** - description`, description 10 words or fewer, one skill per repo. Wrong kind of thing.
- No dedicated "awesome AGENTS.md" list was found. The only one seen before (tairov) is archived. The vibe-coding list links https://agents.md/ ("stewarded by the Linux Foundation", as that list describes it); I did not open it.
- No-code and low-code, indie hacker, and startup boilerplate lists: two searches returned no maintained GitHub awesome list I could open that takes template submissions. A fork of mezod/awesome-indie was mentioned in a search result; I did not open it, so I make no claim about it.
- Search results only (not opened, no claim made): rahulvrane and hesreallyhim agent lists beyond the commit dates above, wshobson/agents, BehiSecc and karanb192 skills lists, 0xWelt/Awesome-Vibe-Coding, EvoMap lists.

Sources for the search steps: web searches run 2026-10-16 (queries on Claude subagents, Claude skills, cursorrules and AGENTS.md, vibe coding, spec-driven development, solo founder and boilerplates, multi-agent lists).

---

## Original survey 2026-10-14 (statuses updated 2026-10-16)

Only lists I opened on 2026-10-14. "Last commit" is the newest commit the GitHub API returned
that day; on three of these it is a bot refreshing star counts, which shows the repository is
alive but not that humans are merging submissions. Nothing here has been submitted. Each
submission is an outward step that waits for Fadi's go, and each is a person acting, not an agent
(see the first list's rule).

Two facts decide the timing. The repository was created on 2026-10-14 (GitHub API, opened). And
support for Codex, Gemini CLI and Cursor is untested (`docs/ASSUMPTIONS.md` A-3 to A-5, confirm by
2026-10-31), so a list for one of those tools should wait for the check to pass. Disclose in each
submission that Fadi is the author.

## 1. hesreallyhim/awesome-claude-code: probably not a fit

Status 2026-10-16: unchanged. 55.8k stars, newest commit 2026-10-16 is a bot. Rules reread: still the issue form only, human-written recommendation, 14 days or 100 stars, one resource at a time, "specific to Claude Code". Not a fit.

- URL: https://github.com/hesreallyhim/awesome-claude-code
- Last commit seen: 2026-10-14 (a bot commit, "update repo ticker data and SVGs").
- Rules: https://github.com/hesreallyhim/awesome-claude-code/blob/main/CONTRIBUTING.md (opened).
  - "ALL RECOMMENDATIONS MUST BE MADE USING THE WEB UI ISSUE FORM TEMPLATE." and "Do not open a PR. Just fill out the form."
  - "resource recommendations must be created by human beings." So Fadi submits it himself.
  - A resource must "Be at least 14 days old (14 days since first commit on default branch) AND show signs of active development" or have at least 100 stars. This repo is 14 days old on 2026-10-28 at the earliest.
  - "if your project requires any form of signup or payment, this is a blocker for reviewing it." The template is free, but using it needs a paid AI tool; the reviewer may count that. Unknown.
  - "Resource descriptions should be written as descriptions - not a sales pitch."; no emojis; one resource at a time.
- The form (https://github.com/hesreallyhim/awesome-claude-code/blob/main/.github/ISSUE_TEMPLATE/recommend-resource.yml, opened) has a required checkbox "This resource is specific to Claude Code". This template targets four tools, so Fadi cannot tick it honestly. Recommendation: do not submit, or submit only a Claude Code-specific piece (the `.claude/` agents and skills), which would need a reason to stand alone. I would skip it.
- If Fadi decides to anyway, the right category in the form's dropdown is "Agent Orchestration > SDLC", and the field values are:
  - Display Name: One-man startup
  - Link: https://github.com/Fadi88/one-man-startup
  - Author Name: Fadi (GitHub: Fadi88)
  - Author Link: https://github.com/Fadi88
  - Description (10 to 500 characters, descriptive, does not address the reader): A GitHub template that assigns Claude Code agents the roles of an established software team: requirements interview, numbered requirements, Definition of Ready, ADRs, test-driven development, independent QA, security review and release approval.

## 2. Piebald-AI/awesome-gemini-cli: wait for A-4

Status 2026-10-16: still wait. A-4 is still open. 517 stars; maintainer commits today. Corrected from above: its AGENTS.md says to fork, edit README.md, and open a PR with its PR template, and it asks for a star on the repository in return (founder's choice; not done). Tracking parameters on non-GitHub links are allowed.

- URL: https://github.com/Piebald-AI/awesome-gemini-cli
- Last commit seen: 2026-10-14 ("Add Latchkey to MCP Servers (#210)", apparently a merged submission).
- Rules: its `CONTRIBUTING.md` is a symbolic link to `AGENTS.md`
  (https://github.com/Piebald-AI/awesome-gemini-cli/blob/main/CONTRIBUTING.md, opened). The rules in
  https://raw.githubusercontent.com/Piebald-AI/awesome-gemini-cli/main/AGENTS.md (opened):
  "Make sure your entry follows the format: `- [Project Name](URL) - Description`", "Add your item to
  the bottom of the appropriate section", "Entries should be related to Gemini CLI (e.g. use it,
  build something on top of it, upgrade it in some way, etc.)", "No need to disclose affiliation, if
  any." I did not see an explicit statement of how to submit (PR or issue); the README only says
  "See CONTRIBUTING.md". Check before acting.
- Section: "Agent Orchestration & CLI Tools" (entries there coordinate Gemini CLI alongside Claude Code and Codex, e.g. Bernstein and Ralph Harness; README opened).
- Exact line:

```
- [one-man-startup](https://github.com/Fadi88/one-man-startup) - GitHub template that gives AI coding agents, Gemini CLI through GEMINI.md among them, the roles and process of a software team: numbered requirements, test-first development, independent QA and approval before anything goes live.
```

- Wait for A-4 (Gemini CLI follows the `@AGENTS.md` import in `GEMINI.md`) to be confirmed, then submit, and mention in the PR that Fadi is the author even though the list does not require it.

## 3. milisp/awesome-codex-cli: not yet, fails its own criteria

Status 2026-10-16: unchanged. 122 stars, last commit 2026-10-16 09:03 UTC by the maintainer. A-3 still open.

- URL: https://github.com/milisp/awesome-codex-cli
- Last commit seen: 2026-10-14 (a bot commit, "refresh repo ticker").
- Rules: https://raw.githubusercontent.com/milisp/awesome-codex-cli/main/contributing.md (opened).
  "External contributions are welcome through **issues only**.", "One entry, one section, 1 factual
  line (no marketing copy).", "Projects must show proven external usage (stars/downloads/community
  activity).", "Real Integration: Functional Codex CLI support (not just a mention in README)."
- A day-old repository with untested Codex support (A-3) meets neither criterion. Revisit after
  2026-10-31 and only if real outside use exists by then.
- Section if it ever qualifies: "Workflows & Knowledge Guides" (README opened; the heading has an emoji after it that I have not reproduced).
- Exact line if it ever qualifies:

```
- [one-man-startup](https://github.com/Fadi88/one-man-startup) - GitHub template that runs a software team's workflow (requirements, test-first development, independent QA, approvals) with AI agents; Codex reads its AGENTS.md.
```

## 4. bradAGI/awesome-cli-coding-agents: doubtful fit

Status 2026-10-16: unchanged, skip. 1.4k stars; last commit 2026-10-12 is a bot star refresh.

- URL: https://github.com/bradAGI/awesome-cli-coding-agents
- Last commit seen: 2026-10-12 ("chore: refresh GitHub star counts", a bot-style commit).
- Rules: the "Contributing" section of its README (opened; no separate CONTRIBUTING file seen): "PRs welcome!", inclusion requires a "CLI or terminal interface (IDE-only tools don't qualify)", the ability to "read/write code or run commands autonomously", and a "valid, active" link. Entries carry a name and link, a star count and a 1 to 2 line description, and "Entries are sorted by GitHub stars within each section."
- Section: "Harnesses & orchestration", then "Orchestrators & autonomous loops" (both in its contents list). Spec-driven workflow entries such as fab-kit sit there.
- The template is not a CLI agent, it drives them, so it is a harness at best, and a sorted-by-stars list puts a new repository at the bottom. Fit is weak; I would skip it, or ask in an issue first. If Fadi submits, copy the format of a neighbouring entry exactly (bold linked name, star-count badge, then a long dash and the description; I cannot reproduce the badge or the dash here) and fill in the star count from the repository page on the day. Description text:

```
Template of AI agent roles and checks for spec-driven, test-first, approval-gated software work, usable from Claude Code, Codex, Gemini CLI and Cursor.
```

## Opened and rejected

- tairov/awesome-agents.md (https://github.com/tairov/awesome-agents.md): the page says "archived by the owner on Jan 26, 2026"; last commit 2025-10-23. Read-only, so it cannot take submissions. This was the only AGENTS.md resource list my search found; I did not open the official https://github.com/openai/agents.md or its site, so there may be a place to be listed there that I did not check.
- e2b-dev/awesome-ai-agents (https://github.com/e2b-dev/awesome-ai-agents): last commit 2026-08-21; accepts PRs or a form, but says "This list is only for AI assistants and agents." The template is not an agent.
- johackim/awesome-indiehackers (https://github.com/johackim/awesome-indiehackers): last commit 2026-03-27; lists people, blogs, books, podcasts, communities and courses, and I found no contribution guidance (its CONTRIBUTING.md returned 404). Not a fit for a template.
- ljinkai/awesome-indie-maker (https://github.com/ljinkai/awesome-indie-maker): last commit 2021-04-19. Stale.

## Not opened

Awesome lists for Claude skills and other solo-founder lists turned up in searches only as
summaries. I did not open them, so I make no claim about them. I found no maintained "awesome
solo founder" list that accepts product submissions.
