Sent: 2026-10-30 13:17 ET

# QA Report #126 — Addendum: admin-session output checks
The admin session ran about 13:14–13:15 ET. Files are in `batch-45/downloads/`; ffprobe/FFT checks were run by QA. This adds to report #126, which itself is unchanged.

## text-sorter (L-265) — output verified (admin session)
- Natural order, ignore case, trim and blank-line removal are correct; Éclair sorts next to E ✓
- Status line "9 lines → 8 (1 removed)" ✓. That's a good B-0187 example and covers part of B-0203 outcome 2.
- Copy Result shows **no toast** → B-0187.
- **Open check:** the input box reads empty after sorting. Either the output replaces the input in place (by design, but then the original is lost with no undo) or it's a bug. Needs an admin recheck: is there an Undo, or is the original shown anywhere? Until then, filed as a question in B-0203.

## video-speed-changer (L-266) — output verified (admin session)
- `v-2x.mp4` (43,486 B): duration **1.52 s** (from 3.0 s) ✓. H.264 320×240 + AAC mono.
- Audio FFT peak **439.8 Hz**, so the pitch is kept ✓ (the source was a 440 Hz tone).

## audio-compressor (L-267) — output verified, one finding (admin session)
- `compressed_a.mp3` (122,297 B): MP3, 44.1 kHz, **mono, 320 kbps**, 3.03 s; peak 440 Hz ✓
- **Finding (added to B-0205):** "Medium" produced a 320 kbps MP3, the highest MP3 bitrate. The 54% saving comes only from WAV→MP3, not from compression. Medium should pick a bitrate from the source (e.g. 128 kbps stereo / 64 kbps mono for voice), and the result should show format + bitrate + % (already in B-0205).

## csv-converter (L-259) — verified (admin session)
- `dash.csv`: `-cmd` → `'-cmd` (BOM, CRLF) ✓. Protection skips only numeric cells like -3, which matches OWASP practice.
- **B-0195 note softened:** the label should just say numbers like -3 are left as they are. Prefixing `+2` is fine.
- Grammar on the page: "1 columns" (same family as "1 rows" in B-0196).
