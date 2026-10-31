Sent: 2026-10-31 00:23 ET

# B-0315 Profit and Expense Manager: math correct; add income lines (tickets, sponsors), break-even and budget-vs-actual export; title has no brand
Priority: P3 · Estimated effort: M · Report: QA-REPORT-171 · Source: live probe 2026-10-31 ~00:17-00:23 ET (headless, logged out, 1280 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An event organiser knows during planning and after the event whether it made money, from every income source, and can show that to a client or committee.

## Why
No GSC row for this page in the analytics raw files (checked).
Checked live with "Try a sample" (Sample offsite): Planned $4,600.00, Spent $2,121.70, Left $2,478.30 ✔; per line planned/spent/left ✔. Profit statement: Income $5,000.00 (Fees), Costs $2,121.70, Profit $2,878.30 (57.6%) ✔ (hand-checked); tax paid on costs $161.70 ✔; per head for 5 heads: income $1,000.00, cost $424.34, profit $575.66 ✔. Copy statement / Download PDF / Download CSV present; downloads not run this pass, so the PDF, CSV and Excel files are unchecked.
Capability (checked on the statement): income shows one "Fees" line in the sample. Separate income lines for tickets, sponsorship, merchandise sales and bar split: unverified absence (the income entry screen was not opened this run). Break-even point and scenario (sell-out vs 60%): unverified absence. Pledged vs paid income: unverified absence.
Competitors (live search): Eventrise Finance (income with Pledged/Invoiced/Paid, vendors, invoices, budget vs actual, receipt upload), Lookport (budget, P&L next to ticket sales, break-even, sell-out vs 60% scenario, PDF), VenueArc (income statement with ticket, sponsorship, F&B, merch lines; Preliminary/Review/Final), inbudget and Eventwise (versions, budget vs actuals, cashflow by month).
Ad script error on load "Error: no_div" from adsbygoogle (console) — not a tool fault, noted only.

## Who uses this
Event planners, wedding planners, small promoters and fundraising committees.

## Outcomes (ranked, demand × effort)
1. Verify and, if missing, add income lines by source (tickets, sponsorship, merchandise, bar/F&B, other) with status pledged / paid (M).
2. Break-even: tickets or guests needed to cover costs; a sell-out vs partial-sales scenario (S–M).
3. Budget vs actual sheet in the Excel/PDF export (S).
4. Title with brand (below).

## SEO
- Now: title "Profit and Expense Manager - Budget, Receipts, Profit" (53, no brand); meta 101; H1 "Profit and Expense Manager"; JSON-LD SoftwareApplication, FAQPage (6 Q), BreadcrumbList ✔ (no Organization, no VideoObject); canonical ✔
- Keywords: event budget, event profit and loss, event expense tracker, event budget template, event P&L
- Suggested Title: "Event Profit and Expense Manager | FreeDailyPro" (47)
- Suggested Meta: "Plan an event budget, log receipts, merch and crew hours, and get a profit statement with per-head figures as Excel, CSV or PDF." (128)
- Suggested H1: "Event Profit and Expense Manager"
- FAQ: keep; add: How do I know my break-even point? · Can I track sponsorship income?

## Constraints
Downloads count against the trial (owner rule). Keep "any currency, relabel only" and the flagging of other-currency lines.

## Test cases
1. Try a sample → profit $2,878.30 (57.6%), per head as above.
2. Add ticket income $3,000 (paid) and sponsor $1,000 (pledged) → statement lists both; pledged shown separately.
3. Ticket price $50 → break-even tickets shown.
4. Download Excel → budget-vs-actual sheet present.
