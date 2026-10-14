# How it works

This page is for the curious and for developers. You don't need it to use the template.

## The files

- **`AGENTS.md`** is the operating manual every AI tool reads first: the rules, the team, the
  three tracks of work (fix, feature, bet) and where everything lives.
- **`agents/`** holds one brief per agent: what it reads, what it produces, the gates it holds
  and what it must never do.
- **`skills/`** holds the methods the agents share, such as grilling, the readiness gate, the
  release checklist and the legal review. Each is a `SKILL.md`.
- **`project.toml`** is your answers from setup: who you are, the product, regions, customers,
  stack, how strict the gates are, which agents are on, your monthly AI budget.
- **`docs/`** is where the work lands: requirements, decisions, one folder per feature, legal
  checklists, experiments and history.
- **`tools/`** holds the checks, written in plain Python with nothing to install.

## One source, every tool

The agents and skills are plain Markdown, so any tool can read them. For tools that have their
own format, `python tools/sync_adapters.py` generates it:

| Tool | What it reads |
|---|---|
| Claude Code | `.claude/agents/` and `.claude/skills/` (generated), `CLAUDE.md` (points to `AGENTS.md`) |
| Cursor | `.cursor/rules/` (generated) |
| Gemini CLI | `GEMINI.md` (points to `AGENTS.md`) |
| Codex and others | `AGENTS.md` directly |

Generated files are never edited by hand. A check fails if they drift from their sources.

What is tested so far is that the files are generated correctly. Whether each tool loads them
as described is an open assumption until someone tries it: see `docs/ASSUMPTIONS.md` (A-2 to A-5).

Each agent has a tier (deep, standard or fast), which maps to a model in each tool. The mapping
lives in `project.toml`, so you can run cheaper or stronger models without touching the agents.

## The rules, and how they are enforced

A rule that matters is turned into a check, not left as a sentence the agents might forget.

| Rule | Enforced by |
|---|---|
| Write the requirement before the code | `tools/checks/req_check.py`: every row is well formed, every tested row is named by a test |
| End every round with all checks passing | `tools/run_all.py`, run before every commit by `tools/githooks/pre-commit` and in GitHub Actions |
| Commits are yours, with no AI credited | `tools/githooks/commit-msg`, tested by `tools/checks/commitmsg_check.py` |
| Agents and skills stay valid and small | `tools/checks/template_check.py` |
| Generated tool files match their sources | `tools/checks/adapters_check.py` |
| Legal checklists carry a disclaimer, a date and sources | `tools/checks/legal_check.py` |
| Experiments are written down before they start | `tools/checks/experiments_check.py` |

When a check fails and you decide to live with it for now, it goes in `tools/known_red.json`
with your name, the date and a date to look again. The sweep then reports it as known, and
reminds you when that date passes.

The template is held to the same rules it gives you. Its own requirements are in
`docs/requirements/TPL.md`.

## Running the checks yourself

```
python tools/run_all.py
```

It prints one line per check and ends with GREEN, or RED and the reason. You need Python 3.11 or
newer.
