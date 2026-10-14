---
name: spec-audit
description: Check whether a feature or codebase is specified well enough to hand to a developer agent - five layers (what it does, its interfaces, its architecture, how it ages, what good looks like here) - and name the decisions an agent would otherwise fill in silently. Use before the readiness gate on any feature that touches existing code, and at setup when a codebase already exists.
---

# Spec audit

An agent given a thin spec does not stop and ask; it fills the gaps with whatever is most common
in the code it learned from. This audit finds those gaps before the work is delegated, so the
founder decides them instead of the agent's habits.

The five layers follow Hamidreza Saghir's framing of under-specified coding agents, as adapted in
Florian Bruniaux's Claude Code guide; this version is written for this template's files.

## The five layers, and where this template keeps each

| Layer | The question | Where it lives here | If missing, the agent will |
|---|---|---|---|
| 1. Behaviour | What must it do, and how do we know it does? | `spec.md`, the requirement rows | guess the behaviour |
| 2. Interfaces | What goes in and out, what errors, what must always hold? | `contract.md`, types and validation in the code | handle errors optimistically, loosen types |
| 3. Architecture | What exists already, where are the boundaries, what must not be created? | `design.md`, `docs/adr/`, `AGENTS.md`, `skills/single-source/` | duplicate an existing module, cross a boundary |
| 4. Lifecycle | What is deliberately unfinished, what is deferred and why? | `docs/HISTORY.md`, `tools/known_red.json`, `p1-open-questions.md`, `p1-closed-decisions.md` | "fix" a deliberate shortcut, or add a band-aid |
| 5. Culture | What does good look like in this project? | `p1-standing-instructions.md`, `project.toml [style]`, linters, the guidelines skills | write average code in its own style |

## How to run it

Read only; change nothing.

1. **Name the scope:** one feature (its work folder) or the whole codebase.
2. **For each layer, look at the files in the table** and at a few real code files in the area
   the work will touch. Grep before reading (`skills/context-budget/`).
3. **Grade each layer:** COMPLETE (an agent could work without guessing), THIN (some decisions
   left open) or MISSING. A grade cites the file, or the absence of one.
4. **For every THIN or MISSING layer, list the silent fills:** the two or three concrete
   decisions an agent would make on its own. Examples: "creates a second auth helper because
   nothing says one exists"; "returns success when one of three writes failed because no error
   contract says otherwise".
5. **Mark the most dangerous fill:** the one hardest to undo later (a data model, a boundary, a
   public interface).

## Verdict

- **Delegate:** every layer COMPLETE, or THIN only where a wrong guess is cheap to undo.
- **Delegate with review:** THIN layers whose fills are listed in the brief, so the reviewer
  checks exactly those decisions.
- **Do not delegate yet:** any MISSING layer whose most dangerous fill is hard to undo. Turn the
  fills into questions for the founder (`skills/grilling/`) or work for `architect`, then audit
  again.

## Report

`docs/work/<id>/spec-audit.md` for a feature, `docs/spec-audit-<date>.md` for a codebase:

| Layer | Grade | Evidence | Silent fills |
|---|---|---|---|

then the verdict, the most dangerous fill, and the fixes in order of how much risk each removes
for how little work. No score out of 100: the grades and the named fills are what the founder
acts on.
