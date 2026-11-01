Sent: 2026-11-01 09:06 AM ET

# /pricing mobile fixes 1-3 (owner approved, Nov 1 9:05 AM ET)

**Intent:** On a phone, /pricing should be easy to tap and should never scroll sideways.

**Why:** Web Design's audit (/workspace/web-design/pricing-mobile/fix-ranking.md). The buttons are 36px, below the 44px minimum. At 375px there's a 2px sideways scroll, and it comes from the shared header, so it also affects the paycheck, mortgage and compound pages. The intro line doesn't mention Book.

**Outcome:**
1. Pricing-card buttons (Buy Day Pass, Subscribe Monthly, Start 7-day trial, See..., Buy N seats) are w-full and min-h-11 (44px) on mobile, replacing h-9. Leave the toggle buttons alone.
2. The header wrapper (div.flex.items-center.gap-1.sm:gap-3) uses max-sm:gap-0 (or gap-0.5), the logo link gets min-w-0 and shrink, and add html,body{overflow-x:clip} as a safety net. At 375px, scrollWidth must equal 375 on /pricing and on the paycheck, mortgage and compound-interest pages.
3. Copy: add Book to the intro line that says what starts at $29.99, and label the $3.99-per-seat block "Team seats".

NOT approved, so don't do them: P2, P4, P6a/c, and the $2,394 vs $2,395 typo.

Source: owner
