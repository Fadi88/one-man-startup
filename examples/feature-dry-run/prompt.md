# Prompt

Paste everything below the line into an AI coding tool opened in a set-up copy of the template
(see `README.md`, "Running it"). The person or agent playing the founder answers from
`dry-run/founder.md` in that copy.

---

This project is set up: `project.toml` is filled in and setup's decisions are in
`docs/requirements/`. Act as the project manager, exactly as `AGENTS.md` and
`agents/orchestrator.md` describe, and take the founder's request below through the feature
track (`skills/new-feature/`).

The founder's message: "I'd like the first real thing now: I take a photo of a receipt and the
app puts it in the right spending category for me."

This is a dry run with a scripted founder. Whoever answers for the founder uses only
`dry-run/founder.md`, answers only what is asked, in the first person, and never volunteers a
line from it. No agent uses anything from that file the founder has not said yet: not in a
question, not in a recommendation, not in a document.

1. Each time you take a role (researcher, feasibility, agentic-workflow, architect,
   product-designer, legal, security, reviewer, a developer, qa), read that agent's file in
   `agents/` and the skills it lists before doing its work, and write its artifact where its
   file says. If the tool can start a separate agent, you may; give it a brief as
   `skills/handoff/` describes.
2. Keep a transcript in `dry-run/transcript.md`: every message to the founder and every answer,
   word for word; each hand-off brief; and one line each time a role starts or ends, naming the
   files it opened.
3. Go through research, grilling, feasibility, the spec and its rows, the spec review, the
   founder's confirmation, the readiness gate, the agentic design, the architect's design,
   contract and tickets, the user experience design with its rendered screens, legal and
   security on the design, and the design review.
4. Then build one small ticket, test first, as its developer; review the diff as `reviewer`;
   and write the QA report as `qa`.
5. Real web research is fine where an agent's file calls for it; keep it brief. Never sign up,
   publish, push, deploy, send, pay or call a paid service. Never commit without the founder's
   go. Do not read anything outside this copy.
6. End with `python tools/run_all.py` green, and show the founder a summary at their level:
   what was decided, what was built, what is open and what they must do next.
