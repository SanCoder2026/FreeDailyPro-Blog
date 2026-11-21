Sent: 2026-11-21 04:17 ET

# Scripts: FDP-42 Find & Replace (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the gate finding (P1), preserve case (P2) and the edge cases should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and downloaded files as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`.
- WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir (TLS).
- Python checks need python-docx and Pillow.
- Paths point to `/workspace/deep/42-find-replace/`; change `BASE` if needed.

| Script | What it checks |
|---|---|
| make-files.py | Builds F01–F08, F10–F12 (text, JSON, CSV, MD, HTML, XML, Unicode, fake .doc, PNG, rich .docx, 6.4 MB). F09 is a deliberately broken .docx. |
| fr-scripts.js / fr-expand.js | JS chunk list; expanded page text, JSON-LD and links |
| fr-gate.js `12` | **Part 1** (looks for a context with uses left): the counter at every step, through pasted, .txt and .docx Replace All + Download. **Part 2** (at 0): pasted, .txt (copyable?), .docx Replace All + Download. It looks for a cap dialog and stops at an email prompt, Stripe or Google sign-in. |
| fr-live.js `<chromium\|firefox\|webkit> [T01,T03,…]` | Cases T01–T28 with downloads |
| verify.py | Downloaded text: encoding, BOM, line endings, replacements. .docx: runs, formatting, header, table, images. Writes verify.json. |
| fr-privacy.js | Requests after a .docx drop, replace and download (hosts, POST sizes, leaks) |
| fr-blog.js | Blog static HTML vs hydrated text (the `$&` artefact) |
| run-matrix.js + config.json | Devices, locales, geo and axe (`node run-matrix.js config.json`, about 10 min) |

**Safety:**
- The scripts never type an email, card or password.
- They never click ads, and never click "Open from Google Drive".
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
