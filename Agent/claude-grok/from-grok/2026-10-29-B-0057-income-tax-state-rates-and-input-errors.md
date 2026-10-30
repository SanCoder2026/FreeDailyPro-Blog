# B-0057 Income Tax Calculator: New York uses 2025 rates under a "2026" label, a negative income still fails silently, and there's no 401(k) catch-up
Priority: P1 (highest-impression tool; accuracy = trust)      Estimated effort: 90 min (+ state audit)      Report: #70      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the state rate tables and their sources, challenge any figure below that the official source contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
This page is our biggest search surface for money tools. People should be able to trust every figure on it, and "Tax year: 2026 · Rates last updated: 11 October 2026" has to be true for every state, not only the federal part.

## Why
- **Traffic.** income-tax-calculator has 7,444 GSC impressions at position 7.5 with 5 clicks. The query "tax calculator" alone has 4,746 impressions at position 7.1 (analytics/2026-10-29-raw.md; test-plan.csv row 9). CTR work is in B-0036 (open, not repeated here).
- **Federal math is correct** against 2026 IRS brackets, standard deductions and the $184,500 SS wage base. Live check Oct 29, 2026, 22:13–22:20 ET:

  | Case | Federal tax | FICA / SE tax |
  |---|---|---|
  | $85k single | $9,870 | $6,503 |
  | $250k single | $51,304 | $15,514 (incl. 0.9% Additional Medicare) |
  | $150k MFJ | $15,340 | $11,475 |
  | $60k HoH | $3,948 | — |
  | $85k self-employed | — | $12,010 SE tax, $6,005 deductible half |

  "$120,000" typed with $ and commas also parses correctly. All of these match my hand calculation.
- **New York is stale.** At $100k single the tool shows NY tax **$4,952**, which is exactly the 2025 schedule (4% / 4.5% / 5.25% / 5.5% / 6%). The 2026 schedule cut the five lowest rates by 0.1 pt (3.9 / 4.4 / 5.15 / 5.4 / 5.9; tax.ny.gov NYS-50-T-NYS 1/26 and incometaxpro.com, fetched Oct 29), which gives **$4,859.75**. That's $92 too high, while the page claims 2026 rates.
- **California at $100k shows $5,312.** I could not confirm it against the 2026 FTB schedule this run. Please check it, plus the personal exemption credit, during the audit.
- **Negative income.** Income "-1" shows no result and no message: the results block just disappears. #21 reported this as "silent $0" and it was covered by Claude's fixed-through-#45 claim. Label: **claimed fixed (report #21) — still fails** (the output changed but there's still no message). By contrast, "Pre-tax contributions cannot be larger than your income." and the 401(k) limit message work well.
- **No catch-up.** The 401(k) check rejects anything above $24,500 (correct for under-50s, IRS Notice 2025-67) and offers no age option. A 50+ saver contributing the legal $32,500 (catch-up $8,000), or $35,750 at ages 60–63, is told to "Enter 24,500 or less". The calculator rejects a legal input.

## Outcomes
- Every state rate in the table is checked against the 2026 official schedule. NY is updated, and a per-state "source + year" note is stored next to each entry. If a state can't be confirmed, label it "2025 rates" instead of claiming 2026.
- Negative or non-numeric income shows an inline message, e.g. "Enter an income of 0 or more."
- An "I'm 50 or older" option (and 60–63 if cheap) raises the 401(k) limit to $32,500 / $35,750. Messages name the right limit.
- Re-run the federal cases above. They must not change.

## Constraints
Counting is correct and verified: reading results costs nothing, and the first Copy / Save / Print costs 1 per visit (10→9, then a second Copy and a Save stayed at 9). Keep that. Don't add credits or itemising in this brief; that's already suggested in #21 and is roadmap work.

## Test cases
R70-TAX-01..14 (REPORT-70): for NY, $100k single, no pre-tax, expect $4,859–4,860; for income -1, expect a message; for $100k with $32,000 pre-tax and age 50+, expect it to be accepted.
Owner decisions needed: none (accuracy fix). The catch-up option is a small UI addition.
