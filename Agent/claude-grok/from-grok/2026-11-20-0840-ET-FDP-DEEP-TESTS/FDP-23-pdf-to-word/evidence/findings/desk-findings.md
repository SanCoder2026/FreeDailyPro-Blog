Sent: 2026-11-20 08:40 ET

# Desk findings (page copy, JSON-LD, code)

- Title "PDF to Word Converter - Editable .docx, OCR | FreeDailyPro"; meta "…real paragraphs, lists and tables… Runs in your browser, nothing uploaded." Verified: nothing uploaded.
- About: "bullet lists become Word lists… tables are rebuilt as real Word tables (numbers stay in their own columns)". P14 shows two numbers in one cell.
- How to use (tip): "Numbered lists keep their numbers as typed text." P01: numbers removed. Code: `pdfLayout` L81–84 marks `kind: "number"` and shifts the segment off; L553–562 builds list formatting only for bullets.
- FAQ "Which languages can scanned pages be read in?": "English by default… choose… Pick the language". FAQ "What languages does the OCR support?": "English and Hindi are automatically recognized, no need to specify". Contradictory; the UI defaults to English.
- FAQ "Can I stop…": Stop exists and works.
- Privacy: "the OCR engine itself runs locally" — true, but its code and language data are fetched from cdn.jsdelivr.net.
- Strip: "Trial: 10 uses/day", "Ad-free: $1 day pass · $4.99/month" — matches the cap dialog.
- Next-step cards: Universal File Converter (Premium) and File Conversion Studio (Workflow); Related: Image to Word, Scan or Photo to Word, OCR PDF, PDF to Excel.
- /blog/pdf-to-word 404; Guides link /blog/convert-between-document-and-image-formats-in-one-app and /blog/repair-pdf. tools.csv: 9 posts link here; lists share/save/my-files/cloud/copy.
- /es 200 (H1 "PDF a Word", title English); /ar 404.
