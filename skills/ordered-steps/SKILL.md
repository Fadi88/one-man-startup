---
name: ordered-steps
description: Outward and irreversible actions wait for the founder's explicit go, one step at a time - "do X, then deploy" means show X and stop. Use before any deploy, merge, push, publish, send, payment, deletion or production data change.
---

# Ordered steps wait

## Two kinds of action

- **Inward:** reading, searching, running tests, writing drafts and code on a branch. Do these
  freely and in parallel.
- **Outward or irreversible:** deploy, merge to main, push, publish, send an email or message to
  anyone, spend money, delete, write to production data, change permissions or settings. Each
  needs the founder's go **for that step**.

## "Then" is a gate

When the founder says "do X, then Y" and Y is outward, do X, show the result, and wait for the
go before Y. Approval for one step does not carry to the next, and approval yesterday does not
carry to today.

## Asking

State exactly what will happen, to what, and whether it can be undone. "Ready to deploy v1.4 to
production; rollback is redeploying v1.3, about two minutes. Go?" Never bundle several outward
steps into one yes.
