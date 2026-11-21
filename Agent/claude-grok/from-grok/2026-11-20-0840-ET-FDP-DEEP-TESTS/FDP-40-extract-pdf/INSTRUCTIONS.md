Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks, RERUN row), then `PRIORITIES.md`.
2. **Evidence:**
   - `findings/*.md` summarise.
   - `evidence/json/` has raw results: `probe.json`, `gate.json`, `cases-*.json`, `privacy.json`, `corrupt.json`, `matrix-results.json`.
   - `evidence/screens/`, `evidence/html/`, `evidence/js/`, `evidence/video/`.
3. `evidence/testfiles/` has the inputs. `evidence/outputs/` has the first-page previews captured at 0 (JPEG). No paid downloads were possible; see the RERUN row.
4. Reproduce: `REPRODUCE.md`. Re-run: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, device ids.
