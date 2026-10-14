---
name: experiment
description: Run every bet, growth idea or workflow change as a pre-registered experiment - hypothesis, the number that would prove it, a read date, and what result would make it wrong - written before it starts. Use for pricing, copy, onboarding, channels, cost cuts and any "let's try".
---

# Experiment

Write the entry in `docs/EXPERIMENTS.md` **before** the change ships. An experiment written after
the result is a story.

## The entry

```markdown
### 7. Annual plan at two months free, from 2026-03-01
- **Why:** monthly churn is 9 percent; annual buyers churn less.
- **Change:** one change only: the annual option on the pricing page.
- **Hypothesis:** some monthly buyers choose annual.
- **Prediction:** at least 15 percent of new paid sign-ups pick annual within 30 days.
- **Wrong if:** under 5 percent pick annual. Then the annual option comes off and we look at
  churn reasons instead.
- **Confounds:** the launch post on 2026-03-03 brings unusual traffic.
- **Read:** 2026-03-31.
```

And one line in the "At a glance" table at the top of the file.

## Rules

- One change at a time, or the result cannot be attributed.
- The read date is kept. Reading early because it looks good is how false wins happen.
- Record what the numbers say, not what was hoped. "Not distinguishable from noise" is a result.
- A closed experiment moves to `docs/EXPERIMENTS_CLOSED.md` with its numbers and verdict.
