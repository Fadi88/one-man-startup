# r/ClaudeAI draft

Venue notes: `../where-to-post.md`, section 2. Rules NOT opened (reddit.com blocked from the
drafting tool). Before posting Fadi must: read the sidebar rules, read Rule 7 (showcase), check the
karma threshold reported in a moderator megathread (50 total karma, unconfirmed), pick the required
flair, and use the "Built with Claude" showcase megathread instead if his karma is below it.

## Title

I made a template that puts Claude Code in the roles of a normal software team (requirements, ADRs, TDD, QA, release approval)

## Body

Disclosure up front: I made this, it is free, MIT licensed, and there is nothing to sell. The
description below was drafted with help from Claude, and I edited it.

The repository is `Fadi88/one-man-startup`, a GitHub template. The idea: if you want to build a
product with an AI agent but do not want the "accept whatever it writes, ask again when it
breaks" loop, give the agents the roles and the process of an established team instead.

In practice that means plain files in your own repo: an operating manual (`AGENTS.md`), agent
files under `agents/`, skills under `skills/`, and checks you can run. Claude Code gets generated
copies under `.claude/`. The workflow:

- a setup interview, then a "grilling" before every feature (the grilling idea comes from Matt Pocock's skills)
- numbered requirements, and every change has to name the one it serves
- a feature does not start until the spec is confirmed and no question on it is still open
- an architect agent records hard-to-reverse choices as ADRs
- developers write the test first
- a separate QA agent checks against the requirements and can stop a release
- a security review, and a legal agent that writes checklists
- nothing outward (deploy, spend, delete, send) without your approval, one step at a time

What I have actually tested: a scripted dry run of the setup interview in Claude Code, scored
against a rubric, passed with two items partial. The same script on a different tool and a Gemini
model failed it, and the failures led to fixes I have not re-run yet. One agent played both
interviewer and founder in those runs. The record is in `examples/setup-dry-run/`.

What I have not: I have not confirmed that Claude Code loads the generated `.claude/agents/` and
`.claude/skills/` files the way I expect (it is open assumption A-2 in `docs/ASSUMPTIONS.md`),
no real non-technical founder has used it yet, and the Codex, Gemini CLI and Cursor adapters are
untested (A-3 to A-5). The agents still make mistakes. The legal agent is not legal advice.

https://github.com/Fadi88/one-man-startup

I would like to hear what is missing from the workflow, or where the setup interview loses you.
