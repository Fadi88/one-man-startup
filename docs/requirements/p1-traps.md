# Traps

Mistakes that cost time once and will cost it again. Each trap says what happened and what it
cost, so the next agent believes it. Traps tied to one kind of file go in that tool's path rules
instead; this file holds the ones that apply everywhere.

- **Measure before theorising.** Read the real values, logs and inputs before explaining a
  failure. The plausible cause is often not the cause.
- **Two implementations drift.** When the same figure is computed twice, they disagree later,
  silently (`skills/single-source/`).
- **A broken checker looks exactly like a clean one.** Every check must fail loudly when it finds
  nothing to check, and must be tried once against a case it should catch.
- **Grep after deleting.** A removed function, route or setting is usually still named somewhere.
- **Scripted edits assert their match count.** A search-and-replace that matched zero times or
  twice the expected number is a bug in the edit, not a success.
- **On Windows, `python3` can be a Microsoft Store stub.** `command -v` finds it, and running it
  only prints an install hint and exits 49. While the template was being built, this made the
  git hooks refuse every commit. Probe that an interpreter runs before using it, as
  `tools/githooks/` does.
- **One odd result is not a pattern.** Explain it; do not change a rule for it.
