Sent: 2026-10-30 15:10 ET

Supersedes: batch-72/report-153/2026-10-30-1506-ET-B-0287-book-spine-calculator-spine-text-seo.md (that file wrongly said there was no under-79-page spine-text warning; it is left unedited).

# B-0287-v2 Book Spine & Cover Calculator: spine safe area on the template, and snippet
Priority: P3 · Estimated effort: S · Report: QA-REPORT-153 · Source: live probe 2026-10-30 ~15:05 ET, admin run ~15:07-15:09 ET (downloads in batch-72/downloads/), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Keep the calculator's exact numbers and make the downloaded template carry every KDP guide a designer needs.

## Why
Live check (KDP, 6×9, 300 pages, white): spine 0.676 in; cover 12.926 × 9.250 in; 3878 × 2775 px — matches KDP's formula.
Admin run at 60 pages: the page warns "Under 79 pages the platform does not allow text on the spine. Keep the spine area clear of text." ✔ Results 0.135 in spine (60 × 0.002252 = 0.1351), 12.385 × 9.250 in, 3716 × 2775 px ✔.
Templates verified (batch-72/downloads):
- cover-template.pdf: 1 page, 891.727 × 666 pt = 12.385 × 9.250 in ✔. Spine fold lines at 441.0 and 450.73 pt (6.125 and 6.260 in; spine 0.1351 in) ✔. Trim rectangle inset 9 pt (0.125 in bleed) ✔. Dashed safe areas 0.25 in inside trim on back and front ✔. Barcode box 144 × 86.4 pt = 2 × 1.2 in, at x 3.875–5.875 in, 0.25 in from the bottom trim and 0.25 in from the spine-side trim of the back cover ✔.
- cover-template.png: 3716 × 2775 px ✔; no DPI tag in the file (checked) — print apps may assume 72 ppi.
- SVG is named cover-layout.svg: viewBox 0 0 12.3851 9.25 ✔, spine lines at 6.125/6.2601 ✔, safe areas ✔; no barcode box in the SVG (checked).
- No spine safe-area margin is drawn inside the spine on any template (checked in PDF and SVG); KDP's template shows a spine safe area.
Title (60) has "Free" and no brand; /es English (L-189). Trial counter showed "0 remaining today" on a fresh load (B-0156).

## Who uses this
Self-publishers making paperback covers in Canva, Affinity or Photoshop.

## Outcomes (ranked)
1. Draw the spine safe area (KDP spine margin) on the PDF, PNG and SVG.
2. Write 300 ppi into the PNG (pHYs) and add the barcode box to the SVG when the option is on.
3. Snippet as below; /es localised.

## SEO
- Now: title "Free Book Spine and Cover Size Calculator: KDP, Ingram, Lulu" (60); meta 157 (contains "Free"); H1 "Book Spine and Cover Size Calculator".
- Keywords: KDP spine calculator, book spine width calculator, KDP cover size, cover template.
- Suggested Title: "Book Spine & Cover Size Calculator: KDP, Ingram, Lulu" (53)
- Suggested Meta: "Work out spine width and full wrap-cover size with bleed for KDP, IngramSpark and Lulu, then download a true-size PDF or PNG cover template with fold lines." (156)
- Suggested H1: keep
- FAQ: How is spine width calculated? · What bleed does KDP need? · Can I put text on a thin spine? · Cream vs white paper?

## Constraints
Do not change the formula, paper constants or the existing under-79-page warning (all verified).

## Test cases
1. KDP 6×9, 300 pages, white → 0.676 in, 12.926 × 9.250 in, 3878 × 2775 px (regression).
2. 60 pages → 0.135 in, 12.385 × 9.250 in, 3716 × 2775 px, warning text shown (regression).
3. Cream 300 pages → 0.750 in spine, 13.000 in width.
4. PDF/PNG/SVG all show a spine safe area; PNG reports 300 ppi.
5. Title ≤60, meta 140–160; 390 px no overflow.
