# Transcript: setup dry run, 2026-10-14

Setup agent run from `prompt.md`; the founder's answers come from `founder.md` and are copied
here word for word. Facts the setup agent looked up itself are noted before each round.

## Round 1: founder, product, gates, budget, tools

Looked up before asking: `project.toml` is the untouched template (every `[owner]`, `[product]`
and `[stack]` field `unset`). The repository's own git identity is `Template Baseline
<baseline@example.com>`, a placeholder from the template copy, so it cannot be your identity
and is not proposed. No application code exists in the repository, so there is no stack to
read off it.

1. **Your name and email for commits.** Every commit in this project is made in your name, with
   no AI tool credited. What name and email should commits carry?
   Recommended: the name and email you use on GitHub. Reason: commits then link to your account
   and the commit hook can check the author.
2. **How much should the agents explain?** Options: non-technical (plain words, every choice
   explained as cost, risk and benefit) or technical (brief, show the diff).
   Recommended: non-technical. Reason: it costs a few more lines per answer and nothing is
   decided on jargon you did not follow; you can switch later.
3. **The product.** What is it called, and what does it do, in one sentence a customer would
   understand?
   Recommended: a working name is fine; it can change before launch. Reason: agents need a name
   and a one-liner to write anything; neither is final.
4. **Stage.** Options: idea (nothing built), prototype (something runs, nobody uses it), beta
   (some real users), live (paying or public).
   Recommended: idea, unless something already runs. Reason: the stage sets how much process
   the first features get.
5. **Gates.** Options: strict, standard, light.
   Recommended: strict. Reason: it buys a numbered requirement before any code, a green test
   sweep before every hand-off, a commit hook that refuses bad commits, and nothing outward
   (deploy, publish, pay, send) without your go; the cost is a few minutes per change.
6. **Monthly AI budget.** The ceiling in US dollars a month for the AI tools that run this team;
   the optimizer agent reports against it and warns before it is reached.
   Recommended: set a number now, even a rough one. Reason: with no ceiling there is nothing to
   warn against, and AI tool bills grow quietly.
7. **Which AI coding tools do you use?** Options: Claude Code, Codex, Gemini CLI, Cursor
   (instruction files are generated for each one you pick).
   Recommended: only the ones you actually use. Reason: fewer generated files to keep in step.

### Founder's answers, round 1

1. Nadia Example. Email: nadia@example.com.
2. Not technical.
3. Receipt Buddy. "Snap a photo of a receipt and it sorts your household spending for you, so you
   can see where the money goes each month."
4. Idea.
5. "Can we go lighter? I want to move fast, it's just an idea."
6. "About 100 dollars a month for the AI stuff."
7. "I'm using Claude Code."

## Round 2: gates again, and the market

Settled in round 1: Nadia Example <nadia@example.com>, not technical, Receipt Buddy at the idea
stage, US$100 a month AI budget, Claude Code only. Pushed back on: gates.

1. **Gates, asked again.** You asked to go lighter. Here is what each level means for you:
   - *strict*: every change starts as a numbered requirement, the full test sweep must pass
     before any hand-off, a commit hook refuses bad commits, and nothing outward (deploy,
     publish, pay, send) happens without your go. Cost: a few extra minutes per change.
   - *standard*: the same outward stops and the same sweep, with lighter paperwork on small
     changes. What could go wrong: small changes slip in without a requirement, and those are
     the ones that are hard to trace later.
   - *light*: speed first, few checks. What could go wrong: on a product that will hold
     people's spending data and take payments, mistakes reach users before anyone sees them.
   Recommended: strict. Reason: at the idea stage there is little code, so strict costs least
   now and is hardest to add later. If you still want lighter, which level, and what is the
   reason I should record?
2. **Regions.** Which countries will your users live in (where they live, not where you do)?
   Recommended: start with one or two countries you can reach yourself. Reason: each country
   adds its own privacy, consumer and tax rules to check before launch.
3. **Domain.** Receipt Buddy reads people's receipts and shows their spending, which puts it in
   consumer personal finance.
   Recommended: record the domain as "personal finance". Reason: it is what the product does,
   and it tells the legal and security agents to treat money data with extra care.
4. **Audience.** Who is it for, in one sentence?
   Recommended: a specific group rather than "everyone". Reason: the design, the wording and
   where we find the first users all follow from it.
5. **Customer size.** Options: consumers (people paying for themselves), small business,
   mid-market, enterprise.
   Recommended: consumers. Reason: a household spending app is bought by individuals; that means
   self-serve sign-up, app store rules and refunds rather than sales contracts.

### Founder's answers, round 2

1. "Fine, standard then, not light. I'll go strict before real users."
2. The UAE and Germany. "I live in Dubai and my sister in Berlin wants it too."
3. I don't know, what do you recommend?
4. "Busy expat families who never get round to tracking spending."
5. Consumers.

Noted from round 2: gates settle on standard, with your reason recorded ("I'll go strict before
real users"). Question 3 had no answer of your own, so the recommendation stands: the domain is
"personal finance". While you answer round 3, I am looking up the privacy, consumer and tax
rules for the UAE and Germany myself; nothing below asks you for them.

## Round 3: the data

1. **Personal data.** What will the app keep about each user?
   Recommended: only the receipt photo, what is printed on it (amounts, shop names, dates) and
   the user's email for sign-in. Reason: every extra field is something more to protect and
   explain in the privacy notice.
2. **Payments.** Will people pay, and will there be a free version?
   Recommended: a paid plan, and if there is a free version, one with firm limits on use.
   Reason: each receipt the AI reads costs you money, so a free version with no limits lets
   anyone, including automated scripts, run up your AI bill.
3. **Sensitive data.** Will the app hold children's data, health data or biometrics (face or
   fingerprint data)?
   Recommended: none of them; adults only (18 and over). Reason: each one adds its own legal
   rules and reviews; your product needs none of them.
4. **Is money data sensitive?** Receipts and spending show how a household lives.
   Recommended: yes, record it as sensitive financial data. Reason: a leak would hurt users,
   and marking it sensitive makes the legal and security agents review every feature that
   touches it.
5. **What the AI does.** What will the AI decide?
   Recommended: it reads the receipt and suggests a spending category the user can change; it
   never decides anything about a person (no credit scores, no approvals). Reason: decisions
   about people bring heavy legal duties in both countries; sorting receipts does not.
6. **Keeping receipt photos.** Should the app keep the photo after the AI has read it?
   Recommended: delete the photo once the figures are read and the user has checked them, keep
   the figures until the user deletes their account. Reason: the photo is the riskiest thing to
   store (it can show card digits and what was bought), and the figures are what the app needs.

### Founder's answers, round 3

1. "Receipt photos, the amounts and shop names on them, the user's email."
2. "Payments: yes, a paid plan. Maybe a free version too, I'm not sure."
3. "No children's data, no health data."
4. "It's money, so I guess that's sensitive?"
5. "The AI reads the receipt photo and picks the category."
6. I don't know, what do you recommend?

Noted from round 3: data is receipt photos, the amounts and shop names on them, and the email;
money data is recorded as sensitive (your question 4 read as a yes to my recommendation; say if
not). Question 6 had no answer of your own, so the recommendation stands: the photo is deleted
once read and checked, the figures are kept until the account is deleted. Two of your answers
left a gap, asked again below (questions 1 and 2).

Looked up before this round, each from the provider's own page, checked 2026-10-14:
- Vercel (website hosting): Hobby is free but "for personal, non-commercial use"; taking
  payments counts as commercial, so a paid app needs Pro at US$20 a month
  (https://vercel.com/pricing, https://vercel.com/docs/limits/fair-use-guidelines).
- Supabase (database, sign-in and file storage): Free plan with 500 MB database, 1 GB files,
  50,000 monthly users, paused after a week unused; Pro from US$25 a month. It has a Frankfurt
  region and no region in the UAE or the Middle East (https://supabase.com/pricing,
  https://supabase.com/docs/guides/platform/regions).
- Anthropic (the AI that reads receipts) supports images; its Haiku 5.5 model is listed at
  US$0.10 per million input tokens and US$0.50 per million output tokens; processing runs
  either anywhere ("global") or in the US only, with no EU or Middle East option
  (https://claude.com/pricing, https://platform.claude.com/docs/en/build-with-claude/vision,
  https://platform.claude.com/docs/en/manage-claude/data-residency).
- Stripe supports businesses in both the UAE and Germany (https://stripe.com/global). Paddle
  sells as the "merchant of record" (it is the seller in law and handles sales tax) at "5% + 50
  cents per Checkout transaction" (https://www.paddle.com/pricing).

## Round 4: the gaps, the free version, the stack, payments and the team

1. **Biometrics and age.** You said no children's or health data; biometrics (face or
   fingerprint data) and the minimum age were not answered.
   Recommended: no biometrics, and the app is for adults (18 and over). Reason: both keep the
   product out of the strictest rules in both countries.
2. **Can people change the category?** You said the AI picks the category.
   Recommended: the AI suggests and the user can always change it. Reason: the AI will
   sometimes be wrong, and a user who cannot fix it stops trusting the totals.
3. **The free version.** You are not sure about one. Every receipt the AI reads costs you
   money, so a free version must have limits; a free version without limits is not offered.
   Recommended: plan for a free version with three hard limits: a number of receipts per
   signed-in user, a smaller number for anyone trying it without signing up, and a daily
   ceiling on what all free use together may cost you, after which the free version pauses
   until the next day. The numbers stay open until the prototype has measured what one receipt
   costs. Reason: the limits are written as requirements now, so nothing free is built without
   them; the numbers come from a measurement, not a guess.
4. **The stack (what it is built with and where it runs).**
   Recommended: a web app that works in the phone's browser and can be added to the home
   screen, built with Next.js, with Supabase for the database, sign-in and photo storage in its
   Frankfurt region, hosted on Vercel, the receipts read by Anthropic's API, and automatic
   tests with Vitest and Playwright. Starting cost: US$0 while it is a prototype nobody pays
   for; once it takes payments, Vercel Pro at US$20 a month, plus Supabase Pro at US$25 a month
   when the free plan is outgrown, plus AI use per receipt. Reason: it is all hosted and widely
   used, so the agents build it well and nothing needs a server you look after; a web app
   avoids app store review and store fees to start.
5. **How you get paid.** Options: through your own company with Stripe (you handle sales tax
   in each country) or through a merchant of record such as Paddle (it handles sales tax, for
   a higher fee).
   Recommended: decide this later, with the legal agent and an accountant, before the payment
   feature is built. Reason: the right answer depends on your company and where you sell; it
   does not block the prototype.
6. **The team (which AI agents are switched on).**
   Recommended: orchestrator, setup, architect, designer, frontend-dev, backend-dev, qa,
   security, legal, growth, social-media and optimizer; leave devops off until the first
   deploy. What each costs in time per feature is not measured yet: each one adds a step on the
   features in its area, and the optimizer will report the real figures after the first
   features. Reason: security and legal are needed because the app holds money data and takes
   payments; growth and social-media because a consumer app is found through content; the
   optimizer watches your US$100 a month.

### Founder's answers, round 4

1. I don't know, what do you recommend?
2. I don't know, what do you recommend?
3. "I don't know the costs yet. Do what you recommend and I'll set the numbers when we know
   them."
4. "No idea. Whatever is simplest and cheap to start."
5. I don't know, what do you recommend?
6. "I don't need the social media one yet, I'll do that myself later."

Noted from round 4: questions 1, 2 and 5 had no answer of your own, so the recommendations
stand (no biometrics, adults only; the user can change the category; the payment route is
decided later with legal and an accountant). Question 4 is read as accepting the recommended
stack. Social media is left off the team, as you asked, and recorded as turned down for now.

## Round 5: confirm the summary before anything is written

The frontier is empty. This is what I will write; nothing is written until you confirm it.

- **You:** Nadia Example <nadia@example.com>, not technical. Commits in your name only.
- **Product:** Receipt Buddy. "Snap a photo of a receipt and it sorts your household spending
  for you, so you can see where the money goes each month." Stage: idea.
- **Market:** users in the UAE (AE) and Germany (DE); domain personal finance; audience "Busy
  expat families who never get round to tracking spending"; consumers.
- **Data:** receipt photos, the amounts and shop names on them, email. Sensitive: financial
  data and payments. No children (adults only), no health data, no biometrics. The AI reads
  the photo and suggests a category the user can change; it decides nothing about a person.
  The photo is deleted once read and checked; the figures are kept until the account is
  deleted.
- **Free version:** if offered, three hard limits (per signed-in user, tighter without sign-up,
  a daily ceiling on all free use), written as requirements now, numbers set by you once the
  prototype has measured the cost of one receipt.
- **Stack:** web app for phone browsers; Next.js, Supabase (Frankfurt), Vercel, Anthropic's API
  for reading receipts, Vitest and Playwright for tests.
- **Gates:** standard, with your reason "I'll go strict before real users".
- **Team:** orchestrator, setup, architect, designer, frontend-dev, backend-dev, qa, security,
  legal, growth, optimizer. Not social-media (you will do it yourself for now), not devops
  (added at the first deploy).
- **Budget:** US$100 a month for AI. **Tools:** Claude Code.
- **Open, for later:** how you get paid (own company with Stripe, or Paddle as merchant of
  record), decided with legal and an accountant before payments are built; the free version's
  numbers; and three questions for the legal agent that came out of my research: sending UAE
  and German users' receipts to an AI provider and a database outside their country, whether
  Germany requires you to name a representative in the EU, and which UAE rules are still
  waiting on official regulations.

1. **Is this what you meant?**
   Recommended: yes. Reason: every line above is one of your answers or a recommendation you
   accepted; anything wrong is cheaper to fix now than after it is written.

### Founder's answers, round 5

1. I don't know, what do you recommend?

Taken as accepting the recommendation: confirmed. Writing the outputs.

## Summary to the founder

Nadia, setup is done. Nothing has been committed, published or sent.

**Decided.** You are the author of every commit (Nadia Example, nadia@example.com), and the
agents will explain things in plain words. Receipt Buddy is at the idea stage, for busy expat
families in the UAE and Germany, sold to consumers, in personal finance. It keeps receipt
photos, the amounts and shop names on them, and the email; money data is treated as sensitive.
Adults only, no health data, no biometrics. The AI suggests a category the user can change and
decides nothing about a person. Photos are deleted once read and checked. It will be a web app
for phone browsers (Next.js, Supabase in Frankfurt, Vercel, Anthropic's API). Gates are
standard, with your reason recorded, and you said you will go strict before real users. The
team is eleven agents; social media is off until you want it, devops until the first deploy.
AI budget US$100 a month; Claude Code only. All of it is in `project.toml` and
`docs/requirements/p1-closed-decisions.md`; what you turned down is in `p1-rejected.md`.

**Open.** How you get paid (your own company with Stripe, or Paddle as merchant of record),
decided with the legal agent and an accountant before payments are built. The free version's
three limits, set once the prototype has measured the cost of one receipt. For the legal agent:
sending users' receipts to a database and an AI outside their country, whether Germany needs
you to name a representative in the EU, the UAE rules still waiting on official regulations,
and whether receipts can reveal sensitive details such as pharmacy purchases. Whether Vercel's
free plan may host the unpaid prototype (assumption A-7). All in `p1-open-questions.md` and
`docs/ASSUMPTIONS.md`.

**Next.** The legal agent reviews the two region packs (`docs/legal/regions/AE.md` and
`DE.md`; many UAE points rest on law firm summaries because the official site was unreachable).
Then the orchestrator starts the first feature, a prototype that reads one receipt and measures
what it costs, against the rows in `docs/requirements/LAUNCH.md` (15 rows, all marked X, not
built). The test sweep is green. Say the word and I will show you the changes to commit.
