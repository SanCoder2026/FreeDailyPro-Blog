Sent: 2026-11-21 14:42 ET

# FDP-66 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in or pays.

- `px66-live.js <zero|left|cases|hints> [chromium|firefox]`: `zero` loops fresh contexts until one is at the cap; `left` until uses are left (env TRIES). Clipboard set/read from a same-origin robots.txt tab; `window.print` stubbed. `cases` runs 22 UA inputs; `hints` presses "Use My Browser's User-Agent".
- `px66-scripts.js`, `px66-expand.js`: JS chunk list and expanded page copy.
- `run-matrix.js config.json`: devices, locales, geo, axe.
