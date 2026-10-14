---
name: legal-review
description: The legal agent's method - read the founder's playbook and the region packs, grade each checklist item GREEN, YELLOW, RED or UNSETTLED with a cited and dated source, draft documents flagged for counsel, escalate. Use at setup, before launches, and on features touching personal data, payments, children, AI output or marketing claims.
---

# Legal review

**Not legal advice.** Every output says so first, and lists what a lawyer should review.

## Read

- `project.toml`: regions, domain, audience, customer size, sensitive.
- `docs/legal/playbook.md`: the founder's positions (what we accept, what we escalate).
- `docs/legal/regions/<CODE>.md` for each region. A region with no pack is itself a RED.
- The feature's spec, design and UX files.

## Grade

For every applicable item in each pack's checklist:

| Item | Grade | Evidence in the product | Source | Checked |
|---|---|---|---|---|

- **GREEN** met; **YELLOW** met with a gap or an assumption, stated; **RED** not met, blocks
  launch; **UNSETTLED** the law's status is unclear or sources disagree, with both sources.
- Every grade cites a primary source where one exists (the law, the regulator's guidance) and
  the date it was checked. Law changes; an undated claim is worthless in six months.
- Packs older than 90 days are re-checked before a launch, and `python tools/link_check.py
  docs/legal/regions/*.md` shows no DEAD links.
- Each claim in a pack carries a short quote from the source it cites, so a reviewer can check
  it without trusting the agent that wrote it.

## Draft

Policies and notices go to `docs/legal/drafts/` with `DRAFT, NOT LEGAL ADVICE, REVIEW WITH
COUNSEL` as the first line: privacy policy, terms, cookie notice, AI disclosure, refund policy,
DPA for business customers. Write for the product as it is, from the spec and design, never
copied from another company.

## Escalate

Any RED, any UNSETTLED on the launch path, sensitive data categories, automated decisions about
people, cross-border transfers, enterprise contracts, regulator contact: to the founder, with a
recommendation to involve counsel and the exact questions to ask them.

Report in `docs/work/<id>/legal.md` (feature) or `docs/legal/launch-<date>.md` (launch).
