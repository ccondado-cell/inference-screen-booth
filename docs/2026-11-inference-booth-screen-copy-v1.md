# Inference Booth Screen: Copy Document v1.3

Nov 19, 2026. Narrative source of truth: Red Hat AI Messaging Guide (Nov 2026).
Evidence sources: EnMaaS blog + deck (Nov 2026), vLLM blogs (Jul/Sep 2026), MLPerf Inference v6.0, Forrester TEI (Feb 2026).
Build method: `2026-11-booth-screen-playbook.md`. Engine cloned from `rhai-agentic-ai-booth-screen` (v3.6).

## Locked decisions

- **Opening thesis:** "Inference worth scaling." with "Models you own. Costs you control." (scene 1). The price frame is stated on scene 3 ("The bill outgrows the budget.") and proven on scene 13 ("Up to 70% lower token costs."), which is where it has evidence.
- **The mantra scene is deleted, not edited.** Scene 12 used to carry the five verbs as a standalone statement. It is gone: Deliver (11) cuts straight to the trillion (12). The frame stood between the last spine claim and the first piece of proof, and the rail already names the five verbs on scenes 7 to 11.
- **Renumbered at v1.3.5.** Fifteen scenes, 96 second loop. The old 13 to 16 are now 12 to 15, and this document uses the new numbers throughout. Older notes in the decisions file keep the old numbers and say so.
- **Closing outcome:** "Become an AI model provider." (scene 15) with "Your models. Your prices. Your rules." underneath. Verbatim outcome language from the Red Hat AI 3.6 deck and the messaging guide.
- **The closer stands alone.** It carries no pronoun and no implied antecedent, so a visitor who walks up cold gets the whole frame. In an attract loop the closer is the scene most likely to be seen first, because it is when people stop walking.
- **Scene 5 and scene 15 are a matched pair.** "Their models. Their prices. Their rules." inverts line for line to "Your models. Your prices. Your rules." Keep the two set identically or the inversion only lands on memory. Accepted risk: "Your rules" could read as a jab at a hyperscaler to a partner who sees only scene 15; the headline above it defuses that, because the reader is becoming a provider too.
- **Spine (7-11), verb-led, control word in red:** Run / Optimize / Distribute / Gate / Deliver
- **Layer stack carries the same five verbs,** one per spine scene, so the rail and the frame beside it name the same action. It is hidden on scene 6, which shows all five names on its own canal: the same five words never share a frame with themselves. Scene 7 is the one frame where a diagram label and a rail word differ on purpose: the red node under the transit says "Runtime" (the component) while the rail says "Run" (the action). Accepted, not an oversight.
- **Scene 6 shows the five verbs before the rail appears.** "One request. One path. Five layers." then a canal with five stations that fill in order, ending on a full pipeline. The words "AI as a service" are reserved for scene 11, which is their payoff.
- **Scene 7 carries modality breadth** ("any model, any modality, any chip", echoing the official tagline pattern) with the MLPerf leading-performance credit. Voice is covered here; no separate voice scene.
- **Scene 8:** "Optimize in the open." Open source implied by headline, proven explicitly at scene 13 (adoption flip).
- **Scene 9 shows routing, not just plumbing.** Same marker, same accelerator, twice: affinity by context, not round robin. No cache rates, no percentages.
- **Residency:** lives at scene 11 only ("where your data lives"). Scene 10 now carries the gateway mechanics (identity, rate limits, guardrails); the residency phrase was cut because scene 11 is where the four environments make it true.
- **Scene 12 is a rate, drawn, not a still.** A trillion a month is a rate, so the frame shows one: seven lanes of ink tokens converge at 520 units per second, a faint field of 96 faster ghosts runs behind them so the stream reads as countless rather than as seventy, and the three node agent loop spends every arrival writing a code panel on the right, fifteen lines, then a red commit rule, then the next panel. Three panels per cut. No words, no digits, no third-party marks on the frame: the headline carries the number and the credit carries the source. The generated river render is retired but kept on disk; the still read as texture, and a texture cannot show a rate.
- **Movement 3 evidence order:** our scale (1T tokens, powering Red Hat's Agentic SDLC) → token-level proof on our own estate (EnMaaS pilot, 70%) → independent validation (Forrester TEI). The proof arc ends on a third party rather than our own pilot data.
- **"Leading" not "best"** for all MLPerf-grounded claims (brand-safe, objection-proof).
- **EnMaaS pilot numbers are cleared for public booth use** (Carlos, Nov 18).
- **60B weekly tokens dropped** (internally benchmarked; the 1T/month figure is the public one).
- **Rejected:** "Serve" (CTO), "Squeeze" (informal), "Frontier" (connotes closed chat assistants), "best" (brand guidelines), vendor/model names on screen, Verizon by name, Inferact comparison (one-on-one only + competitor name), separate voice scene (narrowed the story; folded into scene 7), "Pay less for every one" (sold a discount, not an outcome), "Now you set the price" as the closer (failed the standalone test: "the price" needs a scene the visitor may not have seen), "Go from token consumer to AI provider" (seven words at the cap on the scene that should be shortest), a world map on scene 11 (illegible at 3 m, invites geography questions).

## Copy limits (validated per pass)

Headlines ≤ 7 words. Support ≤ 12 words. No em or en dashes. 3-second read per scene. Every stat carries a credit. No consumer assistant names, vendor logos, third-party agent names, or competitor names.

## The 15 scenes

| # | Movement | Headline | Support | Credit | Visual (motion verb) |
|---|---|---|---|---|---|
| 1 | Open | Inference worth scaling. | Models you own. Costs you control. | None | Hero backdrop with the logo lockup above the headline, calm drift (drift) |
| 2 | Tension | AI demand and cost are compounding. | More users. More agents. More tokens. | None | One cost line draws left to right, flat then a hard turn up, and holds (draw) |
| 3 | Tension | The bill outgrows the budget. | Costs climb unpredictably as usage scales. | None | The same cost line, traced again, crossing a flat gray budget rule once at x 627 and holding above it (draw) |
| 4 | Tension | Scarce chips, stranded capacity. | GPUs idle in one cluster, exhausted in another. | None | One pool: two cold accelerators, one pegged; two requests are refused as a gray ring and rebound toward capacity they never reach (churn) |
| 5 | Tension | Inference chained to one provider. | Their models. Their prices. Their rules. | None | Three models stand inside one provider cloud; tokens run out to users, agents and apps; the provider fades and the consumers burn (starve) |
| 6 | Spine setup | Every token takes one path. | One request. One path. Five layers. | None | One canal, five stations; a token runs the canal and each station fills as it arrives, so the frame ends full (fill) |
| 7 | Spine: Runtime | **Run** any model, any modality, any chip. | Leading performance. Text, voice, vision. | MLPerf Inference v6.0, 2026 | Model, modality, and chip icons; dots flow through one runtime node (flow) |
| 8 | Spine: Optimization | **Optimize** in the open. | New models, validated and optimized in days, every month. | Red Hat AI validated models, 2026 | A model box compresses; exit spacing tightens 25 percent (compress) |
| 9 | Spine: Distribution | **Distribute** across the whole fleet. | 3× throughput. 2× faster first token. | llm-d + vLLM, 2026 | One fleet row; the same marker returns to the same accelerator three times, one new marker adopts a cold one (affinity) |
| 10 | Spine: Gateway | **Gate** every request. | Identity. Rate limits. Guardrails. | None | Fourteen dots at 480 units per second arrive at a gate; ten pass, four are stopped as hollow rings (stop) |
| 11 | Spine: Service | **Deliver** AI as a service. | Where your data lives. Sovereign to edge. | None | Four named environments (sovereign, private, public, edge), each on a red rule, four depth planes, parallax drift (parallax) |
| 12 | Scale | A trillion tokens a month. | Powering Red Hat's Agentic SDLC. | EnMaaS, Red Hat, 2026 | Seven lanes of tokens stream in at 520 units per second into a three node agent loop, which writes a code panel line by line, three panels per 6.4s cut (flow, then write) |
| 13 | Payoff | Up to 70% lower token costs. | Most of our traffic now runs open weight. | Red Hat EnMaaS pilot, 2026 | Columns flip 70/30 to 30/70, red share grows (flip) |
| 14 | Business impact | 233% ROI over three years. | GPU utilization, from 30% to 80%. | Forrester TEI, Feb 2026 | GPU utilization bars fill to 80% and hold (grow) |
| 15 | Closer | Become an AI model provider. | Your models. Your prices. Your rules. | None | Logo, hero backdrop, calm drift (drift) |

## Flags (before build locks)

1. **Scenes 2 and 3 carry no numbers by design.** A line chart is one axis label away from being an unsourced statistic, so the frame has no axis, no units, and no gridlines. It stays an illustration and needs no credit. If an approved external inference-spend forecast arrives later, it slots at scene 2 with a credit, and the chart becomes a figure.
2. **MLPerf freshness:** check whether a v6.x round lands before the show; the "leading" framing survives either way.
3. **Kimi on screen:** scene 8 support says "New models" without naming Kimi K3; the credit line carries the source. No model names on screen.
4. **Forrester TEI scope:** the study is platform-wide (composite, 4 interviews, on-prem focus). Scene 14's two stats (ROI, GPU utilization) are drawn from it as published; if the booth needs inference-only framing, the credit line "Forrester TEI of Red Hat AI" keeps attribution honest.
5. **Agentic SDLC on a public floor:** "Powering Red Hat's Agentic SDLC." is public language, published in the blog we cite and presented at KubeCon, so the precedent is public rather than internal. Confirmed with Carlos, Nov 18.

6. **"Guardrails" needs a hub match.** The word has zero hits in the Red Hat AI Messaging Guide (doc `1PxzWGjgHYHlvEmwNoOgH_9p3Zmfg3V0QuskvcU2N5oM`). Scene 10 support ships on the approved term if the hub confirms it, and falls back to "Identity. Rate limits. Policy." if it does not. This is the only copy line in the build that is not hub-sourced.
7. **Cross-screen vocabulary: Gateway vs Gate.** The governance screen's rail says "Gateway"; the inference screen's rail and scene 10 say "Gate". Both are correct in their own frame, and changing either now would desync the two screens' motion, so the difference is on the record and Carlos owns the call. No change made.
8. **Animation phases reset at scene entry.** Scenes 4, 6 and 9 restart their 6.4 second sequences when the frame is entered, and scene 5 resets its request clock, so a refusal, a fill, a cache hit or an outage always lands inside the scene it belongs to, including after an operator uses the arrow keys.

## Rejected at v1.3

- **"Router" as a station.** Scene 6 is five verbs, not five components. A router is an implementation detail and it broke the one-to-one mapping with the rail.
- **"Prefill" and "decode" as scene 9 labels.** They are correct and they are talk track material. On glass they added jargon without adding a decision.
- **Three model boxes with tether lines (scene 5 v1.2).** The cloud read as a waypoint the models reached. Making the cloud the container is what carries "chained."
- **"Data never leaves your control."** True, but it asserted residency through a negative. Scene 11 says where the data lives, positively, with four named environments.
- **The 1,000-dot density wall and the token thread (scene 12).** At 3 m it read as texture. The trillion is a headline claim; the art now carries "agentic" instead.
- **The horizon service beam and the globe (scene 11).** A beam with nothing hanging from it is decoration, and a globe invites geography questions the frame cannot answer in three seconds.
- **Two curves and two crossings (scene 3 v1.3).** Superseded at v1.3.2. Asking a visitor to compare two lines and read two crossings in three seconds was work without a decision. One line, one crossing, one idea: the bill passes the budget and keeps going.
