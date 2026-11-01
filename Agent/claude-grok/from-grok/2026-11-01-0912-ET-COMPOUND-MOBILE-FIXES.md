Sent: 2026-11-01 09:12 AM ET

# Compound interest calculator mobile fixes 1-7 (owner approved: "Approved everything", 9:10 AM ET)

**Intent:** On a phone, the Final Balance should be visible right away, the page easy to use, and the calculator as clear as NerdWallet's or Calculator.net's.

**Why:** Web Design audit. Exact CSS and markup are in /workspace/web-design/compound-mobile/compound-mobile-fix-list.md. Final Balance is at 931px and should be at about 747px or better.

**Outcome:**
1. Final Balance is above the fold. Replace the two Quick Buy rows with one ads-free link that shows Monthly beside the Day Pass (0910 rule). Put Inflation, Contributions made and Start date under a "More options" toggle, and pair Years with Compounded on one row.
2. Hide the floating back/home stack on mobile with max-sm:hidden (same as the 0911 brief), and move Feedback to the bottom-left.
3. All controls are at least 44px tall, and inputs are 48px.
4. The shared-header overflow is already in the 0906 brief.
5. /tool/compound-interest-calculator gets a 301 to /tool/compound-interest, and the 404 page drops its translated dead links.
6. 12px notes and the table go to 14px, and the three Discover-more rows become one.
7. Add a mobile-friendly stacked bar chart of contributions vs interest by year.

Source: owner
