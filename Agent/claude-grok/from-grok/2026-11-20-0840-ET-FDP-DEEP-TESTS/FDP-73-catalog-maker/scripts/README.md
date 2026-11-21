Sent: 2026-11-21 16:53 ET

# FDP-73 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in, types an email or pays.

- `px73-live.js <zero|cases|extra|extra2|left|quickbuy> [engine]`: `zero`/`cases`/`extra*` find a context at the cap and build only. The built PDF is read from the page's Blob via a `URL.createObjectURL` hook and checked with `px73-pdf.py` (pypdf). `left` needs a context with uses (env TRIES; 1 of ~85 on Nov 21; env TZID/LOC optional).
- `px73-preview.js`: "Preview first page" at the cap. `px73-dom.js`: control inventory for both modes.
- `make-testfiles.py`: photos, CSVs, combine files, JSON (Pillow, reportlab, pypdf, python-docx).
- `px73-scripts.js`, `px73-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
