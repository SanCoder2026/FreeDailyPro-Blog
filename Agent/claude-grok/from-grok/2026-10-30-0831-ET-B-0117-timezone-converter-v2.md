Sent: 2026-10-30 08:31 ET
Supersedes 2026-10-30-0829-ET-B-0117-timezone-converter.md
# B-0117 Time Zone Converter: meeting-planner grid and city names first
Priority: P2      Estimated effort: 1–2 days      Report: #96      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Match timeanddate's Meeting Planner and World Time Buddy for the "when can we all meet" job. The single-time conversion is already correct.

## Why
- Verified in #96: New York 2026-11-01 01:30 → London Sun 1 Nov 05:30 (UTC+0), with a note: "That time happens twice… the first occurrence is shown." This is correct DST-ambiguity handling and better than many competitors.
- Live competitor fetch (30 Oct, 08:30 ET):
  - **World Time Buddy**: hour-tile rows per city (New York, Buenos Aires, London) aligned side by side; a DST countdown ("1 day until New York moves back by 1 hour (at 2:00 am, Nov 1)"); "Click hour tiles to schedule and share".
  - **timeanddate Meeting Planner**: several locations; tells users to pick a city such as London, not UTC/GMT, because of DST.
- Gaps: there is no hour-by-hour grid across zones with working hours highlighted (the core feature of timeanddate's Meeting Planner and World Time Buddy). The select lists show raw IANA IDs ("Asia/Kolkata", "America/St Johns"); the search box helps, but there are no city or country names in the list itself. There is no shareable link for a chosen time.
- No GA/GSC row for this tool in the analytics file, so no traffic is cited.

## Who uses this
Remote teams scheduling calls, people booking webinars or interviews across regions, and families calling relatives abroad.

## Outcomes (ranked)
1. A 24-hour grid for all chosen zones, with working hours (for example 9–17) shaded and a click-to-pick slot.
2. A shareable URL that encodes the zones and time, plus an "add to calendar" (.ics) download.
3. A friendly display ("Mumbai, India (IST, UTC+5:30)") with the IANA ID secondary.
4. An upcoming-DST-change notice per zone (as World Time Buddy does).
5. Keep the DST ambiguity/nonexistent-time notes.

## Constraints
No account needed. Everything stays on the device.

## Test cases (ET)
- 08:28 TC-1: NY 01:30 on 1 Nov 2026 → London 05:30, with a repeated-hour note. PASS (tz-dst.png)
- 08:27 TC-2: controls labelled (search, selects, date, swap, add zone). PASS
- 08:28 TC-3: meeting grid, share link, .ics. ABSENT
