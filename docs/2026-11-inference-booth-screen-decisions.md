# Inference Booth Screen, v1.3 Decision Log

Started Nov 18, 2026. Nothing here is built yet.

**How this works.** We walk one scene at a time. You rule, I write the ruling here. When
every scene has a `DECISION` line, I assemble one build prompt from this file alone, so
the build never has to interpret, only execute.

**Status:** every scene ruled and locked. Nothing is blocked and nothing is waiting on an
external asset. Scenes 5, 6 and 11 each went through more than one iteration after you found
a better device, and all three are final. The scene 11 generated image thread closed with no
image taken, which removes the last dependency rather than adding one.

**What is left is assembly:** the decisions in this file, the twelve build tasks and the
fourteen acceptance checks in the v1.3 prompt, the validator update, the copy doc and the
addendum. Nothing in that list needs a decision from you.

**Numbering, read this first (v1.3.5).** This file is a chronological log, so the headings
below keep the numbers the scenes had when they were ruled. At v1.3.5 the mantra scene was
deleted and the loop went from sixteen scenes to fifteen. **Old 12 (Mantra) is gone. Old 13
through 16 are now 12 through 15.** If a heading says "Scene 13, Scale", the build calls that
scene 12 today. The copy doc and the build use the new numbers; only this log's historical
headings use the old ones.

**Preview pages, open these in the browser:**

| Page | Path | Keys |
|---|---|---|
| Scene 5, models inside the provider | `inference-booth-screen/preview/scene5.html` | click or space restarts the cycle |
| Scene 6, three devices, 6-3 by default | `inference-booth-screen/preview/scene6-variants.html` | 1 2 3 |
| Scene 6, icons versus the rings | `inference-booth-screen/preview/scene6-icons.html` | a icons, b rings |
| Scene 11, deck environments | `inference-booth-screen/preview/scene11-deck.html` | 1 2 3 art, b under structure, c captions, o opacity |
| Scene 11, floating environments | `inference-booth-screen/preview/scene11-float.html` | 1 2 3 art, b beam, o opacity |
| Scene 11, two art candidates | `inference-booth-screen/preview/scene11-art-test.html` | 1 2 3 to switch, o for opacity |

All six are mirrored under `Documents/talks/inference-booth-screen/preview/`. Self contained,
zero network, same fonts and same six point four second cycle as the real build. Scene 5 is
now a single scene rather than a comparison, because you replaced the three variants with
your own design. Scene 6 keeps its three so you can still flip and confirm 6-3.

**Stops:** 1, 2 and 3 together, 4, 5, 6, 8, 9, 10, 12, 13, 11. Scenes 7, 14, 15 and 16
have no open items and are listed at the end only so the sweep is visibly complete.

| # | Scene | Open question | Recommendation | DECISION |
|---|---|---|---|---|
| 1 | 1 Open | Support line, and whether the brand needs a permanent mark | "Lower the cost of every token. From Red Hat AI." | **Decided: see below** |
| 2 | 2 and 3 Tension | How tall the demand curve gets, and what the three labels attach to | Tall exponential, cost crosses the rule first | **Decided: C, see below** |
| 3 | 4 Stranded | Remove the probe dot, and whether to replace the causal read | Remove it, no replacement | **Decided: C, bounced request** |
| 4 | 5 Chained | "one provider" and a visual that shows a failure | Cloud as container, models inside | **Decided: models inside the provider** |
| 5 | 6 One path | The device, the router word, then the marks | Stations on the canal, rail as verbs | **Shipped: 6-3 rings, rail verbs** |
| 6 | 8 Optimize | Nothing structural. Confirm the frame survives the copy changes around it | Keep as built | **No change** |
| 7 | 9 Distribute | What replaces the prefill and decode split | Cache affinity, one fleet row | **Decided: A** |
| 8 | 10 Gate | The guardrails claim, and the fallback if the hub cannot back it | Guardrails, gated on verification | **Decided: A** |
| 9 | 12 Mantra | The five ways versus the price promise | "Five moves. One bill you control." | **Decided: A** |
| 10 | 13 Scale | The icon, and what carries the trillion once the wall goes | Icon plus fast stream, headline carries the number | **Decided: icon sourced, masked flow** |
| 11 | 11 Service | Which image, which environments, and what anchors them | Deck icons, captions, Sovereign first | **Locked: ridge, rules, captions, 0.70, glow on** |

---

## Scene 1, Open

**On the table**

1. The support line. "The inference story. From Red Hat AI." names the topic but sells
   nothing, and in an attract loop scene 1 is the frame a passer by is most likely to
   catch cold.
2. Whether the brand needs a permanent mark on every scene.

**Why 2 matters for 1.** Right now only scene 16 carries the logo. If the opener drops
"From Red Hat AI", a visitor who catches one frame cannot tell who made the screen. Putting
the logo on the opener fixes that at the source, and it is what the governance screen
already does.

**Options for the line** (superseded by the decision below)

| Option | Line | Words | Notes |
|---|---|---|---|
| A | Lower the cost of every token. From Red Hat AI. | 9 | Answers the headline, names the brand, sets up scene 12 |
| B | Inference you own. Costs you control. | 6 | Punchiest, no brand, leans on a permanent mark |
| C | Here is how to lower it. From Red Hat AI. | 9 | Direct, slightly weak as a first frame |

**DECIDED**

- Headline raises the aspiration instead of stating the price, matching the grammar of
  the governance screen's "Agents worth trusting." Two screens, one series.
- Headline: **Inference worth scaling.**
- Support: **Models you own. Costs you control.**
- Scene 1 gets the brand logo, same lockup as scene 16, so the opener and the closer are
  visual bookends and the support is free of brand duty.

**Consequences to build**

1. Scene 12 remains the only place that says "Every token has a price.", and that is now
   a deliberate turn: the loop opens on the aspiration, names the obstacle at the pivot,
   then spends four scenes proving the way through. The copy doc's "opening thesis" line
   changes to name scene 12 as the thesis, not scene 1.
2. Scene 1 gains a `.visual` band holding `red-hat-ai-logo-positive.png`, with the same
   `logo-in replay` treatment as scene 16. Headline and support move down into the text
   block, exactly as scene 16 already sits.
3. Scene 16 keeps its logo. Seeing it twice makes it a return rather than a reveal, which
   is the correct behaviour for a bookend.
4. Validator: `EXPECTED_HEADLINES[1]` and `EXPECTED_SUPPORTS[1]` change. The
   "brand appears only on scene 16" note in D6 of the v1.3 prompt is now void.

**Cost accepted:** the screen no longer opens on the price thesis, so a visitor who
catches only scene 1 learns what they get (scale, ownership, cost control) and not what
the screen is about (the price of a token). Mitigation is the support line, which names
costs.

---

## Scenes 2 and 3, Tension

**On the table**

1. The demand curve becomes exponential. Item 1 of your list.
2. Scene 3 labels demand, cost and budget. Item 2 of your list.

**The constraint that shapes both.** Two lines on one frame with one flat rule means three
objects competing for the same vertical space. There is a hard trade in the geometry:

- To cross a **high** rule early, the cost line has to shoot up and then flatten at the
  top. Flattening at the top reads as "cost is capped", which is the opposite of
  compounding.
- To cross a **low** rule early, the cost line can stay steep all the way, but then the
  demand line has only about 60 units of vertical room before it hits the rule.
- A **tall** demand line is therefore only possible if the demand curve is allowed to
  cross the budget rule too, which puts a tokens line through a dollars line.

**On your Uber instinct:** the temptation is right and the shape is exactly the one to
draw. A single early crossing says "the money ran out in month four and the line kept
going", which is a sharper claim than "cost ended up above plan". What it needs is one
crossing, not two, so the eye has one event.

| Option | Demand | Budget rule | Cost crossing | Trade |
|---|---|---|---|---|
| A | 112 units, ends y 140 | High, y 100 | Around x 590, late and flattening | Taller curve, but the cost line has to ease off at the top, which undercuts "compounding" |
| B | 64 units, sharp late knee, ends y 188, never crosses the rule | Low, y 170 | Around x 430, early and still climbing | Cleanest single event, unit honest, demand line shorter but shaped like a takeoff rather than a steady rise |
| C | Tall, ends y 52 | Low, y 170 | x 430, and demand crosses at x 620 | Biggest demand curve, two crossings, tokens through a dollars line |
| D | Removed | Removed | Not shown | Simplest frame, loses the word the headline is built on |

**Recommendation: B.** One early crossing is the Uber shape and the strongest three second
read. The demand line gets its drama from the knee, not from amplitude: flat for two
thirds of the frame, then a hard turn up that stops just short of the rule, which also
says "the next wave has not landed yet". All three labels then stack in one right hand
gutter at y 44, 160 and 216, so nothing floats over a line and nothing collides.

If B still reads flat on the panel, the one word fix is C: keep everything and let the
demand line run to the top, accepting the second crossing.

**Sub question, decided:** "demand" is labeled on scene 2 as well, so the name persists
across the cut.

**DECIDED: C.** Tall demand, two crossings accepted. The second crossing is the point:
cost breaks the plan first and demand breaks it second, so the frame says the wave has not
finished arriving.

Exact geometry, both scenes on `0 0 960 300`, plot x 40 to 780, baseline y 252:

| Element | Path or position | Label |
|---|---|---|
| Demand | Exponential from (40, 252) to (780, 60), amplitude 192, k 4. Monotone, accelerating, ends slope about 54 times the starting slope | "demand", inline at (500, 196), sitting in the widest gap between the two curves. **Build note v1.3:** measured at 26px, "demand" is 94.7px wide, so at y 196 the rising tail of the curve crosses the last letter by about 15px and the label has under 11px of room between the rule and the curve at that span. The build places it at (790, 74) instead, level with its own endpoint dot and in the same label gutter as budget (790, 160) and cost (790, 44). Same three labels, same meaning, no collision. Revert only with new eyes on the panel. |
| Budget rule | Flat, y 170, x 40 to 780 | "budget" in the right gutter at (790, 160), above the rule |
| Cost | From (40, 252) to (780, 34), crossing y 170 at about x 430, above the demand line at every x | "cost" in the right gutter at (790, 44) |

- Crossings: cost at x 430, demand at x 627. Cost first, always. Check V5 enforces it.
- Demand dot r 7 at (780, 60), cost dot r 7 at (780, 34): 26 units apart so they do not
  merge.
- Scene 2 carries the demand line, its dot and its label, nothing else.
- Scene 3 adds the rule, the cost line, its dot and the other two labels.
- Both scenes keep the identical demand `d` and the identical viewBox, so the cut reads as
  continuity.

**Cost accepted:** a tokens line passes through a dollars line at x 627. The labels are
what make the frame decodable, which is why they are not optional.

### SUPERSEDED at v1.3.2, Nov 19

**Carlos's call:** the bill outgrows the budget is the whole argument, and two lines with two
crossings made the visitor do comparison work in three seconds. One line says it in one
glance.

1. **The red cost line is deleted.** No `line-b`, no red dot, no third label. Retired
   vocabulary: the word "demand" no longer appears as an on-screen label.
2. **The exponential line is relabeled "cost".** Same `d`, byte for byte, same viewBox, same
   gravity: it is the bill now, not the wave.
3. **Scene 2 headline becomes "AI demand and cost are compounding."** (6 words). The
   subject is compound, so the verb is "are"; Carlos's draft read "is compounding" and the
   grammar was fixed without changing his meaning.
4. **One crossing, at x 627.** Cost passes the y 170 rule late and does not come back, which
   is a stronger read than passing early: the plan looks fine for most of the run and then
   it does not. Check V5 now asserts exactly one path, one crossing, inside x 500 to 700.
5. **The crossing is deliberately unmarked.** A ring or a pulsing dot at (627, 170) was
   offered and declined: the frame already carries a rule and a line, and a marker there
   would read as an alert badge.
6. **Scene 3 now draws its own line.** With the second line gone, scene 3 had no motion at
   all, which breaks the nothing-ends-static rule. Both scenes run the same 6.4s draw with
   the same phase, and since a scene lasts exactly one animation period, the reset lands on
   the cut where the crossfade absorbs it. The visitor sees the line trace, cross and hold,
   twice per loop, once with the rule absent and once with it present.

**Live geometry, both scenes:** `0 0 960 300`, plot x 40 to 780, baseline y 252, exponential
from (40, 252) to (780, 60), amplitude 192, k 4, labelled "cost" in the right gutter at
(790, 74). Scene 3 adds only the flat rule at y 170 and its "budget" label at (790, 160).
Two labels total on scene 3. Nothing else changed.

---

## Scene 4, Stranded capacity

**On the table**

1. Remove the floating dot under the boxes. Item 11 of your list.
2. Whether anything replaces what that dot was saying.

The dot was the only element claiming "the work cannot reach the idle capacity". Without
it, the frame says "GPUs are unevenly loaded" and stops short of "and that is why you are
stuck".

**Options**

| Option | Result |
|---|---|
| A | Delete the dot. Frame becomes a state, not a cause |
| B | Delete the dot, add a dashed stub from the pegged box toward a cold one that fades before arriving |
| C | Delete the dot, add one refused request per cycle that visibly bounces toward the cold box and returns |

**Recommendation was A** (the refusal rings plus the idle boxes already carried the cause).
Overruled in favour of C, which is more literal.

**DECIDED: C.** The refused request does the causal work, so the probe dot goes and
something more literal takes its place.

Build: two requests per scene cycle, 3.2s apart, each with a 2.6s life. A red dot descends
from above the frame into the top edge of the pegged accelerator in 1.0s. On impact the red
dot is replaced by a gray ring that expands and fades over 0.6s, which is the refusal. The
request then rebounds up and to the right, fading out after travelling about 40 percent of
the way toward the nearest cold accelerator, so it never reaches the capacity that exists.
Red is the request, gray is the refusal, and the fade is the point.

- Delete the `reach-dot` circle and its CSS rule.
- Replace the three existing `deny-dot` rings with these two bounce events, so the frame
  has one vocabulary rather than two.
- Keep everything else on scene 4 exactly as built.

---

## Scene 5, Chained to one provider

**On the table**

1. The word: "one provider" instead of "one cloud". Item 3.
2. A visual that shows a problem rather than a state. Item 12.

**On 1, DECIDED:** "one provider". No further discussion. It broadens the frame from a
hyperscaler to any model or cloud provider, and it protects the AWS relationship. Side
benefit: it rhymes with the closer, where the reader becomes a provider themselves.

**On 2, TWO ITERATIONS, BOTH YOURS.** The first attempt put three model boxes on the
left feeding a cloud in the middle. It was better than the plug and pipe variants, and you
then found the flaw in it yourself.

**The flaw you caught.** The governance screen already owns a diagram that reads as a
promise: sources on the left, a gate in the middle, models on the right. A mirrored copy on
this screen makes one drawing argue both sides, and it puts "one provider" in the villain
role while Red Hat is also a provider and AWS is the partner standing next to us.

**DECIDED: the cloud is the container, not a waypoint.**

| Zone | Contents |
|---|---|
| Left of centre | One large cloud, the brand cloud icon at 320 by 320, with the three model icons living inside it |
| Right | Three labelled pills, Users, Agents, Apps |
| Between | Three thin gray routes, red tokens running them fast |

- **Geometry, 960 by 360 viewBox.** Cloud at x 115, y 20, 320 square. The three model icons
  are 42 square at y 196, at x 198, 254 and 310.
- **Clearance, measured against the raster's alpha channel, not eyeballed.** The nearest
  cloud ink to each icon is 16, 18 and 16 source pixels, which is roughly 24 pixels on
  screen at 1920. Your first look caught a real collision: at the original 52 size the
  right icon sat 6 source pixels from the stroke, which is why it read as touching. The row
  also moved down from y 176 to y 196, because the cloud's interior is widest between
  source y 190 and 240 and narrows sharply above that.
- **The cloud stroke is thinned with a filter.** The brand cloud icon is a raster PNG, so
  its stroke weight cannot be set. The build applies `filter: url(#cloud-thin)`, which
  erodes the alpha channel by 3 user units, softens the result and refills it in
  `#EE0000` under `sRGB` so the red does not drift. `radius` is the only tunable: higher is
  thinner. If the filter reads soft on the real panel, the permanent fix is the brand SVG
  with a 6px stroke, which does not exist in this project yet.
- **The three model boxes on the left are deleted.** So are the supply lines. The models
  are inside the cloud now, so there is nothing on the left to feed it.
- **Pills** at x 780, 155 by 52, rx 26, y 32, 154 and 276. Labels 24px Red Hat Text.
- **Routes** leave the cloud at x 435, y 158, 180 and 202, and land on x 780, y 58, 180 and
  302. Gray at 1.6px, 0.45 opacity.
- **Tokens** are red, 5 radius, crossing a route in about 880ms at full speed, emitted every
  110ms with the three routes staggered by 37ms.

**Why this is the right frame.** It stops being about a door you pass through and becomes
about ground you stand on. Your models are in their house. That is a different claim from
"one door to every model", so the two screens stop arguing with each other. And it makes the
support line literal: "Their models" is now three models visibly sitting inside somebody
else's cloud.

**The failure, unchanged from the previous iteration, on a 6.4 second cycle.**

| Time | What happens |
|---|---|
| 0.0 to 3.2 | Full flow |
| 3.2 | The cloud and everything inside it fade to 12 percent over 900ms |
| 3.2 to 5.0 | Tokens decelerate on a linear ramp to a dead stop, emissions end about 4.9 |
| 5.0 to 5.7 | Whatever is still in flight fades out. Routes empty |
| 4.4 to 6.4 | The three pills turn red and throb, 1 to 0.94 to 1.05 to 1, on a 900ms period |

- The consumers never dim. The people stay, the supply vanishes.
- The model icons fade with the cloud, because they are inside it and therefore not yours.
- Headline unchanged: "Inference chained to one provider."
- Nothing recovers inside the cycle. It ends on the outage and resets on the cut.

**Three flags on record.**

1. **Red density in the left corner.** The cloud is red line art and so are the three model
   icons. The thinner cloud stroke and the smaller icons take most of this away, but if the
   corner still reads as a red mass on the real panel there is a `.models-neutral` class
   already in the preview that grayscales the three icons. One class, no geometry change.
2. **Fade depth.** 12 percent, not zero, so the cause stays faintly visible. One number.
3. **The throb.** Most red in the sixteen scenes. Earned, because this is the only frame
   where the failure lands on a person. Fallback is outline and label only, no fill.

**Preview:** `inference-booth-screen/preview/scene5.html`. Single scene, click or space
restarts the cycle.

**DECISION:** locked as above, no open questions

---

## Scene 6, One path

**On the table**

1. The device. The current beam puts three labels on the frame while the support line
   claims five layers, so the frame contradicts itself in the time it takes to read it.
2. What the layer is called, and whether the frame shows layers or a path.

**The finding, stated plainly.** This is the "Every token takes one path" scene, and right
now it shows **three** names, Runtime, Router, Gateway, while the support says **five**
layers and the rail behind it lists five. That mismatch is very likely what you were seeing
as an overlap. Nothing is physically colliding; the frame is saying two different things.

**On your Runtime, Fleet, Gateway suggestion.** It is a good instinct and it fixes a real
error. Those three are the actual request path, in the actual order: the request enters the
Gateway, gets placed on the Fleet, and computes on the Runtime. The current frame puts
Gateway third, which is false. The catch is that the five layers are not a path: Optimization
is how the model was made cheap before any request arrives, and Service is how the result
reaches your users. So scene 6 has to pick one of two truths.

| Truth | Frame | Support line | Cost |
|---|---|---|---|
| Layers | Five things, stacked, one path crossing them | Five layers (unchanged) | A stack does not show a journey |
| Path | Three stops: Gateway, Fleet, Runtime | Must change, since three are shown | The five layer reveal moves to scene 7, where the rail appears |

**DECIDED: build three variants and compare.** Same method as scene 5: a self contained
preview page at `preview/scene6-variants.html`, keys 1, 2 and 3, same fonts, same 6.4 second
cycle, zero network, not published.

| Variant | What it shows |
|---|---|
| 6-1, layers | Five horizontal bands stacked, one thick path crossing them top to bottom with a dot inside, each band lighting as the dot passes, names right aligned in one column |
| 6-2, path | Your suggestion: three stops on one thick conduit, Gateway then Fleet then Runtime, dot inside the line, each stop lighting as it arrives, support line adjusted |
| 6-3, bus | Five stubs hanging off one horizontal conduit, five rings lighting in turn, rail hidden on this scene |

**DECIDED: 6-3, stations on the canal, with the stubs deleted.** You spotted that the
five vertical drops were drawing a relationship that did not need drawing, and that
connecting lines between the canal and its own stations is an extra layer of drawing
between a thing and its name.

- One horizontal canal, 12px, gray-25, from x 70 to x 930 at y 100.
- Five stations sitting directly on the canal at x 150, 330, 510, 690 and 870. Each is a
  28 radius white disc with a 3px gray-40 ring.
- The name sits under each station at y 176, 24px, centred.
- One token runs the canal left to right and passes through each station in order. As it
  reaches a station's centre, that station fills solid red, and **it stays filled**. By the
  end of the pass all five are solid.
- The filled stations then breathe very faintly (a red halo at 10 percent) so the frame is
  not static for the last two seconds.
- The token itself is ink, not red. A red token inside a red filled station disappears, and
  ink keeps it visible the whole way through.
- The layer rail stays hidden on this scene, so the five names appear once and only once.
- 6-1 and 6-2 stay on the preview page so you can still flip between them, but 6-3 is the
  build.

The end state matters: the frame finishes with a full pipeline, which is exactly the
condition scene 7 inherits when the rail slides in beside it.

**SHIPPED.** You approved this one as built, then amended the marks. See below. The wiring
into `index.html` happens in the build pass, not now, because the rail word change touches
six scenes and scene 5 has to land in the same commit.

### The icon amendment, proposed and withdrawn

You asked for real icons instead of the discs, I built them, you compared the two on the
same clock, and you kept the discs. Recording it because the reasoning matters more than
the outcome: five different glyphs at 48 pixels each add detail without adding meaning, and
the discs were already carrying the verbs through the captions underneath. More drawing is
not more information.

The five glyphs are still on disk (`assets/icons/step-run-208.png` and four siblings) in
case a later scene wants them. Nothing in the build references them.

**Rejected: a subsection that no longer applies, kept only for the trail**

You asked for real icons instead of identical discs. Circles were carrying the verbs and
nothing else, and five identical rings say less than five different glyphs.

| Verb | Icon | What it is |
|---|---|---|
| Run | `step-run-208.png` | a terminal prompt in a box |
| Optimize | `step-optimize-213.png` | a gear inside a cycle of arrows |
| Distribute | `step-distribute-236.png` | a screen with three nodes linked around it |
| Gate | `step-gate-209.png` | a shield with a keyhole |
| Deliver | `step-deliver-252.png` | a sealed carton |

All five come from the same Red Hat Icon Repository deck as the Agentic AI icon, all 360
square, all red line art, no product names, no logos.

**What has to change to carry them.**

- The 28 radius ring goes. In its place a plain white disc at 34 radius, no stroke, so the
  canal is interrupted cleanly and the glyph sits on white rather than on the line.
- The glyph is 48 square, centred on the canal, so the canal passes behind it and the token
  passes through the station.
- **The fill becomes a relight.** A filled disc can go solid; a line glyph cannot. So an
  unfilled step is the same glyph grayscaled to 30 percent, and the moment the token reaches
  it the glyph returns to full red and stays red for the rest of the pass. Same clock as the
  discs: 12.5, 25.5, 38.5, 51.5 and 64.5 percent.
- The token now sits behind the discs, so it goes into each station and comes back out
  rather than running over the glyph. Five short disappearances instead of one clean line.
  That is the trade for glyphs, and it reads as entering the machine.
- The canal and the five names stay exactly as shipped. You confirmed the frame yourself
  when you said the captions were not the problem.

**Preview:** `inference-booth-screen/preview/scene6-icons.html`. Key `a` is the icons, key
`b` is the approved rings, so the two sit on the same clock and you can flip between them.

**Risk on record:** at 48 square these are small glyphs. The Run prompt and the Deliver
carton have clear silhouettes and will hold at three metres. The Distribute glyph has three
nodes and a screen inside one small square, and it is the one most likely to read as noise
on the panel. If it does, the fallback is a simpler node glyph, and I would rather swap one
icon than redraw the frame.

**DECIDED: the rail becomes five verbs.**

**Where the old words actually live in the build, since this is now a merge question.** You
flagged that `index.html` still reads Runtime, Optimization, Distribution, Gateway, Service.
It does, and it should not change before the build pass. The five names are one block of
five spans at lines 503 to 507 of `index.html`, and the rail is a single element that shows
on scenes 6 through 11. Five edits in one place, and every scene picks it up at once. No
risk of a half renamed rail.

Three other places carry old words, and two of them are deleted rather than renamed:

1. Scene 6's beam labels, Runtime at x 200, Router at x 500, Gateway at x 800. Deleted when
   the new scene 6 lands.
2. Scene 9's prefill and decode. Deleted with the phase split.
3. **Scene 7's diagram node**, a bold red label that reads Runtime at line 678. That one is a
   genuine call, because it names the thing that serves the model, not a stage of the
   journey. Recommendation: keep Runtime there. If the rail says Run one frame away, the
   two words are doing different jobs and both are accurate. Flagging rather than deciding.

| Row | Was | Becomes |
|---|---|---|
| 1 | Runtime | Run |
| 2 | Optimization | Optimize |
| 3 | Distribution | Distribute |
| 4 | Gateway | Gate |
| 5 | Service | Deliver |

Why this is the right fix rather than a plural: "Optimization" alone was off because a
layer named with an abstract noun reads as a category, not as an action. Making all five
verbs fixes that for every row instead of patching one, and it makes each rail row name the
same action as its matching spine scene. Row 2 and scene 8 are now the same word. The rail
is parallel for the first time.

**Knock on to build, in the same pass as the scene work:**

1. `#layer-stack` in `index.html`: five `.layer-label` spans change to Run, Optimize,
   Distribute, Gate, Deliver. The rail is visible on scenes 6 through 11.
2. 6-3's five ring labels use the same five words.
3. Copy doc: the layer list row changes for all five.
4. Validator: add a check that the rail's five labels match the five ring labels on scene 6,
   so the two can never drift apart again.
5. `Router` does not survive anywhere. It was already being deleted; it now has no
   descendant either.

**One cross screen flag, your call to leave.** The governance screen's rail reads
Sandbox, Gateway, Traceability, Proof, Identity. Ours now reads Gate where it says Gateway.
Same architectural layer, two words, across two screens built to read as a series. I am not
changing it quietly. If you want them matched, the options are to make ours "Gateway" and
break the all verbs rule on one row, or to change the governance screen to "Gate" and
republish it. Neither is free, and the current state is defensible because the governance
rail names capabilities while ours names stages.

**DECISION:** locked as above

---

## Scene 8, Optimize

No structural change requested. Listed so the sweep is complete. The only risk is
collision with the new scene 12 wording, and there is none: scene 12 now says "Five moves.
One bill you control." and scene 8 keeps its own headline, so the two no longer share a
claim.

**DECISION:** no change, confirmed

---

## Scene 9, Distribute

**On the table**

The frame currently routes requests to a prefill path and a decode path. That is wrong on
two counts: prefill and decode are phases inside one request, and prefill comes first even
under P/D disaggregation.

| Option | Frame | Truth |
|---|---|---|
| A | One fleet row. Same marker to the same accelerator three times, a ring pulse at each repeat, one new marker adopting a fresh accelerator | KV cache affinity, which is what routing actually exploits |
| B | One fleet row, no extra events, just the repeats | Same idea, flatter frame, less to explain |
| C | Show prefill then decode as two phases inside one accelerator, sequentially | True, but two phases at three meters is unreadable |

**Recommendation:** A. Phase vocabulary moves to the talk track.

**DECIDED: A.** One fleet row, size no larger than four accelerators across, so each one
stays a legible object at three metres.

- Delete both labels, `prefill` and `decode`, and the two row layout with them.
- Same circle marker returns to the same accelerator three times per cycle, 2.4s apart.
- At each repeat, that accelerator emits a ring pulse outward from its outline: this is
  the cache hit, and it is the only new element on the frame.
- One square marker arrives once per cycle and adopts an accelerator that has no cache.
  That accelerator's outline fills faintly for the rest of the cycle: now it holds one too.
- Background traffic stays at one dim dot per accelerator, so nothing competes with the
  marking.
- No percentages, no cache rates, no phase words anywhere, comments included.
- Credit line unchanged: llm-d + vLLM, 2026.

**Phase vocabulary for the talk only:** prefill, decode, and P/D disaggregation are correct
and worth 40 seconds out loud. They are not screen words.

---

## Scene 10, Gate

**On the table**

"Data never leaves your control" is determinism we cannot guarantee, especially with
external providers in the path.

| Option | Support | Note |
|---|---|---|
| A | Identity. Rate limits. Guardrails. | Pitches the feature, needs hub confirmation |
| B | Identity. Rate limits. Policy. | Safe, weaker, no hub risk |
| C | Identity. Rate limits. Guardrails on every request. | Strongest, 7 words, same hub risk as A |

**Recommendation:** A, with B as the instant fallback if the messaging guide cannot back
the guardrail claim. I searched it and found no guardrail language, so this needs either a
confirmation from you or a different approved source.

**DECIDED: A.** Support line becomes **"Identity. Rate limits. Guardrails."**

- Residency is not lost, it moves wholly to scene 11: "Where your data lives. Sovereign to
  edge."
- The phrase "Data never leaves your control" is deleted from the file, comments included,
  so it cannot drift back in.
- One open item before this locks: confirm the approved guardrail term for the gateway
  (TrustyAI guardrails or equivalent). If it cannot be backed, the line becomes B and the
  addendum says why. This is a one line change either way, so the build does not wait on it.

**Build note v1.3.3, Nov 19 (dot speed).** Carlos ruled that the gate has to move at the
speed the visitor just watched on Distribute. The speed that matters on scene 9 is not its
dim background traffic (168 to 276 units per second, four dots at grey 40) but its tracked
markers: 720 units in 1.5s, which is **480 units per second**. The gate was running at 256.
It now runs at 480: a pass is 640px in 1.33s, a stop covers its 390px in 0.81s and then
holds. Density went from 8 dots to 14, staggered 0.42s, because at 480 the old spacing left
the gate almost empty. Ten pass, four stop, interleaved rather than blocked at the end, so a
visitor never sees the gate in a single state. The rule this protects is that nothing
decelerates before the gate: a gate that slows traffic would contradict the scene before it.

---

## Scene 12, Mantra

**On the table**

"Five ways to lower it" includes Deliver, which delivers a service rather than lowering a
bill.

| Option | Support | Cost |
|---|---|---|
| A | Five moves. One bill you control. | One line. "Lower" survives on scene 14 where it is proven |
| B | Five ways to lower it. (unchanged) | The inconsistency you flagged stays |
| C | Replace Deliver in the spine | Scene 11's headline "Deliver AI as a service" has to change too |

**Recommendation:** A.

**DECIDED: A.** Support becomes **"Five moves. One bill you control."**

- Beat words, their timing (0.3s apart from 0.3s to 3.5s) and the mantra drift are
  unchanged.
- Scene 11 keeps Deliver. The spine's five verbs are untouched.
- Scene 12 remains the only frame that says "Every token has a price.", which is now
  deliberate: the loop opens on the aspiration, names the obstacle at the pivot, then
  spends the rest proving the way through.
- "Lower" survives only where it has evidence: scene 14, "Up to 70% lower token costs",
  with the EnMaaS credit.

**Build note v1.3.4, Nov 19 (scene 12 goes silent).** Carlos cut the headline and the support
from this scene: "not necessary and in the way of the evidence." He is right, and the ruling
above is superseded on that point. The scene is now one rule with five nodes and the five
verbs, nothing else.

- **Removed:** h1 "Every token has a price." and support "Five moves. One bill you control."
- **Kept:** the five verbs, their 0.3s stagger from 0.3s to 3.5s, the mantra drift, and the
  five nodes pulsing on the same beats. The node line is the evidence: each dot lands with
  its verb, so the order is shown, not asserted.
- **What this costs:** "Every token has a price." now appears nowhere on glass. The price
  frame is carried by scene 3 ("The bill outgrows the budget.") and proven at scene 14
  ("Up to 70% lower token costs"). Accepted: the claim now sits where its evidence is, and
  the mantra does not need to restate it.
- **What this buys:** the count word "five" leaves the glass, and so does the only line on
  the loop that repeats the spine. The scene no longer tells the visitor what the next six
  seconds are about to show them.
- **Text block:** min-height raised from 30vh to 34vh so the five verbs hold the optical
  centre of the frame without a headline above them. Nothing else moved.

**SUPERSEDED at v1.3.5, Nov 19: the scene is deleted.** Carlos cut the whole frame, not the
line: "delete the entire scene, Deliver jumps directly to the trillion." He is right, and the
reason is structural rather than editorial. The mantra was a summary of the five spine scenes
placed after the five spine scenes. A visitor who watched scenes 7 to 11 had just been told
the five verbs one at a time with their evidence attached, and a visitor who arrived on scene
12 had no reason to care about a list without the evidence. Either way the frame did no work.

- **Removed:** the scene block, its five verbs, the five nodes, the node pulse, the beat
  stagger, and the mantra drift CSS. No strings from it survive anywhere in the file.
- **Not moved anywhere.** The rail already names the five verbs on scenes 7 to 11, and scene 6
  already says "One request. One path. Five layers." A third recital would be the same content
  three times.
- **The consequence for the price frame:** "Every token has a price." was already gone at
  v1.3.4, so nothing further is lost. The price frame lives on scene 3 and is proven on scene
  13 (old 14).
- **Renumbering:** 16 scenes become 15, the loop goes from 102.4s to 96s, and old 13 to 16
  become 12 to 15. The engine's scene 13 ids and `S13_` constants keep their names because
  renaming them would risk a silent break for no visible gain; the code says so in a comment.

---

## Scene 13, Scale

**On the table**

1. Replace the 1,000 dot wall with the Agentic AI icon and fast dots. Item 9.
2. What carries "a trillion" once the wall is gone.

**Icon sourced.** It was in the Red Hat Icon Repository deck, slide 43, the AI/ML special
set, first row fifth column. Exported from the deck and saved as
`assets/icons/agentic-ai-400.png`, 400 by 400.

**DECIDED**

1. **The icon replaces the wall.** Dense, fast flow through the icon, centred at about
   340px.
2. **The flow is masked to the icon's own strokes.** The icon is a raster, so its paths
   cannot be addressed directly. Instead the red strokes become the mask: an animated dot
   pattern sits over the icon and only shows where the strokes are, so the dots appear to
   run inside the red lines. No path tracing, no drift off the artwork. If the mask reads
   noisy on the panel, the fallback is a stream that enters and leaves the icon along its
   horizontal axis.
3. **Dots are ink, not red.** The icon is entirely red, so a red stream would disappear
   into it. Ink keeps the flow visible and keeps the icon the only red object on the frame,
   which is the red discipline for this scene.
4. **The headline carries the trillion.** No second quantification, no density wall, no
   counter. Same division of labour as scene 9: the words make the claim, the credit line
   carries the source, and motion makes it feel large.
5. Delete the `token-thread` block. The exiting flow is the thread now.

**Fallback on record:** if the icon alone reads thin at three metres, composite it over the
dimmed dot wall. Not built unless asked.

**Build note v1.3.1, Nov 19.** The icon is retired. Scene 13 now carries a generated river
render (`assets/gen/scene13-river.png`, 2730 by 1536): beads pour in from the left, funnel
through a red lattice, and come out as software. Two candidates were generated, one flat
line art and one rendered. The flat one wins at 100 percent and loses at booth size: its
dots are about 1.5px and its panel hairlines about 2px at source, so at the roughly 0.37x
it is displayed they fall to 0.55px and 0.7px and alias into a pink wash, and the right
half of the frame (median luminance 255) effectively disappears. The rendered version's
beads are 14 to 18px at source and land at 5 to 6px, so it holds as material. It is shown
in the visual band at full opacity, never dimmed, and it replaces the masked flow, so the
frame's one animation is now a 14 second pan and breathe (1.02 to 1.05 scale, plus or
minus 6px), which carries the drift in the direction the river already runs. Known soft
spot: the panel faces measure 223 on a 255 ground, so the slabs separate only through
their shadow seams. Only worth another render if it reads as a heap on the panel.

### SUPERSEDED at v1.3.3, Nov 19: scene 13 is drawn, not rendered

Carlos asked for a visualization that shows both halves of the sentence at once: a trillion
tokens moving quickly, and those tokens powering an agentic SDLC. A still cannot show
movement, and the render showed a mass but not a rate, so scene 13 is now a live SVG driven
by one rAF clock.

**Composition, left to right, one causal chain**

| Zone | What it is | Why |
|---|---|---|
| Lanes, x -40 to 300 | Seven lanes of ink tokens converge on one point at 520 units per second, 70 tokens on screen | The fastest sustained motion in the loop. Speed is the "quickly" half of the ask, and a converging fan reads as pressure, not as a queue |
| Ghost field, x -40 to 500 | 96 dots at r 1.8, opacity 0.2, 380 to 900 units per second, scattered deterministically | The lanes are the tokens you can count; this is the ones you cannot. Seventy dots cannot say trillion, a countable stream over an uncountable field can |
| Agent loop, centre (372, 170) | Static red ring r 58, a red arc r 46 rotating once per 3.2s, three red nodes pulsing in sequence | Three agents, not one box. The rotation is the loop running; the pulse sequence is work moving between them |
| Panel, x 512 to 976 | Fifteen code lines written one at a time in 1.395s, held 305ms, then a red commit rule sweeps in 160ms and sits under the code for 120ms, then code and rule fade together over 153ms | The SDLC half. Work is produced and shipped, repeatedly, inside one cut. Three panels per 6.4s cut, six per loop, so the rhythm is visible without a counter |

**Why nothing is numbered.** The headline carries the trillion and the credit carries the
source. Putting a second number on the frame would need a second credit line and would start
a units argument at a booth where nobody is standing still long enough to win it.

**Why the lanes consume at x 500.** Every token disappears at the print head, immediately
left of the panel. Nothing exits the frame, so the stream reads as input being spent rather
than as decoration passing through.

**Motion budget.** One clock, one direction, no bounce. The river never resets; the panel
cycles three times per cut; the arc rotates continuously. That is three simultaneous motions,
which is the ceiling for this frame, and all three are the same sentence.

**Retired, kept on disk.** `assets/gen/scene13-river.png` stays for a one line revert. If the
panel is judged less impressive than the render at size, the img tag is one line and the
engine block is one block to disable.

---

## Scene 11, Service

**On the table**

You asked to try a generated image instead of the four plane horizon. The art prompt is
ready in Appendix A of the v1.3 prompt.

**The trade:** a generated image that contains the environments and the beam cannot
parallax against itself, so the four depth planes become one still with a slow breathe. If
the image carries only ground and structures, the build keeps the beam, the icons and the
parallax.

**What you asked for.** You wanted a world horizon with connected dots marking the
environments covered. I checked the governance screen's "office hours" scene, and it has
no world in it: it is six environment icons on a marquee. So the world would be a device
borrowed from memory rather than from the other screen.

**Four directions written up** in `2026-11-inference-booth-screen-scene11-image-prompts.md`,
each with a full Gemini prompt and its cost to the build:

| Variant | Asset | Motion | Risk |
|---|---|---|---|
| A | Ground and horizon only | Parallax survives | Least dramatic, keeps the depth you already have |
| B | Dot globe, no landmass | One slow drift | Says everywhere without asserting borders |
| C | World silhouette, connected dots, no borders | One slow drift | A map invites "are you in my country", and any border artefact is a show floor problem |
| D | World sphere, pale sky, faint stars and orbital arcs | One slow drift | Strongest global claim, weakest control claim |

**Recommendation:** A or B. A is the safe one that loses nothing. B is the one that answers
what you actually described, a globe of dots with no geography, and it keeps the light
theme. C is the one I would avoid on an international floor, and D is the one to take only
if you want a deliberate dark frame in an otherwise white loop.

### Two generated candidates, measured

You generated two images and put them in `assets/gen/`. Both are 16:9, both pale, both
cool, both light enough for a white scene. Both are the B direction, a grid globe with no
landmass.

| Measure | AI Grid Pale | Globe AI Grid 3D |
|---|---|---|
| Pixels | 2730 by 1536 | 2720 by 1554 |
| Mean luminance | 228 | 225 |
| Sky above the globe | 232, cool by 11 points of red against blue | 233, same |
| Ink in the top 20 percent, where the beam sits | 0.5 percent | 0.0 percent |
| Ink in the 20 to 35 percent band | 25 percent | 17 percent |
| Bottom quarter mean luminance | 222 | 215 |
| Darkest point in the bottom quarter | 176 | 148 |
| Globe centre, as a fraction of width | 0.53 | 0.49 |

**What those numbers mean on the frame.**

1. **The beam.** Scene 11 draws its own red horizon at 17.5 percent of the svg. Both images
   keep that band nearly empty, so neither one fights the beam. Globe 3D keeps it cleaner,
   because its sphere starts lower and leaves more air under the line.
2. **The column labels.** Datacenter, Cloud, Sovereign cloud and Edge sit near the bottom of
   the visual, and Globe 3D is 7 points darker there with a darkest point of 148 against
   176. That is the one place on this frame where the art can genuinely hurt legibility,
   and it hurts the 3D globe more.
3. **Balance.** The visual is padded 130 pixels from the left to clear the layer rail, so
   the optical centre of the free area sits right of frame centre. Pale's globe at 0.53 is
   already sitting there. Globe 3D at 0.49 lands behind the rail's column and reads left
   heavy.
4. **Motion.** Globe 3D has volume and shading, so the scene's one art drift, a slow scale
   from 1.01 to 1.06, reads as a sphere breathing. That is a second motion system next to
   the four plane drifts at 9, 11, 14 and 17 seconds. Pale is flat, so the drift stays
   quiet and the red geometry keeps the movement.

**Recommended: AI Grid Pale.** Not because it is prettier, because it keeps the contrast
hierarchy intact. On this frame the order of attention has to be red beam, red tethers,
icons, background. A shaded sphere puts the darkest mass on the screen directly behind the
smallest text.

**One finding that applies to either choice.** Scene 11 currently sits at 0.18 opacity, and
at 0.18 these images are invisible: a mean luminance of 225 composited on white at 0.18
comes out at 250, which is white to the eye at three metres. The visible part is the grid
lines, not the wash. At 0.45 the lines land around 207 and the wash around 241, which is
present and quiet. **The build needs 0.45 for this scene, not 0.18.** The current substrate
was designed to sit at 0.18; these were not.

**Preview:** `inference-booth-screen/preview/scene11-art-test.html`. Keys 1, 2 and 3 switch
between the current substrate and the two candidates, `o` cycles opacity through 0.18,
0.28, 0.40, 0.55 and 0.70, and the rail is on frame at the real v1.2 words because the
label collision is part of what is being judged.

### The environments come from the customer deck

You pointed at slide 5 of the Red Hat AI customer deck and asked for the environment icons
that deck uses, so the booth and the deck speak the same vocabulary.

**What that slide contains.** Six environments and one foundation, all black line art, each
with a short red rule under it: Physical, Virtual, Private Cloud, Sovereign Cloud, Public
Cloud, Edge, over a Hardware Acceleration band that carries the NVIDIA, AMD, Intel, Google,
AWS and IBM logos. The logos do not come with it. Third party marks are barred from the
screen, and the silicon row is a different claim from this frame's.

**What the icon repository already had.** Slide 5's six are near identical to six icons in
the Red Hat Icon Repository deck we used for the Agentic AI glyph, at 360 square and in red:

| Deck name | Repository icon | Match |
|---|---|---|
| Sovereign Cloud | `env-sovereign-cloud-239.png` | frame, cloud, padlock. Effectively exact |
| Public Cloud | `env-public-cloud-169.png` | plain cloud. Exact |
| Edge | `env-edge-198.png` | cloud inside a dotted ring. Same idea, tighter halo |
| Private Cloud | `env-private-cloud-179.png` | cloud with a padlock in the deck, a keyhole here |
| Physical | `image248` | deck is a flat server bar, repository is a server on a stand |
| Virtual | `image225` | dashed box around a server bar, close |

So four of the six are clean matches, and the ones we need are the four clean ones.

**DECIDED: the four named in the support line, in the order the support line reads.**

| Position | Name | Icon | Size |
|---|---|---|---|
| 1 | Sovereign Cloud | frame, cloud, padlock | 64 |
| 2 | Private Cloud | cloud with keyhole | 56 |
| 3 | Public Cloud | plain cloud | 48 |
| 4 | Edge | cloud in a dotted ring | 40 |

- **Sovereign first, edge last, because the support line already says "Sovereign to edge".**
  The frame now reads in the same order as the sentence under it, which it did not before.
- **Captions come back.** Two of the four are clouds, and without words they are two clouds.
  The deck's whole point is that these are named environments, and the four names are what
  makes the deck's lineup legible at a glance.
- **Datacenter is retired from this frame.** Private Cloud carries the on premises idea, and
  the deck does not name a datacenter. If you would rather keep the word, the substitution is
  one caption.
- **The size still descends left to right**, 64 to 40, so the row keeps a sense of depth even
  though nothing hangs from anything.
- **Red, not black.** The deck draws these in black with a red rule. The screen is red line
  art on white, so the glyphs land in red and the rules are red too. The vocabulary matches
  the deck; the medium does not have to.

**A rule under each icon, deck style.** The deck puts a short red rule under every
environment, and that solves the problem the floating version had: four small objects with
nothing under them look unanchored. Four short rules give each one a ground, echo the deck
exactly, and mean the long beam is not needed at all.

### The art question closes itself: the substrate stays

You went with key 1, which is the ridge the scene already had. So after the globe, the pale
grid, the four Gemini prompts and two generated images, scene 11 keeps the art it shipped
with, and what changes is the diagram on top of it.

**That is a good outcome, not a wasted detour.** It removes the last external dependency in
the build: no image to generate, nothing waiting on a model I cannot reach, nothing to
re-render if the panel looks different. The frame now depends only on assets already on
disk.

**One number to carry over correctly.** The 0.45 opacity finding does not apply here. It was
measured on the two generated images, which are pale: mean luminance 225. The existing
substrate is a photograph and much darker, mean luminance 148 with a darkest point of 90.
At 0.18 it composites to a mean of 236. **You set 0.70**, which is a deliberate lift: it
composites to a mean of 180 and a darkest patch of 139, so the ridge becomes a visible
landscape instead of a whisper. That is the right call for a frame whose subject is now the
four environments, because the backdrop finally does something.

**What 0.70 costs, measured, and the one fix it needs.** Captions cannot stay in ink-2 at
this opacity.

| Opacity | Caption in ink-2 (#6A6A6A) | Caption in ink (#151515) |
|---|---|---|
| 0.18 | 4.6 to 1, worst 4.1 | 15.4 to 1, worst 14.0 |
| 0.45 | 3.5 to 1, worst 2.6 | 11.7 to 1, worst 8.9 |
| 0.70 | 2.6 to 1, worst 1.6 | 8.8 to 1, worst 5.4 |

Ink-2 at 0.70 is 2.6 to 1 on average and 1.6 to 1 over the dark part of the photograph, which
is invisible. So the captions go to ink, which is the change that carries the legibility.

**You then turned the halo off, and that is a defensible call with one number behind it.**
The halo existed to rescue ink-2, not ink. With ink at 0.70 the worst patch on the frame is
5.4 to 1, which clears the 4.5 to 1 bar for text this size without any backing. So the
captions sit directly on the photograph by choice, and they hold. The one thing the halo was
also doing is smoothing the photograph's texture out from behind the letters; without it the
captions inherit some of that texture. That is a look, not a failure, and it is one class to
put back if the panel says otherwise.

**Final geometry, 1000 by 320 viewBox.**

| Position | Caption | Icon | Size | Icon top |
|---|---|---|---|---|
| x 160 | Sovereign Cloud | frame, cloud, padlock | 64 | 136 |
| x 380 | Private Cloud | cloud with keyhole | 56 | 144 |
| x 600 | Public Cloud | plain cloud | 48 | 152 |
| x 820 | Edge | cloud in a dotted ring | 40 | 160 |

- Red rule under each at y 214, 80 wide, 3px, centred on each column.
- Captions at y 262, 24px, ink, centred, no halo.
- Parallax kept, 14, 10, 7 and 4 pixels on 9, 11, 14 and 17 second alternates.
- No long beam. The four short rules do that job.
- Substrate at 0.70, art drift unchanged.
- The rail sits on this frame at the **new** verbs, Deliver current, and the visual keeps its
  130px left padding so the rail column clears the Sovereign Cloud icon.
- The four red icons carry a white drop shadow glow, two passes at 2px. At 0.70 they stand on
  a photograph instead of near-white, and thin red line art loses its edge against a busy
  patch without it. This is the one thing on the frame that exists purely because the
  opacity went up.

**Locked on your call, six switches together: art 1 current ridge, a red rule under each, deck
style, captions on, opacity 0.70, caption halo off, icon glow on.**

**DECIDED, and this closes the last stop.**

**Preview:** `inference-booth-screen/preview/scene11-deck.html`. Opens on exactly the locked
state, including the rail at the new verbs and the caption and glow switches where you left
them. Keys 1, 2 and 3 switch the art, `b` cycles the
under structure, `c` toggles the captions, `o` cycles opacity, `h` toggles the caption halo,
`g` adds a white glow behind the red icons if they fight the photograph.

---

### Superseded: the floating version, no captions

Kept for the trail. This is the frame you ruled on before the deck icons came up.

You chose the second reading of your own note, and the instruction was three parts: shrink
the four environment icons, delete the four captions, delete the four red tethers, and float
the icons over the globe instead of hanging them off the beam.

**DECIDED: Globe AI Grid 3D, at 0.45, with the four environments floating and unlabelled.**

- The globe lives on this scene only. Scene 6 does not get it. Confirmed.
- Datacenter, Cloud, Sovereign cloud and Edge lose their captions. The support line already
  says "Sovereign to edge", so the four names are not the only place the claim appears.
- The four tethers are deleted. Nothing is attached to anything.
- The icons shrink from 64, 54, 46 and 38 to 56, 46, 38 and 30, and the sizes still carry
  the depth: nearest is largest.
- The parallax stays. Four drift speeds on four floating objects is the scene's one motion,
  and without tethers it reads better, because a floating icon that drifts looks alive while
  a tethered one that drifts looks broken.
- Opacity goes from 0.18 to 0.45, for the reason measured above. At 0.18 the globe is white
  on white.

**What deleting the tethers costs, stated plainly.** The frame no longer draws a causal
chain from one service beam down to four environments. It now shows four kinds of place
floating in front of a world. That is a weaker drawing of "delivered from one place" and a
stronger drawing of "everywhere you are". The headline still says "Deliver AI as a service",
so the verb survives in words rather than in geometry. If that turns out to be too weak on
the panel, the fix is not the tethers, it is the beam.

**One thing I will not guess at: the beam.** Delete the lines and the horizontal service
beam becomes the only line left on the frame, and with nothing hanging from it, it is a rule
across the top. Three arrangements, all in the preview on one key:

| Mode | Frame | Read |
|---|---|---|
| Beam above, gap under it | A red rule at 58, icons floating 80 below | Service layer exists, environments are not visibly attached to it |
| No beam | Icons only, floating over the globe | Cleanest. The globe carries everywhere, the icons carry which kinds of place |
| Icons on the beam | Four equal icons sitting on the rule | Keeps the causal read without tethers, but a single line of four equal things loses the depth |

My pick is no beam, because a rule with nothing on it is decoration, and the frame is
stronger when every element is doing work. But this is a taste call on your screen, so the
preview has all three.

**Preview:** `inference-booth-screen/preview/scene11-float.html`. Keys 1, 2 and 3 switch the
art, `b` cycles the three beam arrangements, `o` cycles opacity.

**DECISION:** superseded by the deck version above. The globe was dropped and the captions came
back, so none of the three beam arrangements is the build. Kept for the trail only.

---

## No open items

Scene 7 Runtime, scene 11 if option C, scene 14 Payoff, scene 15 Business impact, scene 16
Closer. Hands off unless you raise something.

---

## Cross cutting, decided already

These are not re opened per scene.

1. 6.4 second rhythm, 102.4 second loop.
2. Scenes 5 and 16 stay a matched pair.
3. Every stat keeps its credit.
4. Zero em and en dashes.
5. No third party names, logos or model names on glass.
6. One calm continuous animation per scene.
7. Upper 40 percent of art stays empty.
8. Zero network requests.

## Assembly checklist

When the last `DECISION` line is filled, the build prompt is assembled from:

1. Every DECIDED block, in scene order. Some scenes carry a `DECISION:` line and some
   carry a `DECIDED:` block; both are rulings and both go in.
2. The acceptance checks V1 to V14 in the v1.3 prompt.
3. The documents and validator table, so copy and checks move in the same pass.
4. Appendix A of the v1.3 prompt, if scene 11 takes an image.
5. The prerequisites table, with the icon file and the guardrail confirmation closed out.
