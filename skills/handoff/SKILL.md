---
name: handoff
description: The format for passing work between agents - a brief going out, a short report with file paths coming back. Use for every delegation and every hand-back.
---

# Hand-off

## The brief (orchestrator to agent)

- **Objective:** one sentence, with the requirement ids.
- **Read:** the exact files, nothing else unless stated.
- **Produce:** the artifact and its path.
- **Boundaries:** what not to touch, what needs the founder.
- **Done when:** the checks that must pass, the gate this feeds.

## The hand-back (agent to orchestrator)

- **Status:** done, blocked, or done with gaps.
- **Artifacts:** paths only.
- **Summary:** three lines at most.
- **Verified:** what was run and what it said.
- **Not verified:** what could not be checked, and why.
- **Opened:** the files read, so nobody reads them again.
- **Needs the founder:** decisions surfaced, each with a recommendation.

Update `docs/work/<id>/status.md` with the step and its state.

## Agents working in parallel

Nobody edits a generated or shared file (the index in `docs/REQUIREMENTS.md`, `docs/TEAM.md`,
another area's rows) while others are working. Each writes its own files; the orchestrator runs
`python tools/checks/req_check.py --fix` and settles shared rows once, at the end.

## Rulings

An agent that meets an ambiguity the spec does not settle, and resolves it rather than stopping
(a name, a default, an edge case the rows do not reach), writes a ruling in
`docs/work/<id>/status.md` as it goes: **what was decided, why, and what it costs if wrong.**
Anything on the founder's list (targets, thresholds, prices, scope, legal, permissions, outward
steps) is never ruled; it stops and goes up. The hand-back lists every ruling, and the
orchestrator puts them in front of the founder at the next stopping point so any can be undone
while it is cheap. A ruling nobody wrote down is an assumption nobody can find.

## Answering a review

When `reviewer`, `security`, `legal` or a draft the founder pasted in comes back with findings:

- Read all of them before answering any. If one is unclear, ask about it before implementing
  the others; related findings are misread when only half understood.
- Verify each against the code before agreeing: open the file, run the test. A finding can be
  wrong about this codebase, break something the reviewer did not see, or add a feature nothing
  uses (grep for callers; if none, ask whether to remove instead).
- Agree by restating the fix in one line, or by doing it. Never "you're absolutely right";
  never announce an implementation before verifying. Disagree with evidence (the test, the
  line, the decision it conflicts with), and put a disagreement about architecture or scope to
  the founder through the orchestrator.
- Implement one finding at a time, each with its test: blocking ones first, then simple, then
  complex. Re-run the sweep after each.
- Reply to each finding where it was made (`review.md`, or the pull request thread) with what
  changed, or why not.
