Sent: 2026-11-20 08:40 ET

# Priorities: paycheck-calculator

No P0. Repro steps are in REPRODUCE.md (R-ids).

## P1

1. **401(k) has no annual-limit check (R1).** $200k at 30% deducts $60,000 (limit $24,500) with no warning, and federal tax falls with it. The check already exists in the shared `calcChecks` module (export `p`, "IRS Notice 2025-67") but this tool doesn't import it. Add an age group select like the 401(k) tool.
2. **Silent negative take-home (R2).** 401(k) 150% → −$220.67 per check; Custom state 150% → −$1,957.98. Validate 401(k) 0–100% (and the dollar limit), state rate 0–15%, and show a message whenever deductions exceed pay.
3. **Shared state engine (R3, also #9/#10).** HoH uses the single deduction and brackets (CA HoH $85k = $3,660); Utah deducts a standard deduction instead of applying the taxpayer credit ($2,621 vs ≈ $3,103 at $75k). One fix in stateTaxData `s()` covers all three tools.
4. **Trial-use wording (R4, shared).** The page note says copying, saving or printing uses 1 per visit (intended, owner policy). /terms and /faq say calculators take no trial use. Fix the Terms/FAQ wording; don't change the gate.

## P2

- State-specific pre-tax rules (R5): PA taxes 401(k) deferrals ($2,349 vs $2,609.50); CA/NJ don't allow the HSA deduction (CA $3,251 vs $3,660).
- HSA/FSA has no limit ($50,000 accepted); hours accept 200/week; 401(k) "abc" silently becomes 0 (R6).
- Default state is "Custom rate…" at 0%, so the first result shows no state tax (R7). Prompt for a state or use the visitor's.
- Reuse #10's payroll programs (NY PFL/DBL, NJ TDI/FLI, WA PFML/Cares, MA, RI, HI) and local taxes so both tools agree.
- Blog CA paragraph stale ($2,606.28 vs $2,571.15; no SDI) (R8).
- Video jNpP2-R9-eM: old 3-field UI, $19,236.18 vs $19,047.53 at $750k, "free" wording, an internal sheet name and bookmarks visible (R9). Re-record in a clean profile.
- SEO: meta omits state/401(k)/hourly; title "Online"; H1 has no scope; FAQPage has 1 question; Offer has no billing period; 8 hreflang locales are untranslated English copies (es is translated).
- A11y: axe critical `aria-valid-attr-value` on the Salary/Hourly tab triggers (aria-controls points to a missing panel); no aria-live on the result.
- Cap dialog heading differs by action ("Today's trial uses are done" vs "You've used today's trial uses").

## Not a defect

- Copy/Save/Print charging 1 use per visit (owner policy).
- Ads: keep them in reserved slots below the tool; never between inputs and result.
