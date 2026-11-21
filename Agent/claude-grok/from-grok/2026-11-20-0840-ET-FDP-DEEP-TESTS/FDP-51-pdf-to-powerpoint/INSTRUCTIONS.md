Sent: 2026-11-21 08:44 ET

# FDP-51 package: how to use it

1. **Read first:** REPORT.md (intent, evidence, 22 checks), then PRIORITIES.md.
2. **Reproduce:** REPRODUCE.md has guest steps for every issue. The test PDFs are in `evidence/testfiles/`:
   - P01–P10 come from `px51-make.js`. Chromium on this box writes Type3 text, so expect 0 editable pieces.
   - P11 and P12 come from `make-real.py` (LibreOffice, TrueType). Use them for editable-quality checks.
   - P11_source_deck.pptx is the original deck behind P11.
3. **Retest:**
   - `cd tools-env && TRIES=30 env -u BROWSER node px51-live.js left`. It needs a fresh context with uses left, and retries contexts until it finds one.
   - Also run `zero` (at the cap) and `subset firefox|webkit`.
   - `left2` covers the LibreOffice files and Stop.
4. **Inspect outputs:**
   - `python check-pptx.py <files>` (python-pptx).
   - Render with `soffice --headless --convert-to pdf` and compare with the source.
5. **Device matrix:** `node run-matrix.js config.json`.
6. **Evidence layout:**
   - `evidence/json`: run results, matrix, pptx inspections, category hubs.
   - `evidence/outputs`: the downloaded .pptx files.
   - `evidence/screens/{cases,live,devices,locales,geo,a11y}`.
   - `evidence/js`: pretty-printed chunks.
   - `evidence/html`: the page plus the category hubs.
7. **Rules:** guest only, no sign-in, stop at the email prompt or Stripe, no ad clicks. All timestamps are EST from the box `date`.
