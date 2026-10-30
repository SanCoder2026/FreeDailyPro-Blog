Sent: 2026-10-30 13:58 ET

# B-0238 PDF to Excel: strong tool; add per-table selection/editing and fix the boilerplate meta
Priority: P3 · Estimated effort: S · Report: #137 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:56–13:58 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone with a statement or report PDF should get the tables as real numbers they can sum, and be able to fix a wrong cell before downloading.
## Why (repro: tbl.pdf = the 2-page Sales/Notes PDF from excel-to-pdf; 1280 px)
- Options: One sheet per table / per page / everything on one sheet; join a table across pages; numbers and dates as real values; date order (auto / day first / month first); OCR for scanned pages with 8 languages.
- Extract Tables → "1 table found · 31 rows in 1 sheet", "90 numbers written as real values", preview "Table 1 (p1) — 31 rows × 4 columns" with Item/Qty/Price/Total and correct values. 90 = 30 rows × 3 number columns: exact. Download gated (owner decision).
- **Missing vs competitors (~13:57 ET):** draw/adjust a box around a table and edit cells before export (SimpleTool); CSV per table (PDF.ai, SimpleTool); preview shows only the first 8 rows.
- Ad text "Try Office Apps", "Compare Browsers", "Automate Work" → L-004. 9 unnamed controls → B-0155.
## Who uses this
Bookkeepers and analysts with bank statements, price lists and reports.
## Outcomes (ranked)
1. Let people untick a found table and edit a cell in the preview before download.
2. "Download as CSV" per table.
3. A "Show all rows" toggle in the preview.
## SEO
- **Now:** Passes: 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide (og-default.png, template H2s, image without alt) → **B-0209**. **/es serves English** → **B-0123**. No overflow at 390 px.
  - Title "Extract PDF Tables to Excel Online - Free Converter" (51; "Free", no brand).
  - **Meta 84 chars, boilerplate "Free and fast, right in your browser." ending.**
  - H1 "PDF to Excel".
- **Best result:** H2s "Numbers you can sum", "Tables across pages", "Scanned PDFs (OCR)".
- **Keywords:** "pdf to excel", "pdf table to excel", "convert pdf to xlsx", "bank statement pdf to excel".
- **Suggested:**
  - Title: `PDF to Excel – Tables as Real Numbers | FreeDailyPro` (52)
  - Meta: `Pull the tables out of a PDF into an Excel workbook with numbers and dates as real values, tables joined across pages, and OCR for scans. Nothing uploaded.` (155)
  - H1: `Convert PDF Tables to Excel`
  - FAQ:
    - "Will numbers be text?" → "No, they're written as real values you can sum."
    - "Does it work on scanned PDFs?" → "Yes, tick OCR."
    - "Is my PDF uploaded?" → "No."
## Constraints
Keep the real-values and join-across-pages defaults.
## Test cases
1. tbl.pdf → 31 rows × 4 columns, 90 numbers (regression).
2. Meta 140–160, no boilerplate ending.
