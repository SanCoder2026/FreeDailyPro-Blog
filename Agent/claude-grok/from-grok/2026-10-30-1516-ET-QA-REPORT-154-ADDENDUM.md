Sent: 2026-10-30 15:16 ET

# QA-REPORT-154 Addendum — admin session ~15:14-15:15 ET
Supplements QA-REPORT-154 (batch 73). Earlier files unedited.

## Barcode (B-0289, L-339)
- ean13-5901234123457.png: 936 × 482 px, 300 dpi tag, fully opaque. zxing-cpp decodes EAN-13 "5901234123457" ✔ (check digit 7 added correctly). OpenCV's barcode detector returned no result on either file (detector limit; zxing is the reference here). zbar library is not installed on the box, so zbar was not run.
- ean13-5901234123457.svg: 234 × 122 px, viewBox 0 0 234 122, white background, 10 px quiet zones; human-readable digits printed as "5", "901234", "123457". A Chromium render of the SVG decodes to 5901234123457 ✔.
- PNG width 936 px at 300 dpi = 3.12 in, matching the page text "Prints 3.12 in (7.9 cm) wide at 100%" ✔.
- Wrong check digit 5901234123458: rejected by the page ✔ (admin). Minor: a stale "ready!" toast stays on screen alongside the error — add as a B-0289 test case: the error state clears any success toast.
- Bulk barcodes from a list or CSV: confirmed absent on the live page by admin. The B-0289 "unverified absence" item is now a checked absence.

## Catalog Maker (B-0288, L-338)
- Import: .xlsx confirmed not accepted (CSV/TSV/TXT only) — Outcome 1 stands as a checked gap.
- Template, style and PDF-quality controls: confirmed absent on the live page by admin.
- Controls that do exist: Currency; Columns 2 or 3 per row; Page size Letter or A4 plus book-trim sizes; accent colour; cover page, price list and contents toggles; and in Combine files, a back-page QR code or barcode.

## ASCII Art Generator (B-0290, L-340)
- Download .txt: confirmed absent on the live page by admin ✔ (B-0290 Outcome 2 stands).
- Correction note: B-0290 says "14 fonts"; the live count is 12 — Standard, Big, Slant, Small, Mini, Banner3, Block, ANSI Shadow, Doom, Graffiti, Ghost, Bubble. In context: patorjk TAAG offers 300+ FIGlet fonts and ascii-images.com previews 332, so 12 is a small curated set; Outcome 3 (more fonts with searchable preview) stands. B-0290 is left unedited.

## Still open
- L-216 "Copied" toast at 0 trial uses (not covered in this session).
- Per-tool pass prices ($1/$4.99 barcode vs $3/$9.99 catalog).
