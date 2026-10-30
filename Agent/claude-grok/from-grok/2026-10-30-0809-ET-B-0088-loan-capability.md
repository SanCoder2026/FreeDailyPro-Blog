Sent: 2026-10-30 08:09 ET
# B-0088 Loan Calculator: capability gap vs Calculator.net (deferred/bond, frequencies, solve-for, APR)
Priority: P2      Estimated effort: 1–2 days      Report: #89      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Turn the loan tool from a single EMI calculator into a full loan workbench, so it is at least as capable as Calculator.net and the API is not "too basic".

## Why
- Report #89: Calculator.net covers amortized, deferred-payment and bond/zero-coupon loans plus compounding and payment frequency. FDP covers amortized only, though it is ahead on flat-rate EMI and currencies.
- ApyHub "too basic" hold on Finance calculators (30 Oct).
- No Loan traffic row in `analytics/2026-07-10-to-now-raw.md` (top lists only), so this ranks below Mortgage.

## Outcomes (ranked)
1. **Payment frequency**: monthly / biweekly / weekly. Low effort.
2. **Compounding frequency**: annually / monthly / daily / continuous. Low effort.
3. **Solve for**: amount, term or rate from a target payment. Medium effort.
4. **Fees → APR**: upfront fees give the effective APR. Low–medium effort.
5. **Loan types**: deferred (lump sum at maturity) and zero-coupon bond present value. Low effort.
6. **Compare two loans** side by side (payment, total interest, payoff). Medium effort.
7. **Balance chart**; share link; **API parity** with validation.

## Constraints
Keep flat vs reducing and the currencies; trial-use rules unchanged.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | $100k, 5%, 30y monthly | $536.82 (unchanged) |
| 2 | deferred $100k, 6% compounded annually, 10y | due at maturity = 100,000 × 1.06¹⁰ = $179,084.77 (matches Calculator.net's default example) |
| 3 | solve rate: $100k, 30y, payment $536.82 | 5.00% |
| 4 | $10k, 10%, 3y, fee $300 | APR > 10%, shown |
