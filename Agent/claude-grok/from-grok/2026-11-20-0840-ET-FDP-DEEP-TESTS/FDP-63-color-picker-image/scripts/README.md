Sent: 2026-11-21 13:37 ET

# FDP-63 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in or pays.

- `make63.py`: builds the test images (known pixels) into testfiles/.
- `px63-live.js <zero|left|cases|kbd|quickbuy> [chromium|firefox]`: main runs. `left` loops fresh contexts (env TRIES) until one has uses left. Writes live/*.json and cases/*.png.
- `px63-debug.js`: mapping on 4000×3000 + keyboard nudge across a colour edge (canvas scrolled into view).
- `px63-extra.js <chromium|firefox>`: non-image upload, alpha pick, Firefox copy at the cap.
- `px63-drive.js`: clicks "Open from Google Drive" and stops at whatever opens (records host only).
- `px63-camera.js`, `px63-cam2.js`: camera button (fake device; file chooser check).
- `px63-touch.js`: tap-to-pick on Pixel 7 / iPhone 14 Pro Max.
- `px63-scripts.js`, `px63-expand.js`: JS chunk list and expanded page copy.
- `run-matrix.js config.json`: devices, locales, geo, axe.
