Sent: 2026-11-21 13:02 ET

# FDP-61 scripts (run from /workspace/deep/tools-env with `env -u BROWSER node …`; WebKit needs GIO_EXTRA_MODULES=…/giomods)

- **make61.py:** builds the synthetic test photos (PIL + numpy).
- **px61-live.js `<zero|quickbuy|left|leftB|idcard|perload|msgs> [engine]`:** guest runs. Env TRIES, ANY=1, SUF.
- **px61-orient.js:** EXIF 6 and not-an-image on Chromium, Firefox and WebKit.
- **px61-misc.js:** camera input, Drive (stops at Google sign-in), Share, handles, Edit as Excel.
- **px61-mobile.js:** iPhone 13 / Pixel 7 flow at the cap.
- **px61-scripts.js / px61-expand.js:** first load and expanded info sections.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **Safety:** no sign-in, payment or ad clicks. The scripts redact deviceId, OAuth parameters and the Stripe session.
