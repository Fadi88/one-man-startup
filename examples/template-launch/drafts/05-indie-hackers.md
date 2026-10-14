# Indie Hackers draft

Venue notes: `../where-to-post.md`, section 5. Guidelines page NOT opened (403). Before posting
Fadi must read the current guidelines in a browser and choose the post type the site offers for
sharing a product.

## Title

I made a free template for building software with AI agents the way a normal team would, not by vibe coding

## Body

I made this, it is free and MIT licensed, and I am not selling anything.

The story: people with a business idea and no technical co-founder are told to ask an AI to build
it. Many end up with an app that half works and that nobody can maintain. I wanted the AI to do
the volume of the work while the process stayed the one established teams use. So the repository
holds a small team of AI agents, an operating manual and a set of checks, and the workflow is the
traditional one: a requirements interview before anything is built, numbered requirements, a
confirmed spec before work starts, test-driven development, a separate QA agent that can stop a
release, a security review, and your approval before anything goes live, costs money or deletes
data.

It is aimed at someone who knows their customers and is willing to make decisions. Developers
working alone can use it for the discipline of a team without hiring one.

What I know and what I do not:

- The setup interview has a recorded dry run (in `examples/setup-dry-run/`), with an AI playing
  the founder. It passed in Claude Code. A run on another tool failed and led to fixes that I have
  not re-run.
- No real non-technical founder has used it yet.
- Codex, Gemini CLI and Cursor support is untested (`docs/ASSUMPTIONS.md`, A-2 to A-5).
- The agents make mistakes. The legal agent produces checklists and drafts for a lawyer, not legal advice.
- Running it costs whatever your AI coding tool's subscription costs. Check that tool's pricing page.

https://github.com/Fadi88/one-man-startup

I would like to hear from anyone who builds alone: which step would you skip, and which would you add?
