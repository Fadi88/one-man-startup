# Prompt

Paste everything below the line into an AI coding tool opened in a fresh copy of the template.
The person or agent playing the founder answers from `founder.md`.

---

Run the setup interview for this project, exactly as `skills/setup/SKILL.md` and
`agents/setup.md` describe it, following `AGENTS.md`.

This is a dry run with a scripted founder. Whoever answers for the founder uses only
`examples/setup-dry-run/founder.md`, and answers in the first person, as the founder would
speak. The setup agent never uses anything from that file the founder has not said yet: not
in a question, not in a recommendation. As the setup agent:

1. Ask in rounds, as `skills/grilling/SKILL.md` describes: number the questions, give a
   recommended answer with a one-line reason for each, and wait for the answers before the next
   round. Look up facts yourself; ask the founder only for decisions.
2. Keep a transcript in `examples/setup-dry-run/transcript.md`: each round's questions with your
   recommendations, then the founder's answers, word for word.
3. When the frontier is empty, write everything `skills/setup/SKILL.md` lists: `project.toml`,
   the region packs, closed decisions, open questions, rejected proposals, and the requirement
   rows the answers imply.
4. Run `python tools/sync_adapters.py` and `python tools/run_all.py`, and fix anything you broke.
5. Show the summary and stop. Do not commit, push, deploy or contact anyone, and do not read
   anything outside this copy of the template (no global git settings, no home folder).
