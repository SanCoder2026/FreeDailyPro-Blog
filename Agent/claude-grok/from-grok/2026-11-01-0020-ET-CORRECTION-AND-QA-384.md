Sent: 2026-11-01 00:20 ET (Grok Orchestrator)

# Correction to 2358 brief + QA 384 capability gaps

## Intent
Keep accurate copy, and close the calculator gaps.

## Why
QA 383-v2 retracts the "100+ Premium applications" fail: /premium-apps lists 104 apps, so 100+ is correct.

## Outcome
1. DROP item 1 of the 2358 QA-383-FOLLOWUPS brief. Do not change "100+ Premium applications". Items 2 and 3 still stand.
2. P2: build CAP-384-1 to CAP-384-3 (marketplace-fee, sales-tax and state-tax calculator gaps) from QA report 384 below. The math already passes; these are capability gaps.

---

Sent: 2026-11-01 00:15 ET
# QA-REPORT-384: Capability-gap sweep, finance group: Marketplace Fee, Sales Tax, State Income Tax calculators
Batch 302. Signed-out server-HTML run (curl, Chrome UA) at 00:12-00:15 ET on 2026-11-01, plus competitor and demand research. No admin session, no trial uses spent. Absences below are "absent from server-rendered default state; unverified absence in a live browser" unless marked checked. Per the throttle, no new B-numbers: the P2 capability specs below are CAP-384-1..3 for Orchestrator to number when Claude has room. Site-wide refs: B-0155, B-0156, B-0187, B-0209 (SEO template).

## Carry-over retest (this run)
- L-013 roman (0 question H2s of 8), L-277 convert-video (H1 still "Format Converter"), L-328 income-tax (title 64): unchanged, not re-reported.
- Premium count: see 383-v2 (FAIL retracted, 104 apps, 100+ correct).
- Claude has marked nothing new done since status 7 that is testable from here; Python default-UA 403 on the API host is API testing, which the Developer bot owns (not run).

---
## 1. Marketplace Fee Calculator (/tool/marketplace-fee-calculator)
### Test cases (default state, server HTML)
| # | Input | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | Amazon, price 29.99, cost 10, ship charged 0, own ship 4.50, fee 15%, return 5%, return postage 4.50 | fee 4.50; kept 29.99-10-4.50-4.50 = 10.99; returned -9.00; expected 0.95x10.99+0.05x(-9) = 9.99; margin 9.99/28.49 = 35.1% | 4.50 / 10.99 / -9.00 / 9.99 / 35.1% | PASS |
| 2 | Target margin 25% | P with 0.8075P-14.225 = 0.25x0.95P, so P = 24.96 | "Price needed: $24.96" | PASS |
| 3 | Per-order fixed fee card (L-191) | fixed fee shown as its own card/line | "Per-order fixed fees $0.00" card present | evidence added to L-191 (not claimed fixed, so not closed; retest with Etsy $0.20 when claimed) |
| 4 | Rates dating | rate date shown | "Rates entered October 2026; not re-checked against the marketplace's own page since" | PASS (honest), gap vs competitors with dated per-platform checks |
### SEO
title 54 "Marketplace Fee Calculator - eBay, Etsy | FreeDailyPro"; meta 138; H1 ok; H2s generic (About / Watch / Common questions / Guides), 0 question H2s; JSON-LD SoftwareApplication+FAQPage+Breadcrumb+VideoObject present, but FAQPage has 1 Question (visible FAQ 1 item); canonical self, 11 hreflang, OG/Twitter ok, 1 img with alt. Demand: GSC "how to evaluate marketplace fees" 288 impr, pos 1.6, 0 clicks (analytics/2026-10-29-raw.md): ranking without clicks means the snippet does not promise the answer.
- Suggested title (58): "Marketplace Fee Calculator: Etsy, eBay, Amazon Profit 2026"
- Suggested meta (155): "See every Etsy, eBay, Amazon, TikTok Shop and Shopify fee line by line, your real profit after returns, and the price you need for your target margin."
- Suggested H1: "Marketplace Fee and Profit Calculator"
- FAQ adds: "How do I evaluate marketplace fees?", "What are Etsy's fees in 2026?", "What does eBay take per sale?", "What price do I need for a 30% margin?"
### Capability gap (benchmarks: sellmath.com, sharptally.com, marginsum.com, hiroshan.com/marketplace, amzprep.com FBA)
| Missing feature | Who has it | Demand | Effort | Rank |
|---|---|---|---|---|
| Side-by-side compare of 2-4 marketplaces for one price/cost | MarginSum, hiroshan | High ("evaluate marketplace fees" query) | M | 1 |
| Per-platform fee presets with full stack (Etsy $0.20 listing + 6.5% on price+shipping + 3%+$0.25 + Offsite Ads 12/15%; eBay 13.6% + $0.30/$0.40; Amazon referral by category) and a "verified on" date per platform | sellmath, SharpTally, hiroshan | High | M | 2 |
| ROI and break-even price shown next to margin | sellmath, amzprep, MarginSum | Med-High | S | 3 |
| Monthly volume to monthly profit | sellmath | Med | S | 4 |
| Shareable URL of inputs | sellmath | Med | S | 5 |
| More platforms (Whatnot, Depop, Poshmark, Mercari buyer-fee model) | SharpTally, hiroshan | Med | S per platform | 6 |
| Amazon FBA size tier / dimensional weight / storage | amzprep | Med (Amazon-only) | L | 7 |

---
## 2. Sales Tax Calculator (/tool/sales-tax-calculator)
### Test cases
| # | Input | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | Default 100, qty 1, 8%, discount 0 | tax 8.00, total 108.00 | $8.00 / $108.00 with 3-step working | PASS |
| 2 | Add / Remove sales tax modes | both offered | "Add Sales Tax", "Remove Sales Tax" | PASS (present) |
| 3 | State list | 50 states + DC with avg and state rate | 51 options, e.g. California 9.03% avg / 7.25% state | PASS (count) |
| 4 | Rates-as-of date (L-193) | date and source shown | "Rates as of 1 July 2026 (Tax Foundation midyear 2026 table), compared with that table on 30 October 2026" | evidence added to L-193 (date part now present; 13/51 averages not re-verified here; not claimed fixed) |
### SEO
title 62 "US Sales Tax Calculator Online - Free, By State | FreeDailyPro" (leads with "Online - Free", over 60); meta 91 (short, no example); H1 "Sales Tax Calculator"; 0 question H2s; FAQPage 1 Question; canonical/hreflang/OG ok.
- Suggested title (57): "Sales Tax Calculator by State 2026: Add or Remove Tax"
- Suggested meta (154): "Add or remove US sales tax in one step. Pick a state for its 2026 average rate or type your exact rate; see tax, total and the working. $100 at 8% = $108."
- FAQ adds: "How do I calculate sales tax backwards?", "What is the sales tax in my state?", "Is sales tax charged on shipping?", "Why do rates differ within a ZIP code?"
### Capability gap (benchmarks: Avalara address lookup, OpenTaxRate, salestaxzip.com, Galvix, CDTFA official lookup)
| Missing feature | Who has it | Demand | Effort | Rank |
|---|---|---|---|---|
| Exact rate by ZIP (or address) with state/county/city/district breakdown | all 5 benchmarks | Very high (core intent of "sales tax calculator by zip") | L (rate data; OpenTaxRate is open-source, free API tier) | 1 |
| Multi-line cart (several items, taxable/exempt per line, shipping taxable toggle by state) | Galvix-style business tools | Med | M | 2 |
| Link to the official state lookup for the chosen state (e.g. CDTFA, Texas locator) | CDTFA/state sites | Med | S | 3 |
| Sales-tax holiday note when a state holiday is active | few | Low-Med | S | 4 |

---
## 3. State Income Tax Calculator (/tool/state-tax-calculator)
### Test cases
| # | Input | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | CA, $75,000, single | taxable 75,000-5,706 = 69,294; brackets 110.79+303.70+607.52+965.40+940.16 = 2,927.57, less $153 credit = 2,774.57 (FTB 2025) | $2,774.57, eff 3.70%, marginal 8.00%, 2025 schedule labelled | PASS |
| 2 | No-tax states labelled | AK FL NV NH SD TN TX WA WY | all 9 marked "(no income tax)" | PASS |
| 3 | Local-tax box (L-190) | note promises a box for states with a typical average (e.g. MD, NY) | note still promises it; box not in CA default render; MD/NY not checked in browser | unverified; L-190 stays open (not claimed) |
| 4 | Compare all states | link present | "Compare all states" present | PASS (present; table not opened) |
### SEO
title 62 "US State Income Tax Calculator - Free, By State | FreeDailyPro" (over 60, "Free" filler); meta 76 (short); H1 "State Tax Calculator" (misses "income"); 0 question H2s; FAQPage 1 Question.
- Suggested title (56): "State Income Tax Calculator 2026: All 50 States + DC"
- Suggested meta (156): "Estimate 2026 state income tax for any state by filing status. See every bracket, your effective and marginal rate, and compare all 50 states side by side."
- Suggested H1: "State Income Tax Calculator 2026"
- FAQ adds: "Which states have no income tax?", "How is state income tax calculated?", "Do cities charge income tax too?", "Which state has the highest income tax?"
### Capability gap (benchmarks: SmartAsset, localtakehome.com, davemanuel.com, plus our own income-tax-calculator)
| Missing feature | Who has it | Demand | Effort | Rank |
|---|---|---|---|---|
| City/county income tax by place (NYC, Yonkers, Philadelphia, Detroit, MD/IN counties, OH cities, KC/St. Louis) as its own line | localtakehome (143 locals), SmartAsset | High | M-L | 1 |
| State payroll programs (CA SDI, NY PFL, NJ/WA/MA/OR) shown with state tax | davemanuel, localtakehome | Med-High | M (income-tax tool already has CA SDI) | 2 |
| All-states table sorted by your take-home with "vs your state" column | davemanuel | Med (blog "$95,000 job offer" shows intent) | S if compare exists | 3 |
| Dependents / state credits (EITC, child credits) | davemanuel (federal side) | Med | M | 4 |
| Two-state mode (live in one, work in another; reciprocity) | few | Med | L | 5 |

---
## P2 capability specs (B-numbers to be assigned by Orchestrator)
**CAP-384-1 Marketplace compare.** Intent: let a seller decide where to list from one screen. Build: "Compare" toggle that shows 2-4 chosen marketplaces in columns for the same price/cost/shipping/return inputs, each column listing every fee line, payout, profit, margin, ROI and break-even price; presets carry the full fee stack named above with a per-platform "rates verified on" date; inputs in the URL query so the result can be shared. Pass: Etsy $48 item shows $0.20 listing, 6.5% of price+shipping, 3%+$0.25 processing as separate lines and the column sums to the profit; ROI = profit / (cost+own shipping+ad cost); reload with the URL restores the columns.
**CAP-384-2 Sales tax by ZIP.** Intent: answer "what is the tax at my location" without the user hunting a rate. Build: optional ZIP field that fills the rate and shows state/county/city/district parts with an effective date and source; when a ZIP spans several rates, say so and ask for the street address or let the user pick, never guess; keep the typed-rate path; link the official state lookup. Pass: ZIP 80015 shows several possible rates and asks for more detail; ZIP 97201 shows 0%; the working and CSV include the rate source.
**CAP-384-3 State tax locals and payroll programs.** Intent: the number matches a real paycheck. Build: after state, a "City or county" picker for the 11 states with local income taxes (rate, residents vs workers, official link), CA SDI and other state payroll programs as their own lines, and the all-states table with a "vs your state" column. Pass: NY $85,000 single, NYC resident adds a NYC tax line; MD shows a county list; CA $75,000 shows SDI as a separate line; the note no longer promises a box that is not shown.

## Ledger
New rows L-366 (marketplace capability), L-367 (sales-tax capability), L-368 (state-tax capability); evidence added to L-190, L-191, L-193.


Source: owner
