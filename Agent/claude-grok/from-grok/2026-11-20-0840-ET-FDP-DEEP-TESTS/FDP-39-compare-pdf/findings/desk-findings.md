Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: desk findings (2026-11-21 EST)

- **Page:**
  - Title "Compare Two PDF Files Online - See What Changed | FreeDailyPro".
  - Meta description 104 chars: "See exactly what text changed between two versions of a PDF, redline-style. Fast, right in your browser."
  - Canonical self; in sitemap.
  - JSON-LD: SoftwareApplication, VideoObject, FAQPage (13 Q&As).
- **VideoObject name mismatch (P3):** JSON-LD says "How to Compare Two PDF Files Online | FreeDailyPro.com"; the YouTube title is "How to Use Compare PDF – Free Step-by-Step Walkthrough".
- **FAQ drift (P3):**
  - "Can I download a report…? Download Report saves a plain text file". Live there are two buttons, Report (PDF) and Report (.txt), and a later FAQ says so.
  - "more than a few thousand lines of text" vs Limitations "3000 paragraphs".
- **Copy vs behaviour:** paragraphs, words, headers/footers, page numbers, hyphenation, reflow, scanned detection and empty-page listing all match live.
- **Code** (`ComparePdf-DabDAhev.pretty.js`):
  - Report (PDF) uses the shared gated `D` button.
  - Report (.txt) calls `K` = ToolPage `vt`, gated by `Sa` (shared per-page-load set).
  - Compare itself has no usage call.
  - Word-level diff comes from `textDiff-DxE9AzvO`.
  - The protected-file notice comes from `protectedPdfNotice` (Unlock PDF link).
- **Blogs:**
  - `/blog/compare-pdf` (Oct 17, 2026), "Prove Only One Clause Changed Between Two Contract PDFs". Accurate on views, counters, navigation, word marks, the "same text" message, scanned/OCR, empty-page warnings and 3,000 paragraphs. Two errors:
    - "Trying a password-protected … file. The tool reports that it could not compare the PDFs. Remove the password in your PDF reader first." Live, there is an unlock dialog in the page.
    - "Trial uses apply per day, so a quick dry run on a short pair of files does not need to be wasted on a 90-page agreement" implies Compare costs a use; it doesn't.
  - `/blog/compare-pdf-document-differences` is 200 (not reviewed in depth).
- **Next step:** Redact PDF (workflow "Auditing a legal or financial PDF"). Cross-links Diff Checker.
- **Duplicate group C24:** audio-comparer, text-similarity-checker, diff-checker. Different inputs (audio, plain text), and the PDF-specific paragraph/header logic justifies a separate tool. Shares the diff engine with Diff Checker.
- **Locales:** es…id 200 with translated H1 ("Comparar PDF", "PDF Vergleichen", "PDF比較"…). Title and meta stay English. /ar 404.
- **GSC data is not available.**
