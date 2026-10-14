**Not legal advice.** A starting checklist for the `legal` agent, to be reviewed by counsel before launch.

# Region pack: <COUNTRY OR BLOC> (<ISO CODE>)

As of: <YYYY-MM-DD, the date the sources below were checked>

Setup copies this file to `<CODE>.md` for each region in `project.toml` and fills it from current
primary sources. Anything uncertain is marked UNSETTLED with the sources that disagree. A pack
older than 90 days is re-checked before any launch.

## Laws that apply

| Law | Applies because | Regulator | Status |
|---|---|---|---|
| | | | in force / UNSETTLED |

## Checklist

Grade each item GREEN, YELLOW, RED or UNSETTLED per feature or launch (`skills/legal-review/`).

- **Data protection:** lawful basis for each use of personal data; privacy notice contents;
  user rights (access, correction, deletion, export, objection) and response times; breach
  notification (to whom, how fast); records of processing; data protection officer or
  representative if required; children's data and age thresholds.
- **Cross-border transfer:** may personal data leave the region, and on what basis.
- **Consent and tracking:** cookies, analytics and marketing consent rules.
- **Consumer law:** pricing display, subscriptions and auto-renewal, cancellation, refunds and
  cooling-off periods, unfair terms.
- **E-commerce and payments:** required business information, invoices, tax on digital services.
- **AI:** disclosure of AI interaction and generated content, automated decision rules,
  high-risk uses.
- **Sector rules** for the domain in `project.toml` (health, finance, education, children).
- **Accessibility:** legal accessibility requirements for digital services.
- **App stores and platforms:** the store rules for the platform in `project.toml [stack]`.
- **Language:** whether terms or notices must be offered in a local language.

## Sources

- <primary source, URL, date checked>
