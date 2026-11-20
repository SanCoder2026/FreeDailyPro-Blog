Sent: 2026-11-20 08:40 ET

# FDP-22 Universal File Converter: test cases (guest, fresh context)

| ID | Input (`evidence/testfiles/`) | Action | Expected after fix |
|---|---|---|---|
| UF-01 | small.jpg | each image target | Converted ~1 s; no upload |
| UF-02 | logo.png | targets | PNG not offered for a PNG (P3) |
| UF-03 | photo.heic | JPG, PDF | Converted; no upload |
| UF-04 | contract.pdf | JPG, Word, Text, HTML, Excel | Excel: "No tables were found" |
| UF-05 | table.pdf | Excel, Word | Columns kept separate |
| UF-06 | notes.txt | PDF, Word, HTML | Emoji/CJK render |
| UF-07 | sales.xlsx | PDF, CSV, JSON, Word (table) | JSON dates ISO; consistent keys |
| UF-08 | sales.xls | PDF | Converted |
| UF-09 | data.csv | Excel, JSON | 02134/00501 kept; `=1+1` kept as text |
| UF-10 | deck.pptx | PDF, JPG, .odp | No upload, or disclosed before click; no ".pptx from old formats" target |
| UF-11 | deck.ppt | PDF, .pptx | Same as UF-10 |
| UF-12 | deck.odp | drop | Accepted (page lists .odp) or list fixed |
| UF-13 | letter.docx | PDF, Text, HTML | HTML keeps bold/table |
| UF-14 | letter.doc | drop | Clear ".doc not supported — save as .docx" at detection |
| UF-15 | page.html | PDF, Markdown, Text | No script source in output; script never runs; no remote fetch |
| UF-16 | notes.md | HTML, PDF | Converted |
| UF-17 | notpdf.pdf | drop | "looks damaged" + Repair PDF |
| UF-18 | broken.pptx | PDF | Specific error |
| UF-19/20 | vector.svg / anim.gif | drop | "can't be used here" |
| UF-21 | ocr.png | Text (OCR) | "INVOICE 2026-117 / Total due: 1,234.50 USD" |
| UF-22 | small.jpg at 0 | Convert PDF → Download | Cap dialog → Day Pass → email prompt (stop) |
| UF-23 | small.jpg with uses | Download ×2 | 0 → 1, then free; badge present |
| UF-24 | 21 × .txt, Multiple files | drop | 20 kept; grammatical toast |
