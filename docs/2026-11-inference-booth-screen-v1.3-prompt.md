# Inference Booth Screen, v1.3 Change Request

> **Numbering note added at v1.3.5 (Nov 19).** This prompt was written against a sixteen
> scene cut. The mantra scene was deleted and the loop is now fifteen scenes: old 13 through
> 16 are now 12 through 15. Every reference below uses the old numbers, including the
> do-not-change list. Read "scene 16" as scene 15, and "102.4 second loop" as 96 seconds. The
> prompt is kept as written because it is the record of what was commissioned; the build, the
> copy doc and the addendum carry the new numbers.

Drafted Nov 18, 2026 from Carlos's 12 item review of the v1.2 build. **Status: proposed.
Not approved. Nothing in `index.html` has been changed.**

This document is the improved version of the raw list. It does four things the raw list
could not:

1. Renumbers the 12 items (two of them were numbered 3 and two were numbered 4) and
   states a status for each.
2. Separates the three kinds of work that were mixed together: copy decisions, technical
   corrections, and open design questions that need your ruling before anything is built.
3. Carries the constraints the raw list did not mention, all of which collide with the
   requested changes: the byte identical path across scenes 2 and 3, the no text rule in
   those scenes, the matched pair across scenes 5 and 16, the layer rail geometry, and
   the 6.4 second loop.
4. Adds acceptance checks, so "does it now say what I asked" is answered by running a
   script rather than by watching a loop and guessing.

## 0. Your 12 items, mapped

| Yours | Task | Subject | Status |
|---|---|---|---|
| 1 | B1 | Scene 2 demand line becomes exponential | Ready |
| 2 | B2 | Scene 3 labels its three lines | Ready |
| 3 | B3 | "one provider" instead of "one cloud" | Ready |
| 4 | B4 | Scene 6 overlap, dot inside the line, router naming | Ready, depends on D8 |
| 5 | B5 | Scene 9 Distribute animation is technically wrong | Ready, depends on D2 |
| 6 | B6 | Replace "data never leaves your control" with guardrails | Ready, depends on D3 |
| 7 | B7 | Gemini prompt for the Deliver image | Ready, Appendix A |
| 8 | B8 | "Deliver" does not lower the price | Ready, depends on D4 |
| 9 | B9 | Replace the trillion dot wall with the Agentic AI icon | **Gated on an asset you must supply** |
| 10 | B10 | New support line for scene 1 | Ready, depends on D6 |
| 11 | B11 | Remove the floating dot on scene 4 | Ready |
| 12 | B12 | Alternative visual for scene 5 | **Gated on D7** |

Six are ready to build as written: B1, B2, B3, B7, B10, B11. Four carry a
recommendation you can veto in one word: B4, B5, B6, B8. One needs a file from you before
it can start: B9. One cannot start until you pick a direction: B12.

## 1. Decisions I need from you

Each has a recommendation. A one word veto on any of them is enough.

### D1. One word for the layer, and it is not router

Your ask: you want to go back to "router", but non technical people will not understand
the difference between router and gateway, so use something else.

**Recommendation: delete "router" from the screen completely and call the layer
Gateway.** Reason: scene 10's headline is already "Gate every request." If the layer is
called Gateway, the screenshot, the rail label and the headline all use the same word,
and the audience learns it in one glance because it appears twice on the same frame.
Nothing else needs explaining because nothing else is named.

| Candidate | Reads as | Cost |
|---|---|---|
| **Gateway** (recommended) | A door that inspects and admits | Still a technical word, but the most familiar one here |
| Front door | Plain, memorable, no jargon | Too colloquial for a rail of single nouns |
| Checkpoint | Inspection and permission | Suggests security only, loses the routing job |
| Switchboard | Routing, plain, charming | Dated metaphor, and the audience may not have seen one |
| Control point | Accurate for both jobs | Abstract, says nothing to a line of business visitor |

"Router" survives only in the talk track, where you can say the sentence out loud. It
never appears on the glass.

### D2. What Distribute actually shows

You are right on the technical point, and the current frame is wrong in two ways:
prefill and decode are phases inside a request, not two destinations a request is
divided between; and prefill happens before decode even when P/D disaggregation is in
use.

**Recommendation: drop the phase vocabulary from the screen and show the one thing
routing actually does, which is KV cache affinity.** The build already draws this: the
same request, three times, landing on the same accelerator because that accelerator
already holds its context, and one new request on a fresh accelerator that then becomes
its home. Delete both `prefill` and `decode` labels, put the fleet on one row so the
frame stops implying two paths, and add two events: a small ring pulse on the accelerator
each time a repeat lands (the cache hit), and a fill on the fresh accelerator the first
time the new request lands (now it holds one too).

Prefill, decode and disaggregation stay in the talk track, where you have 40 seconds to
explain them properly. No phase words on glass.

### D3. Guardrails, and a gate before it locks

You are right that "Data never leaves your control" is deterministic in a way we cannot
guarantee, especially with external model providers in the same path.

**Recommendation: scene 10 support becomes "Identity. Rate limits. Guardrails."** Three
parallel nouns, five words, same rhythm as the scene 5 triad, and it pitches the feature
instead of promising an absolute. Residency does not disappear from the story: scene 11
still says "Where your data lives. Sovereign to edge."

**Gate:** I searched the Red Hat AI messaging guide and it contains no "guardrail" claim.
Before this locks, confirm the hub language for the gateway's guardrail capability
(TrustyAI guardrails, or whatever the approved term is). If the hub cannot support it,
the fallback is "Identity. Rate limits. Policy." which is safe but weaker.

### D4. Deliver, and the sentence it sits under

Your ask is correct: scene 12 says "Five ways to lower it" and then lists Deliver, which
delivers a service rather than lowering a bill.

Two ways out, and one of them is much more expensive than it looks:

| Option | Change | Cost |
|---|---|---|
| **A (recommended)** | Scene 12 support becomes **"Five moves. One bill you control."** | One support line. The word "lower" survives where it is proven, on scene 14 with a credit |
| B | Replace the fifth verb Deliver with a cost verb | Scene 11's headline "Deliver AI as a service" has to change too, and that is the best line in the movement |

Option A keeps the honest price promise at the only place it has evidence behind it, and
puts "control" where the fifth layer actually delivers something: control of where
inference runs. It also chains cleanly: price on scene 1, price on scene 12, bill you
control on scene 12 support, your prices on scene 16.

### D5. Scene 13, the icon, and what carries the trillion

Two problems, one of them a hard blocker.

**Blocker:** the Agentic AI icon is not in this build. The icon folder holds ten files and
none of them is agentic. You need to drop the file into
`inference-booth-screen/assets/icons/`. **If the library offers it as SVG, send the SVG,
not the PNG.** Dots running through the icon's own red lines needs real path data; on a
flat PNG we can only approximate the lines, and approximated lines look wrong the moment
the dots drift off them.

**Decision:** if the dot wall goes, nothing on the frame quantifies "a trillion". That is
acceptable (the headline carries the number and the credit line carries the source, which
is how scene 9 already works), but it makes scene 13 the visually lightest scene in
movement 3. The mitigation is motion, not more objects: a dense, fast stream of dots
entering the icon's left ports and leaving its right ports, so the frame reads as high
throughput rather than as a logo.

Fallback if the icon cannot be sourced or reads thin on the panel: keep the 1,000 dot
wall, dim it to a field, and composite the icon over it. That is a hybrid, and it is
worth trying only if the icon alone looks empty at three meters.

### D6. The scene 1 support line

The constraint the raw list did not name: in this loop, scene 1 is the frame where the
brand is least present, and only scene 16 carries the logo. If the opener drops "From
Red Hat AI", a visitor who catches one frame cannot tell who made the screen.

| Option | Line | Words | Brand on frame |
|---|---|---|---|
| **A (recommended)** | Lower the cost of every token. From Red Hat AI. | 9 | Yes |
| B | Inference you own. Costs you control. | 6 | No |
| C | Here is how to lower it. From Red Hat AI. | 9 | Yes |

A answers the headline directly (price, then the response to price), names the brand, and
sets up scene 12 which asks how. C is punchier but reads as a question answered by a
slide, which is slightly weak for a first frame.

### D7. Scene 5, an alternative visual (gated)

You said the current visual works but does not read as a problem. It does not, and the
reason is specific: it shows a *dependency*, and dependencies are not visible until they
break. Nothing on the frame stops working.

| Option | What happens on screen | Reads as |
|---|---|---|
| **A (recommended)** | The three model boxes feed a funnel that becomes a single cord into the provider, with one latch on the cord. When the cord dims, the boxes dim and **their outbound dots stop**. The frame's only motion is the queue that is not moving | Dependency with consequences. You go quiet when they do |
| B | A tollgate: every token passes a meter that climbs while it waits behind a closed valve | Price, not lock in. Duplicates scenes 3 and 12, and does not explain "Their rules" |
| C | Keep the tethers and add the stopped outbound dots only | Cheapest change, smallest gain. Fixes the symptom, not the read |

A costs one new element (the funnel) and one new motion (dots that stop). It is the only
one of the three that makes the frame show a failure rather than state one.

### D8. Scene 6, the device, and the word Distribution

Two readings of your item 4 are possible and I want to be explicit about which one I am
building, because they need different fixes.

- **Reading 1, geometry:** the layer rail physically overlaps a diagram. I measured this
  in v1.2: the rail ends at 271px and the leftmost diagram edge is 485px, so at 1920 it
  cannot overlap.
- **Reading 2, vocabulary (what I believe you are seeing):** scene 6 puts its own three
  labels on the beam, Runtime, Router and Gateway, while the rail behind it lists five
  layers, Runtime, Optimization, Distribution, Gateway, Service. So "Router" lands where
  the rail says "Distribution", "Gateway" is the third thing on the beam but the fourth
  row in the rail, and the frame contradicts itself in the time it takes to read it.

**Recommendation: rebuild scene 6 as a bus, not a pipeline, and let the vocabulary
collide no more.**

- One thick conduit (12px rounded track) across the visual band, a red token moving
  inside it, not above it.
- Five stubs drop from the conduit, each ending in a hollow ring with its label beneath:
  Runtime, Optimization, Distribution, Gateway, Service.
- The token travels the conduit at constant speed and each ring fills and takes its label
  as the token arrives, in the order above, finishing just before the cut.
- The three beam labels Runtime, Router, Gateway are deleted with the beam. The vertical
  rail is not shown on scene 6 at all, so the same five names can never appear twice on
  one frame.

Two notes on this. A bus with stubs down reads as "these five are on the same line",
which avoids claiming a call sequence; a left to right arrow would claim the gateway is
the fourth thing a request reaches, which is false. And scenes 7 to 11 keep the vertical
rail unchanged: scene 6 shows all five at once, then the rail picks one at a time. That
is a deliberate two step teaching move, not a duplicate.

## 2. Build tasks

### B1. Scene 2, the demand line becomes exponential

Current path is concave down, so it reads as growth that is levelling off, which is the
opposite of compounding.

- New shape: near flat for the first third, then a sharp upward turn (hockey stick).
  Reference parametrization, in the 960 by 300 canvas: origin (40, 252), amplitude 200,
  curvature k = 4, end (780, 52).
- Scene 2 keeps no budget rule and no labels.
- The draw animation and the 6.4 second cycle are unchanged.
- Constraint that must survive: scenes 2 and 3 keep a byte identical `d` on the demand
  path. Both canvases widen to `0 0 960 300` together, so the plot keeps its exact screen
  position across the cut.

### B2. Scene 3, label the three lines

- Add three labels, no legend, no axis, no numbers, no units, no gridlines:
  **cost** (red), **budget** (gray), **demand** (ink).
- Budget rule moves from y 150 to y 170 so that the cost line crosses it at about x 420
  and the demand line crosses it at about x 620. Sequence must read cost first, demand
  second.
- Labels at 26px in the existing `.col-label` style. Placement rule: each label within 20
  units of its own line, no label sitting on another line, and at least 40 units between
  any two label baselines. The build places them; the geometry decides whether they sit
  at the right end in a gutter or above their line at 60 percent of the width.
- Scene 3 gains exactly three `<text>` elements. Scene 2 gains none.

**Why this is not a violation of the "no numbers in 2 and 3" rule:** the rule exists so
the chart does not become an unsourced statistic. Three nouns do not create a statistic
and need no credit. The validator check changes from "zero text" to "zero numbers, zero
units, zero axis, zero gridlines, exactly three approved label strings in scene 3 and
zero in scene 2".

### B3. Scene 5, one provider

- Headline: **Inference chained to one provider.**
- Support unchanged: Their models. Their prices. Their rules.
- The matched pair with scene 16 stays intact.
- No change to the visual in this task. The visual is D7.

Note in your favour: "provider" also fixes the AWS relationship problem, because a cloud
provider and a model provider are both in scope, and the frame stops pointing at one
vendor. It also rhymes with the closer, where the reader becomes a provider themselves.

### B4. Scene 6, rebuild

As specified in D8. Delete the beam, its three labels and its dot; add the conduit, five
stubs, five rings, five labels and the travelling token. Keep the BG-02 substrate at 0.22.
Keep the support line "One request. One path. Five layers." Its words now describe exactly
what the frame shows, which they did not before.

Also delete the word Router from the file entirely, comments included, so it cannot come
back by accident.

### B5. Scene 9, Distribute, corrected

- Delete the `prefill` and `decode` labels and the two row layout that implies a split.
- One row of accelerators.
- Keep: the same marker returning to the same accelerator three times per cycle, one dim
  background dot per accelerator, no cache rates, no percentages.
- Add: a ring pulse on the accelerator at each repeat (the cache hit), and a one time fill
  on the fresh accelerator that receives the new marker (it now holds a cache too).
- Nothing on this frame may say prefill, decode, phase, or stage.

### B6. Scene 10, guardrails

- Support becomes: **Identity. Rate limits. Guardrails.**
- Requires the D3 verification first. If the hub does not support guardrails, ship
  "Identity. Rate limits. Policy." instead and say so in the addendum.
- The phrase "Data never leaves your control" must be gone from the file, comments
  included.

### B7. Gemini image prompt

Appendix A. It is ready to paste. One warning is inside it: a baked in beam costs you the
scene 11 parallax, so the recommended variant generates ground and structures only.

### B8. Scene 12, the fifth move

As specified in D4: support becomes **"Five moves. One bill you control."** Beat words,
timing and drift unchanged. Scene 11 keeps Deliver.

### B9. Scene 13, the icon (gated)

- Asset: `assets/icons/agentic-ai-<n>.svg` if the library has it, PNG otherwise. You
  supply it.
- Replace the 1,000 dot wall with the icon, centred, at roughly 340px.
- Dots: dense, fast, entering the icon's left side and leaving its right side. On an SVG,
  ride the icon's own paths. On a PNG, run the stream along the icon's visual axis and
  keep it outside the artwork so it never looks like it is missing the lines.
- Colour: the dots cannot be red on red. Ink or white, or red only where the icon's own
  lines are not.
- Delete the `token-thread` block; the exiting stream is the thread now.
- Keep the 1,000 dot density as the fallback only (D5).

### B10. Scene 1, opener line

As specified in D6, recommended: **Lower the cost of every token. From Red Hat AI.**

### B11. Scene 4, remove the floating dot

- Delete the `reach-dot` circle and the `.reach-dot` CSS rule.
- Keep the three hollow denial rings.
- Honest note: that dot was the only element saying "the work cannot reach the idle
  capacity". With it gone, the frame says "GPUs are unevenly loaded" and stops short of
  "and that is why you are stuck". If that matters when you see it, the cheap fix is a
  single dashed stub from the pegged accelerator toward a cold one that fades before it
  arrives. Not included here, because you asked for the dot gone.

### B12. Scene 5 visual (gated on D7)

As specified in D7 option A, if you pick it: funnel, one cord, one latch, and outbound
dots that stop when the cord dims.

## 3. Documents and validator, same pass

Not optional. Three of these changes move scene content, so the machine checked copy
tables have to move with them or the checks fail with no obvious cause.

| File | Change |
|---|---|
| `tools/validate.py` | `EXPECTED_HEADLINES[5]`, `EXPECTED_SUPPORTS[1]`, `[10]`, `[12]`; relax the scene 2 and 3 text check; add the new checks in section 5 |
| `2026-11-inference-booth-screen-copy-v1.md` | bump to v1.3, new rows, add the router and prefill/decode rejections to the rejected list |
| `inference-booth-screen/addendum.md` | v1.3 entry: what changed, what was deliberately not done, what is unverified |
| `assets/gen/README.md` | only if Appendix A produces an image |

## 4. Do not change

Buried in the raw list, none of these were mentioned, and all of them are easy to break
while doing the above.

1. The 6.4 second scene rhythm and the 102.4 second loop.
2. The matched pair: scene 5 support and scene 16 support, set identically or the
   inversion stops working.
3. Scene 16, the closer. Not in the list. Hands off.
4. The spine order Run, Optimize, Distribute, Gate, Deliver, and its scenes 7, 8, 9, 10,
   11.
5. Every credit line, and the rule that every stat carries one.
6. Zero em and en dashes, everywhere, including comments.
7. No third party names, logos, or model names on glass.
8. One calm continuous animation per scene, nothing static at the end of a scene.
9. The upper 40 percent of any art stays empty.
10. Zero network requests.

## 5. Acceptance checks

Add to `tools/validate.py` and require all to pass before sync.

| # | Check |
|---|---|
| V1 | 16 of 16 scene copy checks pass with the new strings |
| V2 | Scenes 2 and 3 have the same viewBox and a byte identical demand path |
| V3 | The demand path is monotone and accelerating: slope over its last tenth is at least 5 times the slope over its first tenth |
| V4 | Scene 3 has exactly three `<text>` elements, strings cost, budget, demand, and no digits, no units |
| V5 | The cost line crosses the budget rule left of where the demand line crosses it, and both crossings fall between x 300 and x 700 |
| V6 | The word router appears zero times in the file |
| V7 | The words prefill and decode appear zero times in the file |
| V8 | The phrase data never leaves your control appears zero times in the file |
| V9 | `.reach-dot` appears zero times in the file |
| V10 | Scene 6 contains no `<text>` outside its five layer labels, and its five labels are exactly the five rail labels in the same order |
| V11 | Scene 12 support is the approved v1.3 string |
| V12 | If B9 ships: the referenced icon file exists on disk and scene 13 sums to zero `ctrl-dot` circles |
| V13 | Every referenced asset is local, zero network, zero em and en dashes |
| V14 | JS parses under `node --check` |

## 6. Prerequisites

| Item | Owner | Blocks |
|---|---|---|
| Agentic AI icon file, SVG preferred | Carlos | B9 |
| Guardrail claim confirmed against the hub | Carlos, or build flags it | B6 |
| D7 choice for scene 5 | Carlos | B12 |
| Confirmation that reading 2 is what you meant by overlap | Carlos | nothing, it is already built into B4 |

## Appendix A. Gemini prompt for the Deliver image

Two variants. Read the warning between them first.

### Warning

Scene 11's idea is parallax: four environments on four depth planes, each drifting at a
different rate, which is what sells distance without a map. If the image contains the
environments and the beam, that idea is gone, because a single flat image cannot parallax
against itself. You get one artwork with a slow breathe instead.

So: **variant 1 (recommended)** generates ground and structures with no beam, and the
build keeps the red beam, the four icons and the parallax. **Variant 2** generates the
whole frame as one illustration, and you accept that scene 11 becomes a still with a
drift.

### Variant 1, ground and structures only (recommended)

```
A wide, very clean background illustration for a large presentation screen. 16:9,
3840 by 2160, no text anywhere.

Scene: a low horizon seen at eye level, white ground fading to white sky, no visible
horizon line. Four structures stand on one horizontal axis, receding from near left to
far right, each one smaller, softer in contrast and slightly hazier than the one before,
so the frame reads as depth rather than as a lineup.

1. Near left: a compact server rack, matte off white, fine gray panel lines, sitting on
   a slim dark gray base.
2. Middle: a soft cloud form built from three overlapping matte shapes, floating just
   above the ground, no face, no weather symbol.
3. Further: a solid cube with fine concentric seams cut into its faces, like a sealed
   vault, crisp edges, no lock, no keyhole.
4. Far right: a small handheld device, a flat rounded rectangle on a short slim post.

Style: matte 3D, soft even light from above, gentle contact shadows only, no reflections,
no gloss, no depth of field, no grain, no vignette, no wireframe, no blueprint lines.
Palette: white, warm pale gray, mid gray, and nothing else. No red, no blue, no purple,
no neon, no glow.

Composition: the four structures sit in the lower 55 percent of the frame. The upper 40
percent is empty white, reserved for text. Keep the outer 8 percent of the frame clear of
anything important.

Negative: text, letters, numbers, logos, brand marks, watermarks, user interface, charts,
arrows, world map, globe, country outlines, flags, people, hands, dark background, lens
flare, bloom, bokeh.
```

### Variant 2, the whole frame including the beam

Take variant 1 and replace the style and palette paragraphs with this:

```
Palette: white, warm pale gray, mid gray, and exactly one saturated red close to #EE0000.
That red is used for a single element only.

One thin straight red line runs at a constant height across the whole width, from the
left edge to the right edge. It passes behind the server rack, in front of the cloud
form, behind the cube and in front of the handheld device, threading through all four.
The line is flat and even, unbroken, with no glow, no bloom, no taper, and no arrowhead.
```

### If Gemini misbehaves

- Text creeping in: add "no text, no letters, no numbers, the red line is unbroken".
- The beam broken between objects: add "one continuous unbroken line at one constant
  height, never interrupted".
- Too dark or too 3D rendered: add "flat matte lighting, white background, soft shadows,
  product photography on white".
- Ask for four variations and pick, rather than iterating one image.

### Wiring, if you use one

Drop the file at `inference-booth-screen/assets/gen/scene11-horizon.png`.

- Variant 1: keep the SVG beam and the four icon images. Set the image to
  `object-fit: cover`, opacity 0.55, and keep `art-drift`.
- Variant 2: delete the SVG beam `<line>` and the four `<image>` icons from scene 11, keep
  the type and the `.scene.spine` padding, set opacity 0.85, and keep `art-drift` as the
  scene's single motion.
- Either way, update `assets/gen/README.md` with source file, scene, opacity.

## Appendix B. What the raw list left open

Recorded so nothing looks dropped later.

| Raw item | What was missing | Resolution |
|---|---|---|
| All 12 | Two numbered 3, two numbered 4 | Renumbered B1 to B12, mapped in section 0 |
| 1 | No statement of what "exponential" should look like, and no note that the shape must stay identical on scene 3 | B1 gives the shape, the reference numbers and the identical path constraint |
| 2 | Which scenes get labels; whether a legend or inline; that labels break the existing no text validator rule | B2 scopes to scene 3, inline, and rewrites the check |
| 3 | The visual still shows a cloud; whether the cloud should stay | Cloud stays, the word is what changes |
| 4 | Three different asks in one item: a bug, a design proposal, an open naming question | Split into D1, D8 and B4 |
| 4 | "go back to router" and "use something else" contradict each other | Resolved to neither, D1 |
| 5 | No statement of what replaces the split | D2 and B5 |
| 6 | No note that the removed claim has to reappear somewhere | Residency stays on scene 11 |
| 6 | Untested product claim | Gate in D3 |
| 7 | No size, palette, safe area or beam constraint, so the asset would arrive unusable | Appendix A |
| 8 | No note that changing the verb costs scene 11's headline | D4 option A changes the support instead |
| 9 | No asset in the build, and no plan for the quantification that leaves with the wall | Blocker plus D5 |
| 10 | No note that the brand disappears from the opener | D6 |
| 11 | No note that the removed dot was carrying the causal claim | Flagged in B11 |
| 12 | Cannot be built until a direction is chosen | Gated, D7 |

Deliberately not included, because you did not ask: no change to scenes 7, 8, 11 or 16;
no change to the layer rail; no change to the loop timing; no new icons.
