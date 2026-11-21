Sent: 2026-11-21 03:27 ET

# Scripts: FDP-40 Extract PDF (guest QA)

**Intent:** let anyone re-run the live checks behind this report without signing in or paying.
**Why:** the trial-use findings (P1s) should be reproducible on a fresh guest context, and some of them are still pending a usage reset.
**Outcome:** the same JSON and screenshots as in `evidence/`.

Setup: Playwright 1.65 (`npm i playwright@1.65 && npx playwright install chromium firefox webkit`). Run with `env -u BROWSER node <script>`. Python checks need pikepdf, pypdf, reportlab and Pillow.

| Script | What it checks |
|---|---|
| make-pdfs.py | Builds E01_mixed_8p_bookmarks_form.pdf (8 pages, bookmarks, a form, tabs and columns). The other test PDFs are in evidence/testfiles. |
| ex-probe.js | First look: loader defaults (page box "1"), text mode, and the counters around Extract and Copy |
| ex-gate.js | Trial-use gate: part 1 needs a context with uses left (counts per page load and per Download); part 2 is the 0-uses path (cap dialog, text still shown) |
| ex-live.js `<chromium\|firefox> <V\|K\|VK>` | V = first-page previews at 0 uses (order, size); K = page-range parsing, errors, scanned/OCR notice, Unicode, forms |
| ex-copy.js | Copy button vs. selecting the read-only textarea at 0 uses |
| ex-corrupt.js | Damaged or renamed PDFs: shows the "Repair PDF" toast |
| ex-privacy.js | Network requests during extraction (file stays in the browser) |
| ex-left.js | Looks for a fresh context that still has trial uses (none found on Nov 21) |
| run-matrix.js + config.json | Devices, locales, geo and axe (`node run-matrix.js config.json`, about 8 min) |
| verify.py | Checks the downloaded PDF/TXT: page order, page count, text |

Safety: the scripts stop at the Day Pass email field and at Stripe. They never type an email or card details, never sign in, and never click ads.

## RERUN-AFTER-RESET (pending)
When a fresh guest context loads with trial uses (after the daily reset; check `fdp-usage-v1.usageToday` in localStorage):
1. `node ex-gate.js` (part 1): does the count go up on page load, on Extract, or only on Download?
2. `node ex-live.js chromium V`, then click Download PDF and Download Text File, and run `python verify.py <downloads>`.
3. Note whether Save to Google Drive / Save to my cloud storage show up. Don't click them, because they need sign-in.
Report the results as FDP-40 -v2.
