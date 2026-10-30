Sent: 2026-10-30 11:48 ET

# B-0161 Image enhancer: no dead Apply, before/after compare, clear upscale presets
Priority: P2 · Estimated effort: S · Report: #114 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every click should visibly do something, and users should see the improvement.

## Why
Apply with nothing ticked silently does nothing. imgupscaler pushes 2x/4x/8x (×122). FDP's honest "doesn't invent detail" is good, but the presets should be visible.

## Who uses this
People fixing dull or old photos and scans (13 GSC impressions, position 6.5).

## Outcomes (ranked)
1. Disable Apply until an option is on, or pre-tick Sharpness + Clarity. 2. A before/after slider. 3. Upscale presets 2x/4x showing the output pixel size.

## Constraints
Keep it non-AI and keep the honest copy.

## Test cases
Nothing ticked → Apply is disabled or a hint shows. 200×150 at 2x → "400×300" shown and the file is 400×300.
