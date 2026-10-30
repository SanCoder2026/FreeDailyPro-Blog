Sent: 2026-10-30 13:02 ET

# B-0195 Excel/CSV Converter: choose sheet and delimiter, preview more
Priority: P2 · Estimated effort: S · Report: #124 · Source: QA sweep + live competitor fetch 2026-10-30 12:59 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People converting spreadsheets should control what comes out without having to open Excel.
## Why
- Upload of q.csv (quoted commas, escaped quotes, an embedded newline, a leading-zero "007", É) was detected as "comma-separated, UTF-8 — 3 rows, 3 columns" and the preview is correct ✓
- It has a BOM option and formula-injection protection (good). Its Download buttons are untested at 0 trial uses (B-0156).
- convertcsv mentions header ×53, quote ×13, delimiter ×7 and encoding ×5 (live fetch 12:59 ET). There's no output delimiter or encoding choice, and no way to pick the sheet for multi-sheet .xlsx.
- Website tool for the paid "Convert and Parse Raw CSV" API (rule 1).
## Who uses this
Office and finance users moving data between Excel and other systems.
## Outcomes (ranked)
1. A sheet picker for .xlsx inputs with more than one sheet.
2. Choice of output delimiter (, ; tab |) and encoding (UTF-8 / Windows-1252).
3. An option to keep leading zeros (and long IDs) as text in .xlsx.
## Constraints
Everything stays in the browser. Keep the BOM and injection options.
## Test cases
1. A 2-sheet xlsx → pick Sheet2 → CSV of Sheet2.
2. "007" → stays 007 in the xlsx cell.
3. Semicolon output → `name;note;n`.
