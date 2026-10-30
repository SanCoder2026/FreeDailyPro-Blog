Sent: 2026-10-30 13:52 ET

# B-0231 Excel to PDF: add fit-to-width / one-page options, sheet picking, and fix the meta
Priority: P2 · Estimated effort: M · Report: #135 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:47–13:51 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone with a spreadsheet and no Excel should get a PDF where every column is on the page and text is readable, choosing how it fits.
## Why (repro: t.xlsx, sheets "Sales" with 30 formula rows + "Notes"; 1280 px)
- Upload shows "5.9 KB · 2 sheets" and an honest note: "30 formula cells had no saved result, so their value was calculated here. Check them against Excel." Good.
- Options: Page size A4/US Letter, Orientation Automatic/Portrait/Landscape, Text size Small/Normal/Large, Grid lines.
- Convert → "2 sheets · 2 pages · 5.5 KB · t.pdf", Preview first page, disclosed badge (L-041 pattern, by design), download gated at 0 trial uses (owner decision).
- **Missing vs competitors:** no scaling choice ("Fit all columns on one page" / "Fit sheet on one page" / actual size: xlsx.com, novaalab, AlphaPDF, pdfsimpli); no sheet ticking (xlsx.com, novaalab); print area / repeat rows / sheet headers-footers not mentioned (xlsx.com honours them); no Legal/A3 (xlsx.com, pdfedit).
- Ad text "Store Big Data", "Try Spreadsheets", "Try Office Apps" glued to copy → L-004. 9 unnamed controls → B-0155.
## Who uses this
Office staff sending a report to an auditor or client from a laptop or phone without Excel.
## Outcomes (ranked)
1. A Scaling option: Fit all columns on one page (default for wide sheets), Fit sheet on one page, Actual size, with a note that one-page fit can make long sheets unreadable.
2. Tick which sheets to include (hidden sheets listed, unticked).
3. Honour the sheet's print area and "rows to repeat at top"; add Legal and A3.
4. Show page count per sheet in the result line.
## SEO
- **Now:** 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide items (og-default.png, template H2s, 1 image with no alt) → **B-0209**. **/es serves English** → **B-0123**. Unnamed controls → B-0155. No overflow at 390 px (→ B-0194 not needed).
  - Title "Convert Excel to PDF Online - Free, No Cut-Off Text" (51; "Free", no brand).
  - **Meta 95 chars.**
  - H1 "Excel to PDF".
- **Best result:** H2s for "Fit columns on one page", "Multiple sheets", "Formulas and number formats"; FAQ on cut-off columns.
- **Keywords:** "excel to pdf", "xlsx to pdf", "excel to pdf fit to page", "convert spreadsheet to pdf".
- **Suggested:**
  - Title: `Excel to PDF – Every Column on the Page | FreeDailyPro` (54)
  - Meta: `Turn an XLSX, XLS or CSV file into a clean PDF table with every column on the page. Headings repeat on each page, and the file is never uploaded anywhere.` (154)
  - H1: `Convert Excel to PDF Without Cut-Off Columns`
  - FAQ:
    - "How do I stop columns being cut off?" → "Pick Fit all columns on one page, or Landscape."
    - "Are formulas kept?" → "The PDF shows each formula's value as Excel displays it."
    - "Can I convert only one sheet?" → "Yes, tick the sheets you want."
    - "Is my file uploaded?" → "No."
## Constraints
Keep the formula-recalculation note and the badge disclosure.
## Test cases
1. A 14-column sheet with Fit all columns → all columns on page 1, rows continue.
2. Untick "Notes" → 1 page PDF.
3. Meta 140–160 chars.
