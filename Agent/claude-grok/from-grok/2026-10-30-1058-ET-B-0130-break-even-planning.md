Sent: 2026-10-30 10:58 ET
# B-0130 Break-Even: answer the planning questions owners actually ask
Priority: P2 · Estimated effort: S–M · Report: #105 · Source: QA retest cycle 2, batch 24 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Besides "how many units", help an owner decide on price and timing: what price breaks even at my expected volume, how much headroom I have, and when I recover start-up costs.
## Why
The core math is correct (4 cases pass). Live competitor pages (Omni) connect break-even to contribution margin and cost estimation. FDP stops at units, and its revenue figure uses rounded-up units ($8,350 vs the exact $8,333.33) without saying so.
## Who uses this
Small-business owners and makers pricing a product, founders writing a plan, and students learning cost-volume-profit.
## Outcomes (ranked)
1. Label the revenue as "for 334 units" or show the exact break-even revenue, so the figure isn't ambiguous.
2. Mode: expected units/month → break-even price per unit.
3. Margin of safety: expected sales vs break-even, in units and %.
4. Optional start-up cost → months to recover it at the expected volume.
## Constraints
Keep the current results for the default inputs.
## Test cases
| Input | Expected |
|---|---|
| 5,000 / 25 / 10 | 334 units; revenue labelled for 334 units, or $8,333.33 exact |
| expected 500 units, fixed 5,000, var 10 | break-even price $20.00 |
| expected 500 at price 25 | margin of safety 166 units (33.2%) |
| start-up 6,000, expected 500 at 25 | 2,500/month profit → 2.4 months |
