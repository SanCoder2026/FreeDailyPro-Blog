Sent: 2026-10-31 12:23 PM ET

# QA ADDENDUM — P1: print-royalty-calculator nearby-price table uses 60% royalty on every row

**Intent:** The table should never tell an author that a price makes money when every sale actually loses money. Authors choose their list price from this table, so a wrong row leads straight to a bad pricing decision.

**What's wrong:** On /tool/print-royalty-calculator (Amazon KDP, black ink, 300 pages, printing cost $4.60), with the list price at $12.00, the main calculator is correct (60%, earns $2.60). But the nearby-price table applies the **60%** rate to every row, including rows below $9.99, where KDP's rule (as the page itself states) is **50%**:

| Row | Shown (60%) | Correct (50%) |
|---|---|---|
| $8.00 | +$0.20 | **−$0.60** |
| $9.00 | +$0.80 | **−$0.10** |

So the table shows a profit where each sale loses money. Rows from $9.99 up ($10, $11, $12) are correct at 60%.

**Fix:** Work out the royalty rate for each row from that row's own list price, using the same rule as the main calculator: 50% at $9.98 or less, 60% from $9.99, for each marketplace/preset. Show negative earnings clearly as a loss. Then check the other presets and rate modes too.

**Evidence:** 2026-10-31-1223-ET-royalty-table-12.png (in this folder).

Source: owner
