Sent: 2026-10-30 11:01 ET
# B-0135 Student Loan: compare with income-driven repayment
Priority: P2 · Estimated effort: M · Report: #106 · Source: QA retest cycle 2, batch 25 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Borrowers should see whether standard repayment or an income-driven plan suits them, using current federal plan rules, without leaving the page.
## Why
Standard amortisation is correct (4 cases match an independent script, to the cent). NerdWallet (live) covers income-driven plans and refinancing. FDP's footer names "IBR, SAVE, PAYE" and sends users away. The federal plan lineup has changed recently and needs checking against studentaid.gov (it didn't render for a live fetch here).
## Who uses this
Recent graduates choosing a plan, and parents or borrowers deciding whether extra payments or a lower payment makes more sense.
## Outcomes (ranked)
1. The plan names in the footer match studentaid.gov as of the review date, with a dated line.
2. An optional income, household size and state → estimated income-driven payment under the plans currently open to new borrowers, next to the standard payment, with total paid and term.
3. Refinance comparison: new rate/term → payment and interest difference, with a note that federal protections are lost.
## Constraints
Keep the current standard results, extra-payment and lump-sum logic.
## Test cases
| Input | Expected |
|---|---|
| 30,000 @5.5% 10y | 325.58 / 9,069.36 (unchanged) |
| + income 45,000, household 1 | IDR payment shown with plan name and source date |
| refinance @4% 10y | payment 303.74; interest saved shown |
