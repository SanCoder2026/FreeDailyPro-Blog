Sent: 2026-11-20 23:58 ET

# Scripts (Playwright 1.65, Node)

Output paths point at our box (`/workspace/deep/29-loan-calculator/…`). Run with `env -u BROWSER node <script>`. All scripts are guest-only: they never sign in, never pay, never type an email or card, and never click ads.

- `lc-probe.js`: starting count, chunks, controls and test ids.
- `lc-copy.js`: expands the page copy; saves the text and JSON-LD.
- `lc-live.js [ids] [out]`: main cases L01–L20 and workbench cases W01–W19 (reading results only).
- `lc-gate.js`: 9 export actions (main bar, workbench bar, result actions) at 0 and with uses (max 6 contexts). At 0 it would follow a cap dialog to the email prompt and stop (none appeared).
- `lc-misc.js`: trial/pass copy, head tags, keyboard order, print PDFs.
- `lc-share.js`: Share, favorites, URL round-trip.
- `lc-privacy.js`: requests carrying the typed amount/rate/extra.
- `lc-blog.js`: dumps /blog/loan-calculator (currently "Post Not Found").
- `run-matrix.js` + `config.json`: devices / locales / geo / axe.
