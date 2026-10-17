# Proposal: lessons from setting up Fuel & Train (2026-10-17)

Proposed changes, not decisions. Collected while a real project (Fuel & Train, an Android
fitness app) ran setup, research, six grilling rounds, architecture and the first designs on this
template in one day. Each lesson says what happened, what it cost, and a suggested change. The
template's founder decides which to take; each accepted one becomes a TPL row before any change.

## Setup

1. **`clean_template.py` refuses until `[product] name` is set**, but `skills/setup/4-finish.md`
   lists cleaning before nothing else, and `3-write.md` lists `project.toml` first. Running it
   early just fails. Suggest: say in step 4 that `project.toml` must be written first.
2. **The budget question gets misread.** Asked twice; both times the founder answered about AI
   features in the product, not what the agent team costs. Suggest wording: "How much may the AI
   assistants that build the app cost you per month? This is not about AI inside your app."
3. **Repository visibility is never checked.** The founder said the GitHub repository was
   private; it was public, and setup had already pushed. Suggest: step 4 checks visibility
   (`gh repo view --json visibility`) and matches it to `project.toml` before the first push.
4. **An existing app in a sibling folder.** The founder pointed at his personal app "one level
   above". Setup had no branch for "rebuild a generic version of an existing product". Suggest a
   setup branch: copy, rebuild, or rebuild borrowing requirements, plus a helper that mines the
   old requirement rows into per-screen candidate files (worked well here).
5. **Decisions changed several times in one session** (regions, server, name). Superseding a
   closed decision had no convention. Suggest: a closed decision that replaces another marks
   the old one "(Superseded on <date> by ...)" and `decision-log` says so.
6. **Countries in groups.** "MENA" means about 19 packs. Setup should ask which countries, and
   say each one is its own pack and legal check.

## Team and agents

7. **`AGENTS.md` ships at 8,992 of its 9,000-character budget**, so adding any agent means
   trimming the team table. Suggest leaving headroom (about 500 characters).
8. **Per-platform architects and designers.** The founder wanted a lead architect plus an
   Android architect and an Android designer (`agents/android-architect.md`,
   `agents/android-designer.md`). Suggest offering these as optional template agents.
9. **`legal` has no shell**, so it cannot run `tools/link_check.py` on the packs it writes; both
   legal runs had to hand the check back. Suggest `run` access for `legal`, or the setup step
   says the orchestrator runs it.

## Skills

10. **A design humanizer.** The founder asked for designs that do not look AI-made, by analogy
    with the writing humanizer. `skills/human-design/` (tells to refuse, a render-and-inspect
    gate, blind second check by `reviewer`) is a candidate template skill.
11. **Big grilling rounds.** Research for three screens produced 45 suggestions plus about 40
    old-app decisions. Asking each in chat is too much for one founder. Pattern used: a choices
    file with every recommendation (`docs/work/round-3-choices.md`) plus a handful of key
    questions in chat. Suggest adding this to `skills/grilling/`.

## Tools

12. **`link_check.py` reports ftc.gov as DEAD 404** while a browser loads the pages. Suggest a
    retry with a browser user agent, or a "verify by hand" list of hosts.
13. **Writing `project.toml` turned the backslash-u escapes for the banned dashes into the
    literal characters** (it happened again writing this file), and the
    style check went red on `banned_chars` itself. Suggest the style check skip that one line,
    or a comment warning editors to keep the escapes.
14. **CRLF warnings on Windows** on every commit. Suggest a `.gitattributes` with `* text=auto`.
15. **Every new agent forces another AGENTS.md trim.** Adding `explainer-writer` took the file to
    9,036 characters and needed three rounds of shortening other agents' job lines. Suggest
    moving the team table to its own file (for example `agents/README.md`) checked against
    `agents/`, so the operating manual stays short.
16. **Specialist content agents.** The founder asked for an agent that writes scripts for
    AI-made explainer videos (`agents/explainer-writer.md`): sourced claims, education not
    advice, both languages, `legal` before anything is published. A candidate optional agent for
    health and education products.
17. **Writing hundreds of rows at once.** Five writers in parallel produced several hundred rows from
    research, old-app candidates and a choices file; each listed its conflicts between sources
    and "proposed shared rows" instead of editing shared files. Worth writing into
    `skills/new-feature/` as the pattern for several screens at once.
18. **A new project's first push ran the template's website workflow and failed** (the `pages`
    run on the initial commit, 2026-10-17), because setup removes `.github/workflows/pages.yml`
    only later. Already fixed in the template the same day: the workflow now runs only in the
    template's own repository, guarded by a check. Nothing to do here; listed so it is not
    proposed twice.
19. **Architects must cite makers' pages but have no web access.** `architect` and
    `android-architect` have only read and edit, while their briefs require options "read from
    the provider's own pages and dated". Both runs left their facts unconfirmed and registered
    over a dozen assumptions for another agent to check. Suggest `web` access for both, or a
    standing step where `feasibility` confirms an architect's facts.
20. **The designer cannot see its own work.** `product-designer` and `android-designer` have no
    shell or browser, so they cannot render the mockups the human-design gate requires; every
    render and the screenshot look were done by the orchestrator with headless Chrome. Suggest a
    `tools/render_mockups.py` (HTML to PNG at set widths) and `run` access for designers. Built here as `tools/render_mockups.py` (TEAM-6): it captures every
    `section#screen-N` as its own PNG with Playwright; full-page captures cut off or repeated
    content, so screens must be captured one by one.
21. **Contrast is hand-computed.** Designers computed WCAG ratios by hand and one claimed pass
    was a fail (4.1 to 1). Suggest a `tools/contrast.py` that reads a palette table from
    `brand.md` and fails under 4.5 to 1, run by the sweep.
22. **Many subagents have no shell, so they cannot end their round green.** Writers, designers,
    architects and legal all handed back "sweep not run". Rule 4 then falls to the orchestrator
    every time. Suggest the orchestrator brief says so, or `run` access where checks matter.
23. **Late changes miss work already in flight.** Settings, the three modes and "Ramadan
    configurable" arrived while five agents were mid-edit; the re-check found the misses.
    Suggest the orchestrator re-briefs running agents (or queues a re-check) whenever a CORE
    row changes during a parallel round.
24. **Duplicate rows across area files.** Parallel writers specified the same behaviour in two
    files. What worked: an ownership list from the orchestrator, and the duplicate rewritten as
    "Covered by <ID>." with status n/a, never deleted. Worth adding to
    `skills/requirement-first/`.
25. **Shared files edited in parallel.** Agents writing their own area files all needed the
    generated index in `docs/REQUIREMENTS.md`; telling them not to touch it and running
    `req_check.py --fix` once at the end avoided clashes. Worth a line in `skills/handoff/`.
26. **A one-word "yes" with several questions open is ambiguous.** The orchestrator read one
    "yes" as covering two different questions and had to say so. Suggest `founder-voice` asks
    for answers by number whenever more than one question is open.
27. **Material Design pages return only a title to fetch tools**, so design facts from
    m3.material.io cannot be confirmed by agents. Suggest a standing "confirm on a real phone or
    emulator" step for platform UI facts, owned by `qa`.
28. **Workflows need the founder's opt-in.** The orchestrator once batched five writers as a
    workflow without asking; parallel agent calls do the same job. Suggest the orchestrator
    brief names this explicitly.
