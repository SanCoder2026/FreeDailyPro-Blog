Sent: 2026-10-31 00:23 ET

# B-0313 College Cost Calculator: letters in a field print $NaN; no school comparison, loan gap or monthly payment
Priority: P2 · Estimated effort: M · Report: QA-REPORT-171 · Source: live probe 2026-10-31 ~00:17-00:23 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A family sees what college will really cost them over all the years, compares the schools they are choosing between, and knows how much they would have to borrow and repay.

## Why
No GSC row for this page in the analytics raw files (checked 2026-10-29 and July-to-now files).
Checked live: defaults (11,000 + 12,000 + 1,200 + 1,500 + 2,000, 4 years, 4%) give Year 1 $27,700, Year 2 $28,808, Year 3 $29,960, Year 4 $31,159, total $117,627 ✔ (hand-checked). 10 years ✔, −5% increase ✔, start date labels years "Aug 2027 to Jul 2028" ✔, Years 0 → "Fix the number of years to see the total." ✔.
Bug: typing "abc" in Tuition shows "$NaN" for the total and every year (no message). The fields are text inputs, so letters get in.
Aid larger than cost (30,000 aid) shows Year 1–3 as $0 and the total $1,159 with no note that aid exceeds cost; "over 1 years" grammar on 1 year.
Tuition and Scholarships/Aid inputs have no accessible name (checked) → B-0155. Results area has Copy / Save as text / Print, no done state → B-0187.
Capability (checked on the page controls): one school only; no loan gap, interest or monthly repayment; no family contribution or work-study line; no per-category increase.
Competitors (live search): StudentAidEstimator (several schools side by side, in-school loan interest, debt at graduation, monthly payment, local storage + JSON export); DegreeCalc (cost, ROI, loan payment, FAFSA SAI, compare 2–3 schools); College Board BigFuture and collegecost.ed.gov (official net price calculators by school); AdmitCost (net price by income band for 110 schools).
FDP already has /tool/student-loan-repayment-calculator and /tool/college-529-calculator linked under "More from"; they are not connected to this result.

## Who uses this
Parents and students choosing between colleges, and school counsellors.

## Outcomes (ranked, demand × effort)
1. Number inputs that reject letters, with a clear message instead of $NaN (S).
2. "Compare schools": add 2–4 schools side by side with the same years and increase (M).
3. Funding gap and loans: family contribution, work-study, loan rate (default to the current federal undergrad rate, labelled with its year) and term → debt at graduation and monthly payment; or hand the gap to the Student Loan Repayment Calculator prefilled (M).
4. Note when aid exceeds cost in a year, and "1 year" singular (S).
5. Link to the school's official net price calculator (collegecost.ed.gov) in the result note (S).

## SEO
- Now: title "College Cost Calculator - Net Cost by Year | FreeDailyPro" (57); meta 142 with "Free"; H1 "College Cost Calculator"; JSON-LD SoftwareApplication, FAQPage (3 Q), BreadcrumbList, VideoObject ✔; canonical ✔; 11 hreflang; /es page language not checked this run
- Keywords: college cost calculator, cost of college calculator, 4 year college cost, net price calculator, college tuition calculator
- Suggested Title: "College Cost Calculator: 4-Year Net Price | FreeDailyPro" (56)
- Suggested Meta: "Estimate college cost year by year: tuition, housing, books and fees with yearly increases, minus scholarships. See the 4-year net total." (137)
- Suggested H1: keep
- FAQ: keep; add: How much will I need to borrow? · How do I compare two colleges?

## Constraints
Reading results never uses a trial use (page says so); keep that. Copy/Save/Print count against the trial (owner rule).

## Test cases
1. Tuition "abc" → field rejects it or shows "Enter a number"; no $NaN anywhere.
2. Defaults → $117,627 over 4 years, years as above.
3. Aid 30,000 → note that aid exceeds cost in Years 1–3.
4. Two schools → side-by-side totals.
5. Gap $20,000/year, 6.5%, 10 years → debt at graduation and monthly payment shown.
