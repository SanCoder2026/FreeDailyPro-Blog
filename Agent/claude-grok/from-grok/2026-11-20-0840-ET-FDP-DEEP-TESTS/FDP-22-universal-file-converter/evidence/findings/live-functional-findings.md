Sent: 2026-11-20 08:40 ET

# Live functional findings (headless Chromium, guest, 2026-11-19 17:28–17:53 EST)

Method: one fresh context per input file; for each offered target: drop, press target, wait for "Converted", capture the result from memory, Start over. Every request to freedailypro.com logged with POST size. Nothing downloaded in the battery (conversion is free; Download is the gate).

## Detection and targets (all correct)
| ID | Input | Detected | Targets shown |
|---|---|---|---|
| U01/U02 | small.jpg / logo.png | Image | PDF, PNG, JPG, WebP, ICO, Base64 text, Text (OCR) (PNG offered for a PNG) |
| U03 | photo.heic | HEIC photo | same 7 |
| U04/U05 | contract.pdf / table.pdf | PDF | JPG, Excel, Word, Text, HTML |
| U06 | notes.txt | Text file | PDF, Word, HTML |
| U07/U08 | sales.xlsx / sales.xls | Spreadsheet | PDF, CSV, JSON, Word (table) |
| U09 | data.csv | CSV | Excel, JSON, PDF |
| U10/U11 | deck.pptx / deck.ppt | PowerPoint presentation | PDF, JPG, PowerPoint .pptx (from old formats), OpenDocument .odp |
| U13/U14 | letter.docx / letter.doc | Word document | PDF, Text, HTML |
| U15 | page.html | HTML file | PDF, Markdown, Text |
| U16 | notes.md | Markdown file | HTML, PDF |
| U12 | deck.odp | — | rejected: "can't be used here" (page lists .odp as input) |
| U19/U20 | vector.svg / anim.gif | — | rejected: "can't be used here" (stated limitation) |
| U17 | notpdf.pdf (text renamed) | — | "can't be read — it looks damaged" + Repair PDF link (good) |

## Server upload (P1)
- U10 deck.pptx → OpenDocument .odp: `POST /api/trpc/presentation.convert?batch=1`, 40,246 bytes (30,134-byte file, base64). Output deck-converted.odp 25,547 B.
- U11 deck.ppt → PDF: same endpoint, 870,466 bytes; → .pptx: 870,466 bytes.
- U10 .pptx → PDF / JPG: no upload (font file only).
- All other conversions: no request except `/fonts/DejaVuSans-subset.ttf` for text PDFs. OCR fetches tesseract worker/core/eng.traineddata from cdn.jsdelivr.net.
- Code: `legacyDeck.pretty.js` L53 `presentation.convert.mutate({ fileBase64, … })`, 30 MB cap L17.

## Data fidelity
- CSV (`1,"Ana, María","says ""hi""",02134,"1,234.50"` …): Excel keeps quotes, commas, multiline, CJK, `=1+1` as text (t="str" — safe) but ZIP 02134→2134, 00501→501 (numbers). JSON: same zero loss, and `=1+1` → "" (P1).
- xlsx → CSV/JSON: first sheet only (documented); formula column without cached values → empty; JSON dates serial (46023) vs CSV ISO; row 1 lacks "Total" key.
- PDF → Word: paragraphs only; table PDF → Excel: "Table 1 (p1)" with merged columns ("9.99 02134"); contract.pdf → Excel: "No tables were found in this PDF to convert." (good).
- txt → PDF: emoji and 日本語 render (images); wraps correctly.
- docx → HTML: text kept, bold and table lost (tabs inside `<p>`).
- HTML → Markdown: good (bold, link, image kept; table as HTML). HTML → Text/PDF: `<style>` dropped but `<script>` source printed as text. Script did not execute; remote `<img>` not fetched during conversion.
- OCR (ocr.png "INVOICE 2026-117 / Total due: 1,234.50 USD"): exact text in ~2 s (`json/ocr-result.txt`). The battery's 60 s OCR timeouts (U01-6, U21) were caused by our Blob-subclass capture hook breaking the worker; re-run without it passed — not a site bug.
- HEIC → JPG 731,203 B, → PDF 732,540 B; JPG → PDF 5,144 B etc., all ~1 s.

## Dead ends (toasts captured immediately, `json/toasts.json`)
- letter.doc (real Word 97) → PDF: "That conversion didn't work on this file. Try a different file or target format." Console: "NotDocxError: This isn't a Word (.docx) file."
- deck.pptx → "PowerPoint .pptx (from old formats)": "This file is already a .pptx."
- broken.pptx → PDF: same generic toast (console: "doesn't look like a valid .pptx").

## Gate, dialogs, edit, batch
- Converted-file Download at 0: "WE VALUE YOUR USAGE · Today's trial uses are done … Monthly pass — $9.99/month … Buy Day Pass — $3" → "Premium Day Pass, $3 · Enter your email…" (stopped).
- With uses: Download 0 → 1, file small-converted.pdf (`dl-1-small-converted.pdf`) 6,141 B = 5,144 B result + badge "Created with FreeDailyPro.com" (intentional); 2nd Download free (1 → 1).
- Original-file Download at 0 downloads the original (`contract.pdf`) without a dialog — fine.
- Save to Google Drive → Google sign-in popup (closed). Save to my cloud storage → "$4.99 per month, 1 GB … Sign in" (Not now).
- Edit (PDF): Resize, Crop, Rotate 90°, Watermark, Page numbers, Compress, Password protect, Merge in another PDF, Improve quality. Compress levels: Recommended (~50% smaller), Medium (~25% smaller), Strong (~50% smaller).
- Multiple files, 21 .txt: 20 kept, toast "A batch holds up to 20 files — 1 were left out." Buttons include "Merge these into one text file".
- Live regions: a status region (counter) and an empty polite region.
- Keyboard: 31 Tabs to the drop zone; Enter opens the file chooser.

## Browsers
Firefox and WebKit: data.csv → Excel and photo.heic → JPG both converted; no page errors (WebKit: ad-frame cross-origin notices only).
