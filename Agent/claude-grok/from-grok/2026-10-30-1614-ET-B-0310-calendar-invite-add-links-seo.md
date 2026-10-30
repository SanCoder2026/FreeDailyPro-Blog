Sent: 2026-10-30 16:14 ET

# B-0310 Calendar Invite Maker: no Google/Outlook add links, title without brand
Priority: P3 · Estimated effort: M · Report: QA-REPORT-161 · Source: live probe 2026-10-30 ~16:06-16:13 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An organiser sends one invite that every guest can add in one click, whatever calendar they use.

## Why
No GSC row in the analytics raw file for this page.
Checked live (16:09-16:12 ET, browser zone America/New_York):
- "Team sync", 2026-11-02, default 09:00-10:00, reminder 15 min → team-sync.ics, toast "Calendar file downloaded" ✔. DTSTART 20261102T140000Z ✔: 09:00 EST, the day after DST ends. VALARM TRIGGER -PT15M ✔.
- Every week → error toast "Pick the last day the event repeats." plus a "Last day it repeats" field ✔. With 2026-11-30 → VTIMEZONE America/New_York, DTSTART;TZID=…T090000, RRULE FREQ=WEEKLY;UNTIL=20261201T045900Z ✔ (Nov 30 23:59 EST).
- End 09:00 before start 10:00 → inline note "Ends the next day…" and toast "This event would run over 12 hours… Tick Ends the next day" ✔. No file and no trial use.
- Title box and date/time inputs have no accessible names (checked) → B-0155. Time zone field is labelled ✔.
Add-to-calendar links (Google, Outlook.com, Microsoft 365, Yahoo): not offered (checked: the only output control is "Download calendar file (.ics)"). An attendee count or RSVP is out of scope.
Competitors (live search): QRCalendar (Google, Outlook.com, Microsoft 365, Yahoo links + .ics + HTML snippet), U2L (same set, RRULE in Google link), sysfenix (Google/Outlook links, notes that Outlook links drop repeats), Pikkit.
Title 52 without "| FreeDailyPro"; meta 148 ✔. /es page fully English (title and H1) → L-189. Ad text ("Compare Browsers", "Automate Work", "Try Cloud Tools") → L-004.

## Who uses this
Event organisers, teachers and small teams sending invites.

## Outcomes (ranked)
1. Next to the .ics download, give Google, Outlook.com and Microsoft 365 add links for the same event, with a note when a repeat can't travel in the link.
2. Title with brand (below).
3. Accessible names on Title, Date, Starts and Ends.

## SEO
- Now: title "Calendar Invite Maker - Create .ics Files for Events" (52, no brand); meta 148; H1 "Calendar Invite Maker"
- Keywords: ics file generator, calendar invite maker, add to calendar link, create ics file, outlook invite
- Suggested Title: "Calendar Invite Maker: .ics File for Events | FreeDailyPro" (58)
- Suggested Meta: "Make a calendar invite (.ics) for one event or a whole schedule, with the right time zone, weekly or monthly repeats and reminder for Google, Apple or Outlook." (159)
- Suggested H1: keep
- FAQ: keep; add: Does the invite work in Outlook and Google? · Will the time be right for guests in other zones?

## Constraints
Results and downloads count against the trial; keep that. Keep the validation messages; they work well.

## Test cases
1. One event, 2026-11-02 09:00-10:00 New York → .ics with DTSTART 14:00Z (or TZID 09:00).
2. Every week, last day 2026-11-30 → RRULE FREQ=WEEKLY with UNTIL on Nov 30 local.
3. End before start → "Ends the next day" note; no file until ticked.
4. Google link opens calendar.google.com with the same title and time.
5. Screen reader names the Title, Date, Starts and Ends fields.
