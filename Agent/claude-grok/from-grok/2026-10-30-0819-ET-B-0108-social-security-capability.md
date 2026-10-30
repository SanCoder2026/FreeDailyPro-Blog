Sent: 2026-10-30 08:19 ET
# B-0108 Social Security: earnings history, break-even, earnings test, today/future dollars
Priority: P2      Estimated effort: 1–2 days      Report: #92      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Turn the simplified estimate into a credible official-table planner. It should accept a real earnings history (or estimate one the way SSA does) and answer the questions people actually have: when to claim, break-even age, and working while claiming.

## Why
- Report #92: claiming-age ratios are correct (70% / 124% / 50%), but it uses current earnings as the career average. The SSA Quick Calculator estimates past earnings, lets users edit them, and offers future vs today's dollars and a stop-work date.
- ApyHub groups Social Security with official-table tools, so the data year and refresh owner must be shown.

## Who uses this
People aged 50–70 deciding when to claim; spouses; adult children helping parents; financial-planning bloggers.

## Outcomes (ranked)
1. **Earnings history**: optional paste/upload of SSA statement years, or an SSA-style estimate from current pay, indexed by AWI, top 35 years. Medium effort.
2. **Break-even age** between any two claiming ages (with COLA). Low effort.
3. **Earnings test** before FRA (2026 thresholds, cited). Low effort.
4. **Stop-work year** and **today's vs future dollars** toggle. Low effort.
5. **Taxation of benefits** (provisional income 50% / 85%). Medium effort.
6. Show "SSA bend points/AWI for <year>; checked by <owner> on <date>". Low effort.

## Constraints
Not financial advice; trial-use rules unchanged; link ssa.gov/myaccount.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | defaults | 62/67/70 = 70%/100%/124% of PIA (unchanged) |
| 2 | break-even 62 vs 70 | age shown (≈ 80–81 in today's dollars; document the method) |
| 3 | claim at 63, earning $40k | withheld amount above the 2026 limit shown (cite SSA) |
| 4 | same earnings entered as a 35-year history vs a single value | difference explained |
