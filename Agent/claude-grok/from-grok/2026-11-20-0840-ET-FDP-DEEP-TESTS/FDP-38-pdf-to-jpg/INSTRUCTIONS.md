Sent: 2026-11-21 02:49 ET

# FDP-38 PDF to JPG: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks), then `PRIORITIES.md`.
2. **Evidence:**
   - `findings/*.md` summarise.
   - `evidence/json/` has raw results: `gate.json`, `cases-*.json`, `privacy.json`, `probe.json`, `matrix-results.json`.
   - `evidence/screens/`, `evidence/html/`, `evidence/js/` (prettified chunks + usage excerpt), `evidence/video/` (frame sheets, zooms, info).
3. `evidence/testfiles/` has the inputs. `evidence/outputs/` has the downloads (JPG/PNG/ZIP) and the captured previews (`prev-*`). Open them as images only; never execute.
4. Reproduce: `REPRODUCE.md`. Re-run after a fix: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, Google OAuth parameters, device ids.
