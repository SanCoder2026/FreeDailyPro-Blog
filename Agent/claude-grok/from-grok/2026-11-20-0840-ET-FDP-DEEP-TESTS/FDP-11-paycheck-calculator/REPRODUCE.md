Sent: 2026-11-20 08:40 ET

# Reproduce: paycheck-calculator

Guest browser, https://www.freedailypro.com/tool/paycheck-calculator. Reading results costs nothing. Scripted: `node scripts/pc-live.js <ids>`.

- **R1 (401(k) limit):** Salary 200000, State Texas, 401(k) % 30 → 401(k) box $60,000, federal $22,334, no message. Expected a limit message ($24,500). `pc-live.js P11_401k_30pct_200k`
- **R2 (negative net):** Salary 75000, Texas, 401(k) 150 → net −$220.67 (−$5,738 a year). Then State "Custom rate…", rate 150, 401(k) 0 → net −$1,957.98. `P12_401k_150pct,P17_custom_150pct`
- **R3 (shared engine):** California, 85000, Single → state $3,660; switch to Head of household → still $3,660. Utah, 75000 → $2,621 (TC-40: ≈ $3,103). `P06_CA_85k,P07_CA_hoh_85k,P10_UT_75k`
- **R4 (wording):** read the note under the result ("Copying, saving or printing uses 1 per visit"), then /terms ("calculators … take no trial use at all") and /faq ("… never use a trial use").
- **R5 (state pre-tax rules):** Pennsylvania, 85000, 401(k) 10 → $2,349 (expected $2,609.50). California, 85000, HSA 4400 → $3,251 (expected $3,660). `P09_PA_85k_401k10,P15_CA_hsa_4400`
- **R6 (limits/validation):** HSA 50000 accepted; Hourly tab, hours 200 accepted; 401(k) "abc" → treated as 0, no message. `P13_hsa_50000,P26_hourly_25x200,P21_401k_abc`
- **R7 (default state):** fresh load → State "Custom rate…", rate 0, State tax (yr) $0. `P01_default`
- **R8 (blog):** /blog/paycheck-calculator CA paragraph vs California 90000 single bi-weekly → $2,571.15, state $4,125, CA SDI $1,170. `pc-live.js B02_CA_90k x.json`
- **R9 (video):** play the embedded video at 0:40–0:52 (3-field UI, $750,000 → $19,236.18); live Custom 0%, 750000 → $19,047.53. `pc-live.js V01_video_750k_custom0 x.json`
- **Gate:** at 0 remaining, click Copy result / Save as text / Print → cap dialog (stop there; don't enter an email or card). With uses left: pending (RERUN row 11).
