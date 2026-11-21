Sent: 2026-11-21 17:36 ET

# FDP-77 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only; nothing signs in, types an email or pays.

- `px77-harness.js [cases.json]`: the tool's `dates-DoPZ1fRV.js` functions and its per-job / total / gap functions copied verbatim (renamed only where minified names collide). Cases: `px77-cases.json` (22), `px77-blogcases.json` (the blog's example).
- `px77-live.js <zero|left|cases> [firefox]`: `zero` at 10/10, `left` with uses (env TRIES); 8 actions (3 jobs, Copy summary, Ctrl+C, edit, untick, reload) with POSTs per action, clipboard read back in Chromium; `cases` enters every harness case live.
- `px77-blog.js`, `px77-scripts.js`, `px77-expand.js`: blog text, JS chunk list, expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
- No test files are needed (date input only), so there's no make-testfiles.py.
