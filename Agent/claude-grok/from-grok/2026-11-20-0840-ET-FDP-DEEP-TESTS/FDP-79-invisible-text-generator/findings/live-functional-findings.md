Sent: 2026-11-21 18:03 ET

# Live functional findings (FDP-79)

- Zero (Chromium 10/10) and left (Firefox 0/10): 7 copies each, 0 `usage.log` POSTs, no dialog (owner question).
- All 9 variants copy the right code points; 500 Line Breaks = 1,000 code points.
- Lost first click after clearing the box (layout shift when the note disappears): Chromium, Firefox, Pixel 7 tap. iPhone 14 tap copied.
- Clipboard refused → toast asks to select text by hand; nothing selectable (0 text nodes with the character).
- Test box reads code points correctly, including emoji as one.
