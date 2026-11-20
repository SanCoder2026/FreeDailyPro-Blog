Sent: 2026-11-20 08:40 ET

# Live functional findings: Resize & Crop (headless Chromium unless noted)

- **Written:** 2026-11-19 16:37 EST (box `date`, ET). Runs took place 2026-11-19 16:21–16:35 EST.
- **Capture:** the result stays in memory until Download, so `rc-battery.js` records the blob from `canvas.toBlob` (init-script hook). Crop results come from the "Cropped result preview" image.
- **Inspection:** `scripts/rc-inspect.py` (Pillow): format, size, EXIF, GPS, DPI → `evidence/json/inspect.json`.
- **Contexts:** one fresh context per case; every context loaded at 10/10 used.

| Case | Input | Settings | Output (inspected) | UI said | Verdict |
|---|---|---|---|---|---|
| R01 | photo.jpg 4000×3000, EXIF orientation 6, GPS, 300 DPI | width 1200, lock on | JPEG 1200×1600 upright; **EXIF and GPS removed**; no DPI | "Original: 3000 x 4000px", "Resized to 1200x1600" | PASS (privacy plus) |
| R02 | plain.jpg 4000×3000 | 50 % of original | 2000×1500 | correct | PASS |
| R03 | plain.jpg | unlocked 1080×1080 Fill (default) | 1080×1080 stretched | correct | PASS (default stretches) |
| R04 | plain.jpg | Cover 1080×1080 | 1080×1080 cropped | correct | PASS |
| R05 | plain.jpg | Contain 1080×1080 | 1080×1080, white bars (JPEG) | correct | PASS |
| R06 | plain.jpg | **Inside** 1080×1080 | **1080×810** | "Preview at 1080 x 1080px", toast **"Resized to 1080x1080"** | **FAIL** (message) |
| R07 | plain.jpg | **Outside** 1080×1080 | **1440×1080** | toast **"Resized to 1080x1080"** | **FAIL** (message) |
| R08 | alpha.png 800×600 | Contain 1000×1000 | PNG RGBA, transparent bars | correct | PASS |
| R09 | tiny.png 50×50 | width 500 + **Never make it bigger** | **50×50** | "Preview at 500 x 500px", toast **"Resized to 500x500"** | **FAIL** (message) |
| R10 | tiny.png | width 500 | 500×500 | inline "Enlarging an image more than twice its size makes it look soft or blurry." | PASS |
| R11 | plain.jpg | rotate 90 + mirror + B&W, width 600 | 600×800 grayscale | correct | PASS |
| R12 | img.webp | width 600 | WebP 600×400 | correct | PASS |
| R13 | img.bmp | width 320 | **PNG** 320×240 (download name .png) | — | PASS; FAQ says BMP stays BMP |
| R14 | anim.gif (6 frames) | width 150 | **PNG**, 1 frame | — | PASS; FAQ says GIF stays GIF (blog correctly says PNG) |
| R15 | img.tiff | width 500 | PNG 500×500 | — | PASS |
| R16 | vector.svg 400×300 | width 800 | PNG 800×600, sharp | — | PASS |
| R17 | notimage.jpg | — | toast `"notimage.jpg" could not be read as an image. The file may be damaged or not a picture.` | — | PASS |
| R18 | huge108mp.jpg 12000×9000 | width 2000 | 2000×1500 | — | PASS (opens a 108 MP input) |
| R19 | plain.jpg | width 20000 | inline "Width can be at most 16,384 px", button disabled | — | PASS |
| R20 | plain.jpg | width 1.5 | inline "Width must be a whole number of pixels", button disabled | — | PASS |
| R21 | plain.jpg | 10 cm at 300 DPI | 1181×886, **no DPI tag in the file** | — | PASS (copy says so) |
| R22 | plain.jpg | 4 in at 300 DPI | 1200×900, no DPI tag | — | PASS |
| R23 | photo.heic 2000×1500 | width 1000 | JPEG 1000×750 | — | PASS |
| R24 | img.avif | width 600 | PNG 600×400 | — | PASS (AVIF → PNG not documented) |
| K01 | plain.jpg | 1:1, typed X100 Y200 1200×1200 | JPEG 1200×1200 | "Cropped to 1200x1200" | PASS |
| K02 | plain.jpg | 1:1 2000×2000 + scale to 500 | 500×500 | correct | PASS |
| K03 | photo.jpg (EXIF-rotated) | Freeform 0,0,1500,1000 | 1500×1000 from the upright top-left | correct | PASS |
| K04 | plain.jpg | 9:16 900×1600 → "Resize this crop" → 540 | 900×1600, then 540×960; Original reads 900×1600 after the hand-off | correct | PASS |
| K05 | alpha.png | 16:9 800×450 | PNG RGBA 800×450 | correct | PASS |

## Gate, keyboard, a11y (`gate-kbd.json`, 16:31–16:33 EST)

- **Count and charging:**
  - Start 10 used (0 remaining).
  - Resize and Crop are never charged (about 35 runs, count stayed 10).
  - Row text: "0 remaining today Get a Day Pass to download".
- **Download → cap dialog** "Today's trial uses are done… Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images" → "Buy Day Pass — $1" → email prompt "Day Pass, $1… Continue to payment". Stopped there; nothing typed.
- **Drive at 0:** the same cap dialog. Cloud storage: "$4.99 per month, 1 GB… Sign in with your email first". Stopped.
- **Crop before any drag:** the X/Y/Width/Height boxes show the full image (0, 0, 4000, 3000), with Apply Crop disabled and the hint "Drag on the image to select the area to keep."
- **1:1 preset:** draws the largest centred square (500, 0, 3000, 3000), as the blog says, and enables Apply Crop.
- **Keyboard-only crop works:** type X/Y/W/H, then Enter on Apply Crop → "Cropped to 3000x3000".
- **Accessibility gaps:**
  - The 9 ratio buttons have no `aria-pressed`.
  - axe on Resize: **label (critical) ×1** (`.w-24`, the unlabeled "percent / cm / inch" value box).
  - Two elements are named "Unit".
  - The result is announced only by a toast; focus goes to BODY.
  - Result image alt: "Cropped result preview".
- **Result row:** Download, Save to Google Drive, Save to my cloud storage, Resize this crop, New. **No share-result, copy or print button.** tools.csv lists share/save/print; print is an unverified absence beyond this row.
- **Next steps:** "NEXT STEP: PREMIUM APPLICATION — Document Scanner" and "Next: Flip & Rotate" (rotate is already built in).
- **Phones (Chromium emulation, crop mode):**
  - Apply Crop sits at y≈1100 (iPhone SE viewport 584, Pixel 7 839), so a scroll is needed.
  - A CDP touch-drag moved the selection on Pixel 7 (X 500 → 1000) but not on iPhone SE. The image was probably partly off-screen; inconclusive.

## Browsers (`browsers.json`)

- Firefox 1440 and WebKit 1440 both:
  - resize to 1200×900
  - open the HEIC file (2000×1500)
  - crop with the 1:1 preset (1500×1500)
- No crash: the WebKit harness limit seen with audio/video does not affect images.
