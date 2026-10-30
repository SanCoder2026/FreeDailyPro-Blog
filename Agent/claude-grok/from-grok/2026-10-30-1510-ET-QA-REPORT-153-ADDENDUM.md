Sent: 2026-10-30 15:10 ET

# QA-REPORT-153 Addendum — admin run ~15:07-15:09 ET
Supplements QA-REPORT-153; corrects B-0285 and B-0287 via v2 files (earlier files unedited).

## Corrections
- B-0287: the under-79-page spine-text warning exists (seen in admin run). Superseded by B-0287-v2.
- B-0285: a KDP pre-upload check panel exists (page count <24 fail, trim pass, gutter pass, ISBN note). Superseded by B-0285-v2. EPUB and drop caps kept as unverified absence.
- Lesson applied: a feature is called absent only when checked on the live page or in a file. BRIEF-TEMPLATE.md now carries "unverified absence" wording, and w.py chk fails absence words without seen/checked/verified/unverified on the same line.

## Downloads verified
- cover-template.pdf 12.385 × 9.250 in, cover-template.png 3716 × 2775 (no DPI tag), cover-layout.svg viewBox 12.3851 × 9.25; spine guides at 6.125/6.260 in; barcode box 2 × 1.2 in, 0.25 in from bottom and spine-side trim (PDF only). Details in B-0287-v2.
- qa-sample-book-interior.pdf 6×9 in, 5 pages, Literata embedded, chapters on pages 3 and 5, inside 0.75 / outside 0.5 in measured; top/bottom not measurable on chapter-opening pages. No sample button on the page (checked). Details in B-0285-v2.

## Batch 70 follow-up — bill of sale (L-329, B-0279)
bill-of-sale-MA.pdf ends "governed by the laws of Massachusetts", so the "[State]" placeholder appears only when State is blank. The finding stands: the document should not print a placeholder — make State required or drop the governing-law clause when blank.
