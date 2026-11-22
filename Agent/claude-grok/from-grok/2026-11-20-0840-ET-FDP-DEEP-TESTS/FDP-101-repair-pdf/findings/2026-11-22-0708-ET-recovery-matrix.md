Sent: 2026-11-22 07:08 ET

Sent: 2026-11-22 07:08 ET

# FDP-101 recovery matrix: input vs FDP vs qpdf vs mutool, in pdf.js / PDFium / MuPDF

E03 rows were opened without a password here; with PW=test101 the input, qpdf and mutool outputs all open 5/5 (analysis/E03-with-password.txt). ZZ-PRIVNAME-Quokka7 is a renamed copy of X01 used only for the privacy run.

Legend: js=pdf.js, pdfium=PDFium (Chrome engine), mu=MuPDF; Np/Mt = pages / pages with their PAGE-n text marker; U = shows the rev2 incremental update; img/ol/frm = images, outline entries, form value kept; qpdfN = qpdf --check exit (0 clean, 3 warnings, 2 error). ✗ = does not open.

| input | input | FDP | qpdf | mutool |
|---|---|---|---|---|
| C00-control-valid.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| E01-rc4-emptyuser-bad-startxref.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| E02-aes256-emptyuser-no-trailer.pdf | js ✗ · pdfium ✗ · mu 5p/0t img1 ol5 frm✗ · qpdf2 | js 5p/0t · pdfium 5p/0t · mu 5p/0t img1 ol5 frm✗ · qpdf2 | js 5p/0t · pdfium 5p/0t · mu 5p/0t img1 ol5 frm✗ · qpdf2 | js 5p/0t · pdfium 5p/0t · mu 5p/0t img1 ol5 frm✗ · qpdf2 |
| E03-aes256-userpw-bad-startxref.pdf | js ✗ · pdfium ✗ · mu ✗ · qpdf2 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js ✗ · pdfium ✗ · mu ✗ · qpdf2 | js ✗ · pdfium ✗ · mu ✗ · qpdf2 |
| I00-incremental-valid.pdf | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 |
| I01-incremental-bad-offsets.pdf | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf3 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 |
| I02-incremental-interrupted.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| I03-incremental-bad-prev.pdf | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf3 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4tU img1 ol5 frm✓ · qpdf0 |
| J01-junk-512-before-header.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| J02-junk-2048-before-header.pdf | js 5p/5t · pdfium ✗ · mu 5p/5t img1 ol5 frm✓ · qpdf3 | no output | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| N01-docx-renamed.pdf | js ✗ · pdfium ✗ · mu ✗ · qpdf2 | no output | no output | no output |
| N02-jpeg-renamed.pdf | js ✗ · pdfium ✗ · mu 1p/0t img0 ol0 frm✗ · qpdf2 | no output | no output | no output |
| N03-html-error-page.pdf | js ✗ · pdfium ✗ · mu 1p/0t img0 ol1 frm✗ · qpdf2 | no output | no output | no output |
| N04-plain-text.pdf | js ✗ · pdfium ✗ · mu ✗ · qpdf2 | no output | no output | no output |
| O01-broken-object-stream.pdf | js ✗ · pdfium ✗ · mu 0p/0t img0 ol0 frm✗ · qpdf2 | js 2p/2t · pdfium 2p/2t · mu 2p/2t img1 ol0 frm✗ · qpdf0 | no output | js ✗ · pdfium ✗ · mu 0p/0t img0 ol0 frm✗ · qpdf2 |
| P01-pagetree-missing-kid.pdf | js 3p/2t · pdfium ✗ · mu 5p/4t img1 ol5 frm✗ · qpdf0 | js 3p/2t · pdfium ✗ · mu 5p/4t img1 ol5 frm✗ · qpdf0 | js 4p/4t · pdfium 4p/4t · mu 4p/4t img1 ol5 frm✗ · qpdf0 | js 3p/2t · pdfium ✗ · mu 5p/4t img1 ol5 frm✗ · qpdf0 |
| P02-catalog-pages-missing.pdf | js ✗ · pdfium ✗ · mu 0p/0t img0 ol5 frm✗ · qpdf2 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol0 frm✓ · qpdf0 | no output | js ✗ · pdfium ✗ · mu 0p/0t img0 ol5 frm✗ · qpdf2 |
| T01-truncated-after-p3.pdf | js ✗ · pdfium ✗ · mu 5p/3t img1 ol5 frm✓ · qpdf3 | js 5p/3t · pdfium 5p/3t · mu 5p/3t img1 ol5 frm✓ · qpdf3 | js 5p/2t · pdfium 5p/2t · mu 5p/2t img1 ol5 frm✓ · qpdf3 | js 5p/3t · pdfium 5p/3t · mu 5p/3t img1 ol5 frm✓ · qpdf0 |
| T02-linearized-cut-60pct.pdf | js ✗ · pdfium ✗ · mu 0p/0t img0 ol0 frm✗ · qpdf2 | js 1p/1t · pdfium 1p/1t · mu 1p/1t img0 ol0 frm✗ · qpdf0 | no output | js ✗ · pdfium ✗ · mu 0p/0t img0 ol0 frm✗ · qpdf2 |
| T03-truncated-at-40pct.pdf | js ✗ · pdfium ✗ · mu ✗ · qpdf2 | no output | no output | no output |
| T04-interleaved-cut-70pct.pdf | js ✗ · pdfium ✗ · mu 5p/3t img1 ol3 frm✓ · qpdf3 | no output | js 5p/2t · pdfium 5p/2t · mu 5p/2t img1 ol2 frm✓ · qpdf3 | js 5p/3t · pdfium 5p/3t · mu 5p/3t img1 ol3 frm✓ · qpdf3 |
| X01-bad-startxref.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| X02-bad-xref-offsets.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| X03-missing-trailer.pdf | js ✗ · pdfium ✗ · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| X04-no-xref-trailer-eof.pdf | js ✗ · pdfium ✗ · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 |
| Z01-zero-byte.pdf | empty | no output | no output | no output |
| ZZ-PRIVNAME-Quokka7.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf3 | no output | no output | no output |
| base.pdf | js 5p/5t · pdfium 5p/5t · mu 5p/5t img1 ol5 frm✓ · qpdf0 | no output | no output | no output |

## Reading it

- **FDP better than both baselines:** O01 (2 pages vs none), P02 (5/5 vs none), T02 (1 page vs none), E03 (password dialog then clean, unencrypted 5/5).
- **Equal:** C00, E01, X01, X02, X03, X04, J01, I00, I01, I03. T01 pages are equal too: mutool also keeps blank p4–p5, but FDP reports "Recovered 5 pages".
- **FDP worse:**
  - T04: no output vs 5 pages, 2–3 readable;
  - J02: refused vs 5/5;
  - I02: unsaved rev2 vs last saved rev1;
  - P01: output still broken in PDFium/pdf.js; qpdf gives a clean 4-page file.
- **Extras:**
  - the lenient path keeps the outline (ol5), form value, image and link;
  - the scan path (O01, P02, T02) drops the outline and Title. That is documented on the page.
  - Title/Author are lost whenever the trailer is gone (X03, X04, T01, P02; analysis/meta.txt).
- Renders (PDFium): analysis/render-T01-fdp, render-P01-fdp, render-P01-qpdf, render-T04-mutool, render-E02-fdp, render-I02-fdp.
