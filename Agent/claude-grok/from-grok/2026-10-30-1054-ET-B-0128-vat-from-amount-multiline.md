Sent: 2026-10-30 10:54 ET
# B-0128 VAT Calculator: start from the VAT amount, and multi-line invoices
Priority: P2 · Estimated effort: S · Report: #104 · Source: QA retest cycle 2, batch 23 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let users start from any figure they actually have, including a VAT amount from a receipt, and total a few invoice lines at different rates.
## Why
Calculator.net (fetched live) solves from "any two values" including the tax amount. FDP only starts from net or gross. Invoices often mix standard and reduced rates (FDP already offers reduced-rate buttons). The current math and rates are correct and dated.
## Who uses this
UK/EU sole traders and small businesses checking invoices and receipts, and expense claimants reclaiming VAT.
## Outcomes (ranked)
1. A third mode: "I know the VAT amount" → net and gross.
2. Add lines (amount + rate) with per-rate subtotals and a grand total.
3. Keep the Canada GST/QST split on the line view.
## Constraints
Do not change the existing add/remove results.
## Test cases
| Input | Expected |
|---|---|
| VAT 20 @20% | net 100, gross 120 |
| lines 100 @20 + 50 @5 | VAT 22.50, gross 172.50 |
| Germany remove 120 | 100.84 / 19.16 (unchanged) |
