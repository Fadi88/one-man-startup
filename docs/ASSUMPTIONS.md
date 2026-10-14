# Assumptions

Things this project relies on that are not confirmed yet. Each one says how it will be confirmed
and by when, and is labelled where it is used (`skills/verified-claims/SKILL.md`). The sweep
fails when an open assumption passes its confirm-by date.

Status is `open`, `confirmed` or `disproved`. A confirmed or disproved entry keeps its row, with
what settled it in the last column.

| ID | Assumption | Used in | How to confirm | Confirm by | Status | Settled by |
|---|---|---|---|---|---|---|
| A-1 | The setup interview runs end to end, writes `project.toml`, the region packs and the first decisions, and leaves the sweep green. | TPL-14, README | Run setup for a made-up company and keep the transcript. | 2026-10-31 | confirmed | Scripted dry run in Claude Code, 2026-10-14: `examples/setup-dry-run/results/2026-10-14-claude-code.md`. |
| A-2 | Claude Code loads the generated `.claude/agents/` and `.claude/skills/` files, including the `tools`, `model` and `skills` fields. | TPL-15, `docs/HOW-IT-WORKS.md` | Open the repo in Claude Code and list the agents and skills. | 2026-10-31 | open | |
| A-3 | Codex reads `AGENTS.md` as the project's instructions. | TPL-15, README | Open the repo in Codex and ask what the constitution says. | 2026-10-31 | open | |
| A-4 | Gemini CLI follows the `@AGENTS.md` import in `GEMINI.md`. | TPL-15, README | Open the repo in Gemini CLI and ask what the constitution says. | 2026-10-31 | open | |
| A-5 | Cursor picks up `.cursor/rules/*.mdc` with `alwaysApply: false` as rules the agent can request by description. | TPL-15, README | Open the repo in Cursor and check the rules list. | 2026-10-31 | open | |
| A-6 | GitHub shows the diagrams in `docs/images/` in the viewer's light or dark theme. | README | Push and view the README on github.com in both themes. | 2026-10-31 | open | |
| A-7 | A real non-technical founder can finish setup without outside help, in a length they find acceptable. | README | Run setup with a real person who does not code; note where they got stuck and how long it took. | 2026-11-15 | open | |
