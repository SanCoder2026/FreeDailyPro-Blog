Sent: 2026-11-21 18:56 ET

# FDP-82 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only.

- `make-testfiles.py [dir]`: beep clips (numpy + ffmpeg + Pillow, seed 82).
- `analyze.py file…`: beep times + pitch per channel, rate, channels, codec, bitrate, streams.
- `px82-live.js <zero|left|cases> [firefox]` (env TRIES, ONLY, SUF): `zero`/`left` X01–X09 with POSTs, dialogs, downloads and player bytes; `cases` 33 sets/settings.
- `px82-fmtdup.js`: format menu options, M4A/WAV merges, duplicate toasts. `px82-big.js`: 2 × 30 MB guest limit.
- `px82-drive.js`, `px82-qb.js quickbuy`: Drive popup host (params redacted); Day Pass / Monthly, stop before typing.
- `px82-blog.js`, `px82-scripts.js`, `px82-expand.js`, `run-matrix.js config.json`.
