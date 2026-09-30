#!/usr/bin/env python3
"""Turn raw phone screenshots into article images for the portfolio.

One source makes a body image; two or more make a side-by-side card for the
`image:` front matter. The crop is proportional rather than in pixels, so the
same numbers work on any screenshot with the same aspect ratio.

    script/shot.py static/img/portfolio/kazz-home.webp shots/home.png
    script/shot.py --card static/img/portfolio/kazz-front.webp shots/home.png shots/ai.png

Requires Pillow:  python3 -m pip install --user pillow
"""
import argparse
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is not installed:  python3 -m pip install --user pillow")

# Theme tokens, same ones the SVG diagrams use.
BAND = (247, 250, 250)    # --band fill  #f7fafa
BORDER = (205, 205, 205)  # neutral border #cdcdcd

# Defaults that produced the existing Kazz images.
BODY = dict(height=820, pad=44, radius=20)
CARD = dict(height=660, pad=60, radius=18)
TOP, BOTTOM = 0.032, 0.635


def panel(path, top, bottom, height):
    """Trim the status and navigation bars, keep the meaningful top of the
    screen, and scale to a common height so panels line up."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    im = im.crop((0, int(h * top), w, int(h * bottom)))
    cw, ch = im.size
    return im.resize((int(cw * height / ch), height), Image.LANCZOS)


def compose(panels, pad, gap, radius):
    height = panels[0].height
    width = pad * 2 + sum(p.width for p in panels) + gap * (len(panels) - 1)
    canvas = Image.new("RGB", (width, height + pad * 2), BAND)
    x = pad
    for p in panels:
        mask = Image.new("L", p.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [0, 0, p.width - 1, p.height - 1], radius=radius, fill=255)
        canvas.paste(p, (x, pad), mask)
        ImageDraw.Draw(canvas).rounded_rectangle(
            [x, pad, x + p.width - 1, pad + p.height - 1],
            radius=radius, outline=BORDER, width=2)
        x += p.width + gap
    return canvas


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", help="destination .webp")
    ap.add_argument("sources", nargs="+", help="raw screenshots")
    ap.add_argument("--card", action="store_true",
                    help="card proportions (implied by two or more sources)")
    ap.add_argument("--top", type=float, default=TOP,
                    help=f"fraction trimmed off the top, the status bar (default {TOP})")
    ap.add_argument("--bottom", type=float, default=BOTTOM,
                    help=f"fraction of the screen kept (default {BOTTOM})")
    ap.add_argument("--height", type=int, help="panel height after scaling")
    ap.add_argument("--pad", type=int, help="margin around the panels")
    ap.add_argument("--gap", type=int, default=48, help="space between panels (default 48)")
    ap.add_argument("--radius", type=int, help="corner radius")
    ap.add_argument("--quality", type=int, default=88, help="webp quality (default 88)")
    a = ap.parse_args()

    preset = CARD if (a.card or len(a.sources) > 1) else BODY
    height = a.height or preset["height"]
    pad = a.pad if a.pad is not None else preset["pad"]
    radius = a.radius if a.radius is not None else preset["radius"]

    panels = [panel(s, a.top, a.bottom, height) for s in a.sources]
    out = compose(panels, pad, a.gap, radius)
    out.save(a.out, "WEBP", quality=a.quality, method=6)
    print(f"{a.out}  {out.width}x{out.height}  ratio {out.width / out.height:.2f}")


if __name__ == "__main__":
    main()
