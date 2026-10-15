# Playbook: B2C organic growth

For projects whose `project.toml [product] customer_size` is `consumers`. The `growth` agent
works from this file; the founder decides every value marked **Founder decides**. Nothing here
is a fact about any particular market or product: numbers come from the project's own
experiments and from sources the agents cite and date (`skills/verified-claims/`).

## 1. Validate before you build

1. **Smoke test, before any app code:** a landing page with one positioning and a waitlist, in
   one market from `project.toml [product] regions`, plus the first build-in-public posts.
   - The go or stop number and its read date: **Founder decides**, written as an experiment in
     `docs/EXPERIMENTS.md` before the page goes live.
2. **Prototype the one core feature.** Measure the real cost per use (AI calls, storage) and
   fill in the unit economics table in section 5.
3. **Build** through the feature track in `AGENTS.md`: spec, readiness gate, build, QA,
   security, and the legal launch review. Analytics and consent are designed into each feature,
   not added after.
4. **Launch in one market.** Read each channel experiment on its date.
5. **Add the next market** only after the first passes.

## 2. The free tier is strict

A free tier with no hard limits is an open tab on your AI and hosting bill, run up by anyone
who finds it, including scripts. This template treats free-tier limits as requirements, not as
a later optimisation.

- **Every free action that costs money is capped.** A per-user limit on each costly action
  (an AI call, a file processed, a message sent), per day or per month.
- **A trial without sign-up is capped harder**, per device and per network address, and gives
  less than a signed-in free account.
- **A global daily ceiling** on what the free tier may spend. When it is reached, the free tier
  pauses or degrades and paid users are unaffected. The founder is alerted.
- **No uncapped path.** No free endpoint calls an AI provider or another paid service without
  passing the cap check first. Security reviews this on every feature with a free path.
- **The limits are numbers the founder chose**, written as requirement rows, and each row is
  `T` (a test proves the cap holds) before the release gate opens (`skills/release/`).
- **Abuse is assumed.** Rate limits, bot protection on sign-up and the no-login trial, and
  alerts on unusual spend are part of the first version, not the second.

### Tiers of access

Match what each kind of user can trigger to what they have proven:

| Who | What they get |
|---|---|
| Anonymous visitor | Pre-computed or cached results for showcase inputs, plus a very small number of live actions behind a bot challenge, on the cheapest model that does the job, with a hard output limit. |
| Signed-in free user | A daily or monthly count of live actions on a low-cost model. |
| Paying user | The full product, still with a fair-use ceiling so one account cannot cost more than it pays. |

How the caps are counted:

- **Never identify an anonymous user by network address alone.** Many people share one address
  (mobile carriers, offices), so an address-only limit blocks real customers. Combine signals
  (a signed cookie, the address range, the connection's characteristics); `legal` checks that
  the combination is allowed under each region's privacy rules before it ships.
- **Mobile apps can prove they are the real app.** Where the product has a store app, the
  platforms' app attestation services (Apple App Attest, Google Play Integrity) let free-tier
  endpoints accept calls only from the genuine app, alongside or instead of a bot challenge.
- **Reserve before the call, give it back on failure.** The cost of an action is counted before
  the paid service is called, and returned automatically if the call fails, so a provider error
  never eats a user's allowance or turns into a support ticket.
- **New paying users may ramp up.** Where a region gives a right of withdrawal or a refund
  window, a founder may choose a lower allowance during that window so the window cannot be
  used to run up costs and then refund. This is an option, with the wording checked by `legal`.

Behind all three:

- **A provider-side spending limit** as the last line of defence, where the AI provider offers
  one, set below what the founder can afford to lose in a day.
- **A fallback provider** for outages, chosen with the same data terms as the main one.

Limits, models and the fair-use ceiling: **Founder decides**, with the cost per action from the
prototype in front of them.

## 3. Organic channels

Each channel is an experiment with a prediction, a "wrong if" and a read date, written before
any work starts (`skills/experiment/`). A channel that misses its number is dropped or changed,
not kept out of hope.

### 3.1 Useful tools that people search for

Small working tools (a calculator, a checker, a generator) that answer one specific question the
target customer searches for, free and without sign-up, each leading into the product.

- **Prefer working tools to text pages.** A page made from a template with only the keyword
  swapped is what search engines' spam policies target; the growth agent reads the current
  guidance, cites it and dates it, before the first batch.
- **A quality gate for any page made in bulk:** it publishes only if it does something useful
  on its own and carries content that is not on any other page. The founder sets the bar.
- **Structured data** describing the product and its answers, following the search engines'
  own documentation.
- **AI answer engines** (chat assistants that search the web) are a second audience for the
  same pages. Conventions aimed at them, such as an `llms.txt` file, are proposals rather than
  standards, so any work on them is an experiment with its own read date.
- Each tool page has a clear next step into the product: save this, repeat it weekly, go deeper.
- Prediction, wrong if, read date: **Founder decides**.

### 3.2 Sharing that comes from the product

Sharing built on the product's own output (a result, a streak, a report) with a link back.

- **One tap to share:** a read-only public page for the output and a preview image sized for the
  platforms the audience uses, with a small, honest "made with" link.
- **Shared pages expose nothing private:** the user sees exactly what will be public before it
  is.
- **Shared pages can be abused** to host spam or phishing on the product's domain. Content is
  checked before a page is public, outbound links are stripped or marked, and pages are kept out
  of search indexes until they pass a quality bar the founder sets.

- Referral tracking and analytics need consent per region (`docs/legal/regions/`).
- Any reward for inviting others is checked by the legal agent against consumer law and the
  rules of any app store the product is in, before it ships.
- Prediction, wrong if, read date: **Founder decides**.

### 3.3 Building in public

A public log of the build, on the networks and communities where the target customer already
is, to find the first users and early feedback.

- No testimonials, user counts or trust badges until there are real users to quote, with their
  permission.
- Prediction (for example, waitlist sign-ups by a date), wrong if, read date: **Founder decides**.

### 3.4 A new domain starts from nothing

A brand-new website gets little search traffic at first, however good its pages are. Early
reach comes from elsewhere:

- **Useful open-source pieces**, such as the calculation behind a free tool, published with a
  link back, when the founder is happy to share that code.
- **Listings** on product directories and launch sites that fit the product, submitted by the
  founder (`social-media` drafts, the founder posts).
- **Genuine answers in communities** where the customer asks for help: each community's rules
  read first, the founder's connection to the product disclosed, and a link only where it
  answers the question. Posting to manipulate search results or AI answers is not done.

Each of these is an experiment with its own number and read date.

### 3.5 App stores, if the product is in one

Search inside an app store works differently from web search. Listing text, screenshots and
ratings are set per store and per language. Ask for a rating only after a success (a saved or
shared result), never during onboarding or after an error, and within each store's rules for
review prompts.

Two store rules shape the product itself, so read the current guidelines (cited and dated) before
designing a store app: an app that only wraps a website risks rejection for too little native
function, and linking to an outside payment page is restricted, with rules that differ by region.

## 4. Conversion

- **Onboarding:** the user reaches the product's core result before being asked to sign up,
  within the strict limits of section 2. Saving, exporting or doing more is what asks for
  sign-in, and whatever the user made before signing in moves into their new account.
- **Measure the funnel** (landing, first result, sign-up, payment) from the first version, and
  work on the step that loses the most people.
- **Web to app without starting over.** When a free web tool leads into an app, what the user did
  on the web is waiting in the app after install (through a sign-in link, or a deferred deep link
  where the platform supports it), so nobody re-enters what they already gave.
- **The paywall is an experiment too:** where it appears, what it says and which plan it shows
  first are each tested with a prediction and a read date, never changed on a hunch, and never
  with pressure tactics (`agents/product-designer.md`, no dark patterns).
- **Sign-in:** the fewest options the audience needs; one-tap providers where they fit.
- **Pricing:** anchored to what the problem costs the customer today. Free and paid tiers shown
  plainly; cancelling is as easy as subscribing; no renewal traps. Price: **Founder decides**.
- **Prices** shown in the customer's currency, including tax where the market requires it.
  Discounts with deadlines only when the deadline is real; `legal` checks the wording.
- **Data:** say plainly which data goes to an AI provider or another service, and which never
  leaves the device. Promise no encryption a feature cannot keep.
- **Analytics and cookies:** whether a consent banner is needed depends on what is stored on the
  device and on each region's rules, not on an analytics vendor's marketing. `legal` decides per
  region from the packs.

## 4a. Keeping customers

Getting a user is wasted if they leave in the second month. Keep them with value, never with
traps:

- **The product gets more useful with use:** saved history, templates, settings and progress
  that a fresh chat with a general AI would not have.
- **Their data is always theirs:** export is one click at any time. Value built up is a reason
  to stay, not a lock.
- **Annual plans** may be offered alongside monthly. Whether the annual plan may be shown
  pre-selected, and how its saving is worded, is checked by `legal` per region.
- **Cancelling stays as easy as subscribing.** Offering a pause or a discount on the way out is
  allowed only if cancelling remains one clear, quick path; `legal` checks the flow against each
  region's rules.
- **Churn is measured from the first paying user** and read monthly, with retention ideas run as
  experiments.

## 5. Payments, tax and data

Decide these before building checkout, with `legal`, and with an accountant where tax is
involved:

- **Who sells to the customer.** Either the founder's own company, using a payment processor and
  handling sales tax in each market, or a merchant of record that sells on the founder's behalf
  and takes on the tax filings, for a higher fee. Compare both with fees and terms read from each
  provider's own pages, dated, and with what the founder's accountant says.
- **App store billing**, if the product sells inside a store, follows that store's rules and fees.
- **Where data lives:** the database region chosen for the users' regions; personal data sent to
  an AI provider only under terms that say whether it is retained or used for training (zero
  retention where the provider offers it); personal details stripped from prompts where the
  feature works without them. Cross-border transfers go to `legal`, which escalates them.
- **AI transparency:** where a region requires telling users they are dealing with AI, or
  marking AI-generated content (including machine-readable marking in exports), the region pack
  says so with its source and the date it applies from; `legal` grades it per feature.
- **Self-serve from day one:** deleting an account and its data, exporting data, and getting
  invoices are buttons, not emails to the founder.

## 6. Risks to plan for from day one

| Risk | What it looks like | Mitigation |
|---|---|---|
| Spend attack on the free tier | Scripts hammer the no-login trial overnight. | Section 2: caps, bot challenge, global ceiling, provider-side limit, alerts. |
| AI provider outage | The main provider fails during a launch. | A fallback provider with the same data terms, tested before launch. |
| Support overload | Many billing and invoice questions at once. | A self-serve billing portal; help pages written as features ship. |
| Search penalty | Bulk pages judged thin. | The quality gate in 3.1; publish in small batches and read the results. |
| Share page abuse | Spam or phishing hosted on the product's shared pages. | Section 3.2: check before public, strip links, keep out of search until it passes. |
| Refund window abuse | Heavy use right after buying, then a refund. | The optional ramp for new paying users in section 2, with `legal` wording. |
| Real users blocked | A limit keyed on network address blocks everyone behind one carrier. | Combine signals, never address alone (section 2). |

## 7. Unit economics

Every value has a source and a date, or is measured, or stays blank. The gross margin target is a
founder decision checked against this table, never a claim.

| Per paying user per month | Value | Source |
|---|---|---|
| Price | | founder decision |
| minus app store commission, if the product is in a store | | the store's official page, dated |
| minus payment processing fees | | the processor's pricing page, dated |
| minus VAT or sales tax | | per market, sourced |
| minus cost of the paying user's own usage | | measured in the prototype; count savings from prompt caching or batching only once measured, since caches belong to one provider and expire |
| minus cost of free users, per paying user | | measured, divided by the conversion rate |
| **= net per paying user** | | |

| Fixed per month | Value | Source |
|---|---|---|
| Hosting and database | | provider pricing pages, dated |
| Domain, email, other tools | | |
| The founder's own AI subscriptions | | |
| **= fixed costs** | | |

**Break-even paying users = fixed costs / net per paying user.**

### Stress test

Run the table at several traffic levels. Every rate in it is an assumption until the project
measures it, and sits in `docs/ASSUMPTIONS.md` until then.

| Monthly visitors | Visitor to free user rate | Free to paid rate | Paying users | Revenue after fees and tax | Variable cost (paid and free usage) | Fixed cost | Profit |
|---|---|---|---|---|---|---|---|
| | assumed, then measured | assumed, then measured | | | | | |

## 8. Questions this playbook leaves to the founder

The product, the customer, the first market, the platform, the price, the free-tier limits and
models, who sells to the customer (own company or merchant of record), the data region, and
every experiment's numbers. The setup interview and the new-feature grilling ask them; the
answers go in `project.toml`, the requirement rows and `docs/requirements/p1-closed-decisions.md`.
