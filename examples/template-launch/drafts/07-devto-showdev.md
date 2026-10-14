# DEV `#showdev` draft (post only, no article)

Venue notes: `../where-to-post.md`, section 7. Pages opened 2026-10-14: https://dev.to/t/showdev,
https://dev.to/guidelines-for-ai-assisted-articles-on-dev, https://dev.to/code-of-conduct.

Tags: `showdev`, plus two or three of `ai`, `opensource`, `productivity` (tag names not verified
against DEV's current tag list). Set the AI disclosure in the editor if it offers one. The
disclosure line at the end of the body satisfies the written guideline and must stay.

## Title

Show DEV: a template that gives AI agents the roles and process of a normal software team

## Body

I made this. It is free and MIT licensed, and there is nothing to buy.

`one-man-startup` is a GitHub template. It is aimed at people who want to build a software
product with AI coding agents but do not want vibe coding: describing something, accepting what
the AI writes, and asking again when it breaks. Instead the agents are put in the roles of an
established team, and the workflow is the established one.

- Requirements first: every change names a numbered requirement.
- Definition of Ready: a feature does not start until its spec is confirmed and no question on it is open.
- Architecture Decision Records for hard-to-reverse choices.
- Test-driven development.
- Independent QA that checks against the requirements and can stop a release.
- A security review.
- Every round re-runs every check (continuous integration), locally and in GitHub Actions.
- Release approval: deploys, spending, deletes and messages wait for the human, one step at a time.

It is plain files: an operating manual in `AGENTS.md`, agent files, skills, and checks. Tool
adapters are generated from them for Claude Code and Cursor, Codex is meant to read `AGENTS.md`
directly, and Gemini CLI goes through a `GEMINI.md` that imports it. `docs/HOW-IT-WORKS.md` explains how the pieces fit.

Limits: one recorded dry run of the setup interview (an AI playing the founder) passed in Claude
Code; a run on another tool failed and led to fixes. I have not confirmed that any of the four
tools load the files the way I expect (`docs/ASSUMPTIONS.md`, A-2 to A-5), and no real
non-technical founder has used it. The agents make mistakes. The legal agent is not legal advice.

Repository: https://github.com/Fadi88/one-man-startup

Feedback welcome, especially on what a real team would insist on that is missing.

*AI disclosure: this post was drafted with an AI assistant and edited by me. The project itself
is built with AI agents.*
