Sent: 2026-10-30 14:33 ET

# B-0267 Arrivals and Departures Board: board works before the gate; add times, flight numbers and pickup grouping; Save project is gated
Priority: P3 · Estimated effort: M · Report: #147 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:30–14:33 ET. L-243: next 3 untested tools alphabetically after agenda-cue-sheet-builder. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An event planner should see who lands when, group guests into pickups, and hand the driver a manifest.
## Why (1280 px; 0 trial uses)
- Try a sample: tiles (4 arrivals, 4 departures, busiest day 2026-11-12 (4)), day list "Arriving (4): Amara Okafor, Fatima Al-Sayed, Lukas Meyer, Maya Patel", "Leaving (1)…", "Leaving (3)…", and a travel-dates table for 7 guests. Copy / CSV / PDF present.
- **"Save project" opened "Your result is ready… this download needs a pass" at 0 trial uses.** Gating is the owner's decision; noted because a project file is the user's own data (also affects Agenda/Accommodation, which share the project).
- **Dates only:** the page says to put flight numbers or times in guest notes. No time, airport, terminal or pax/bags fields.
- **Missing vs competitors (~14:32 ET):** grouping by time window, terminal and vehicle capacity (EventProgrammer, DMC Pilot); hour-by-hour arrivals and bags (EventProgrammer manifest template); per-vehicle passenger manifest with driver/plate (TransferCRM, EventProgrammer); live link for greeters with status (pending, landed, picked up) (EventProgrammer, DMC Pilot). EventProgrammer's free template columns (Date, Direction, Airport, Terminal, Flight No, Flight Time, Pickup Time, Pax, Bags, Hotel, Vehicle, Status) are a good minimal target.
- Unnamed controls → B-0155. No overflow at 390 px.
## Who uses this
Wedding planners, DMCs and conference teams arranging airport pickups.
## Outcomes (ranked)
1. Arrival/departure time and flight number fields; board sorted by time.
2. Group guests landing within N minutes into one pickup, with pax count.
3. Per-pickup manifest in the CSV/PDF.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**. Site-wide → **B-0209**.
  - Title "Arrivals and Departures Board - Plan Pickups and Shuttles" (57), no brand. Meta 140 ✔ (borderline; ends "Free and fast, right in your browser"). H1 "Arrivals and Departures Board".
- **Keywords:** "airport transfer manifest", "guest arrivals schedule", "event shuttle schedule", "airport pickup list".
- **Suggested:**
  - Title: `Arrivals & Departures Board – Event Pickups | FreeDailyPro` (58)
  - Meta: `See which guests arrive and leave each day of your event, spot the busiest day, and download a pickup sheet as CSV or PDF for drivers and the welcome desk.` (155)
  - H1: `Guest Arrivals and Departures by Day`
  - FAQ: "Can I add flight numbers?" · "Does it track flights?" → "No." · "Where do the dates come from?"
## Constraints
Keep downloads gated per the owner's decision.
## Test cases
1. Try a sample → board shows 4 arriving on 2026-11-12.
2. Admin: CSV/PDF pickup sheet contents.
3. Title ≤ 60; meta 140–160.
