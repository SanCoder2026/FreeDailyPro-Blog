Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: desk findings

- **Written:** 2026-11-19 13:21 EST. Sources: curl of the tool, locales, /terms, /faq, /pricing, sitemap and blog posts (`html/`); JS bundles (`js/`); WebSearch.
- **Classification:** Professional Tool, Finance, Tax & Retirement. TEST-ORDER row 9. Test-plan rank 9: 7,449 impressions, position 7.5, CTR 0.1% (owner's export). **GSC data is not available** to this tester.

## Page and SEO
- **Title:** "Income Tax Calculator 2026: Federal, State & FICA | FreeDailyPro".
- **Meta:** 156 chars.
- **H1:** "2026 Income Tax Calculator — Federal, State and FICA". It is strong and specific.
- **Schema:**
  - FAQPage with 10 questions
  - SoftwareApplication with an Offer of 4.99 and **no billing period** (P2; same as earlier tools)
  - VideoObject UvcrEE6Swwc
- **Sitemap:** listed, lastmod 2026-11-19, with a video block. The video block title "How to Calculate US Income Tax Online **Free** – Federal State FICA" differs from the YouTube title, and its publication date is 2026-09-22 vs the YouTube upload date 20260923 (likely a timezone difference).
- **CTR 0.1% at position 7.5:** the title is not the problem.
  - Snippet: the meta leads with "Estimate 2026 take-home pay". Competitors (pay44, takehomeus, netpaycalculator, paychecktakehomecalculator, netwagetax) all promise "all 50 states + local", and paychecktakehomecalculator advertises 107 cities including NYC and Philadelphia.
  - Local taxes and HoH accuracy are the content gaps (see live findings).
- **Brand query** "FreeDailyPro income tax calculator 2026" (WebSearch index, not Google): the tool page is **not** in the top 5. The hits were a Blogspot mirror, /solutions/freelancer, /category/tax-calculators (it 301s to /category/finance-calculators), the comparison blog and paycheck-calculator. This is an index snapshot only.

## Locales (hreflang: en, es, pt, fr, de, ja, hi, zh, ko, id, x-default)
- **All return 200, are self-canonical and set `lang`.**
- **Only es is localized:** "Calculadora de impuestos 2026 de EE. UU. gratis | FreeDailyPro".
  - **P2:** "gratis" in the title and og/twitter titles, while copy/save/print cost trial uses. Owner wording rule: say "trial uses".
- **P2:** de, fr, hi, id, ja, ko, pt and zh keep the English title, description and H1 under a localized `lang`. These are thin duplicates.
- **/ar/tool/income-tax-calculator returns 404.** It is not in hreflang, so that is consistent. The matrix's /ar entry was misconfigured (relative URL); curl covered it.

## Terms and FAQ vs behaviour (P0)
- **/terms:** "Text utilities, calculators and simple converters take no trial use at all."
- **/faq (also in the FAQ schema):** "Text, calculator and converter tools (… unit and tax calculators …) never use a trial use."
- **Tool page and blog:** "Copying, saving or printing uses 1 per visit." This is confirmed live (see live findings §6).
- The cap dialog promises a pass "removes the 'Created with FreeDailyPro.com' mark". The .txt does carry "Calculated with FreeDailyPro.com", so the dialog copy fits here.

## Blog
- **Related posts:**
  - `/blog/estimate-us-self-employment-tax-2026`: accurate SE math, but it states the Income Tax Calculator does **not** model QBI. It does, so the post is stale (P2).
  - `/blog/us-uk-india-tax-calculators-compared`
  - `/blog/self-employed-tax-retirement-calculators`
  - `/blog/paycheck-calculator`
  - `/blog/state-tax-calculator`
- **No dedicated post:** `/blog/income-tax-calculator` returns 404, and no sitemap entry with that slug was found (live-verified for this slug only).

## Cluster C25 overlap
- **Same family:** paycheck-calculator ("Take-Home Pay"), state-tax-calculator ("50 States"), self-employment-tax, 401k-calculator, india-income-tax (#288) and uk-tax-calculator.
- **Overlap:** income-tax and paycheck both compute federal + FICA + state take-home, so the risk is keyword cannibalisation on "take-home pay".
- **Recommendation:** keep both and differentiate.
  - income-tax: annual liability and brackets
  - paycheck: per-period withholding and W-4
  - Cross-link them with one line each (the page already links all of them under "Guides and next steps").

## Competitors (WebSearch, 2026-11-19)
- pay44.app, takehomeus.com, netpaycalculator.app, paychecktakehomecalculator.com and netwagetax.com: 50 states + DC, SS 6.2% to $184,500, 401(k)/HSA pre-tax, and in some cases cities.
- **FreeDailyPro ahead:**
  - it runs locally
  - it shows its sources and rate dates per state ("Rates last updated: 11 October 2026", per-state source notes)
  - it has an SE mode with QBI
  - it has a 401(k) age catch-up
- **Behind:**
  - local taxes
  - HoH state schedules
  - HSA field
  - senior deduction
  - copying a result costs a trial use (competitors don't charge for this)
