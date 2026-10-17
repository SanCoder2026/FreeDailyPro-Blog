# Event apps (Guest, Door Check, Booth Leads): content brief for blog posts and videos

Written by Claude, 2026-10-17. For Grok. Read `GROK-HANDOFF.md` and `site-blog-pack/1-NEW-BLOG-RULES.md` first; everything in them still applies, and so does `event-suite-content-brief.md` (words to avoid, US examples, video script format). This brief adds the three new apps and CORRECTS the plan and data facts in the older brief (see "What changed").

Link every post to `https://www.freedailypro.com/tool/event-suite` and to the Premium plan. Hand in under `from-grok/` as usual (`YYYY-MM-DD-HHMM-event-apps-posts`). Each post is also a 90 to 150 second video script, so write short steps, one action per sentence, and add the `## Video script` section (6 to 10 lines: what is on screen, then the spoken sentence). Video title format: "How to <task> with Event Suite | FreeDailyPro".

## What changed since the Event Suite brief (use these facts, not the old ones)
- **Both plans include 1 GB of account storage**: Event Suite ($29.99 a month) and Event Suite Premium ($49.99 a month). Saved projects work on both. Monthly only, 7-day trial the first time, no day pass.
- **Premium adds**: the three event apps, email to guests with RSVP links and scheduled reminders, and optional text reminders through the organiser's own Twilio account.
- **No automatic expiry** of event data. It stays until the organiser deletes it, or Premium ends, or the account is deleted. The only limit is the 1 GB, shared by saved projects, published events, check-ins and leads.

## What the apps are
Three installable apps. Nothing to download from a store: the person opens a link on their phone and adds it to the home screen. They work with no signal after the first load and update themselves when the site is updated. No logins for guests, door staff or exhibitors: each person gets a private link.

The organiser starts in Event Suite Premium and presses **Publish event**. That saves a snapshot of the event and creates a guest link and a door link; the organiser adds one booth link per exhibitor. Each link has a QR code to share. After changing the plan, the organiser presses **Update** and the apps pick up the change (when opened, and about once a minute while open). The organiser can stop (revoke) or replace (rotate) any link at any time, and delete the published event.

### 1. Event Guide (for guests), `/apps/guest/<link>`
Tabs: Now, Programme, Venue, News, My pass.
- Now: what is on right now and what is next, in the event's own time zone.
- Programme: by day, with room and speaker; add one session or the whole programme to the phone calendar (.ics file).
- Venue: name, address, "Open map" link, notes from the organiser.
- News: announcements the organiser published.
- My pass: the guest pastes the pass code from their invitation, or scans the QR on it, and the QR shows on their screen for the door. The pass stays on their phone only; we never learn which guest opened a link.
- Keeps the last copy so it opens with no signal. If the organiser stops the link, the guest sees a message and keeps the last copy.

### 2. Door Check (for door staff), `/apps/door/<link>`
- Scan a guest's pass QR with the phone camera (or search by name). Result: Valid, Already in (with the time), Declined, Not on the list, or Not a pass for this event.
- Works with no signal: the guest list and the key that checks passes are on the phone. Check-ins are queued and sent when back online; every door's check-ins are merged, so two doors do not let the same guest in twice.
- Shows a running count. The door link shows the guest list, so tell readers to give it only to door staff.

### 3. Booth Leads (for exhibitor staff), `/apps/booth/<link>`
- Capture a visitor in about ten seconds: scan their badge or contact QR, or type name, company, email, phone, what they were interested in, mark Hot, Warm or Cold, tick "Follow up after the event", add a note.
- Warns when the same person is added twice. Tap a lead to edit it. Download all leads as a CSV file for the CRM or a mail merge.
- Offline first: leads are kept on the phone and sent when back online.
- Privacy: leads belong to that exhibitor's link. The organiser sees only how many leads there are, not who they are.

## Data (say this truthfully in a closing FAQ-style note; do not say "we store nothing" about Premium)
Free browsing and Event Suite keep everything in the browser tab unless the organiser chooses to save a project to their account (up to 1 GB). For Premium event apps we keep the published event (details, programme, announcements), the guest list shown to door staff (name, ticket type, status), the door check-ins, and each booth's leads. For guest messaging we keep guest names, emails, RSVP answers and, for guests who chose text, mobile numbers, up to 180 days. All of it is kept until the organiser deletes it or Premium ends, and is erased when Premium ends or the account is deleted. Download a copy first.

## Limits (say them plainly in each post's "Limits and good to know" box)
- A published event can be up to 2 MB (roughly 20,000 guests). Up to 50 published events and 60 links per event.
- Up to 300 programme items and 100 announcements.
- Do not promise results, speed at the door, or that the camera works in every phone, light or browser. Say "use the Search box if a code will not scan".
- iPhone: Share, then Add to Home Screen. Android: browser menu, Install app. Say both.

## Posts to write (700 to 1,100 words; one real task each; real worked example with made-up US names)
| # | Working title | Reader's job | Link also to |
|---|---|---|---|
| 1 | Publish Your Event and Share the Guest App | Press Publish event, share the guest link and QR, update after a change | event-suite |
| 2 | Give Guests a Programme, Map and Pass on Their Phones | Guest side: open link, now/next, add to calendar, save the pass | programme-show-day-planner |
| 3 | Check Guests In at the Door With No Signal | Door staff setup, scan, Already in, two doors, offline queue | guest-manager, badge-pass-maker |
| 4 | Capture Booth Leads in Ten Seconds | Exhibitor flow, hot/warm/cold, CSV download | booth-manager |
| 5 | One Link per Exhibitor: Running a Trade Show Floor | Organiser creates booth links, counts, stop a link | booth-manager |
| 6 | Install the Event Apps on iPhone and Android | Add to Home Screen steps, offline use, updates | (apps FAQ) |
| 7 | What Event Suite Premium Keeps About Your Event | Plain data note: what is stored, how to delete, 1 GB | pricing page |

Posts 3 to 5 should show the actual screens' wording (for example "Valid", "Already in", "Follow up after the event"). Add one screenshot-style image per post (hero 1200x630 WebP as usual). App icons: Door Check is teal with a scan-and-check symbol, Booth Leads is orange with a contact card, Event Guide is blue with a calendar and check.

## Quality notes from the last batch check (apply to these posts too)
The site checker flagged, across recent posts: the word "free" in titles or body, mentions of AI, titles over 70 characters, fewer than 5 tags, fewer than 3 links to other pages on the site, and bodies under 500 words. Keep every new post clear of these.
