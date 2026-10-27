---
name: human-design
description: Keeps every screen, icon, image and line of interface copy from looking AI-generated - the tells to refuse, what to do instead, and a render-and-inspect gate that the reviewer repeats blind. Use with frontend-design on every design and every ticket that changes what users see.
---

# Human design

The design humanizer: `frontend-design` sets the direction, this skill refuses the defaults that
make a product look machine-made. A design is not done until it passes the gate at the end.

First written for a real project made from this template, from two public rule lists for the
same job: anti-ai-slop (https://github.com/Vinayak-Shukla-03/anti-ai-slop) and Hallmark
(https://github.com/Nutlope/hallmark), both MIT-licensed (GitHub, checked 2026-10-17). The
wording here is our own.

## The tells, and what to do instead

| Refuse | Instead |
|---|---|
| The toolkit's default colours left as they are, and gradients by reflex | A palette from `docs/design/brand.md`, one accent with a job |
| One typeface at one weight everywhere; a second script (Arabic, say) only as a fallback | A type scale with real contrast in size and weight; faces chosen to sit together in every language the product uses |
| Every block the same rounded card with the same padding | Size, spacing and radius that show what matters most; a list where a list is clearer |
| Emoji as icons, mixed icon sets, sparkle or magic icons | One icon set, its licence recorded, one stroke and size system |
| Filler copy ("unlock", "elevate", "seamless", "your journey", "not X, it's Y"), hype, exclamation marks | Plain words the audience would use themselves |
| Placeholder data: round numbers, lorem ipsum, made-up stats or testimonials | Realistic sample data with its rough edges; any real number has a source |
| Generic 3D blobs, abstract waves, AI-generated people, mascot empty states | No image unless it earns its place; real photography or drawn illustration with its licence; empty states that say what to do next |
| Fade-in on everything, motion for decoration | Motion only where it explains a change, and off under reduced motion |
| The same screen shape as every template in the category | Structure from the task and the moment the user is in |

## Made for these people

Before drawing, write two lines in `ux.md` (or `ux-<platform>.md`): who is using it and in what
moment, and what this screen must make easy for them. After drawing, compare it with three real products in the
category (from `research.md`) and name one thing that is ours and not theirs. If nothing is,
redesign.

## The gate

1. Render the screens: the mockups with `python tools/render_mockups.py`, then the build on a
   device, emulator or browser.
2. Look at each in light and dark, in every language and reading direction the product has,
   and at the largest text size.
3. Walk the table above screen by screen, and write a pass or the tell found in
   `docs/work/<id>/human-design.md`, with the screenshot paths.
4. `reviewer` repeats step 3 without reading yours first, then compares. Any tell either of you
   finds blocks the hand-off until it is fixed.
5. The founder sees the screenshots before a design goes to build, shown to them as
   `skills/founder-voice/` says, never as paths.
