Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: live functional findings

- **Written:** 2026-11-19 13:32:10 EST (box `date`, ET). Guest, headless Playwright 1.65.1 (Chromium). No sign-in, no card or email entered, no ad clicks.
- **Raw results:**
  - `json/cases-S01-S30.json` (S01–S30 + S10b)
  - `json/compare-75000-single.json` (all 51 rows)
  - `json/blog95.json`
  - `json/gate.json` (export actions)
  - `json/kbd.json`, `json/axe.json`, `json/probe.json`

## 1. What is right (PASS)
Each case was checked by hand against the state's own figures.
- **CA single $75k:** $2,774.57. This matches FTB 2025 Schedule X with the $5,706 standard deduction and $153 credit, and SumAtlas. **CA MFJ $150k:** $5,549.14, matching Schedule Y and the $306 credit. **CA $10M:** the 1% Mental Health Services Tax is applied.
- **NY single:**
  - $85k gives $3,993.00, matching the 2026 NYS-50-T rates.
  - NYC gives $2,859.69 (bands 3.078–3.876%).
  - Yonkers gives $668.83 (16.75% of state tax).
  - PFL gives $367.20.
- **MD $85k:**
  - state $3,673.88
  - Montgomery $2,510.40 (3.20%)
  - Anne Arundel $2,186.43 (bands)
  - Frederick MFS $2,092.12 (bands; matches the Comptroller's 2026 withholding table)
- **Philadelphia:** resident 3.735% → $3,174.75; non-resident 3.425% → $2,911.25. Both match the phila.gov rates from 1 July 2026.
- **Other states:**
  - IL $3,567.71 (4.95%, $2,925 exemption)
  - MA $3,530
  - NJ $2,596 (incl. TDI $142.50 and FLI)
  - WA PFML $605.40 + WA Cares $435
  - TX $0
  - NC single $2,483.78
- **The "Compare all states" table** lists 51 rows, sorted by tax. Clicking a row selects that state. It costs no trial use.
- **Negative income** shows the alert "Income cannot be negative".
- **The CSV** (`downloads/live-state-tax-ca.csv`) has a UTF-8 BOM, numeric cells and no formula risk. The .txt export carries the full breakdown, sources and "Calculated with FreeDailyPro.com" (intentional).

## 2. P1: head of household is computed as single in every state
- In the shared engine `stateTaxData` `s()`, the standard deduction is `std[mfj ? 1 : 0]` and brackets are joint only for MFJ. So HoH gets the single deduction and single brackets, except in SC, which has a phase table. This is the same engine as income-tax-calculator (#9).
- **CA HoH $75k:** the tool shows $2,774.57 (= single). FTB 2025 Schedule Z with the $11,412 deduction gives **$1,118.19**, so the tool overstates by **$1,656** (2.5×).
- **NC HoH $75k:** the tool shows $2,483.78 (= single). NC's HoH deduction is $19,125 (G.S. 105-153.5), which gives **$2,229.41**, so the tool overstates by $254.
- **NY HoH $85k:** = single ($3,993). NY has a separate HoH deduction ($11,200) and brackets.
- **GA HoH = single:** this may be correct for GA (unverified).
- The Compare view uses the same engine, so every HoH ranking carries this.

## 3. P1: Utah is computed with a standard deduction it doesn't have
- **Tool:** UT $75k single shows **$2,621.05** = 4.45% × (75,000 − 16,100).
- **Utah's 2026 rules** (TC-40 draft instructions and the Legislature's 2026 tax-credit review): 4.45% of income, minus the taxpayer tax credit. The credit is 6% × the federal standard deduction (966), reduced by 1.3% of income above $18,696 (731.95).
- That gives 3,337.50 − 234.05 = **$3,103.45**, so the tool **understates by about $482**.
- Above about $93k the credit is fully phased out but the tool still deducts $16,100. The gap then reaches **$716**. SumAtlas shows $3,110 at $75k.

## 4. P1: "85k", "abc" and other non-numbers silently show $0.00
- Typing "85k" or "abc" shows "Estimated California State Income Tax $0.00" with SDI $0.00. There is no alert and `aria-invalid` is not set (`screens/live/input-85k-shows-zero.png`).
- The Income Tax Calculator (#9) rejects the same inputs with "Enter an income as a number".
- The blog even documents the behaviour ("blank or negative values are treated as zero").

## 5. P2: personal credits and exemptions omitted in some states
- The footer says "Uses each state's standard deduction and exemptions; credits … are not modelled". The page FAQ says "the brackets are added up and **any state credit is taken off**".
- **Omitted, and confirmed against the state source:**
  - Oregon's $256 exemption credit (AGI ≤ $100k; OR-40 instructions): OR $75k shows $5,989 vs $5,733.
  - Delaware's $110 personal credit (30 Del. C. § 1110): DE shows $3,719 vs $3,609.
- **Likely omitted (secondary source only):** Iowa's $40 credit ($2,238 vs $2,198) and Rhode Island's personal exemption ($2,393 vs $2,196).
- The CA $153 credit *is* modelled, so the treatment is inconsistent.
- **Unverified differences above $100** vs SumAtlas (an independent calculator, not an official source) at $75k single: SC (+$497), WI (−$312), NE (+$176), AR (+$165), GA (+$150), MT (+$596), ME (−$439), AZ (−$193).
  - These need checking against each state's 2026 form before any change. Some may be SumAtlas's error.

## 6. P2: other behaviour
- **Contradictory notice:** with a city or county picked (NYC, Montgomery, Philadelphia), the result shows the "City" line, yet the notice still says "State tax only: local income tax is not included, so your total is likely higher". By code, `pe(x, N)` uses `N = box && !locality`.
- **The NY "typical local" box adds 3.5% for every New York resident,** although only NYC and Yonkers residents pay it. In Compare with local on, all of NY is ranked as if it were NYC.
- **Two export bars:** "Copy report / Download CSV / Print or save as PDF" and "Copy result / Save as text / Print". The cap dialog for "Copy report" says "downloading needs a pass".
- **Compare rows** are clickable `<tr>`s with no tabindex or role, so keyboard users can't pick a state from the ranking.

## 7. Trial cost (owner policy: copying and results may count, so this is about wording only)
- **Page note:** "Reading results never uses a trial use. Copying, saving or printing uses 1 per visit."
- **Live, context with 10 left** (13:27 EST): the first action, **Download CSV**, cost 1 (10 → 9) and downloaded `state-tax-ca.csv`. Copy report, Print or save as PDF, Copy result, Save as text and Print then cost nothing more on the same visit. This is **consistent with the page note**.
- **Live, context at 0:** all six actions open the cap dialog. Compare all states and reading are free.
- **Wording mismatch (P1, wording fix, shared with #9):**
  - /terms says "Text utilities, calculators and simple converters take no trial use at all".
  - /faq says "tax calculators … never use a trial use".
  - Both disagree with the page note and the live behaviour. Under owner policy the charge is intended, so the fix is to the Terms and FAQ wording.
- **Starting state (display-only):** of 9 tracked fresh contexts (13:25–13:28 EST), 7 loaded at 0 remaining and 2 at 10. The 31 calculation cases ran in one of the 10-left contexts and used nothing (reading is free).
- **History:** "Recent calculations … Kept only while this page is open." There is no localStorage key for it (verified).

## 8. Keyboard and a11y
- The tab order runs State → Filing status → source link → Compare/Hide → table region → "How this was calculated" → exports → Clear → Copy result…
- There is no aria-live or role=status on the result.
- **axe on main** (MD, compare open): `scrollable-region-focusable` serious ×1 (`.max-h-96`, the compare table) and `heading-order` moderate ×1.
