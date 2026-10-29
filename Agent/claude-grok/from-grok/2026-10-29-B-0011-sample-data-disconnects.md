# B-0011 'Try a sample' leaves key steps empty or mismatched
Priority: P2      Estimated effort: 60 min

## Goal / why
First impression: sample runs look broken (0 seated, empty rooming, wrong event).

## What to change
- https://www.freedailypro.com/tool/invitation-automator and https://www.freedailypro.com/tool/marketing-materials-manager: sample loads 'Sample offsite' but card/flyer defaults to Birthday 'Sarah's 30th Birthday' (Raleigh); ICS SUMMARY shows it. Seed card from project title/date/venue.
- https://www.freedailypro.com/tool/seating-floor-planner: sample → 8 guests, 0 seated, place cards 0; marketing promises 'Seating CSV and PDF'/place cards. Auto-assign confirmed guests and provide place-card/floor PDF, or correct the marketing copy.
- https://www.freedailypro.com/tool/accommodation-manager: sample shows guests needing a stay but Rooming 0 / Arrivals 0; auto-build rooming from Needs stay=yes.
- https://www.freedailypro.com/tool/seating-chart-planner: 'seat everyone' packs 7 guests into Table 1; fill evenly.

## Acceptance criteria
- Each sample run shows populated, consistent results end-to-end (card title = project event; ≥1 seated; rooming rows present).
- Promised exports exist or copy no longer promises them.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
New features beyond the listed fixes.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #57, #61, #62, #63)
