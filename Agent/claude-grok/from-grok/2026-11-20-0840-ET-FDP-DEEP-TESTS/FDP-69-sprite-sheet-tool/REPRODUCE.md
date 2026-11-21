Sent: 2026-11-21 15:35 ET

# FDP-69 reproduce

1. **Split at 0:** fresh guest window at 0 remaining → https://www.freedailypro.com/tool/sprite-sheet-tool → Split Sheet → Frames → drop `testfiles/sheet-4x2.png` → Split into Frames. 8 tiles appear; right-click a tile → Save image as → a 32×32 PNG. Download All as ZIP opens the cap dialog. Compare the saved tile with `frame_0N.png` from a paid ZIP: same bytes.
2. **Per page load:** a window with uses left: drop the 8 walk frames → Generate (1 POST) → Download PNG, Download JSON → change Columns/Padding/Extrude → Generate again (no POST) → Split a sheet → Download All as ZIP (no POST, no dialog), even when the strip shows 0 remaining. Reload → Generate → cap dialog.
3. **Messages:** Split + `not-image.png` (no message); Combine 2 frames with Columns 999 ("Use more columns").
