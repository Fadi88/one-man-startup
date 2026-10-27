---
name: grilling
description: Interview the founder relentlessly about a plan, feature or decision until there is a shared understanding with nothing silently assumed. Used by setup, new-feature and bets, or whenever the founder says grill.
---

# Grilling

The goal is a plan with no hidden assumptions, reached with as few of the founder's minutes as
possible.

The founder can ask for it on anything ("grill me on this idea", or `/grilling` in Claude Code);
run it on what they named, or on the plan under discussion if they named none.

## The design tree

Every decision has decisions that hang off it. Map them as a tree before asking anything. The
**frontier** is every decision whose prerequisites are already settled: the questions that can
be asked now without guessing at answers not yet given.

## Their level

Word every round for the founder's level (`skills/founder-voice/`). If `project.toml [owner]
level` is unset, the level is the first question of round one.

## What others do

For a feature or a bet, read `docs/work/<id>/research.md` before round one (the orchestrator has
`researcher` write it first). Each suggestion in it becomes a question in the round where its
branch is on the frontier, with the evidence beside the recommendation: "Rivals A and B do X;
do we? Recommended yes, because ...". What the founder copies, beats or ignores is theirs.

## Rounds

Ask the whole frontier in one round, numbered. For each question:

- a title and the question, with the options when there are options;
- **your recommended answer and the reason in one line**, worded so that "yes" accepts it.

When a round would hold more than about ten questions (a default; the founder can set another) (a large research brief, decisions carried over
from an old app), put every question with its recommendation in a choices file,
`docs/work/<id>/round-<n>-choices.md`, numbered, where the founder marks each one or writes "accept
all", and ask only the few that change the most in chat.

Then wait. A question whose answer depends on another question in the same round belongs to a
later round.

After each round, settled decisions push the frontier out. Recompute it and ask the next round.

## Facts are yours, decisions are theirs

Never ask the founder for a fact you can find: in the repo, in `project.toml`, in the docs, on
the web. Go and get it (in parallel, with a helper agent if the tool has one) and ask the rest
of the frontier meanwhile; only the questions that depend on that fact wait for it. Decisions,
preferences, money, risk and anything outward are the founder's; put each one to them.

## Push back

A grilling that only collects answers is a form. When an answer conflicts with an earlier one,
with `project.toml`, with a closed decision or with the evidence, say so in the next round and
ask which wins.

## Anti-goals and playback

The tree always has a branch for **anti-goals**: the ways the thing could work exactly as
specified and still fail the founder (the feature ships and nobody finds it; it works and
doubles the support load; it is legal in one region and not the next). Ask for them as a
question like any other, with your own candidates as the recommendation.

After each round, before computing the next frontier, **play back** what is now understood in
a short paragraph at the founder's level, with every guess marked as a guess, and ask what is
wrong or missing. The playback is where the silent assumptions surface.

## Approval is of the written thing

"Sounds good" or "go ahead" during a round approves nothing but the next round. Only the
written outcome, shown in full, is confirmed. A spike (a throwaway build to learn something)
happens when the founder asks for one; keeping any of its code needs a fresh confirmation of
the spec it now serves.

## Done

The session ends when the frontier is empty: every branch visited, nothing assumed. Then write
the outcome down (the spec, the decision rows, `project.toml`, whatever the caller asked for),
show it, and **do not act on it until the founder confirms it is what they meant.**

## Record what was turned down

Every recommendation or option the founder declined in any round goes into
`docs/requirements/p1-rejected.md` the same day: the date, what was proposed, who proposed it,
and the founder's reason (or "no reason given"). Every option they chose goes into
`p1-closed-decisions.md`. A grilling whose rejected options are not written down will be
re-asked next month as if it never happened.
