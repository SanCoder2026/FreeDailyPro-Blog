Sent: 2026-11-21 18:23 ET

# FDP-80 test cases

Input: `beeps20.wav` = 20 s, 20 ms 1 kHz beep at every whole second, 2 kHz at 10 s; other formats encoded from it. Output read with `analyze.py` (duration, beep onsets). All in Chromium at 10/10 (Trim works without uses).

| ID | Input / action | Expected | Result |
|---|---|---|---|
| X01–X10 zero (10/10) | Trim, player bytes, Download, re-trim, Remove, new WAV, reload | Gated | Trim + player work; every Download → cap dialog. **Player saveable (P1 owner rule)** |
| X01–X10 left (0/10, try 25) | Same | 1 use per Download | **7 files for 2 uses (P1)** |
| F01–F07 | WAV, MP3, FLAC, M4A, OGG, Opus, MP4 video; 3.25–7.5 | 4.25 s, beep at 0.75 | **4.2 s, beep 0.70 (P2)**; formats right (Opus → OGG/Vorbis, MP4 → M4A, documented) |
| F08 | MP3 with title + cover; 2–6 | Tags + cover kept | PASS |
| M01 / M02 | Remove 5–15 / 12–end | 10 s / 12 s, joined | PASS |
| M03 | Remove all | Message | PASS |
| A01 / A02 | Fades 2+2 on 10 s / 5+5 on 3 s | Fades; capped | PASS |
| T01 | 0:03.5 → 0:08 | 4.5 s | PASS |
| T02 | End 25 on 20 s | Clamp | PASS (5 s) |
| T03 / T04 / T07 / T09 | end<start / start>dur / -1 / abc | Message, Trim off | PASS |
| T05 | 0:05:10 on 6 min | 310 s or a message | **Read as 5 s; confusing error (P3)** |
| T06 | 2,5 | 2.5 or a message | 2 silently (P3) |
| T08 | 3 → 3.05 | 0.05 s | 0.1 s; summary "0:00.0" (P3) |
| T10 | End first, then Start 3.25 | 3.25 | **3.3 (P2)** |
| T11 | Slider key after 3.25 | — | Start 3.3 |
| E01 / E02 | Video without audio / corrupt MP3 | Message, no use | PASS ("Nothing was used from your trial") |
| E03 | 0.5 s file, 0–0.3 | 0.3 s | PASS |
| R01 | Ringtone from 1:00 on 6 min | 1:00–1:30 | PASS |
| L01 | 63 MB WAV | Notice | 50 MB guest limit; drop zone says 500 MB (P2) |
| QB / GD | Quick Buy / Open from Google Drive | Email+Stripe / Google sign-in | Stopped / popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales partly English |
