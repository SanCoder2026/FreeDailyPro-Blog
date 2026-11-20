Sent: 2026-11-20 08:40 ET

# FDP-23 PDF to Word: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | Numbered-list numbers ("1.", "2.", "3.") dropped: no text, no Word numbering; page says they're kept as typed text | `testfiles/outputs/out-P01.docx`, `pdfLayout` L73–94, L553–562 | Keep the number as text or emit decimal numbering |
| 2 | P1 | Video: "Free Step-by-Step Walkthrough", "Try PDF to Word free", "10 free uses daily", "0 free uses remaining today" banner, old UI, never opens the .docx | `screens/video/quad.png`, `video/v.info.json` | Re-record today's Pro flow with trial-use wording |
| 3 | P1 (verify) | WebKit page crash during OCR of a 2-page 150-dpi scan (3/3); Chromium/Firefox fine | `json/webkit-ocr.json`, `json/browsers.json` | Reproduce on Safari; lower OCR memory (downscale page images, one worker) |
| 4 | P2 | Text-column table: "9.99 02134" in one cell, ZIP column empty; page says "numbers stay in their own columns" | `out-P14.docx` | Split on column x-positions |
| 5 | P2 | FAQ "English and Hindi are automatically recognized, no need to specify" contradicts the language picker and the other FAQ; wrong language gives garbage (P18) | `html/tool-expanded.txt` L102–113, `out-P18.docx` | One true answer |
| 6 | P2 | Headings exported as bold 14 pt runs, not Heading 1/2 (no navigation pane / TOC) | `out-P01.docx` | Map large bold lines to Heading styles |
| 7 | P2 | axe: label-content-name-mismatch (`.right-2`), preview contrast (`.bg-gray-100`), scrollable preview not focusable (`.max-h-[28rem]`) | `json/gate-kbd.json`, matrix a11y | Fix names; tabindex=0 on preview |
| 8 | P3 | OCR on scans: "Süd" → "Siid", 東京 → "35", table not rebuilt from a scan | `out-P04.docx` | Note in Limitations |
| 9 | P3 | Owner-restricted PDF: toast "Unlocked" only | P09 | Say restrictions don't carry to Word |
| 10 | P3 | OCR worker and language data from cdn.jsdelivr.net; Privacy says the engine "runs locally" | battery P04 requests | Name the host or self-host |
| 11 | P3 | tools.csv lists share/copy; result offers Download, Drive, cloud only | gate resultButtons | Update catalogue |
| 12 | P3 | /blog/pdf-to-word 404; locale titles English; /ar 404; ja desktop 3 px, iPhone SE 9 px overflow | matrix, curl | Localise; site-wide fixes |
