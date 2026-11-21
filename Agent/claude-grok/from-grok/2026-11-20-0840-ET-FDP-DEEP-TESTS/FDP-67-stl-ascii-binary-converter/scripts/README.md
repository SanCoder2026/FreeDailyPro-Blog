Sent: 2026-11-21 14:59 ET

# FDP-67 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px67-live.js <zero|left|batch|perload|extra|cases|quickbuy> [engine]`: `zero` finds a context at the cap; `left`/`batch`/`perload` find one with uses left (env TRIES); `extra` (CAP=1 for the cap) clicks the Drive/cloud buttons and closes any popup; `cases` = validation at any count (ANY=1); `quickbuy` stops at the email dialog / Stripe page. SUF adds a suffix to output names.
- `make-testfiles.py`: generates the test STLs (numpy).
- `px67-scripts.js`, `px67-expand.js`: JS chunk list and expanded page copy; `px67-mesh-peek.js`: mesh-3d-converter copy for the C46 check.
- `run-matrix.js config.json`: devices, locales, geo, axe.
