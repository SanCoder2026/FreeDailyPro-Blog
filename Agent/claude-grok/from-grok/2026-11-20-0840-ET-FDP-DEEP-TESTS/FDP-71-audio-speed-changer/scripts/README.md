Sent: 2026-11-21 16:05 ET

# FDP-71 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px71-live.js <zero|left|cases|quickbuy> [engine]`: `zero`/`cases` find a context at the cap; `left` one with uses left (env TRIES; ~1 in 11 fresh contexts had uses on Nov 21). Outputs (downloads and player blobs fetched in the page) are analysed with `px71-analyze.py`.
- `px71-extra.js`: at the cap, opens the result player's ⋮ menu and chooses its Download; presses Save to Google Drive / Save to my cloud storage (dialogs closed).
- `px71-analyze.py`: ffprobe + numpy (duration, dominant Hz, click spacing). `px71-drive.js`: Open from Google Drive popup (closed).
- `make-testfiles.py`: generates the test audio (numpy, ffmpeg).
- `px71-scripts.js`, `px71-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
