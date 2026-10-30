Sent: 2026-10-30 08:17 ET
# B-0105 FIRE: savings-rate framing, chart, Coast FIRE
Priority: P2      Estimated effort: 0.5 day      Report: #91      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make FIRE the clearest early-retirement planner by adding the savings-rate view people expect and a chart. It is already ahead on Lean/Fat variants.

## Why
- Report #91: correct (3.88% real return ✓, $1M at 4%). Networthify centres on income → savings rate → years and has a chart; FDP has neither.
- ApyHub calls FIRE "plain growth", so the value is the site experience only.

## Who uses this
Savers aged 20–45 aiming to retire early; FIRE-community readers comparing Lean/Fat/Coast targets.

## Outcomes (ranked)
1. **Income input → savings rate %**, and years shown as a function of savings rate. Low effort.
2. **Chart** of the portfolio vs the FIRE number. Low effort.
3. **Coast FIRE** (amount needed now so you can stop contributing) and **Barista FIRE** (part-time income). Low effort.

## Constraints
Not investment advice; trial-use rules unchanged.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | defaults | $1,000,000 / 25 y 11 m (unchanged) |
| 2 | income $50k, expenses $20k, $0 saved, 5% real, 4% WR | savings rate 60%; ≈12.4 yrs (Networthify, perpetual-withdrawal basis; document any difference) |
| 3 | Coast: age 30, retire 60, $1M target, 5% real | Coast number = 1,000,000 / 1.05^30 ≈ $231,377 |
