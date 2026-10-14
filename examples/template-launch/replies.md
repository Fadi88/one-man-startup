# Draft replies

Short answers for Fadi to adapt and send himself, in his own words. Every fact comes from this
repository, with the file named. Where the repository does not say, the reply says so instead of
filling the gap. Nothing here has been posted.

Hacker News asks for humans in conversation ("Don't post generated text or AI-edited text. HN is
for conversation between humans."; guidelines opened 2026-10-14), so on HN write these fresh from
the facts, do not paste them.

## "Isn't this just vibe coding with extra steps?"

The steps are the point, so I would not argue the label. Vibe coding, as the README defines it, is
describing what you want, accepting whatever the AI writes, and asking again when something breaks.
Here the work is written down first as numbered requirements, a feature does not start until its
spec is confirmed and has no open question (README, "Definition of Ready"), tests are written
before the code, someone other than the builder checks the result against the requirements and can
stop a release, and nothing goes live, costs money or deletes data without a human's approval. Each
step in the README is paired with its standard name. What I cannot show yet is that it works better
in practice: the only recorded test is the setup interview, and it had an AI playing the founder
(`examples/setup-dry-run/REPORT-2026-10-14.md`).

## "Does it really need no code?"

The claim in the README is that you never write code and do not need to read it; you need to know
your customers and be willing to make decisions. What backs it today is narrower: a scripted dry
run of the setup interview passed in Claude Code (two items partial), and the same script on a
different tool with a Gemini model failed and led to fixes. A real non-technical founder has not
yet gone through it, so how far one gets without help is an open assumption (`docs/ASSUMPTIONS.md`,
A-7). The agents make mistakes, which is why the approval steps exist.

## "How much does it cost to run?"

I have no figure and will not invent one. From the README: the template is free (MIT); a GitHub
account, Git and Python are free; the AI coding tool is a paid subscription, so check that tool's
own pricing page; hosting once your app is live has its own costs, and the agents are told to
state what each option costs before you choose. Every agent run uses your AI subscription. Setup
asks for your monthly AI budget, and an optimizer agent looks for waste, such as a stronger model
than a job needs, and proposes savings that you approve.

## "Why not just hire a developer?"

You may well be better off with one. The README does not claim to replace a developer, and I have
no data comparing the two. It is for someone who has an idea and no technical co-founder, and who
wants to see what is being built and why. Developers who work alone are also named as users. What
it gives you is a process with checks: the agents are not shown to do everything a developer
does, so a lawyer should still review the legal drafts before launch, especially with payments,
health data, children or financial data (README, "It isn't legal advice").

## "Does it work with Codex, Gemini CLI and Cursor, or only Claude Code?"

It is written for all four, but only partly tested. The setup interview was run in Claude Code and,
separately, on Antigravity CLI with a Gemini model. Whether Claude Code, Codex, Gemini CLI and
Cursor load the files the way I expect is still open (`docs/ASSUMPTIONS.md`, A-2 to A-5, confirm by
2026-10-31). The Antigravity run was told which files to read, so it does not settle that either.

## "The AI will make mistakes. Why trust it?"

Do not trust it blindly; the README says the agents "can be wrong, and sometimes confidently
wrong". The design answer is that checks sit at every step: requirements before code, tests,
independent QA, a security review, every check re-run on each change, and your approval for
anything outward. Those catch mistakes and will not catch all of them, and they will not catch a
bad business idea. The grilling interview is there for that, not a guarantee.

## "Is the legal agent a lawyer?"

No. The legal agent writes checklists and first drafts of a privacy policy and terms, marked for a
lawyer to review (README, "It isn't legal advice").

## "What if the free plan gets abused?"

If a product has a free plan or trial, the agents build hard limits into the first version: a cap
per user, a tighter one for people who have not signed up, and a daily ceiling on what the free
plan can spend in total. You choose the numbers (README, "Free tiers are strict").

## "Am I locked in?"

The README says everything the agents make is ordinary code and documents in your own GitHub
repository, and nothing is locked into this template or any one AI tool. I have not tested
leaving, so treat that as the design intent.

## "How is this different from spec-kit or BMAD?"

I have not compared them feature by feature, and I will not claim to. Both are credited in the
README for ideas. What this one is aimed at is the person who does not code and the whole business
workflow around the build: a setup interview, a legal checklist per country, growth and social
media agents, and approval gates for anything outward. Read each project's own README for what it
does.
