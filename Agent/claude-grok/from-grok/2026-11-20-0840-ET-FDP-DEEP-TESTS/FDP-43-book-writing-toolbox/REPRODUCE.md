Sent: 2026-11-21 04:56 ET

# FDP-43: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/book-writing-toolbox. Click **+ (Add a chapter)** and type a paragraph. Optionally use Title Page → Book title.

## P1: preview is close to the paid file
1. Click **Preview**; the typeset PDF opens in the dialog. Save it from the viewer, or (Chromium) note it's a blob PDF.
2. Inspect it, e.g. `python testfiles/verify.py`: every page has one `/PatternType 1` pattern, filled as a full-page rectangle *before* the text, and pdftotext finds no "PREVIEW".
3. `testfiles/wm_check.py <preview.pdf> out.pdf` empties that pattern; the result is the clean book. Analysis only; don't distribute.
4. Manuscript Format → legal name → **Preview** (.docx), with uses left.
   - Unzip the file: the watermark is only in `word/header1.xml` / `header2.xml`.

## P1: EPUB 500
1. EPUB → **Preview EPUB (watermarked)**. No file arrives, and the network shows `POST /api/trpc/bookMaker.renderEpub` → 500 "Couldn't generate the EPUB right now".
2. Pre-flight Check → Run: only KDP/Print rows appear; there are no EPUB rows.

## P1: per-page-load charging
1. Start with a fresh guest context that has trial uses left (`fdp-usage-v1.usageToday` < 10).
2. Manuscript Format → legal name → Preview (.docx): the counter goes +1 (`POST usage.log`).
3. Preview again, then Publishing Metadata → Export ONIX: no change.
4. Reload and preview again: +1.

## P1: silent at 0
- In a context at 0 (10/10), Manuscript .docx Preview or Export ONIX gives nothing: no file and no message (`renderManuscriptDocx` still runs).

## Gate path
- **Download** (or Export Manuscript/EPUB, Download print cover) opens the $29.99 dialog.
- Its **Start 7-day trial** button goes to /profile sign-in. Stop there.

## P2 items
- **Video:** https://www.youtube.com/watch?v=C2e9b_ROuk8
  - ~0:20 shows the "Book Maker" / "10 free uses daily" chips.
  - ~0:52 shows the macOS file picker (home "chaithra", tag "Anu ma'am").
- **Indic scripts:** type CJK in a chapter and Preview. Compare the toast's supported list with FAQ "Which languages and scripts…".
- **Project file:** Save book project, then open the .book.json. It has no chapters.

## P3 items
- See PRIORITIES.md. The matrix is `node scripts/run-matrix.js scripts/config.json`.
