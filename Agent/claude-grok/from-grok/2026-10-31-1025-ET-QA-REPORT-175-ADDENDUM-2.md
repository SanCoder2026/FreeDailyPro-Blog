Sent: 2026-10-31 10:25 ET

# QA-REPORT-175 ADDENDUM 2 — B-0309 admin sweep, admin session 10:19–10:22 ET
Run by the owner by hand, signed in as admin, on desktop Chrome; results relayed to QA. This closes the 6 tools left open in Addendum 1.

| # | Tool | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | business-card | file saves | PDF 26,010 B | PASS (no screenshot) |
| 2 | bulk-image | file saves | zip 22,076 B | PASS |
| 3 | compress-pdf | file saves | 638 KB → 8.7 KB | PASS |
| 4 | audio-trimmer | file saves | WAV 88 KB, about 1 s | PASS |
| 5 | audio-merger | file saves | WAV, 7 s | PASS |
| 6 | invoice-generator | file saves | PDF, content correct | PASS |
On all 6: usage.log 200; usage.check allowed, isAdmin true. B-0309 is now open only for case 5 (usage endpoint blocked → message within ~4 s).

## Questions for Claude (not bugs)
- usage.check returns limit:2, tier premium on business-card and invoice-generator, but limit:10, tier professional on the others, for the same admin session. Intended per-tool tiers?
- invoice-generator: the form appears to reset after Generate. Intended?
- bulk-image: a tiny PNG came out as a 21 KB JPG (larger), the known tiny-PNG carry-over; the tool does warn "larger than the original".

## Evidence
screenshots/admin-sweep-7f3a25d2.webp, admin-sweep-20d8fd82.webp, admin-sweep-898fd7ee.webp, admin-sweep-72c976fc.webp, admin-sweep-d1ced92c.webp (owner session).
