Sent: 2026-11-21 18:39 ET

# FDP-81 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only.

- `make-testfiles.py [dir]`: tone-burst test files (numpy + ffmpeg), including many.wav (left out of the zip).
- `analyze.py file…`: bursts, gaps, lead/trail, rate, channels, codec.
- `px81-live.js <zero|left|cases> [firefox]` (env TRIES, ONLY, SUF): `zero`/`left` X01–X10 with POSTs, dialogs, downloads and player bytes; `cases` 23 settings/files.
- `px81-drive.js`, `px81-qb.js quickbuy`: Drive popup host (params redacted); Day Pass / Monthly, stop before typing.
- `px81-blog.js`, `px81-scripts.js`, `px81-expand.js`, `run-matrix.js config.json`.
