Sent: 2026-11-20 08:40 ET

# FDP-06 QR Code Generator: reproduce

- **Written:** 2026-11-19 12:05:23 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks.
  - Logos: `evidence/testfiles/` or `python3 scripts/make-testfiles.py <dir>`.
  - To decode without downloading, run `canvas.toDataURL()` in DevTools on `main canvas`, save the PNG, then run `python3 scripts/decode-previews.py <dir>` (pip: zxing-cpp, opencv-python-headless, pillow).
- **Automation:** `cd /workspace/deep/tools-env`. The scripts write to `/workspace/deep/06-qr-generator/live/`.

## R-01: fresh contexts load at 0 remaining

1. Open the tool in several fresh profiles, or run `node scripts/qr-probe.js`.
2. Read the strip and localStorage `fdp-usage-v1`.
3. **Seen 2026-11-19 11:49–12:01 EST:** 22/22 at 0 (`usageToday 10`, `allowed false`). See `json/probe.json`, `kbd.json`, `matrix-results.json`.
4. Display-only evidence; verify server-side.

## R-02: copy denies WiFi / vCard / SVG

1. Expand "Details: when to use it, limits, privacy" → "When not to use it". It says "this tool encodes plain text and URLs only, not those specialized formats" and "this tool's PNG output is the wrong format".
2. Open the WiFi tab and fill in an SSID and password. Decoding the preview gives `WIFI:T:WPA;S:…;P:…;;`.
3. Do the same on the Contact tab: decoding gives BEGIN:VCARD. A "Download SVG" button is present.

## R-03: vCard semicolon

1. Open the Contact tab. Enter First name José and Company "Smith; Jones & Co, LLC".
2. Decoding gives `ORG:Smith; Jones & Co\, LLC`. Expected: `ORG:Smith\; Jones & Co\, LLC`.
3. **Code:** qrHelpers `p(e)` has `.replace(/;/g,";")`.

## R-04: logo stretched

1. Use the Link tab. Upload `logo_wide_800x200_circle.png`.
2. The red circle shows as a tall ellipse (15×54 px in the 300 px preview). See `screens/live/x-Q31_logo_wide.png`.
3. Script: `node scripts/qr-logo-aspect.js`.
4. **Code:** `drawImage(m,w,R,h,h)`.

## R-05: unreadable logo accepted silently

Upload `text_renamed.png`. You get "Logo added. Error correction raised automatically…" and EC H, but no logo and no error.

## R-06: Pro vs Premium overlap

1. Compare the Pro title ("…Instant, With Logo") with /tool/custom-qr's ("QR Code Generator with Logo - Custom Colors and Shapes").
2. The Pro tool's "Next step" card says "Put your logo in the middle…", while the Pro tool already has "Logo (optional)".

## R-07: locales

1. Run `curl -s https://www.freedailypro.com/es/tool/qr-generator | grep -o '<title>.*</title>'`. It shows "Generador de códigos QR gratis…".
2. For /pt …/id, the title and client-rendered H1 are English. /ar returns 404.
3. Evidence: `html/tool-*.html`, `screens/locales/`.

## R-08: mark disclosure

1. Click Download PNG at 0. The dialog says passes remove "the 'Created with FreeDailyPro.com' mark from your PDFs and images".
2. Nothing near the Download buttons mentions it.
3. Whether QR downloads are actually marked: **re-run** (R-11).

## R-09: phone layout

On Pixel 7 the Download PNG button is at y=869 and the canvas at y=1094 (viewport 839). On iPhone SE, scrollWidth is 329. See `json/kbd.json`, `json/matrix-results.json`.

## R-10: a11y

1. axe on main: button-name critical ×2 (select triggers), label critical ×1 (logo input).
2. The canvas has no aria-label.
3. ArrowRight on the Link tab doesn't move.
4. Script: `node scripts/qr-kbd.js`.

## R-11: downloads (needs re-run after midnight UTC)

1. After 7:00 PM ET, run `node scripts/qr-battery.js 6`.
2. Then run `python3 scripts/inspect-qr-downloads.py /workspace/deep/06-qr-generator/live/downloads`.
3. Check QR-27…QR-35.
