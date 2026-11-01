Sent: 2026-11-01 08:52 AM ET
# AUDIO & SCREEN TEST KIT (owner-approved build) - B format

**Working with us:** you're our build partner, not an order-taker. Inspect the real codebase, reuse existing tool-page, registry, trial-meter and FAQ/schema patterns, challenge anything weak, and choose the best implementation. Full plan (features, competitors, tests, API/MCP): /workspace/freedailypro-growth-orchestrator/plans/2026-11-01-audio-screen-test-kit-plan.md (summary here).

## Intent
Ship a hub plus 6 on-device browser test pages that are the best and easiest on the web for "check my speakers/earbuds/sub/screen/hearing" and "help me sleep": one tap, an answer in under a minute, nothing uploaded, no mic, no ads, phone-friendly.

## Why
Santosh approved this Nov 1, 8:51 AM ET. YouTube views on these intents total ~1.6B (noise 1.06B, bass 300.7M, stereo 145.7M, hearing 54.3M, tone 42.1M, dead pixel 13.4M + fixer 3.68M). No such page exists in our sitemap. Rivals (soundtester.net, soundtest.app, speaker-test.com, szynalski, onlinetonegenerator, coderspace, jscreenfix, deadpixeltest.org, myNoise, Noisli) are free and signupless, so friction loses us the audience.

## Tier decision
**Professional Tools.** Running and listening to every test is un-metered and needs no sign-in. Output actions (WAV export, result-card download/share, saved/printed pixel report) count as 1 Professional Tools trial use per visit (10/day), charged on delivery, per the standing owner rule. Not Premium, not Workflow. Premium extras are deferred until Santosh decides; don't build them.

## Outcomes per page
1. **Stereo L/R + phase.** *Intent:* tell in 10 s whether left/right work, are swapped, mono or unbalanced. *Outcome:* L/R/Both + guided L->R->Both->phase run, spoken "left/right" cues, big side indicator, balance/centre check, in/out-of-phase test, diagnosis quiz with a fix per result, pass/fail card, keyboard L/R/B/Space, phone-mono warning.
2. **Bass/subwoofer sweep.** *Intent:* "how low does my setup go, where does it rattle". *Outcome:* 20-200 Hz log sweep (10-300 selectable) with live Hz, fixed tones 20/30/40/60/80 Hz, lowest-note finder showing "Your bass reaches ~X Hz", rattle finder (mark Hz, replay), sub phase 0/180, L/R/Both, WAV export, auto-stop, low start below 30 Hz, car-audio presets + short placement/crossover guide. Bar: soundtester.net/bass-test.
3. **Tone generator + sweep.** *Intent:* precise tones without ads. *Outcome:* Hz entry + slider + fine keys (0.01 Hz, octave x2/x1/2), note names, 4 waveforms, lin/log sweep, L/R/Both, share link that restores settings, WAV export longer than rivals' 10 s (you pick a safe cap).
4. **Hearing-age test.** *Intent:* fun, honest "how old are your ears". *Outcome:* 1 kHz calibration, per-ear rising HF sweep, press when it fades, result in Hz per ear, shareable card, "not a medical test". **Age bands only from a cited, owner-approved published table; never invent one.** Until Santosh approves a source, ship Hz-only (no age claim).
5. **Dead pixel test + stuck-pixel fixer.** *Intent:* check a screen before the return window closes, try to fix a stuck pixel. *Outcome:* one-tap fullscreen, 10+ colours + gradients + backlight-bleed screen, auto-cycle, arrows/Space/Esc and tap/swipe, hidden cursor, tap to mark a pixel (coords + resolution), launch fixer at the mark (movable, resizable, per-dot random flash, 10 min/1 hr countdown) only after a mandatory photosensitivity warning, dead/stuck/hot/dust guide, return-window checklist with no invented retailer thresholds.
6. **Noise mixer + sleep timer.** *Intent:* beat "press play on a 10-hour video". *Outcome:* live-generated endless white/pink/brown/grey + fan/rain-like layers with per-layer sliders, presets in the URL, sleep timer 15/30/60/90 with gradual fade-out, keeps playing with screen off where supported (Media Session), no signup.
**Hub:** "Audio & Screen Test Kit" (slug your choice) linking all 6, a "new device check" path (stereo->bass->pixel), /category/audio-tools and related live tools (audio-comparer, audio-normalizer, ringtone-maker, screen-recorder, screenshot-tool).

## SEO
Titles: "Left Right Speaker Test: Stereo Sound Check | FreeDailyPro", "Bass Test: Subwoofer Sweep 20-200 Hz | FreeDailyPro", "Dead Pixel Test & Stuck Pixel Fixer | FreeDailyPro"; you write the other 3 and the hub, all <=60 chars and containing "FreeDailyPro" (CAP-384 failed on that). Metas/FAQs in /workspace/freedailypro-seo-engine/hourly/2026-11-01-1000-audio-screen-test-kit-benchmark.md. "Free" only in title/meta/og/schema, never visible UI; site count "300+".

## Constraints
No AI features. All audio/pixel work client-side; no mic/camera permission; no audio network requests. Audio safety on every page: low default volume (~25%), click-free ramp-in, "lower your volume first" notice before first sound, extra caution/cap for <30 Hz and >12 kHz, default auto-stop, big Stop + Space/Esc. Signed-out visitors must never be auto-redirected to Google (P1 bug filed). Premium extras and API/MCP are out of this build unless sharing the WAV code makes tone/sweep/noise endpoints trivial; if so, propose first (see plan section 10).

## Acceptance tests
- Stereo: L only left, R only right, Both centred (wired headphones + analyser); out-of-phase audibly hollow; each quiz branch gives correct fix; card renders.
- Bass: live readout within 1 Hz of generated; finder returns tapped Hz; rattle marks replay exact Hz; 180 phase inverts; WAV correct length/rate/frequency (FFT) and plays in VLC.
- Tone: 1 kHz entry measures 1000 +/-0.5 Hz; sweep endpoints correct; share link restores all settings; WAV length matches.
- Hearing: calibration required; per-ear routing; result = Hz at press; no age shown without visible citation.
- Pixel: solid edge-to-edge colours; Esc exits; interval honoured; mark saves coords; fixer blocked until warning accepted, stops on Esc/tap.
- Noise: no audible loop seam over 10 min; timer fades and stops; preset URL restores.
- All: Chrome, Safari macOS/iOS, Firefox, Edge, Android Chrome; 360 px layout; keyboard-only; visible focus; ARIA live region names channel/Hz; AA contrast; no permission prompts; trial counter moves only on export/share (1 per visit); volume warning visible before first sound.

## Process
Inspect -> restate -> propose (flag disagreements) -> implement (phase 1: hub + stereo + bass + pixel; phase 2: tone + noise + hearing) -> verify on the live build.

## Reply requested
Reply in from-claude/ with a **status per page** (hub + 6): slug, commit, LIVE / PUSHED-UNCHECKED / BLOCKED, and any deviations. We promote nothing until Testing Bot's live check passes.

Source: owner
