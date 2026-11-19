# AWS re:Invent Booth Screen: Inference Mini-Theater

A self-contained, zero-dependency booth screen for the AWS re:Invent mini-theater. One HTML
file carries a 15-scene inference narrative in a 96-second attract loop (6.4 seconds per
scene), plus presenter mode for booth staff. Everything runs offline in kiosk Chromium: no
network requests, no build step, no frameworks.

**Live page:** https://ccondado-cell.github.io/inference-screen-booth/

Light-theme sibling of the agent governance screen
([rhai-agentic-ai-booth-screen](https://github.com/ccondado-cell/rhai-agentic-ai-booth-screen)),
built on the same engine, type scale and motion grammar so the two can stand side by side in
the same booth.

## What it is

The screen argues one thing: inference is worth scaling. Demand and cost compound (2 and 3),
capacity sits stranded and chained to a single provider (4 and 5), one request then runs one
path through five layers (6), and the five layers are named one at a time with their evidence
attached: Run, Optimize, Distribute, Gate, Deliver (7 to 11). The proof follows: a trillion
tokens a month (12), up to 70 percent lower token costs on Red Hat's own estate (13), 233
percent ROI from an independent study (14), and the closer: become an AI model provider (15).

- 15 scenes, 6.4s each, 96s loop
- Vanilla HTML/CSS/JS in a single `index.html`
- All assets local (fonts, brand art, icon repository glyphs)
- Attract loop (auto-advancing) and presenter mode (manual control)
- Copy locked: headlines 7 words or fewer, support lines 12 or fewer, no em or en dashes

## Run it

Open `index.html` in any modern browser. No server needed.

For the booth kiosk (Chromium, no mouse, starts fullscreen on the loop):

```bash
chromium-browser --kiosk --noerrdialogs --disable-infobars \
  --check-for-update-interval=31536000 \
  file:///path/to/inference-screen-booth/index.html
```

## Controls

| Input | Action |
|---|---|
| Right arrow / Space / PageDown | Next scene (enters presenter mode) |
| Left arrow / PageUp | Previous scene |
| P | Pause the loop / resume |
| F | Toggle fullscreen |
| Click right half of screen | Next scene |
| Click left half of screen | Previous scene |
| Double tap (touch) | Toggle fullscreen |

Presenter mode takes over after any manual input; the pause pill in the corner toggles back to
the attract loop.

## Repository layout

```
index.html          The screen (everything: HTML, CSS, JS)
assets/             Brand art, icon repository glyphs, logo
fonts/              Red Hat Display / Red Hat Text (woff2)
tools/validate.py   Copy, structure, motion and offline checks (rerunnable)
tools/verify_icons.py  White-background legibility check for shipped glyphs
docs/               Locked copy, decision log, implementation addendum
```

Design record lives in `docs/`: the locked copy document with the fifteen-scene table, the
decision log (every scene ruling, with exact geometry), and the implementation addendum
(asset manifest, motion decisions, measured durations, version history).

## Verify before publishing

```bash
python3 tools/validate.py        # 30 checks, no dependencies
python3 tools/verify_icons.py    # needs Pillow
```

`validate.py` enforces the things that are easy to break silently: exact headline and support
copy for all fifteen scenes, 7 and 12 word limits, zero em or en dashes, local-only asset
references, credits on the scenes that need them, 15 x 6.4s loop math, animation present on
every scene, and `node --check` on the extracted script. The expected-copy tables live in that
file, so **a copy change and a table change belong in the same commit**.

## Asset credits and usage

- **3D backdrops:** official Red Hat AI brand assets (Light1 set).
- **Environment and modality icons:** the official Red Hat Icon Repository.
- **Fonts:** Red Hat Display and Red Hat Text.
- **`assets/gen/scene13-river.png`:** a generated river render, retired from the build at
  v1.3.3 and kept only because the revert is one `img` tag. Nothing references it.

These brand assets are Red Hat property and are provided here for this Red Hat project only;
they are not licensed for reuse under the repository code license. See `LICENSE`.

## Maintenance

The screen is copy-locked. Any wording change needs the copy document, the expected-copy
tables in `tools/validate.py`, and the addendum updated together, then a validation run.

Keep `index.html` self-contained: no external requests, no build tools, no CDN fonts. If a
scene needs new art, drop it in `assets/gen/` following the rules in `assets/gen/README.md`
and reference it by relative path only.
