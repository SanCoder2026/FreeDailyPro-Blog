Sent: 2026-11-21 16:05 ET

# FDP-71 reproduce

1. **Player Download at 0:** guest Chrome window with 0 remaining → https://www.freedailypro.com/tool/audio-speed-changer → drop `testfiles/tone-10s-44k.wav` → 2x → Change Speed → in the "Listen to the result" player press ⋮ → Download. A 5.0 s WAV is saved; the counter stays at 10/10. The page's Download button opens the cap dialog. Compare with a paid `speed_2x_tone-10s-44k.wav`: same bytes.
2. **Per page load:** a window with uses left: Download (1 POST) → Download again → 2x → Change Speed → Download → New → MP3 0.5x → Download → New → M4A 1.25x +12 → Download: no further POST, even at 0 remaining. Reload → first Download charges again.
3. **Non-audio:** drop `not-audio.mp3` → 2x → Change Speed → ~75 s → toast with "Check the browser console (F12)".
