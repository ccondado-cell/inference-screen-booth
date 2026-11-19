# STATUS

> Handoff file: whoever touches this last updates it before ending a session
> (done / in flight / next / how to verify).

**Build version:** v1.3.5, Nov 19, 2026. Fifteen scenes, 96 second loop.

## Where the file lives

`inference-screen-booth/index.html` is the published copy. The working notes
folder (`talks/inference-booth-screen/`) and the Documents mirror are copies
kept in sync by `rsync`, verified with `md5sum`. When the two disagree, this
repo wins.

## Done

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
