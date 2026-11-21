Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-09 income-tax-calculator (re-run after the trial reset)

**Supersedes:** `FDP-09-income-tax-calculator-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-09-income-tax-calculator-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 9 result: DONE (2026-11-20 22:26 EST)

| Check | Result |
|---|---|
| IT-34: **Save as text** as the first action, uses left | **−1** (0 → 1); file `income-tax-calculator-result.txt` downloaded. A second Save on the same visit was **free** (stays 1). |
| IT-35: **Print** as the first action, uses left | **−1** (0 → 1, `window.print` stubbed). A second Print was **free** (stays 1). |

Together with Nov 19 (Copy result −1 first, repeats free): **1 trial use per visit for any export**, which matches the page note and the Oct 30 owner policy (copy/results count). The test-case "Expected: no use" wording for IT-34/35 is superseded: the policy-correct result is 1 per visit, and that is what happens.
