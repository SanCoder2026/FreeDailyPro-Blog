Sent: 2026-11-21 08:14 ET

# FDP-50 test cases (guest; run after fixes)

| ID | Input / steps | Expected | Today (2026-11-21) |
|---|---|---|---|
| T01 | T01 3-page statement, defaults → Download | +1 use; 1 sheet, 76 rows, header repeat dropped, $ amounts numeric, "( )" negative, mm/dd dates | PASS (L01) |
| T02 | Same load: new file → Download | +1 use | FAIL (stays at 1) |
| T03 | Re-download same result | no extra use | PASS |
| T04 | At 10/10 in a fresh context → Download / Save to Google Drive | cap dialog $1/$4.99 | PASS (Z01, zero-drive) |
| T05 | T02 header words | all 5 money columns numeric | FAIL (text) |
| T06 | T03 German | Menge 1500, 2000, 1, 750; Betrag 1234.56; Anteil 12.5% | FAIL (Menge 1.5/2) / PASS rest |
| T07 | T04 French | 1234.56 numeric | FAIL (text) |
| T08 | T05 table in prose + two-column text | only the table (5×3) | PASS |
| T09 | T06 two-row table | "No tables were found…" (documented) | PASS |
| T10 | T07 ZIP/phone/card/codes | text with leading zeros; Spend numeric | PASS |
| T11 | T08 scan, OCR on | values match text layer | PARTIAL (10/104 cells wrong) |
| T12 | T08, OCR off | "No readable text… Turn on OCR" | PASS |
| T13 | T09 password (u123) | unlock dialog, then runs | PASS (no tables in that file) |
| T14 | T10 prose only | "No tables were found" + PDF to Word hint | PASS |
| T15 | T11 "=SUM(…)" text | stored as text, no formulas | PASS (0 `<f>`) |
| T16 | T12 CR/DR, USD | numeric with sign | FAIL (text) |
| T17 | T13 wrapped cells | table found | FAIL (no tables) |
| T18 | T14 40 pages × 40 rows | 1 table, 1601 rows, < 5 s | PASS (0.5 s) |
| T19 | T15 dates auto / Day first | ambiguous left as text with note; Day first converts | PASS |
| T20 | One sheet per page / Everything on one sheet / values off | 3 sheets / 1 sheet / all text | PASS |
| T21 | T16 truncated | "can't be read — it looks damaged… Repair PDF" | PASS |
| T22 | Network | no document bytes POSTed; OCR data from jsDelivr only | PASS |
| T23 | Save to Google Drive / cloud / Open from Drive | sign-in | Untested (sign-in) |
| T24 | Firefox / WebKit subset | same outputs | see subset-*.json |
