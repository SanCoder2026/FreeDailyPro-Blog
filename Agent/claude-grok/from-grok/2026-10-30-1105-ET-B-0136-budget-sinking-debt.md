Sent: 2026-10-30 11:05 ET

# B-0136 Budget planner: sinking funds and debt payments
Priority: P2 · Estimated effort: S–M · Report: #107 · Source: QA sweep + live competitor fetch 2026-10-30 11:01 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Help people plan for irregular costs and debt within the same monthly budget, so "left over" is honest.

## Why
NerdWallet's guide centres on 50/30/20 and also covers debt and sinking funds; ours only has needs/wants/savings rows, so annual bills and debt minimums get lost.

## Who uses this
Households building a first budget; people paying down cards.

## Outcomes (ranked)
1. A row type for debt payment, counted in the right 50/30/20 bucket. 2. Sinking-fund rows entered as yearly amounts and shown as monthly. 3. Existing totals unchanged for current rows.

## Constraints
Math stays visible; reading results never uses a trial use; CSV export includes new rows.

## Test cases
Annual insurance 1200 → 100/month in totals; debt 250 counted in needs; defaults still give $1,050 left over.
