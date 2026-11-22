Sent: 2026-11-22 06:03 ET

Sent: 2026-11-22 06:03 ET

# FDP-99 shipped-code review and local replay (2026-11-22 05:53–06:00 ET)

Chunks (evidence/js): `LegalProductionDesk-DnUlw46t.js` (desk), `batesNumbering-CBMvEZsH.js` (shared stamp engine with Bates Numbering), `ToolPage-B4roIUf_.js` (download helper `vt`, trial badge `nt`), `WorkflowProductGate-BDNk2iP2.js`, `workflowCta-oWYKzOWD.js`, `useExportGate-CyqDPJOh.js` (loaded, not imported by the desk).

| Page claim | Code | Match |
|---|---|---|
| Running Bates ranges with warnings for gaps and mistakes | `je()`: start/digits/prefix checks, width overflow, duplicates, missing reasons/descriptions, page count must be ≥1 | Yes |
| One button stamps every PDF and builds a ZIP | `L()`: `production/` folder, `<Begin>_<name>.pdf`, then production-log.csv, withheld-documents.csv, privilege-log.csv, cover-letter.txt → `<matter>-production.zip` | Yes |
| Withheld get no numbers | rows with `withhold` skipped; later ranges shift | Yes |
| Privilege log with date, author, recipients, description | `ee()` columns; `ve()` warnings for missing fields | Yes |
| Cover letter from the list | `Ne()`: date, recipient, Re:, volume, counts, ranges, redacted/withheld sentences | Yes |
| Each log as CSV or Excel | production log CSV+XLSX, privilege log CSV+XLSX, withheld **CSV only** | Partly (R6) |
| Legend on every page | `s()` draws the legend on every page | Yes |
| Back up lists, not PDFs; cleared when the tab closes | BackupBar + useSessionStored | Yes |
| Page counts must match | `ye()` (pdf.js numPages vs list) | Yes (hidden pages not counted, R1) |
| Doesn't redact | No redaction code | Yes |
| Stamping | pdf-lib load → white box + bold label (drawTextAnywhere), `pageView` rotation → save; no `copyPages` | In place; keeps hidden objects (R1, R2) |
| Downloads | `S()` = ToolPage `vt(blob, name)` with no options (#98 passes `{free:true}`) | R3 |

## Local replay (`scripts/rep99-stamp.js`, same pdf-lib load → draw → save as `s()`)
1. **#93 output `core-r2-0-book-removed-pages.pdf`** (book.pdf, p5 removed): stamped 19 pages ABC000001–19. `recover93.py` on the stamped file recovers **3 hidden pages**: "PAGE-5-SECRET account 4000-0000-0000-0005" with `gone_ssn=gone_ssn-VALUE`, "PAGE-10-SECRET…", "PAGE-2-SECRET…" with `keep_name`. None has a Bates label.
2. **#87 Redact PDF output `left-0-redacted_secrets.pdf`**: after stamping, the page text still has no name/SSN/email/card (the #87 removals hold), but the embedded file `notes.txt` ("Private notes about Jonathan Reed, SSN 123-45-6789") is still inside. The same stamping on the unredacted original keeps everything, so the desk can't tell the two apart.

The replay is a reimplementation of the stamping path, not the live desk; confirm with S01/S02 once signed in.
