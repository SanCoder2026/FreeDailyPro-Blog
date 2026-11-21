Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases, stale-compare, gate, uses-left, share, misc, probe, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool chunks, raw and prettified.
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, blog text.
  - `evidence/screens/`:
    - `live/`: stale, stale-compare, compare-match, file-60MB, share, blog top, probe.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/`:
    - `vectors.json`: inputs and the expected hashlib digests.
    - `files/F01_hello.txt` and `F03_empty.txt`.
    - `make-files.py`: recreates the 10 MB and 60 MB files, which are not shipped.
    - `outputs/print-preview.pdf`.
    - Never executed.
  - `evidence/video/`: metadata, sheets, zoom.
  - `scripts/`.
- **Sign-in blocked / untested:** none. No cap dialog, pass or Stripe prompt appeared, so the payment path was not reachable (check 5 N/A).
- **Pending:** RERUN-AFTER-RESET row 32. A context with uses left (after 7:00 PM ET) must show whether Generate is charged. Report it as FDP-32 -v2.
- **Trial uses spent:** 0 observed (every counter stayed where it loaded; display-only).
- **Retest:** `env -u BROWSER node scripts/hg-stale.js` (expect no Match after editing), then `hg-live.js`, `hg-gate.js`, `hg-uses.js`, `hg-misc.js`, `hg-share.js` and `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
