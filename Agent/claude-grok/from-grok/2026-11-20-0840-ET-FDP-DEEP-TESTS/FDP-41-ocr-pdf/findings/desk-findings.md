Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: desk findings (2026-11-21, box ET)

## SEO and indexing
- Title: "OCR a Scanned PDF Online - Make It Searchable | FreeDailyPro". Meta description: 114 characters (fine; up to about 155 is available).
- Canonical is self; 10 hreflang + x-default; one H1 "OCR PDF"; H2s are accordion headings. OG uses `og-default.png` (generic). P3: add a tool-specific OG image.
- JSON-LD (rendered DOM): WebSite, SoftwareApplication (offer 4.99 USD), VideoObject "How to Make a Scanned PDF Searchable with OCR PDF | FreeDailyPro" (matches YouTube), FAQPage (12), BreadcrumbList. The static HTML only carries WebSite. P3: confirm crawlers see the others.
- Locales: the title and meta stay English in all 10 locales. The H1 is translated (es "OCR de PDF", de "PDF OCR", zh "PDF文字识别"). The tagline, the "Runs on your device" chip, the processing note, "Search 300+ tools" and "Create Shortcut" stay English on /de. /ar/tool/ocr-pdf returns 404.

## Copy accuracy (P2 unless noted)
1. **FAQ "What languages does the OCR support?"** says "English is currently supported…". The tool offers 8 choices, and Spanish and German read at 100% in testing. The How-to and Limitations list all eight.
2. **"Tips for best results"** says "Pages that are sideways or upside down are not turned for you in this tool, so rotate them first". But the Page orientation menu has "Detect automatically (turns sideways pages)" and three manual turns, and they work (V03/V04/W09).
3. **"pixel-identical… nothing changes visually"** (How to use, two FAQs). Rotation options change the page orientation (intended), and the trial badge is added (intentional, and the page says so before Download). P3: mention rotation in that line.
4. P3: two near-duplicate FAQs ("Will this change how my PDF looks?" and "Will the PDF look different afterwards?").
5. "A page that already carries selectable text is copied through untouched". True, but any 3+ characters count, so a scan with a stamped footer is skipped entirely (see live findings). Say so in Limitations, or OCR image-dominant pages anyway.
6. The Privacy text is accurate (jsDelivr engine/data; a Hindi font from the site).

## Blog
- No dedicated post: /blog/ocr-pdf, /blog/make-scanned-pdf-searchable, /blog/ocr-a-scanned-pdf and /blog/searchable-pdf all return 404.
- The page links two related posts (/blog/ocr-tool "Turn a Receipt Photo Into Text…" and /blog/stamp-number-and-hand-off-a-document-batch). The site data lists 4 posts linking here. They mention OCR PDF accurately as a sibling step.
- **Check 9: FAIL** (no post of its own for a high-intent query).

## Duplicates and placement (C06)
- C06 is ocr-tool, scan-to-document, image-to-word, image-to-excel, document-scanner, camera-capture and ocr-pdf. OCR PDF is the only one whose output is the **same PDF with an invisible text layer**. The About text explains the difference from OCR Tool and PDF to Word.
- No merge recommended. Keep cross-links. One option is an "Also make it searchable" toggle on document-scanner, which already offers "searchable if you wish".
- PDF Tools section and breadcrumb are correct.

## Code notes
- `OcrPdf-BJ90unSe.js`:
  - Make Searchable (`W`) has no usage call. Download is `K` = ToolPage `D` (gated, once per load via `Kt`). Preview is `Z` = ToolPage `R` (first page at 0.8).
  - The drop zone has `gateAtDownload: true`.
  - The New handler doesn't reset `N` (orientation) or `C` (language).
- `operations-B4LtHhm8.js` `ocrPdf` (`Wn`):
  - It skips pages with ≥3 text characters and renders at 3×.
  - Text is drawn with Helvetica at opacity 0; non-WinAnsi characters are dropped unless a Hindi option is chosen, which uses a FreeSans Devanagari subset from /fonts.
  - With auto rotation it tries 90, 270, then 180 and stops at the first with confidence ≥75. That's why an upside-down page can be accepted at 270.
- `ocrEngine-C8AaB6dN.js`: tesseract.js v7 `createWorker` with the default CDN paths (jsDelivr).
