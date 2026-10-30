Sent: 2026-10-30 14:53 ET

# B-0278 Income Tax Calculator: add California SDI and convert page-1 impressions
Priority: P1 · Estimated effort: S · Report: QA-REPORT-150 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~14:50 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make state take-home results match what a real pay stub shows, and turn a top-10 ranking for "tax calculator" into clicks.

## Why
GSC page: 5 clicks / 7,449 impressions / 0.1% CTR / avg position 7.5. "tax calculator" 4/4,746/0.1%/pos 7.1. Ranking on page 1 with 0.1% CTR means the snippet is not winning.
Live check ($75,000, single, California, ~14:51 ET): federal $7,670 (taxable $58,900 after $16,100 standard deduction — matches 2026 brackets), FICA $5,738, CA tax $2,775 (matches 2025 FTB schedules less exemption credit), take-home $58,818. California SDI (1.3% of all wages in 2026, no cap, per EDD) is not deducted: $975 missing, so take-home is overstated by ~$975. Competitors fiftystatepay.com and teampredict.ai both show SDI line by line and give ~$57,565 take-home at $75k.

## Who uses this
Employees comparing offers or states, and freelancers estimating net pay.

## Outcomes (ranked)
1. Deduct state payroll taxes on employee wages: CA SDI 1.3% (also NY/NJ/HI/RI/WA/MA-style PFL/SDI where applicable), shown as its own line.
2. Note that CA uses 2025 rates (already shown) — keep the source note.
3. Snippet rewrite: the brand-less title with "Free" should become the suggested title; meta to 140–160.
4. Per-paycheck view (biweekly/semimonthly) — both competitors lead with it.

## SEO
- Now: title "Tax Calculator 2026: Free Federal + State Take-Home Pay" (55); meta 145; H1 "2026 Income Tax Calculator — Federal, State and FICA"; /es localised (good).
- Keywords: tax calculator, income tax calculator 2026, take home pay calculator, state income tax calculator.
- Suggested Title: "Income Tax Calculator 2026: Federal, State & FICA" (49)
- Suggested Meta: "Estimate 2026 take-home pay: federal brackets, FICA and state income tax for all filing statuses, with 401(k) and self-employment options. See your net pay." (156)
- Suggested H1: "2026 Income Tax Calculator — Federal, State and FICA" (keep)
- FAQ: Does it include SDI? · Which year's state rates? · Paycheck vs annual? · Self-employment tax?

## Constraints
Do not change federal math (verified correct). Estimate disclaimer stays.

## Test cases
1. $75,000, single, no state → federal $7,670, FICA $5,738, take-home $61,593 (regression).
2. $75,000, single, California → CA tax $2,775, SDI $975 line, take-home $57,843.
3. $250,000, CA → SDI $3,250 (no wage cap).
4. Self-employed toggle: SDI not applied.
5. Title ≤60, meta 140–160; 390 px no overflow.
