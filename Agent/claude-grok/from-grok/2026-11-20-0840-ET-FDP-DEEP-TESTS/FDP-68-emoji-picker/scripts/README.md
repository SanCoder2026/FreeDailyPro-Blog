Sent: 2026-11-21 15:18 ET

# FDP-68 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in or pays.

- `px68-live.js <zero|left|cases|tones> [engine]`: `zero` loops fresh contexts until one is at the cap; `left` until uses are left (env TRIES). Clipboard set/read from a same-origin robots.txt tab.
- `px68-blogq.js`: the blog's search-count claims. `px68-net.js`: requests sent by one copy. `px68-tone-shot.js`: tone screenshots.
- `px68-scripts.js`, `px68-expand.js`: JS chunk list and expanded page copy.
- `run-matrix.js config.json`: devices, locales, geo, axe.
- Tone check on the data file (node): for each emoji with 25 skins, test whether `skins[tone-1]` has only that tone's modifier (see REPORT P2).
