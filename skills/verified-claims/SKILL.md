---
name: verified-claims
description: No unconfirmed assumptions - every factual claim the founder or a user will read is confirmed by a source, test or measurement, or cut, or registered in docs/ASSUMPTIONS.md and labelled. Use when writing any document, copy, report, estimate or recommendation, and when reviewing one.
---

# Verified claims

A plausible guess reads exactly like a fact. Once it is written down, the next agent repeats it
and the founder makes a decision on it. So guesses are not written down as facts.

## Before a claim goes in

For each statement of fact (a price, a duration, a limit, a count, a date, legal status, what a
tool or service supports, what a test covers), ask: how do I know?

- **A source:** link it and the date you read it. Prefer the primary source (the provider's
  pricing page, the law, the official docs) over a blog about it. **Cite only a page you opened
  in this session**, and quote the sentence that supports the claim. A page you could not open
  is not a source: say so, or mark the claim UNSETTLED. Never write "checked" for a page you
  did not read. `python tools/link_check.py <files>` finds cited links that do not exist.
- **A test or measurement:** name it, or the command and its output.
- **Neither:** cut the claim, or say the true thing instead ("check the tool's pricing page"
  rather than a price you remember).

## When we have to rely on it anyway

Some things can only be confirmed later (how long setup takes, whether a tool loads a file the
way its docs say). Register each one in `docs/ASSUMPTIONS.md`:

| ID | Assumption | Used in | How to confirm | Confirm by | Status |

and label it where it is used, linking the register. The sweep fails when an open assumption is
past its confirm-by date. When it is confirmed or disproved, update the status and fix every
place it was used in the same change.

## Estimates

An estimate is allowed when it is labelled as one, with what it is based on: "about 3 hours,
estimated from the last two features of this size". An unlabelled number is a claim.

## Reviewing

When you review someone else's artifact, a claim with no source is a finding, the same as a bug.
