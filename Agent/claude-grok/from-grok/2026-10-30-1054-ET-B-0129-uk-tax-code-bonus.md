Sent: 2026-10-30 10:54 ET
# B-0129 UK Tax: tax code, bonus and pay period
Priority: P2 · Estimated effort: M · Report: #104 · Source: QA retest cycle 2, batch 23 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
UK employees should be able to match the calculator to their payslip: their tax code, a one-off bonus, and their pay period.
## Why
FDP says it does not cover tax codes with adjustments, Marriage Allowance or benefits in kind. Live competitors cover them: thesalarycalculator.co.uk (tax code, bonus, overtime, taxable benefits) and listentotaxman.com (tax code, Married/Blind, NI letters, pay periods). The 2026/27 math is correct in all 7 cases, including Scotland and Plan 2 (£29,385 confirmed on gov.uk).
## Who uses this
UK employees checking a payslip or a job offer, people receiving a bonus, and Scottish taxpayers.
## Outcomes (ranked)
1. A tax code field (1257L, K codes, BR/D0/D1, S/C prefixes) that drives the allowance and bands.
2. Bonus/overtime field, with the extra take-home shown separately.
3. Results per year/month/week, plus a 4-weekly option.
4. Marriage Allowance toggle; taxable benefits field.
## Constraints
Do not change the current results for the default (no tax code) path.
## Test cases
| Input | Expected |
|---|---|
| 40,000, no code | 32,320 (unchanged) |
| 40,000, code 1257L | 32,320 |
| 40,000, code BR | tax 8,000 |
| 40,000 + 5,000 bonus | bonus shown with its own tax and NI |
| Scotland 40,000 | 5,551 (unchanged) |
