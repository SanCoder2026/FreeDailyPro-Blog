Sent: 2026-11-21 17:13 ET

# FDP-75 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. Guest contexts only; nothing signs in, types an email or pays.

- `make-testfiles.py` (python-docx): builds the 15 papers in testfiles/; `make_footer_pageno()` (call it explicitly) adds footer-pageno.docx.
- `px75-live.js <zero|left|quickbuy> [firefox]`: `zero` a context at 10/10; `left` one with uses (env TRIES), drops every paper in one load via "Check another file", reads the checklist, logs `usage.log` POSTs and whether doc text is in them, then reload + drop; `quickbuy` stops at the email dialog / Stripe.
- `px75-harness.js <APA|MLA|Chicago> files…`: the tool's checker `De` copied verbatim from the bundle; needs `npm i @xmldom/xmldom jszip` (NODE_PATH).
- `px75-blog.js`: blog text + links. `px75-scripts.js`, `px75-expand.js`: JS chunk list and expanded page copy. `run-matrix.js config.json`: devices, locales, geo, axe.
