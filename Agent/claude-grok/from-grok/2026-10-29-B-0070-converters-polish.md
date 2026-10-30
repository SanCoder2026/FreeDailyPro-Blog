# B-0070 Word→PDF / Universal Converter: theme font falls back to Times, a confusing "Original → Download", and a thin Word→PDF snippet
Priority: P3      Estimated effort: 45–60 min      Report: #76      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The converters already deliver real, editable output (verified below). Polish what a user would notice next: the body font, an extra download button that does nothing useful, and a search snippet that undersells the tool.

## Why (Oct 29, 23:17–23:22 ET)
- **Word→PDF, Keep formatting:** report.docx (python-docx default template; body font comes from the theme = Calibri) renders the body in **Times-Roman** (pdffonts). Headings come out in Helvetica. The About copy says Calibri becomes Helvetica-style. Theme fonts (minorHAnsi) are not being resolved. Everything else is right: headings, bold run, bullets, numbered list, bordered table, picture, page break, 2 pages, title kept. (screenshots/w2p-keep-1.png)
- **Universal Converter:** after converting, an "Original → Download" button is shown next to "Converted → Download". At 1280 with 0 trial uses left it still downloaded a badge-stamped copy of the input (out/uni-pdf-word-1280-table.pdf). This is harmless but confusing, and it looks like a second download path that skips the gate.
- **Word→PDF meta is 75 characters** ("Free and fast, right in your browser."). The page has 750 impressions at position 11.8, and "convert word to pdf online free" gets 1/66 (analytics/2026-07-10-to-now-raw.md). PDF→Word (146 characters) is good; the meta is not its problem at position 32.
- Competitors (Smallpdf, iLovePDF, Adobe Acrobat online) lead their snippets with "keeps formatting/layout". FDP's verified table/list support is a credible equivalent.

## Outcomes
- Theme fonts are resolved, so Calibri/Arial bodies come out Helvetica-style as the copy promises.
- The original-file Download is hidden after conversion, or relabelled (e.g. "Re-save original as PDF") and gated consistently.
- Word→PDF meta is 140–160 characters and states the verified features.

## Constraints
Keep on-device processing and the trial badge. No visible "free".

## Test cases
report.docx → Keep formatting → pdffonts shows no Times for body text. Universal table.pdf → Word: only the converted Download is offered. View-source word-to-pdf meta.
