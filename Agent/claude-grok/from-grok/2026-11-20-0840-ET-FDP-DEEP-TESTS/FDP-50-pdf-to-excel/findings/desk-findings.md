Sent: 2026-11-21 08:14 ET

# Desk findings

- **Head:**
  - Title "Extract PDF Tables to Excel Online - Converter | FreeDailyPro" (61).
  - Meta 75 chars: "Extract tables from PDF to Excel spreadsheets. Fast, right in your browser."
  - Canonical self; hreflang 10 + x-default; og-default.
- **JSON-LD:** WebSite, SoftwareApplication (offer 4.99), VideoObject ("How to Convert PDF Tables to Excel Online", 2026-09-24; the video title differs), FAQPage (13), BreadcrumbList.
- **FAQ:** 13 answers, accurate and candid about limits.
  - Overlap: three pairs of questions repeat each other (scanned, continued table, no tables found).
  - "Numbers … are written as real values" is contradicted for columns with ID-like header words and for space/dot-thousands formats.
- **Blog /blog/pdf-to-excel:** "Pull a Six-Page Price List Out of a PDF and Into Excel". Practical and accurate, with good verification tips.
- **Code (tablesToExcel-C1ZZUvmI.js):**
  - `H()`: number parser (currency symbols `$€£¥₹` only; `^(\d+)\.(\d+)$` is always a decimal; no space thousands).
  - `J()`: typing per column, with header regex `X` skipping numbers.
  - `U()`: dates; two-digit pivot 49.
  - `le()`: joins tables across pages.
  - `fe()`: writes the workbook with SheetJS; cells are typed `s`/`n`; no formulas.
- **Code (pdfToExcel-38p0cUiA.js):** tesseract worker with PSM AUTO; OCR picks the largest page image or renders at 3× scale.
- **Duplicates:** none for this tool. Related tools: image-to-excel and scan-to-document (C06 OCR family).
