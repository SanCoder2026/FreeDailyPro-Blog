Sent: 2026-10-30 13:52 ET

# QA Report #133 addendum: admin session ~13:46–13:48 ET
Files: batch-52/downloads/ (admin downloads). Checked on the box with pypdf, pdftotext, pdftoppm + PIL.

## extract-pdf (L-288, B-0226): confirmed
- On a fresh reload Text mode comes prefilled with page "1" although the field says "leave empty for all pages". Only clearing it gives all 3 pages: p-text.txt, 88 B, with "--- Page 1/2/3 ---" markers. So the default is page 1, not a carry-over from Pages mode as #133 guessed.
- **B-0226 outcome 1 changes to: "In Text mode the page field should default to empty (all pages), matching its label; say 'Reading pages 1–3'."** Test case 1 stands.
- Pages mode, page 2: p-pages-2.pdf, 873 B, pypdf: 1 page (A4), text "Page 2 hello" only. No badge in the content stream; expected, since admin downloads are from a paid session (the logged-out badge disclosure stays by design).

## compare-pdf (L-287, B-0225): both reports correct
- pdf-comparison-report.pdf (1,425 B, 1 page), pdftotext: "Original: p.pdf (3 pages) / Revised: q.pdf (3 pages) / 1 change: 1 edited, 0 added, 0 removed / 1. Changed — original page 2, revised page 2 / Page 2 hello → Page 2 hello CHANGED".
- pdf-comparison-report.txt (192 B): same content with a [+CHANGED+] word marker.
- Flaky: the first upload into the Original slot sometimes doesn't take (seen by admin and in our script); worth a fix (B-0225 test case: first upload always registers).

## ocr-pdf (L-289, B-0227): works
- searchable_scan.pdf, 44,735 B (scan.pdf 44,243 B), 1 page. pdftotext: "Invoice 4821 total 199 dollars" (exact).
- The page image is byte-identical to scan.pdf's (same 1240×1754 image stream, same MD5); rendered pages differ by 0 pixels, so the text layer is invisible and the scan is unchanged.

No new briefs; B-0226 outcome 1 is amended above.
