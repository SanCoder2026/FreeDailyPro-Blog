Sent: 2026-11-20 23:05 ET

# Scripts (Playwright 1.65, Node 24)

Output paths at the top point at our box (`/workspace/deep/27-bmi-calculator/…`). Run with `env -u BROWSER node <script>`. WebKit on Linux needs `GIO_EXTRA_MODULES` (run-matrix sets it if `giomods/` is present). All scripts are guest-only: they never sign in, never pay, never type an email or card, and never click ads.

- `bmi-probe.js`: starting count, JS chunks, controls and test ids.
- `bmi-copy.js`: expands About / How to use / FAQ / Details / Guides; saves the copy and JSON-LD.
- `bmi-live.js [ids] [out]`: 46 calculation cases (B01–B39 metric, I01–I07 imperial), reading only.
- `bmi-gate.js`: the 6 exports in a context at 0 and in one with uses (max 6 contexts); at 0 it would follow a cap dialog to the Day Pass email prompt and stop (none appeared).
- `bmi-misc.js`: on-page trial/pass copy, head SEO tags, keyboard tab order, print rendering to `print-preview.pdf`.
- `bmi-share.js`: Share this tool, Add to favorites, URL round-trip.
- `bmi-privacy.js`: records every request whose URL or body contains the typed weight/height.
- `bmi-blog.js`: dumps the blog text and links.
- `run-matrix.js` + `config.json`: devices / locales / geo / axe matrix.
