Sent: 2026-11-20 23:25 ET

# Scripts (Playwright 1.65, Node)

Output paths at the top point at our box (`/workspace/deep/28-mortgage-calculator/…`). Run with `env -u BROWSER node <script>`. WebKit on Linux needs `GIO_EXTRA_MODULES` (run-matrix sets it if `giomods/` exists). All scripts are guest-only: they never sign in, never pay, never type an email or card, and never click ads.

- `mc-probe.js`: starting count, JS chunks, controls and test ids.
- `mc-copy.js`: expands About / How to use / FAQ / Details / Guides; saves the copy and JSON-LD.
- `mc-live.js [ids] [out]`: calculation cases M01–M44 and blog cases B01–B04, typed into the UI, reading results only.
- `mc-gate.js`: the 6 exports in a context at 0 and in contexts with uses (max 6). At 0 it would follow a cap dialog to the Day Pass email prompt and stop (none appeared).
- `mc-misc.js`: on-page trial/pass copy, head SEO tags, keyboard order, print rendering (`print-preview.pdf`, `print-preview-schedule.pdf`).
- `mc-share.js`: Share this tool, Add to favorites, URL round-trip.
- `mc-privacy.js`: records every request whose URL or body contains the typed price/income/debts.
- `mc-blog.js`: dumps the blog text and links.
- `run-matrix.js` + `config.json`: devices / locales / geo / axe matrix.
