Sent: 2026-10-30 14:19 ET

# B-0256 Accommodation Manager: usable before the gate; add hotel-list reconciliation and roommate/room-type counts; shorten title, real meta
Priority: P3 · Estimated effort: M · Report: #143 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:16–14:18 ET. L-243: no untested tools remain behind live ApyHub APIs, so alphabetical (first 3 untested). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An event planner should build a rooming list from the guest list and send the hotel a clean block request, then check the hotel's reply.
## Why (1280 px; 0 trial uses)
- Premium ("Trial: 2 uses/day · 0 remaining today", $3/$9.99). Four steps visible and usable: 1 Guests → 2 Rooming list → 3 Arrivals → 4 Labels; "Add a guest…", status Confirmed/Invited/Waitlist/Declined, Import CSV, Get a blank CSV, Download CSV/Excel, Save/Open project, Try a sample. No gate met on page load (download gating untested; admin run needed).
- Shares the event "project" with Document Assembler (see L-308 guest-pass copy).
- **Missing vs competitors (~14:18 ET):** import and match the hotel's returned rooming list, flagging name/date/room-type differences (Blocks, EventProgrammer); allotment vs pickup per room type and cutoff dates (EventProgrammer, EventPipe); roommates grouped and up to N guests per room (Blocks, EventProgrammer); a read-only list link per hotel (EventProgrammer); reconciliation report after the event (EventPipe, EventProgrammer). Enterprise tools; keep scope small — reconciliation import is the one most worth copying.
- No overflow at 390 px.
## Who uses this
Wedding planners, conference organisers and HR teams booking hotel rooms for a group.
## Outcomes (ranked)
1. "Check hotel's list": import the hotel CSV and show differences.
2. Allotment vs booked per room type.
3. Roommate grouping in the rooming list.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**.
  - **Title "Accommodation Manager - Rooming List and Arrivals | FreeDailyPro" is 64 chars.**
  - **Meta 95.** H1 "Accommodation Manager".
- **Keywords:** "rooming list template", "hotel rooming list", "room block request", "event accommodation".
- **Suggested:**
  - Title: `Hotel Rooming List & Room Block Maker | FreeDailyPro` (52)
  - Meta: `Build a hotel rooming list from your guest list, send a room block request, and print arrivals, departures and room labels. Import or export CSV and Excel.` (155)
  - H1: `Rooming List and Hotel Block Manager`
  - FAQ: "What is a rooming list?" · "Can I import my guest list?" → "Yes, CSV." · "Is my data stored?" → "In this tab only."
## Constraints
Keep downloads gated per the owner's decision.
## Test cases
1. Try a sample → rooming list shows rooms and guests; Download CSV has one row per guest (admin).
2. Title ≤ 60; meta 140–160.
