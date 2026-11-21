Sent: 2026-11-21 03:05 ET

# FDP-38 scripts (Playwright 1.65, Node; run with `env -u BROWSER node <script>` from a folder with playwright installed; Python with reportlab, pikepdf, PIL)

- `make-pdfs.py`: builds Q01 (photo page), Q02 (100-inch page), Q03 (mixed sizes) and the dupA/dupB same-name pair. P01–P07, U01 and U05 come from FDP-36/37 (included in evidence/testfiles).
- `pj-copy.js`: expanded copy + JSON-LD. `pj-probe.js`: controls, result UI, preview blobs (sizes/dims), chunk list.
- `pj-live.js [chromium|firefox] [K01,…]`: cases K01–K18 + pair page (no Download).
- `pj-gate.js`: finds a context with uses left (up to 14):
  - Download A/A2, then Drive/cloud (stops at sign-in).
  - Convert another → B and C, then reload → D, reload → E; it captures previews (`prev-*`) for comparison.
  - Then a context at 0: Print preview, Download → cap dialog → Day Pass (stops at email), range-37 preview, Quick Buy day/monthly (stops at Stripe), keyboard.
- `pj-privacy.js`: request scan for PDF/JPEG/PNG bytes, names and password; storage; Share. `pj-blog.js`: blog text.
- `run-matrix.js config.json`: devices / locales / geo / axe.
Never type an email or card; never click ads; never sign in.
