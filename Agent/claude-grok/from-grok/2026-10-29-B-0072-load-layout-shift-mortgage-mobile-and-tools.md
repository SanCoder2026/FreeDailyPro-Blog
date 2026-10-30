# B-0072 Load layout shift: Mortgage (mobile) and /tools (desktop)
Priority: P2      Estimated effort: 30–60 min      Report: #78, #80      Source: Testing Bot      Related: B-0041

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Pages should hold still while they load, so visitors on a phone don't lose their place or tap an ad by accident.

## Why
- /tool/mortgage-calculator at 390 px, no input, 23:30 ET: load CLS 0.32 and 0.48 (2 of 2). Shifts come from the `mg-first-payment` results block and a `google-auto-placed` ad inserted in the content column (≈0.21). Desktop is 0.04.
- /tools at 1280 px: CLS 0.28–0.37 in 3 of 5 loads; the tool-chip row (`flex items-center gap-1 sm:gap-3`) shifts at about 430 ms. Mobile is 0.001.
- /tools has 166 views (GA, row 8); calculators rank on high-impression queries. Google treats CLS > 0.1 as poor.

## Outcomes
Load CLS < 0.1 on both pages at both widths, in repeated loads, with ads still showing.

## Constraints
Don't remove ads or change their count; reserve space, or keep auto-placed ads out of the calculator column. No change to the trial-use logic.

## Test cases
Load each page 5× at 390 and 1280 with a PerformanceObserver: every run < 0.1; no ad overlaps the inputs/results.
