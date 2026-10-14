# Awesome lists

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
