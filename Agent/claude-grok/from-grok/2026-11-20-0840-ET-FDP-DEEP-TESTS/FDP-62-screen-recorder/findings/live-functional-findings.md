Sent: 2026-11-21 13:20 ET

# Live functional findings (FDP-62)

- **zero.json (Chromium, 2/2):** defaults Camera/countdown/Mic on, mic picker shown (fake devices). Full take with countdown "2" seen, meter 2, Pause holds the timer at 00:05, "Recorded 00:07". Download → cap dialog, no POST. Region take (camera and countdown off): Record Selected Region shown after the drag, "Recorded 00:05". Download → cap dialog. The player still plays the whole clip (5.06 s, 642×290).
- **zero-firefox.json:** same, "Recorded 00:08", region 642×290.
- **left.json (0/2 on try 5):**
  - L02: 1280×720 VP9/Opus, 8.56 s, 484 KB. One POST; count 0→2 (server pool).
  - L04: region + camera, 642×290, 4.94 s, at 2/2 with no POST and no dialog.
  - After reload, L06 → cap dialog.
- **deny.json:** camera and mic denied toasts; recording continues.
- **nodm.json:** phone note shown; Start enabled → toast "Screen recording isn't supported in this browser".
- **stopcheck.json:** Stop responds in ~50 ms with mic on or off. A long "Recorded 00:19/00:20" in deny/L05 was a script wait on the missing mic meter, not the site.
- **quickbuy.json:** Day → email prompt; Monthly → Stripe (stopped, redacted).
- **WebKit:** tab crash at load (zero-webkit*.log). `enumerateDevices()` crashes WebKit on example.com too (px62-wk2.js) → env.
