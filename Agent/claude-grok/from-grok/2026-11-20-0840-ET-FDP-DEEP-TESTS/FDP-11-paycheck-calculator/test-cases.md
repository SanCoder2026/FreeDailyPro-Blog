Sent: 2026-11-20 08:40 ET

# Test cases: paycheck-calculator (PC-)

Run on https://www.freedailypro.com/tool/paycheck-calculator, guest. Default inputs unless stated: $75,000 salary, single, bi-weekly, 401(k) 0, health 0, HSA 0. "Live" = 2026-11-19 13:39–13:47 EST. Expected = 2026 IRS/SSA rules or the state's own rules.

| ID | Input | Expected | Live (before fix) | Status |
|---|---|---|---|---|
| PC-01 | TX, $75k | Net $2,368.94; fed $7,670; SS $4,650; Med $1,088 | Same | PASS |
| PC-02 | TX, $150k MFJ | Fed $15,340 | Same | PASS |
| PC-03 | TX, $60k HoH | Fed $3,948 | Same | PASS |
| PC-04 | TX, $250k | SS capped $11,439; Med $4,075 (incl. 0.9% over $200k); fed $51,304 | Same | PASS |
| PC-05 | TX, $400k MFS | Med $8,275 (0.9% over $125k); fed $103,134 | Same | PASS |
| PC-06 | TX, health $200/check | SS $4,328, Med $1,012, fed $6,526 | Same | PASS |
| PC-07 | Hourly $25 × 50 h | Gross $71,500/yr ($2,750/check) | Same | PASS |
| PC-08 | Salary "abc", "85k", "-5" | Error, no result | Errors shown | PASS |
| PC-09 | TX, $200k, 401(k) 30% | Warning: above the 2026 limit of $24,500 (catch-up by age) | $60,000 deducted, no warning | FAIL (P1) |
| PC-10 | TX, 401(k) 150% | Error | 401(k) $75,000, net −$220.67 | FAIL (P1) |
| PC-11 | Custom state 150% | Error (e.g. max 15%) | State $112,500, net −$1,957.98 | FAIL (P1) |
| PC-12 | Any input making net < 0 | Message, never a silent negative take-home | Negative shown silently | FAIL (P1) |
| PC-13 | CA, $85k, HoH | CA HoH deduction/brackets (lower than single $3,660) | $3,660 | FAIL (P1, shared) |
| PC-14 | UT, $75k | ≈ $3,103 (taxpayer credit) | $2,621 | FAIL (P1, shared) |
| PC-15 | PA, $85k, 401(k) 10% | PA $2,609.50 (401(k) taxed by PA) | $2,349 | FAIL (P2) |
| PC-16 | CA, $85k, HSA $4,400 | CA tax stays $3,660 (no CA HSA deduction) | $3,251 | FAIL (P2) |
| PC-17 | HSA/FSA $50,000 | Warning above 2026 limits | Accepted | FAIL (P2) |
| PC-18 | 401(k) "abc" | Error like the salary field | Silently 0 | FAIL (P2) |
| PC-19 | Hours 200/week | Error (max 168) | Accepted | FAIL (P2) |
| PC-20 | First load | State prompt or visitor state, not Custom 0% | Custom rate… 0% | FAIL (P2) |
| PC-21 | NY / NJ / WA $85k | Payroll programs deducted or reused from #10 | Not deducted (disclosed) | PARTIAL (P2) |
| PC-22 | Blog CA $90k | Blog = live | Blog $2,606.28 vs live $2,571.15 | FAIL (P2) |
| PC-23 | At 0 remaining: Copy result / Save as text / Print | Cap dialog, no export | Cap dialog for all three | PASS |
| PC-24 | With uses left: first export, then the other two | 1 use for the visit, later free (page note) | Not observed (all contexts at 0) | RERUN |
| PC-25 | /terms and /faq trial wording | Matches the page note | Says calculators take no trial use | FAIL (P1 wording) |
| PC-26 | axe on main (Salary, Hourly) | 0 critical | aria-valid-attr-value on tab trigger (aria-controls to a missing panel) | FAIL (P2) |
| PC-27 | Result region | Announced (aria-live/role=status) when inputs change | None | FAIL (P2) |
| PC-28 | Meta description / FAQ count | Mentions state tax, 401(k), hourly; 4+ FAQs | Federal + FICA only; 1 FAQ | FAIL (P2) |
| PC-29 | Video | Current UI and figures | Old 3-field UI; $19,236.18 vs $19,047.53 | FAIL (P2) |
