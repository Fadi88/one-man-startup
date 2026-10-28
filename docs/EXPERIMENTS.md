# Experiments

Bets, growth ideas and workflow changes, each written before it starts
(`skills/experiment/SKILL.md`). New entries go at the end. Closed ones move to
`EXPERIMENTS_CLOSED.md` with their numbers.

## At a glance

| # | Start | Experiment | Status | Read date |
|---|---|---|---|---|
| 1 | 2026-10-14 | Repo page: new description, topics and social preview | running | 2026-10-28 |
| 2 | 2026-10-20 | Launch week: one post a day, Show HN first | planned | 2026-11-03 |
| 3 | 2026-10-18 | Trigger-only descriptions on three discipline skills | running | 2026-11-01 |
| 4 | 2026-10-28 | Regression re-run of the feature dry run | planned | 2026-11-04 |

## The entries

### 1. Repo page: new description, topics and social preview, from 2026-10-14
- **Why:** the repository had the old premise in its description, four topics and GitHub's
  generic link card.
- **Change:** description and topics updated on 2026-10-14; social preview image uploaded by
  Fadi. No posts anywhere, so visits in this window come from search, topics and shared links.
- **Baseline:** GitHub Insights, Traffic, on 2026-10-14: 0 views, 0 unique visitors, no
  referrers in the previous 14 days (the repository is new).
- **Hypothesis:** people find the repository through GitHub search and topics without any post.
- **Prediction:** proposed, for Fadi to confirm: at least one referrer other than direct links
  appears in Traffic before the launch week starts.
- **Wrong if:** Traffic shows no visitors from github.com search or topic pages by the read
  date. Then the topics and description are not doing work on their own, and the launch posts
  carry it.
- **Confounds:** any link Fadi shares himself in this window.
- **Read:** 2026-10-28.

### 2. Launch week, one post a day, from 2026-10-20
- **Why:** to learn which venue reaches people who use the template, not only people who look.
- **Change:** the posts in `examples/template-launch/drafts/` (kept locally, not in the repository), one venue a day in the order of
  `examples/template-launch/where-to-post.md`, each rewritten and sent by Fadi.
- **Hypothesis:** one venue brings most of the visitors, and it is not the same venue that
  brings the people who press "Use this template".
- **Prediction:** proposed, for Fadi to confirm: in Traffic's referrers for the 14 days after
  the first post, one venue accounts for more visitors than all others together.
- **Wrong if:** no venue stands out (the top referrer has under a third of referred visitors).
  Then no channel is worth doubling down on yet, and the next step is the real-product build in
  public, not more posts.
- **Confounds:** posts on different days meet different news cycles; a repost by someone else.
- **Read:** 2026-11-03 (Traffic keeps 14 days, so read it before it rolls off).

### 3. Trigger-only descriptions on three discipline skills, from 2026-10-18
- **Why:** obra/superpowers reports that an agent reading a workflow summary in a skill's
  description follows the summary and skips the body, and once skipped a review step that way.
  The template's descriptions summarise the workflow. One project's observation is not a fact
  about this template, so it is tested before thirty descriptions are rewritten.
- **Change:** on 2026-10-18 the descriptions of `verify-green`, `requirement-first` and
  `ordered-steps` were rewritten as "Use when ..." triggers with no workflow summary. The other
  skills keep their summaries as the control.
- **Baseline:** no count exists of how often a skill's body was opened before its rule was
  applied; the hand-back's "Opened" list (`skills/handoff/`) is where it can be read from.
- **Hypothesis:** an agent whose skill description names only the triggers opens the body more
  often before acting on the rule.
- **Prediction:** proposed, for Fadi to confirm: in the dry runs and real sessions recorded
  under `examples/` before the read date, the three trigger-only skills appear in "Opened" lists
  at least as often as `bug-fix` and `handoff`, the two summarised skills used most often.
- **Wrong if:** they appear less often, or the agents cite their rules without having opened
  them more often than they do for the control skills. Then descriptions go back to summaries.
- **Confounds:** the three skills also gained excuse tables the same day (TPL-57), which may
  change how often they are opened for a different reason.
- **Read:** 2026-11-01.

### 4. Regression re-run of the feature dry run, from 2026-10-28
- **Why:** a Reddit comment on the launch post: the real test of the template is whether, after
  a week of changes, the reviewer catches regressions in older features and not only new code.
- **Change:** TPL-105 to TPL-110: a founder list in every review round, an "Older features"
  line on every diff review, and the re-run in `examples/feature-dry-run/README.md`.
- **Baseline:** the 2026-10-28 run (`examples/feature-dry-run/results/2026-10-28-claude-code/`):
  its `review.md` has no founder list and no diff round checked earlier features, since there
  were none.
- **Hypothesis:** the first feature's spec tests, run by the sweep on every round (TPL-109),
  catch a regression planted in its code while a second feature is built, and the reviewer's
  older-features step names it too.
- **Prediction:** proposed, for Fadi to confirm: in the re-run, the sweep goes red on the planted
  RCPT-6 regression and `review.md` has it as a blocking finding, both before the diff reaches
  `qa` (rubric M22 PASS), and every review round passes `tools/checks/review_check.py` (M21 PASS).
- **Wrong if:** the sweep stays green with the regression in place (the suite did not run, or
  RCPT-6's test does not assert what the row says), or the regression reaches `qa` unflagged.
  Then the spec tests are not the guard the rows claim, and that is fixed before anything else.
- **Design:** old against new. One copy stays on the template from before TPL-105 (commit
  `669bb64`), the other takes the current one; both get the same planted regression and the
  same second request.
- **Confounds:** whoever plants the regression knows where it is; one agent playing every role
  may carry that knowledge into the review (the README's first limit). The template changes made
  in the week also change the first feature's track.
- **Read:** 2026-11-04.
