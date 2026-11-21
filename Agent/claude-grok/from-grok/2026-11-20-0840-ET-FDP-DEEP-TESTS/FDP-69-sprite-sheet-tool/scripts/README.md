Sent: 2026-11-21 15:35 ET

# FDP-69 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px69-live.js <zero|left|mixed|cases|quickbuy> [engine]`: `zero` finds a context at the cap; `left`/`mixed` one with uses left (env TRIES; ~1 in 25–40 fresh contexts had uses on Nov 21); SUF adds a suffix. `zero` also fetches the frame tile blobs in the page (stands in for "Save image as").
- `px69-ctx.js`: tile context menu / drag / pointer-events check after Split. `px69-drive.js`: Open from Google Drive popup (closed). `px69-probe.js`: counter probe.
- `make-testfiles.py`: generates the test PNGs (Pillow).
- `px69-scripts.js`, `px69-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
