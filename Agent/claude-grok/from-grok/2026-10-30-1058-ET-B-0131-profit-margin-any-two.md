Sent: 2026-10-30 10:58 ET
# B-0131 Profit Margin: start from any two numbers, include selling costs
Priority: P2 · Estimated effort: S · Report: #105 · Source: QA retest cycle 2, batch 24 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Sellers should get margin, markup, profit and price from whichever two numbers they know, with shipping and acquisition costs included.
## Why
The math and edge messages are correct (6 cases pass). Live: Shopify's calculator takes markup % plus advanced shipping and customer-acquisition cost; Calculator.net solves from "any two" of cost, revenue, margin and profit. FDP only offers cost + price, or cost + target margin.
## Who uses this
Online sellers and retailers setting prices, wholesalers quoting with a markup, and anyone confused about margin vs markup.
## Outcomes (ranked)
1. Target-markup mode: cost + markup → price and margin.
2. Optional shipping and acquisition cost per unit, included in profit.
3. "Any two" solving (cost/price/profit/margin).
## Constraints
Keep the margin vs markup note and the current edge messages.
## Test cases
| Input | Expected |
|---|---|
| cost 20, markup 75% | price 35, margin 42.9% |
| cost 20, price 35, shipping 3, CAC 2 | profit 10, margin 28.6% |
| price 35, margin 42.9% | cost ≈ 20 |
| target 100% | still "impossible" |
