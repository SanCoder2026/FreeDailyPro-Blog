Sent: 2026-10-30 08:17 ET
# B-0103 College 529: cost-based goal, accessible labels, tax comparison — fix the 2,029-impression zero-click page
Priority: P2      Estimated effort: 1 day      Report: #91      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Turn the 529 page into the plan people searching for "529" expect: start from what college will cost and end with a monthly amount, and make every input accessible.

## Why
- testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md: `/tool/college-529-calculator` 2,029 impressions, 0 clicks.
- Report #91: the 4 main inputs have no accessible names. Calculator.net builds the goal from today's cost, college inflation, years of attendance and % from savings, and compares the tax on returns.

## Who uses this
Parents and grandparents of young children; new parents choosing a state plan; people checking whether they are on track before FAFSA years.

## Outcomes (ranked)
1. **Accessible labels** on all inputs (`<label for>` or aria-label). Low effort.
2. **Cost-based goal**: school type (with dated, sourced reference costs) or today's cost × college-inflation % × years of attendance × % from savings → goal → monthly amount. Low/medium effort.
3. **529 vs taxable account** (tax on returns), plus an optional state deduction rate. Low effort.
4. **Year-by-year table and chart**; one-time lump sum. Low effort.
5. Snippet: a title/meta that answer "how much to save per month for college". Low effort.

## Constraints
Not investment advice; trial-use rules unchanged; no visible "free".

## Test cases
| # | Check | Expected |
|---|---|---|
| 1 | Accessibility tree | 4 named inputs |
| 2 | $30,990 today, 5% inflation, 4 yrs, starts in 3 yrs, 100% from savings, $0 saved, 5% return | monthly amount shown; goal equals the sum of the inflated yearly costs |
| 3 | Tax rate 25% vs 529 | 529 needs a lower monthly amount |
