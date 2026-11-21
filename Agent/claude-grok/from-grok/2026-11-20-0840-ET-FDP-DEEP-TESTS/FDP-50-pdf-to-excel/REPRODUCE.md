Sent: 2026-11-21 08:14 ET

# FDP-50: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/pdf-to-excel. The test PDFs are in `evidence/testfiles/` (made by `px-make.js` with Chromium page.pdf, so they have a real text layer).

## P1: per-page-load charging
1. Use a fresh context with uses left. `localStorage['fdp-usage-v1'].usageToday` should be < 10; fresh contexts usually load at 10, so retry if needed.
2. Drop T01 → Extract Tables → Download Excel File. The count goes +1.
3. Click Convert Another → drop T02 → Extract → Download. Repeat with other files. The counter stays put: 15 new workbooks for 1 use in left.json.
4. Reload → new file → Download: +1. Another new file → Download: no change (L21).

## P1: money columns left as text (T02)
1. Drop `T02_header_words.pdf` → Extract. The summary says "4 numbers written as real values." (only Qty).
2. Download and open the workbook. B2:F5 ("Invoice Amount", "Account Balance", "Order Total", "Unit price (no VAT)", "Number of units") are text strings. `=SUM(B2:B5)` gives 0.

## P1: European thousands become decimals (T03)
1. Drop `T03_german.pdf` → Extract → Download.
2. Column C (Menge) holds 1.5, 2, 1 and 750, with number format 0.000. It shows "1.500" but is worth 1.5. SUM is 754.5, not 4,251.

## P2 items
- **French spaces:** T04: "Montant" (1 234,56 €) stays text; the summary says "0 numbers…".
- **CR/DR and currency codes:** T12: "1,234.00 CR" and "USD 1.50" stay text.
- **OCR:** T08 (an image of T01 page 1) → Extract with OCR on. Amount cells read "($111.25)" as -5111.25 (7 of 8), with format 0.00. Compare against T01 page 1.
- **Preview at 0:** in a context at 10/10, drop T02 → Extract. All 5 rows are shown in the preview; Download → cap dialog.
- **Video:** https://www.youtube.com/watch?v=dGgPVkXxdII. At about 0:20 it shows "0 free uses remaining today"; at about 0:39 the Windows picker shows the OneDrive account name.

## P3 items
- **Wrapped cells:** T13 → "No tables were found".
- **Two-digit years:** T15 "Short year" column: 21/11/50 becomes 1950.
