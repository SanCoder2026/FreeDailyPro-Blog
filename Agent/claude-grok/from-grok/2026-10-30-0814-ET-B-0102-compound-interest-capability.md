Sent: 2026-10-30 08:14 ET
# B-0102 Compound Interest: scenarios, withdrawals, solve-for, chart — and merge with the loan service
Priority: P2      Estimated effort: 1 day      Report: #90      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the compound-interest tool more useful than the SEC's Investor.gov calculator (scenarios, withdrawals, solve-for) and follow ApyHub's suggestion to merge simple and compound interest into the loan/interest service instead of listing a "plain growth" API.

## Why
- Report #90: the maths is correct ($2,009.66 ✓), but Investor.gov offers a rate range (± variance) with a chart and negative contributions (withdrawals). FDP has a table only, no withdrawals, no scenarios, no continuous compounding, no solve-for.
- ApyHub: "simple-interest and compound-interest seem very basic … Would you merge simple and compound interest into the loan service?"
- No GSC/GA row for this page in testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md (no metric cited).

## Who uses this
- **Site:** savers and students learning compounding; people planning a savings goal.
- **API callers:** savings/goal features in banking and budgeting apps. They only need it as part of a **loan + interest service** (B-0088), not as a standalone listing.

## Outcomes (ranked)
1. **Chart**: balance vs contributions over time. Low effort.
2. **Rate range**: show results at rate − x and rate + x (as Investor.gov does). Low effort.
3. **Withdrawals**: negative monthly contribution, with a depletion warning. Low effort.
4. **Solve for**: years to reach a target, or the rate/contribution needed. Medium effort.
5. **Continuous compounding**; **annual contribution increase %**; optional **tax on interest** rate. Low effort.
6. **API**: merge into the loan/interest service from B-0088 (simple, compound, amortized). Do not list it standalone.

## Constraints
Not investment advice; trial-use rules unchanged.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | $1,000, 7%, 10y, monthly | $2,009.66 (unchanged) |
| 2 | continuous, same inputs | 1000·e^0.7 = $2,013.75 |
| 3 | target $10,000, $1,000 + $100/mo, 7% monthly | years-to-target shown, matching a manual FV check |
| 4 | contribution −$50/mo on $1,000 at 5% | depletion date shown |
| 5 | range ±2% | three columns: 5% / 7% / 9% |
