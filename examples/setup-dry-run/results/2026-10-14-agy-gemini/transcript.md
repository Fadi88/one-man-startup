# Setup dry run transcript

This transcript documents the setup interview for Receipt Buddy conducted with founder Nadia Example on 14 October 2026. The interview follows the setup interview design tree from `skills/setup/SKILL.md` and the grilling process from `skills/grilling/SKILL.md`.

---

## Round 1

### Setup agent

1. **Founder identity and background**
   What is your name, preferred email address for repository commits, and your technical background?
   *Recommended answer:* Provide your full name, email address, and indicate "non-technical".
   *Reason:* Setting your background to non-technical ensures all agents explain decisions plainly without unexplained technical jargon.

2. **Product name, description, and stage**
   What is the name of your product, what is its one-sentence summary, and what is its current stage (idea, prototype, beta, or live)?
   *Recommended answer:* Name the product, describe its purpose in one sentence, and set stage to "idea".
   *Reason:* Setting stage to idea keeps process overhead low and focuses early work on validating the core concept before building unnecessary scaffolding.

### Founder

Name: Nadia Example. Email: nadia@example.com.
Not technical. Has used ChatGPT, never written code, has a GitHub account.

Name: Receipt Buddy.
One sentence: "Snap a photo of a receipt and it sorts your household spending for you, so you can see where the money goes each month."
Stage: idea.

---

## Round 2

### Setup agent

3. **Market regions, audience, and customer size**
   Which geographic regions will your users live in (please specify ISO country codes), who is the primary target audience in a sentence, and what is the customer segment size (consumers, small-business, mid-market, or enterprise)?
   *Recommended answer:* Target the United Arab Emirates (AE) and Germany (DE), define the audience around household budgeting, and set customer size to consumers.
   *Reason:* Selecting consumer self-serve avoids enterprise compliance requirements like single sign-on while matching household spending tracking needs.

4. **Data handling, sensitive data, payments, and AI scope**
   What personal information will the app collect and store, will there be paid plans or a free tier, is any collected data sensitive (such as financial, health, or children's data), and what exact role will AI perform?
   *Recommended answer:* Collect user emails and receipt data, classify financial records as sensitive data, support paid subscriptions, and limit AI strictly to reading receipt images and assigning categories.
   *Reason:* Financial records require strong encryption and explicit privacy disclosures, while scoping AI to receipt processing bounds operational and regulatory risk.

### Founder

Regions: the UAE and Germany. "I live in Dubai and my sister in Berlin wants it too."
Audience: "Busy expat families who never get round to tracking spending."
Customer size: consumers.

Receipt photos, the amounts and shop names on them, the user's email.
Payments: yes, a paid plan. "Maybe a free version too, I'm not sure."
No children's data, no health data. "It's money, so I guess that's sensitive?"
The AI reads the receipt photo and picks the category.

---

## Round 3

### Setup agent

5. **Technical stack**
   What platform, frontend, backend, database, and hosting architecture should we select for Receipt Buddy?
   *Recommended answer:* Web platform using Next.js for frontend and backend API routes, hosted on Cloudflare Pages, with PostgreSQL database on Supabase, and OpenAI gpt-4o-mini vision for receipt parsing, with test and build commands set to "none yet".
   *Reason:* This hosted architecture starts at $0 per month on free tiers (Supabase provides a 500 MB database; Cloudflare Pages permits commercial use on its free tier), keeping initial costs at zero while code is written.

6. **Repository quality gates**
   Which gate level should we enforce for this project: strict, standard, or light?
   *Recommended answer:* Strict.
   *Reason:* Strict gates require numbered requirement rows before writing code, mandate a clean test sweep on every hand-off, install commit hooks, and stop accidental spend or data corruption.

7. **Free tier usage limits**
   Since you mentioned potentially offering a free tier alongside a paid plan, how should we structure free tier limits?
   Options:
   - Strict caps: capped scans per registered user, tighter cap for guests without sign-up, and a global daily AI cost limit (with exact numbers set once cost per receipt scan is measured in prototype).
   - Paid plan only (or upfront paid trial).
   (Note: An uncapped free tier is prohibited by project policy to prevent runaway AI bills.)
   *Recommended answer:* Strict caps with per-user scan limits, a strict guest limit, and a daily circuit breaker.
   *Reason:* Strict caps protect your monthly AI budget against runaway script abuse while letting prospective users test the receipt scanner.

8. **Monthly AI budget ceiling**
   What monthly spend ceiling in USD should the optimizer agent monitor against for AI inference costs?
   *Recommended answer:* $100 per month.
   *Reason:* A $100 ceiling provides sufficient headroom for development and prototype verification while establishing a hard stop against accidental overruns.

9. **AI coding tools**
   Which AI coding tool do you use so we can generate the corresponding configuration files?
   *Recommended answer:* Claude Code.
   *Reason:* Targeting your active AI tool keeps repository configuration minimal and avoids maintaining unused tool adapters.

### Founder

Stack: "No idea. Whatever is simplest and cheap to start."

Gates: "Can we go lighter? I want to move fast, it's just an idea."

Free tier: "I don't know the costs yet. Do what you recommend and I'll set the numbers when we know them."

Budget: "About 100 dollars a month for the AI stuff."

Tools: "I'm using Claude Code."

---

## Round 4

### Setup agent

10. **Process gates compromise**
    In Round 3, you asked: "Can we go lighter? I want to move fast, it's just an idea." Strict gates require requirement rows before code, green test sweeps on hand-offs, and commit hooks that block broken commits. Light turns off these protections and risks regressions and corrupted data. Standard keeps requirement rows and green test sweeps on hand-offs, but skips the strict commit hook restrictions. Can we set gates to standard during this idea phase, and upgrade to strict before taking real users?
    *Recommended answer:* Standard for now, upgrading to strict before launching to real users.
    *Reason:* Standard gives you development speed while preserving requirement tracking and clean test runs to keep the codebase healthy.

11. **Agent team roster**
    Which AI agent roles should be enabled in `project.toml`?
    Available agents: orchestrator, setup, architect, designer, frontend-dev, backend-dev, qa, security, legal, devops, growth, social-media, optimizer.
    *Recommended answer:* Enable all 13 agents to cover the entire development and marketing lifecycle.
    *Reason:* Having the full team ready allows seamless hand-offs as the product moves from idea to architecture, implementation, legal checks, and social launch.

### Founder

Gates: "Fine, standard then, not light. I'll go strict before real users."

Team: "I don't need the social media one yet, I'll do that myself later."

---

## Round 5

### Setup agent

12. **Setup confirmation**
    Here is the complete summary of decisions for Receipt Buddy:
    - **Owner:** Nadia Example (nadia@example.com), level: non-technical.
    - **Product:** Receipt Buddy, idea stage. One-liner: "Snap a photo of a receipt and it sorts your household spending for you, so you can see where the money goes each month."
    - **Market:** Regions UAE (AE) and Germany (DE). Audience: "Busy expat families who never get round to tracking spending." Customer size: consumers. Domain: fintech.
    - **Data and sensitivity:** Financial transaction data and payments marked sensitive. Storing receipt photos, amounts, vendor names, and user emails. AI role limited to receipt OCR and expense categorization.
    - **Legal packs:** Created for UAE (`AE.md`) and Germany (`DE.md`). Flagged cross-border transfer of receipt data to third-country AI APIs for legal review.
    - **Stack:** Web platform, Next.js frontend and API routes, Cloudflare Pages hosting, Supabase PostgreSQL database, OpenAI gpt-4o-mini vision for receipt processing; test and build commands set to "none yet".
    - **Quality gates:** Standard (founder chose standard to move fast during idea stage, committing to strict before real users).
    - **Team:** 12 agents enabled (excluding social-media per founder decision).
    - **Budget:** $100 monthly AI spend ceiling.
    - **Tools:** Claude Code (`targets = ["claude"]`).
    - **Free tier:** Strict caps marked X in `LAUNCH.md` (per-user monthly scan cap, tighter per-device guest scan cap, global daily AI spend ceiling; numbers left open for founder to set once prototype costs are measured).
    - **Requirements:** Created `docs/requirements/LAUNCH.md` with requirement rows marked X for consumer, privacy, and free tier requirements.

    Do you confirm this setup summary?
    *Recommended answer:* Yes, that's what I meant.
    *Reason:* Confirms all settings before applying them and running the verification checks.

### Founder

"Yes, that's what I meant."
