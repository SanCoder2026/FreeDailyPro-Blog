Sent: 2026-11-21 18:23 ET

# FDP-80 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only.

- `make-testfiles.py [dir]`: builds the beep test files (numpy + ffmpeg), including the 6 and 12 min WAVs left out of the zip.
- `analyze.py file…`: duration, codec, tags and beep onsets/pitch for any output.
- `px80-live.js <zero|left|cases> [firefox]` (env TRIES, ONLY, SUF): `zero`/`left` X01–X10 with POSTs, dialogs, downloads and the result player's bytes; `cases` formats, modes, fades, time inputs, errors, size limit.
- `px80-drive.js`: what "Open from Google Drive" opens (host only, params redacted). `px80-qb.js quickbuy`: Day Pass / Monthly, stops before typing.
- `px80-blog.js`, `px80-scripts.js`, `px80-expand.js`: blog text, JS chunks, expanded copy. `run-matrix.js config.json`: devices, locales, geo, axe.
