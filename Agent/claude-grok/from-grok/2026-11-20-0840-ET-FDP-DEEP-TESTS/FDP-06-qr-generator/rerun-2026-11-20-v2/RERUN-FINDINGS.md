Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-06 qr-generator (re-run after the trial reset)

**Supersedes:** `FDP-06-qr-generator-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-06-qr-generator-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 6 result: DONE (2026-11-20 22:20–22:21 EST)

One fresh context loaded at "10 remaining today"; each scenario is a new page visit.

| Check | Result |
|---|---|
| QR-27 cost | B1: PNG **0 → 1**; then SVG of the same code **free** (1 → 1); PNG again **free** (1 → 1). So 1 use per visit, not per file. B2–B8 cost 1 each (1 → 8). After reload: 8 used. PASS under the policy (downloads are counted). |
| QR-28 size | PNG is exactly **1000, 2000 and 200 px** (B1–B3). Quiet zone 4 modules (B1: 1000 px over 33 modules incl. margin). PASS |
| QR-29 mark | **No mark** on any PNG or SVG: `svg_text` empty, no FreeDailyPro mention. B5/B8 `corner_br_nonbg_pixels` > 0 are QR modules (smaller margin on denser codes), not a badge. PASS |
| Decoding | Every file decodes to the exact input. B8 (2,900 × "y", EC L) decodes from the PNG: length 2900, exact. PASS |
| QR-30 WiFi | Escaping kept. PASS |
| **QR-31 vCard ORG** | Still **FAIL**: the file contains `ORG:Smith; Jones & Co\, LLC`. The comma is escaped but the semicolon is not, so contact apps split the company into "Smith" and "Jones & Co, LLC". |
| QR-32 logo | PNG and SVG decode; the SVG keeps the logo as `<image>`; EC H with a logo. PASS |
| QR-33 colours | Kept in PNG and SVG (background `#fff7e6`). PASS |
| QR-35 file names | Fixed `qrcode.png` / `qrcode.svg` (confirmed). Enhancement stays open. |
