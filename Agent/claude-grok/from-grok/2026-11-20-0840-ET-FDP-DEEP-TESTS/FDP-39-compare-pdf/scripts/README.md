Sent: 2026-11-21 03:05 ET

# FDP-39 scripts (Playwright 1.65, Node; run with `env -u BROWSER node <script>` from a folder with playwright installed; Python with reportlab, PIL)

- `make-pdfs.py`: builds the C01–C14 pairs (known edits, restyle/reflow, blank page, scan, two columns, 50 pages with an edit on p.37, Unicode, 3,200 lines, hyphenation). U01/P06/P07 come from FDP-36/37 (included).
- `cp-copy.js`: expanded copy + JSON-LD. `cp-probe.js`: controls, result text, usage before/after Compare, chunk list.
- `cp-live.js [chromium|firefox] [K01,…]`: cases K01–K19 (no Download).
- `cp-gate.js`: finds a context with uses left (up to 14):
  - Compare (count), Report PDF A/A2, .txt T.
  - New Comparison → B (.txt) and C (PDF), then reload → D, reload → E.
  - Then a context at 0: keyboard, a 50-page compare, both reports → cap dialog → Day Pass (stops at email), C01/C02 Side by Side screenshot, copy check, Quick Buy day/monthly (stops at Stripe).
- `cp-privacy.js`: request scan for PDF bytes, document text, names and password; storage; Share. `cp-blog.js`: blog text.
- `run-matrix.js config.json`: devices / locales / geo / axe.
Never type an email or card; never click ads; never sign in.
