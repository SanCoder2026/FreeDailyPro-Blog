Sent: 2026-10-30 15:06 ET

# B-0285 Book Interior Maker: EPUB from the same manuscript, preflight, and a title that fits
Priority: P2 · Estimated effort: M · Report: QA-REPORT-153 · Source: live probe 2026-10-30 ~15:05 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Take an author from manuscript to an upload-ready KDP/IngramSpark interior in one place, with confidence it will pass the platform's checks.

## Why
Live check: pasted Markdown chapter added; Build interior showed the margin note "At 150 pages the platform minimum for the inside margin is 0.375 in; your setting of 0.75 in is used if it is higher" (matches KDP's 24–150-page gutter rule). Premium, 2 trial uses/day. Title is 65 chars (over 60); meta 134; /es title English (L-189).
Live competitors: Book Formatter (bookformatter.app) and DraftToDone export both a print PDF and an EPUB 3 from the same file; Book Formatter shows a Check panel listing anything KDP would reject; Univers Studio and Book Formatter add drop caps and scene-break ornaments; Typeset Studio adds a preflight report.

## Who uses this
Self-publishing authors preparing paperbacks for KDP, IngramSpark, Lulu or B&N Press.

## Outcomes (ranked)
1. Preflight panel before download: trim, gutter vs page count, margins, embedded fonts, even page count.
2. EPUB 3 export from the same chapters.
3. Drop caps and scene-break styling options.
4. Snippet as below; /es localised.

## SEO
- Now: title "Book Interior Maker: Manuscript to Print-Style PDF | FreeDailyPro" (65); meta 134; H1 "Book Interior Maker".
- Keywords: book interior formatter, KDP interior PDF, format book for print, manuscript to PDF.
- Suggested Title: "Book Interior Maker – Manuscript to Print PDF | FreeDailyPro" (60)
- Suggested Meta: "Turn manuscript chapters into a print-ready interior PDF: trim size, mirrored margins, page numbers, running heads and a page-flip preview, all in your browser." (160)
- Suggested H1: "Book Interior Maker – Manuscript to Print-Ready PDF"
- FAQ: Will KDP accept the PDF? · Which trim sizes? · Are fonts embedded? · Can I get an EPUB too?

## Constraints
Premium gating unchanged. Keep "not legal advice" note on the copyright template.

## Test cases
1. 6×9, KDP, 200-page manuscript → inside margin ≥0.5 in (151–300 rule) and the note says so.
2. PDF page size 6×9 in, fonts embedded (pdffonts), even page count, chapters start on recto.
3. Preflight flags a 0.3 in outside margin as below KDP minimum.
4. EPUB passes EPUBCheck.
5. Title ≤60, meta 140–160; 390 px no overflow.
