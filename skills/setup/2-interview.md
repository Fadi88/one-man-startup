# Setup step 2: the interview

Part of `skills/setup/SKILL.md`.

Ask as few rounds as the dependencies allow; a non-technical founder should not face 25
questions. Combine branches whose prerequisites are settled, and defer anything not needed
before the first feature to `p1-open-questions.md`.

1. **Founder:** name and email for commits; their technical level, asked as `skills/founder-voice/`
   words it (non-technical, basics or technical). It sets how every agent talks to them.
2. **Product:** name, one sentence, stage (idea, prototype, beta, live).
3. **Market** (unlocked by 2):
   - regions (ISO codes, where users live, not where the founder lives);
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
   release to users.
8. **Budget:** monthly AI spend ceiling for the optimizer to report against.
9. **Tools:** which AI coding tools the founder uses (adapters are generated for each). Always
   include the tool running this setup, or its generated files are removed by the sync.
10. **Licence** (unlocked by 2 and 5): who may use, copy or sell the product's code. Explain the
    options and what each means for the business from `skills/setup/licences.md`, at the
    founder's level, and recommend one. Say it is not legal advice, and that `legal` can look
    at it before launch.
