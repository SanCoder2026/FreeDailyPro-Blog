# B-0043 Addendum to B-0036: exact title, meta and FAQ rewrites + ranked missing-tool candidates

Priority: P1      Estimated effort: ~2.5 h (rewrites ~1.5 h; candidate list is read-only planning)

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
B-0036 asked for CTR lift on high-impression pages. This addendum gives the exact, data-backed copy for the first six pages, so the change can ship tonight instead of being drafted from scratch. Goal: turn positions 7–9 with ~0% CTR into real clicks, since search visitors are our most engaged traffic (56–67%) and drive ad revenue.

## Why / evidence
- Search Console Jul 10–Oct 29 2026: Roman Numeral Converter ~49K impressions at position 9 with 0.1% CTR; tax calculator 4.7K at pos 7.1 (0.1%); unit converter 4.4K at pos 7.1 (0%); tip calculator 5.7K at pos 7.0 (0 clicks); citation generator 2.4K at pos 8.6 (0%); BMI calculator online 504 at pos 6.8 (0%).
- Current titles lead with specs or brand, several are over 60 chars (truncated), and the citation meta is only 77 chars, so Google rewrites it.
- Prepared by the Programmatic SEO + Content Engine bot from live pages fetched Oct 29 ~9:50 PM ET.

## Outcomes / acceptance criteria
- Each of the six pages below ships the proposed **title, meta description, H1 and visible FAQ + matching FAQPage JSON-LD** (one JSON-LD block, not duplicated after hydration; see B-0052). Mirror Roman Numeral Converter on `/es/` in Spanish.
- **'free' rule:** "free" stays in the SEO title and meta description only. Never in H1, visible copy or FAQ answers. (Standing owner decision.)
- **Count wording**, wherever a site count appears: "300+ professional tools, premium applications and workflow products". No other count phrasing.
- **Items marked *verify*:** check the claim against the live tool before shipping (e.g. Roman step-by-step breakdown, tax take-home/effective rate and filing statuses, tip presets 15/18/20%, citation source types). If the tool doesn't do it, change the copy to match the tool. Don't build a feature just to match copy, and report each verify result.
- Titles ≤ 60 chars, metas ≤ 160 chars. Report before/after for each page, and live-check with view-source.
- Testing Bot verifies independently; GSC CTR is rechecked after 2–4 weeks.

## Ranked missing-tool candidates (planning only, do not build tonight)
GSC capture only covers the top ~100 queries, so this list is partial. Please send back a feasibility/effort estimate for each in your report:
1. **spell check** (408 impr, pos 6.8): partial, /tool/grammar-checker. Spell-check mode or landing page.
2. **barcode scanner online** (31, pos 8.8): missing; /tool/qr-scanner is QR only. Extend to 1D barcodes (camera + image, in-browser).
3. **mla format checker** (10, pos 5.9): partial. MLA preset on /tool/paper-format-checker.
4. **font match** (9, pos 21.8): missing. Font identifier from an image. **AI item: pending owner decision.** Don't build.
5. **pdf file recovery** (2): low priority.
- Tip calculator and cost of living comparison already exist as **plain calculators**. Treat them as snippet/ranking work (tip is in the rewrites below; cost of living sits at pos 77), not as new or AI tools.
- Any AI-powered item (font identifier, AI spell/grammar modes) is **pending the owner**. List it, don't implement it.
- Also from the data: "how to evaluate marketplace fees" ranks at pos 1.6 with 288 impressions and 0 clicks, so check that snippet. Word counter (2,320 impr, pos 9.1) and barcode generator (1,516, pos 5.5) are good next rewrite candidates.

## Not in scope / do not decide
New tools, AI features, pricing/trial changes, and URL or slug changes.

## Owner decisions needed
AI candidates (font identifier, AI spell mode). Nothing else.

---
# Appendix: exact rewrites per page (from the SEO bot)
## Roman Numeral Converter — `/tool/roman-numeral-converter`
**Target queries (GSC: clicks / impr / CTR / pos):** roman numeral converter 57 / 48,950 / 0.1% / 9.0; roman numerals converter 1 / 23 / 4.3% / 11.2; xxmxx roman numerals converter 3 / 11 / 27.3% / 4.4. Pages: /tool/roman-numeral-converter 50 / 38,580 / 0.1% / 9.5; /es/tool/roman-numeral-converter 11 / 9,585 / 0.1% / 8.2

| | Current (live) | Proposed |
|---|---|---|
| Title | Roman Numeral Converter - 1 to 3999, Both Ways, Free (52) | **Roman Numeral Converter: Numbers, Dates & Years Free** (52) |
| Meta | Convert any number from 1 to 3999 to a Roman numeral, or a Roman numeral back to a number. Instant, free, and dates can be written in numerals too. (147) | **Free Roman numeral converter: turn numbers 1–3999 or dates into Roman numerals and back, with step-by-step breakdown. Private, runs in your browser.** (148) |
| H1 | Roman Numeral Converter | **Roman Numeral Converter — Numbers, Years and Dates** |
| FAQ schema | 1 Q (large numbers / 5000) | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How do I convert a number to Roman numerals?** Type any whole number from 1 to 3,999 and the Roman numeral appears instantly, built from thousands, hundreds, tens and ones.
2. **How do I convert Roman numerals back to numbers?** Switch direction and type the numeral, for example MMXXVI. A smaller letter before a larger one is subtracted (IV, IX, XL, CM); otherwise letters are added. MMXXVI = 2026.
3. **How do I write a date or year in Roman numerals?** Use date mode and pick your order, such as Month.Day.Year (US). Each part is converted separately, so 7.4.1776 becomes VII.IV.MDCCLXXVI — popular for tattoos, weddings and anniversaries.
4. **Why does the converter stop at 3,999?** Standard numerals have no letter above M (1,000) and repeat a letter at most three times, so MMMCMXCIX (3,999) is the largest standard value. Larger numbers need a bar over letters, which is outside the standard set.
5. **What do I, V, X, L, C, D and M stand for?** I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 and M = 1,000.
6. **Is there a zero in Roman numerals?** No. The Roman system has no symbol for zero, so 0 and negative numbers cannot be converted.
7. **Is what I type sent anywhere?** No. The conversion runs entirely in your browser and nothing is uploaded.

**Rationale:** Pos ~9 but 0.1% CTR: the title leads with a spec ('1 to 3999') and 'dates' (high-intent tattoo/wedding use) is buried at the end of the meta. Proposed front-loads Numbers, Dates & Years; expands FAQ schema from 1 to 7 Qs for rich-result space. *Verify* a step-by-step breakdown exists in the UI — if not, replace with 'instant results'. Mirror on /es/ (9,585 impr). Also fix the mobile horizontal scroll on the date selector noted in the raw file.

## Income Tax Calculator — `/tool/income-tax-calculator`
**Target queries (GSC: clicks / impr / CTR / pos):** tax calculator 4 / 4,746 / 0.1% / 7.1; state income tax calculator 1 / 17 / 5.9% / 65.8. Page: /tool/income-tax-calculator 5 / 7,449 / 0.1% / 7.5

| | Current (live) | Proposed |
|---|---|---|
| Title | Income Tax Calculator 2026 - US Federal, State & FICA (53) | **Tax Calculator 2026: Free Federal + State Take-Home Pay** (55) |
| Meta | Estimate your 2026 US income tax: federal, FICA or self-employment tax and state tax, by filing status. Free tax calculator, runs in your browser. (146) | **Free 2026 tax calculator: estimate federal, state and FICA tax, take-home pay and effective rate by filing status. Private, runs in your browser.** (145) |
| H1 | Income Tax Calculator | **2026 Income Tax Calculator — Federal, State and FICA** |
| FAQ schema | 1 Q (is it exact?) | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How much tax will I pay in 2026?** Enter income, filing status and state. The calculator applies 2026 federal brackets and the standard deduction, adds Social Security and Medicare (FICA) and state tax, and shows total tax, take-home pay and effective rate.
2. **What is the difference between marginal and effective tax rate?** The marginal rate is the bracket your last dollar falls in. The effective rate is total tax divided by income, always lower because lower brackets are taxed at lower rates.
3. **Does it include state income tax?** Yes. Pick your state and its tax is added; states with no wage income tax show zero for that line.
4. **Can I use it if I am self-employed?** Yes. Choose self-employment and it calculates self-employment tax instead of employee FICA.
5. **Does filing status change the result?** Yes. Single, married filing jointly, married filing separately and head of household each have their own brackets and standard deduction.
6. **Is this exactly what I will owe?** It is an estimate based on standard rates and brackets and does not cover every deduction or credit. Confirm with a tax professional or the official forms before filing.
7. **Is my income data saved or uploaded?** No. Every number stays in your browser and is never sent to a server.

**Rationale:** Generic head term 'tax calculator' at pos 7.1, 0.1% CTR. Searchers want a take-home/owed answer; current title doesn't start with the exact query and never says 'take-home pay'. *Verify* the take-home and effective-rate outputs and the filing-status list in the UI. Add internal links to sales-tax, state-tax, UK and India calculators to catch non-US 'tax calculator' searchers.

## Unit Converter — `/tool/unit-converter`
**Target queries (GSC: clicks / impr / CTR / pos):** unit converter 2 / 4,424 / 0% / 7.1. Page: /tool/unit-converter 2 / 4,782 / 0% / 7.4

| | Current (live) | Proposed |
|---|---|---|
| Title | Unit Converter - Length, Weight, Temperature & More, Free (57) | **Unit Converter: Free Metric & Imperial, All Units at Once** (57) |
| Meta | Convert length, weight, temperature, volume, area, speed, time, data, pressure, energy and fuel economy instantly. Free unit converter, metric, US and UK. (154) | **Free unit converter for length, weight, temperature, volume, area, speed, data and more. See every unit at once, with exact metric, US and UK factors.** (150) |
| H1 | Unit Converter | **Unit Converter — Metric, US and UK Units** |
| FAQ schema | 6 Qs | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How do I convert between units?** Choose a category such as length or weight, enter a value and pick the from-unit. The result appears instantly, and the list below shows the value in every other unit of that category.
2. **How do I convert cm to inches or kg to pounds?** Pick Length or Weight, type the value and choose centimeters or kilograms. One inch is exactly 2.54 cm and one pound is exactly 0.45359237 kg.
3. **How does Fahrenheit to Celsius work?** Temperature uses a formula rather than a multiplier: °C = (°F − 32) × 5/9. The converter applies it for you.
4. **Why are there two kinds of gallon and ton?** The US gallon is 3.785411784 liters and the UK gallon is 4.54609 liters. A short ton is 2,000 pounds and a long ton is 2,240 pounds.
5. **What is the difference between a kilobyte and a kibibyte?** A kilobyte is 1,000 bytes and a kibibyte is 1,024 bytes; the same split applies at mega, giga and tera level.
6. **How accurate are the conversions?** Factors use exact definitions wherever they exist, such as 1 inch = 25.4 mm and 1 mile = 1,609.344 m.
7. **Is my data sent anywhere?** No. All conversions run in your browser.

**Rationale:** 0% CTR at pos 7 — Google's own converter widget answers most searches, so the snippet must sell a differentiator ('every unit at once', exact US/UK factors). Existing FAQ is good; add cm/in and kg/lb how-to Qs for long-tail intent.

## Tip Calculator — `/tool/tip-calculator`
**Target queries (GSC: clicks / impr / CTR / pos):** tip calculator 0 / 5,660 / 0% / 7.0 (page not in top-50 pages capture)

| | Current (live) | Proposed |
|---|---|---|
| Title | Tip Calculator - Split the Bill & Tip Per Person, Free (54) | **Tip Calculator: Free Bill Split & Tip Per Person** (48) |
| Meta | Work out the tip, the total bill and each person's share when you split the check. Choose a tip percentage or enter your own. Free tip calculator, no signup. (157) | **Free tip calculator: get the tip, total and each person's share in seconds. Pick 15%, 18%, 20% or any rate, tip before or after tax, round shares up.** (149) |
| H1 | Tip Calculator | **Tip Calculator — Split the Bill and Tip Per Person** |
| FAQ schema | 6 Qs | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How do I calculate a tip?** Enter the bill and choose a tip percentage; the tool shows the tip and new total. A 20% tip on $50 is $10, for a $60 total.
2. **How much should I tip at a restaurant?** In the US, 15% to 20% of the pre-tax bill is common for sit-down service, more for excellent service. Customs vary by country.
3. **How do I split the bill and tip between people?** Enter the number of people and each share of bill plus tip is shown. Leftover cents are spread so the shares add up exactly to the total.
4. **Should the tip be calculated before or after tax?** Customs differ, so you can choose. In the US the tip usually starts on the pre-tax amount.
5. **What does rounding each share up do?** Each share is raised to the next whole unit of the currency and the extra goes to the tip.
6. **Can I use a currency other than dollars?** Yes. The currency selector sets the symbol, decimals and rounding unit; yen, for example, has no decimals.
7. **Is anything I enter saved?** No. The calculation runs in your browser and nothing is stored or sent.

**Rationale:** 5,660 impr at pos 7, zero clicks. Current snippet is generic; proposed meta shows concrete percentages searchers scan for plus before/after-tax and round-up features the tool already has. *Verify* preset buttons are 15/18/20% — change to the actual presets if not.

## Citation Generator — `/tool/citation-generator`
**Target queries (GSC: clicks / impr / CTR / pos):** citation generator 0 / 2,448 / 0% / 8.6; mla format checker 1 / 10 / 10% / 5.9 (adjacent)

| | Current (live) | Proposed |
|---|---|---|
| Title | Citation Generator Online - APA, MLA, Chicago | FreeDailyPro (60) | **Citation Generator: Free APA 7, MLA 9, Chicago, Harvard** (55) |
| Meta | Generate APA, MLA, Chicago, or Harvard citations, and build a reference list. (77) | **Free citation generator for APA 7, MLA 9, Chicago and Harvard. Format books, journals and websites, then copy a sorted reference list. No signup needed.** (152) |
| H1 | Citation Generator | **Citation Generator — APA, MLA, Chicago and Harvard** |
| FAQ schema | 6 Qs | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How do I create a citation?** Pick a style (APA, MLA, Chicago or Harvard), choose the source type and fill in author, title, year and other fields. The formatted citation appears as you type and can be copied or added to your reference list.
2. **Which citation styles are supported?** APA 7th edition, MLA 9th edition, Chicago 17th edition (Notes-Bibliography, bibliography entry) and Harvard.
3. **What if there is no author or no year?** Leave the author empty and the title moves to the front; a blank year prints n.d. where the style calls for it.
4. **Does it look up a source from a URL or DOI?** No. It never visits the address — every field is typed by you, so you control each detail and your research stays private.
5. **In what order does the reference list appear?** Alphabetical by the first word of each entry: the author's last name, or the title when there is no author.
6. **Can I submit the result without checking it?** Check each citation against your course's or publisher's style guide; the tool handles formatting, but the details you enter must be correct.
7. **Is my reference list stored online?** No. Everything stays in your browser.

**Rationale:** Live meta is only 77 chars, so Google rewrites it; title spends 14 chars on the brand. Proposed adds edition numbers (APA 7 / MLA 9) students search for. *Verify* source types (books/journals/websites) against the live form. Cross-link to /tool/paper-format-checker for 'mla format checker'.

## BMI Calculator — `/tool/bmi-calculator`
**Target queries (GSC: clicks / impr / CTR / pos):** bmi calculator online 0 / 504 / 0% / 6.8; body fat calculator 1 / 203 / 0.5% / 19.6 (separate tool); /es/tool/body-fat-calculator 2 / 103 / 1.9% / 46.3

| | Current (live) | Proposed |
|---|---|---|
| Title | BMI Calculator Online - Metric & Imperial, Free | FreeDailyPro (62) | **BMI Calculator: Free Metric & Imperial + Healthy Weight** (55) |
| Meta | Calculate your Body Mass Index (BMI) online in metric or imperial units. Free BMI calculator, instant result, nothing is saved. (127) | **Free BMI calculator for adults: enter height and weight in kg/cm or lb/ft to get your BMI, category and healthy weight range for your height. Private.** (150) |
| H1 | BMI Calculator | **BMI Calculator — Body Mass Index and Healthy Weight Range** |
| FAQ schema | 6 Qs | 7 Qs below |

**Proposed FAQ (visible + FAQPage JSON-LD):**
1. **How do I calculate my BMI?** Enter height and weight in metric (cm, kg) or imperial (ft, in, lb). BMI is weight in kilograms divided by height in meters squared.
2. **What is a healthy BMI?** For adults, 18.5 up to 25 is Normal. Under 18.5 is Underweight, 25 up to 30 is Overweight and 30 or more is Obese.
3. **What is a healthy weight for my height?** The calculator shows the weights that give a BMI of 18.5 and 24.9 at your height.
4. **Is BMI accurate for athletes or older adults?** It can mislead: BMI cannot tell muscle from fat. A body fat estimate adds useful context.
5. **Why does it say my height or weight is out of range?** Heights from 100 to 250 cm and weights from 30 to 300 kg (or the same span in imperial) are accepted.
6. **Is BMI a complete measure of health?** No. It is a quick screening number, not a diagnosis — talk to a clinician about your health.
7. **Is my data saved?** No. Height and weight stay in your browser and are never stored or uploaded.

**Rationale:** Live title is 62 chars (truncates). 'Healthy weight range' is a real on-page feature and a top follow-up intent — surface it. Link FAQ Q4 to /tool/body-fat-calculator to pick up body fat calculator impressions.


Candidate data: `2026-10-29-B-0043-missing-tool-demand.csv` (same folder).

Source: owner
