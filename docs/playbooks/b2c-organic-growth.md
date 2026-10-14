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

Limits: **Founder decides**, with the cost per action from the prototype in front of them.

## 3. Organic channels

Each channel is an experiment with a prediction, a "wrong if" and a read date, written before
any work starts (`skills/experiment/`). A channel that misses its number is dropped or changed,
not kept out of hope.

### 3.1 Useful pages that people search for

Free calculators, templates or small tools answering a specific question the target customer
searches for, each leading into the product.

- Every page must be useful on its own. Mass-produced thin pages can be treated as spam by
  search engines; the growth agent reads the current search engine guidance, cites it and
  dates it, before the first batch.
- Prediction, wrong if, read date: **Founder decides**.

### 3.2 Sharing that comes from the product

Sharing built on the product's own output (a result, a streak, a report) with a link back.

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

## 4. Conversion

- **Onboarding:** the user reaches the product's core result before being asked to sign up,
  within the strict limits of section 2.
- **Sign-in:** the fewest options the audience needs; one-tap providers where they fit.
- **Pricing:** anchored to what the problem costs the customer today. Free and paid tiers shown
  plainly; cancelling is as easy as subscribing; no renewal traps. Price: **Founder decides**.
- **Data:** say plainly which data goes to an AI provider or another service, and which never
  leaves the device. Promise no encryption a feature cannot keep.

## 5. Unit economics

Every value has a source and a date, or is measured, or stays blank. The gross margin target is a
founder decision checked against this table, never a claim.

| Per paying user per month | Value | Source |
|---|---|---|
| Price | | founder decision |
| minus app store commission, if the product is in a store | | the store's official page, dated |
| minus payment processing fees | | the processor's pricing page, dated |
| minus VAT or sales tax | | per market, sourced |
| minus cost of the paying user's own usage | | measured in the prototype |
| minus cost of free users, per paying user | | measured, divided by the conversion rate |
| **= net per paying user** | | |

| Fixed per month | Value | Source |
|---|---|---|
| Hosting and database | | provider pricing pages, dated |
| Domain, email, other tools | | |
| The founder's own AI subscriptions | | |
| **= fixed costs** | | |

**Break-even paying users = fixed costs / net per paying user.**

## 6. Questions this playbook leaves to the founder

The product, the customer, the first market, the platform, the price, the free-tier limits and
every experiment's numbers. The setup interview and the new-feature grilling ask them; the
answers go in `project.toml`, the requirement rows and `docs/requirements/p1-closed-decisions.md`.
