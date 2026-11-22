Sent: 2026-11-22 06:03 ET

# FDP-99 package: how to use it

0. **File names:** every file starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references leave the prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md; REPRODUCE.md; test-cases.md (G = guest, P = local replay, S = signed in); findings/ (value-and-merge, desk-code-review, content-seo-locales).
2. **Scope:** Workflow Product behind sign-in + trial. Live tests stop at sign-in. Desk behaviour comes from the shipped code; R1 and R2 were also replayed locally with pdf-lib on #93/#87 outputs (evidence/replay). Risks are not counted as findings; SIGNIN-NEEDED.md has the rows.
3. **Scripts:** see scripts/README.md.
4. **Evidence:** `json/` (live, live-firefox, matrix), `html/` (page, JSON-LD, links, pricing, workflow-products), `js/` (desk, Bates engine, ToolPage, gate), `blog/`, `video/channel.txt`, `replay/` (inputs, stamped outputs, recovered pages), `screens/` (JPG ≤1400 px).
5. **Rules:** guest only; no sign-in, payment, email or ad clicks; IDs redacted; test data made up.
6. **Retest:** REPORT "After fixes, rerun"; S01–S03 first once a trial account is available.
Sent: 2026-11-22 06:03 ET
