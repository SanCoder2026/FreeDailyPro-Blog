Sent: 2026-10-30 10:47 ET
# B-0126 Sales Tax: date the state rates and refresh them
Priority: P2 · Estimated effort: S–M · Report: #103 · Source: QA retest cycle 2, batch 22 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Users should know how current the preset rates are, and the presets should match a published current source.
## Why
13 of 51 state averages differ from Tax Foundation's 2026 table (fetched live 10:44 ET), e.g. LA 10.13 vs 10.11, WA 9.57 vs 9.51, WY 5.39 vs 5.56, NC 7.10 vs 7.00, and the page shows no date. Avalara (live) offers ZIP/address rates updated monthly; Calculator.net solves for any of the three values.
## Who uses this
Shoppers estimating checkout totals, small businesses quoting prices, and people backing tax out of a receipt.
## Outcomes (ranked)
1. Presets match one named source, with "rates as of <date>" shown.
2. A note that local rates vary, with a prompt to type the exact rate (Custom already exists).
3. Optional: a ZIP lookup, or a link to the state's lookup.
## Constraints
The math is correct (add, remove, quantity, discount hand-checked); do not change it.
## Test cases
| Input | Expected |
|---|---|
| Louisiana preset | 10.11% (TF 2026) or a dated alternative source |
| Wyoming preset | 5.56% |
| any state | "as of" date visible at 1280 and 390 |
| TN, 19.99 × 3, 10% off | 59.16 (unchanged) |
