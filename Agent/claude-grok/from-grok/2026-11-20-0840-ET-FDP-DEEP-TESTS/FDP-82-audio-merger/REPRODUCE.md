Sent: 2026-11-21 18:56 ET

# FDP-82 reproduce

Build inputs: `python3 scripts/make-testfiles.py testfiles` (or use `evidence/testfiles/`).

1. **Per-page-load (P1):** guest window with uses left → https://www.freedailypro.com/tool/audio-merger → add `a.wav` + `b.mp3` → Merge Audio → Download (+1, one `usage.log` POST) → Download again → New → `b.mp3` + `a.wav`, Gap 1 s → Merge → Download → New → `a.wav`, `b.flac`, `short.wav` → Merge → Download: counter unchanged. Reload → one more charge, next set free.
2. **Save at 0 (P1 by owner rule):** window at 10/10 → add two clips → Merge Audio (no dialog) → "Listen to the result" ⋮ → Download, or right-click → Save audio as → same bytes as the paid Download.
3. **Bitrate (P2):** `cover.mp3` (128 kbps + 1.4 MB picture) first, `a.wav` second, Same as first file → Merge → `ffprobe` shows 320 kbps.
4. **Size copy (P2):** two 30 MB WAVs (`px82-big.js` makes the test; files from `ffmpeg -f lavfi -i sine -t 340`) → notice "a file over 50.0 MB (57.2 MB)", Merge disabled; drop zone says 500 MB.
