Sent: 2026-10-30 08:14 ET
# B-0100 Roth IRA: no tool exists — add a Roth mode with 2026 limits and phase-outs
Priority: P2      Estimated effort: 1–2 days      Report: #90      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Give Roth searchers a real answer on the site (how much can I contribute, what will it grow to, Roth vs traditional), built on the existing retirement engine so it is data-backed rather than "plain growth".

## Why
- Report #90: `/tool/roth-ira-calculator` and `/tool/roth-calculator` → 404; nothing in the sitemap.
- Competitors: NerdWallet computes the 2026 contribution limit from filing status + MAGI phase-out; Calculator.net compares Roth vs a taxable account with an annual schedule.
- ApyHub accepts calculators that depend on "yearly limits and official tables", which is exactly the Roth phase-out logic.

## Who uses this
- **Site:** US savers deciding Roth vs traditional; high earners checking phase-out and backdoor eligibility. There is no GSC data yet, because no page exists.
- **API callers:** robo-advisers, HR benefits portals, budgeting apps that need the **current-year limit + phase-out** (hard part: yearly IRS updates).

## Outcomes (ranked)
1. **Eligibility**: tax year, filing status, MAGI, age → allowed contribution (full / reduced by the IRS proration formula / none). 2026: $7,500, $8,600 at 50+; single $153k–$168k, MFJ $242k–$252k, MFS lived-with-spouse $0–$10k. Cite IRS and state the refresh owner.
2. **Growth**: balance at retirement, Roth vs taxable account (marginal rate input) vs traditional IRA, with an annual schedule and CSV.
3. **Backdoor note** when over the limit (link to the guide, not advice).
4. Route `/tool/roth-ira-calculator` to the new tool; add it to the sitemap.
5. **API parity** with `taxYear` and `sourceUpdated` in the response; 400 on bad input.

## Constraints
Not investment advice; trial-use rules unchanged; no visible "free".

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | 2026, single, MAGI $100k, age 30 | $7,500 allowed |
| 2 | 2026, single, MAGI $160,500, age 30 | reduced: 7,500 × (168,000 − 160,500)/15,000 = $3,750 |
| 3 | 2026, MFJ, MAGI $260k | $0, with a backdoor note |
| 4 | $30k balance, $7,500/yr, 6%, 30→65, 25% marginal | Roth balance ≈ $1.07M vs taxable lower (compare with Calculator.net's $1,066,343 for the same inputs; small differences from timing assumptions should be documented) |
