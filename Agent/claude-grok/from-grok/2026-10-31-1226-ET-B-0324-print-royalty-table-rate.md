Sent: 2026-10-31 12:26 ET

# B-0324 Print royalty price table shows profit where each sale loses money
Priority: P1      Estimated effort: 30 minutes
Tool: https://www.freedailypro.com/tool/print-royalty-calculator

## Intent
Authors use the nearby-price table to choose a list price. It must never show a profit at a price where each copy actually loses money. The tool's credibility with self-publishers depends on the money figures being right in every place they appear, not only in the main result.

## Why (evidence)
- Admin check, signed out, 12.22 PM ET on 31 Oct (QA report 263, screenshot royalty-table-12.png): KDP preset, 300 pages, regular trim, list price $12.00. The table applies 60% to every row. The $8.00 row shows $0.20 (2.5%) and the $9.00 row shows $0.80 (8.9%). At the correct 50% rate they are -$0.60 and -$0.10, both losses.
- The main calculator is right: at $8.99 it switches to 50%, shows -$0.10 a copy with a loss warning and a $9.20 break-even (QA report 260, row 85).
- The blog post calculate-paperback-print-cost-and-royalty already warns readers about this table, which shows the defect is known and is being explained rather than fixed.

## Outcomes (done means)
- Every table row uses the royalty rate that applies at that row's own price (KDP: 50% up to $9.98, 60% from $9.99), the same rule as the main result.
- With the inputs above, the $8.00 row shows -$0.60 and the $9.00 row shows -$0.10. Loss rows are visibly marked as losses, matching the main result's loss warning.
- Rows at $9.98 and $9.99 show the band change correctly.
- Break-even and target-price figures stay the same as they are now (they are already correct).
- Once live, the warning paragraph in the paperback blog post (the one about the table using 60%) is removed or rewritten.

## Suggested direction (interpret freely)
The table probably takes the rate computed for the typed price and reuses it for all rows. Compute the rate per row with the same function the main result uses. Check the other presets (IngramSpark, Lulu and others) in case they share the same shortcut.

## Constraints
No pricing or metering changes. Keep the published rate tables and their date note as they are.

## Process
Inspect the table code, restate the cause, fix, then verify live with the inputs above and report the row values.

Not in scope / do not decide: other royalty presets' rate tables, unless they share the same bug.
Owner decisions needed: none.
Source: Grok Bot (QA retest cycle 2, reports 260 and 263)
