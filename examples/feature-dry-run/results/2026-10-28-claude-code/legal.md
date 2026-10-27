Not legal advice. This is a checklist for the founder and her lawyer; a lawyer should review every UNSETTLED item below before any real user's receipt is processed.

# Legal: RCPT-1, a receipt photo sorted into a spending category

Written by `legal`, following `skills/legal-review/`. Packs read: `docs/legal/regions/AE.md` and
`docs/legal/regions/DE.md` (As of 2026-10-14, under 90 days old);
`python tools/link_check.py docs/legal/regions/AE.md docs/legal/regions/DE.md` on 2026-10-28:
"31 URLs, 0 dead, 0 to open by hand". Playbook: `docs/legal/playbook.md`.

## Part 1, before the gate (2026-10-28): the open question on health information in receipts

`p1-open-questions.md` says this question "Blocks: the categorisation feature's spec", so it is
answered before the readiness gate rather than after the design.

| Item | Grade | Evidence in the product | Source | Checked |
|---|---|---|---|---|
| DE: receipts can reveal special-category data (pharmacy items, donations, union dues) | UNSETTLED | No health category (RCPT-3); one category per receipt, no item lines stored (RCPT-2 stores shop, date, total, category); photo deleted once read (LAUNCH-6) or after 24 hours (RCPT-15) | DE pack, Checklist, "Data protection": "whether incidental inference makes this Art. 9 processing is contested" | 2026-10-28 |
| AE: sensitive data under the PDPL | UNSETTLED | as above | AE pack, Checklist, "Data protection" (secondary summary [2]; the article numbers were not checked against the official text) | 2026-10-28 |

The pack does not settle the question and I do not settle it either. What the design changes is
the size of the risk: the app would never label a receipt as health, and it keeps no item lines,
so what it stores is the shop name, a date, a total and one of six categories. The shop name
alone (a pharmacy) can still hint at health.

**For the founder (a decision, `docs/legal/playbook.md` escalates "Sensitive categories"):**

1. Build and test with made-up receipts now, with the protections above, and ask a lawyer
   before any real user's receipt is read. My recommendation: yes. The question then blocks the
   first real users (beta), not the plan or the build.

**Questions for counsel:** is storing a shop name that is a pharmacy, with a total, special-category
processing under GDPR Art. 9 when no item is stored and no health label is applied? Does the UAE
PDPL treat it as sensitive data?

## Part 2, on the design (2026-10-28)

Read: `spec.md`, `design.md`, `ux.md`, `agentic.md`, the screenshots, both packs, the playbook.

| Item | Grade | Evidence in the product | Source | Checked |
|---|---|---|---|---|
| Permission before the first read (LAUNCH-7) | YELLOW | Screen 1 names Anthropic and asks; but "Not now" is a text link under a filled button, so the choice leans toward yes | DE pack, "Consent and tracking"; playbook "never pre-ticked"; `agents/product-designer.md` "No dark patterns" | 2026-10-28 |
| Screen 1 says "we don't keep the photo afterwards" | YELLOW | True for Receipt Buddy (ADR 0001). What Anthropic keeps is not shown on screen 1; the vision page says "Image uploads are ephemeral and not stored beyond the duration of the API request", but Anthropic's API data retention terms were not read for this review | https://platform.claude.com/docs/en/build-with-claude/vision (FAQ) | 2026-10-28 |
| Cross-border transfer (photo to Anthropic, data to Frankfurt) | UNSETTLED | Unchanged by the design; blocks beta (`p1-open-questions.md`) | both packs, "Cross-border transfer" | 2026-10-28 |
| AI transparency | UNSETTLED | Screen 1 says the AI reads and picks; the check screens do not say the category came from AI | DE pack, "AI": "Whether a receipt reader that produces no synthetic media and has no chat triggers them is UNSETTLED" | 2026-10-28 |
| Automated decisions about people | GREEN | The AI suggests; the user saves every receipt (RCPT-2, LAUNCH-5) | DE pack, "AI"; closed decision 2026-10-14 | 2026-10-28 |
| Data kept and deleted | GREEN | Photo never stored (ADR 0001); figures deleted on delete or with the account (RCPT-20, LAUNCH-9) | playbook "Retention"; LAUNCH-6 | 2026-10-28 |
| Export includes all personal data (review N5) | YELLOW | RCPT-19 keeps the AI's category and hides it from users; an access or export request (LAUNCH-10) should include it, since it is data about the user's receipts | DE pack, "Data protection" (rights requests; EU text not opened) | 2026-10-28 |
| Special-category data | UNSETTLED | Part 1; the founder's decision stands; counsel before beta | part 1 | 2026-10-28 |

**For the founder** (through the orchestrator): none of these blocks the build. Before any real
user: the transfer and special-category questions go to counsel (already open). Two fixes for
the designer: give "Not now" equal weight on screen 1, and say on screen 1 what Anthropic keeps
once its terms are read. One row to add: the export (LAUNCH-10) includes the AI's category.

**Questions for counsel:** as part 1, plus: does a receipt reader that only suggests a category
fall under the AI Act's transparency duties?
