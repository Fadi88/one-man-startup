# Example: a feature dry run

A repeatable test of the feature track (TPL-74), and an example of what it produces. The
fictional founder of the setup dry run, Nadia Example of Receipt Buddy, asks for her first
feature: upload a receipt photo and the AI sorts it into a spending category. The feature
touches AI output, personal data and financial data, so it pulls in nearly the whole track:
`researcher`, grilling, `feasibility`, the spec review, the readiness gate, `agentic-workflow`,
`architect`, `product-designer`, `legal`, `security`, a developer, `reviewer` and `qa`.

Most feature-track rows were written and never run (status `U`). The run is there to find out
whether they work when followed, so an honest FAIL is worth more than a forced PASS.

## Files

| File | What it is |
|---|---|
| `prompt.md` | The prompt that starts the run, pasted into an AI coding tool opened in a set-up copy. |
| `founder.md` | The founder's fixed answers to feature questions. Whoever plays her answers only what is asked, only from this file. |
| `rubric.md` | What a passing run must show, item by item, each naming the row it tests. |
| `results/<date>-<tool>.md` | Each run's score, findings ranked by severity, and the fix proposed for each FAIL. |
| `results/<date>-<tool>/` | The files that run produced (the work folder and the transcript), kept as the worked example. |

## Running it

1. Clone the template into an empty folder outside this repository.
2. Make it a set-up project from the setup dry run's outputs in
   `examples/setup-dry-run/results/<date>-<tool>/`: fill `project.toml` with its answers (map
   any agent name that has since been renamed, and record that you did), then run
   `python tools/clean_template.py --yes` as setup would. The clean-out deletes `examples/`,
   and with it the decision files' template sections and the template's assumptions, so copy
   the setup outputs in after it: the region packs to `docs/legal/regions/`, the `p1-*.md`
   files and `LAUNCH.md` to `docs/requirements/` (their "This project" sections only), and the
   project's own assumptions into `docs/ASSUMPTIONS.md`. Run
   `python tools/checks/req_check.py --fix`, `python tools/sync_adapters.py` and
   `python tools/run_all.py`; it must be green before the run starts.
3. Copy `founder.md` into the copy as `dry-run/founder.md`, set `git config core.hooksPath
   tools/githooks` there as setup does, and commit a baseline.
4. Open the copy in your AI coding tool and paste `prompt.md`.
5. When the run finishes, score it against `rubric.md`, save the result under `results/`, and
   copy `docs/work/<id>/` and `dry-run/transcript.md` into `results/<date>-<tool>/`.

## Limits

- One agent playing the project manager, every role and the founder cannot be independent of
  itself: it knows the founder's script and the rubric. Where a role can be started as a
  separate agent with only its brief, that is better, and the result says which ones were.
- A scripted founder shows that the rules can be followed; it does not show how a real founder
  experiences the track. That needs a real person.
- The run stops at one small ticket. Release, rollback, the dashboard build and monitoring in
  staging are not reached, so their rows stay untested by it.
- Nothing is deployed and no paid service is called, so AI accuracy and real cost per receipt
  are designed and estimated, never measured.
