Sent: 2026-10-30 12:08 ET

# B-0172 Color converter: say when input is invalid or clamped; add OKLCH/LAB
Priority: P2 · Estimated effort: S · Report: #117 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Never show a black swatch for a typo, and support the modern CSS colour spaces.

## Why
Conversions and WCAG contrast (including alpha) are exact. #GGGGGG blanks every field and shows #000000. rgb(300,0,0) silently becomes red. colordesigner.io lists LAB/LCH/OKLCH (×27).

## Who uses this
Designers and front-end devs (50 GA views).

## Outcomes (ranked)
1. An inline "Not a valid colour" message, keeping the previous result. 2. "Clamped 300→255" notice. 3. OKLCH and LAB rows.

## Constraints
Keep the current formats and contrast readout.

## Test cases
#GGGGGG → message, the swatch doesn't change to black. rgb(300,0,0) → notice. #6366f1 → oklch(58.5% 0.2 277) ±0.5.
