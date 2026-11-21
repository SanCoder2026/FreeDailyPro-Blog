Sent: 2026-11-21 18:03 ET

# FDP-79 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only.

- `px79-live.js <zero|left|cases> [firefox]`: `zero` at 10/10, `left` with uses (env TRIES): 7 copies with POSTs and clipboard per action; `cases`: 9 variants, 12 count inputs, slider, Test box, keyboard.
- `px79-shift.js`: the lost-click check on Chromium, Firefox, Pixel 7 and iPhone 14 (button box before/after, toast). The second click's "Couldn't copy" in Chromium there is because that context had no clipboard permission.
- `px79-noclip.js`: Copy with clipboard refused; counts selectable text nodes holding the character.
- `px79-blog.js`, `px79-scripts.js`, `px79-expand.js`: blog text, JS chunks, expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
- No test files are needed (generated text only), so there's no make-testfiles.py.
