Sent: 2026-10-30 10:58 ET
# B-0132 Discount: fixed-amount coupons
Priority: P2 · Estimated effort: S · Report: #105 · Source: QA retest cycle 2, batch 24 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Shoppers should be able to enter a coupon as an amount ("$15 off"), alone or combined with a percent discount, and see the real final price.
## Why
Calculator.net (live) offers "Percent off" and "Fixed amount off". FDP is percent-only. The current math is correct (6 cases, including stacked discounts, tax, price increase and JPY rounding).
## Who uses this
Shoppers comparing sale prices and coupon stacks, and small retailers checking promo pricing.
## Outcomes (ranked)
1. Each discount can be % or a fixed amount.
2. The order of applying them is stated, with a toggle (amount first or percent first).
3. Find mode can also report "you saved X as a fixed amount".
## Constraints
Keep current results, rounding and messages.
## Test cases
| Input | Expected |
|---|---|
| 100, $15 off | 85 |
| 100, 20% then $15 off | 65 |
| 100, $15 off then 20% | 68 |
| 100, $120 off | blocked (cannot go below 0) |
| 100, 20% then 10%, tax 8% | 77.76 (unchanged) |
