---
name: diagram-style
description: Draw architecture, flow, or sequence diagrams for the muchlis.dev portfolio as inline SVG matching the site's "sea" theme. Use whenever a portfolio or blog article needs a diagram, a new article image, or an existing diagram edited. Covers the two required variants (detail + card), the exact color and type tokens, layout rules, and the render-and-check step.
---

# Diagram style — muchlis.dev

Diagrams on this site are hand-written SVG files in `static/img/portfolio/`, referenced from Markdown. Never inline raw `<svg>` into a `.md` file: Goldmark strips raw HTML unless `unsafe` is enabled, and this site does not enable it.

## Always produce two files

A single diagram cannot serve both jobs. The masonry card renders at roughly **260px wide**, where 11–14px text is an unreadable smudge. Make both:

| File | Purpose | viewBox | Min font |
|---|---|---|---|
| `<topic>-<subject>.svg` | detail diagram, embedded in the article body | `0 0 900 452` (wide) | 11px |
| `<topic>-card.svg` | thumbnail, the article's `image:` frontmatter | `0 0 600 400` (3:2) | 20px |

The card is a **simplified restatement**, not a shrunk copy: at most 3 boxes, one vertical flow, no bands, no side notes. Keep the detail diagram for the mechanism.

**Exception:** an article has only one thumbnail, so only the diagram that feeds `image:` needs a card variant. A second or third diagram placed further down the body is a detail file on its own — do not invent a card for it.

## Tokens

Taken from the theme's `style.sea.css`. Do not invent colors.

```
accent (teal)     #379392   primary flow, key service borders, emphasized arrows
accent fill       #eef7f7   fill for the single most important box
accent fill dark  #379392   card only: solid fill for the key box, text #ffffff on it
accent text light #d8ecec   card only: subtitle on a solid teal box
heading text      #333333   box titles
body text         #666666   explanatory notes
muted text        #8c9a9a   band labels, arrow labels, secondary arrows
subtitle text     #999999   box subtitles
neutral border    #cdcdcd   ordinary boxes
band fill         #f7fafa   grouping band background
band border       #e6eded
page / box fill   #ffffff
```

Font is always `Roboto,Helvetica,Arial,sans-serif` — matches the theme body font.

| Role | Detail | Card |
|---|---|---|
| Box title | `500 14px` | `500 34px` |
| Box subtitle | `400 11px` `#999999` | `400 22px` |
| Band label | `600 11px`, `letter-spacing:1.2px`, uppercase, `#8c9a9a` | — |
| Arrow label | `400 11px` `#8c9a9a`; teal path → `500 11px` `#379392` | `500 20px` `#379392` |
| Note text | `400 13px` `#666666` | — |

Strokes: boxes `1.5` (detail) / `3` (card). Arrows `1.5` grey, `2` teal (detail) / `3` (card). Corners `rx="6"` detail, `rx="10"` card.

## Layout rules

1. **Group with bands, not boxes.** A rounded `band` rect behind a row of boxes, with an uppercase label in its top-left, carries the idea (`REQUEST PATH · SYNCHRONOUS`). Use a `·` separator, entity-escaped as `&#183;`.
2. **Colour carries the argument.** Teal marks the path the reader should follow; everything incidental stays grey. If every arrow is teal, none of them mean anything.
3. **Fill only the single most important box** (`#eef7f7`). Give supporting services a teal *border* on white. Plain infrastructure gets a grey border.
4. **Draw crossing arrows before the boxes** so a long connector reads as one continuous line, then gets cleanly overlapped by the boxes it joins.
5. **Two arrows must never leave one box from the same point.** Offset their x (e.g. publish leaves at `x=500`, the response elbow at `x=400`).
6. **Spend leftover space on a note**, not on padding — 3–4 lines of `13px` `#666666` explaining *why* the mechanism exists.
7. Box titles and subtitles are centred with `text-anchor:middle` on the box's centre x.
8. Define arrowheads once in `<defs>` as `<marker>` with `orient="auto-start-reverse"`; one marker per arrow colour.
9. Put CSS in a single `<style>` block with short class names. It keeps the file editable by hand later.

## Accessibility

Every diagram carries `role="img"` and `aria-labelledby="t d"`, with `<title id="t">` (short name) and `<desc id="d">` (one sentence stating the actual mechanism, not "a diagram of X").

## Escaping

SVG is XML. Escape `&` as `&amp;`, `—` as `&#8212;`, `·` as `&#183;`. An unescaped entity silently breaks the whole file.

## Referencing from Markdown

Use reference-style links, matching the existing articles:

```markdown
![COGS calculation flow][flow]

[flow]: /img/portfolio/majoo-cogs-flow.svg
```

And in frontmatter: `image: "/img/portfolio/majoo-card.svg"`.

## Always verify before finishing

Valid XML is not the same as a good diagram. Run all three:

```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('static/img/portfolio/NAME.svg')"
rsvg-convert -w 1350 -b white static/img/portfolio/NAME.svg -o /tmp/check.png        # detail
rsvg-convert -w 260  -b white static/img/portfolio/NAME-card.svg -o /tmp/check-card.png  # card
```

Then **look at both PNGs**. Check for overlapping text, arrows landing short of a box, labels colliding with lines, and lopsided empty space. The 260px render is the one that catches an unusable card.

## Worked example

`static/img/portfolio/majoo-cogs-flow.svg` and `majoo-card.svg` are the reference implementation. Read them before drawing a new one.
