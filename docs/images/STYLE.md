# Visual style: modern product

Chosen by the founder on 2026-10-28 (TPL-81). It applies to the README images in this folder, the
landing page (`site/index.html`) and the founder's status page. Earlier styles (hand-drawn,
warm paper flattened) were turned down; see `docs/requirements/p1-rejected.md`.

The idea: a white ground, plenty of space, and one saturated colour, raspberry, used for the one
thing that matters on each screen. Everything else is ink and soft greys. Shapes are rounded, type
is a clean sans-serif with real contrast in size and weight (heavy 800 headings, regular body).
No gradients, no drop shadows, no glass, no blobs, no emoji, no badges. Dark theme is kept
(TPL-19): the same tokens with the dark values below.

## Colour tokens

| Token | Light | Dark | Role |
|---|---|---|---|
| page | #FFFFFF | #0F0D14 | Page and image ground |
| surface | #F7F5FA | #1A1722 | Cards, panels, table, chips |
| line | #E4E0EB | #2C2837 | Hairlines and image borders (decorative) |
| ink | #14121F | #F4F2F8 | Headings and body text |
| soft | #55505F | #B5AFC2 | Secondary text |
| brand | #D6246E | #D6246E | Fills: primary button, hero circle, numerals, connectors |
| brand-ink | #B0124F | #FF6FA6 | Brand-coloured text and links |
| tint | #FDEBF3 | #2A1420 | Wash behind brand content |
| on-brand | #FFFFFF | #FFFFFF | Text on a brand fill |
| ok | #1B7A4B | #5FD3A0 | The word "sweep green" only (status) |

## Type

Web-safe system stack, because GitHub renders README SVGs without loading web fonts and nothing
needs a licence or a download:

`-apple-system, "Segoe UI Variable", "Segoe UI", system-ui, Roboto, "Helvetica Neue", Arial, sans-serif`

Monospace for file names: `ui-monospace, "SF Mono", Menlo, Consolas, monospace`.

Scale: page title 84 / 800 / -2.5px tracking; section title 28 to 44 / 800 / -1px; lead 20 to 26 / 700;
body 17 / 400 / 1.65; small 13 to 15; eyebrow 14 / 800 / +2.4px tracking, upper case.

## Shape and space

Radii: 10 (focus ring, small), 20 (cards on the page), 24 (cards inside images), 28 (images),
pill 999 (buttons, tags). Spacing scale in px: 4, 8, 12, 16, 24, 32, 48, 72. Borders 1.5 px, only
on the outer frame of an image; inside, a card is a filled surface with no border.

What is ours: one raspberry hue, not the usual blue or indigo, and a single filled "end" element
per picture (the "You say go" card, the project manager, the AI tool) so the eye lands on where
the human or the control sits.

## CSS custom properties

```css
:root {
  --page: #ffffff; --surface: #f7f5fa; --line: #e4e0eb;
  --ink: #14121f; --soft: #55505f;
  --brand: #d6246e; --brand-ink: #b0124f; --brand-hover: #b0124f; --tint: #fdebf3; --on-brand: #ffffff;
  --ok: #1b7a4b;
  --font: -apple-system, "Segoe UI Variable", "Segoe UI", system-ui, Roboto, "Helvetica Neue", Arial, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --r-s: 10px; --r-m: 20px; --r-l: 28px; --r-pill: 999px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --page: #0f0d14; --surface: #1a1722; --line: #2c2837;
    --ink: #f4f2f8; --soft: #b5afc2;
    --brand-ink: #ff6fa6; --tint: #2a1420; --ok: #5fd3a0;
  }
}
```

## Contrast pairs

| Pair | Text | Background | Minimum |
|---|---|---|---|
| Body on page | #14121F | #FFFFFF | 4.5 |
| Soft text on page | #55505F | #FFFFFF | 4.5 |
| Body on surface | #14121F | #F7F5FA | 4.5 |
| Soft text on surface | #55505F | #F7F5FA | 4.5 |
| Brand text on page | #B0124F | #FFFFFF | 4.5 |
| Brand text on surface | #B0124F | #F7F5FA | 4.5 |
| Brand text on tint | #B0124F | #FDEBF3 | 4.5 |
| Body on tint | #14121F | #FDEBF3 | 4.5 |
| On-brand text on brand fill | #FFFFFF | #D6246E | 4.5 |
| On-brand text on brand-ink fill | #FFFFFF | #B0124F | 4.5 |
| White on ink fill | #FFFFFF | #14121F | 4.5 |
| Status text on page | #1B7A4B | #FFFFFF | 4.5 |
| Brand shape on page | #D6246E | #FFFFFF | 3 |
| Brand shape on tint | #D6246E | #FDEBF3 | 3 |
| Dashed outline on page | #8B8399 | #FFFFFF | 3 |
| Body on page, dark | #F4F2F8 | #0F0D14 | 4.5 |
| Soft text on page, dark | #B5AFC2 | #0F0D14 | 4.5 |
| Body on surface, dark | #F4F2F8 | #1A1722 | 4.5 |
| Soft text on surface, dark | #B5AFC2 | #1A1722 | 4.5 |
| Brand text on page, dark | #FF6FA6 | #0F0D14 | 4.5 |
| Brand text on surface, dark | #FF6FA6 | #1A1722 | 4.5 |
| Brand text on tint, dark | #FF6FA6 | #2A1420 | 4.5 |
| Body on tint, dark | #F4F2F8 | #2A1420 | 4.5 |
| Soft text on tint, dark | #D9D4E3 | #2A1420 | 4.5 |
| Dark text on light fill, dark | #14121F | #F4F2F8 | 4.5 |
| Dark text on brand-light fill, dark | #14121F | #FF6FA6 | 4.5 |
| Status text on page, dark | #5FD3A0 | #0F0D14 | 4.5 |
| Brand shape on page, dark | #FF6FA6 | #0F0D14 | 3 |
| Dashed outline on page, dark | #6F687D | #0F0D14 | 3 |

## Rules for new pictures

- Same words, same structure: restyling never changes copy.
- Brand fill is for the element that matters most, plus small marks (dots, numerals, connectors).
- Text sizes of 13 and up in images; names of files in the monospace stack.
- A picture must read in both themes: use classes with a `prefers-color-scheme: dark` block, as
  the SVGs here do.
- No em dash or en dash characters (`project.toml [style] banned_chars`).
