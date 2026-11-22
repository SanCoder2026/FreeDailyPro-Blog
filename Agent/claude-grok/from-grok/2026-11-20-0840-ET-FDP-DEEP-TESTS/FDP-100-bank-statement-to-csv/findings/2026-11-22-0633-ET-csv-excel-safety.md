Sent: 2026-11-22 06:34 ET

Sent: 2026-11-22 06:33 ET

# FDP-100 CSV / Excel import safety (downloads from D01–D04)

- `statement.csv` (L): bytes start EF BB BF (UTF-8 BOM); CRLF; header `Date,Description,Amount,Balance`; ISO dates; amounts `-23.40` (dot decimal).
- Formula guard: `'=HYPERLINK(""http://example.invalid/x"",""Refund"")`, `'+SUM(1,2) Example Shop`, `'@Home Example Furnishings`, `'-2+3 Odd Merchant Name`. Plain numbers are unchanged.
- Non-Latin text: Cyrillic, accents and emoji are byte-exact. Japanese is split with spaces and Arabic is reversed presentation forms; these come from the text join (P3 #11), not the CSV writer.
- `statement.xlsx`: sheet "Transactions"; dates are date cells (yyyy-mm-dd); descriptions are text (formula-like names stay text); amounts and balances are numbers (#,##0.00); empty balance left blank.
- Locale import (LibreOffice 1031 de-DE vs 1033 en-US, same CSV of F): de-DE gives 0/20 numeric amounts (text "-1200.00"); en-US gives 20/20, sum −2,685.04 (= expected). Excel itself was not available on the box; LibreOffice is the stand-in.
- #84 check: no 1.2 in the files. "-1200.00" is exported correctly. The 1.2 appears only when a European user retypes a cell (V03).
