**Not legal advice.** A starting checklist for the `legal` agent, to be reviewed by counsel before launch.

# Region pack: United Arab Emirates (AE)

As of: 2026-10-14

Setup copied this file from `_TEMPLATE.md` and filled it from current primary sources. Anything uncertain is marked UNSETTLED with the sources that disagree. A pack older than 90 days is re-checked before any launch.

## Laws that apply

| Law | Applies because | Regulator | Status |
|---|---|---|---|
| Federal Decree-Law No. 45 of 2021 on Personal Data Protection (PDPL) | Processing personal data of UAE residents (emails, receipt images) | UAE Data Office | in force (Executive Regulations UNSETTLED) |
| Federal Law No. 15 of 2020 on Consumer Protection | Offering consumer services and paid subscriptions in the UAE | Ministry of Economy | in force |
| Federal Decree-Law No. 14 of 2023 on Commerce through Modern Technology Means | Digital commerce and online transactions | Ministry of Economy / TDRA | in force |
| Federal Decree-Law No. 34 of 2021 on Cybercrimes | Data security, unauthorized access, electronic payments | UAE Cyber Security Council / Ministry of Interior | in force |

## Checklist

Grade each item GREEN, YELLOW, RED or UNSETTLED per feature or launch (`skills/legal-review/`).

- **Data protection:** Federal Decree-Law No. 45 of 2021 sets the primary data protection framework. Lawful basis required (consent or contract performance). Privacy notice must state processing purpose, data categories, and user rights (access, correction, erasure, restriction). Breach notification required to UAE Data Office and data subjects without undue delay. DPO required if processing involves high risk or large scale data processing.
- **Cross-border transfer:** Personal data transfer outside the UAE is governed by Articles 22 and 23 of the PDPL. Permitted to countries with an adequate level of protection, or under appropriate safeguards (standard contractual clauses approved by the Data Office, binding corporate rules, or explicit user consent). UNSETTLED: The formal list of adequate jurisdictions and standard clauses awaits final executive regulations. Sending receipt images or text to US-hosted AI APIs (such as OpenAI) requires legal counsel review and explicit user consent as a safeguard.
- **Consent and tracking:** Consent required for processing personal data unless a statutory exemption applies. Electronic direct marketing requires explicit prior opt-in consent.
- **Consumer law:** Federal Law No. 15 of 2020 mandates fair pricing, clear contract terms, and prohibits deceptive subscription practices. Total price must clearly indicate any applicable taxes (VAT at 5%). Terms and conditions must be transparent before purchase.
- **E-commerce and payments:** Federal Decree-Law No. 14 of 2023 requires digital commerce providers to maintain transparent business details, provide electronic invoices/receipts, and process payments through licensed payment service providers.
- **AI:** PDPL Article 18 grants data subjects the right to object to decisions based solely on automated processing. Users must be notified that receipt data extraction and expense categorization use automated AI models.
- **Device identifiers:** UNSETTLED. Whether non-cookie device identifiers or tracking require explicit consent awaits operational guidance in the PDPL executive regulations.
- **Sector rules:** Receipt Buddy provides household budgeting and does not handle deposits, credit, or regulated investment advice, so a Central Bank financial institution license is not required. Payment processing must integrate with an authorized payment aggregator (such as Stripe UAE).
- **Accessibility:** UAE National Policy for Empowering People of Determination encourages digital accessibility across online services.
- **App stores and platforms:** Web platform deployed via Cloudflare Pages.
- **Language:** Federal Law No. 15 of 2020 requires consumer contracts, terms, warnings, and customer service to be made available in Arabic alongside English.

## Sources

- UAE Federal Decree-Law No. 45 of 2021 on the Protection of Personal Data, official text published in the UAE Official Gazette No. 716, in force 2 January 2022, checked 2026-10-14: https://uaecabinet.ae/en/legislation
- UAE Federal Law No. 15 of 2020 on Consumer Protection, Ministry of Economy, in force 2020, checked 2026-10-14: https://www.moec.gov.ae/en/consumer-protection
- UAE Federal Decree-Law No. 14 of 2023 on Commerce through Modern Technology Means, Ministry of Economy, checked 2026-10-14: https://www.moec.gov.ae
- Auro Security, Overview of UAE PDPL Implementation and Pending Executive Regulations, checked 2026-10-14: https://www.aurosecurity.com/uae-pdpl-guide
- Chambers and Partners, Data Protection and Privacy: United Arab Emirates Practice Guide, checked 2026-10-14: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2024/united-arab-emirates
