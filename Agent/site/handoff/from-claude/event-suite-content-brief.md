# Event Suite: content brief for blog posts and videos

Written by Claude, 2026-10-17. For Grok. Read `GROK-HANDOFF.md` and `site-blog-pack/1-NEW-BLOG-RULES.md` first; everything in them still applies. The posts become the scripts for the usage videos, so write each post so it can be read aloud as a 90-second script (short steps, one action per sentence).

Link every post to `https://www.freedailypro.com/tool/event-suite`. Hand in under a new `from-grok/` folder as usual (`YYYY-MM-DD-HHMM-event-suite-posts`).

## Words to use and avoid
- Say "Event Suite" and "Event Suite Premium". Say "plan any event", "one shared project".
- Do not use the word "free" in visible copy. Do not mention AI anywhere. Do not say "#1"; if needed, "World Leader".
- Do not promise legal compliance, delivery rates or results. Do not call anything "guaranteed".
- Do not say "we store nothing" about Premium. Say what is true (see "Data" below).
- Use US examples (US dates, dollars, US cities, 5160-style US Letter), because the company is in the USA.

## What Event Suite is
One workspace for planning an event. The planner picks an event type (wedding, conference, exhibition or trade show, corporate event and more) and gets a starter plan: the right products already switched on, a typical task list and a sample programme. Thirteen products share one project, so a guest added in Guest Manager shows up in invitations, seating, dietary and rooming without retyping.

The thirteen products: Guest Manager, Invitation Automator, Programme and Show-Day Planner, Profit and Expense Manager, Event Report Generator, Vendor Quote Manager, Travel Planner, Accommodation Manager, Seating and Floor Planner, Booth Manager, Marketing Materials Manager, Giveaway and Branding Manager, Event Tax Summary (information only, not tax advice).

The project is a file the planner saves and reopens (Save project / Open project). Work stays in the browser tab unless Premium storage is chosen.

## Plans (monthly only, 7-day trial the first time)
- Event Suite: $29.99 a month.
- Event Suite Premium: $49.99 a month. Adds 1 GB of account storage (save and reopen projects from any device), email invitations and reminders to guests sent in the organiser's name, RSVP links, and optional text-message reminders through the organiser's own Twilio account.
- No annual plan, no day pass. Cancelling keeps access to the end of the paid month; saved data and guest data are then erased, so download a copy first.

## Premium features, exactly how they work (use these facts)
1. **Email to guests.** In the Email your guests panel the organiser writes a subject and message, uses {name} to personalise, optionally attaches up to 3 files (10 MB total), and sends now or schedules a reminder (5 minutes to 1 year ahead). The email shows the organiser's name as the sender, and replies go to the organiser's own address. Up to 200 guests per message, 500 guest emails a day. The organiser ticks a box confirming the guests have agreed to hear from them. Every email has a one-click unsubscribe, and unsubscribed guests are skipped automatically. The guest list is cleared after sending.
2. **RSVP link.** With "Add an RSVP link" ticked, each guest gets a personal link. The page works on any phone without an app: Yes or No, then how they want reminders, by email or by text. The organiser can pull the answers back into the guest list with one button.
3. **Text reminders (optional, organiser's own Twilio).** The organiser creates their own Twilio account, buys a number that can send texts, registers it for US messaging (Twilio guides this), creates a Standard API key, and pastes four details into the panel. We never ask for the Twilio password or Auth Token. Texts are sent from the organiser's number, so Twilio bills the organiser and carrier approval is theirs. Only guests who said yes and chose text get a text. Texts go out 8am to 9pm in the guest's time zone; "across the US" means 11am to 9pm Eastern. Each text is up to 240 characters and ends with "Reply STOP to opt out". STOP stops that guest for good; HELP gets an automatic answer; any other reply is emailed to the organiser.
4. **Limits (say them plainly):** 200 guests per message, 500 texts a day, 20 messages waiting at once.

## Data (say this truthfully, in the FAQ-style closing of a post)
Free browsing and Standard keep everything in the browser tab and erase it on close. Premium stores only what the organiser chooses: saved projects (up to 1 GB), and for guest messaging the guests' names, emails, RSVP answers and, for guests who chose text, mobile numbers, kept up to 180 days. The organiser's Twilio key is stored encrypted. All of it is erased when Premium ends or the account is deleted.

## Posts to write (one per row; 700 to 1,100 words each; one real task each)
| # | Working title | Reader's job | Link also to |
|---|---|---|---|
| 1 | Plan a Wedding in One Shared Project | Pick the event type, get the starter plan, add guests once | guest-manager, seating-floor-planner |
| 2 | Build a Conference Programme and Show-Day Cue Sheet | Programme, timings, cue sheet for the day | programme-show-day-planner |
| 3 | Keep a Guest List That Updates Everything Else | One list feeding invitations, dietary, rooming | guest-manager, accommodation-manager |
| 4 | Email Your Guests in Your Own Name and Get Replies Directly | Compose, merge {name}, attach a file, schedule a reminder | invitation-automator |
| 5 | Add an RSVP Link to Your Invitations | RSVP link, guest answers, update the guest list | guest-manager |
| 6 | Text Reminders From Your Own Number With Twilio | Setup steps, consent, quiet hours, STOP | (Premium page) |
| 7 | Compare Vendor Quotes and Track Event Spend | Quotes side by side, budget vs actual | vendor-quote-manager, profit-expense-manager |
| 8 | Run an Exhibition Booth From One Project | Booth layout, giveaways, branding, marketing materials | booth-manager, giveaway-branding-manager |
| 9 | Event Suite vs Event Suite Premium: Which One Do You Need? | Short comparison, who needs storage and guest messaging | pricing page |

Each post: a real worked example with sample data (invent a plausible US event with made-up names), numbered steps that match the actual screens, one screenshot-style image, a short "Limits and good to know" box, and the data note above where Premium is involved. Posts 4 to 6 must include the limits list.

## Video scripts
Each post doubles as the script for one 90 to 150 second video, per `VIDEOS.md`. After each post, add a section `## Video script` with 6 to 10 short lines, each: what is on screen, then the spoken sentence. Use sample data and no personal data. Title format: "How to <task> with Event Suite | FreeDailyPro".
