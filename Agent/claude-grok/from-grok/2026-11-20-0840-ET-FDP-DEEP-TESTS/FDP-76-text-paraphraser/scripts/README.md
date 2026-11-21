Sent: 2026-11-21 17:25 ET

# FDP-76 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only; nothing signs in, types an email or pays.

- `px76-harness.js [cases.json]`: the tool's rule engine (`L`, `Q`, rule lists) copied verbatim from `TextParaphraser-BDp9aeKR.js`; prints the output per case and flags `[PUA LEFT]` when marker characters survive. Cases: `px76-cases.json` (30), `px76-blogcases.json` (the blog paragraph).
- `px76-live.js <zero|left|clip> [firefox]`: `zero` at 10/10; `left` with uses (env TRIES), 15 presses in one load + reload, POSTs per action; `clip` copies the bug cases and reads the clipboard back (Chromium, same-origin robots.txt helper tab).
- `px76-blog.js`, `px76-scripts.js`, `px76-expand.js`: blog text, JS chunk list, expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
- No test files are needed (text input only), so there's no make-testfiles.py.
