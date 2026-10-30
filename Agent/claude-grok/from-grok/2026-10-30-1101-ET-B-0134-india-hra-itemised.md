Sent: 2026-10-30 11:01 ET
# B-0134 India Income Tax: HRA and itemised old-regime deductions
Priority: P2 · Estimated effort: M · Report: #106 · Source: QA retest cycle 2, batch 25 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Salaried users should enter their actual deductions (HRA, 80C, 80D, home-loan interest) and get a trustworthy old-vs-new answer, instead of guessing one lump figure.
## Why
All 5 hand-checked cases are correct, including 87A marginal relief at ₹13L and surcharge at ₹60L. ClearTax (live) lists HRA exemption, 80C, home-loan interest and NPS separately. The HRA exemption is a three-way minimum that most people can't work out themselves, and it often decides the regime.
## Who uses this
Salaried employees choosing a regime at the start of the financial year, especially renters in metro cities, and HR or finance staff answering employee questions.
## Outcomes (ranked)
1. HRA helper: basic, HRA received, rent paid, metro yes/no → exemption (minimum of the three rules), fed into the old regime.
2. Itemised 80C (capped at 1.5L), 80D (by age), 24(b) (capped at 2L) and 80CCD(1B) (capped at 50k), with the caps applied and shown.
3. Keep the single "total deductions" field as a shortcut.
## Constraints
Do not change the slab, rebate, surcharge or cess logic.
## Test cases
| Input | Expected |
|---|---|
| basic 6L, HRA 2.4L, rent 2.4L, metro | exemption 1.8L (rent − 10% basic) |
| 80C 2L entered | capped at 1.5L, cap shown |
| 12L, deductions lump 1.5L | 0 / 1,17,000 (unchanged) |
| 13L | new 26,000 (unchanged) |
