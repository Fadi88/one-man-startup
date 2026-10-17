# Setup step 2: the interview

Part of `skills/setup/SKILL.md`.

Ask as few rounds as the dependencies allow; a non-technical founder should not face 25
questions. Combine branches whose prerequisites are settled, and defer anything not needed
before the first feature to `p1-open-questions.md`.

1. **Founder:** name and email for commits; their technical level, asked as `skills/founder-voice/`
   words it (non-technical, basics or technical). It sets how every agent talks to them.
2. **Product:** name, one sentence, stage (idea, prototype, beta, live), and origin: a new idea,
   or a generic version of an app that already exists ("rebuild"). For a rebuild, ask which app
   and its public site (`based_on`), and say what changes: `researcher` maps that app's features
   first and the founder cuts them to a first version, and `legal` checks that nothing of the
   original's own is copied (name, logo, images, text, code).
   If it is the founder's own existing app ("own"; `based_on` is its folder or repository),
   ask which way, with a recommendation:
   - **copy:** keep its code and carry on here; run `skills/spec-audit/` on it (step 5);
   - **rebuild:** start the code fresh and use the old app only as a reference;
   - **borrow:** start fresh, but mine the old app's requirements: one
     `docs/work/<id>/candidates-<screen>.md` per screen, each candidate quoting where in the old
     app it came from, put to the founder in the first grilling as options.
3. **Market** (unlocked by 2):
   - regions (ISO codes, where users live, not where the founder lives). A group (MENA, the
     EU, the Gulf) is asked as its list of countries: each country is its own pack and its own
     legal check, so recommend starting with the few where the first users are;
   - domain;
   - audience in a sentence;
   - customer size: consumers, small business, mid-market, enterprise.
4. **Data** (unlocked by 2, and asked with 3 in one round): what personal data, payments,
   health, children, biometrics, AI decisions about people. Each one becomes a `sensitive`
   entry and switches on gates.
5. **Stack** (unlocked by 2 and 4): platform, frontend, backend, database, hosting, the test and
   build commands ("none yet" when no code exists). Recommend what the founder already knows,
   hosted, boring. If a codebase exists, read it and propose what it already is. Run
   `skills/spec-audit/` on it, and put its most dangerous silent fills into the next round.
6. **Gates:** recommend **strict** and say what it buys, using the table in `skills/gates/`,
   never your own description of a level. If the founder picks lighter, ask for the reason and
   record it.
7. **Team** (unlocked by 2, 4 and 6): the smallest set of agents the stage needs. Recommend, say
   what each one does and when it is first needed, let the founder trim. Time per feature is not
   measured yet, so do not quote one. If the product calls AI or another paid service per
   action, recommend `dashboard` from the start: usage, spend and caps need a place to be seen
   and controlled before the first user arrives. Recommend `android-dev`, `ios-dev` and
   `desktop-dev` only for the apps the stack's platform includes, `agentic-workflow` if the
   product's AI acts or decides for users, and `rollback` and `debugger` before the first
   release to users. `platform-architect`, `platform-designer` and `explainer-writer` are
   optional: off unless one platform's app is large, or the product teaches ideas in video.
8. **Budget:** what the founder can spend each month on the AI tools building the product (their
   Claude, ChatGPT or Cursor plan, and any API use by the agents), for the optimizer to report
   against. Say plainly that this is not about AI inside the product: that cost is measured per
   feature by `feasibility` and capped by the free-tier rows when there is a free tier.
9. **Tools:** which AI coding tools the founder uses (adapters are generated for each). Always
   include the tool running this setup, or its generated files are removed by the sync.
10. **Licence** (unlocked by 2 and 5): who may use, copy or sell the product's code. Explain the
    options and what each means for the business from `skills/setup/licences.md`, at the
    founder's level, and recommend one. Say it is not legal advice, and that `legal` can look
    at it before launch.
