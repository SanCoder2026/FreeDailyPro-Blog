Sent: 2026-11-20 08:40 ET

# Desk findings: paycheck-calculator

- **Run:** 2026-11-19 13:36–13:47 EST (box `date`, ET). curl, JS bundles, WebSearch. **GSC data is not available.**

## Page and SEO (`html/tool.html`)

| Item | Live | Note |
|---|---|---|
| HTTP / canonical | 200, self-canonical | PASS |
| Title | "Paycheck Calculator Online - Take-Home Pay \| FreeDailyPro" | Generic; no "2026", no "state tax / 401(k)". The es page title is stronger |
| Meta description | "Estimate take-home pay after federal tax and FICA withholding. Fast, right in your browser." | **Omits state tax, 401(k), HSA, hourly** (the tool does all of them). The category page uses the same stale line. The es meta already lists state, 401(k) and HSA/FSA |
| H1 | "Paycheck Calculator" | No year or scope |
| JSON-LD | SoftwareApplication, Offer 4.99 USD (no billing period), FAQPage with **1 question**, VideoObject (uploadDate 2026-09-22) | #10 has 7 FAQs; this page has 1 |
| hreflang | en, es, pt, fr, de, ja, hi, zh, ko, id, x-default | **Only es is translated** (title, H1, meta). fr/de/pt/ja/hi/zh/ko/id serve the English page under their own URLs. /ar → 404 (not in hreflang, so consistent) |
| Brand query | WebSearch "paycheck calculator take-home pay 2026 freedailypro": tool #1, blog #2, API blog #3 | Search index only, not GSC |

## Competitors (WebSearch, 13:46 EST)

ADP, PaycheckCity, SmartAsset (and NetPayGuide) cover all 50 states **plus local/city taxes**, work and residence state, post-tax deductions, bonus/supplemental pay, multiple hourly rates, and W-4 inputs. Sources: smartasset.com/taxes/paycheck-calculator, paycheckcity.com/calculator, eathealthy365 NYC comparison, netpayguide.com/best-paycheck-calculator.

FreeDailyPro has: all 50 states + DC (52 options incl. Custom), filing status, 4 pay frequencies, hourly with overtime, 401(k), section 125 premiums, HSA/FSA, exact 2026 federal/FICA incl. Additional Medicare, an honest footer. **Missing:** local taxes (NYC, Philadelphia, MD counties etc., which the sister State Tax Calculator already computes), state payroll programs other than CA SDI (also already in #10), 401(k)/HSA limit warnings, Roth/post-tax deductions, bonus pay, W-4 extra withholding.

## Cluster C25 overlap

Shares the stateTaxData engine with income-tax-calculator (#9) and state-tax-calculator (#10). HoH = single and the Utah structure (reported in #10) also show here. #10 has local taxes and 7 payroll programs; #11 does not, so the same CA/NY/NJ salary gives different state-side totals across the two tools. Keep both pages (different jobs); share the payroll/local module.

## Blog (`html/blog.html`, /blog/paycheck-calculator, Oct 24, 2026)

Good angle ($90k offer to biweekly take-home). TX, 401(k), health, hourly, semi-monthly and monthly figures match the live tool exactly. **The CA paragraph is stale** ($2,606.28 / $4,382 / $168.53 vs live $2,571.15 / $4,125 + SDI $1,170 / $203.66). It doesn't mention CA SDI.

## FAQ / guide vs behaviour

The one FAQ ("Will this match my actual paycheck exactly?") and the How-to match behaviour. The footer discloses missing NJ/NY/HI/RI/WA/MA programs and local taxes. Nothing warns about 401(k) / HSA limits.

## Trial-use wording (shared, P1)

Page note: "Reading results never uses a trial use. Copying, saving or printing uses 1 per visit." /terms: "Text utilities, calculators and simple converters take no trial use at all". /faq: "Text, calculator and converter tools … never use a trial use". Re-checked by curl at 13:44 EST (`html/terms.html`, `html/faq.html`). Owner policy: charges are intended, so fix the Terms/FAQ wording.
