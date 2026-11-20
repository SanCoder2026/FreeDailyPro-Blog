Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: desk findings

- **Written:** 2026-11-19 (ET). Sources: curl of the tool, 9 locales, /ar, the sitemap and the blog (`html/`); JS bundles (`js/`); WebSearch.
- **Classification:** Professional Tool, Finance, Tax & Retirement. TEST-ORDER row 10, grouped with test-plan rank 9 (Income Tax / Tax Calculator), cluster C25. **GSC data is not available.**

## Page and SEO
- **Title:** "State Income Tax Calculator 2026, 50 States | FreeDailyPro".
- **Meta:** "Estimate 2026 state income tax for any state by filing status. See every bracket, your effective and marginal rate, and compare all 50 states side by side." It is clear.
- **H1:** "State Income Tax Calculator 2026".
- **Schema:**
  - FAQPage with 7 questions
  - SoftwareApplication with an Offer of 4.99 and **no billing period** (P2)
  - VideoObject uRiqzi4ARPY
  - BreadcrumbList
- **Sitemap:** present (lastmod 2026-11-19) with a video block. The video title is "How to Estimate State Income Tax by State **Free** | FreeDailyPro.com" (P2 wording). There is no publication_date.
- **Brand query** "FreeDailyPro state tax calculator" (WebSearch index): the tool is **#1**.

## Locales
- All 9 hreflang locales (es, pt, fr, de, ja, hi, zh, ko, id) return 200 with the **English title and H1** (P2: thin duplicates). Unlike #9, es is not localized.
- /ar returns 404 and is not in hreflang.

## FAQ vs behaviour
- **"Do cities charge income tax too?"** It lists NYC, Yonkers, the MD counties, Baltimore City, Philadelphia, Detroit, Kansas City, St. Louis and Columbus. This matches the code.
- **"How is state income tax calculated? … any state credit is taken off":** only CA's credit is modelled; the OR, DE and IA credits are not (live findings §5).
- **The disclaimer** says "credits … are not modelled", which contradicts the FAQ line above.
- **The site Terms and FAQ** say calculators take no trial use, while the tool charges 1 per visit for copy, save or print. Under owner policy the charge is intended, so the Terms and FAQ wording should change (P1 wording, shared with #9).

## Blog: /blog/state-tax-calculator ("Compare State Income Tax on a $95,000 Job Offer", 17 Oct 2026)
- **Stale numbers** (live tool at 13:29 EST, `json/blog95.json`):

| State | Blog | Tool now |
|---|---|---|
| NY | $4,652 | $4,564.75 |
| CA | $4,847 | $4,589.98 |
| OR | $7,763 | $7,738.88 |
| NY with local box | $7,697 | $7,609.75 |

  - NC, CO and TX match.
  - The NY figure uses the 2025 rates (4–6%); the "6%" marginal rate is stale too (the tool now says 5.9%).
- **Misleading sentence:** "The tool uses the federal standard deduction for the filing status (16,100 …) as its starting point and then applies each state's own deduction". The tool uses each state's own deduction; the federal one applies only where a state conforms.
- **Not mentioned:** the city/county picker and the payroll-program lines (newer features).
- It documents "blank or negative values are treated as zero" (see the live P1 on "85k").

## Cluster C25
- **Overlap:** income-tax-calculator (#9) and paycheck-calculator (#11) embed the same state engine.
- **Unique here:** compare all states, city/county lines and the payroll programs.
- **Recommendation:** keep it. Fixing the HoH and Utah logic in `stateTaxData` fixes all three tools.

## Competitors (WebSearch 2026-11-19)
- **SumAtlas** (all 51 ranked, compare two states, SDI), **TaxSaveIQ** (per-state pages, SALT), **TaxMath** (state vs state), **AfterTaxLab** (federal + FICA + state, 60 cities) and the **Tax Foundation** table.
- **FreeDailyPro ahead:**
  - named local taxes with bands (NYC, MD counties, Philadelphia non-resident)
  - 7 payroll programs with sources and dates
  - bracket table and steps
  - CSV/PDF export
  - local-only
- **Behind:**
  - HoH schedules
  - personal credits (OR, DE, IA)
  - Utah credit logic
  - "next $1,000" figure (SumAtlas)
  - two-state compare
