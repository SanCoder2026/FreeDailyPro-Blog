Sent: 2026-11-20 22:15 ET

# FDP-26 Invoice Generator: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | "Page 1 of 2" footer drawn over Balance due on a 23-line / 4-rate invoice; totals never page-break (re-verified Nov 20) | `screens/live/balance-overlap-1120.png`, `testfiles/outputs/2026-11-20/B-pdf-long-INV-002.pdf`, InvoiceGenerator L300/L356 | Keep the totals block together and above the footer; break to a new page when needed |
| 2 | P1 | PDF then Word of the same invoice → INV-001.pdf and INV-002.docx (Excel INV-003) | `json/spend-1120/spend-A.json` | Advance the number only on "new invoice"; every format of one invoice shares it |
| 3 | P1 | Video says "free" ×4 and shows the old form | `findings/video-findings.md` | Re-record with the Premium strip, current features and pricing |
| 4 | P1 (policy question) | One trial use per visit unlocks every later download (each a new invoice); reload charges again | `json/spend-1120/spend-B.json`, `json/spend-*.json` | Santosh decides per file / per invoice / per visit |
| 5 | P2 | Mixed RTL + digits in Notes reordered (bank code split) in Chromium, WebKit, Firefox | `screens/live/notes-bidi.png`, `chromium-vs-firefox-pdf-1120.png` | Isolate RTL runs (bidi isolates per run) |
| 6 | P2 | "1.500" parsed as 1.5 | ui-AB.log S5 | Locale-aware parsing or a "did you mean 1,500?" hint |
| 7 | P2 | At the cap Save profile is blocked while toasts say "Save your profile to keep it" | ui2.json | Let the local profile save without a pass, or change the toast |
| 8 | P3 | Excel vs PDF tax rounding; discount >100 FAQ; emoji toast; "Tax" column header; negative totals hide lines; focus on line-item errors; locale titles; currency default; SE overflow | desk/live findings | Small fixes |
