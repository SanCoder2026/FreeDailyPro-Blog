Sent: 2026-10-30 15:45 ET

# B-0305 Business Days Calculator: US-only holidays, title without brand
Priority: P3 · Estimated effort: M · Report: QA-REPORT-159 · Source: live probe 2026-10-30 ~15:42-15:44 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Anyone, in any country, gets a deadline that skips their public holidays.

## Why
No GSC row in the analytics raw file for this page (calculator queries are tracked in testing-guidance 2026-10-30-apyhub-feedback-and-calculator-queries.md).
Checked live (15:43 ET): 2026-12-21 → 2027-01-04, Sat/Sun weekend, end not counted → 10 working days, 4 weekend days ✔. After "Add US federal holidays" (22 listed) → 8 working days, 2 holidays skipped (Dec 25, Jan 1) ✔. Add mode: today + 10 working days → Wednesday, January 6, 2027 ✔ (Dec 25 and Jan 1 skipped). Date inputs named "Start date"/"End date" ✔. Four weekend choices ✔.
Checked live: the only holiday preset is "Add US federal holidays"; other countries need typing dates by hand. The URL stays the same after changes (checked), so a result can't be shared by link.
Competitors (live search): timeanddate (200+ countries/regions), OpenWorkdays (246 countries), BizDays Global (170+), businessdaycalculator.org (25 countries, Net 30/60/90 deadlines).
Title 52 without "| FreeDailyPro"; meta 150 has "Free". /es title English → L-189. Ad text ("Learn Math", "Shop Holiday Decor" after the holiday count) → L-004.

## Who uses this
Office staff, HR, logistics and anyone working out a deadline.

## Outcomes (ranked)
1. Holiday presets for more countries (at least UK, Canada, Australia, India, Germany, France).
2. Snippet with brand as below.
3. Net 30/60/90 shortcut; shareable URL.

## SEO
- Now: title "Business Days Calculator - Count or Add Working Days" (52, no brand); meta 150 (has Free); H1 "Business Days Calculator"
- Keywords: business days calculator, working days calculator, add business days, business days between dates
- Suggested Title: "Business Days Calculator: Count or Add Days | FreeDailyPro" (58)
- Suggested Meta: "Count working days between two dates or add working days to find a deadline. Choose the weekend, add US federal holidays or your own, and copy the result." (154)
- Suggested H1: keep
- FAQ: Is the start date counted? · Which holidays are included? · Can I use a Friday–Saturday weekend? · How do I subtract business days?

## Constraints
Keep the custom holiday box and weekend options.

## Test cases
1. Dec 21 2026 → Jan 4 2027 with US holidays → 8 (regression).
2. UK preset 2026 → Dec 25, Dec 28 (Boxing Day substitute) skipped.
3. Add −5 working days from 2027-01-06 → 2026-12-29 with US holidays.
4. Title ≤60 with brand, meta 140–160; 390 px no overflow.
