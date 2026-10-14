---
name: known-reds
description: The register of failing checks the founder has decided to live with for now, each matched by its failing line, owned and dated. Use when a red is accepted, rechecked or fixed.
---

# Known reds

`tools/known_red.json` is a list. Each entry:

```json
{
  "check": "pricing_check.py",
  "fails": "FAIL  monthly price under the floor",
  "reason": "Launch discount, decided on the 1 March call.",
  "decided_by": "founder",
  "decided_on": "2026-03-01",
  "recheck": "2026-04-01"
}
```

- `fails` is matched against the failing line, not the file. A second, different failure in the
  same check still shows as NEW RED.
- `recheck` is a date, or `null` for a standing decision. An overdue recheck turns the sweep red.
- When the check passes again the sweep says "now passes, prune"; remove the entry in the same
  change.
- Keep `reason` to one or two sentences. The register is a list, not a diary.

Only the founder adds an entry. An agent proposes the exact entry and waits.
