Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: test cases

- **URL:** https://www.freedailypro.com/tool/convert-image, guest.
- **Inputs:** `evidence/testfiles/` (`make-files.py` recreates them; the 2 MB T14 is not shipped).
- **"Live"** = 2026-11-21 01:28–01:45 EST. Scripts: `cim-live.js`, `cim-pairs.js`, `cim-gate.js`, `cim-gate2.js`, `cim-gate3.js`, `cim-axe-loaded.js`, `cim-share.js`, `cim-misc.js`, `run-matrix.js`.

| ID | Step | Expected | Live |
|---|---|---|---|
| CI-01 | C01: T01_logo_transparent.png → default (JPEG)  | JPEG, white fill | PASS (800×600 image/jpeg) |
| CI-02 | C02: T01_logo_transparent.png → JPEG fill | red fill | PASS (800×600 image/jpeg) |
| CI-03 | C03: T01_logo_transparent.png → WebP  | WebP keeps alpha | PASS (800×600 image/webp) |
| CI-04 | C04: T01_logo_transparent.png → GIF  | GIF keeps transparency | PASS (800×600 image/gif) |
| CI-05 | C05: T01_logo_transparent.png → BMP  | 24-bit BMP | PASS (800×600 image/bmp) |
| CI-06 | C06: T01_logo_transparent.png → ICO  | ICO 16/32/48 | PASS (48×48 image/x-icon) |
| CI-07 | C07: T01_logo_transparent.png → TIFF  | TIFF | PASS (0×0 image/tiff) |
| CI-08 | C08: T02_photo_exif_gps_orient6.jpg → default (PNG)  | upright PNG, no EXIF | PASS (1200×1600 image/png) |
| CI-09 | C09: T02_photo_exif_gps_orient6.jpg → JPEG keep | EXIF+GPS kept | PASS (1200×1600 image/jpeg) |
| CI-10 | C10: T02_photo_exif_gps_orient6.jpg → JPEG  | EXIF/GPS removed | PASS (1200×1600 image/jpeg) |
| CI-11 | C11: T02_photo_exif_gps_orient6.jpg → JPEG dpi | 150 dpi | PASS (1200×1600 image/jpeg) |
| CI-12 | C12: T03_lossy.webp → default (JPEG)  | JPEG | PASS (640×480 image/jpeg) |
| CI-13 | C13: T04_animated.webp → PNG  | first frame + note | PASS (320×240 image/png) |
| CI-14 | C14: T05_photo.avif → default (PNG)  | PNG | PASS (640×480 image/png) |
| CI-15 | C15: T06_animated_5f.gif → default (PNG)  | first/all choice | PASS (200×200 image/png) |
| CI-16 | C16: T06_animated_5f.gif → PNG allFrames | 5-frame ZIP | PASS (5 frames saved as separate PNG images in one ZIP (188 KB).) |
| CI-17 | C17: T07_old.bmp → default (PNG)  | PNG | PASS (300×200 image/png) |
| CI-18 | C18: T08_2page.tiff → default (JPEG)  | first page | PASS (400×300 image/jpeg) |
| CI-19 | C19: T09_sized.svg → default (PNG)  | 400x200 | PASS (400×200 image/png) |
| CI-20 | C20: T10_nosize_script.svg → PNG  | 300x150, no script | PASS (300×150 image/png) |
| CI-21 | C21: T11_iphone.heic → default (JPEG)  | JPEG | PASS (1024×768 image/jpeg) |
| CI-22 | C22: T12_notimage.png → default (None)  | clear error, no use | PASS ("T12_notimage.png" could not be read as an image. The file may be dama) |
| CI-23 | C23: T13_truncated.jpg → default (PNG)  | damaged warning | PARTIAL (silent, transparent gap) (800×600 image/png) |
| CI-24 | C24: T14_big_6000x4000.jpg → WebP  | fast WebP | PASS (6000×4000 image/webp) |
| CI-25 | C25: T14_big_6000x4000.jpg → JPEG w | 1920x1280 | PASS (1920×1280 image/jpeg) |
| CI-26 | C26: T16_square_64.png → PNG w, noEnlarge | stays 64 | PASS (64×64 image/png) |
| CI-27 | C27: T16_square_64.png → PNG w | 512 | PASS (512×512 image/png) |
| CI-28 | C28: T03_lossy.webp → PNG rotate, gray, flop | 480x640 grey mirrored | PASS (480×640 image/png) |
| CI-29 | C29: T15_photo été #1.png → JPEG  | name kept | PASS (500×500 image/jpeg) |
| CI-30 | C30: T01_logo_transparent.png → JPEG quality | smaller | PASS (800×600 image/jpeg) |
| CI-31 | C31: T14_big_6000x4000.jpg → JPEG w | validation | PASS (Width must be a whole number from 1 to 16384.) |
| CI-32 | C32: T01_logo_transparent.png → AVIF  | AVIF output | Unavailable (disabled in Chromium/Firefox) (800×600 image/jpeg) |
| CI-33 | Pair pages ×7 | target preselected | PASS |
| CI-34 | Batch 5 files incl. non-image | ZIP of 4 + skip list | PASS |
| CI-35 | Uses left: Convert | uncounted | PASS |
| CI-36 | Uses left: first Download | −1 | PASS (0→1) |
| CI-37 | Same page: Download of other images / frames ZIP / batch | per policy | **Policy question** (no charge) |
| CI-38 | Batch first after reload | −1 per batch | PASS (1→2) |
| CI-39 | At 0: Download / Convert all | cap dialog → Day Pass email | PASS (stopped) |
| CI-40 | At 0: preview | not the full file | **FAIL** (full output) |
| CI-41 | Quick Buy day / monthly | email prompt / Stripe | PASS (stopped) |
| CI-42 | Save to Google Drive / my cloud storage | — | **Untested: sign-in** |
| CI-43 | Keyboard: Tab to drop zone, Enter | file chooser | PASS |
| CI-44 | Share | plain URL | PASS |
| CI-45 | Firefox C01/C14/C21 | same as Chromium | PASS |
| CI-46 | Matrix + axe | no overflow, labelled | PARTIAL |
