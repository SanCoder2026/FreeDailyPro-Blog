Sent: 2026-10-30 14:19 ET

# QA-REPORT-141 ADDENDUM — admin session ~14:15–14:17 ET
Supersedes nothing; adds admin evidence to QA-REPORT-141 (B-0249–B-0251). Downloads were saved to /workspace/fdp-qa/batch-60/downloads/ (wrong path) and copied to retest-cycle-2/batch-60/downloads/ (QA_Doc.pdf, exhibits-stamped.zip). Verified on the box at ~14:19 ET with pypdf and pdftotext.

## document-assembler (B-0249, L-308)
- **Confirmed bug, not gating:** with no cover title, Assemble does nothing. The only hint is static help text "A cover needs a title"; no inline error, no focus.
- With title "QA Doc": toast "Document assembled!", QA_Doc.pdf 55,007 B, 7 pages.
- pypdf: p1 cover "QA Doc"; p2 "Table of Contents · docA 1 · docB 4"; p3–p7 = docA (3) + docB (2), stamped page numbers 1–5. Bookmarks: docA, docB. TOC page numbers match the stamped numbers. Source pages had no extractable text beyond the stamped numbers (admin's docA/docB files).
- Brief change: Outcome 1 stands (show an inline error and focus the title field). Trim from gaps: TOC, bookmarks and page numbers exist.

## exhibit-stamper (B-0250, L-309)
- exhibits-stamped.zip: docA-exhibit.pdf (28,704 B, 3 pp), docB-exhibit.pdf (19,525 B, 2 pp), exhibit-index.csv.
- pdftotext: "Exhibit A" on docA page 1 only; "Exhibit B" on docB page 1 only ✔.
- CSV: `Exhibit,Document,Stamped file,Pages,Description` with rows A/docA.pdf/3 and B/docB.pdf/2 ✔ (Description empty).
- Trim from gaps: the label in file names and an exhibit index already exist. Gate-before-preview finding stands.

## caption-generator (B-0251, L-310) — quality fail, supports B-0251
- All 12 captions are templates that paste the user's text verbatim, starting lowercase ("new coffee shop opening in Pune…"); the detail line is appended unchanged; no rewrite, no use of the city or event.
- Hashtags are junk: `#NewCoffeeShopOpeningPune #New #Coffee #Shop #Opening`.
- Professional tone example: "Now available: new coffee shop opening in Pune."
- No caption file was saved to downloads; the full 12 captions must be quoted from the admin session evidence (only the lines above were supplied).
- Outcomes: real generation; sentence case; relevant hashtags (e.g. #PuneCafe, #OatMilkLatte).
