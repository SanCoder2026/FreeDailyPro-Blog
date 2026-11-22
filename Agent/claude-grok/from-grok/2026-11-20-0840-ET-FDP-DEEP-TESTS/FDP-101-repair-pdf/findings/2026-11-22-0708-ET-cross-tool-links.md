Sent: 2026-11-22 07:08 ET

Sent: 2026-11-22 07:08 ET

# FDP-101 other tools' damaged-file messages → Repair PDF

Source: ToolPage-B4roIUf_.js (shared drop zone). A PDF counts as "damaged" when `qn(file)` holds: no `%%EOF` in the last 8 KB (`Tn`), pdf-lib can't find pages (`Pn`) and pdf.js can't open it (`In`). Then the toast reads `"<name>" can't be read — it looks damaged`, "Try the Repair PDF tool, then add the repaired file.", with the action **Repair PDF** → `window.location.assign("/tool/repair-pdf")`. A second helper, pdfLoadError-Bi-AAFkg.js, has the text "could not be opened as a PDF. It may be damaged, cut short, or not a PDF at all. Try Repair PDF, or choose a different file." (no link). It was not seen live on the pages tested.

| Page | File | Message | Repair action lands on | File carried |
|---|---|---|---|---|
| /tool/merge-pdf | T02 | toast + Repair PDF | /tool/repair-pdf (en) ✓ | no |
| /tool/compress-pdf | T02 | toast + Repair PDF | /tool/repair-pdf ✓ | no |
| /tool/split-pdf | T02 | toast + Repair PDF | /tool/repair-pdf ✓ | no |
| /tool/add-page-numbers | T02 | toast + Repair PDF | /tool/repair-pdf ✓ | no |
| /tool/pdf-to-word | T02, T03 | toast + Repair PDF (+ guide link /blog/repair-pdf) | /tool/repair-pdf ✓ | no |
| /tool/rotate-pdf | T02 | "couldn't be read as a PDF. It may not be a PDF at all, or it may be damaged. Nothing was used. Try another file." | no link | — |
| /tool/pdf-to-jpg | T02, T03 | "This file couldn't be read as a PDF: … It may be damaged. Nothing was used." | no link | — |
| /tool/pdf-to-text | T02 | no file input found by the script (page layout differs); not tested | — | — |
| /es/tool/merge-pdf | T02 | English toast | **/tool/repair-pdf (English; /es page has H1 "Reparar PDF")** | no |
| /de/tool/compress-pdf | T02 | English toast | **/tool/repair-pdf (English)** | no |
| /fr/tool/pdf-to-word | T02 | English toast; guide link localized (/fr/blog/repair-pdf) | **/tool/repair-pdf (English)** | no |
| /tool/merge-pdf | X03 (missing trailer, EOF present) | none; accepted | — | — |

Repair's own failure links (T03/T04): "Try PDF to Word →" (/tool/pdf-to-word, localized) leads to the toast above, i.e. back to Repair. "Try PDF to JPG →" leads to "couldn't be read". Both are dead ends for the files Repair can't save (P2 #6).
