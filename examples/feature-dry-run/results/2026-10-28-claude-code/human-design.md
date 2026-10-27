# Human design gate: RCPT-1 (designer's walk)

Written by `product-designer`, 2026-10-28, after `python tools/render_mockups.py` ("receipt.html:
7 screens"). Screenshots: `docs/design/mockups/shots/receipt-screen-1.png` to `-7.png`. Light:
screens 1 to 6; dark: screen 7; Arabic right to left: screen 6. Largest text size: not rendered
(the renderer has no text-size setting); checked by reading the CSS only, so not verified.

| Tell (`skills/human-design/`) | Result | Screens |
|---|---|---|
| Toolkit default colours, gradients | pass: brand palette, one accent, no gradient | all |
| One typeface, one weight; second script as fallback | partial: system face only; Arabic uses the system Arabic face at the same steps, chosen, not a fallback, but not compared side by side | 2, 6 |
| Every block the same card | pass: fields, chips and list rows differ in shape and weight | 2, 5 |
| Emoji or mixed icons, sparkle icons | pass: no icons at all | all |
| Filler copy, hype, exclamation marks | pass: plain words, no exclamation marks | all |
| Placeholder data | pass: real-looking shops and amounts with rough edges (143.75, 61.20) | 2, 5, 6, 7 |
| Blobs, waves, AI people, mascot empty states | pass: no images | all |
| Decorative motion | pass: none drawn | all |
| Same screen shape as every template | pass by intent: figures and category on one screen | 2 |

**Found by me, not fixed yet (for review):**

1. Screen 1: "Not now" is an underlined text link under a filled button. `ux.md` says "'Not now'
   as visible as yes"; the screenshot shows it is not. Either the copy in `ux.md` or the screen is
   wrong; a consent choice should not lean (for `legal`).
2. Screen 2 and 7: "Tap any line to fix it" but the shop and date fields look like read-only rows;
   no sign they can be edited.
3. Nine states in `ux.md` are described, not drawn (listed there).

The founder sees the screenshots before build (`skills/human-design/` step 5).

## Revision after review round 4 (2026-10-28)

Re-rendered: `render_mockups.py` "receipt.html: 21 screens". Now rendered: dark (7, 13 to 16),
Arabic right to left (6, 17 to 20), 200 percent text (21), and the states drawn new (8 to 12).
Looked at 17 and 21 again after the change; the rest by the same CSS.

| Issue | State |
|---|---|
| Screen 1 "Not now" weaker than yes | fixed: both are full-width buttons, one filled, one outlined |
| "Tap any line to fix it" with no cue | fixed: every field, the total included, ends in "Edit" |
| Arabic copy word for word ("تجاهل") | fixed ("لا تحفظه"); native reading still needed (A-14) |
| Arabic hint line missing | fixed on screen 6 |
| States described, not drawn | 5 of them now drawn; 6 remain one-line states on screen 3's layout |
| Largest text | rendered (21): the total wraps as "AED" over "143.75"; readable, nothing cut off. Pass, noted |
| Arabic typeface, compared side by side | pass: screens 6 and 17 to 20 against 2 and 1 to 5 |

## Second revision after review round 5 (2026-10-28)

`render_mockups.py`: "receipt.html: 31 screens". Added dark (22 to 26) and Arabic (27 to 31) of
the saved receipt, two currencies, empty month, allowance used up and reading; "Back to October"
on screen 8; the Arabic hint dropped to match the English "Edit" cue. Walk repeated on 8, 22 and
27 by looking; the rest by the same CSS. No new tell found.
