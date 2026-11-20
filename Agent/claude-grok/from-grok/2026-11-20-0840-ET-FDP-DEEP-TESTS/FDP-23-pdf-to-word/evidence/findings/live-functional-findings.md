Sent: 2026-11-20 08:40 ET

# Live functional findings (headless Chromium, guest, 2026-11-19 17:58–18:10 EST)

Method: fresh context per case; drop, options, Convert to Word, poll status; the .docx captured from memory (Blob-constructor Proxy that records Word blobs only). Every non-asset request logged. Download not pressed in the battery.

| ID | Input | Result | Time | Notes |
|---|---|---|---|---|
| P01 | rich.pdf (headings, bold/italic, bullets, numbered list, ruled table, picture, 2 pages) | 2 pages · 1 table · 1 picture | 0.5 s | Fonts Calibri/Cambria, sizes, bold, italic, bullets (Word numbering), table 4×4 exact incl. 02134/00501, picture. **Lost: "1." "2." "3." of the numbered list.** Headings = bold runs, not Heading styles. |
| P02 | rich.pdf pages "2" | 1 page | 0.6 s | — |
| P03 | rich.pdf pages "5" | "Pages to convert: Page 5 is outside this PDF's 2 pages" | — | Good message |
| P04 | scan_rich_2p.pdf (image-only) | 2 pages read with OCR | 4 s | Good; "Süd"→"Siid", 東京→"35", table as text line |
| P05 | C_scan_grey_4p.pdf | 4 pages OCR | 17 s | Minor misreads ("ine", "sitamst") |
| P06 | G_nonlatin_2p.pdf | 2 pages | 0.5 s | Japanese, Cyrillic, Greek, Turkish exact; Arabic same order as the source's own text layer |
| P07 | H_rotated_p2_3p.pdf | 3 pages | 0.5 s | Section 2 landscape 842×595 |
| P08 | J_password (user123) | password dialog → wrong: "That password didn't work" → right → 2 pages | — | `json/password.json` |
| P09 | K_owner_only_restricted | 2 pages, toast "Unlocked …" | 0.5 s | — |
| P10–P12 | truncated / text renamed .pdf / empty | "can't be read — it looks damaged · Try the Repair PDF tool" | — | `json/bad-inputs.json` |
| P13 | I_form_1p.pdf | 1 page · 2 form field values | 0.5 s | "Name: Jane Example", "☒ I agree" |
| P14 | table.pdf (text-column table) | 2 pages · 1 table | 0.5 s | Price and ZIP merged ("9.99 02134"); ZIP column empty |
| P15 | contract.pdf | 2 pages | 0.5 s | Running header → Word header "Service Agreement - page {PAGE} of {NUMPAGES}" (fields) — good |
| P16 | A_a4_3p.pdf | 3 pages | 0.5 s | Token-identical |
| P17 | 500-page PDF, pages "1-3,6" | 4 pages | 0.5 s | — |
| P18 | scan_rich_2p.pdf, language Hindi (wrong) | 2 pages OCR | 13 s | Devanagari garbage; no warning (documented) |
| P19 | 500-page PDF | 500 pages | 1.1 s | 12 KB .docx |
| P20 | twocol.pdf (60 numbered sentences in 2 columns) | 2 pages | 0.5 s | All 60 in order — columns read correctly |

Token diff vs pdftotext: P01 missing only `1.` `2.` `3.` and the bullet glyphs (now Word bullets); P13/P14/P16 none; P15 header collapsed into one header with fields.

Network: no POST to freedailypro.com other than analytics (funnel.hit, insight.hit) in any case; OCR fetches tesseract worker/core/eng data from cdn.jsdelivr.net.

## Gate, dialogs
- With uses (18:02:35 EST, start 0): convert 0 → 0; Download 1 → rich.docx (`dl-1-rich.docx`) 13,702 B = memory (sha match), 0 → 1; Download 2 free; Convert another + same file + Download free (1 → 1).
- At cap (18:02:55, start 10): Download → "WE VALUE YOUR USAGE · Today's trial uses are done · … You've used today's 10 trial uses. Monthly for $4.99 … Day Pass for $1 … Either pass removes the "Created with FreeDailyPro.com" mark from your PDFs and images" → Buy Day Pass → "Day Pass, $1 · Enter your email and go straight to payment" (stopped). Result kept. Save to Google Drive at cap → same cap dialog. Save to my cloud storage → "$4.99 per month, 1 GB … Sign in" (Not now).
- Stop during OCR ("Reading page 1 of 4 with OCR…") returns to Convert to Word immediately.
- Keyboard: 28 Tabs to the drop zone; Enter opens the chooser. Options labelled ("Language of scanned pages…", "Pages to convert (the PDF has 2):"). Live regions: step tracker and the "Converted:" summary are polite.
- Phones: iPhone SE and Pixel 7 convert by tap; Download Word File at y≈746 / 671 px.

## Browsers
Firefox: rich.pdf 1.1 s, scan 3.8 s OCR — OK. WebKit: rich.pdf OK; scan_rich_2p.pdf → **page crashed** (3/3 attempts); C_scan_grey_4p.pdf OK. Playwright WebKit on Linux, not real Safari.
