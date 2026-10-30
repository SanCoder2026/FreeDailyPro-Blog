Sent: 2026-10-30 15:06 ET

# B-0286 Book Page Count Estimator: check calibration and link to spine and print cost
Priority: P3 · Estimated effort: S · Report: QA-REPORT-153 · Source: live probe 2026-10-30 ~15:05 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Give an author a page count they can plan cost and cover around, close to what the typeset book will be.

## Why
Live check: 80,000 words, 6×9 in, defaults → 256 pages (range 228–282), "about 374 words per page", text area 4.50×7.50 in, 37 lines. Live benchmarks for the same case: InfyCalculator ~300 words/page → 296 pages incl. chapters and matter; BookFoundry 267; Cambric midpoint 288 (range 252–344); BookPrint Tools 249. FreeDailyPro sits at the low end and its words/page is ~25% above the common 300 benchmark — worth checking the default typeface/size assumptions. Not confirmed as a bug.
Title (55) has "Free" and no brand; /es English (L-189). Trial counter showed "0 remaining today" on a fresh load (B-0156).
Competitors add spine width and KDP print cost/royalty next to the page count (InfyCalculator, BookFoundry).

## Who uses this
Authors and small publishers planning trim size, cost and cover before typesetting.

## Outcomes (ranked)
1. Review default words-per-page model against a typeset sample; state the defaults (font, size, leading) next to the result.
2. Show spine width for the estimate and a link to the Spine & Cover calculator with the page count filled in.
3. Optional KDP print cost estimate.
4. Snippet as below.

## SEO
- Now: title "Free Book Page Count Estimator: Words to Pages and Back" (55); meta 157 (contains "Free"); H1 "Book Page Count Estimator".
- Keywords: book page count calculator, words to pages, how many pages is 80000 words.
- Suggested Title: "Book Page Count Estimator – Words to Pages | FreeDailyPro" (57)
- Suggested Meta: "Estimate printed pages from word count, trim size, font and margins, or work back from a page target to words. Shows a likely range and the maths behind it." (156)
- Suggested H1: keep
- FAQ: How many pages is 80,000 words? · Why a range? · Does font matter? · Why an even number?

## Constraints
Keep the "maths" disclosure and range.

## Test cases
1. 80,000 words, 6×9, 11 pt Garamond, 1.2 spacing → result within 250–300 pages; defaults shown.
2. Pages to words: 300 pages 6×9 → words shown and consistent with test 1 inverse.
3. Odd result always rounded up to even.
4. Spine link opens the calculator with page count filled.
5. Title ≤60, meta 140–160; 390 px no overflow.
