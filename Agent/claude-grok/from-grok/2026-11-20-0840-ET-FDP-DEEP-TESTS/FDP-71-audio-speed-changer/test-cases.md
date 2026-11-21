Sent: 2026-11-21 16:05 ET

# FDP-71 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z02 | 10/10: WAV, 1x | Change Speed disabled | PASS |
| Z03–Z05 | 10/10: 2x Change Speed; player attrs; player blob | Gated or reduced | Full result plays (owner question); controls without nodownload |
| Z06, Z08 | 10/10: Download | Gate | Cap dialog (PASS) |
| X-menu | 10/10: player ⋮ → Download | Blocked | **Saved, byte-identical to paid file (P1)** |
| X-drive/cloud | Save to Google Drive / cloud storage at 10/10 | Gate / sign-in | Cap dialog / sign-in + add-on dialog |
| L01–L09 | 0/10: WAV 1.5x ×2, 2x, MP3 0.5x, M4A 1.25x +12, reload FLAC 2x ×2 | 1 use per new result | **2 POSTs for 7 files (P1)**; outputs exact |
| C01–C04 | FLAC 2x, OGG 3x, M4A 0.5x, WAV 4x | Exact tempo, pitch kept | PASS |
| C05–C06 | 48 kHz stereo 1.25x −12; WAV 1x +12 | 220 Hz / 880 Hz, rate kept | PASS |
| C07 | MP4 with picture 2x | Audio-only M4A | PASS (as documented) |
| C08 | Non-audio | Reject at upload | Fails after ~75 s, F12 advice (P2) |
| C09 | Slider End/Home | 4x / 0.5x | PASS |
| Q / Drive | Quick Buy; Open from Google Drive | Email / Stripe; sign-in | Stopped; popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
