Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-11 paycheck-calculator (re-run after the trial reset)

**Supersedes:** `FDP-11-paycheck-calculator-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-11-paycheck-calculator-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 11 result: COST DONE; export content for 401(k)/section 125 still pending (2026-11-20 22:26–22:33 EST)

`pc-gate.js` (22:26): context 0 loaded at 10; context 2 loaded at 0.

| Check | Result |
|---|---|
| First export with uses left | **Copy result 0 → 1**; then Save as text (`paycheck-calculator-result.txt`) and Print were **free** on the same visit. 1 per visit, as the page note says ("Copying, saving or printing uses 1 per visit"). PASS under the policy. |
| At 0 | All three open the cap dialog (re-confirmed). |
| .txt content (default inputs) | Has take-home, gross, Federal, State, Social Security, Medicare, the CA SDI disclaimer note, the per-visit note and "Calculated with FreeDailyPro.com". With default inputs (no state tax, 401(k) 0, health 0) there are no SDI, 401(k) or section 125 lines to show. |
| .txt with CA + 401(k) 6% + health $150 | On screen: state $2,855, SDI $1,105, 401(k) $5,100, section 125 $3,900 (`content-1120.json`). **Save was blocked:** 2 extra fresh contexts (22:33 EST) loaded at 0. Whether the export includes these lines is **still pending**. 4 of the row's 6 contexts used. |
