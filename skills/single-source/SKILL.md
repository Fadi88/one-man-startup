---
name: single-source
description: Every derived figure (a total, a price, a score, a status) is computed in exactly one place and read everywhere; documents never carry hand-typed counts. Use when adding any number a user or the founder will see.
---

# Single source of truth

Two places that compute the same figure will disagree one day, and the day they do, nobody will
know which is right.

- A figure is computed once, in one function, on the side that owns its data (usually the
  server). Every screen, export, email and report reads that result.
- A client that needs a figure gets it from the contract; it does not recompute it.
- Documents never carry counts typed by hand ("42 requirements", "12 endpoints"). A script
  computes them, and the sweep checks they are current. A plausible number looks exactly like a
  correct one.
- When you find a second computation, do not fix the one that looks wrong. Delete one, point it
  at the other, and add a test that would have caught the drift.
