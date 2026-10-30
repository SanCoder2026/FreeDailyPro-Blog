Sent: 2026-10-30 10:47 ET
# B-0125 Marketplace Fee: show every fee in the breakdown
Priority: P2 · Estimated effort: S · Report: #103 · Source: QA retest cycle 2, batch 22 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A seller should be able to add up the cards on screen and reach the profit shown.
## Why
On Etsy the $0.20 per-order fee is deducted (profit 12.19) but not shown, so the visible cards add up to 12.39. A seller who checks the math loses trust. GSC: "how to evaluate marketplace fees" 0 clicks / 288 impr / pos 1.6. The page ranks but earns no clicks, so the result has to be convincing. Live eBay fees show 13.6% charged on shipping and sales tax, with a 2.35% tier above $7,500. Competitor Salecalc's Etsy rates date from 2022.
## Who uses this
Small sellers on Etsy, eBay, Amazon and Mercari pricing a listing, and resellers checking whether a flip is worth it.
## Outcomes (ranked)
1. Per-order fixed fees and processing fixed fees get their own result lines (or are folded into labelled totals) so the cards sum to the profit.
2. The price-0 error message names the actual problem ("Enter a selling price above 0").
3. Every preset shows a "rates checked <month year>" line, as eBay already does.
4. Optional: eBay can include sales tax in the fee base and apply the >$7,500 tier.
## Constraints
Keep the current math; Amazon, Etsy and eBay were hand-checked correct.
## Test cases
| Input | Expected |
|---|---|
| Etsy defaults (29.99/10/4.50) | lines include $0.20; visible sum = 12.19 |
| eBay defaults | fee 4.08 + per-order 0.40 shown; profit 11.01 |
| price 0 | message about price, not "negative / outside 0–100" |
