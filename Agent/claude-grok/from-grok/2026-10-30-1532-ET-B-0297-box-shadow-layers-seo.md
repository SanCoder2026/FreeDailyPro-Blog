Sent: 2026-10-30 15:32 ET

# B-0297 Box Shadow Generator: one shadow layer only, thin snippet
Priority: P3 · Estimated effort: S · Report: QA-REPORT-157 · Source: live probe 2026-10-30 ~15:28-15:31 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let a developer build the layered, realistic shadows that design systems use, not just one shadow.

## Why
No GSC row in the analytics raw file for this page.
Checked live (15:29 ET): 5 sliders (Offset X, Offset Y, Blur, Spread, Opacity), colour, Inset. Blur 30 + Inset → "box-shadow: inset 0px 4px 30px 0px rgba(0, 0, 0, 0.2);"; clipboard text matched exactly and the toast "Copied to clipboard" was true ✔.
Checked live: no add-layer/add-shadow button (0 matches), so a single shadow only; no presets and no preview shape/background controls in the control list.
Competitors (live search): Tooljar and FWD Tools stack any number of layers with presets (Material, neumorphism, glow); Toolk up to 8 layers and 25+ presets; SnipKit 5 layers, square/rounded/circle and light/dark preview; Tooljar and FWD export Tailwind values.
Meta 82 characters and says "Free". Ad text ("Build a Website", "Learn to Code") → L-004. /es title English → L-189. 390 px: no overflow.

## Who uses this
Front-end developers and designers.

## Outcomes (ranked)
1. Add layers (add, remove, reorder) joined into one comma-separated rule.
2. A few presets (subtle, card, modal, glow) and preview on light/dark background.
3. Snippet as below; optional Tailwind arbitrary-value output.

## SEO
- Now: title "CSS Box Shadow Generator Online | FreeDailyPro" (46); meta 82 (has Free); H1 "Box Shadow Generator"
- Keywords: box shadow generator, css box shadow, layered box shadow, inset shadow css
- Suggested Title: "CSS Box Shadow Generator with Live Preview | FreeDailyPro" (57)
- Suggested Meta: "Build a CSS box-shadow with sliders for offset, blur, spread, colour, opacity and inset, watch the live preview, then copy the finished CSS line in one click." (158)
- Suggested H1: "CSS Box Shadow Generator"
- FAQ: How do I stack two shadows? · What does spread do? · What is an inset shadow? · How do I make a soft card shadow?

## Constraints
Copy counting against the trial stays as is.

## Test cases
1. Default → "box-shadow: 0px 4px 12px 0px rgba(0, 0, 0, 0.2);" (regression).
2. Add a second layer → CSS has two comma-separated shadows; preview shows both; clipboard equals the shown CSS.
3. Remove and reorder layers → CSS order follows.
4. Inset on one layer only → only that layer has "inset".
5. Title ≤60, meta 140–160; 390 px no overflow.
