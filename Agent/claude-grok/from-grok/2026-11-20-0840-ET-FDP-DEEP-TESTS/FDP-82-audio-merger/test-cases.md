Sent: 2026-11-21 18:56 ET

# FDP-82 test cases

Clips (each 20 ms beeps at whole seconds): `a.wav` 3 s 44.1 kHz 1 kHz; `b.*` 2 s 2 kHz (mp3 128k, m4a, ogg, flac); `c48.wav` 2 s 48 kHz 3 kHz; `st.wav` stereo, beeps left only; `short.wav` 0.4 s; `cover.mp3`; `video.mp4`; `corrupt.mp3`. Outputs read with `analyze.py` (beep times + pitch = clip order). Cases ran in Chromium at 10/10 (merging works without uses).

| ID | Setting | Expected | Result |
|---|---|---|---|
| X01–X09 zero (10/10) | Merge, player, Download ×2, new sets, reload | Downloads gated | Every Download → cap dialog; **player bytes = paid file (P1)** |
| X01–X09 left (0/10, try 9) | Same | 1 use per Download | **6 files for 2 uses (P1)** |
| O01 / O02 | a+b / b+a | Order kept | PASS (1,1,1,2,2 / 2,2,1,1,1 kHz) |
| O03 | a,b,c48; c moved to top | c,a,b at 48 kHz | PASS + resample note for 2nd and 3rd |
| O04 | Remove middle | a,c | PASS |
| G01–G03 | Gap 0.25 / 2 / 5 | Silence after every clip but last | PASS (exact: 3.25, 5.0, 8.0 s onsets; totals 7.5/7.0/10.0) |
| X01 / X02 | Crossfade 0.5 / 1 (3 clips) | Shorter by overlaps | PASS (4.5 s; 5.0 s) |
| X03 / X04 | Crossfade 3 with 0.4 s clip / 5 with 2 s clip | Capped at half | PASS (0.2 s → 3.2 s; 1 s → 4.0 s) + note |
| X05 | Gap 2 then Crossfade 0.5 | Gap cleared | PASS |
| R01 / R02 | 48 k first / 44.1 k first | First clip's rate | PASS + note |
| S01 / S02 | Stereo first / mono first | — | Stereo kept / **stereo folded to mono (P3)** |
| F01–F04 | Same as first: mp3, m4a, ogg, flac | Family kept | PASS (mp3 128 kbps) |
| F05–F09 | To MP3 / FLAC / M4A / OGG / WAV | Format chosen | PASS (WAV source → 192 kbps MP3) |
| E01 | cover.mp3 first | ≤ 128 kbps | **320 kbps (P2)**, no kHz in the row, cover dropped |
| E02 | video.mp4 first | Audio only | PASS (m4a family) |
| E03 | corrupt clip | Clear error | Generic F12 toast (P3) |
| E04 / E06 | Duplicate in one drop / later drop | Skipped + toast | PASS ("That file is already in the list — skipped the duplicate.") |
| E05 | One clip | Merge disabled | PASS |
| E07 | Five clips | Order + total 9.4 s | PASS |
| B01 | 2 × 28.6 MB WAV | 50 MB guest limit | Blocked; wording "a file over 50 MB" (P2) |
| QB / GD | Quick Buy / Open from Google Drive | Email + Stripe / Google sign-in | Stopped / popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales partly English |
