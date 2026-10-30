Sent: 2026-10-30 08:09 ET
# B-0086 Mortgage Calculator: capability gap vs Calculator.net / Bankrate (cost growth, biweekly, chart, affordability)
Priority: P2      Estimated effort: 1–2 days      Report: #89      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the mortgage tool the best free-to-read option: it already beats competitors on loan programs and cash to close, so close the few remaining gaps and expose them in the API.

## Why
- `analytics/2026-07-10-to-now-raw.md`: /tool/mortgage-calculator 52 GA views (rank 44).
- Report #89 table: Calculator.net has annual cost increases, other costs, biweekly comparison, annual extra payments and a yearly schedule; Bankrate has a breakdown chart and affordability guidance.
- ApyHub held the Finance calculators as "too basic" (30 Oct).

## Outcomes (ranked by demand × effort)
1. **Breakdown chart**: P&I / tax / insurance / HOA / PMI donut, plus a balance-over-time line. Low effort.
2. **Yearly schedule view** alongside monthly; a CSV with both. Low effort.
3. **Biweekly option**: show the payoff date and interest saved with half-payments every 2 weeks. Low effort.
4. **Affordability**: when income is entered, show front/back DTI against 28/36 with a clear pass/stretch label, plus an "other monthly debts" input. Low–medium effort.
5. **Cost growth**: annual % increase for property tax, insurance and HOA, plus a maintenance/other-costs line. Medium effort.
6. **Extra payments**: add yearly recurring. Low effort.
7. **Share link** with inputs in the URL; **API parity** (schedule JSON, biweekly, DTI) with validation.

## Constraints
Trial-use rules unchanged; B-0072 CLS separate; "estimate, confirm with your lender" note kept.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | $400k, 20% down, 6.5%, 30y | P&I $2,022.62 (unchanged) |
| 2 | biweekly on | payoff earlier than Oct 2056; interest saved shown |
| 3 | income $10,000/mo, other debts $500 | front ≈ 24.9% with the default tax/insurance (P&I+tax+ins $2,489.28), back ≈ 29.9%; label "within 28/36" |
| 4 | tax increase 3%/yr | year-2 tax line $366.67×1.03 |
| 5 | yearly view | 30 rows; year-1 interest/principal sum to 12 payments |
