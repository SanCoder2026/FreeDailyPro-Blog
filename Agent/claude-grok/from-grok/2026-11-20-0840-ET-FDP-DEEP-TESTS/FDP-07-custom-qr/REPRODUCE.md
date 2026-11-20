Sent: 2026-11-20 08:40 ET

# FDP-07 QR Code Generator with Logo (custom-qr): reproduce

- **Written:** 2026-11-19 12:36:49 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks. Stop at the cap dialog.
  - Logos: `evidence/testfiles/`.
  - To decode without downloading, run `document.querySelector('main canvas').toDataURL()` in DevTools, save the PNG, then run `python3 scripts/decode-previews.py <dir>`.
- **Automation:** `cd /workspace/deep/tools-env`. The scripts write to `/workspace/deep/07-custom-qr/live/`.

## R-01: downloads continue at 0 remaining on the same page load
1. Use a fresh profile that shows "2 remaining today".
2. Download PNG. Then, without reloading, change the content and Download PNG, then SVG, then PNG.
3. **Seen 2026-11-19 12:15–12:18 EST:**
   - E: 2 → 1, then 1 → 1 → 1 (three files saved).
   - C: 2 → 0 after one PNG, then a vCard PNG still downloaded at 0.
   - F: ZIP 2 → 0, then PNG 2000 downloaded at 0.
4. Reload at 0 and Download → the cap dialog appears (H, 12:19–12:22 EST).
5. Script: `node scripts/cq-battery.js E_count_trace_4_downloads_new_content,F_zip_2000_then_png2000`. Evidence: `json/battery-1795108682122.json`, `battery-1795108740865.json`, `battery-1795108962459.json`.

## R-02: one click costs 1 or 2; the starting allowance varies
- C (text PNG), D (SVG) and F (ZIP) went 2 → 0 on a single click; A, B and E went 2 → 1.
- The matrix and geo fresh contexts loaded at 0 (10) or 2 (6). See `json/matrix-results.json` (aboveFold.trialText, geo.trial).

## R-03: trial vector PDF does not decode
1. Download vector PDF (default 50 mm).
2. Run `pdftoppm -r 600 -png custom-qr.pdf out`, then decode with zxing-cpp. Nothing decodes. It also fails after adding a white border.
3. See `pdf-renders/A3_…-1.png`: the badge covers the bottom-right modules. B1 (frame + logo) also covers the frame text.
4. Compare with the PNG/SVG of the same code: they decode and have no mark.

## R-04: long text crashes the page
1. Text tab → paste 2,400 characters.
2. The whole page shows "An unexpected error occurred… Reload page"; console "code length overflow (19220>18672)". 2,300 characters work.
3. Script: `node scripts/cq-long.js`. Evidence: `screens/live/x-long-2400-crash.png`, `json/long-frame.json`.

## R-05: Unicode corrupted
1. Text tab → "Line 1⏎Grüße 日本 👍".
2. Decode the preview → "Line 1⏎Grüße å, =M". The downloaded PNG (C1) gives the same.
3. qr-generator encodes the same text correctly.

## R-06: PDF frame non-ASCII → "?"
Frame text "Escanéame 扫码" → the PDF has "Escan?ame ??" (`pdftotext`). Code: `replace(/[^\x20-\x7E]/g,"?")`.

## R-07: copy denies features
Details → "When not to use it": "Skip it for Wi-Fi join codes, contact cards, e-mail or text-message shortcuts…". The WiFi, Contact, Email and SMS tabs all decode correctly (`previews/C18…C22`).

## R-08: quiet zone
`inspect-qr-downloads.py` reports a margin of 50 px on 1000 px PNGs, about 36 px modules for the default URL, so about 1.4 modules. Code: `margin: Math.round(size*.04)`.

## R-09: vCard ";"
Contact: Company "Smith; Jones & Co, LLC" → decodes `ORG:Smith; Jones & Co\, LLC` (";" is unescaped).

## R-10: phone layout and a11y
- `node scripts/cq-kbd.js`: Pixel 7 Download y≈1029, canvas y≈1342.
- axe: button-name ×4 and label ×1 critical.
- The tabs have no aria-controls, and arrow keys don't move the selection. Evidence: `json/kbd.json`.

## R-11: bulk ZIP capped at 1000 px
Choose 2000 px, paste 3 lines, and download the ZIP → three 1000×1000 PNGs (`downloads/zip-extracted/`). Code: `Math.min(Number(size),1e3)`.
