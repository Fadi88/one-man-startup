---
name: tailoring
description: Turn the founder's taste into rules - notice a preference they show (a correction, a draft they reword, "I prefer", "always", "never"), log it, and on the second sign suggest it as a standing instruction with a decision card. Use when the founder corrects or rewords work, states a preference, or turns something down for taste rather than fact.
---

# Tailoring

The template starts with the same rules for everyone. Tailoring makes it the founder's: the
orchestrator notices what they like and dislike and offers it back as a rule, so they never have
to say it a third time (TPL-117).

## Notice

A sign of taste is any of:

- a correction of finished work ("too long", "no emojis", "say baht, not THB");
- a draft they reword before using it: the difference is the preference;
- "I prefer", "I like", "I hate", "always", "never", "from now on";
- a proposal turned down for taste, not for a fact (that one also goes in `p1-rejected.md`).

Log each one the same day in `docs/requirements/p1-tailoring.md`: the date, their words quoted
exactly, and what it was about. A paraphrase drifts.

## Suggest

Suggest a rule when the same preference shows a second time, or the first time they say
"always", "never" or "from now on". At most one suggestion per stopping point, after the work
in hand, never in the middle of a decision about something else. Use the card
(`skills/founder-voice/card.md`):

```
**Decision:** make this a standing rule: "Prices are shown in baht, never in dollars."
**Recommendation:** yes. You corrected this on 3 and 9 November.
**Could go wrong:** a page for foreign visitors would also show baht.
**Undo:** I remove the line; one minute.
**Reply with one:**
`yes, make it a rule`
`no, it depends`
```

Word the rule so a stranger could follow it, and say where it applies (copy, design, reports,
code, the way agents talk to them).

## After the answer

- **Yes:** add it to `p1-standing-instructions.md` under "From the founder", with the date and
  their words, and mark the log entry `-> rule`. If it must always hold and a check can see it
  (a word that must never appear, a currency, a length), propose that check as a requirement
  row: a rule that must hold is enforced (rule 5).
- **No:** record it in `p1-rejected.md` with their reason, mark the log entry `-> declined`, and
  do not suggest it again without a new sign.
- **Not now:** mark it `-> later`; it may come back after a third sign.

## Limits

A preference never loosens the constitution in `AGENTS.md`. "Just deploy, don't ask" is not
tailoring; it is a change to rule 2, put to the founder as that, with what it would risk. Taste
about how things look or read is tailoring; a target, a price or a legal position is a decision
for `skills/decision-log/`.
