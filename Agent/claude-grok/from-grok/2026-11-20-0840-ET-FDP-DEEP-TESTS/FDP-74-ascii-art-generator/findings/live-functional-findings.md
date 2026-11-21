Sent: 2026-11-21 17:04 ET

# Live functional findings (FDP-74)

- Copy never counts: 30 copies (button + Ctrl+C, 0/10 and 10/10, Chromium + Firefox) → 0 `usage.log`, no dialog (owner question).
- 12 fonts correct against pyfiglet (+1 leading column on 5); width note and >80 warning right; emoji and other scripts refused cleanly; accents transliterated.
- P3: Centre blank line with trailing spaces; 60-character cut is silent; the note calls quotes and dashes "accented letters".
