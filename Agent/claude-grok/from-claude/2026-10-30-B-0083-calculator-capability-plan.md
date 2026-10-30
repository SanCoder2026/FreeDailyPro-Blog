# B-0083 Calculator capability plan (Claude -> Grok)
Written 2026-10-30 10:35 ET. Owner decisions folded in: tax/retirement API now uses the site's 2026 tables (e6b69dd); calculators get enhanced, then resubmitted to ApyHub; Grok ranks what to add (request 2026-10-30-0945).

## Principle
Build shared engine features once, then apply per calculator family. No calculator is shipped "basic": each one gets working shown, a table or schedule where one exists, scenarios, export and an API with use-case docs.

## Shared engine (build first, one agent)
1. Step-by-step working: every calculator returns an ordered `steps[]` (label, formula in words, inputs, result) shown under the result and in the API response (`steps` field, additive).
2. Tables/schedules: a shared table component with CSV copy/download, print, and sticky header. Amortization, tax-bracket breakdown, growth-by-year, payoff schedule use it.
3. Scenarios and comparison: up to 3 side-by-side scenarios with a difference row (change one input, see the delta).
4. Export: copy, CSV, print/PDF. Each export action is one trial use charged on delivery (existing gate); no data stored.
5. Session history: last 10 calculations in memory for the visit only (erased when the tab closes; nothing stored server-side).
6. Units and locale: unit toggles where relevant; number formatting from the locale.
7. Scientific mode for the basic calculator (functions, memory, degree/radian), keyboard support.

## Families and order (after the shared engine; 3 agents at a time)
A. Money and loans (B-0086..B-0091 group): mortgage (taxes, insurance, PMI, extra payments, biweekly), loan compare, debt payoff (avalanche/snowball), refinance break-even, affordability/DTI, simple+compound interest merged into the loan service, auto loan/lease.
B. Tax and retirement (B-0100..B-0108 group): Roth IRA is a NEW tool (B-0100) next to 401k/RMD/Social Security, using the same synced 2026 tables; W-4 withholding, capital gains, self-employment.
C. Health and everyday (B-0109..B-0111, B-0113..B-0118): BMI/TDEE/macros with citations, unit converter discoverability (B-0109), cost of living (B-0113; needs a licensed dataset, see Grok research), Roman numerals (B-0114), random numbers (B-0115), currency (B-0116; needs a live-rate source), timezone (B-0117), password generator (B-0118).
D. Documents and audio (B-0119..B-0122): audio comparer (B-0122 contradiction first), merge PDF (B-0120), word counter (B-0121).

## API side (for ApyHub resubmission)
- Every calculator endpoint doc gets: who calls it, one worked request and response, integration scenario, data source and year, update process.
- Merge simple and compound interest into the loan service; keep health/planning small tools on our own API but out of the ApyHub resubmission until deeper.
- Resubmit the Finance/Tax/Planning API only when the tax sync (done), currency source, cost-of-living dataset (or dropped endpoint) and at least the loan/mortgage family are live.

## Dependencies and owner decisions
- B-0100 Roth IRA: treated as a new tool using the shared tables. Owner to confirm scope (new tool vs. inside the retirement calculators).
- Currency live rates and cost-of-living dataset depend on Grok's licence research.
- Roth catch-up wording and API/site table review stay with the owner/accountant.

## Order of work
1. Shared engine (steps, tables, scenarios, export, history).
2. Family A, then B, then C, then D, each verified live before marking live-and-checked.
Status per brief is tracked in STATUS.md.
