Sent: 2026-11-21 15:54 ET

# FDP-70 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px70-live.js <zero|left|limits|fit|cases|quickbuy> [engine]`: `zero` finds a context at the cap; `left`/`limits` one with uses left (env TRIES; ~1 in 11–18 fresh contexts had uses on Nov 21); SUF adds a suffix. Every saved file is checked with Pillow (size, DPI). `zero` also reads the 300 px preview canvas in the page (test only). `fit` runs auto-fit on 3 photos × US/UK and screenshots the guide ovals.
- `px70-drive.js`: Open from Google Drive popup (closed). `px70-camera.js`: camera button with Chromium's fake device (native picker; nothing to capture headless).
- `make-testfiles.py`: downloads the two openly licensed portraits and derives the other test files (Pillow, curl).
- `px70-scripts.js`, `px70-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
