# Feasibility: RCPT-1, a receipt photo sorted into a spending category

Written by `feasibility`, 2026-10-28, from grilling rounds 1 and 2 (`dry-run/transcript.md`)
and `research.md`, before the spec is confirmed.

**Verdict: go with changes.** Every part can be built on the chosen stack; the two changes below
keep each photo under the hosting limit and the cost per receipt well under the founder's two
cents. How well the AI reads Arabic and German receipts is not confirmed and needs a test with
made-up receipts before build.

## For Nadia

It can be built with what we chose at setup. Reading one receipt with the cheaper AI would cost
about six hundredths of a US cent; with the more capable one, about one and a quarter cents.
Both are under your two-cent line. Two changes make it work better: make the photo smaller on the
phone before it is sent, and test the AI first on made-up receipts in English, Arabic and German.

## Parts

| Part | How it would be done | Risk | Source (read 2026-10-28) |
|---|---|---|---|
| Read the photo with AI | Anthropic API, one call with the image and the fixed category list; the API takes JPEG, PNG, GIF and WebP | low | https://platform.claude.com/docs/en/build-with-claude/vision ("Claude supports JPEG, PNG, GIF, and WebP images") |
| Photo size limit | Images up to 8000x8000 px and 10 MB (base64) per image on the API | low | same page ("The maximum dimensions for each image are 8000x8000 px"; "10 MB (base64-encoded) on the Claude API") |
| Upload through the hosting | Vercel Functions take at most 4.5 MB per request body; larger returns 413 | medium | https://vercel.com/docs/functions/limitations ("The maximum payload size for the request body or the response body of a Vercel Function is **4.5 MB**") |
| Time per read | Vercel Hobby functions run up to 300 s | low | same page ("Hobby: 300s default and maximum") |
| Reading Arabic and German receipts | Not confirmed by the provider for receipts; the vision page warns of mistakes on "low-quality, rotated, or very small images" | high | vision page, "Limitations" |
| Prompt injection from receipt text | Text in the image is read by the model like any other input | medium | not a provider claim; designed for in `agentic.md` |
| Where the AI processes data | Open legal question from setup (cross-border transfer); US-only processing costs 1.1x | medium (legal, not technical) | https://platform.claude.com/docs/en/about-claude/pricing ("specifying US-only inference ... incurs a 1.1x multiplier") |

## Cost

Per receipt, assuming the photo is sent at the model's largest size (4,784 image tokens for
Claude 4.7 and later models, vision page table), about 600 tokens of instructions and about 150
tokens of answer (the 600 and 150 are estimates, assumption A-11):

| Model | Price per million tokens, input / output | Per receipt | 1x: 3,000 receipts a month | 10x: 30,000 a month |
|---|---|---|---|---|
| Claude Haiku 5.5 | $0.10 / $0.50 | about $0.0006 | about $1.84 | about $18.40 |
| Claude Sonnet 5.5 | $2 / $10 | about $0.0123 | about $36.80 | about $368 |

Prices: https://platform.claude.com/docs/en/about-claude/pricing, read 2026-10-28 (rows "Claude
Haiku 5.5 (for prompts up to 100,000 tokens) | $0.10 / MTok ... | $0.50 / MTok" and "Claude
Sonnet 5.5 | $2 / MTok ... | $10 / MTok"). The 1x usage (100 users, 30 receipts each a month) is
an assumption (A-12); the product has no users yet.

Against the founder's line ("If one receipt costs more than a couple of cents, tell me"): both
are under it. `project.toml [budget]` (US$100) is the founder's spend on the AI tools that build
the product, not this cost, so it is not compared here.

## Blockers and dependencies

- An Anthropic API account and key: the founder's step (`skills/human-steps/`), before the spike.
- The cross-border transfer question (`p1-open-questions.md`): blocks any real user's receipt,
  not the build or a test with made-up receipts.
- The free allowance numbers (LAUNCH-1 to LAUNCH-3): block any free path going live, not build.

## Changes recommended

1. **Shrink the photo on the phone before it is sent**, to the largest size the model uses
   (2,576 px on the long edge). It caps the cost per receipt, and a photo that size should fit
   under the 4.5 MB limit (not measured: the spike measures it, A-13). Yes or no?
2. **Test the AI on made-up receipts first** (a spike): about 30 invented receipts in English,
   Arabic and German, including blurred, long and hostile ones, read by both models; wrong if the
   cheaper model gets fewer than the founder's pass bar right. Needs the founder's go and an API
   account, and costs well under a dollar at the prices above. Yes or no?
3. **Start with the cheaper model**, and move to the more capable one only if the cheaper one
   fails the test. Yes or no?

## Not verified

- How well either model reads receipts in Arabic or German: assumption A-10, to be settled by
  the spike.
- The token estimates for instructions and answer: assumption A-11.
- Usage at launch: assumption A-12.
- Supabase storage limits and pricing for photos: not read in this check; photos are deleted
  after reading (LAUNCH-6), so storage is small. For `architect`.
