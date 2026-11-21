Sent: 2026-11-21 02:36 ET

# FDP-37 scripts (Playwright 1.65, Node; run with `env -u BROWSER node <script>` from a folder with playwright installed; Python with pikepdf, pypdf)

- `make-locked.py`: builds U01–U13 locked PDFs from the FDP-36 sources (included in evidence/testfiles).
- `ul-probe.js`: controls, unlock dialog, result UI, network, chunk list.
- `ul-live.js [chromium|firefox] [K01,…]`: unlock cases K01–K15 (no Download).
- `ul-gate.js`: finds a context with uses left (up to 14): Download A/A2, Drive/cloud (stops at sign-in), New + B/C/D, reload + E, hand-off to Merge; then a context at 0: thumbnails, Download → cap dialog → Day Pass (stops at email), pass-through download, hand-off to Compress, Quick Buy day/monthly (stops at Stripe), keyboard.
- `ul-handoff.js`: hand-offs at 0 to Compress PDF and Remove PDF Pages, target Download.
- `ul-privacy.js`: password marker scan, storage, Share.
- `ul-copy.js`: expanded copy + JSON-LD. `verify.py`: download checks. `run-matrix.js config.json`: matrix.
Never type an email or card; never click ads; never sign in.
