# event-apps-posts
Date and time: 2026-10-17 18:30
Type: NEW (Event Suite Premium event apps: Guest / Door Check / Booth Leads)

Source brief: `from-claude/event-apps-content-brief.md` (a16c2a4)
Also follows: event-suite-content-brief.md (corrected plan/data facts), GROK-HANDOFF.md, 1-NEW-BLOG-RULES.md

What is in it:
- posts/ (7) dedicated posts for Event Guide, Door Check, Booth Leads, install, and Premium data
- images/ (7) 1200x630 WebP bottom-stripe heroes

## Posts (schedule one per day)
- 2027-04-12 | `capture-booth-leads-in-ten-seconds` | Capture Booth Leads in Ten Seconds | ~1141 words
- 2027-04-11 | `door-check-guests-offline-no-signal` | Check Guests In at the Door With No Signal | ~1097 words
- 2027-04-15 | `event-suite-premium-data-what-is-kept` | What Event Suite Premium Keeps About Your Event | ~1064 words
- 2027-04-10 | `guest-programme-map-and-pass-on-phone` | Give Guests a Programme, Map and Pass on Their Phones | ~1088 words
- 2027-04-14 | `install-event-apps-iphone-android` | Install the Event Apps on iPhone and Android | ~1135 words
- 2027-04-13 | `one-link-per-exhibitor-trade-show-floor` | One Link per Exhibitor: Running a Trade Show Floor | ~1107 words
- 2027-04-09 | `publish-event-share-guest-app` | Publish Your Event and Share the Guest App | ~1144 words

## Videos
Each post includes `## Video script` (8 lines: on-screen + spoken). Title format: "How to <task> with Event Suite | FreeDailyPro".

## Corrected plan facts used (supersede older Event Suite brief where they conflict)
- Both plans include 1 GB account storage (Event Suite $29.99/mo, Premium $49.99/mo)
- Premium adds: three event apps, email to guests with RSVP + scheduled reminders, optional Twilio texts via organiser's account
- No automatic data expiry; stays until organiser deletes, Premium ends, or account deleted; limit is 1 GB shared
- Published event up to 2 MB (~20k guests), 50 published events, 60 links/event, 300 programme items, 100 announcements

## Tool id note (Claude / site)
- Primary tool in every post: `event-suite` → https://www.freedailypro.com/tool/event-suite
- **`event-suite` is not yet in site-blog-pack/tool-ids.txt** (only event-budget-planner, event-checklist-planner, event-day-schedule exist as event tools). Please add `event-suite` to tool-ids before site import, or the validator will reject.
- Related tools used (all valid ids): event-checklist-planner, event-day-schedule, guest-list-tracker, event-budget-planner
- Brief suggested guest-manager, badge-pass-maker, booth-manager, programme-show-day-planner — those ids are also absent from tool-ids.txt, so valid siblings were used instead.

## Quality checks
- Titles ≤70, no "free", no AI
- Descriptions 70–150 chars
- Tags ≥5
- ≥3 internal site links
- 1000+ body words (range ~1060–1140)
- shared_long=0 across the batch
- contact paragraph last
- Limits and good to know box in each post
- Video script section present
- Heroes 1200x630 WebP <150KB with FreeDailyPro bottom stripe

## Anything Claude should know
- Worked example thread: Midwest Product Expo 2027, Columbus OH, organiser Priya Nair (and door lead Marcus Holt where relevant)
- App UI wording used: Valid, Already in, Follow up after the event, Hot/Warm/Cold, Publish event, Update, Now/Programme/Venue/News/My pass
- iPhone: Share → Add to Home Screen; Android: browser menu → Install app
- Install and publish heroes are slightly smaller files; regenerate later if visual quality is insufficient
