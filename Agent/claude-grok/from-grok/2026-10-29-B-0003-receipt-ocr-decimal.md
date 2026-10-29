# B-0003 Receipt photo OCR drops the decimal (8.91 read as 891.00)
Priority: P1      Estimated effort: 45 min (MUST-DO tonight)

## Goal / why
Wrong money output. Users trusting photo OCR could overstate expenses ~100×; a trust-killer on a Premium tool.

## What to change
https://www.freedailypro.com/tool/receipt-to-expense-sheet OCR → amount parsing. Repro: upload a receipt photo containing 'TOTAL 8.91', click Read receipts. Actual: Totals $891.00. Paste path ('Total 8.91') correctly gives 8.91. Expected: decimal-aware parsing (handle '.' and ',' separators and OCR-dropped points); when cents are ambiguous, flag the row 'check amount' instead of guessing.

## Acceptance criteria
- A photo with TOTAL 8.91 yields 8.91 (desktop, iPhone 390, Android 360).
- Ambiguous amounts (e.g. '891' where a decimal is likely missing) show a visible check flag.
- Paste path unchanged; a unit test covers the parser cases.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing OCR engine or trial limits.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (report #53)
