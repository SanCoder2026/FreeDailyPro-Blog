Sent: 2026-11-22 06:34 ET

# FDP-100 package: how to use it

0. **File names:** every file starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references leave the prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md, REPRODUCE.md, test-cases.md and findings/ (parser-code-review, csv-excel-safety, content-seo-locales).
2. **Test data:** evidence/testfiles has 13 synthetic statements (fake names, accounts, amounts) and expected.json. evidence/analysis has accuracy.json/txt (live parse vs expected) and the LibreOffice de-DE/en-US imports.
3. **Evidence:** `json/` (parse per file, paste, variants, download, zero, mobile, scan, quickbuy, share, matrix), `downloads/` (the CSV/XLSX the tool produced), `screens/` (JPG ≤1400 px, tall pages cut at 6000 px), `html/`, `js/` (tool, csvParse, utils), `blog/`, `video/` (info + frames).
4. **Scripts:** see scripts/README.md.
5. **Rules:** guest only; no sign-in, payment, email or ad clicks; Stripe/OAuth IDs redacted; all test data made up.
6. **Retest:** REPORT "After fixes, rerun". Parsing costs no trial use; the download case needs a context with uses left (after midnight UTC, 7 PM ET).
Sent: 2026-11-22 06:33 ET
