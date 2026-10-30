Sent: 2026-10-30 15:10 ET

Supersedes: batch-72/report-153/2026-10-30-1506-ET-B-0285-book-interior-maker-epub-preflight-seo.md (that file wrongly said there was no pre-upload check panel; it is left unedited).

# B-0285-v2 Book Interior Maker: EPUB from the same manuscript, drop caps, and a title that fits
Priority: P2 · Estimated effort: M · Report: QA-REPORT-153 · Source: live probe 2026-10-30 ~15:05 ET, admin run ~15:07-15:09 ET (downloads in batch-72/downloads/), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Take an author from manuscript to an upload-ready KDP/IngramSpark interior in one place.

## Why
Live check: Build interior shows the margin note "At 150 pages the platform minimum for the inside margin is 0.375 in" (matches KDP's 24–150-page gutter rule). Admin run: a KDP pre-upload check panel exists (page count fails under 24, trim pass, gutter pass, ISBN note) — keep it.
Output verified (qa-sample-book-interior.pdf, 5 pages): page size 432×648 pt = 6×9 in ✔; Literata Regular and Bold embedded ✔; "Chapter 1" on page 3 and "Chapter 2" on page 5 (right-hand pages, page 4 blank) ✔; text block x 54–396 pt on rectos = inside 0.75 in, outside 0.5 in ✔. Top/bottom 0.75 in: consistent with the settings, but the sample has only chapter-opening pages (sunk start at 113 pt) so a full body page was not available to measure; folio sits 0.375 in from the bottom edge.
There is no "load sample" button (checked on live page): a first-time user must supply a manuscript before seeing any output.
Competitors (seen in live search): Book Formatter and DraftToDone export both a print PDF and an EPUB 3 from the same file; Book Formatter and Univers Studio offer drop caps and scene-break ornaments. FreeDailyPro: EPUB export and drop caps — unverified absence, not seen in this run's options list; confirm before building.
Title 65 chars (over 60); meta 134; /es title English (L-189).

## Who uses this
Self-publishing authors preparing paperbacks for KDP, IngramSpark, Lulu or B&N Press.

## Outcomes (ranked)
1. EPUB 3 export from the same chapters (if not already present).
2. Drop caps and scene-break styling options (if not already present).
3. A "Try with sample chapters" button so the preview can be seen before uploading anything.
4. Snippet as below; /es localised.

## SEO
- Now: title "Book Interior Maker: Manuscript to Print-Style PDF | FreeDailyPro" (65); meta 134; H1 "Book Interior Maker".
- Keywords: book interior formatter, KDP interior PDF, format book for print, manuscript to PDF.
- Suggested Title: "Book Interior Maker – Manuscript to Print PDF | FreeDailyPro" (60)
- Suggested Meta: "Turn manuscript chapters into a print-ready interior PDF: trim size, mirrored margins, page numbers, running heads and a page-flip preview, all in your browser." (160)
- Suggested H1: "Book Interior Maker – Manuscript to Print-Ready PDF"
- FAQ: Will KDP accept the PDF? · Which trim sizes? · Are fonts embedded? · Can I get an EPUB too?

## Constraints
Premium gating unchanged. Keep the check panel and the "not legal advice" note.

## Test cases
1. 6×9, KDP, 200-page manuscript → inside margin ≥0.5 in (151–300 rule) and the note says so.
2. PDF 6×9 in, fonts embedded, chapters on odd pages with blank versos (regression of the sample above).
3. Check panel: 20-page book → page count fail; 24+ → pass.
4. EPUB passes EPUBCheck.
5. Sample button produces a preview without any upload.
6. Title ≤60, meta 140–160; 390 px no overflow.
