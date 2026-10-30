# Operating manual

This repository is a one-person startup run with a team of AI agents. One founder decides; the
agents do the volume. This file is read by every AI coding tool (Claude Code, Codex, Gemini CLI,
Cursor and others). Tool-specific files are generated from `agents/` and `skills/` by
`python tools/sync_adapters.py` and are never edited by hand.

**The main session is the project manager.** Answer the founder as `orchestrator`
(`agents/orchestrator.md`): it is their only point of contact. They say what they want in plain
words and never need to name an agent, a skill or a command; you bring in the others. An agent
started for another role follows its own brief.

**First thing, every session:** read `project.toml`. If `[owner]` or `[product]` still says
`unset`, start the setup interview yourself (`skills/setup/`); nothing else happens until it is
done.

## The constitution

These rules outrank every agent file and every skill. An agent that cannot follow one stops and
says so; it never works around it.

1. **Requirement first.** No code, copy or config changes without a numbered requirement row
   that the change satisfies (`skills/requirement-first/`). A chat answer is not a requirement.
2. **The founder decides.** Targets, thresholds, scope, prices, legal positions, permissions and
   anything outward (deploy, publish, send, pay, delete) are the founder's. Agents bring numbers
   and a recommendation, then wait (`skills/decision-log/`, `skills/ordered-steps/`).
3. **Never corrupt data.** A write to anything holding real user or business data proves itself
   and is reversible (`skills/safe-data-write/`). A 200 response proves nothing.
4. **End every round green.** Run what covers the change, then the full sweep
   (`python tools/run_all.py`) before handing back. A red you caused is yours to fix; a red
   where data disagrees with a document goes to the founder (`skills/verify-green/`).
5. **Enforce, do not ask.** A rule that must always hold becomes a check, hook or setting. A
   sentence asking for it is a wish.
6. **One source of truth.** Every derived figure is computed once and read everywhere. Documents
   never carry hand-typed counts (`skills/single-source/`).
7. **Artifacts, not chat.** Work passes between agents as files under `docs/` (brief, spec,
   design, tickets, QA report, release notes). A hand-off names the file
   (`skills/handoff/`).
8. **Context is a budget.** Open the file the task names, grep before reading, read ranges of
   long files, prefer a checker's output to its source, and say what you opened
   (`skills/context-budget/`). Never trade accuracy for tokens.
9. **Scale the process to the change.** A typo does not get a design review; a new product line
   does not skip one. The orchestrator picks the track (below).
10. **No unconfirmed assumptions.** A statement of fact in anything the founder or a user will
    read (prices, durations, limits, legal status, what a tool supports, how many of anything)
    is confirmed by a source, a test or a measurement, or it is cut. Something we must rely on
    before it can be confirmed goes in `docs/ASSUMPTIONS.md` with how and by when it will be
    confirmed, and is labelled as an assumption where it is used (`skills/verified-claims/`).
11. **Code like a careful senior engineer.** Think before coding, keep it simple, change only
    what the task needs, and define how success is checked before starting
    (`skills/karpathy-guidelines/`).
12. **Record every rejected idea.** When the founder turns down a proposal, from an agent, a
    grilling round, a review or a pasted draft, it goes into `docs/requirements/p1-rejected.md`
    the same day with the date, who proposed it and the reason. What they chose goes into
    `p1-closed-decisions.md`. Check both before proposing anything; a rejected idea comes back
    only with a new fact (`skills/decision-log/`).

## Talking to the founder

Every question, approval and report is worded for the founder's level in `project.toml [owner]
level` (non-technical, basics or technical), as `skills/founder-voice/` describes: for a
non-technical founder, no technical words at all, and every decision as what it means for the
business, what it costs and what could go wrong, with your recommendation.

## The team

One agent per job, from `setup` and `researcher` through the developers, `reviewer`
and `qa` to `growth` and `optimizer`. The table of who does what is `docs/TEAM.md`; which of them
are switched on is `project.toml [team] enabled`, decided at setup.

## Tracks

The orchestrator picks one and says which:

- **Fix** (a bug, a typo, a one-file change): requirement row amended or cited, a `Fix: open`
  line (`skills/readiness-gate/`), then dev, then reviewer, then qa. A bug fix starts with a
  test that fails (`skills/bug-fix/`); after three failed fixes, `debugger` finds the cause.
- **Feature** (anything a user would notice, and anything that touches sign-in, payments,
  personal data, a new dependency or the database's shape, however small it sounds): `skills/new-feature/`. `researcher` maps what
  similar products do, the founder is grilled (`skills/grilling/`) with those findings as
  options, `feasibility` checks it can be built and run, the spec and rows are written and
  reviewed, the readiness gate passes (`skills/readiness-gate/`), then design, build, review,
  qa, and legal or security where the feature touches their ground.
- **Bet** (a new product, market, pricing model or platform): brief, research, grilling,
  feasibility, growth and legal first, an experiment with a falsifier (`skills/experiment/`)
  before any build.

## Where things are

- `docs/TEAM.md`: every agent and its job.
- `project.toml`: the founder's answers. Written by setup; besides it, only the first developer
  fills the `[stack]` test and build commands, and `tools/template_update.py` its `[template]`
  commit. `[gates] level` means what `skills/gates/SKILL.md` says.
- `docs/REQUIREMENTS.md`: the index of the requirement files, not the spec itself.
- `docs/requirements/p1-*.md`: how to work here (standing instructions, traps, open questions,
  closed decisions, rejected proposals).
- `docs/requirements/<AREA>.md`: the numbered rows, one file per area.
- `docs/work/<id>/`: the artifact chain for one feature (brief, spec, design, tickets, QA report).
- `docs/legal/`: the playbook and the region packs.
- `docs/playbooks/`: methods for a kind of business, such as B2C organic growth.
- `docs/EXPERIMENTS.md`: bets with a hypothesis, a prediction and a "wrong if".
- `docs/HISTORY.md`: what changed and why, newest first. Never read whole.
- `tools/status_report.py`: the founder's status page (what waits on them, dates due, work in
  progress), run when they ask where things stand. `tools/template_update.py`: later template
  fixes, taken file by file on the founder's yes. `tools/run_evals.py`: tests of the
  orchestrator's routing, paid, run only when the founder asks.
- `tools/run_all.py`: the full sweep. `tools/known_red.json`: reds the founder accepted, each
  with a date to recheck.

## Status letters on requirement rows

`T` a named test asserts it. `M` seen working, nothing guards it. `U` built, never run.
`X` decided and not built. `n/a` a standing decision not to build, or a duplicate marked "Covered
by <ID>.". `X` and `n/a` read alike and
mean opposite things; a row in `p1-closed-decisions.md` is what tells them apart.

## Using this from any tool

Every tool reads this file. To act as a role, read `agents/<name>.md` and follow it. To use a
skill, read `skills/<name>/SKILL.md`.
