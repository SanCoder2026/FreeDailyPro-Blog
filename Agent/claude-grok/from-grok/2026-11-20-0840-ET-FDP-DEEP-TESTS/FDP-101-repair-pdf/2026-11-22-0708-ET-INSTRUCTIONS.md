Sent: 2026-11-22 07:08 ET

# FDP-101 package: how to use it

0. **File names:** every file starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references leave the prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md, REPRODUCE.md, test-cases.md and findings/ (recovery-matrix, cross-tool-links, content-seo-privacy).
2. **Test data:** evidence/testfiles has base.pdf and the 25 damaged copies. All content is made up ("Alex Sample", example.invalid). `O01.objstm-note.txt` says which bytes were randomised.
3. **Evidence:**
   - `outputs/fdp/`: what the tool produced, identical to its download;
   - `outputs/qpdf/`, `outputs/mutool/`: the baselines;
   - `analysis/`: per-engine JSON, compare-all.md, renders;
   - `json/`: corpus, download, zero, privacy, links, extras, share, matrix;
   - `screens/`: JPG ≤1400 px;
   - `html/`, `js/`: tool, operations, pdfRecover, repairDiagnose, pdfLoadError;
   - `blog/`, `video/`: info + frames.
4. **Scripts:** see scripts/README.md.
5. **Rules:** guest only; no sign-in, payment, email or ad clicks; Stripe/OAuth IDs redacted; all test data made up.
6. **Retest:** REPORT "After fixes, rerun". Repair costs no trial use. Only the download case needs a context with uses left (after midnight UTC, 7 PM ET).
