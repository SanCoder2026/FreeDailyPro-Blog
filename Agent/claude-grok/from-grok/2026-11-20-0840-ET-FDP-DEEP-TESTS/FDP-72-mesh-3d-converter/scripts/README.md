Sent: 2026-11-21 16:17 ET

# FDP-72 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px72-live.js <zero|left|cases|quickbuy> [engine]`: `zero`/`cases` find a context at the cap; `left` one with uses left (env TRIES; ~1 in 20 fresh contexts had uses on Nov 21). Downloads are analysed with `px72-analyze.py` (trimesh; `pip install trimesh lxml networkx`).
- `px72-extra.js`: Reduce-triangles carry-over check; Save to Google Drive / cloud storage dialogs at the cap. `px72-drive.js`: Open from Google Drive popup (closed).
- `make-testfiles.py`: generates the test meshes (trimesh, numpy).
- `px72-scripts.js`, `px72-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
