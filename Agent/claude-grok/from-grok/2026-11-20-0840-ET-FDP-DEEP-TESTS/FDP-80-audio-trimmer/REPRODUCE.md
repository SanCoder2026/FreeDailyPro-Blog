Sent: 2026-11-21 18:23 ET

# FDP-80 reproduce

1. **Per-page-load (P1):** guest window with uses left → https://www.freedailypro.com/tool/audio-trimmer → drop any MP3 → Trim Audio → Download (+1, one `usage.log` POST) → change Start/End → Trim → Download → Remove selection → Remove Section → Download → New → drop a WAV → Trim → Download: counter unchanged. Reload → one more charge.
2. **Save at 0 (P1 by owner rule):** window at 10/10 → drop a file → Trim Audio (works, no dialog) → in "Listen to the result" open the player's ⋮ menu → Download (or right-click → Save audio as) → the trimmed file; the page's Download shows the cap dialog.
3. **Hundredths lost (P2):** drop `testfiles/beeps20.wav` → Start `3.25` Enter, End `7.5` Enter → summary "Keeping 0:04.3" → Trim Audio → result is 4.2 s; `python analyze.py` shows the first beep at 0.70 s (expected 0.75).
4. **50 MB (P2):** `python make-testfiles.py` → drop `big12min.wav` (63 MB) → size notice, Trim disabled, while the drop zone mentions 500 MB.
