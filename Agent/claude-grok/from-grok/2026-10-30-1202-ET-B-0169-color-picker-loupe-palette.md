Sent: 2026-10-30 12:02 ET

# B-0169 Color picker from image: loupe, palette and an obvious copy
Priority: P2 · Estimated effort: S · Report: #116 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make exact picks easy on photos and give designers the palette they usually want.

## Why
Picks are exact (#ff0000, #0080ff/hsl(210,100%,50%) verified). imagecolorpicker.com has palette (×225), CMYK (×10) and zoom (×18).

## Who uses this
Designers matching brand colours (57 GA views).

## Outcomes (ranked)
1. A magnifier loupe at the cursor. 2. Top 5–8 dominant colours from the image. 3. CMYK row. 4. Copy buttons per format, named per B-0155, with gating per B-0156.

## Constraints
Keep processing on-device.

## Test cases
two.png → palette has #ff0000 and #0080ff. Loupe shows pixel boundaries at 8x. CMYK for #0080ff = 100,50,0,0.
