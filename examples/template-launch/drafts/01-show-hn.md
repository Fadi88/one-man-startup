# Show HN draft

Venue notes: `../where-to-post.md`, section 1. Rules opened 2026-10-14:
https://news.ycombinator.com/showhn.html and https://news.ycombinator.com/newsguidelines.html.

Before posting: HN says "Please don't put generated text in HN posts." and "Don't post generated
text or AI-edited text." in comments. This draft was written by an AI agent. Rewrite the title and
the first comment in your own words, keeping the facts. Do not ask anyone to upvote or comment.
Be online for the day.

A Show HN is a title plus a URL (or text, not both), so the explanation goes in the first comment.

## Title (72 characters)

Show HN: Template that runs a startup's software workflow with AI agents

## URL

https://github.com/Fadi88/one-man-startup

## First comment, by the author, posted right after submitting

I made this. It is a GitHub template for people who want to build a software product with AI
coding agents but without the "describe it, accept the output, ask again when it breaks" loop.
The README calls the aim "build a software startup without writing code", and says plainly that
this is not vibe coding.

What it actually is: a repository of plain files (an operating manual in AGENTS.md, a team of
role files, skills, and checks) that you copy and open in an AI coding tool. The agents are put
in the roles of an ordinary software team and the process is the ordinary one: you are
interviewed about requirements first, each requirement is numbered and every change cites one, a
feature cannot start until the spec is confirmed (a Definition of Ready), the architect records
hard-to-reverse choices as ADRs, developers write the test first, a separate QA agent checks work
against the requirements and can stop a release, a security reviewer looks at data exposure, every
round re-runs all checks, and anything outward (deploy, spending, deleting, sending) waits for
the human's approval, one step at a time. The README has a table mapping each step to its
standard name.

What I have tested, and what I have not:

- The only recorded test is the setup interview. A scripted dry run in Claude Code passed my
  rubric (two items partial). The same script on Antigravity CLI with a Gemini model failed it,
  which led to fixes that I have not yet re-run. In both runs one agent played both the
  interviewer and the founder, so the answers are not independent. The report is in
  examples/setup-dry-run/REPORT-2026-10-14.md.
- Nobody who does not code has used it yet, so I do not know where a real non-technical founder
  gets stuck (docs/ASSUMPTIONS.md, A-7).
- The files are written for Claude Code, Codex, Gemini CLI and Cursor. I have not confirmed that
  Claude Code, Codex, Gemini CLI or Cursor load them as intended (A-2 to A-5, all open as I write).
- The agents make mistakes, some confidently. The tests and approval steps are there to catch
  them and will not catch everything. The legal agent writes checklists and first drafts marked
  for a lawyer to review; it is not legal advice.
- You need a paid subscription to one of the AI tools. I have not put a price in the README,
  because that is the vendors' to state.

[Fadi: if you have built something real with it, add one factual sentence and a link here. I found
no record of that in the repository, so I did not write one.]

MIT licensed. I would most like to hear where the workflow is wrong or missing something a real
team would insist on, and which step reads as ceremony.
