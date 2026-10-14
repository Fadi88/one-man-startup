# Where to post

Audience: non-technical founders and solo builders, plus developers curious about agent workflows.
Written 2026-10-14. Every "checked" date below is 2026-10-14.

How to read the evidence lines. "Opened" means I opened the page in this session and the quote is
from it. "Not opened" means the page refused or failed, and what follows is a search-result
summary or nothing; such a venue's rules must be read by Fadi before anything is posted, and I
state no rule from memory. I have no usage statistics for any platform, so the ranking is a
judgment about fit and about how well the venue's rules are known, not a measurement.

## Ranking, best first

| # | Venue | Verdict | Why |
|---|---|---|---|
| 1 | Show HN | Post | The project can be tried (copy it, run setup), the rules are open and clear, and the audience includes the developers curious about agent workflows. Also the harshest audience for "no code" claims, so the honest framing matters most here. |
| 2 | r/ClaudeAI | Post, after reading Rule 7 | The closest match to people already using Claude Code. Showcase posts reportedly need 50 karma, so Fadi's account must be checked first. |
| 3 | LinkedIn | Post | The only venue besides HN whose policy page I could open and which has no per-community limit. Fits non-technical founders and Fadi's own network. |
| 4 | r/SideProject | Post, after reading the rules | Described by third parties as the promotion-friendly sub for builders. Rules not opened. |
| 5 | Indie Hackers | Post, after reading the guidelines | Solo builders are the audience. Guidelines page refused me (403). |
| 6 | X | Optional, short | One short thread. Rules page not opened. Worth it only if Fadi already has an audience there. |
| 7 | DEV, tag `#showdev` | Optional, post only | Short project post, with AI disclosure. No article, as decided. |
| Hold | GitHub Discussions "Show and tell" for Gemini CLI and Codex, Cursor forum "Built for Cursor" | After 2026-10-31 | Only once A-3, A-4, A-5 are confirmed (see below). |
| Hold | awesome lists | See `awesome-lists.md` | Mostly gated by repo age or by the untested tool support. |
| Skip | Product Hunt, Lobsters, r/SaaS, r/ChatGPTCoding, r/cursor, r/indiehackers, r/EntrepreneurRideAlong, tool Discords | | Reasons at the end of this file. |

## Launch week

Do the tool checks first: open the repo in Claude Code, Codex, Gemini CLI and
Cursor and run what `docs/ASSUMPTIONS.md` A-2 to A-5 says. Their confirm-by date is 2026-10-31.
If they pass, the posts can say so. If not, the drafts already say "untested", which is honest
either way, but a launch of a Claude Code template whose own load check (A-2) is still open is a
weaker first impression than one where it is closed.

Spacing is my recommendation, not a venue rule. One venue per day, so Fadi can answer every
comment on the day and fix what the comments find before the next post.

| Day | Date | Post | Notes |
|---|---|---|---|
| Tue | 2026-10-20 | Show HN | Fadi is online all day to answer. HN documents no best time. Post the first comment right after submitting. |
| Wed | 2026-10-21 | LinkedIn | Plain-language version, aimed at non-technical founders. |
| Thu | 2026-10-22 | r/ClaudeAI | Only if the karma and Rule 7 check passes. Do not post the same text to other Claude subreddits the same day. |
| Fri | 2026-10-23 | r/SideProject | Use the weekly share thread if one exists when you check. |
| Mon | 2026-10-26 | Indie Hackers | |
| Tue | 2026-10-27 | X thread, then DEV `#showdev` if wanted | Both optional. |
| Wed | 2026-10-28 | First day `awesome-claude-code` could accept it (repo must be 14 days old) | Read `awesome-lists.md` first: the fit is doubtful. |

If a post gets a bad reception, stop and read the comments before the next one. One odd result
is not a pattern, but a repeated objection is a fix to the README or the drafts.

## Experiment entry (ready to paste into `docs/EXPERIMENTS.md` if Fadi approves)

Not written into that file: it is outside this folder, and the thresholds are Fadi's.

```markdown
### N. Launch week for the template, from 2026-10-20
- **Why:** nobody outside the repo knows the template exists.
- **Change:** one post per venue in `examples/template-launch/where-to-post.md`, one per day.
- **Hypothesis:** the venues that fit the audience send people who copy the template.
- **Prediction:** Fadi sets the number before 2026-10-20 (there is no baseline to base one on).
  Counted per venue: visits and "Use this template" clicks from that venue, not upvotes or likes.
- **Wrong if:** Fadi sets the number; suggested form: a venue that sends visits but no copies in
  the read window comes off the list, and the README or the post gets the fix its comments asked for.
- **Confounds:** several venues in one week, and a post on one venue is seen on another. Visits
  can only be split by referrer, and I have not checked what GitHub's traffic page shows.
- **Read:** 2026-11-03 (two weeks after the first post).
```

## Venue by venue

### 1. Show HN

- Rules: https://news.ycombinator.com/showhn.html (opened) and
  https://news.ycombinator.com/newsguidelines.html (opened). Checked 2026-10-14.
- What matters:
  - "Show HN is for something you've made that other people can play with."
  - "Off topic: blog posts, sign-up pages, newsletters, lists, and other reading material." and "Don't post landing pages or fundraisers." Link the GitHub repo, not a page about it.
  - "Please make it easy for users to try your thing out, ideally without barriers such as signups or emails." The template needs a paid AI coding tool to be used; say so in the post.
  - "Don't post quickly-generated one-offs; anybody can do that now."
  - "The project must be something you've worked on personally and which you're around to discuss." Hence the day of availability.
  - "Please don't ask friends to upvote or comment." and "Don't solicit upvotes, comments, or submissions."
  - "Please don't use HN primarily for promotion." and "It's ok to post your own stuff part of the time."
  - "Don't post generated text or AI-edited text. HN is for conversation between humans." (comments) and "Please don't put generated text in HN posts." (submissions). The draft in `drafts/01-show-hn.md` was drafted by an AI, so Fadi must rewrite title, text and first comment himself. This is the rule most likely to bite.
- Format: title starting "Show HN:", a link to the repo, and the author's first comment. The showhn page does not mention a first comment or any timing; those are conventions I cannot cite.
- When: no documented best time. Tuesday 2026-10-20 in the plan above is my choice, not HN's.

### 2. r/ClaudeAI

- Rules page: https://www.reddit.com/r/ClaudeAI/about/rules.json. Not opened (this tool is blocked from reddit.com, and the mirrors I tried returned 502, 429 or a bot wall).
- Secondhand, not verified: a web-search summary of a moderator-pinned "Built with Claude" project showcase megathread dated 2026-04-15 says showcase posts in the feed need the author to have at least 50 total karma, and that lower-karma authors are sent to the megathread; it also refers to "Rule 7" for showcase requirements. I did not open the thread (https://redlib.groet-infra.nl/r/ClaudeAI/comments/1sly3jm/built_with_claude_project_showcase_megathread/ returned 502 twice). A third-party launch note advises against posting the same content to r/ClaudeCode the same day; that is that author's opinion, not a rule.
- Fadi must: read the sidebar rules and Rule 7, check his karma, use the flair the sub requires, and follow the megathread route if his karma is under the threshold.
- Format: a plain description of the template, what was tested, and what was not; screenshots of the README diagrams help. Draft: `drafts/02-r-claudeai.md`.
- When: not documented.

### 3. LinkedIn

- Policy: https://www.linkedin.com/legal/professional-community-policies (opened). Checked 2026-10-14.
- What matters: "Do not spam members or the platform."; "Don't do things to artificially increase engagement with your content."; "Do not share false or misleading content". No self-promotion limit or AI-disclosure rule appears on that page, and it has no dedicated AI policy. Do not use engagement groups or ask contacts to boost the post.
- Format: a personal post in the first person, plain words, one link (put it in the first comment if Fadi prefers, a style choice, not a rule). Draft: `drafts/03-linkedin.md`.
- When: not documented.

### 4. r/SideProject

- Rules page: https://www.reddit.com/r/SideProject/about/rules.json. Not opened (reddit.com blocked; https://safereddit.com/r/SideProject/about gave a bot wall; https://redlib.catsarch.com/r/SideProject/about gave 429).
- Secondhand only: a third-party guide describes weekly "Share your project" threads where promotion is welcome if you also engage with others' projects (the web search result I saw quoted it; I did not open it). Unverified.
- Fadi must read the rules and the pinned threads before posting. Draft: `drafts/04-r-sideproject.md`.
- When: not documented.

### 5. Indie Hackers

- Guidelines: https://www.indiehackers.com/guidelines returned 403, and the home page also returned 403. Not opened.
- Secondhand only: community threads and third-party guides say promotional posts are viewed unfavourably and that a "Show IH" style post is the norm for sharing a product. None is official. Fadi must read the current guidelines in a browser first.
- Format: a first-person story post (what I built, why, what is untested) with the link at the end. Draft: `drafts/05-indie-hackers.md`.
- When: not documented.

### 6. X

- Rules: https://x.com/rules returned 402; https://help.x.com/en/rules-and-policies/platform-manipulation returned 403. Not opened. I state no rule.
- Format: a short thread, the first post self-contained, no hashtags needed. Draft: `drafts/06-x.md`.
- Only worth it if Fadi already has followers who are founders or developers. Do not buy followers or use engagement groups (this agent's own rule).

### 7. DEV, `#showdev` (post only)

- Pages opened 2026-10-14: https://dev.to/t/showdev (tag guidelines), https://dev.to/guidelines-for-ai-assisted-articles-on-dev (AI-assisted articles), https://dev.to/code-of-conduct (conduct).
- What matters:
  - The tag is "For showing off projects and launching products." and posts should stay "community-driven and not overly corporate or salesy."
  - AI-assisted articles should "Disclose the fact that they were generated or assisted by AI in the post", with the #ABotWroteThis tag at the top or a statement anywhere, including the end. The draft is AI-assisted, so it carries a disclosure line. Keep it.
  - They also should not "Promote any business, program, or course (including your own)." The template is free and MIT licensed with nothing for sale, which I read as fine, but I am not DEV's moderator; keep the post about the project, with no sign-up, newsletter or paid offer.
  - The conduct page lists "Following our AI Guidelines and disclosing AI assistance if used to create content" as expected behaviour.
- A search result (not opened) mentions a newer in-editor AI disclosure setting on DEV. Check the editor for it when posting.
- Format: a short post. No article, as Fadi decided. Draft: `drafts/07-devto-showdev.md`.

### Hold: the four tools' own communities

- Cursor forum: https://forum.cursor.com/c/showcase/9 (opened) has a Showcase category with "Built with Cursor" ("Show off projects that Cursor helped you build!") and "Built for Cursor" ("Share extensions, MCP servers, rules, and integrations you've built for the Cursor."). Guidelines https://forum.cursor.com/guidelines (opened) say Showcase is the place, "Contribute to the community first", "If you sell or profit from something you share, say so", and that dropping product links into other people's threads is "closer to spam than participation." Cursor support is untested (A-5), so wait until it is confirmed, then post in "Built for Cursor", written as rules for Cursor.
- Gemini CLI: https://github.com/google-gemini/gemini-cli/discussions (opened) has a "Show and tell" category. Codex: https://github.com/openai/codex/discussions (opened) has "Show and tell". Neither page showed posting rules. Gemini CLI and Codex support are untested (A-3, A-4), so wait for those checks to pass.
- Claude: https://github.com/anthropics/claude-code/discussions returned 404 (no Discussions). The Claude Discord rules could not be found: a search found only unofficial notes. Not opened; skip until Fadi has joined and read the rules channel himself.

### Skipped, and why

- Product Hunt: https://www.producthunt.com/launch (opened) says "Company accounts are prohibited.", the only real rule is that "you cannot ask people directly to upvote your product", and launches are timed to 12:01 am Pacific as a suggestion. https://www.producthunt.com/launch/before-launch (opened) says "Newly created accounts will even need to wait 1 week before posting a product." and recommends joining three months or more before launch. It covers nothing on open source or AI disclosure, and the community guidelines URL I tried returned 404. A free GitHub template is not what that audience browses for, and a launch day is a lot of effort for an uncertain fit. Skip unless Fadi's account is old and he wants it.
- Lobsters: https://lobste.rs/about and https://lobste.rs/ both refused the connection from here. I could not read its rules or confirm how an account is obtained. Skip; I will not guess.
- r/SaaS: third-party guides disagree about whether product posts are allowed at all. Unverified; skip.
- r/ChatGPTCoding, r/cursor, r/indiehackers, r/EntrepreneurRideAlong: I could not open their rules, and my searches found nothing usable on the first two. A third-party guide describes r/EntrepreneurRideAlong as a place for journey and milestone posts, which suits a later "what happened after launch" post better than a launch. Skip for now. I could not verify that any of these subreddits exists or is active, so I recommend none.
- Claude Discord and other chat servers: no official rules found; see above.
