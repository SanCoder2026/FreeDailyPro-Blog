Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF (unlock-pdf): deep test report for Claude

- **Written:** 2026-11-21 02:34 EST (box `date`, ET). Testing ran 2026-11-21 02:23–02:33 EST.
- **Tool:** https://www.freedailypro.com/tool/unlock-pdf. Row 37 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)"; tools.csv tag `gated:file-job`. No duplicate group; Add Password to PDF (#36) is its inverse. **GSC data is not available.**
- **Classification:** Professional Tool. Everything ran in the browser; no PDF Toolkit API or upload call was seen (`json/privacy.json`).
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD (5 FAQs), 10 locales + /ar, blog URL, sitemap, YouTube search. JS: `UnlockPdf`, `PdfPageThumbnails`.
  - **Headless Playwright:** 15 live cases (Chromium, 3 also in Firefox); privacy marker scan + Share; a uses-left gate run (5 downloads); an at-0 run; hand-offs to Compress PDF and Remove PDF Pages at 0; Quick Buy; keyboard; 10-device / 11-locale / 6-geo / axe matrix.
  - **pikepdf/pypdf verification** of every download.
- **Starting counts (display-only):** the 3rd fresh context had 10 left and was used for the gate run; the others loaded at 0. Locally 1 use was logged; then the display jumped to 10 at the post-reload download (see Why).
- **Constraints kept:** guest only, no sign-in, no email or card typed (stopped at the Day Pass email prompt and Stripe Checkout; session id redacted), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage (email sign-in dialog). Open from Google Drive not clicked.
- **Pending:** nothing needs the 7:00 PM ET reset, so no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Owner context: Santosh decided (Nov 20) that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision, and so would full-quality previews at 0. Both are P1 gate gaps. This tool has the first problem; its at-0 preview is low-resolution thumbnails, which don't deliver the product.

Code to look at:
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI` with the set `Kt` (`evidence/js/index-B1CTyGtY.excerpt-usage.js`). The Download button (`ToolPage` `ql`, imported here as `D as j`) logs once per tool per page load.
- **`UnlockPdf-C2SvH1Cm.pretty.js`:** the unlock itself runs in the shared drop zone (`ToolPage` `x`/`y`); the page shows status, thumbnails (≤12) and `j` with `freeDownload: !unlocked` (unprotected files are free on purpose).
- **The 1 → 10 display jump** after reload: worth checking how `usage.check` / `usage.log` reconcile the local count with the server's.

After you ship, rerun `scripts/ul-gate.js` (every unlocked Download should follow the decision), `ul-live.js chromium`, `ul-handoff.js`, `verify.py`, then test-cases.md (UL-01…UL-30).

## Intent

Someone has a PDF they're allowed to use, but it nags for a password or blocks printing. They want:
- the protection gone in seconds
- proof the copy opens freely
- nothing uploaded
- a clear answer when the file isn't protected or the password is wrong

The engine delivers:
- AES-256, AES-128, RC4-128 and RC4-40 all unlock with the right password; owner-only restrictions drop without a prompt.
- Every download is unencrypted and matches the original: pages, title, author, form fields, outlines, links, page size, text.
- Wrong passwords get a gentle retry; spaces count; corrupt and non-PDF files get a clear message; unprotected files pass through free and say so.
- Nothing leaves the tab.

Trust and revenue break in three places:
- **Gate:** only the first Download per page load costs a use.
- **Discovery:** no blog post and no video.
- **Locales and meta:** thin.

## Why: what the evidence says

- **P1 gate gap (conflicts with the Nov 20 decision): one trial use per page load.** `json/gate.json` (02:25:21–02:27:17 EST):
  - Download A 0 → 1; A again 1 → 1.
  - New + AES-128 file B 1 → **1**; New + owner-only file C 1 → **1**. Two more unlocked files free.
  - After reload, Download E 1 → 10 (display jumped to the full daily count; looks like server reconciliation, display-only evidence).
- **Preview at 0 (PASS, not a leak):** up to 12 thumbnails at 244×316 px of the first pages. The product is a password-free file, which stays behind the cap dialog. Hand-offs to Compress / Remove Pages at 0 also end at the cap dialog (`json/handoff.json`).
- **P2: no blog post** (`/blog/unlock-pdf` 404, none in the sitemap) **and no video** (no Watch section; channel search found none; VIDEOS.md lists it missing).
- **P2: SEO:** meta description 73 chars; FAQPage only 5 Q&As; no VideoObject; H1 untranslated in all 9 locales; English title/meta under hreflang; /ar 404; generic og:image.
- **P2: completeness:** no "Several files" batch (Add Password has one); no Checked-style "opens without a password" verification line.
- **P3 items:**
  - At 0, after a blocked Download, the banner "downloading was not done" stays while an unprotected pass-through file downloads.
  - Unprotected files are uncounted: a policy note, low risk since the output is the identical input.
  - Limitations don't mention RC4 support.
  - Owner-only restrictions are removed with no password (a deliberate-policy note).
  - iPhone SE 9 px / ja 3 px overflow; eye-button label mismatch; ad-caption contrast.

## Outcomes we want

1. Every unlocked Download is counted as Santosh decided; unprotected pass-through stays free if he confirms.
2. The local counter and the server agree without sudden jumps (or the jump is explained in the strip).
3. A blog post and a short current-UI video (AES file → password → Download → opens freely; owner-only file; hand-off to Merge).
4. A richer meta description, more FAQs (RC4, owner-only, trial cost), translated H1/title/meta.
5. Premium Applications step: batch unlock with one password, a verification line.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | AES-256/128, RC4-128/40, owner-only; outputs unencrypted and identical in structure (`json/verify.json`). |
| 2 | Completeness vs competitors | PARTIAL | Strong core; no batch, no verification line. |
| 3 | Ease of use | PASS | Drop → password box → result; retry; clear errors. |
| 4 | Layout attractiveness | PASS (minor) | Thumbnails help; iPhone SE 9 px, ja 3 px. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; monthly → Stripe Checkout. |
| 6 | Information correct | PASS (minor) | Copy matches behaviour; RC4 not mentioned; trial cost not explained. |
| 7 | Indexing | PASS | 200; canonical self; in sitemap. |
| 8 | SEO | PARTIAL | Good title; meta 73 chars; FAQPage 5; no VideoObject; H1/title untranslated; /ar 404. |
| 9 | Blog exists and accurate | **FAIL** | `/blog/unlock-pdf` 404; none in the sitemap. |
| 10 | YouTube video exists | **FAIL** | No embed; channel search found none. |
| 11 | FAQ and guide correct | PASS | All five FAQs and How-to match live behaviour. |
| 12 | Video shows current capabilities | N/A | No video. |
| 13 | Storage | PASS | Nothing stored; Drive/cloud need sign-in (untested). |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PASS | `-unlocked.pdf`; pass-through keeps the original name. |
| 16 | Usage count | **FAIL (P1 gate gap)** | First Download per page load −1; B and C free; display jump 1 → 10 after reload. No full-quality preview at 0. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (demand strong) | "unlock pdf", "remove pdf password" are evergreen high-volume queries; no AI needed. |
| 20 | Merge better? | No | Distinct from Add Password; cross-linked. |
| 21 | Remove? | No | |
| 22 | Duplicates | None | |

## Severity summary
- P0: 0. Unlocking and privacy hold.
- P1: 1 (one use per page load, against the Nov 20 decision). Full-quality preview at 0: not present.
- P2: about 4 (no blog, no video, SEO/locales, completeness).
- P3: several.
