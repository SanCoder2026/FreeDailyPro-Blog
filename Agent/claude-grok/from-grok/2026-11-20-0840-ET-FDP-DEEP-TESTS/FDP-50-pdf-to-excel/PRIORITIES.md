Sent: 2026-11-21 08:14 ET

# FDP-50 PDF to Excel: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | **Per-page-load charging.** One trial use covered 15 different workbooks in one page load (left.json L01–L18; 2 `usage.log` POSTs for 17 downloads in total). After a reload took the count to 2, another new workbook downloaded with no charge (L21) | json/left.json, outputs/ | Charge per new result (file + options hash) and check the cap on every Download. Shared ToolPage DownloadButton fix (same as FDP-44–49) |
| P1 (data) | **Money columns silently left as text when the header contains an ID-like word.** `X` in `tablesToExcel` (`id|no|number|account|invoice|order|ref|…`) skips number conversion for the whole column. "Invoice Amount", "Account Balance", "Order Total", "Unit price (no VAT)" and "Number of units" all came out as text ("1,200.00" strings). SUM gives 0, and no note says why. The page promises "numbers … are written as real values, so SUM, sorting and filters work", and the target users are bookkeepers | outputs/L02, json/left.json L02 ("4 numbers written") | Test the identifier heuristic on the values (leading zeros, fixed width, no decimals or separators) rather than the header words. At minimum, match whole headers ("ID", "Invoice No", "Account #"). When a numeric-looking column is kept as text, add a note naming it |
| P1 (data) | **German/European whole thousands become decimals.** "1.500" → 1.5 and "2.000" → 2 (format 0.000). `^(\d+)\.(\d+)$` treats a dot as the decimal point even when the column's other values use "." as a thousands separator. The Menge column sums to 754.5 instead of 4,251, and it looks right on screen | outputs/L03 | Decide the separators per column, from any value that shows both separators ("1.234,56") or a comma decimal. Treat "1.500" as ambiguous; leave it as text with a note, or offer a "decimal comma" option |
| P2 | **French/Swiss space thousands ("1 234,56 €") stay text.** Those columns can't be summed (0 numbers written) | outputs/L04 | Accept space, narrow no-break space and apostrophe as thousands separators |
| P2 | **Bank "CR/DR" suffixes and currency codes ("USD 1.50", "1,234.00 CR") stay text** | outputs/L12 | Parse CR/DR (DR negative) and 3-letter ISO codes |
| P2 | **OCR reads "($111.25)" as -5111.25.** It happened on 7 of 8 parenthesised amounts, plus 3 digit misreads. The result is a silent ×46 error, under the generic "check numbers" warning | outputs/L08 vs L16, json/ocr-compare.txt (100 dpi page image) | After OCR, treat a leading "5"/"S" right after "(" in a currency column as "$". Flag cells whose format fell back to "0.00" in a "$" column |
| P2 | **Video:** old UI ("10 free uses daily", "0 free uses remaining today"; no Options box or preview); "FREE · PRIVATE · NO LOGIN"; "200+ Free Productivity Tools" end card; description "Try … free" / "Free daily uses"; the Windows picker shows the creator's OneDrive name | video/f07crop.png, f13pick.png, sheet01–03 | Re-record the current UI with "trial uses" wording on a clean profile |
| P2 (owner question) | **Preview at 0 trial uses** shows the first 8 rows of every sheet as selectable text. Small tables (≤8 rows) are fully readable at 0 (Z01: all 5 rows), although the workbook (typed numbers/dates) stays gated | screens/cases/Z01.png | Owner call: keep as is (helpful check), or blur or limit to 3 rows at 0 |
| P2 | Locale pages (see devices-locales findings) | json/matrix-results.json | |
| P3 | A table with wrapped multi-line cells (4 rows) isn't found at all ("No tables were found") | outputs none / L13 | At least say "a table may have wrapped cells", or merge continuation lines that have empty other columns |
| P3 | Two-digit years: "21/11/50" → 1950 and "/49" → 2049 (pivot 49). Excel uses 29 | outputs/L15 | Match Excel's pivot, or note it |
| P3 | Meta description 75 chars; og-default; VideoObject title "How to Convert PDF Tables to Excel Online" vs the video "How to Use PDF to Excel – Free Step-by-Step Walkthrough" | html/ | Fuller meta, own OG image, sync VideoObject |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:**
  - Save to Google Drive: Google sign-in popup with uses left; cap dialog at 0.
  - Save to my cloud storage: "Sign in with your email first", $4.99/month add-on.
  - Open from Google Drive: Google popup.
  - Paid-pass output.
