**Not legal advice.** A starting checklist for the `legal` agent, to be reviewed by counsel before launch.

# Region pack: Germany (DE)

As of: 2026-10-14

Written by `setup` for Receipt Buddy (`project.toml`: personal finance, consumers, receipt
photos read by an AI provider, paid plan, founder based in the UAE). Every claim names its
source and whether it was opened on 2026-10-14. EUR-Lex returned empty pages that day, so the
texts of the GDPR, the Consumer Rights Directive, the Accessibility Directive, the AI Act and
the standard contractual clauses were not opened; points resting on them are marked "EU text
not opened" and `legal` confirms them on EUR-Lex before launch. German statutes were read on
gesetze-im-internet.de. Anything uncertain is UNSETTLED.

## Laws that apply

| Law | Applies because | Regulator | Status |
|---|---|---|---|
| GDPR, Regulation (EU) 2016/679 | Personal data of people in Germany, offered a service from outside the EU | German data protection authorities | in force (EU text not opened [1]) |
| BDSG (Federal Data Protection Act) | German additions to the GDPR | BfDI and state authorities | in force [2] |
| TDDDG s.25 | Storing or reading information on the user's device | data protection authorities | in force [3] |
| BGB consumer contract rules (ss.312 to 312k, 355, 356, 309) | Paid online subscriptions to consumers | civil courts, consumer associations | in force [4][5][6][7] |
| PAngV (price display) | Prices shown to consumers | state authorities | in force [8] |
| DDG s.5 (Impressum) | A commercial digital service | | in force [9] |
| UStG and the EU non-Union OSS scheme | Digital service sold to German consumers | Federal Central Tax Office | in force [10][11] |
| AI Act, Regulation (EU) 2024/1689 | An AI system used in the product | EU and national authorities | transparency duties from August 2026 per the Commission [12]; scope for this product UNSETTLED |
| BFSG (accessibility) | E-commerce services to consumers | market surveillance | in force since 28 June 2025; microenterprise exemption likely applies [13] |

## Checklist

Grade each item GREEN, YELLOW, RED or UNSETTLED per feature or launch (`skills/legal-review/`).

- **Data protection:** lawful basis per use (contract for reading receipts; EU text not
  opened). A controller outside the EU offering services to people in the EU must name a
  representative in the EU, and failing to do so is a breach (EDPB Guidelines 3/2018 [14]);
  the exemption for occasional, low-risk processing is unlikely to fit a subscription app.
  Raised for `legal` in `p1-open-questions.md`. Breach notice to the authority within 72 hours
  and answers to rights requests within one month (EU text not opened). A data protection
  officer is required in Germany where at least 20 people are regularly employed in automated
  processing, or regardless of headcount where a data protection impact assessment is needed
  (BDSG s.38 [2]). UNSETTLED: receipts can reveal special-category data (pharmacy items,
  donations, union dues); whether incidental inference makes this Art. 9 processing is
  contested. Mitigation already decided: the photo is deleted once read and checked. Children:
  adults only (closed decision 2026-10-14).
- **Cross-border transfer:** UNSETTLED. The EU-US Data Privacy Framework adequacy decision of
  10 July 2023 is in effect and covers only certified US recipients [15]. Secondary sources
  report that a challenge was dismissed by the General Court on 3 September 2025 and that an
  appeal is pending; not confirmed, as CURIA was not reachable. The UAE has no EU adequacy decision [16], so data reaching
  the founder or any service in the UAE needs another basis such as standard contractual
  clauses. Anthropic's processing is "global" or US only [17]. Raised for `legal`.
- **Consent and tracking:** storing or reading information on the device needs consent unless
  strictly necessary for the service the user asked for (TDDDG s.25 [3]). Analytics need
  consent unless `legal` finds them strictly necessary.
- **Consumer law:** the order button must read "zahlungspflichtig bestellen" or something
  equally clear (BGB s.312j(3) [4]); a permanent "Verträge hier kündigen" cancellation button
  leading to a "jetzt kündigen" confirmation (BGB s.312k [4]); limits on subscription terms:
  first term at most two years, tacit renewal only for an indefinite term cancellable with at
  most one month's notice (BGB s.309 Nr.9 [7]). Withdrawal: the right lapses early for
  services only on full performance with express consent and acknowledgement (s.356(5)), and
  for digital content when performance starts with consent, acknowledgement and confirmation
  (s.356(6)) [6]. UNSETTLED: how this applies to an ongoing app subscription as a digital
  service (BGB s.327), and whether s.312k reaches an app with no website. Exit offers and
  pre-selection: not researched; `legal` to check.
- **E-commerce and payments:** prices shown to consumers include VAT (PAngV ss.2, 3 [8]);
  Impressum with name, address, legal form, email, register number and VAT ID where one exists
  (DDG s.5 [9]). German VAT is 19% (UStG s.12 [10]); a business with no EU establishment can
  account for it through the non-Union OSS scheme, registering in one member state [11]. Place
  of supply in the customer's country: EU text not opened.
- **AI:** the Commission says the AI Act's transparency rules apply from August 2026 [12].
  Whether a receipt reader that produces no synthetic media and has no chat triggers them is
  UNSETTLED; an AI chat feature would. Automated decisions with legal or similar effects:
  none planned (closed decision 2026-10-14), so GDPR Art. 22 is unlikely to apply (EU text not
  opened).
- **Device identifiers:** TDDDG s.25 [3], as above.
- **Sector rules:** personal finance. An account information service is one that consolidates
  information on payment accounts held elsewhere (ZAG s.1(34) [18]); reading receipt photos
  with no access to payment accounts falls outside that definition. Adding bank linking would
  reopen this.
- **Accessibility:** the BFSG covers e-commerce services offered to consumers through websites
  and apps after 28 June 2025, and does not apply to microenterprises providing services
  (fewer than 10 staff and turnover or balance sheet at most EUR 2 million) [13]. A solo
  founder is likely exempt (assumption A-9, `docs/ASSUMPTIONS.md`); `legal` re-checks as the company grows.
- **App stores and platforms:** the stack is a web app; store rules apply only if a store app
  is added. Apple's EU terms changed on 1 October 2026 [19]; Google Play requires Play Billing
  for digital subscriptions [20]. Re-read both before any store app.
- **Language:** UNSETTLED. No general statutory requirement for German-language terms was found;
  terms a consumer cannot understand risk being unenforceable (not researched in a primary
  source). Recommended to `legal`: German terms and notices.

## Sources

1. GDPR, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679, fetch returned empty 2026-10-14, not opened.
2. BDSG s.38, https://www.gesetze-im-internet.de/bdsg_2018/__38.html, opened 2026-10-14.
3. TDDDG s.25, https://www.gesetze-im-internet.de/ttdsg/__25.html, opened 2026-10-14.
4. BGB ss.312j, 312k, https://www.gesetze-im-internet.de/bgb/, opened 2026-10-14.
5. BGB s.355, https://www.gesetze-im-internet.de/bgb/__355.html, not opened 2026-10-14.
6. BGB s.356, https://www.gesetze-im-internet.de/bgb/__356.html, opened 2026-10-14.
7. BGB s.309, https://www.gesetze-im-internet.de/bgb/__309.html, opened 2026-10-14.
8. PAngV ss.2, 3, https://www.gesetze-im-internet.de/pangv_2022/__2.html and https://www.gesetze-im-internet.de/pangv_2022/__3.html, opened 2026-10-14.
9. DDG s.5, https://www.gesetze-im-internet.de/ddg/__5.html, opened 2026-10-14.
10. UStG s.12, https://www.gesetze-im-internet.de/ustg_1980/__12.html, opened 2026-10-14.
11. European Commission, VAT One Stop Shop registration, https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en, opened 2026-10-14.
12. European Commission, "AI Act", https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, opened 2026-10-14.
13. BFSG ss.1 to 3, https://www.gesetze-im-internet.de/bfsg/, opened 2026-10-14.
14. EDPB Guidelines 3/2018 on territorial scope, https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_3_2018_territorial_scope_after_public_consultation_en_1.pdf, read from extracts 2026-10-14.
15. European Commission, EU-US data transfers, https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en, opened 2026-10-14.
16. European Commission, adequacy decisions, https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en, opened 2026-10-14.
17. Anthropic, "Data residency", https://platform.claude.com/docs/en/manage-claude/data-residency, opened 2026-10-14.
18. ZAG s.1, https://www.gesetze-im-internet.de/zag_2018/__1.html, opened 2026-10-14.
19. Apple, "Distributing apps in the EU", https://developer.apple.com/support/dma-and-apps-in-the-eu/, opened 2026-10-14.
20. Google, "Payments", Play Console Help, https://support.google.com/googleplay/android-developer/answer/9858738, opened 2026-10-14.
