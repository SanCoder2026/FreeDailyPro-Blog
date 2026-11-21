Sent: 2026-11-21 06:22 ET

# FDP-46: live functional findings (2026-11-21 EST)

## Gate at 0 (zero.json)
- Download one PDF and Download ZIP → cap dialog ("You've used today's trial uses… Monthly $4.99 / Day Pass $1… removes the 'Created with FreeDailyPro.com' mark"). Z02/Z03-dialog.png.
- Day Pass → email prompt (stopped, dlg-daypass.png). Quick Buy monthly → Stripe Checkout title (stopped, quickbuy-*.png).
- The text preview works at 0; it isn't a PDF, so it isn't a gate gap. Keyboard reaches #mm-csv and #mm-template.
- No Save to Drive or cloud-save buttons (verified live); only Open from Google Drive (sign-in, untested).

## With uses left (left.json, one page load, 06:10–06:13 EST)
- **P1:** L01 0→1; L01z, L03b, L04, L07, L08, L09, L13, L14 all downloaded with the counter at 1. Reload + download → 2.
- L01: 2 pages, Letter, Helvetica, badge bottom right on each page. L01z: record-1.pdf, record-2.pdf (name field left at its placeholder).
- L03b: first sheet hidden → toast 'Read the sheet "Visible". Only the first sheet is used.' and "1 document ready."
- L04: BOM + semicolons parsed correctly.
- L05: pasting over a filled table box with an empty template → no starter template, so nothing to download (code: only when the box was empty). P3.
- L06: 501 rows → both downloads disabled, "Up to 500 rows at a time. Split the table."
- L07 (Certificate, landscape): 5 pages, 16 images (CJK, Arabic, emoji drawn as pictures); Devanagari drawn as FreeSans text, unshaped ("प्रयिा शर्‍मा"). P2.
- L08 ZIP: ".. .. evil.pdf", "a b c d.pdf", "Ann.pdf", "ann-2.pdf", "record-5.pdf", "CON.pdf", 60 × "x", "spaced name.pdf". Each PDF carries the badge.
- L09: 4 pages for 3 records (long paragraph continues; 400-character unbroken word wraps). The overflow report wasn't captured (unverified).
- L10: type size 5/73 → "Type size has to be between 6 and 72." and downloads disabled.
- L11 corrupt xlsx → "Couldn't read that file. Use a CSV, a tab-separated text file or an Excel sheet." (N-M11-corrupt.png).
- L12 .docx → '"M12_word.docx" can't be used here. Check the file type this tool accepts.'
- L13 braces header → "Dear {{{{Name}}}}" and "Not in your table: {{Name}}. Columns are {{Name}}, Plain." P3.
- L14 500 rows → ZIP with 500 unique PDFs, 850,556 B, about 2.5 s.
- **Privacy:** 1,013 requests; none carried table values (net.hits empty).

## Preview stepping at 0 (next-at0.json)
- L02b and L03 downloads failed on my test selector ("Next" matched two buttons); the preview checks were redone at 0.
- M02: {{ course }} matched; {{Frist}} stays visible with "Not in your table" note; record 6 "Dear  Blank-First" with "Empty value in rows: 6".
- M03: "5 records"; record 2 "Dear José" (the hidden row). P2.
- ZIP de-duplication and blank-name handling are covered by L08.

## Firefox / WebKit (subset-*.json, at 0)
- Same counts, previews and notes as Chromium for the example, M02, M03, M07 and M06.
