Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: live functional findings (guest, headless Playwright 1.65, 2026-11-21 01:27–01:45 EST)

Test files: synthetic, made by `testfiles/make-files.py` (T01 transparent PNG … T16 64 px PNG; HEIC via pillow-heif). Results: `json/cases-chromium.json` (C01–C32), `json/cases-firefox-*.json`, `json/gate.json`, `json/gate2.json`, `json/gate3.json`, `json/pairs.json`, `json/axe-loaded.json`. Saved result previews: `testfiles/outputs/`.

## Conversions (Chromium, all in the browser)
| Case | Input → output | Result |
|---|---|---|
| C01 | transparent PNG → JPEG (default target) | 800×600, transparent area white (fill picker shown first) PASS |
| C02 | same, Fill #ff0000 | corners red PASS |
| C03 | → WebP | alpha kept PASS |
| C04 | → GIF | transparency kept, 3 KB PASS |
| C05 | → BMP | 24-bit (fill), 1.4 MB; "325.7x larger … WebP is usually smaller" note PASS |
| C06 | → ICO | one .ico with 16/32/48 (default ticks; 64/128/256 offered) PASS |
| C07 | → TIFF | 32-bit uncompressed 1.9 MB; preview can't render TIFF (expected) PASS |
| C08 | JPEG with EXIF Orientation 6 + GPS → PNG (default target) | turned upright 1200×1600, no EXIF PASS |
| C09 | → JPEG, Keep camera/date/location | EXIF kept incl. **GPS**, Orientation reset to 1 PASS |
| C10 | → JPEG default | EXIF and GPS removed PASS (privacy default) |
| C11 | → JPEG, print resolution 150 | JFIF 150 dpi PASS |
| C12 | WebP → JPEG | PASS |
| C13 | animated WebP → PNG | note "This WebP is animated. Only its first frame is converted." PASS |
| C14 | AVIF → PNG (default) | PASS |
| C15/C16 | animated GIF (5 frames) | choice "First frame only / All 5 frames (ZIP)"; all → ZIP of 5 PNGs PASS |
| C17 | BMP → PNG | PASS |
| C18 | 2-page TIFF → JPEG | first page 400×300 PASS (as documented) |
| C19 | SVG 400×200 → PNG | 400×200 PASS |
| C20 | SVG with no size, `onload=alert` and `<script>` | 300×150 as documented; no script ran (no dialog) PASS |
| C21 | HEIC → JPEG (default) | 1024×768 in 160 ms PASS |
| C22 | text renamed .png | toast "could not be read as an image… Nothing was used from your trial." PASS |
| C23 | truncated JPEG (first 3 KB) | converted silently to an 800×600 PNG whose unreadable lower part is transparent; no "may be damaged" warning (P3) |
| C24 | 6000×4000 JPEG → WebP | 1.3 s, 2037 KB → 143 KB PASS |
| C25 | → JPEG width 1920 | 1920×1280 PASS |
| C26/C27 | 64 px → width 512, "Never make it bigger" on/off | 64×64 / 512×512 PASS |
| C28 | rotate 90 + mirror + black and white | 480×640 grey PASS |
| C29 | name "T15_photo été #1.png" | kept name, `.jpg` PASS |
| C30 | quality to minimum (40) | smaller file PASS |
| C31 | width "abc" | "Width must be a whole number from 1 to 16384.", Convert disabled PASS |
| C32 | AVIF output | option "AVIF (not available here)" disabled in Chromium and in Playwright Firefox; page says "use a current Chrome or Firefox desktop" (unverified in a real desktop browser) |

- Pair pages (`json/pairs.json`): png-to-ico, heic-to-png, gif-to-png, webp-to-jpg, jpg-to-webp, svg-to-png, png-to-jpg each preselect the target ("Drop a PNG image to convert to ICO"). PASS. (png-to-jpg accepts a WebP too — fine.)
- Batch (`json/gate.json`): 5 files incl. a non-image → "5 in, 4 out (1 skipped - see the list)", per-file lines with sizes, `bulk-processed-images.zip` with 4 JPEGs (accented name kept). Batch quality starts at **80 %**, single at 92 %; the FAQ says "starts at 92" (P3).
- Firefox (Playwright): C01, C14, C21 work the same.

## Privacy (PASS)
- No request carried image data in any case: only ad pings (2–9 KB) and `insight.hit`/`funnel.hit`; no third-party upload host. `useUploadApi` is bundled but no upload call was seen. SVG scripts did not run. Default output strips EXIF/GPS.

## Trial use and payment
- **Converting is free; Download is charged — but only once per page load.**
  - `gate.json` (01:36:46–01:38:04 EST, context loaded with `usageToday` 0): Convert 0 → 0; Download 0 → **1**; Download again 1 → 1; Save to Google Drive → Google sign-in popup (stopped); Save to my cloud storage → "Sign in with your email first… $4.99 per month, 1 GB" (stopped); GIF all-frames ZIP Download 1 → **1**; reload; batch of 5 → 1 → **2**.
  - `gate2.json` (01:39:53–01:40:20 EST): Download A 0 → **1**, then B and C (different images, after New) 1 → **1**; reload; GIF all-frames ZIP 1 → **2**, then SVG 2 → **2**.
  - `gate3.json` (01:45:00–01:45:18 EST): single Download 0 → 1, then a batch of 3 in the same page load 1 → **1**; reload; batch 1 → 2, then single Download 2 → **2**.
  - Code (`js/index-*.js` `xI`/`vI`, set `Kt`): after the first allowed use of a tool, every later use in that page load returns "allowed" without logging.
  - So with one trial use left a guest can convert and download any number of images (and batches of any size) until they reload. Not in the Nov 20 uncounted list → **P1 policy question**. Probably shared across tools that use the same hook (it explains the FDP-33 ZIP result) — unverified for other tools.
- **Result preview = the full output, also at 0.** The on-page preview `<img>` is a blob of the converted file: same bytes as the Download (sha256 `ebfb1788…` both, `gate.json`), full resolution (C24 6000×4000). At 0 remaining (C01, C02) the preview still shows; Download opens the cap dialog, but "Save image as…" on the preview gives the same file (not clicked; browser behaviour). P1 (gate leak).
- No "Created with FreeDailyPro.com" mark on any converted image (download = preview bytes), but the cap dialog says "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images" (P3 copy).
- At 0 (`gate.json` zero, 01:38–01:39 EST): Download and "Get a Day Pass to download" → cap dialog "Today's trial uses are done … downloading needs a pass… Monthly $4.99 … Day Pass $1" → Buy Day Pass → "Day Pass, $1 … Email | Continue to payment" (stopped, nothing typed). Batch Convert all at 0 → cap dialog, no ZIP. Quick Buy day → same email prompt; Quick Buy monthly → Stripe Checkout (session id redacted; stopped). 10 → 10.
- Trial uses spent by this test: 6 (three uses-left contexts × 2; display-only).

## Keyboard / a11y
- Drop zone reachable by Tab (28 stops), Enter opens the file chooser (PASS).
- Option checkboxes have proper labels (`label for`). The Quality slider has no accessible name (axe aria-input-field-name, serious). Both strip buttons named "Quick Buy". Text links in "Which tool should I use?" rely on colour (link-in-text-block).

## Print / Share
- Share copies only the tool URL (`json/share.json`). Print (`testfiles/outputs/print-preview.pdf`) shows the page; no dedicated print action (none promised).
