# The team

Every agent in `agents/`, with its job. `tools/checks/template_check.py` keeps this table in step
with the agent files (TPL-4), so adding an agent means adding its row here and nothing in
`AGENTS.md`. Which agents are switched on for this project is decided at setup
(`project.toml [team] enabled`); a tiny project may run with five.

| Agent | Job |
|---|---|
| [`orchestrator`](../agents/orchestrator.md) | Project manager: picks the track and the agents, holds the gates. |
| [`setup`](../agents/setup.md) | Interviews the founder and writes `project.toml` and the first decisions. |
| [`researcher`](../agents/researcher.md) | Finds what similar products do, as options for the grilling. |
| [`feasibility`](../agents/feasibility.md) | Checks an idea can be built and run on this stack and budget. |
| [`architect`](../agents/architect.md) | The system map, and per feature the design, contract and tickets. |
| [`agentic-workflow`](../agents/agentic-workflow.md) | Designs the product's AI workflows: guardrails, evals, cost. |
| [`platform-architect`](../agents/platform-architect.md) | Optional: one platform's app inside, under the lead architect. |
| [`product-designer`](../agents/product-designer.md) | Designs what users see, for every platform. |
| [`platform-designer`](../agents/platform-designer.md) | Optional: one platform's screens, inside the shared brand. |
| [`web-dev`](../agents/web-dev.md) | Builds the web app, test first. |
| [`android-dev`](../agents/android-dev.md) | Builds the Android app, test first. |
| [`ios-dev`](../agents/ios-dev.md) | Builds the iOS app, test first. |
| [`desktop-dev`](../agents/desktop-dev.md) | Builds the desktop app, test first. |
| [`backend-dev`](../agents/backend-dev.md) | Builds the server, data and integrations, test first. |
| [`debugger`](../agents/debugger.md) | Finds the cause of hard bugs, proved by a failing test. |
| [`reviewer`](../agents/reviewer.md) | Second reader of every spec, design and diff. Never edits the work. |
| [`qa`](../agents/qa.md) | Tests against the rows and holds the release gate. |
| [`rollback`](../agents/rollback.md) | On QA's call, puts the last good version back live. |
| [`security`](../agents/security.md) | Threat model, secrets, auth, dependencies, data exposure. |
| [`legal`](../agents/legal.md) | Privacy, terms and regional law. Checklists, not legal advice. |
| [`dashboard`](../agents/dashboard.md) | The founder's dashboard: health, AI usage and spend, controls. |
| [`devops`](../agents/devops.md) | Environments, CI, release, rollback, monitoring. |
| [`growth`](../agents/growth.md) | Positioning, landing copy, pricing experiments, analytics. |
| [`social-media`](../agents/social-media.md) | Platforms, voice and post drafts. Posting waits for the founder. |
| [`explainer-writer`](../agents/explainer-writer.md) | Optional: scripts for explainer videos, sourced, education not advice. |
| [`optimizer`](../agents/optimizer.md) | Audits the workflow for cost and waste. Proposes, never applies. |
