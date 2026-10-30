Sent: 2026-10-30 14:29 ET

# B-0265 Mortgage Calculator: #3 page in the last 7 days; title leads with "Free"; meta 133; add PMI, HOA and an amortization chart
Priority: P2 · Estimated effort: M · Report: #146 · Source: SEO backfill 10 (next top-GA tested tools after #144): curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:28–14:29 ET; GA4/GSC from analytics/2026-07-10-to-now-raw.md and testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md: GA #44 (52 views); last 7 days 34 views (#3 page site-wide, 1m30s engagement in 28d). No GSC query row in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A home buyer should get the full monthly cost (PITI + PMI + HOA), a payoff date and a yearly schedule, and trust it over the bank sites.
## Why
- Function tested earlier: CLS 0.32–0.48 on mobile (L-129); gaps chart, yearly view, biweekly, DTI 28/36 (L-160).
- Title "Mortgage Calculator Online Free - Payment, Payoff Date" (54): "Free" in the middle, no brand. **Meta 133.** H1 "Mortgage Calculator".
- 200, sitemap, 11 hreflang, valid JSON-LD. /es serves the English title → **B-0123**.
- **Top 5 (~14:29 ET):** Zillow, LendingTree, Redfin, Bankrate, NerdWallet all add **PMI when the down payment is under 20%** and **HOA fees**; down payment as $ or %; payoff date and total interest (NerdWallet); yearly amortization table (LendingTree, NerdWallet); FHA/VA notes (NerdWallet). These add to L-160.
## Who uses this
First-time buyers and people refinancing.
## Outcomes (ranked)
1. PMI (auto under 20% down) and HOA in the monthly total.
2. Yearly amortization table and chart (L-160).
3. Title/meta fixes; fix mobile CLS (L-129).
## SEO
- **Keywords:** "mortgage calculator", "mortgage calculator with pmi and taxes", "monthly mortgage payment", "amortization schedule".
- **Suggested:**
  - Title: `Mortgage Calculator – Payment, Taxes & Payoff | FreeDailyPro` (60)
  - Meta: `Work out your monthly mortgage payment with property tax and insurance, see total interest and your payoff date, and view the full payment schedule by year.` (156)
  - H1: `Mortgage Calculator with Taxes and Insurance`
  - FAQ: "What is PITI?" · "When do I pay PMI?" → "Usually under 20% down." · "How is the payment calculated?" (formula)
## Constraints
Do not show live lender rates; keep it a calculator.
## Test cases
1. $300k loan, 6.5%, 30 years → P&I $1,896.20.
2. 10% down → PMI line appears.
3. Title ≤ 60, no "Free"; meta 140–160.
