Sent: 2026-11-21 14:26 ET

# FDP-65 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in or pays.

- `px65-live.js <zero|left|cases> [chromium|firefox]`: `zero` loops fresh contexts until one is at the cap; `left` until uses are left (env TRIES). The clipboard is set/read from a same-origin robots.txt tab, so the tool's clipboard wrapper isn't involved.
- `px65-alpha.js`: 4/8-digit HEX alpha round trips, colour-picker check, Firefox copy at the cap.
- `px65-scripts.js`, `px65-expand.js`: JS chunk list and expanded page copy.
- `run-matrix.js config.json`: devices, locales, geo, axe.
