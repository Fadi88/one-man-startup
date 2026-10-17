# Setup step 4: finish

Part of `skills/setup/SKILL.md`.

1. **Clean out the template** (the first setup only, when `tools/clean_template.py` exists),
   after step 3 has written `project.toml`: the script refuses while `[product] name` is unset. Run
   it without `--yes` and tell the founder in their words what it removes: the template's own
   decisions, experiments, assumptions, landing page, examples and README, and that publishing
   is switched off (`project.toml [publish] enabled = false`): nothing goes on the internet
   until they ask for it. Run it with `--yes` on their go. It keeps the template's licence notice in `docs/licenses/one-man-startup.txt`,
   which the template's licence requires, and leaves no `LICENSE` behind.
2. **Write the licence** the founder chose (`skills/setup/licences.md`, "Writing the file").
3. **Run the checks**: `python tools/sync_adapters.py`, `python tools/checks/req_check.py --fix`
   (the new `LAUNCH.md` changes the index) and `python tools/run_all.py`.
4. **Show the founder** the summary, what changed and the green checks. Commit on their go.
