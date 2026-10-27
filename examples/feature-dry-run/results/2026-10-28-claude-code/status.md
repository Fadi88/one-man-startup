# Status: RCPT-1, a receipt photo sorted into a spending category

- **Track:** feature (`skills/new-feature/`), opened 2026-10-28. Gates level: standard.
- **Area:** `docs/requirements/RCPT.md` (every row in it), with LAUNCH-1 to LAUNCH-7.

## Steps

| Step | Owner | State |
|---|---|---|
| Team: switch on researcher, feasibility, agentic-workflow, reviewer, dashboard | orchestrator, founder | done 2026-10-28 |
| Research (`research.md`) | researcher | done 2026-10-28 |
| Grilling rounds 1 to 4 | orchestrator, founder | done 2026-10-28 |
| Feasibility (`feasibility.md`) | feasibility | done 2026-10-28, go with changes, changes put to founder in round 3 |
| Spec and rows (`spec.md`, `RCPT.md`) | orchestrator | written 2026-10-28 |
| Spec review (`review.md` rounds 1 to 3) | reviewer (separate agent) | done; 13 blocking found, all fixed (N9 verified by the orchestrator, ruling 5) |
| Founder confirms the spec | founder | confirmed 2026-10-28 (grilling round 7) |
| Readiness gate | orchestrator | pass 1 done (design only, ruling 6); pass 2 waiting |
| AI design (`agentic.md`) | agentic-workflow | done 2026-10-28 |
| Design, contract, tickets | architect | done; revised after review round 4 |
| UX and rendered screens (`ux.md`, `human-design.md`) | product-designer | done; revised after review round 4 |
| Legal and security on the design | legal, security | done 2026-10-28 (`legal.md` part 2, `security.md`) |
| Design review | reviewer (fresh separate agent) | rounds 4 to 6: 17 blocking found; 16 closed by the reviewer, F1 closed by the orchestrator (ruling 8) |
| Readiness gate pass 2 | orchestrator | passed 2026-10-28 (`readiness.md`) |
| T1 built test first, reviewed (rounds 7, 8), QA | backend-dev, reviewer, qa | done 2026-10-28; `qa.md` PASS WITH KNOWN ISSUES (2, for T3) |
| T2 to T8 | backend-dev, web-dev, agentic-workflow, qa | not started; T3 waits for `devops`, T8 for the founder's API account |
| Dashboard counters (RCPT-11) | dashboard | scheduled, before the first real user |
| Spike on made-up receipts (experiment 1) | founder's account and go | waiting on the founder |

## Rulings

Decisions agents took themselves, for the founder at the next stopping point
(`skills/handoff/`, "Rulings").

1. **The area is new, prefix `RCPT`.** Why: no existing area fits a feature's rows. Cost if
   wrong: a rename of the area's ids, cheap now.
2. **RCPT-4 refines LAUNCH-5 instead of replacing it.** Why: LAUNCH-5 says the AI only
   suggests, RCPT-4 adds when the user may change it; neither repeats the other. Cost if wrong:
   one row marked "Covered by", cheap.
3. **A receipt counts in the month of its printed date** (or the date the user set), not the day
   it was saved (review N4). Why: "where the money goes each month" is about when it was spent.
   Cost if wrong: one query changes; no data is lost, both dates are kept.
4. **A symbol naming more than one currency ("$") is treated like no currency** (review N8): the
   user picks. Why: guessing a currency would put money in the wrong total. Cost if wrong: one
   extra tap for some users.
5. **N9 checked by the orchestrator, not a fourth review round.** Why: a one-line record fix,
   verified by `grep -c` (1 match); a fresh deep-tier reviewer costs a full read. Cost if wrong:
   a stale decision entry, caught by the next review.

6. **The readiness gate is run twice** (`readiness.md`). Why: lines 5 to 7 need the architect's
   files, and the architect is only routed after the gate passes, so the gate as written can never
   open. Pass 1 opens design only; pass 2 opens build. Cost if wrong: none to the product; it
   bends a process rule, so it goes to `reviewer` with the design (crosses the gate, a module of
   the process).
7. **AI answer limits** (`agentic.md`): at most 300 output tokens; a date more than one day in the
   future is treated as not found. Why: the answer is five short fields; a future date is a misread.
   Cost if wrong: a rare long receipt answer cut off, seen in the evals.

Rulings 1 to 4 were put to the founder on 2026-10-28 with the spec and kept. Rulings 5 to 8 go to
her at the next stopping point, with the screenshots.
8. **Design review F1 closed by the orchestrator after the third round with the same reviewer**
   (`agents/orchestrator.md`: three rounds with the same agent, then two with a fresh deep-tier
   one, then adjudication). The fix is the reviewer's own sentence, copied into `ux.md` step 4,
   checked by `grep`; S17 taken as its second option (the browser's own words). Why: a fresh
   deep-tier reviewer would read the whole design again for one sentence. Cost if wrong: a stale
   line in `ux.md`, caught by `reviewer` on the T6 diff.
9. **T1 accepts any three-letter currency code** and leaves the ISO 4217 table check to the save
   (contract "Fields"). Why: the table lives on the server (review S5) and T1 has no database.
   Cost if wrong: an unknown code reaches the check screen and is refused at save.
