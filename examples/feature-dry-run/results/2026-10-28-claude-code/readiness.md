# Readiness gate: RCPT-1

Run by the orchestrator (`skills/readiness-gate/SKILL.md`). Each line met or not met, with the file
that shows it.

## Pass 1, 2026-10-28, after the founder confirmed the spec

| # | Line | Result | Shown by |
|---|---|---|---|
| 1 | Spec exists and the founder confirmed it, date in `status.md` | met | `spec.md`; `status.md` "confirmed 2026-10-28"; transcript round 7 |
| 2 | Every behaviour has a row; every row cites a testable outcome | met | `spec.md` rows table; `RCPT.md` (reviewed three rounds, B3, B5 fixed the two untestable rows) |
| 3 | No open question blocks this feature | met | `p1-open-questions.md`: transfer blocks beta, counsel question blocks beta, free numbers block a free path going live; none blocks the build |
| 4 | Success number, read date, review focus with rows | met | `spec.md` "How we know it works" (RCPT-17), "Review focus" (6 items, each with rows) |
| 5 | Stores data: `design.md` names source of truth, retention, deletion | **not met** | no `design.md` yet |
| 6 | Client and server: `contract.md` exists | **not met** | no `contract.md` yet |
| 7 | `tickets.md` slices the work, cites rows | **not met** | no `tickets.md` yet |
| 8 | Constitution not broken by the plan | met | rows before design (rule 1); founder decided targets, caps, legal position (rule 2); estimates labelled (A-10 to A-13, rule 10) |
| 9 | `legal` and `security` scheduled in `status.md` | met | `status.md` steps table |
| 10 | Touches existing code: `spec-audit.md` | met (not applicable) | no product code exists yet |

**Result: shut** (lines 5 to 7). Those three are written by `architect`, and
`skills/new-feature/SKILL.md` step 6 routes to `architect` only "When it passes"; `agents/architect.md`
says "Use after the readiness gate". As written, the gate can never open for a feature that stores
data. Ruling 6 in `status.md`: pass 1 opens the design work (agentic, architect, product-designer,
legal, security) and nothing else; lines 5 to 7 are checked again in pass 2, and no ticket is built
before pass 2 passes (`agents/orchestrator.md`: "No build before the readiness gate passes").

## Pass 2, 2026-10-28, after the design reviews and the founder's go

| # | Line | Result | Shown by |
|---|---|---|---|
| 1 | Spec confirmed | met | as pass 1; the spec changed only by founder decisions since (rows RCPT-24 to RCPT-28, each in `p1-closed-decisions.md`) |
| 2 | Every behaviour a row, every row testable | met | `RCPT.md`; new rows RCPT-25 to RCPT-28 name their measure |
| 3 | No open question blocks this feature | met | `p1-open-questions.md`: what remains blocks beta, a free path going live, or the German launch, not the build |
| 4 | Success number, read date, review focus | met | `spec.md`; review focus mapped to tickets in `tickets.md` |
| 5 | `design.md` names source of truth, retention, deletion | met | `design.md` "Data", "Retention and deletion"; ADR 0001 |
| 6 | `contract.md` exists | met | `contract.md` (revised after rounds 4 and 5) |
| 7 | `tickets.md` slices the work, cites rows, blocking edges | met | `tickets.md` T1 to T8 |
| 8 | Constitution not broken; bent rules accepted by the founder | met | rulings 5 to 8 kept by the founder (transcript section 13) |
| 9 | `legal` and `security` scheduled | met | `legal.md` parts 1 and 2, `security.md` done; `security` on every diff |
| 10 | Existing code: spec audit | met (not applicable) | no product code yet |

Design review: no blocking finding open (`review.md` round 6; F1 closed by ruling 8). **Result:
open for build**, starting with T1 (founder's go, transcript section 13). T3 waits for `devops`
and the LAUNCH-1 to LAUNCH-3 numbers for live use.
