Sent: 2026-11-21 13:37 ET

# Live functional findings (FDP-63)

- **Charge point:** first copy per page load (`usage.log` POST). Upload/pick/palette/magnifier are free. Further copies in the same load (other formats, palette, a second image) are free; reload charges again. **P1 per-page-load.** (left.json, left-firefox.json)
- **At the cap:** values visible and selectable; copy → cap dialog, no clipboard write. **Owner question** (results visible at 0).
- **Accuracy:** exact on PNG, ±2 on JPEG q60, EXIF orientation respected, 1×1 and 4000×3000 mapped correctly. Alpha ignored. Non-image silent.
- **Keyboard and touch:** arrows 1 px / Shift 10 px; tap works on Pixel 7 and iPhone 14 (WebKit).
- **Drive:** Google sign-in popup (untested). **Camera:** file input with `capture`, desktop file chooser.
- **Firefox:** same behaviour; first copy jumped 0→10 (server pooling).
