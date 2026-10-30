Sent: 2026-10-30 15:20 ET

# B-0293 Border Radius Generator: false "Copied" toast, elliptical corners, title over 60
Priority: P2 · Estimated effort: S · Report: QA-REPORT-155 · Source: live probe 2026-10-30 ~15:17-15:20 ET (headless, logged out, 1280/390 px), live competitor search; no GSC rows for these pages in the analytics raw file

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A quick, trustworthy way to get the exact border-radius CSS, including blob shapes.

## Why
Checked live (~15:19 ET): per-corner sliders 0–200 px; unlinked TL 10, TR 40, BL 0, BR 80 → "border-radius: 10px 40px 80px 0px;" — correct clockwise order ✔; preview matches.
Switching to % changed BR from 80 to 50 ("10% 40% 50% 0%") without telling the user — checked live.
Bug (checked live): at 0 trial uses ("Trial: 10 uses/day · 0 remaining today"), Copy CSS shows "Copied to clipboard" while the paywall opens and the clipboard stays empty (read back as ""). Same pattern as L-216 / B-0156. Copy counting against the trial stays; only the toast is wrong.
Checked live: four radius sliders only and output never uses the slash form, so elliptical (8-value) corners and blob presets are not offered.
Competitors (live search): A2Z Tools, WebToolar, AnyTool and MyToolStudio offer 8-value elliptical radii, blob presets/randomiser and units beyond px/% (rem/em); WebToolar and MyToolStudio copy Tailwind.
Title 62 (over 60, has "Free"); meta 85. /es title English → L-189. Ad text ("Build a Website") → L-004.

## Who uses this
Front-end developers and designers.

## Outcomes (ranked)
1. Show the paywall without a "Copied" toast when nothing was copied.
2. Elliptical mode (horizontal / vertical radius per corner) with a blob preset.
3. Tell the user when switching to % caps a value at 50%.
4. Snippet as below.

## SEO
- Now: title "CSS Border Radius Generator - Free, Visual Tool | FreeDailyPro" (62, has Free); meta 85; H1 "Border Radius Generator"
- Keywords: border radius generator, css rounded corners, border-radius css, css blob shape
- Suggested Title: "CSS Border Radius Generator: Per-Corner | FreeDailyPro" (54)
- Suggested Meta: "Shape rounded corners visually: link all four or set each corner in px or %, watch the live preview and copy border-radius CSS shorthand for your stylesheet." (157)
- Suggested H1: "CSS Border Radius Generator"
- FAQ: What order are the four values? · px or %? · How do I make a blob shape? · Why does 9999px make a pill?

## Constraints
Do not raise copy limits; keep trial counting.

## Test cases
1. Unlinked 10/40/0/80 px → "border-radius: 10px 40px 80px 0px;" (regression).
2. At 0 trial uses, Copy → paywall, no "Copied" toast.
3. Elliptical TL 30%/30% … → output uses the slash form and the preview matches.
4. px → % with a value above 50 → visible note.
5. Title ≤60, meta 140–160; 390 px no overflow.
