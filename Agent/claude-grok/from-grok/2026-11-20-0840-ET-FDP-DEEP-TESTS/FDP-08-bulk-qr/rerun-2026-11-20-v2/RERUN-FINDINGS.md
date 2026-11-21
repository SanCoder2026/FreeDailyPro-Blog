Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-08 bulk-qr (re-run after the trial reset)

**Supersedes:** `FDP-08-bulk-qr-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-08-bulk-qr-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 8 result: C and E DONE; A and B still at 0 (2026-11-20 22:25–22:35 EST)

Run 1 (22:25): A, B and E loaded at 0 and skipped themselves; C loaded at 10. Run 2 (22:33, A/B/E only): A and B loaded at 0; E loaded at 10.

| Check | Result |
|---|---|
| **C: 500 codes at 300 px (BQ-33)** | Done in **8.7 s**, toast "Generated 500 QR codes in one ZIP", ZIP **2,331,739 B**, count **0 → 1**. Inspection (`bq-inspect-C1-1120.json`): 500 PNGs numbered 001–500, all **300 × 300**, quiet zone **4.05 modules**, **500/500 decode** to their exact line, index.csv has a UTF-8 BOM and 500 rows that match. No mark. PASS |
| **E: one 3,000-character line + one valid line (BQ-34)** | Preview said "2 QR codes will be generated". Generate: **no download, no toast or error captured, and the count went 0 → 10** (stayed 10 after reload). So nothing was delivered while the counter showed today's uses all gone. Whether that is a real charge or the box-IP total syncing is unverified (display-only). BQ-07 is still FAIL. |
| A: repeat list / SVG cost (BQ-29) | **Still at 0**, pending. |
| B: names with accents/CJK, 2000 px, EC H, formula guard (BQ-17, BQ-30, BQ-32) | **Still at 0**, pending. |

**Counter jumps (display-only):** in today's re-run a single action sometimes moved the counter straight to 10 used (merge-pdf 6→10, compress-pdf 8→10, video-to-gif 0→10, resize-crop 0→10, bulk-qr 0→10 on a failed generate). This matches the intermittent jump seen in FDP-02. It may be the box IP's daily total syncing into the page; that is unverified, and no backend claim is made. To a real visitor it would look like one click spending all of today's trial uses.

**New P1 (display-only):** a failed bulk generate with a too-long line delivered nothing, yet the strip went from 10 remaining to 0.
