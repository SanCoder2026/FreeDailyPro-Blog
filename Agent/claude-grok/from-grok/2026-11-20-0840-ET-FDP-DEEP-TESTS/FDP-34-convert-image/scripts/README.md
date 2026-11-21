Sent: 2026-11-21 01:50 ET

# Scripts (Playwright 1.65, Node)

Output paths point at our box (`/workspace/deep/34-convert-image/…`). Run with `env -u BROWSER node <script>`. Guest-only: never sign in, pay, type an email or card, or click ads. Recreate test files with `evidence/testfiles/make-files.py` (Pillow, pillow-heif, piexif).

- `cim-probe.js`: starting count, controls before/after loading a file, format list.
- `cim-explore.js`, `cim-batch-explore.js`: one Convert / batch UI dump (no Download).
- `cim-live.js [C01,…] [chromium|firefox]`: 32 conversion cases, one fresh page each; saves the result preview; request scan.
- `cim-pairs.js`: 7 pair pages, preselected target.
- `cim-gate.js`: uses-left context (max 14 tries): Convert, Download ×2, Drive/cloud (stops at sign-in), frames ZIP, batch; then at 0: Download → cap dialog → Day Pass email prompt (stops), batch at 0, Quick Buy day/monthly (stops), keyboard.
- `cim-gate2.js`: Downloads of different images in one page load, reload, frames ZIP.
- `cim-gate3.js`: batch after a single Download, and single after a batch.
- `cim-axe-loaded.js`: axe on the loaded state + accessible names.
- `cim-copy.js`, `cim-blog.js`, `cim-misc.js`, `cim-share.js`: page copy and JSON-LD, blog text, head/keyboard/print, Share.
- `run-matrix.js config.json`: 10 devices, 11 locales (incl. /ar), 6 geo, axe.
