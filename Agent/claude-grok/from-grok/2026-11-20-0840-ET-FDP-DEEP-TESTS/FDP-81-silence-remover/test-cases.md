Sent: 2026-11-21 18:39 ET

# FDP-81 test cases

Input `speech.wav`: lead 1.0 s, six 1 s tone bursts, gaps 0.1/0.3/0.6/1.5/3.0 s, trail 2.0 s, floor -50 dBFS (14.5 s). Outputs read with `analyze.py`. All in Chromium at 10/10 (processing works without uses).

| ID | Setting | Expected | Result |
|---|---|---|---|
| X01–X10 zero (10/10) | Drop, Preview, Remove, result player, Download ×2, new MP3/FLAC, reload + 48k/22k | Downloads gated | Every Download → cap dialog; **Preview + result saveable (P1 owner rule)** |
| X01–X10 left (0/10, try 16) | Same | 1 use per Download | **6 files for 2 uses (P1)** |
| D01 | Defaults (-35 dB, 0.5 s, remove) | Lead, 0.6/1.5/3.0, trail cut; 0.1/0.3 kept | PASS: 14.5 → 6.5 s; cut pauses 0.02–0.03 s |
| D02 / D03 / D04 | Shorten 0.3 / 0.5 / 1 | Pauses ≈ setting | PASS (0.28 / 0.48 / 1.0; 0.6 s left alone at 1 s) |
| D05 / D06 | Min 0.2 / 2.0 | 0.3 cut / only 3.0 + trail | PASS |
| D07 / D08 | Un-tick lead / Keep all | Lead kept / Remove off | PASS ("1 kept") |
| N01 | Floor -30 dB at -35 | No pauses | PASS ("No pauses found at these settings") |
| N02 / N03 | Auto threshold | floor +10 dB | PASS (-30 → -20; -50 → -40) |
| N04 / N05 | Soft speech -40 dB / all quiet | Message | PASS ("The whole file is quieter…") |
| N06 | -15 dB | Still correct | PASS |
| R01 / R02 | 48 kHz / 22.05 kHz | Rate kept | PASS (summary states it) |
| S01 | Stereo, R fills one gap | Gap kept | PASS |
| F01–F04 | MP3 / M4A / FLAC / OGG | Same family | PASS |
| M01 | 1,100 × 0.5 s gaps, 8 kHz | 1,100 at min 0.5 | **550 (P3)**; list capped at 1000 note not reached |
| P01 | Preview vs result | Same audio | PCM identical |
| QB / GD | Quick Buy / Open from Google Drive | Email+Stripe / Google sign-in | Stopped / popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales partly English |
