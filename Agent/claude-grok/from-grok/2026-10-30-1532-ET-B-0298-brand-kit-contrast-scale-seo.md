Sent: 2026-10-30 15:32 ET

# B-0298 Brand Kit: large-text contrast, scale 500 differs from the main colour, title brand
Priority: P3 · Estimated effort: S · Report: QA-REPORT-157 · Source: live probe 2026-10-30 ~15:28-15:31 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A small business owner gets a kit they can trust for real accessibility decisions and hand straight to a developer.

## Why
No GSC row in the analytics raw file for this page.
Checked live (15:30 ET): brand "Acme Test", default #2563EB → ZIP with acme-test-brand-sheet.pdf, -colors.css, -tokens.json, -palette.svg ✔. Contrast checked by formula: #2563EB on white 5.17 (shown 5.1:1 AA ✔); #EB2563 4.22 (shown 4.2:1 Fail); #EBAD25 1.99 (shown 1.9:1).
- #EB2563 at 4.2:1 is labelled "Fail" with no note that it passes AA for large text (3:1). A user may throw out a usable heading colour.
- The shade scale's 500 step is #1F5FEA while the chosen primary is #2563EB (CSS file, checked). Users expecting primary = 500 get a different colour.
Competitors (live search): DebugSwift reads colours off an uploaded logo and shows the colours on a website/card/post mockup; Ultimate Design Tools exports Tailwind v3/v4 and DTCG tokens and adds the Google Fonts @import; CommonNinja exports a PNG brand board.
FreeDailyPro: logo colour pick and Tailwind export — not in the control list (checked).
Title ends without "| FreeDailyPro" (checked); meta 123. Trial: 2 uses/day; the ZIP used one. /es title English → L-189.

## Who uses this
Founders and freelancers setting up a brand.

## Outcomes (ranked)
1. Show "AA large" (≥3:1) as well as AA/AAA, on page and in the PDF.
2. Make the scale step nearest the primary equal the primary, or label which step it is.
3. Snippet with brand suffix; optional Tailwind export and font @import in the CSS.

## SEO
- Now: title "Brand Kit - Colour Palette, Contrast Checks, Brand Sheet" (56, no brand); meta 123; H1 "Brand Kit"
- Keywords: brand kit generator, brand colour palette, brand style guide, brand sheet pdf
- Suggested Title: "Brand Kit Generator: Palette, Contrast, Fonts | FreeDailyPro" (60)
- Suggested Meta: "Turn one brand colour into a palette, ten-step shade scale, WCAG contrast checks and a font pairing, then download a ZIP with brand sheet PDF, CSS and tokens." (158)
- Suggested H1: "Brand Kit Generator"
- FAQ: What is in the ZIP? · Are the fonts free for commercial use? · What do AA and AAA mean? · Can I use my own colour?

## Constraints
Download gating at 0 trial uses is fine; keep it local.

## Test cases
1. #2563EB → ZIP has PDF, CSS, JSON, SVG (regression).
2. #EB2563 → shows Fail for normal text and Pass for large text.
3. Primary #2563EB → a scale step equals #2563EB or the label says which step is closest.
4. Ratios shown match the WCAG formula to 1 decimal.
5. Title ≤60 with brand, meta 140–160; 390 px no overflow.
