**Not legal advice.** A starting checklist for the `legal` agent, to be reviewed by counsel before launch.

# Region pack: Germany (DE)

As of: 2026-10-14

Setup copied this file from `_TEMPLATE.md` and filled it from current primary sources. Anything uncertain is marked UNSETTLED with the sources that disagree. A pack older than 90 days is re-checked before any launch.

## Laws that apply

| Law | Applies because | Regulator | Status |
|---|---|---|---|
| Regulation (EU) 2016/679 (GDPR) and BDSG | Processing personal data of users in Germany | BfDI / State Data Protection Authorities (LDI) | in force |
| Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG) | Storing or accessing data on user devices (cookies, tokens) | Federal Network Agency (BNetzA) / BfDI | in force |
| Digitale-Dienste-Gesetz (DDG) | Provider identification and digital service obligations | Federal Network Agency (BNetzA) | in force (since 14 May 2024) |
| Bürgerliches Gesetzbuch (BGB) §§ 312g, 312j, 312k, 356 | Consumer subscription contracts, cancellation button, withdrawal rights | Federal Ministry of Justice (BMJ) / Consumer Courts | in force |
| Regulation (EU) 2024/1689 (EU AI Act) | AI interaction transparency and synthetic processing | European AI Office / National Competent Authorities | in force (since 1 August 2024; Art. 50 phase-in) |
| Preisangabenverordnung (PAngV) | Displaying prices to consumers with VAT included | Consumer Protection Agencies / Courts | in force |

## Checklist

Grade each item GREEN, YELLOW, RED or UNSETTLED per feature or launch (`skills/legal-review/`).

- **Data protection:** GDPR applies in full. Lawful basis required (contract performance under Art. 6(1)(b) for core features, consent under Art. 6(1)(a) for optional analytics). Privacy notice must list data categories, processing purposes, legal bases, retention periods, and user rights (access, rectification, erasure, restriction, objection, and portable export under Art. 20). Breach notification to supervisory authority within 72 hours.
- **Cross-border transfer:** Chapter V GDPR governs data transfers outside the European Economic Area. Transfers of receipt images or text to US-based AI APIs (such as OpenAI) require verification of provider certification under the EU-U.S. Data Privacy Framework or execution of Standard Contractual Clauses (SCCs) with a documented Transfer Impact Assessment (TIA). Legal counsel must review provider terms before production deployment.
- **Consent and tracking:** Section 25 TDDDG requires prior, informed, freely given consent before storing or reading non-essential identifiers on a user device. Essential session cookies do not require consent. Pre-checked consent boxes are prohibited.
- **Consumer law:** BGB § 312g grants consumers a statutory 14-day right of withdrawal for online contracts. For digital services starting immediately, BGB § 356(5) allows the right of withdrawal to expire if the consumer gives explicit prior consent and acknowledges the loss of the withdrawal right. Checkout buttons must clearly read "zahlungspflichtig bestellen" or equivalent unambiguous wording under BGB § 312j. Subscription services must feature a prominent, easily accessible online cancellation button ("Kündigungsbutton") under BGB § 312k.
- **E-commerce and payments:** Section 5 DDG (replacing former § 5 TMG) requires an easily reachable, directly accessible, and permanently available provider identification (Impressum) containing company name, legal structure, postal address, email, and register details. Invoices must show applicable VAT (Mehrwertsteuer at 19%). Prices shown to German consumers must include VAT under PAngV.
- **AI:** Regulation (EU) 2024/1689 (EU AI Act) Article 50 requires providers to inform natural persons when they are interacting with an AI system or when content has been artificially generated or sorted. The UI must clearly disclose that receipt data extraction and categorization are automated.
- **Device identifiers:** Section 25 TDDDG applies to device fingerprinting and client-side storage alike, requiring consent if used for cross-site or non-essential tracking.
- **Sector rules:** Expense organization and budgeting do not constitute banking or licensed financial advice under the German Banking Act (KWG), provided the service does not execute payments directly or hold customer deposits. Payment collection must be handled through a licensed payment gateway.
- **Accessibility:** Barrierefreiheitsstärkungsgesetz (BFSG) mandates accessibility compliance for consumer-facing digital services effective June 2025. Web design should follow WCAG 2.1 AA standards.
- **App stores and platforms:** Web platform deployed on Cloudflare Pages.
- **Language:** Consumer contracts, terms of service, privacy notices, withdrawal instructions, and checkout language must be provided in German to be legally enforceable against consumers residing in Germany.

## Sources

- Regulation (EU) 2016/679 of the European Parliament and of the Council (General Data Protection Regulation), in force 25 May 2018, checked 2026-10-14: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Digitale-Dienste-Gesetz (DDG) vom 6. Mai 2024, BGBl. 2024 I Nr. 149, in force 14 May 2024, replacing Telemediengesetz (TMG), checked 2026-10-14: https://www.recht.bund.de/bgbl/1/2024/149/VO.html
- Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG), checked 2026-10-14: https://www.gesetze-im-internet.de/tdddg/
- Bürgerliches Gesetzbuch (BGB) §§ 312g, 312j, 312k, 356 (Consumer contracts and cancellation rules), checked 2026-10-14: https://www.gesetze-im-internet.de/bgb/
- Regulation (EU) 2024/1689 of the European Parliament and of the Council (Artificial Intelligence Act), in force 1 August 2024, checked 2026-10-14: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Preisangabenverordnung (PAngV), checked 2026-10-14: https://www.gesetze-im-internet.de/pangv_2022/
