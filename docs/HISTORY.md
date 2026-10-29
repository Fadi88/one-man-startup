# History

What changed and why, newest first, each entry naming the requirement ids it touched. Never read
whole: grep for an id or a date.

## Changes

- **2026-10-29.** TPL-117, TPL-118: tailoring. The orchestrator logs signs of the founder's
  taste in `docs/requirements/p1-tailoring.md` and, seen twice, offers one as a standing rule on
  a decision card (`skills/tailoring/`); the README says so.
- **2026-10-29.** Experiment 1 (repo page) closed as mixed: 77 visitors in 14 days, 2 from
  github.com, the launch post inside the window; moved to `docs/EXPERIMENTS_CLOSED.md`.
- **2026-10-29.** TPL-113 to TPL-116, from a Reddit comment on the launch post: every decision
  put to the founder is a card with a recommendation, what could go wrong, how to undo it and two
  replies to copy (`skills/founder-voice/`), and open questions are checked for it by
  `tools/checks/card_check.py`; a hand-back names its folder, branch, commit and running version
  (`skills/handoff/`); a "done" report ends with one thing the founder can check themselves.
- **2026-10-28.** TPL-111, TPL-112: A/B testing on a random sample in `skills/experiment/` and
  `growth`, sized and read with `tools/ab_size.py`; A/B entries checked for their design. The
  dry run's old-against-new template comparison (TPL-108) is no longer called A/B.
- **2026-10-28.** TPL-105 to TPL-110, from a Reddit comment on the launch post: every review
  round opens with a founder list (what a user would see, blocks launch or can wait), checked by
  `tools/checks/review_check.py`; the orchestrator passes it on word for word; diff reviews check
  the rows of earlier features; the feature dry run gains a regression re-run (experiment 4).
  TPL-109, TPL-110: the sweep runs the product's whole test suite every round, and a row a
  release shipped must stay `T` (`tools/checks/regression_check.py`).
- **2026-10-28.** TPL-102 to TPL-104: `req_check.py` reads the product's test folders
  (`[stack] test_paths`), QA's spec-based regression run over the scope the orchestrator sets,
  and tests per area on the status page.
- **2026-10-28.** TPL-98 to TPL-101, from a pasted repository review: a living contract and
  screen description folded in at release (after OpenSpec), rows for an existing app written
  area by area (after Spec Kit's guide), the feature track for sign-in, payments, personal data,
  new dependencies and schema changes with three routing tests, and the sweep result on the
  status page; TPL-97: launch drafts removed from the repository and its history.
- **2026-10-28.** TPL-82 to TPL-96, TPL-57: fixes from the feature dry run. The readiness gate
  has a design pass and a build pass, with `tools/checks/gate_check.py` guarding product code;
  setup always recommends researcher, feasibility and reviewer; the grilling asks the AI quality
  bar, speed and interface languages; legal answers a blocking question before the spec; the
  product's AI cost is never compared with `[budget]`; re-reviews of documents use copies; the
  spend rule counts agents at once; screens are shown to the founder, never pointed at; the
  architect, backend and qa checklists gain what the reviewers caught; red flags in three
  discipline skills; render, link check and playbook fixes.
- **2026-10-28.** TPL-74 to TPL-81: a feature-track dry run (`examples/feature-dry-run/`), the
  commit hook refuses a subject without requirement ids, `grill-me` folded into `grilling`,
  `tools/template_update.py`, `tools/status_report.py`, `tools/run_evals.py` with nine routing
  cases, due dates at session start (`tools/lib/overdue.py`), and the modern product style for
  the README images, landing page and status page (`docs/images/STYLE.md`); TPL-38 now points at
  that style.
- **2026-10-21.** TPL-66 to TPL-73: eight practices taken from addyosmani/agent-skills (the
  performance and observability skills, schema expand-then-contract, the floor check, reviews
  briefed without the author's reasoning, contract rules with idempotency keys, test shape,
  flags for incomplete work); the rest recorded in `p1-rejected.md`.
- **2026-10-18.** TPL-57 to TPL-65: nine practices taken from obra/superpowers (excuse tables,
  fresh evidence, rulings, review focus, a capped fix loop, answering reviews, a session-start
  hook, typed discards, anti-goals and playback in grilling); experiment 3 opened on
  trigger-only descriptions; the rest recorded in `p1-rejected.md`.
