Sent: 2026-11-21 17:13 ET

# Live functional findings (FDP-75)

- **P1 per-page-load charging:** Firefox context at 0/10 (try 9 of 30). L01 apa-good 0→1/10 (1 POST). L02–L14: 13 more papers, full reports, 0 POSTs, counter 1/10. L90 reload + drop: 1→2/10 (1 POST). L91 same file again: 0. Net log: 2 `usage.log` POSTs, 125 bytes each, no document text.
- Zero (10/10, Chromium): drop → cap dialog "You've used today's 10 trial uses…", no report, 0 POSTs. `.doc` → inline error. Open from Google Drive → accounts.google.com popup (closed).
- Chromium `left`: 40 contexts, all at 10/10.
- Quick Buy: Day Pass → "Day Pass, $1 | Enter your email…" (stopped). Monthly → checkout.stripe.com (stopped; ID redacted).
- Checklist accuracy: all 14 live papers correct; harness identical for all styles (see test-cases.md). Style switching re-scores without a charge.
