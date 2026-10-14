# Example: a setup dry run

A repeatable test of the setup interview, and an example of what setup produces. A fictional
founder with fixed answers (`founder.md`) is interviewed by the setup agent in a fresh copy of
this template, following `prompt.md`. The result is scored against `rubric.md`.

## Files

| File | What it is |
|---|---|
| `prompt.md` | The prompt that starts the run. Paste it into any AI coding tool opened in a fresh copy of the template. |
| `founder.md` | The founder's answers. Whoever plays the founder answers only what is asked, only from this file. |
| `rubric.md` | What a passing run must show, item by item. |
| `results/<date>-<tool>.md` | Each run's score, findings and the fixes made because of it. |
| `results/<date>-<tool>/` | The files that run produced, kept as the worked example. |
| `REPORT-<date>.md` | The test report comparing that day's runs, with the fixes they led to. |

## Running it

1. Make a fresh copy of the template (clone it into an empty folder).
2. Open that copy in your AI coding tool and paste `prompt.md`.
3. When the run finishes, score it against `rubric.md` and save the result under `results/`.

A run with a scripted founder shows that the interview and its outputs work. It does not show
how a real founder experiences it; that needs a real person (see `docs/ASSUMPTIONS.md`).
