# APPLY-MAP — topic-mismatch abstract heroes (25)

**Batch:** `2026-11-10-1245-hero-topic-audit-25-abstract-fails`

**Source:** Full live audit of **361** downloadable `/blog/{slug}.webp` heroes (367 sitemap blog slugs; 6 missing hero files).

**Prior packs status (already live):**
- `2026-11-10-0325-hero-photoreal-upgrade-owner-26` → **26/26 MATCH live**
- `2026-10-28-1345` → 36 live · `2026-10-29-0230` → 20 live · `2026-10-31-1700` → 5 live

## Fail criteria used
- Abstract teal/neon UI only (no person doing the task)
- Pure code / lock / timer screens with no person
- Wrong topic (person present but no tool UI for the title)
- Rule: if image could fit any post → FAIL

## How Claude should apply

1. Replace live `/blog/{slug}.webp` with `images/{slug}.webp`
2. Images only
3. Verify MD5 after deploy

| # | Blog slug | Blog title | Why failed | MD5 | bytes |
|---|-----------|------------|------------|-----|-------|
| 1 | `audio-comparer` | Are These Two Audio Files the Same Recording? How to Check | waveforms_only_no_person | `7d3ab2928c86485701932431b8e61885` | 46652 |
| 2 | `build-aisle-sorted-grocery-list` | Build a Grocery List Sorted by Aisle | list_ui_only_no_person | `0f634c79b89237eb69daf13c13356962` | 60300 |
| 3 | `convert-curl-to-fetch-and-python` | Convert cURL to fetch and Python Requests | pure_code_no_person | `70d7386b2451185bbf06233b869a475b` | 52394 |
| 4 | `convert-json-api-data-to-csv-tables` | Convert JSON API Data to CSV Tables and Back | pure_code_no_person | `067567907f15ba37e5b78b58cd4de103` | 49836 |
| 5 | `corporate-safe-tools` | Getting Document Work Done When Chat Assistants Are Blocked | abstract_teal_no_person | `86eee436c2502f13c8c6327c6d0bcedd` | 41390 |
| 6 | `create-email-signature-for-gmail-and-outlook` | Create an Email Signature for Gmail and Outlook | generic_meeting_no_signature_ui | `e71074110ae8cdd3ad207839a2ae78fc` | 46810 |
| 7 | `cron-builder` | Read a Cron Schedule Before It Runs Your Job at the Wrong Hour | pure_ui_no_person | `761d154820cc6615afab58ef285e827d` | 41838 |
| 8 | `css-js-minifier` | Minify a Stylesheet and Script Safely, and Read the Gzip Number | pure_code_no_person | `d984242b475d14493434a40d7364dc87` | 48806 |
| 9 | `delete-unwanted-pages-from-pdf` | Delete Unwanted Pages From a PDF | abstract_teal_no_person | `48d3a1d7df18f6beab12af786654b340` | 48052 |
| 10 | `download-site-launch-kit-zip` | Download a Site Launch Kit ZIP | abstract_zip_only | `dc91dd7a8ce76551a0586dd05c85c009` | 47370 |
| 11 | `find-final-exam-score-needed-for-target-grade` | Find the Final Exam Score You Need for a Target Grade | abstract_teal_no_person | `c0e9396d10778a4e7969c3eff8dadca7` | 48258 |
| 12 | `format-sql-queries-for-readable-review` | Format SQL Queries for Readable Review | pure_code_abstract | `d156498bb8653b5ee29e2cdd1e1765e3` | 53334 |
| 13 | `json-formatter` | Format and Validate JSON Before You Paste It Into Production | pure_code_no_person | `7b3fdbe427e95fa2d98a8b6ff226913c` | 47574 |
| 14 | `jwt-decoder-debug-tokens` | Decode JWTs Instantly in Your Browser for Auth Debugging | pure_tokens_no_person | `f1152fcbed6e06fbbc525bb7a802199d` | 55004 |
| 15 | `make-srt-vtt-subtitles-from-audio` | Make SRT and VTT Subtitles From Audio | abstract_teal_no_person | `760cf571831480f1bff0534aa56fb7a7` | 55308 |
| 16 | `manage-hotel-rooming-list-and-arrivals` | Manage Hotel Rooming Lists and Arrivals | abstract_teal_no_person | `cade1b88efe78cbd6b6d82cf37c2139c` | 59114 |
| 17 | `mesh-3d-viewer` | Read an STL | abstract_mesh_only | `2e4273dff2221cb820489ecc45b6089f` | 69678 |
| 18 | `password-strength` | Why "Welcome2026!" Scores Fair and How to Do Better | abstract_lock_only | `8457beea0aebe79a503845e4e760ed49` | 48598 |
| 19 | `plan-guest-arrivals-and-departures` | Plan Guest Arrivals and Departures for Shuttles | abstract_teal_no_person | `273e0e6f395ef7356445bd5040982b4a` | 64552 |
| 20 | `play-video-clip-backwards-for-effects` | Play a Video Clip Backwards for Effects | flat_abstract_ui | `43c08c02fd22a3b1d716cbf3970b38bd` | 48014 |
| 21 | `remove-audio-track-from-video-file` | Remove the Audio Track From a Video File | flat_abstract_ui | `ab69fc4a97f5e18749cdba206e613a14` | 46542 |
| 22 | `run-prize-draw-and-event-merch` | Run a Fair Prize Draw and Event Merch Plan | abstract_teal_no_person | `55f91405151d5b4b23587160ecbecaf6` | 47880 |
| 23 | `run-stage-countdown-and-focus-rounds` | Run a Stage Countdown or Focus Work Rounds | abstract_numbers_only | `f15d9db035d59fe61874e299b237b605` | 44250 |
| 24 | `sprite-sheet-tool` | Pack 12 UI Icons Into One Sprite Sheet and Split It Again | abstract_icons_only | `d7bf09271b0d9777793fc7ebbf6a4be1` | 58372 |
| 25 | `timestamp-converter` | Read Unix Timestamps in Logs: Seconds, Milliseconds, UTC | abstract_ui_no_person | `cead7428ed6aeefa98caaccf751daa66` | 62672 |

**Total:** 25
