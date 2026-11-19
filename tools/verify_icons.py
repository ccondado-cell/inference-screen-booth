#!/usr/bin/env python3
"""Verify every shipped icon PNG works on a WHITE background.

This screen is the light-theme sibling of the agentic governance screen, so a
light or white glyph would be invisible on it. The check counts opaque pixels
and requires the dominant glyph color to be either Red Hat Red (r > 150, g < 80,
b < 80) or dark (r, g, b all < 80). Anything pale is rejected.

Screens the files that actually ship, in assets/icons/. No external paths, no
assumptions about the Red Hat Icon Repository being present.

Usage:  python3 tools/verify_icons.py        (exit 0 = pass, 1 = failure)
Needs:  Pillow (pip install pillow)
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_DIR = os.path.join(ROOT, 'assets', 'icons')

# Glyphs screened during the build and deliberately not shipped, kept for the
# record: image-mode-691.png, a near-white glyph at rgb(233, 217, 217) that
# would vanish on this ground.


def check(path):
    im = Image.open(path).convert('RGBA')
    px = im.load()
    w, h = im.size
    opaque = 0
    rs = gs = bs = 0
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            r, g, b, a = px[x, y]
            if a > 200:
                opaque += 1
                rs += r
                gs += g
                bs += b
    if opaque == 0:
        return None, 0, 'REJECT: no opaque pixels'
    r, g, b = rs / opaque, gs / opaque, bs / opaque
    if r > 150 and g < 80 and b < 80:
        verdict = 'OK-red'
    elif r < 80 and g < 80 and b < 80:
        verdict = 'OK-dark'
    else:
        verdict = f'REJECT: pale glyph rgb({r:.0f},{g:.0f},{b:.0f})'
    return (r, g, b), opaque, verdict


def main():
    if not os.path.isdir(ICON_DIR):
        print(f'no icon directory at {ICON_DIR}')
        return 1

    names = sorted(n for n in os.listdir(ICON_DIR) if n.lower().endswith('.png'))
    if not names:
        print('no PNGs found in assets/icons/')
        return 1

    print(f"{'icon':42s} {'opaque':>7s} {'avg glyph rgb':>16s}  verdict")
    failures = 0
    for name in names:
        rgb, opaque, verdict = check(os.path.join(ICON_DIR, name))
        rgb_s = f'({rgb[0]:.0f},{rgb[1]:.0f},{rgb[2]:.0f})' if rgb else '-'
        print(f'{name:42s} {opaque:7d} {rgb_s:>16s}  {verdict}')
        if verdict.startswith('REJECT'):
            failures += 1

    print()
    print(f'{len(names)} icons checked, {failures} rejected')
    print('ALL PASS' if failures == 0 else f'{failures} FAILURE(S)')
    return 0 if failures == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
