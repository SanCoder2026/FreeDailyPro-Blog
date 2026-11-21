Sent: 2026-11-21 13:20 ET

# FDP-62 scripts (run from /workspace/deep/tools-env with `env -u BROWSER node …`)

- **px62-live.js `<zero|quickbuy|left|perload|nodm|deny|stopcheck> [engine]`:**
  - Guest runs. `getDisplayMedia` is a canvas + 440 Hz stub in the test browser only.
  - Chromium uses `--use-fake-device-for-media-stream --use-fake-ui-for-media-stream`; Firefox uses fake-stream prefs.
  - Env TRIES, ANY=1, SUF.
- **px62-wk.js / px62-wk2.js:** WebKit crash isolation (site pages vs `enumerateDevices()` on example.com).
- **px62-scripts.js / px62-expand.js:** first load and expanded info sections.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **Safety:** no sign-in, payment or ad clicks. The scripts redact deviceId, OAuth parameters and the Stripe session.
