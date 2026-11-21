Sent: 2026-11-21 18:39 ET

# Live functional findings (FDP-81)

- Zero (10/10): Preview, Remove Silence and the result player all work; Download ×7 → cap dialog; 0 POSTs.
- Left (0/10): 6 Downloads, 2 POSTs (first per page load).
- Byte checks: result player at 10/10 = paid Download (`cmp`); Preview PCM = Download PCM (md5).
- Detection and shortening are accurate on every case; sample rate and channels preserved; Auto threshold matches the FAQ.
- Firefox left search stopped after Chromium found a context.
