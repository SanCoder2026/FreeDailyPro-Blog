Sent: 2026-11-20 08:40 ET

# Test cases: FDP-19 Resize & Crop (rerun after any fix)

"Today" = observed 2026-11-19 16:21–16:35 EST in headless Chromium. Cases R01–R24 and K01–K05 are in `scripts/rc-cases.json`. Run `node scripts/rc-battery.js [IDs]`, then `python scripts/rc-inspect.py <live dir>`.

| ID | Input / action | Expected | Today |
|---|---|---|---|
| RC-01 | photo.jpg (EXIF 6, GPS) width 1200 | 1200×1600 upright; GPS removed | PASS |
| RC-02 | 50 % / 10 cm@300 / 4 in@300 | 2000 / 1181 / 1200 wide | PASS |
| RC-03 | Fill / Cover / Contain 1080² | exact 1080×1080 | PASS |
| RC-04 | Inside 1080² on 4:3 | file 1080×810 **and message says 1080×810** | **FAIL** (says 1080×1080) |
| RC-05 | Outside 1080² on 4:3 | file 1440×1080 and message matches | **FAIL** |
| RC-06 | tiny.png + Never enlarge, 500 | file 50×50 and message says not enlarged | **FAIL** (says 500×500) |
| RC-07 | tiny.png 500 | inline soft/blurry warning | PASS |
| RC-08 | alpha.png Contain | transparent padding | PASS |
| RC-09 | rotate 90 + mirror + B&W | 600×800 gray | PASS |
| RC-10 | webp / bmp / gif / tiff / svg / heic / avif | type per the FAQ | PARTIAL (BMP/GIF → PNG contradict the FAQ) |
| RC-11 | notimage.jpg | "could not be read as an image" | PASS |
| RC-12 | 108 MP JPEG → 2000 | opens, resizes | PASS |
| RC-13 | width 20000 / 1.5 | inline error, button off | PASS |
| RC-14 | Crop 1:1 click | centred largest square, Apply enabled | PASS |
| RC-15 | Crop typed X/Y/W/H (keyboard only) | exact crop | PASS |
| RC-16 | Crop + scale to width 500 | 500×500 | PASS |
| RC-17 | EXIF-rotated crop | from the upright image | PASS |
| RC-18 | Resize this crop → 540 | 540×960 | PASS |
| RC-19 | Firefox / WebKit resize + HEIC + 1:1 crop | works | PASS |
| RC-20 | At 0: Download → cap → Day Pass | email prompt (stop) | PASS |
| RC-21 | With uses: Download ×2, bytes, name, mark (`scripts/rc-reset.js`) | +1 once; same bytes; `resized_plain.jpg`; no mark (or as policy says) | **Pending: needs re-run after midnight UTC (7:00 PM ET)** |
| RC-22 | axe with a file in Resize | no critical | **FAIL** (label ×1) |
| RC-23 | Ratio state and result announcement | aria-pressed; live region; focus to result | **FAIL** |
| RC-24 | Copy/video consistency | formats, preview, ratios, video UI | **FAIL** |
