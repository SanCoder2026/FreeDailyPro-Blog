Sent: 2026-10-30 11:01 ET
# B-0133 GST: multi-item invoices and rate lookup
Priority: P2 · Estimated effort: M · Report: #106 · Source: QA retest cycle 2, batch 25 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A small Indian business should be able to total a simple invoice with items at different GST rates, and find the rate for an item.
## Why
The single-amount math is correct (5 cases, including paise splitting and lakh formatting). ClearTax (live) pairs its GST calculator with HSN lookup and invoice totals. Since GST 2.0 moved many items between rates, people often don't know which rate applies.
## Who uses this
Shopkeepers, freelancers and small suppliers in India raising or checking invoices; buyers checking a bill.
## Outcomes (ranked)
1. Add lines (amount + rate) with a per-rate CGST/SGST/IGST summary and an invoice total in words.
2. A rate finder: search an item or HSN/SAC → suggested rate, with a "confirm with CBIC" note.
3. Keep the single-amount view as the default.
## Constraints
Keep the current rounding rule (equal halves, base adjusted by 1 paisa).
## Test cases
| Input | Expected |
|---|---|
| 1,000 @18 + 500 @5 intra | CGST 90 + 12.50; SGST same; total 1,705 |
| same, inter-state | IGST 205 |
| single 1,000.01 remove @5 | 952.39 / 47.62 (unchanged) |
