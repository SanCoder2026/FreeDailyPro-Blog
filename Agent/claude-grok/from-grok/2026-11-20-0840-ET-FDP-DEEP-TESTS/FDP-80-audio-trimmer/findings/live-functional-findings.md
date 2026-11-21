Sent: 2026-11-21 18:23 ET

# Live functional findings (FDP-80)

- Zero (Chromium 10/10): trim and Remove section work, result player plays; Download → cap dialog ×7; 0 POSTs. Player bytes saved.
- Left (Chromium 0/10, try 25): 7 Downloads, 2 POSTs (first in each page load).
- Player at 10/10 = Download with uses, byte for byte (`cmp`).
- Cuts are sample-exact at tenths in all 7 formats; hundredths are rounded to tenths at Trim.
- Errors: no-audio video, corrupt file, negative, text, reversed and past-end times all handled with clear messages.
- Firefox: 40 fresh contexts all at 10/10.
