Sent: 2026-11-20 08:40 ET

# Live functional findings: paycheck-calculator

- **Run:** 2026-11-19 13:39–13:44 EST (box `date`, ET), headless Chromium 1366×900, guest, `scripts/pc-live.js`.
- **Files:** `json/cases.json` (P01–P30), `json/blog-cases.json` (B01–B08), `json/video-case.json` (V01).
- **Reference:** federal tax and FICA were recomputed with an independent 2026 script (`ref_federal.py`, carried over from #9: 2026 brackets, standard deduction $16,100 / $32,200 / $24,150 HoH, SS 6.2% to $184,500, Medicare 1.45% + 0.9% over $200k / $250k / $125k).
- Reading results never changed `fdp-usage-v1` (display-only evidence).

## Federal and FICA: exact

All 30 cases match the reference to the dollar: P02 $7,670, P03 MFJ $15,340, P04 HoH $3,948, P05 $51,304 (SS capped at $11,439, Additional Medicare included), P11 $22,334, P13 $890, P14 $6,526, P15 $8,902, P24 $4,060, P26 $90,534, P28 MFS $400k $103,134 (Additional Medicare from $125k), V01 $750k $227,500. Section 125 (health premium, HSA/FSA) correctly reduces SS and Medicare (P14 SS $4,328 = $69,800 × 6.2%); 401(k) correctly does not. Hourly: 40 h at rate + 1.5× over 40, × 52 (P25 $71,500 gross). Pay frequency divides the same annual net (P22/P23).

## Defects

| ID | Case | Live | Expected | Severity |
|---|---|---|---|---|
| F1 | P11: $200,000, 401(k) 30% | 401(k) $60,000 deducted, no warning; federal tax drops to $22,334 | 2026 employee limit is $24,500 (+$8,000 catch-up 50+). The shared module `calcChecks-BMsAp5Al.js` already has this check (export `p`: "Pre-tax contributions are above the 2026 employee 401(k) limit of $24,500 (IRS Notice 2025-67)…"), but PaycheckCalculator imports only the number check (`import { a as k }`, pc.pretty.js line 20). Take-home is understated by ~$27k/yr of deferral that cannot legally happen | P1 |
| F2 | P12: 401(k) 150% | Capped at 100% ($75,000), net **−$220.67 per check / −$5,738 a year**, no error | Reject >100% or cap at the legal limit; never show a negative take-home without a message | P1 |
| F3 | P17: Custom state rate 150% | State tax $112,500, net **−$1,957.98 / −$50,908 a year**, no error | Validate 0–15% (or similar) | P1 (same fix as F2) |
| F4 | P07 CA HoH $85k | State $3,660 (= single, P06) | CA HoH uses Schedule Z and an $11,412 deduction, so lower. Shared engine bug, already reported in #10 | P1 (shared) |
| F5 | P10 UT $75k | State $2,621 | ≈ $3,103 (Utah taxpayer credit, not a deduction). Shared, see #10 | P1 (shared) |
| F6 | P09 PA $85k, 401(k) 10% | State $2,349 (401(k) deducted) | PA taxes 401(k) deferrals: 3.07% × $85,000 = $2,609.50 | P2 |
| F7 | P15 CA $85k, HSA $4,400 | State $3,251 (HSA deducted) | CA (and NJ) don't allow the HSA deduction, so CA should stay at $3,660 for HSA (premiums are fine) | P2 |
| F8 | P13: HSA/FSA $50,000 | Accepted, take-home $853.75/check | 2026 HSA limits $4,400 / $8,750; health FSA ~$3,400. Warn above limits | P2 |
| F9 | P21: 401(k) "abc" | Silently treated as 0 | Salary and hours show an error for text (P18, P19, P27); deduction fields should too | P2 |
| F10 | P26: 200 hours/week | Accepted ($255k a year from $25/h) | Max 168 h/week; warn above ~80 | P2 |
| F11 | P01 default | State is "Custom rate…" at 0%, so the first result has no state tax | Default to a state picker prompt (or the visitor's state); the blog itself lists "leaving the state on custom 0%" as a mistake | P2 |
| F12 | P08 NY, P29 NJ, P30 WA | NY PFL/SDI, NJ TDI/FLI, WA PFML/Cares not deducted (disclosed in the footer) | The State Tax Calculator (#10) already computes these 7 payroll programs; the paycheck tool could reuse them | P2 |

## Input validation that works

"abc", "85k" and "-5" in salary show "Enter an annual salary as a number." / "…of 0 or more. It cannot be negative." (role=alert). "abc" in hours shows "Enter hours per week as a number."

## Blog figures vs live (B01–B08)

All Texas figures in /blog/paycheck-calculator match to the cent ($2,774.81; $2,612.81; $2,669.28; $2,507.28; hourly $2,210.93 from $2,660.00; semi-monthly $3,006.04; monthly $6,012.08). **California is stale:** the blog says $2,606.28 per check and state tax ≈ $4,382 ($168.53 less than TX); live shows **$2,571.15**, state $4,125 **plus CA SDI $1,170** ($203.66 less than TX). P2.

## Trial gate (`json/gate.json`, `json/gate-run1.json`)

- **Starting counts (display-only):** the cases context (13:39:42 EST) loaded at usageToday 0 (10 remaining) and was still 0 after 30 read-only cases, so reading is free. At 13:40 and 13:41 EST, 12 fresh Chromium gate contexts, and later the blog (13:43), video (13:44) and kbd (13:42) contexts, all loaded at **10 of 10 used, 0 remaining**.
- At 0, Copy result, Save as text and Print all open the cap dialog ("Today's trial uses are done" for Copy/Save; "You've used today's trial uses" for Print: two wordings for the same state, P2 cosmetic). Screenshot `screens/live/gate-copy-at-zero.png`.
- **Not observed:** what the first export costs with uses left. Pending: RERUN-AFTER-RESET row #11.
- The page note says "Reading results never uses a trial use. Copying, saving or printing uses 1 per visit." /terms ("Text utilities, calculators and simple converters take no trial use at all") and /faq ("Text, calculator and converter tools … never use a trial use") say otherwise (re-checked live 13:44 EST). Per owner policy the charge is intended; **fix the Terms/FAQ wording** (P1, shared with #9/#10).
