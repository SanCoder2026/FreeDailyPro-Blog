Sent: 2026-11-21 02:24 ET

# FDP-36 scripts (Playwright 1.65, Node; run with `env -u BROWSER node <script>` from a folder with playwright installed; Python ones with pikepdf, pypdf, cryptography, reportlab)

- `make-pdfs.py`: builds the synthetic PDFs (form, 50 pages, AES/RC4 user-password, owner-only, corrupt, text, 52 MB, B1–B6).
- `pp-probe.js`: controls, Protect, Checked line, network, script chunk list.
- `pp-live.js [chromium|firefox] [L01,…]`: input/password cases L01–L15 (no Download).
- `pp-unlock.js`: already-protected inputs (wrong/right password, RC4, Cancel).
- `pp-gate.js`: finds a context with uses left (up to 14 fresh contexts): Download A/A2, Drive/cloud (stops at sign-in), New + B/C/D, reload + E, batch 5 and 6 (per-file + ZIP); then a context at 0: Protect, Download → cap dialog → Day Pass (stops at email), batch at 0, Quick Buy day/monthly (stops at Stripe), keyboard.
- `verify.py`: pikepdf/pypdf check of downloads (encryption, pages, fields, outlines, links, permissions).
- `pp-privacy.js`, `pp-share.js`, `pp-copy.js`, `pp-blog.js`: privacy marker scan, Share, expanded copy + JSON-LD, blog text.
- `run-matrix.js config.json`: 10 devices, 11 locales, 6 geos, axe.
Never type an email or card; never click ads; never sign in.
