Sent: 2026-11-21 17:50 ET

# Live functional findings (FDP-78)

- Zero (Chromium 10/10): Get Thumbnails works, preview + tiles visible; all Download and ZIP presses show the cap dialog; 0 files.
- Left (Chromium 0/10): 9 files saved for 2 uses (X02 and X10 after reload). Files in `evidence/downloads/`.
- Badge: maxres 89,022 B vs original 65,324 B, two "Created with FreeDailyPro.com" marks. Small (120×90) identical to YouTube's.
- Parse: 18/25 handled as expected; co.uk, attribution_link, gaming rejected (P3).
- Resubmit bug confirmed in Chromium and Firefox.
- Quick Buy: Day Pass → email dialog; Monthly → Stripe checkout (ID redacted). Stopped.
