Sent: 2026-11-21 17:04 ET

# FDP-74 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only; nothing signs in, types an email or pays.

- `px74-live.js <zero|left|cases> [engine]`: `zero` finds a context at 10/10; `left` one with uses (env TRIES; 1 of 19 on Nov 21); `cases` runs fonts and text cases and saves the art to `live/art/`. The clipboard is read from a same-origin helper tab (Chromium only).
- Font comparison: `pip install pyfiglet`, then compare `pyfiglet.figlet_format(text, font=…)` with `live/art/<Font>.txt` (see REPORT "What works").
- `px74-scripts.js`, `px74-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
- No test files are needed (text input only), so there's no make-testfiles.py.
