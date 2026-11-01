Sent: 2026-11-01 09:10 AM ET

# Paycheck calculator mobile fixes 1-6, and Monthly shown beside the Day Pass everywhere (owner approved)

**Intent:** On a phone, the paycheck result should be visible without scrolling and the page easy to tap. Every upsell should show the monthly plan, not only the $1 day pass.

**Why:** Santosh, Nov 1 9:08 AM ET: "Approved everything. But also show monthly plan apart from daily pass". The take-home result starts at 807px on a 375px phone, below the fold. Text fields are 36px and the Salary/Hourly tabs are 29px. Exact CSS and markup are in /workspace/web-design/paycheck-mobile/paycheck-mobile-fix-list.md.

**Outcome (paycheck calculator):**
1. The result is above the fold. Fold the two Quick Buy rows into the trial line, and put 401k/Health/HSA in a <details> that's closed by default.
2. Every field and button is at least 44px tall, and inputs are 48px.
3. The shared-header 2px overflow is fixed (already in the 0906 pricing brief).
4. The 401k/Health/HSA fields stack on mobile.
5. The disclaimer is 13-14px, with a one-line summary and the rest collapsed.
6. The duplicate Discover-more row and the duplicate share control are removed.

**Outcome (site-wide upsell):** Wherever an upsell or paywall shows the Day Pass, it also shows the Monthly plan beside it at the real price. Professional Tools show "$1 day pass · $4.99/mo"; Premium Applications show "$3 day pass · $9.99/mo". Use "trial uses" wording and never "free tools". Report the list of components you changed.

Source: owner
