Sent: 2026-11-01 09:11 AM ET

# Mortgage calculator mobile fixes 1-5 (owner approved: "Approved everything", 9:10 AM ET)

**Intent:** The mortgage calculator should be easy to tap on a phone, and nothing should cover the results.

**Why:** Web Design audit. Exact CSS and Tailwind are in /workspace/web-design/mortgage-mobile/mortgage-mobile-fix-list.md. QA-393 shows the floating back/home stack covering the result card.

**Outcome:**
1. Add max-sm:hidden to the floating back/home stack and keep Feedback. This is a shared component, so check it on every tool page.
2. Inputs and selects are at least 48px; buttons, links and the checkbox row are at least 44px.
3. The shared-header overflow is already in the 0906 brief.
4. Keep one Quick Buy row (folded into the trial line), one export row and one "standard rates" line, and remove the repeats.
5. The note and disclaimer go from 12px to 14px.
The site-wide rule from the 0910 brief, Monthly beside the Day Pass, applies here too. NOT approved: any change to the pinned "Try Cloud Tools" banner.

Source: owner
