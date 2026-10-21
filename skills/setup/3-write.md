# Setup step 3: write it down

Part of `skills/setup/SKILL.md`. Only after the founder confirms the summary.

- `project.toml`, every field the answers settled, including `[product] licence`.
- `docs/legal/regions/<CODE>.md` for each region, copied from `docs/legal/regions/_TEMPLATE.md`,
  filled from current sources, each claim cited and dated with a short quote, unsettled points
  marked UNSETTLED, and `python tools/link_check.py` run on the packs with no DEAD links.
  Hand the packs to `legal` to review before any launch.
- `docs/requirements/p1-closed-decisions.md`: one dated line per decision taken, with the reason,
  including a public repository the founder chose to keep in step 1. Write it after the clean-out
  in step 4, which removes the template's own decisions.
- `docs/requirements/p1-open-questions.md`: what the founder deferred, and what each blocks.
- Requirement rows in `docs/requirements/LAUNCH.md` (prefix `LAUNCH`), marked `X`, for what
  customer size and domain imply (an enterprise customer implies SSO and a DPA; consumers in
  the EU imply cookie consent and data export).
- A row in `LAUNCH.md`, marked `X`, for the coverage bar on changed lines the founder chose,
  asserted by the stack's test command in CI once code exists.
- If `origin` is "rebuild": a row in `LAUNCH.md` marked `X`, "Nothing in the product copies
  the name, logo, icons, images, text or code of <based_on>, and its name cannot be mistaken
  for the original's", for `legal` to grade before launch.
- If the product has a free tier or a trial: requirement rows marked `X` for its caps (per user,
  per device without sign-up, a global daily spend ceiling), with the numbers left for the
  founder to set once the prototype has measured the cost per action. A free tier with no caps
  is not offered as an option.
- `git config --local user.name` and `user.email` set to the founder (this repository only),
  and `git config core.hooksPath tools/githooks`.
