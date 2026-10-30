Sent: 2026-10-30 14:47 ET

# B-0273 Badge and Pass Maker: sample flow works end to end; add CSV field merge, role colours and a door count; shorten the title
Priority: P3 · Estimated effort: M · Report: #149 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:44–14:47 ET. L-243: next 3 untested tools alphabetically after avatar-builder. No GA/GSC rows for these pages in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An organiser should go from guest list to printed badges with QR passes to a fast door check, without retyping names.
## Why (1280 px; 0 trial uses)
- "Trial: 2 uses/day", $3 / $9.99. Three steps share one list: Guests → Badges and passes → Door check.
- Try a sample: 8 guests (5 confirmed, 1 invited, 1 waitlist, 1 declined; 4 need a room; 4 diet notes).
- Step 2: who gets a badge (confirmed + attended / all except declined / everyone), sheet presets Avery 5392 (6 per Letter sheet, 4×3 in) and L7165 (8 per A4) or "My own grid", event name, band colour, text position, walk-in blanks, start-at badge, QR on/off, outlines. Preview: "5 badges, 1 sheet". "Print at 100%" note ✔. **Make badges PDF** opens the trial-uses dialog (owner's decision).
- Step 3: camera scanner or image upload; works offline.
- The pass-key warning on Save project is clear; see the #147 addendum about the plain-text key (optional passphrase gap applies here too).
- **Missing vs competitors (~14:46 ET):** place any CSV column on the badge (company, role, pronouns) (ClearEvent, Hi.Events); colour band by role or ticket type (Hi.Events, CardDeck, Guidebook); front and back badges (ClearEvent, Guidebook); live arrival count on the door step (Hi.Events check-in, CardDeck); Avery 74459 and A6/4×6 sizes (ClearEvent, Hi.Events).
- No overflow at 390 px. Ad text "Compare Browsers" stuck to copy → L-004. /es English title → **B-0123**.
## Who uses this
Conference, meetup and wedding organisers running their own door.
## Outcomes (ranked)
1. Choose which guest fields print (organisation, role).
2. Band colour by role/status.
3. Door step shows "checked in X of Y".
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD. **Title 64 chars** ("Badge and Pass Maker - Event Badges and QR Passes | FreeDailyPro"). **Meta 122.** H1 "Badge and Pass Maker".
- **Keywords:** "event badge maker", "name badge template avery 5392", "qr code check in badges", "printable name badges".
- **Suggested:**
  - Title: `Badge and Pass Maker – Name Badges with QR | FreeDailyPro` (57)
  - Meta: `Print event name badges with a QR pass on each, on Avery 5392 or L7165 sheets or your own grid, then check guests in at the door by scanning, even offline.` (155)
  - H1: `Event Name Badges with QR Check-In`
  - FAQ: "Which badge sheets does it fit?" · "Does the door check work offline?" · "Who can make valid passes?"
## Constraints
Keep downloads within the trial-uses rule.
## Test cases
1. Try a sample → "Confirmed and attended" preview shows 5 badges, 1 sheet.
2. Admin: badges PDF at 100% matches Avery 5392; QR scans in Door check.
3. Title ≤ 60; meta 140–160.
