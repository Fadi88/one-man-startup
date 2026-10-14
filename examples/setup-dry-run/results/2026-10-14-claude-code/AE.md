**Not legal advice.** A starting checklist for the `legal` agent, to be reviewed by counsel before launch.

# Region pack: United Arab Emirates (AE)

As of: 2026-10-14

Written by `setup` for Receipt Buddy (`project.toml`: personal finance, consumers, receipt
photos read by an AI provider, paid plan). Every claim names its source and whether the page
was opened on 2026-10-14. The official legislation site (uaelegislation.gov.ae) and the Central
Bank rulebook refused access (HTTP 403) on that date, so most law content below rests on law
firm summaries, marked "secondary". `legal` confirms each against the official text before
launch. Anything uncertain is UNSETTLED.

## Laws that apply

| Law | Applies because | Regulator | Status |
|---|---|---|---|
| Federal Decree-Law No. 45 of 2021 on the Protection of Personal Data (PDPL) | Personal data (email, receipts) of people in the UAE | UAE Data Office | in force since 2 January 2022 [1]; executive regulations UNSETTLED [2][3] |
| Federal Law No. 15 of 2020 on Consumer Protection and its executive regulations, Cabinet Decision No. 66 of 2023 | Paid service to consumers | Ministry of Economy | in force; regulations effective 14 October 2023 (secondary [4]) |
| Federal Decree-Law No. 14 of 2023 on Modern Technology Trade | Selling through a website or app | Ministry of Economy | UNSETTLED: effective date and implementing regulations not confirmed (secondary, not opened [5]) |
| Federal VAT law (Decree-Law No. 8 of 2017) | Digital service sold to UAE consumers | Federal Tax Authority | in force; thresholds from the FTA [6]; electronic services rule from secondary sources only [7] |
| CBUAE Open Finance Regulation | Only if the product accessed bank data or made payments | Central Bank of the UAE | likely not applicable, UNSETTLED [8] |
| Free zone laws (DIFC Data Protection Law No. 5 of 2020; ADGM Data Protection Regulations 2021) | Only if the business is set up in DIFC or ADGM | DIFC / ADGM commissioners | not applicable unless the company is formed there (secondary [2][3]) |

## Checklist

Grade each item GREEN, YELLOW, RED or UNSETTLED per feature or launch (`skills/legal-review/`).

- **Data protection:** the PDPL makes consent the default basis, with exceptions including
  performing a contract; it gives rights of access, portability, correction or erasure,
  restriction, objection and rights on automated decisions; it requires breach notification to
  the Data Office with timing left to the executive regulations; a data protection officer is
  needed for high-risk processing or large volumes of sensitive data; and it reaches
  controllers outside the UAE who process data of people in the UAE. All of this is from a
  secondary summary [2]; the article numbers were not checked against the official text.
  UNSETTLED: whether the executive regulations have been issued. Two law firm guides say not
  [2][3]; some vendor blogs (not opened) claim they have, without citing a resolution number.
  Treat as not issued until an Official Gazette number is found. Children: the product is for
  adults only (closed decision 2026-10-14).
- **Cross-border transfer:** UNSETTLED. Transfers are allowed to countries the Data Office
  finds adequate or under an agreement, otherwise only under listed exceptions (secondary
  [2][3]); no adequacy list was found. Receipt Buddy's planned stack sends data out of the UAE:
  the database in Frankfurt [9] and receipt images to Anthropic, whose processing options are
  "global" or US only [10]. Raised for `legal` in `p1-open-questions.md`.
- **Consent and tracking:** UNSETTLED. No UAE cookie-specific rule was found; whether the PDPL's
  general consent rules require opt-in for analytics cookies is disputed by vendor blogs (not
  opened). `legal` decides per the closed decision on consent banners.
- **Consumer law:** price display rules and refund options when a service fails (executive
  regulations Arts. 5 and 13, secondary [4]); e-commerce suppliers must give identity and
  service details (Art. 40, secondary [4]). UNSETTLED: any Arabic-language or AED-pricing duty
  for app text, terms or invoices was not confirmed. Auto-renewal, cancellation and exit
  offers: not researched; `legal` to check.
- **E-commerce and payments:** VAT is 5% (shown on the FTA site [6]). The mandatory
  registration threshold of AED 375,000 "is not applicable to foreign businesses" [6].
  Electronic services used in the UAE are taxed there (secondary [7], FTA guide not opened).
  Whether an app store or merchant of record collects the VAT instead: not confirmed. The
  payment route is an open founder decision.
- **AI:** no binding federal AI statute was found (secondary trackers, not opened). The UAE
  Charter for the Development and Use of AI is non-binding (secondary). A claimed "Dubai AI Act"
  rests on one low-quality site and is treated as unconfirmed. The app makes no decisions about
  people (closed decision 2026-10-14). Apple's guideline 5.1.2(i) requires clear disclosure and
  explicit permission before personal data is shared with a third-party AI [11].
- **Device identifiers:** UNSETTLED, as for consent and tracking.
- **Sector rules:** personal finance. A spending tracker that only reads receipt photos, with no
  bank account access, payments, stored value or advice, does not appear to need a Central Bank
  licence under the Open Finance Regulation (secondary [8]; rulebook not opened). UNSETTLED
  until `legal` reads the rulebook. Adding bank account linking reopens this.
- **Accessibility:** UNSETTLED. A TDRA National Digital Accessibility Policy of 18 March 2024
  is reported to cover private providers of public services including e-commerce (search
  results only); whether any binding duty reaches a private consumer app was not confirmed.
- **App stores and platforms:** the stack is a web app, so store rules apply only if a store
  app is added. For reference: Apple 3.1.1 requires in-app purchase for subscriptions that
  unlock features [11]; Google Play requires Play Billing for digital subscriptions [12].
- **Language:** UNSETTLED, see consumer law.

## Sources

1. UAE Government portal, "Data protection laws", https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws, opened 2026-10-14.
2. DLA Piper, Data Protection Laws of the World, UAE (as of 6 January 2025), https://www.dlapiperdataprotection.com/countries/uae-general/law.html, secondary, opened 2026-10-14.
3. Pinsent Masons, "Business in the UAE: navigating the data protection regime" (2 March 2023), https://www.pinsentmasons.com/en-gb/out-law/guides/business-in-the-uae-navigating-data-protection-regime, secondary, opened 2026-10-14.
4. Bracewell, "Seller beware: impact of new executive regulations under UAE's consumer protection law", https://www.bracewell.com/resources/seller-beware-impact-new-executive-regulations-under-uaes-consumer-protection-law/, secondary, opened 2026-10-14.
5. Reed Smith, "UAE federal law on modern trading by technological means", https://www.reedsmith.com/our-insights/blogs/viewpoints/102iqny/uae-federal-law-on-modern-trading-by-technological-means/, secondary, not opened (search result only), 2026-10-14.
6. Federal Tax Authority, "Registration for VAT", https://tax.gov.ae/en/taxes/vat/vat.topics/registration.for.vat.aspx, opened 2026-10-14.
7. PwC, "FTA publishes e-commerce VAT guide" (2020), https://www.pwc.com/m1/en/tax/documents/2020/united-arab-emirates-fta-publishes-e-commerce-vat-guide.pdf, secondary, not opened, 2026-10-14.
8. Pinsent Masons, "UAE open finance" (updated 3 November 2025), https://www.pinsentmasons.com/out-law/guides/uae-open-finance, secondary, opened 2026-10-14. The CBUAE rulebook (rulebook.centralbank.ae) returned 403.
9. Supabase, "Regions", https://supabase.com/docs/guides/platform/regions, opened 2026-10-14 (Frankfurt listed; no UAE or Middle East region).
10. Anthropic, "Data residency", https://platform.claude.com/docs/en/manage-claude/data-residency, opened 2026-10-14.
11. Apple, App Store Review Guidelines, https://developer.apple.com/app-store/review/guidelines/, opened 2026-10-14.
12. Google, "Payments", Play Console Help, https://support.google.com/googleplay/android-developer/answer/9858738, opened 2026-10-14.
