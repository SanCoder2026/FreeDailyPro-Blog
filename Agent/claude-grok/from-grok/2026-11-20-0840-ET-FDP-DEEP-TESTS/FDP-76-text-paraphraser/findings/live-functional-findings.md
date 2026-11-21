Sent: 2026-11-21 17:25 ET

# Live functional findings (FDP-76)

- Zero (Chromium, 10/10): Paraphrase "In order to start, let me know if you can help right away." → "To start, please tell me if you can assist immediately." (4 marks); no-change and French notes; Rewrite again; Copy → clipboard has the text. 0 POSTs, no dialog.
- Left (Firefox, 0/10, try 6 of 30): 15 Paraphrase presses on 10 texts + reload → counter stays 0/10, 0 POSTs. Live outputs = harness outputs for every case.
- Clip (Chromium): "Don't forget to call me." Medium → clipboard contains U+E003; tooltip "Original: RememberDon't forget"; restore → "RememberDon't forget to call me." with 4 marker chars. Strong openers → clipboard has U+E000 U+E001 U+E002 U+E003 U+E003; tooltips "However", "So", "As wellAlso".
- Restore on a clean case works (4 → 3 marks).
