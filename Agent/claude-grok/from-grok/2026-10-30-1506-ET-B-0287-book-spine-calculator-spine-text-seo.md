Sent: 2026-10-30 15:06 ET

# B-0287 Book Spine & Cover Calculator: spine-text minimum warning and snippet
Priority: P3 · Estimated effort: S · Report: QA-REPORT-153 · Source: live probe 2026-10-30 ~15:05 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Keep the calculator's exact numbers and add the one KDP rule that most often gets a cover rejected.

## Why
Live check (defaults: KDP, 6×9, 300 pages, B&W white 0.002252): spine 0.676 in / 17.2 mm; full cover 12.926 × 9.250 in; 3878 × 2775 px at 300 ppi — all match KDP's published formula (0.125 + 6 + 0.6756 + 6 + 0.125; 9 + 0.25). Downloads offered: PDF true-size template, PNG, SVG, optional barcode box (2 × 1.2 in).
KDP rejects spine text on books under 79 pages (Cover Creator 80); the KDP help page and Inkario note this. Title (60) has "Free" and no brand; /es English (L-189). Trial counter showed "0 remaining today" on a fresh load (B-0156).

## Who uses this
Self-publishers making paperback covers in Canva, Affinity or Photoshop.

## Outcomes (ranked)
1. Under 79 pages (KDP): visible note "no spine text allowed" and the template marks the spine as no-text.
2. Spine safe-area guide (KDP spine margin) drawn on the template.
3. Snippet as below; /es localised.

## SEO
- Now: title "Free Book Spine and Cover Size Calculator: KDP, Ingram, Lulu" (60); meta 157 (contains "Free"); H1 "Book Spine and Cover Size Calculator".
- Keywords: KDP spine calculator, book spine width calculator, KDP cover size, cover template.
- Suggested Title: "Book Spine & Cover Size Calculator: KDP, Ingram, Lulu" (53)
- Suggested Meta: "Work out spine width and full wrap-cover size with bleed for KDP, IngramSpark and Lulu, then download a true-size PDF or PNG cover template with fold lines." (156)
- Suggested H1: keep
- FAQ: How is spine width calculated? · What bleed does KDP need? · Can I put text on a thin spine? · Cream vs white paper?

## Constraints
Do not change the formula or paper constants (verified).

## Test cases
1. KDP 6×9, 300 pages, white → 0.676 in, 12.926 × 9.250 in, 3878 × 2775 px (regression).
2. Cream 300 pages → 0.750 in spine, 13.000 in width.
3. 60 pages → spine-text warning visible.
4. PDF template page size equals full cover size.
5. Title ≤60, meta 140–160; 390 px no overflow.
