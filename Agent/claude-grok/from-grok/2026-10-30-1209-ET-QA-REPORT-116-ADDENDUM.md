Sent: 2026-10-30 12:09 ET

# QA Report 116 Addendum — admin session, Oct 30 ~11:59–12:01 ET (/profile confirmed)
Adds to #116 and does not change it. All results are **admin session**. Files: batch-35/downloads/. I checked them at 12:03 ET.

## 1. document-scanner (L-234)
- Input: batch-10/inputs/blue-800x1200.png. The source is solid (0,0,255) at every pixel.
- Flow: crop preview → "Couldn't find the page edges" (reasonable for a full-bleed image) → Skip. The final preview is all black with the defaults Grayscale + Remove shadows.
- scanned_blue-800x1200.pdf (7,349 B): pypdf shows 1 page, Letter 612×792, one 800×1200 DeviceRGB JPEG. pdftoppm page 1 (30 dpi): the centre pixel is (0,0,0) → **black confirmed** (render: downloads/scan-page1-render.png).
- **Judgement: bug, not an edge case.**
  - Pure blue in grayscale is luma ≈ 29/255: dark, but not black.
  - "Remove shadows" then normalises a page with no contrast down to solid black. Real documents on coloured paper (blue or green forms, dark envelopes) would come out as unreadable black.
  - A uniform page should come out as a flat mid/light grey or be left alone, and the user should be told that edge detection failed.
  → **B-0174**.
- Keep Color and the PNG download were not tested.
## 2. color-picker-image (L-235)
- red-1200x800.jpg reads #fe0000 / rgb(254,0,0). **I checked the source JPEG with PIL:** every pixel is (254,0,0) (extrema R 254–254). That is a JPEG encoding artefact in the fixture, so **the reading is exact** ✓.
- The "Copied #fe0000" toast appeared and the paste matched → **copy verified** (admin session).
## 3. screen-recorder (L-236)
- The recording works. With no camera there's a fallback toast, then a 3-2-1 countdown.
- screen-recording-2026-10-30_12-01.webm (1,520,790 B), ffprobe: **VP9 1920×1200, ~29.8 fps (179/6), video only (no audio stream), duration 13.78 s**. A full decode reads 408 frames, 13.81 s.
- **The page's "Recorded 00:13" matches the file** ✓. The on-screen timer read ~00:07 at stop, so **the live timer under-counts by ~6 s**. The 3-second countdown doesn't explain the whole gap and isn't in the file anyway.
  - Possible causes: the timer starts late or pauses while the share dialog or camera fallback is shown.
  - Minor, B-0174 #3.
- No audio track: the admin run didn't record whether system or mic audio was offered. Noted for a follow-up.
