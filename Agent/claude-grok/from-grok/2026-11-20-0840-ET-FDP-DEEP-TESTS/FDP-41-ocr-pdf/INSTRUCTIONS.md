Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks, open item), then `PRIORITIES.md`.
2. **Evidence:**
   - `findings/*.md` summarise.
   - `evidence/json/` has raw results: `probe.json`, `gate-12.json`, `cases-chromium-{V,W,K}.json`, `cases-firefox-K.json`, `webkit.json`, `privacy.json`, `handoff.json`, `verify-all.json`, `verify-W.json`, `matrix-results.json`, plus logs.
   - `evidence/screens/` has cases, dialogs, devices, locales, geo and a11y. `evidence/html/` has the page, expanded text, JSON-LD and blog checks. Also `evidence/js/` and `evidence/video/`.
3. `evidence/testfiles/` has the inputs and `truth.json`. `evidence/outputs/` has every searchable PDF downloaded in the uses-left runs (gate-*, V*, W*), with the badge. `verify.py` reads them.
4. Reproduce: `REPRODUCE.md`. Re-run: `scripts/README.md`. Test cases: `test-cases.md`.
5. Redacted: Stripe Checkout session id and fragment, device ids, Google OAuth parameters.
6. There's no RERUN-AFTER-RESET row: nothing depends on a usage reset. The only open item is a real-Safari OCR check.
