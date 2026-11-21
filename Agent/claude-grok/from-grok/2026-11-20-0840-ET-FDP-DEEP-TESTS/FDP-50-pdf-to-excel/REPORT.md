Sent: 2026-11-21 08:14 ET

# FDP-50 PDF to Excel (pdf-to-excel): deep test report for Claude

- **Written:** 2026-11-21 08:12 EST (box `date`, ET). Testing ran 2026-11-21 07:48–08:11 EST.
- **Tool:** https://www.freedailypro.com/tool/pdf-to-excel. Row 50 of TEST-ORDER.md: **Professional Tool**, PDF Tools, plan note "test-plan (unranked): L-243 rank 1 (PDF Toolkit API live)". No duplicate group (related: C06 OCR family, image-to-excel).
  - Video: dGgPVkXxdII. Blog: /blog/pdf-to-excel.
  - **GSC data is not available.** The API side was not tested (no API/MCP testing).
- **Offer:** 10 trial uses a day, charged at Download (`gateAtDownload`). Options, Extract and the preview (up to 8 rows per sheet) are open. $1 Day Pass / $4.99 monthly.
  - Everything runs in the browser:
    - pdf.js text positions → table detection (3+ aligned rows) → joining across pages → typed cells (numbers, currency, percent, dates) → SheetJS xlsx.
    - Optional OCR (tesseract.js, with language data from jsDelivr).
    - Password PDFs unlock locally.
- **Testers:**
  - **Desk review:** copy, FAQ (13), Details, JSON-LD, blog, JS (PdfToExcel, pdfToExcel, tablesToExcel).
  - **Headless Playwright:**
    - at the cap (zero.json)
    - one long load with uses left plus a reload (left.json, 24 cases)
    - Firefox/WebKit subsets
  - **Checks:**
    - 16 test PDFs (real text layers, plus a scan)
    - every workbook opened with openpyxl (types, formats, formulas, autofilter)
    - OCR compared cell by cell
    - network scan
    - matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe
    - the video, frame by frame
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Day Pass email prompt and Stripe Checkout.
  - No ad clicks, no API/MCP calls, no site or repo changes.
  - The only password typed was the test PDF's own.
- **Sign-in (untested):**
  - Save to Google Drive: Google sign-in popup with uses left; cap dialog at 0.
  - Save to my cloud storage: "Sign in with your email first"; $4.99/month add-on.
  - Open from Google Drive: Google popup.
  - Paid-pass output.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. The "Created with FreeDailyPro.com" badge is intentional.

**Code to look at:**
- **ToolPage DownloadButton (`gateAtDownload`):** charges once per tool per page load and doesn't re-check the cap later. Same root cause as FDP-44 to FDP-49.
- **`tablesToExcel-C1ZZUvmI.js`:**
  - `J()`: `if (c) continue;`, where `c = X.test(headerText)`. A single word such as "invoice", "account", "order", "number" or "no" anywhere in the header blocks number typing for the whole column.
  - `H()`:
    - `^(\d+)\.(\d+)$` reads "1.500" as 1.5 even when the column's other values are "1.234,56".
    - No space, narrow-space or apostrophe thousands.
    - Currency only for `$€£¥₹` symbols, not ISO codes; no CR/DR.
  - `U()`: two-digit years use pivot 49.
- **`pdfToExcel-38p0cUiA.js`:** OCR text goes through the same `H()`. "(5111.25)" (an OCR'd "($111.25)") parses cleanly as a number, so nothing flags it.

**After you ship:**
- Rerun `scripts/px-live.js left`. Expect +1 per new workbook, and the cap dialog at 10/10 without a reload.
- Open T02, T03, T04, T12 and T08 with `check-xlsx.py`.
- Work through test-cases.md.

## Intent

A bookkeeper, analyst or small-business owner has a bank statement, price list or report in PDF. They want the table in Excel with numbers they can SUM and dates they can sort, without retyping and without uploading financial documents.

The core is strong:
- **Real tables:** a US 3-page statement became one 76-row table with the repeated header dropped, "$" amounts typed as currency, parenthesised negatives, and month-first dates inferred with a clear note.
- **Detection:** prose and two-column text are correctly ignored. Identifiers (ZIP, phone, card numbers, leading-zero codes) are kept as text.
- **Dates:** ambiguous dates are left as text with an honest note, and "Day first" fixes them.
- **Safety:** formula-like strings are stored safely as text.
- **Scale:** 40 pages × 40 rows → 1,601 rows in 0.5 s.
- **Messages:** clear wording for no tables, scans with OCR off, damaged and password files.
- **Privacy:** nothing is uploaded; only OCR assets come from jsDelivr, as documented.

What undercuts it:
- **Charging per page load:** 15 workbooks for one trial use.
- **Silent wrong data, the worst failure for this audience:**
  - Ordinary money columns named "Invoice Amount", "Account Balance" or "Order Total" are written as text, so SUM returns 0.
  - In German-style files, whole thousands like "1.500" become 1.5 while still *looking* like "1.500". A bookkeeper who trusts the "numbers written as real values" summary will report wrong totals.
- **Old video:** it says "free" and demos an old UI at "0 free uses remaining".

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - left.json: L01 0→1. Then L02–L18 produced 15 new workbooks plus a re-download, all at 1.
  - After a reload, L20 went 1→2. L21, a new workbook, still downloaded at 2.
  - Only 2 `usage.log` POSTs in all.
- **P1, data: header words block number typing.**
  - T02 has 7 columns. Only "Qty" was typed (summary: "4 numbers written as real values").
  - "Invoice Amount", "Account Balance", "Order Total", "Unit price (no VAT)" and "Number of units" are strings in the workbook.
  - No note explains this. The tool's own FAQ says amounts are written as real values "so SUM, sorting and filters work".
- **P1, data: European thousands become decimals.**
  - T03 Menge: "1.500" → 1.5 and "2.000" → 2, written with format `0.000` so that it *displays* "1.500".
  - SUM is 754.5 instead of 4,251. Betrag ("1.234,56 €") is correct, so the column-level evidence for "." as the thousands separator is right there.
- **P2 items:**
  - **French space thousands:** "1 234,56 €" stays text (T04: 0 numbers).
  - **Bank-style amounts:** "1,234.00 CR / 200.00 DR" and "USD 1.50" stay text (T12).
  - **OCR money errors:**
    - On a 100 dpi image of T01 page 1, 7 of 8 parenthesised amounts became "-5xxx.25" ("$" read as "5"), and 3 more digits were misread: 10 of 104 cells wrong.
    - The OCR warning is shown, but the systematic "$"→"5" case could be caught (the format fell back to `0.00` in a "$" column).
    - My scan is low resolution, so real 300 dpi scans would do better (unverified).
  - **Video (check 12 FAIL):**
    - Old UI and "0 free uses remaining today" during the demo.
    - "FREE · PRIVATE · NO LOGIN", the "200+ Free Productivity Tools" end card, and the "Try … free" / "Free daily uses" description.
    - The OneDrive account label is visible in the file picker.
  - **Preview at 0 (owner question):** up to 8 rows per sheet are shown as selectable text at 10/10. A table of 8 rows or fewer is fully readable without a trial use (Z01). The typed workbook stays gated.
  - **Locale pages:** the H1 is translated, but the title, meta, section headings, "Watch: … in Action" and the video title stay English on all 10 locales. The /de page still parses "1.500" as 1.5.
- **P3 items:**
  - **Wrapped cells:** a 4-row table with wrapped description cells isn't found at all (documented limit; a pointer would help).
  - **Two-digit years:** "21/11/50" → 1950 (pivot 49, unlike Excel's 29).
  - **Head and FAQ:** meta 75 chars; og-default; VideoObject title differs from the video; three duplicate FAQ pairs.
  - **Layout and axe:** iPhone SE 9 px overflow; /ja 3 px; axe label-content-name-mismatch (1), region (1), color-contrast on the ad label (2).
  - **Counter display:** in one WebKit context the strip said "0 remaining today" while the server still accepted a download (one `usage.log`). A recheck in 3 fresh WebKit contexts at 10/10 showed the cap dialog correctly, so this is a display mismatch, not a bypass (unverified cause).

## Outcomes we want

1. Each new workbook takes one trial use, and a re-download stays free. At the cap, the dialog shows without needing a reload.
2. Every column a person would call money is typed as a number, whatever its header, in US, European, French/Swiss and bank (CR/DR, ISO code) formats.
3. Ambiguous cases ("1.500") are flagged in a note instead of being silently guessed.
4. An OCR pass that catches "$"→"5" in money columns.
5. A new video of the current Options and preview flow with "trial uses" wording.
6. An owner decision on how much preview is shown at 0.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (with data P1s) | Tables found, joined, typed; 1,601 rows fast; OCR works. |
| 2 | Completeness vs competitors | PARTIAL | Compared with Adobe Export PDF, Smallpdf, iLovePDF, Tabula: better typing/joining notes than most, local-only; misses European/space formats, CR/DR, wrapped cells; no manual table-area selection (Tabula has it). |
| 3 | Ease of use | PASS | Clear options, honest notes, preview before download. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow, /ja 3 px. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $1 email prompt (stopped); Quick Buy monthly → Stripe (stopped). |
| 6 | Information correct | PARTIAL | "Numbers … written as real values" not true for ID-word headers and European/space formats. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 61 good; meta 75 short; og-default; VideoObject title mismatch. |
| 9 | Blog exists and accurate | PASS | Practical, accurate. |
| 10 | YouTube video exists | PASS | dGgPVkXxdII embedded. |
| 11 | FAQ and guide correct | PARTIAL | 13 answers, candid; 3 duplicate pairs; the real-values promise has the gaps above. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, "free" wording, demo at 0 uses, account label visible. |
| 13 | Storage | Sign-in untested | Save to my cloud storage needs email sign-in + $4.99 add-on. |
| 14 | Sharing | PASS / sign-in untested | Share this tool works; Save to Google Drive needs Google sign-in. |
| 15 | Downloads | PARTIAL (data P1) | Valid xlsx, autofilter, formats; wrong types/values in T02/T03. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 15 workbooks for one use. |
| 17 | Categorization in section | PASS | PDF Tools / Professional Tools. |
| 18 | Correct section of site | PASS | PDF Tools; links to Excel to PDF, PDF to Word, OCR. |
| 19 | AI need/demand | PASS | L-243 rank 1; chat assistants can't reliably return typed xlsx from a private PDF locally. |
| 20 | Merge better? | No | Distinct from image-to-excel (photos) though they could share the typing engine. |
| 21 | Remove? | No | Demand rank 1. |
| 22 | Duplicates | None | Keep; cross-link Image to Excel for photos (already listed). |
