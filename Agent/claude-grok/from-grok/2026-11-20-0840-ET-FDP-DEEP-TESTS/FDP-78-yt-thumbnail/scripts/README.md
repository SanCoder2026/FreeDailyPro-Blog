Sent: 2026-11-21 17:50 ET

# FDP-78 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only.

- `px78-live.js <zero|left|parse|resubmit> [firefox]`: `zero` at 10/10; `left` searches for a context with uses (env TRIES) and runs X01–X11 with POSTs, downloads and dialogs per action; `parse` P01–P25; `resubmit` S01–S04.
- `px78-qb.js quickbuy`: a copy of the #75 runner (only `quickbuy` mode used here): opens Day Pass and Monthly, stops before typing.
- `px78-blog.js`, `px78-scripts.js`, `px78-expand.js`: blog text, JS chunk list, expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
- No test files are needed (URL input only), so there's no make-testfiles.py.
