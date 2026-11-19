# Inference Booth Screen: Addendum

## v1.3.6, Nov 19, 2026 (scene 7 dots ride the spokes)

**Change class:** one scene's motion rebuilt, one output group added, validator gains V15. No
copy changed, no scene added or removed, no timing changed anywhere else.

**The bug.** Carlos noticed the dots on scene 7 were not on the connector lines. They were
worse than off the lines. Each dot ran a single translate from `(140, sy)` to `(780, 190)`,
which is a shallower angle than any spoke, so:

| at x | dot y | its own spoke |
|---|---|---|
| 430, box left edge | 117 | 190 |
| 600, box right edge | 152 | 190 |
| 780, convergence | 190 | 180 units past the node |

The top stream ran 73 units above its line, every stream crossed the face of the box instead
of entering it, and the convergence of all five happened to the right of the node at the
moment opacity hit zero. The scene asserted "five inputs, one runtime" in words and showed
five unrelated streaks.

**The fix, in geometry**

| | before | now |
|---|---|---|
| Dot start | `(140, sy)` | `(132, sy)`, the right edge of the icon column |
| Dot end | `(780, 190)`, outside the node | `(430, 190)`, the node's left edge, where they are consumed |
| Speed | 246 units per second | **480**, the speed Distribute and Gate run at |
| Leg time | 2.6s for 640 units | 0.62 to 0.68s for 298 to 327 units |
| Dots on frame | 15, drifting | 15 in, 3 out, on five rails that are never empty |
| Exit | implied, after the fade | one stream of three leaves the right edge, 156 units |

Three dots per spoke, spaced a third of a leg apart, each spoke starting 0.11 seconds after the
one above it so the five trains never pulse in unison. The single output stream runs at the
same 480, so the box is neither a sink nor a pass-through that ignores its contents.

**Why the exit stream exists.** With the dots consumed at the left edge, a node that emits
nothing reads as a wall, and the "and out the other side" half of the sentence disappears. One
short stream keeps the causal chain complete without adding a second motion language: it is
the same dot, the same speed, the same direction.

**Rejected, with the reason.** A no-spokes variant was built and compared side by side
(`preview/scene7-variants.html`), where the five converging dot trains are the only connection
drawn. It is the more distinctive frame and the weaker read at 3 metres: five unanchored trains
in a 6.4 second cut were judged more likely to look like scattered motion than like one input
per icon. The preview file stays as the record; it is not published with the repo.

**Verified, not assumed.** The init block was executed against a stub DOM and every generated
circle inspected: all fifteen input dots land on `(430, 190)` to within 0.01 units, all run at
480 units per second to within 0.6, durations come out 0.621, 0.636 and 0.681 seconds, and all
three output dots land on `(760, 190)`.

**Validator.** New check V15 locks the six engine constants, asserts the five spokes still run
from x 132 to x 430 at y 190 with their icon y values, asserts the output group exists, and
asserts the retired `--dx:640px` diagonal is gone. 31 of 31 pass, `node --check` clean.

**Still unverified.** The convergence at the box's left edge carries two or three dots at a
time. If it reads as a jam rather than as delivery, the fix is two dots per spoke instead of
three, which thins arrivals by a third without changing any speed.

---

## v1.3.5, Nov 19, 2026 (the mantra scene is deleted, 16 scenes become 15)

**Change class:** one scene removed, four scenes renumbered, one CSS block removed, loop
duration changed, validator retargeted. No copy changed on any surviving scene.

Carlos cut the whole frame, not the line above it: "delete the entire scene. I want Deliver
AI as a Service to jump directly to A trillion tokens a month."

**Numbering, old to new**

| old | new | scene |
|---|---|---|
| 11 | 11 | Deliver AI as a service. (unchanged) |
| 12 | gone | Mantra: five verbs standing alone |
| 13 | 12 | A trillion tokens a month. |
| 14 | 13 | Up to 70% lower token costs. |
| 15 | 14 | 233% ROI over three years. |
| 16 | 15 | Become an AI model provider. |

Loop goes from 102.4 seconds to **96 seconds**. `TOTAL_SCENES` 16 to 15, `LOOP_INTERVAL`
unchanged at 6400.

**Why the scene went.** It was a summary of the five spine scenes, placed after the five
spine scenes. A visitor who watched 7 to 11 had just been given the five verbs one at a time
with evidence attached to each; a visitor who arrived on 12 had no reason to care about a
list with the evidence removed. Either way the frame did no work, and it sat between the last
claim and the first piece of proof. Nothing was moved into another scene: the rail already
names the five verbs across 7 to 11 and scene 6 already says "One request. One path. Five
layers." A third recital would be the same content three times.

**What was removed**

- The scene block, the five verbs, the five nodes on their rule, the node pop, the node
  pulse, the beat stagger from 0.3s to 3.5s, and the mantra drift keyframes. Zero references
  to any of them remain in the file.
- The validator's copy tables and credits map, retargeted to fifteen scenes.

**What was deliberately not removed**

- **The engine's scene 13 names.** `s13-river`, `s13-loop`, `S13_SPEED`, `restartScene13` all
  still carry 13, and the trillion scene is now scene 12 at index 11. Renaming them buys
  nothing a visitor can see and risks a silent break in a 900 line script, so the code
  carries a comment explaining the history instead. The restart hook moved from `i === 12` to
  `i === 11`.
- **The old numbers in earlier addendum entries and in the decisions log.** Those are a
  chronological record, so they keep the numbers the scenes had when they were written. The
  decisions log now opens with a numbering note that says so.

**Validator.** Check 1 is fifteen scenes with ids 1 to 15. Check 4c is inverted: it now
asserts the mantra markup and classes are entirely absent, so the deletion cannot be undone
by a stray copy and paste. Check 4d is retired with the scene it guarded. Check 6 reports
fifteen headlines and fifteen supports word for word. V11 is rewritten as an adjacency test:
scene 11 must be the Deliver headline and scene 12 must be the trillion, with no mantra in
either block, so a future insert cannot quietly put a beat back between them. X3 is 15 x
6.4s = 96s. X4 points at scene 12. **30 of 30 pass**, `node --check` clean, 27 infinite
animation rules, zero network, zero dashes.

**One thing to watch.** Deliver now cuts straight into a dense, fast, high-contrast animation
(the lanes and the panel). That is a hard edit from a still horizon to a moving machine, and
it should feel like a gear change rather than a glitch. If it reads as a jolt at kiosk size,
the fix is not to restore a scene but to give the trillion frame a 0.45s fade up on its first
cut, which the existing scene transition already supports.

---

## v1.3.4, Nov 19, 2026 (scene 12 goes silent)

**Change class:** scene 12 copy removed, one inline height changed, validator gains check 4d
and V11 rewritten. No other scene touched.

Carlos cut the headline and the support from the mantra: "not necessary and in the way of the
evidence." Removed:

- h1 "Every token has a price."
- support "Five moves. One bill you control."

Kept, unchanged: the five verbs, their 0.3s stagger from 0.3s to 3.5s, the mantra drift, and
the five nodes pulsing on the same beats from the same rule. The scene is now a rule, five
dots lighting in order, and five words landing with them. The order is shown rather than
asserted, which is what the cut asked for.

**Layout.** The text block's min-height goes from 30vh to 34vh so five words hold the optical
centre of the frame without a headline over them. Nothing else moved.

**Two consequences worth naming.**

1. "Every token has a price." now appears nowhere on glass. The price frame is carried by
   scene 3 ("The bill outgrows the budget.") and proven on scene 14 ("Up to 70% lower token
   costs"). That is a defensible place for it, but it does mean the loop no longer states the
   price promise as a proposition.
2. The word "five" leaves the glass. Scene 6 still names the five layers, so the count is not
   lost, but scene 12 no longer supplies a second count.

**Validator.** New check 4d asserts scene 12 has no h1, no support, and no substitute text,
and that neither retired string survives anywhere in the file. V11 is reversed from "carries
the approved string" to "carries no headline and no support". Expected copy tables now hold
empty strings for scene 12, so check 6 reports 30 lines word for word with scene 12 blank by
design rather than silently tolerating a gap. 31 of 31 pass, `node --check` clean.

**Still unverified.** Whether five words alone hold a six second frame at 3 m, or whether the
scene now reads as a pause rather than as a statement. If it feels empty, the lighter fix is
not to bring the h1 back but to raise the mantra size one step, from 3.4vw to 3.8vw.

---

## v1.3.3, Nov 19, 2026 (gate speed, and scene 13 becomes a live rate)

**Change class:** scene 10 timing and density, scene 13 rebuilt from a still into a drawn
animation, validator X4 and V12 rewritten. No copy changed on either scene.

### Scene 10, the gate now moves at 480

Carlos's read was that the gate felt slower than Distribute even after the last pass. He was
right, and the measurement says why: the previous build matched scene 9's *background*
traffic, which is four grey dots at 168 to 276 units per second and which nobody tracks. The
markers a visitor actually follows on Distribute are the red ones at 720 units in 1.5s, which
is 480 units per second.

| | before | now |
|---|---|---|
| Pass speed | 640px in 2.5s, 256 units per second | 640px in 1.33s, 480 units per second |
| Stop speed to the gate | 390px in 1.56s, 250 units per second | 390px in 0.81s, 480 units per second |
| Dots on the frame | 8, 5 passing and 3 stopped, 0.8s stagger | 14, 10 passing and 4 stopped, 0.42s stagger |
| Order | all five passes first, then the three stops | interleaved through the whole cycle |

Nothing decelerates before the gate, and nothing after it: a stop is a state change to a
hollow ring, not a slowdown. The staggered interleave also means the gate is never in a
single state, which is what it looked like before at 8 dots.

### Scene 13, a still becomes a rate

The generated render was a good object and a bad argument: it showed a mass, and the sentence
is about a rate. The scene is now a live SVG on one rAF clock, left to right:

1. **Seven lanes of tokens**, 70 on screen, converging at 520 units per second. This is the
   fastest sustained motion in the whole loop, on purpose: "moving quickly" is half of what
   the scene has to say.
2. **A ghost field of 96 dots** behind the lanes, r 1.8 at 0.2 opacity, 380 to 900 units per
   second, scattered by arithmetic rather than by randomness so every load and every loop is
   the identical frame. The lanes are the tokens you can count; the field is the ones you
   cannot. Seventy dots cannot say trillion, a countable stream over an uncountable field can.
3. **A three node agent loop** at (372, 170): a static red ring, a red arc rotating once per
   3.2s, and three nodes pulsing in sequence. Three agents, not one box, and the pulse order
   is work moving between them.
4. **A panel the loop writes**, fifteen code lines at 93ms each, then a 305ms hold, then a red
   commit rule sweeps across in 160ms and sits under the code for 120ms, then code and rule
   fade together. Three panels per cut, six per loop.

Every token is consumed at x 500, immediately left of the panel, so nothing exits the frame
and the stream reads as input being spent.

**Phase reset.** The panel cycle restarts at the cut, like scene 5's outro, so the first line
and the last commit always land inside the scene even after an operator uses the arrow keys.

**Why the fade and not a cut.** The first build cleared the panel instantly between panels.
At kiosk scale that reads as a dropped frame, so the clear is now a 153ms fade of the code
group and the commit rule together. A functional simulation over 420 frames confirms the
order: line one at the cut, panel complete at 1.4s, rule sweeping from 1.7s, full rule under
full code at 1.9s, both fading from 1.98s, next panel at 2.13s.

**Retired but kept.** `assets/gen/scene13-river.png` is still on disk and the revert is one
img tag plus one engine block. The render is stronger as an image and weaker as an argument.

**Validator.** X4 now asserts the four animated parts exist and that the still is no longer
referenced in the document (while still present on disk). V12 asserts the engine constants:
520 units per second, three panels per cut, a restart hook, and no randomness anywhere. 30 of
30 pass, `node --check` clean, 28 infinite animation rules.

**Still unverified.** The whole frame at panel size: whether 70 tokens plus 96 ghosts reads as
abundance rather than as clutter, whether the code panel reads as software at 3 m or as a
grey barcode, and whether a white panel outlined in gray-40 holds the right half of the
frame. The three most likely fixes, in order: drop the ghost field to 60, thin the code
bars from 7 to 6, or darken the panel border to ink at 0.35.

---

## v1.3.2, Nov 19, 2026 (one line, one crossing)

**Change class:** scenes 2 and 3 markup, two CSS rules retired, validator V2 to V5, copy doc
table. No other scene touched.

Carlos ruled that the bill outgrowing the budget is the whole argument, and that two lines
with two crossings made the visitor compare instead of read. So the red cost line, its dot
and its label are gone, and the surviving exponential line is now labelled "cost". Same path,
byte for byte, in both scenes.

**Copy**
- Scene 2 headline: "AI demand and cost are compounding." (6 words, his line with the verb
  agreement fixed).
- Scene 3 headline and support unchanged: "The bill outgrows the budget." / "Costs climb
  unpredictably as usage scales."
- Labels on scene 3: "cost" at (790, 74) and "budget" at (790, 160). Two, not three.

**Motion.** Removing the second line left scene 3 with no animation, which would have made it
a six second still. Scene 3 now carries the same draw as scene 2. Both run the same 6.4s
period, and a scene lasts exactly one period, so their phases are identical and the loop
reset lands on the cut rather than mid-scene. The line traces, crosses the rule late and
holds. Two infinite animation rules retired (`draw-b`, `dot-in-b`), so the count goes from 29
to 27.

**Declined.** A grey or red ring at the crossing (627, 170) to mark the money moment. It was
offered and not taken; the frame has a rule and a line, and a marker reads as an alert.

**Validator.** V2 now says "cost path". V3 unchanged and still measures 39.6x acceleration.
V4 now expects two labels. V5 was rewritten from "cost crosses left of demand" to: exactly
one path in scene 3, `line-b` fully retired, one crossing inside x 500 to 700. 30 of 30 pass,
`node --check` clean.

**Copy doc drift fixed in the same pass.** The doc's scene table still carried the v1.0 scene
1 line ("Every token has a price." / "The inference story. From Red Hat AI.") while the locked
decisions section and the build both had v1.3's "Inference worth scaling." / "Models you own.
Costs you control." The build was right and the table was stale; the table now matches the
build. Worth knowing that this is the second time the table drifted while the locked section
moved, so the table is the thing to re-read before a copy review, not the build.

**Still unverified.** The single crossing at panel size: does the line read as clearly over
the rule at 3 m, or does the flat rule get lost at 3 to 4 percent grey? If it gets lost, the
one fix is a slightly darker rule, not a marker.

---

## v1.3.1, Nov 19, 2026 (scene 13 art swap)

**Change class:** one asset, one scene, one validator check. No copy changed.

Scene 13's Agentic AI icon is retired and the frame now carries a generated river render,
`assets/gen/scene13-river.png`, 2730 by 1536. Beads pour in from the left, funnel through
a red lattice, and come out as software.

Two candidates were generated: a flat line art version and a rendered version. The flat
one is the better illustration and the worse screen element. In the visual band the art is
displayed at roughly 0.37x of source, which takes its 1.5px dots to 0.55px and its 2px
panel hairlines to 0.7px, so both fall below a pixel and alias into a pink wash. Its right
cluster has a median luminance of 255, so the half of the image that carries "agentic
SDLC" would have vanished at 3 m. The render's beads are 14 to 18px at source and land at
5 to 6px, so the mass holds as material rather than as texture. That is the whole reason
for the swap: not taste, scale.

**Placement.** Visual band, full opacity, never dimmed, max width 1000px with the box
capped to the band height and `object-fit: contain` so it cannot overflow into the text
block on a shorter panel. Not full bleed: at full bleed the band sits at 36 to 67 percent
of the frame and runs into the top of the text block at about 63 percent.

**Motion.** The masked flow is gone, so the frame's one continuous animation is now a 14
second pan and breathe, scale 1.02 to 1.05 with a plus or minus 6px drift in the direction
the river already runs. The 1.02 floor is what keeps an edge from showing.

**Validator.** X4 now checks the render instead of the icon, and V12 checks that the dot
wall is gone and the icon reference is fully retired. 30 of 30 pass, `node --check` clean.

**Known soft spot.** The panel faces measure 223 on a 255 ground, about 1.2 to 1, so the
slabs separate only through their shadow seams. It was judged not worth another render.
If it reads as a pale heap on the panel, the one line fix in the prompt is to darken the
panel faces about 15 percent or give each slab a thin gray edge.

**Still unverified.** The whole image at panel size: does the lattice read as a process,
and do the slabs read as software, or as a pile of boxes?

---

## v1.3, Nov 19, 2026 (eleven scene rulings, the rail, the validator)

**Change class:** four copy lines, one new opener lockup, seven scene rebuilds, the
layer rail re-lettered, scene 13 re-arted, and fifteen new validator checks. Copy doc
v1.3 governs word for word. Every ruling came from
`2026-11-inference-booth-screen-decisions.md`; nothing here re-opens a decision.

### Copy

| Scene | Was | Now |
|---|---|---|
| 1 headline | Every token has a price. | Inference worth scaling. |
| 1 support | The inference story. From Red Hat AI. | Models you own. Costs you control. |
| 5 headline | Inference chained to one cloud. | Inference chained to one provider. |
| 10 support | Identity. Rate limits. Data never leaves your control. | Identity. Rate limits. Guardrails. |
| 12 support | Five ways to lower it. | Five moves. One bill you control. |

Scene 1 and scene 16 are now a visual bookend: the same logo lockup above the headline
in the same `.visual` band, so the opener and the closer rhyme and the brand sits in the
same place twice per loop. The price frame survives once, at scene 12, where the five
moves explain it.

### The rail

Run, Optimize, Distribute, Gate, Deliver. One verb per spine scene, matching the red
verb in the headline beside it. It is hidden on scene 6, which shows all five names on
its own canal; two sets of the same five words in one frame would read as a mistake. For
the same reason scene 6's own node label was not "Runtime": the canal names actions, not
components. Scene 7 keeps its inline red "Runtime" label under the transit node while the
rail beside it reads Run, because there the frame is naming the component and the rail is
naming the action. That pairing is on the record as accepted, not overlooked.

### Scene rebuilds

1. **Scene 2 and 3, one curve.** Demand is exponential (`(e^4u - 1)/(e^4 - 1)`), plotted
   on a single baseline, byte identical across both scenes. The budget rule is flat at
   y 170. Cost crosses it at x 430, demand at x 627, so the money breaks the plan before
   the wave does. Three labels in scene 3 (cost, budget, demand), one in scene 2. No
   axis, no units, no gridlines, no digits.
2. **Scene 4, refusal as a consequence.** The three deny rings and the probe are gone.
   Two requests per cycle descend into the pegged accelerator, become an expanding gray
   ring for 0.6s, then rebound up and right, fading about 40 percent of the way to cold
   capacity they never reach. Red is the request, gray is the refusal, the fade is the
   point, and no word states it.
3. **Scene 5, the cloud is the container.** Three model boxes, three tethers and the
   pulse are gone. One 320px brand cloud at x 115, three 42px models standing inside it
   at y 196, three consumer pills at x 780, routes from the cloud edge to each pill.
   Tokens run at full speed to 3.2s, decelerate linearly to a dead stop at 5.0s, the
   provider and its models fade to 12 percent, and from 4.4s the three consumers turn
   red and throb. Nothing recovers inside the cycle: it ends on the outage.
4. **Scene 6, one canal, five stations.** The beam, the three nodes and the word Router
   are gone. A 12px canal with five stations; an ink token runs it and each station fills
   as it arrives and stays filled, so the frame ends on a full pipeline, which is what
   scene 7 inherits.
5. **Scene 9, cache affinity.** Prefill and decode are gone and the fleet is one row of
   four. The same marker returns to the same accelerator three times, 2.2s apart, and
   each arrival fires a ring pulse, which is the cache hit. One square marker adopts an
   accelerator with no cache and that outline fills faintly for the rest of the cycle.
   No percentages, no phase words.
6. **Scene 11, the deck's four environments.** The datacenter, the globe, the long beam
   and the vertical drop lines are gone. Four customer deck icons in support line order
   (sovereign 64, private 56, public 48, edge 40) on a red rule under each, captions in
   ink at 24px, parallax 14/10/7/4px on 9/11/14/17s, ridge at 0.70, caption halo off,
   icon glow on. The glow exists only because the ridge went up: it keeps thin red line
   art legible on a photograph.
7. **Scene 13, the icon replaces the wall.** The 1,000-dot wall, its column animations
   and the token thread are gone. `.agentic-ai-400.png` carries the frame and a field of
   ink dots is masked to the icon's own red strokes, so the flow runs inside the lines
   with no path tracing and no drift off the artwork. Alpha mask, not luminance: the
   artwork is red and a luminance mask would render the flow at about a fifth strength.

### Phase alignment

Scenes 4, 6 and 9 carry `.replay` on their generated or repeated elements, so their 6.4
second sequences restart when the frame is entered rather than when the page loaded.
Scene 5 resets its request clock through `restartScene5()` inside `showScene`. Without
this, an operator who used the arrow keys would leave a refusal, a fill, a cache hit or
the outage landing on the wrong scene, which is the one failure mode a booth screen
cannot hide.

### Validator

`tools/validate.py` now runs 30 checks, all clear: the original 16, V2 to V14 from the
v1.3 prompt, and X4 rewritten from the retired dot wall to the icon plus alpha mask. The
new checks parse the curve rather than trusting it: same viewBox and byte identical
demand path across scenes 2 and 3, monotone and accelerating (measured 39.6x, floor 5x),
both crossings between x 300 and x 700 with cost left of demand, exactly three labels in
scene 3 with no digits or units, zero hits for router, prefill, decode, the residency
phrase and `.reach-dot`, scene 6 naming exactly the five rail verbs in order, scene 12's
new support string, the icon on disk with zero dot wall remnants, zero network, zero
dashes, and `node --check` on the extracted script.

### Deviations from the change request, and why

1. **Scene 11 captions are 24px ink everywhere, including "Edge".** The decision fixed
   size differences in the icons only. Uniform captions keep the four names reading as
   one list; the icon sizes alone carry the depth cue.
2. **Scene 5 pills are 155px wide, not fitted to text.** One width makes the three
   consumers read as one class of thing, and the shortest label ("Apps") is what set the
   minimum.
3. **Scene 9 keeps one dim background dot per accelerator.** Removing them made the
   frame end empty while the marked requests were between hops. They are gray, 4px, and
   slower than the marked traffic, so they do not compete.
4. **Scene 13's flow dots are ink, not red.** The icon is the only red object on the
   frame, and red dots inside red lines would have erased the line work.
5. **The demand label moved from (500, 196) to (790, 74).** Measured in the actual font,
   "demand" is 94.7px wide at 26px. Over that span the exponential tail climbs about
   30px, so the ruled position left the curve crossing the last letter by roughly 15px,
   with under 11px of clearance between the budget rule and the curve. The label now
   sits level with its own endpoint dot, in the same right hand gutter as budget
   (790, 160) and cost (790, 44), so all three labels share one column. Same three
   labels, same attachment, no collision. Recorded in the decisions file as a build note.

### Still unverified

No headless browser on this machine, so validation is static. Needs eyes on the panel:

- Scene 1: does the logo lockup plus headline fit without crowding the hero art?
- Scene 3: is the cost crossing at x 430 legible before demand crosses at x 627?
- Scene 5: do the three 42px models read as inside the cloud, or on top of its edge?
- Scene 5: does the 12 percent provider fade read as an outage, and do the pills throb
  enough without looking like an error dialog?
- Scene 6: do the filled stations read as progress, or as five red discs?
- Scene 9: does the ring pulse read as a cache hit, or as a click?
- Scene 11: do the deck icons hold up at 0.70 on the photograph, and is the white glow
  visible without haloing?
- Scene 13: does the masked flow read as movement inside the icon, or as noise?
- Scene 16: unchanged logo lockup, still unverified for balance against scene 1.

### Still open

- "Guardrails" has zero hits in the Red Hat AI Messaging Guide. Scene 10 ships on the
  approved term if the hub confirms it; the fallback is "Identity. Rate limits. Policy."
- Rail says Gate, the governance screen says Gateway. On the record, no change made.
- Two hub facts cited in the talk hit their review date on Nov 20 and 21 (OpenShell
  timeline, gateway naming map) and need re-verification after GA day, Nov 18.
- The external stat slot at scenes 2 and 3 is still open by design.

---

## v1.2, Nov 18, 2026 (copy, proof order, seven visuals)

**Change class:** five copy lines across four scenes, one scene reorder, seven visual
rebuilds, one layout fix across six scenes, one art move. Copy doc v1.2 governs word
for word; `tools/validate.py` updated in the same pass.

### Copy

| Scene | Was | Now |
|---|---|---|
| 5 support | Their models. Their hardware. Their rules. | Their models. Their prices. Their rules. |
| 6 support | Runtime to router to gateway. | One request. One path. Five layers. |
| 13 support | Red Hat engineering, running its own AI. | Powering Red Hat's Agentic SDLC. |
| 16 headline | Every token has a price. | Become an AI model provider. |
| 16 support | Pay less for every one. | Your models. Your prices. Your rules. |

Scene 16 is now standalone: no pronoun, no implied antecedent. It also inverts scene 5
line for line, which is the whole reason the pair is worth having. "Now you set the
price" was ruled out for failing exactly that standalone test.

### Proof order

Scenes 14 and 15 swapped. The arc is now scale (1T) then our own estate (70%) then the
independent referee (233% ROI). It ends on a third party instead of our own pilot.

**Renumber trap, handled:** `EXPECTED_HEADLINES`, `EXPECTED_SUPPORTS` and
`EXPECTED_CREDITS` in the validator are keyed to scene numbers, so the HTML, the
validator and the copy doc were renumbered in one pass. Checks 6 and 7 would have
failed otherwise, with no obvious cause.

### Visuals

1. **Scenes 2 and 3, one chart carried.** The bar columns are gone. Scene 2 draws a dark
   demand line; scene 3 repeats it at the identical path (verified by diffing the `d`
   attribute) and adds a red bill line breaking away above a flat gray budget rule.
   No axis, no numbers, no units, no gridlines: it stays an illustration and needs no
   credit. Both lines run on a 6.4 second cycle, so the redraw lands exactly on the
   scene cut and the reset is never visible.
2. **Scene 4, one pool.** Three accelerators in one row, two cold, one pegged. Requests
   arrive at the pegged box and change state to hollow gray rings, the gate's
   vocabulary, rather than fading out. One probe drifts toward cold capacity, stops
   short, and returns. Nothing else on the frame.
3. **Scene 5, one causal event.** A request rides the middle tether, then the provider
   dims and everything behind it dims with it, once per cycle, restoring by 4.7s.
4. **Scene 8, spacing not speed.** Inbound stream 0.42s apart, outbound 0.32s apart at
   the same speed: 25 percent tighter, no implied multiple. The box still breathes.
5. **Scene 9, affinity routing.** Fan-out reduced to one dim dot per box so nothing
   competes; on top, three circle markers route to the same accelerator because it
   already holds their context, and one square marker goes elsewhere. Repeated every
   2.4 seconds, so the pattern reads as affinity rather than round robin. No cache
   rates, no percentages.
6. **Scene 11, a horizon.** The marquee is gone. Four environments sit on four depth
   planes under one red service beam, each plane drifting at its own rate (16px, 11px,
   7px, 4px). The differential sells distance without geography and without a map.
   `BG-01-ToT` moved here from scene 13 and now functions as the horizon.
7. **Scene 13, where the tokens go.** The 1,000 dot wall is untouched. Four red dots
   peel off its right edge and leave the frame. No labels, no pipeline, no icons.

### Deviations from the change request, and why

1. **Stack clearance went on `.visual`, not `.content-wrapper`.** The request asked for
   left padding on the wrapper. That moves the centred headline right by half the
   padding, and the headline is the one element identical across all sixteen scenes.
   Padding on the visual shifts the diagrams 65px right and leaves the type on its
   optical axis. One value for scenes 6 to 11 (scene 6 added beyond the request, so
   the whole spine shares one column).
2. **The layer stack also moved up, from `top: 50%` to `top: 34%`.** The measurable
   collision was vertical, not horizontal: a frame-centred rail ran into the top of the
   headline on the spine scenes. Pinned to the centre of the visual band it clears the
   text block by about 150px at 1920x1080, and it no longer depends on headline length.
3. **Scene 5 dims the provider and all three model boxes, not one box.** One box dimming
   says "one workload stalled". The headline says everything is chained to one cloud, so
   the provider goes quiet and the three models go quiet with it, in one gesture,
   sequenced so the cause precedes the effect.
4. **Scene 11 substrate at 0.18.** A judgment call, not a measurement: the ridge is
   red-free, but at 0.20 it risked reading as a second diagram edge under a 4px red
   beam. 0.18 keeps it as ground. Adjust the inline opacity if it reads flat.

### Validation

`tools/validate.py`: 16 of 16 pass, 25 infinite animation rules, no em or en dashes,
all references local, zero network. Added checks, all clear:

1. Scenes 2 and 3 share a byte-identical line path and the same viewBox.
2. Neither scene 2 nor scene 3 contains a `<text>` element, a number, or an axis.
3. No diagram in scenes 6 to 11 overlaps the layer rail at 1920x1080. Leftmost diagram
   edge is 485px, rail ends at 271px, gutter 214px.
4. Denials in scene 4 end as hollow rings, held to 100 percent of the cycle.
5. Scene 9 routes the same marker to the same accelerator three times per cycle.
6. Scene 13 still sums to exactly 1,000 dots with the original radius formula.
7. Every scene carries an infinite animation.

JS syntax checked with `node --check`.

### Still unverified

No headless browser on this machine, so validation is static. Needs eyes on the panel:

- The line charts at 3 m: is the divergence in scene 3 legible in one second?
- Scene 4: do the hollow rings read as refusal, or as loading?
- Scene 11: does the parallax read as depth, or as drift?
- Scene 15: the utilization bars still carry the 30 to 80 claim; unchanged, still unverified.
- Scene 13: does the thread register, or is it too subtle at distance?

### Still open

- Scene 2 and 3 still carry no number by design. The external stat slot is open, not forgotten.
- MLPerf v6.x freshness remains a copy question.
- Optional bespoke horizon generation (section 7a of the change request), only if the
  moved ridge reads flat on the panel.
