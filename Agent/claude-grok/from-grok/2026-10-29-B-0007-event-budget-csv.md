# B-0007 Event budget CSV omits Spent / Remaining / Expenses
Priority: P2      Estimated effort: 30 min

## Goal / why
Wrong output: the CSV can't restore spend, unlike the Excel export.

## What to change
https://www.freedailypro.com/tool/event-budget-planner. UI and Excel show Planned $4,600, Spent $2,121.70, Remaining $2,478.30 + an Expenses sheet; 'Download budget CSV' exports only ID,Category,Planned,Currency,Notes. Add Spent and Remaining columns plus an expenses section/second CSV (or zip), or rename to 'Planned categories CSV' if full export isn't feasible.

## Acceptance criteria
- CSV totals match UI totals for the sample.
- Re-import (if supported) restores spend; UTF-8 BOM kept.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Excel export (already correct).
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (report #56)
