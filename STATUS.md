# STATUS

> Handoff file: whoever touches this last updates it before ending a session
> (done / in flight / next / how to verify).

**Build version:** v1.3.6, Nov 19, 2026. Fifteen scenes, 96 second loop.
**Live:** https://ccondado-cell.github.io/inference-screen-booth/ (Pages, main branch, root
folder, rebuilds on push).

**Publishing gotcha, recorded once.** Pages was enabled on this repo while `main` pointed at
the root folder, yet no build had ever run: `has_pages` was true, the `github-pages`
environment existed, and the site returned GitHub's "Site not found". The first successful
build came from a plain push to `main`, not from the Pages settings. If the site ever 404s
again with the setting looking correct, push any commit and the build will queue.

## Where the file lives

This clone is the **only** real copy. Every other path is a symlink, so an edit
here is immediately the file Carlos opens, with nothing to sync and no second
copy to drift.

```
inference-screen-booth/index.html   the published page, served by GitHub Pages
inference-screen-booth/docs/        copy doc, decision log, change request, addendum
inference-screen-booth/assets/      brand art, glyphs, logo
inference-screen-booth/fonts/       the three woff2 files
inference-screen-booth/tools/       validate.py, verify_icons.py
```

Links into the two places the page is opened from:

```
talks/inference-booth-screen/index.html   -> this repo's index.html
talks/inference-booth-screen/assets       -> this repo's assets (directory link)
talks/inference-booth-screen/fonts        -> this repo's fonts
talks/inference-booth-screen/tools        -> this repo's tools
Documents/talks/inference-booth-screen/   the same, for review and sharing
```

Relative paths still resolve through the links, because the browser follows the
directory links, so the page renders identically from either path.

**Two rules that follow from this.**

1. Edit files here, never in the symlinked folders. There is one copy.
2. Never `rsync --delete` into those folders. It replaces links with copies and
   the drift comes back.

`preview/` (scene studies) and `BUILD-REPORT.md` live only in the talks folder:
working material, not published. `preview/` is gitignored here.

## Done

- v1.3.6: scene 7's dots now ride the five spokes into the runtime's left edge at 480 units
  per second and are consumed there, with one stream leaving the right edge. Before this they
  ran a shallower diagonal that put the top dot 73 units above its own line and converged 180
  units to the right of the node, so the frame contradicted its own headline. Validator gains
  V15, which locks the geometry. 31 of 31 pass.
- v1.3.5: the mantra scene deleted, sixteen scenes renumbered to fifteen, loop
  shortened from 102.4s to 96s. Deliver now cuts straight to the trillion.
  Validator retargeted: check 4c inverted to assert the mantra markup is gone,
  V11 rewritten as an adjacency test between scenes 11 and 12.
- v1.3.4: scene 12 (then the mantra) lost its headline and support. Superseded
  by v1.3.5, which removed the scene.
- v1.3.3: gate dots moved to 480 units per second with fourteen dots and an
  interleaved pass and stop order; scene 13 (now 12) rebuilt from a still render
  into a live SVG rate: seven lanes, ninety-six ghosts, three node loop, panel
  written fifteen lines at a time, three panels per cut.
- v1.3.2: the cost line in scene 2 is the only line, one crossing at x 627 in
  scene 3, red bill line retired.
- Validator at 30 of 30, `node --check` clean, 27 infinite animation rules, zero
  network, zero em and en dashes.

## In flight

Nothing is mid-edit. All deliverables are consistent at v1.3.5.

## Next

1. **Visual verification on the panel.** No headless browser was available
   during the build, so none of the following has been seen at 3 metres: the
   light-theme contrast, the single crossing in scene 3, the scene 5 outage
   read, the fills in scene 6, the ring pulse in scene 9, the captions over the
   scene 11 photograph, the gate speed at 480, and the whole of the trillion
   animation (river density, loop legibility, whether the code panel reads as
   software rather than a grey barcode).
2. **One open copy question.** Scene 10 ships on "Guardrails" pending
   confirmation from the Red Hat AI messaging guide; the fallback is "Identity.
   Rate limits. Policy." One line plus the validator table if it changes.
3. **Two hub facts to re-verify** after GA day: the OpenShell timeline and the
   gateway naming map. Both were cited with a review-after date of Nov 20 and 21.
4. **Carry to the owner:** the Gateway on one screen and Gate on the other. No
   change made; it needs a ruling, not an edit.

## How to verify

```bash
python3 tools/validate.py        # 30 checks
python3 tools/verify_icons.py    # white-background glyph check (needs Pillow)
```

To see the trillion animation's beat order without a browser, extract the engine
between `// Init Scene 12 (the trillion scene` and `// Init Scene 5`, stub the DOM,
and step `requestAnimationFrame` at 60fps: line one lands at the cut, the panel is
complete at 1.4s, the commit rule sweeps from 1.7s, full rule under full code at
1.9s, both fade from 1.98s, the next panel starts at 2.13s.

## Known soft spots

- Scene 12 (the trillion) has the only unresolved read: if seventy tokens plus
  ninety-six ghosts look like clutter rather than abundance, drop `S13_GHOSTS`
  to 60. If the code panel reads as a barcode, thin the bars from 7 to 6.
- The engine still calls the trillion scene `s13` and `S13_*` throughout, because
  it was scene 13 before the renumbering. The comment at the head of that block
  says so; do not rename without re-running validation.
- Five words alone on a frame, five node pulses, and a rail word differing from a
  diagram label (Runtime versus Run on scene 7) are all deliberate, and each is
  documented in `docs/2026-11-inference-booth-screen-decisions.md`.
