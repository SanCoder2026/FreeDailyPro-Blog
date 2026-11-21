Sent: 2026-11-21 03:05 ET

# FDP-38 PDF to JPG: live functional findings (guest, headless Playwright, 2026-11-21 02:36–02:46 EST)

Raw: `evidence/json/gate.json`, `cases-chromium.json` (+ `cases-chromium-K16_K17.json` rerun), `cases-firefox-*.json`, `privacy.json`, `probe.json`. Counters below are `fdp-usage-v1.usageToday` (display-only evidence).

## Gate run (fresh context with 10 left: the 11th tried; 10 others loaded at 0)
| Step | Action | Used before → after | Label on Download |
|---|---|---|---|
| A | P01 3 pages High JPG → Download ZIP | 0 → **1** | "· uses 1 trial use" |
| A2 | Same ZIP again | 1 → 1 | (none) |
| Drive | Save to Google Drive | 1 → 1 | Google sign-in popup (untested) |
| Cloud | Save to my cloud storage | 1 → 1 | "Cloud storage $4.99/month … Sign in" dialog (untested) |
| B | Convert another: P02 1 page → single JPG | 1 → **1** | no "uses 1 trial use" |
| C | Convert another: P03 range 2-4 PNG → ZIP | 1 → **1** | no "uses 1 trial use" |
| reload | | 1 | |
| D | Q01 Print JPG → single JPG (783 KB) | 1 → 2 | "uses 1 trial use" |
| reload | | | |
| E | dupA/report.pdf + dupB/report.pdf + P02 → ZIP | 2 → 3 | "uses 1 trial use" |

**P1 gate gap (conflicts with the Nov 20 decision):** after the first charged Download, every later conversion in the same page load downloads free (B and C were different PDFs). The label itself drops "uses 1 trial use", so the code knows. Same shared set `Kt` as #35–37.

## Previews = full outputs, clean of the badge, at 0 trial uses (P1)
- Convert costs nothing (no usage call in `G`). After Convert, `ne()` renders the first 12 output blobs as `<img src="blob:…">`, shown at 160 px tall but **full resolution**.
- Gate step A previews: 1224×1584 JPEG, 27,369 / 25,119 / 25,151 B, the same figures as the caption.
- **The preview is cleaner than the paid trial download.** `gate-B` download (43,613 B) has the "Created with FreeDailyPro.com" badge top and bottom; the preview of the same page (22,818 B) has none (`evidence/screens/cmp-preview-vs-download-B.png`; 61,621 differing pixels, all inside the badge boxes). The badge is intentional on trial downloads, but a pass is sold as removing it, and the preview already gives a badge-free copy for nothing.
- **At 0 trial uses** (banner "0 remaining"): Q01 Print → preview 2550×3300, 1,065,785 B (sha c4de0f73…, identical to the uses-left preview); Download → cap dialog "Today's trial uses are done … downloading needs a pass", nothing downloaded, count stayed 10. Page range "37" on the 50-page PDF → a 2550×3300 preview of page 37 (89,473 B; Print setting kept): any page can be pulled one at a time, 12 per Convert.
- Users get it with right-click → Save image as (no contextmenu block in `PdfToJpg-CeZwXbKx.pretty.js`).

## Cap dialog, payment, keyboard (at 0)
- Cap dialog → "Buy Day Pass — $1" → "Day Pass, $1 | Enter your email and go straight to payment …" (stopped at the email field). Quick Buy day → same email prompt; Quick Buy monthly → Stripe Checkout (session id redacted; stopped).
- Keyboard: 28 Tabs reach Quick Buy and then the drop zone; Enter opens the file chooser.

## Live cases (Chromium; no Download)
| Case | Input | Result |
|---|---|---|
| K01 | P01 Standard | 918×1188, 16.4 KB/page. Matches 108 dpi on Letter. |
| K02 | P01 Maximum | 1836×2376. |
| K03 | P01 Print PNG | 2550×3300 PNG, about 202 KB/page. |
| K04 | range "3" | 1 page → "Download page as JPG · P01_payslip_3p_form-page-03.jpg". |
| K05 | P03 "1, 3-5" | Pages 01, 03, 04, 05. |
| K06 | "60" | Toast "Page 60 is outside this PDF's 50 pages"; no result. |
| K07 | "8-" | 43 pages; 12 thumbnails + "…and 31 more images in the download". |
| K08 | Q02 100-inch page, Print | "1 page was very large, so the resolution was lowered…" → 4000×4000 (16 MP cap). |
| K09 | Q03 mixed sizes | Letter 1224×1584, A4 landscape 1683×1190, 4-inch square 576×576. Each page keeps its own size. |
| K10 | U01 AES, pw old123 | Shared unlock dialog → "Unlocked" → 3 pages. |
| K11 | U05 owner-only | Silently unlocked → converted. |
| K12/K13 | corrupt / text renamed .pdf | "This file couldn't be read as a PDF: … Nothing was used." |
| K14 | dupA + dupB report.pdf + corrupt | Corrupt rejected at load; ZIP has `report/` and `report (2)/` (confirmed in gate-E). |
| K15 | 2 PDFs + range | Range box disabled; all pages converted. |
| K16 | P03 50 pages Print | 3.4 s; 50 pages, 4.26 MB ZIP. |
| K17 | U01 + P02, Skip | Toast "Skipped "U01…" — it's password-protected"; P02 converted. |
| K18 | "5-3, x" | Toast ""5-3" starts after it ends". |

- **Firefox** (K01, K04, K08, K10, K14): same behaviour. JPGs are about 2.6× larger (page 3 at High: 64.2 KB vs 24.6 KB in Chromium) because of the browser's JPEG encoder. P3: the blog's size guidance assumes Chromium.
- **Pair page** `/tool/pdf-to-jpg/pdf-to-png`: H1 "PDF to PNG Converter", canonical self, PNG preselected. The title says "Free, No Upload" (wording).
- **Password copy mismatch (P3):**
  - Tool copy: "Password-protected PDFs are skipped and listed."
  - Blog: "fail with an error message."
  - Live: a password dialog unlocks them in the browser; Skip gives a toast.
- **Privacy:** 228 requests, 12.7 KB of POST bodies total (ads/analytics). No request contained %PDF, JPEG/PNG bytes, file names or the password. Storage and cookies are clean. Share copied only the tool URL. Files are not restored after a reload.
