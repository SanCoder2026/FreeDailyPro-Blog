Sent: 2026-11-21 18:39 ET

# FDP-81 reproduce

1. **Per-page-load (P1):** guest window with uses left → https://www.freedailypro.com/tool/silence-remover → drop `testfiles/speech.wav` → Remove Silence → Download (+1, one `usage.log` POST) → Download again → New → drop `speech.mp3`, Shorten to 0.5 s → Remove Silence → Download → New → `speech.flac` → Download: counter unchanged. Reload → one more charge.
2. **Save at 0 (P1 by owner rule):** window at 10/10 → drop a file → "Preview the result" (no dialog) → player ⋮ → Download, or right-click → Save audio as → full WAV of the edit. Remove Silence → the result player saves the same bytes as the paid Download.
3. **Blog 0.15 s (P2):** Remove completely on `speech.wav` → `analyze.py` shows cut pauses of 0.02–0.03 s, not 0.3 s.
4. **Boundary (P3):** `many.wav` (1,100 × 0.5 s gaps) at defaults → "550 of 550 cut".
