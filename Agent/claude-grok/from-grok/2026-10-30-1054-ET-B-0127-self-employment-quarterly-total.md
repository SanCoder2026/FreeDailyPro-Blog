Sent: 2026-10-30 10:54 ET
# B-0127 Self-Employment Tax: one quarterly payment figure
Priority: P2 · Estimated effort: M · Report: #104 · Source: QA retest cycle 2, batch 23 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A freelancer should leave with the actual amount to pay each quarter (SE tax + federal income tax, optionally state), not only the SE part.
## Why
The page's own note says the payments "should cover income tax as well", then sends people to another tool. Keeper (fetched live) offers quarterly-tax and tax-bill calculators that include federal and state tax. The SE math itself is correct (all 6 hand-checked cases pass).
## Who uses this
New freelancers and 1099 contractors working out their first estimated payment, and side-gig earners with W-2 wages.
## Outcomes (ranked)
1. An optional "include income tax" step that reuses the Income Tax tool's self-employed mode and shows one quarterly total with the parts listed.
2. Safe-harbour hint (100%/110% of last year's tax) as an alternative figure.
3. Optional state estimate, reusing the State Tax tool.
4. A short message for a negative profit ("no SE tax on a loss").
## Constraints
Keep the current SE figures and lines unchanged.
## Test cases
| Input | Expected |
|---|---|
| 60,000 single, income tax off | 8,477.73 / 2,119.43 per quarter (unchanged) |
| 60,000 single, income tax on | SE + federal income tax after the half-SE deduction, both shown |
| 60,000 + W-2 180,000 | SE 2,483.58 unchanged |
| −5,000 | 0 + loss message |
