Sent: 2026-11-21 14:26 ET

# FDP-65: reproduce

All guest, fresh browser contexts. Times EST.

1. **No trial use (owner question):** `TRIES=20 px65-live.js zero` (context at 10/10): type `#ff6600`, Copy HEX/RGB/OKLCH → "Copied", clipboard set, no dialog; click the HEX row, Ctrl+A, Ctrl+C → clipboard set. `TRIES=40 px65-live.js left`: no `usage.log` POST at any step, counter 0/10.
2. **Alpha:** enter `#ff6600aa` → HEX row `#ff6600ab`; `#ff660001` → `#ff660000`; `#ff6600fe` → `#ff6600`.
3. **oklch:** enter `oklch(70% 0.2 50)` → accepted with the gamut note (Limitations say it's rejected).
