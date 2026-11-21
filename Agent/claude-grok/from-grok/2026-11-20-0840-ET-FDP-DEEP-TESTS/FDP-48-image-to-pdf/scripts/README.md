Sent: 2026-11-21 07:23 ET

# Scripts (Playwright 1.65, Node 24; run with `env -u BROWSER node`; WebKit needs GIO_EXTRA_MODULES)

- **ip-expand.js / ip-scripts.js:** page text with details expanded, JSON-LD, links; JS chunk capture.
- **ip-live.js `<zero|left|subset|gps> [engine]`:**
  - **zero:** at the cap.
  - **left:** finds a context with uses left (TRIES env, about 1 in 25) and runs L01–L14.
  - **subset:** S01–S04 for firefox/webkit.
  - **gps:** G01/G02.
  - Toasts are polled from `[data-sonner-toast]`.
- **ip-pairs.js:** pair landing pages.
- **ip-preview.js:** Preview first page at 0.
- **ip-wk.js / ip-wk2.js:** WebKit crash isolation.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **make-files.py:** P16–P24 and R01–R07.
  - P01–P15 are reused from FDP-34.
  - **P25_gps_orient1.jpg** was made inline with Pillow: a JPEG with GPS 40°44'54.36"N 73°59'8.5"W, Make "TestCam", Model "X", orientation 1.
- **Reading EXIF back:** `pdfimages -j out.pdf x && python -c "from PIL import Image;e=Image.open('x-000.jpg').getexif();print(e.get(271),e.get_ifd(0x8825))"`
- No sign-in, no payment and no ad clicks in any script. The scripts redact deviceId and OAuth params.
