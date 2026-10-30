Sent: 2026-10-30 08:07 ET
# B-0089 Income Tax Calculator: capability gap vs Calculator.net / NerdWallet (refund, credits, itemising)
Priority: P2      Estimated effort: 2–4 days      Report: #88      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the most-searched calculator on the site (7,449 impressions on the tool page) at least as useful as Calculator.net and NerdWallet, so searchers stay on it, the paid API is no longer "too basic", and the page can earn clicks above position 7.

## Why
- GA/GSC: `analytics/2026-07-10-to-now-raw.md` (GSC rows are clicks/impressions/CTR/position): /tool/income-tax-calculator 5/7,449/0.1%/7.5; query "tax calculator" 4/4,746/0.1%/7.1.
- ApyHub held the Finance/Tax calculator API as "too basic" on 30 Oct (orchestrator email notes).
- Report #88 table: competitors offer refund/owed, credits, itemised-vs-standard, other income and a tax-year switch; FDP offers none of these. FDP already wins on 50-state coverage, so keep and build on that.

## Outcomes (ranked by demand × effort)
1. **Refund or owed**: a "Federal tax withheld" (and state withheld) input → "Estimated refund $X" / "You may owe $X". Low effort, matches "refund estimator" intent.
2. **Dependents and credits**: number of children under 17 → Child Tax Credit ($2,200 each, $1,700 refundable, phase-out from $200k/$400k MFJ); optional EITC and dependent-care fields, or an "Other credits $" field. Medium effort.
3. **Deductions**: standard vs itemised (mortgage interest, SALT capped at $40,400 for 2026 with phase-down, charity) with automatic max; senior +$6,000 deduction (65+); tips/overtime deductions (2025–2028). Medium effort.
4. **Other income**: interest, ordinary/qualified dividends, short/long-term capital gains (0/15/20% LTCG brackets), Social Security. Medium effort.
5. **Tax-year switch** 2025/2026. Low effort, since the 2025 tables already exist for the state notes.
6. **Breakdown**: a bracket-by-bracket table and a simple stacked bar (federal/FICA/state/take-home); per-paycheck view (weekly/biweekly/monthly). Low effort.
7. **Save/share**: URL query parameters restore inputs (no PII stored). Export: the existing Save as text + CSV of the breakdown.
8. **API parity**: every new input/output above is exposed on the calculator API with a JSON schema, validation (400 on negative/NaN), and documented examples. This is the ApyHub "depth" ask.

## Constraints
- Trial-use rules unchanged (reading is free; copy/save/print/share = 1 per visit).
- Cite official sources (IRS Rev. Proc., SSA) and keep the "estimate, not tax advice" note.
- No visible "free" (B-0019). Keep the B-0057 state-year labels honest.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | $85,000 single, no state, withheld $9,000 | federal $9,870; refund/owe shows owe $870 |
| 2 | $120,000 MFJ, 2 children | CTC −$4,400 applied before refund/owe |
| 3 | itemised $35,000 MFJ | standard ($32,200 for 2026) used; label says why |
| 4 | LTCG $10,000 on a $60,000 single wage | LTCG taxed at 15% for the part above the 0% threshold, shown separately |
| 5 | toggle 2025 | brackets/std deduction switch to 2025 values |
| 6 | API POST with the case 2 inputs | same numbers as the UI; −1 income → 400 with a field error |
