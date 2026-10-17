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
| A-9 | On a fresh copy, Claude Code answers the first "hello" as the project manager, checks Git and Python, and starts setup without being asked. | TPL-26, `docs/START-HERE.md` | Start Claude Code on a fresh copy, say hello, keep a screenshot of the reply. | 2026-10-31 | confirmed | Claude Code 2.1.300 in a terminal, 2026-10-15: `docs/images/start/5-first-hello.png`. |
| A-10 | Claude's desktop app (Code tab) behaves the same as A-9 on a fresh copy. | `docs/START-HERE.md` | Follow the guide in the desktop app's Code tab instead of the terminal. | 2026-11-15 | open | |
| A-11 | GitHub's API answers 404 to a request without sign-in for a private repository, so `tools/repo_visibility.py` prints NOT PUBLIC for it. Measured 2026-10-17: this public repository answers, a missing one answers 404; a private one not yet tried. | TPL-39, `tools/repo_visibility.py` | Run the script in a copy made private, keep the output. | 2026-11-15 | confirmed | 2026-10-17: for the founder's own private repository `Fadi88/tracker_app` (`gh repo view` says PRIVATE), `visibility()` printed `NOT PUBLIC Fadi88/tracker_app`. |
| A-12 | In an interactive Claude Code session on a trusted folder, the hook generated into `.claude/agents/<name>.md` for check access blocks any other command. Measured 2026-10-17 with Claude Code 2.1.302 and the same hook passed through `--agents`: `echo guard-test` blocked, `python tools/checks/legal_check.py` ran. Not yet measured from the project file, which the docs say needs the folder trusted (https://code.claude.com/docs/en/sub-agents.md). | TPL-42 | In a new session, ask `legal` to run `echo guard-test`; it must be blocked. | 2026-10-31 | open | |
| A-8 | GitHub plays the CSS animation in `docs/images/demo.svg` when the README shows it. | README, TPL-21 | View the README on github.com and watch the demo replay. | 2026-10-31 | open | |
