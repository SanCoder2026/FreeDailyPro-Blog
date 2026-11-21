Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF (pdf-password): deep test report for Claude

- **Written:** 2026-11-21 02:22 EST (box `date`, ET). Testing ran 2026-11-21 02:07–02:20 EST.
- **Tool:** https://www.freedailypro.com/tool/pdf-password. Row 36 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)"; tools.csv tag `gated:file-job`, bundle `secure-send-packet`. No duplicate group; Unlock PDF (#37) is its inverse. **GSC data is not available.**
- **Classification:** Professional Tool. Everything ran in the browser (pdf-lib); no PDF Toolkit API or upload call was seen (`json/privacy.json`).
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD (13 FAQs), 10 locales + /ar, blog, sitemap. JS: `PdfPassword`, `operations`, `BatchRunner`, `batch`, `protectedPdfNotice`.
  - **YouTube video:** yt-dlp, 37 frames, 4 sheets, zooms.
  - **Headless Playwright:** 15 live cases (Chromium, 3 also in Firefox); unlock-dialog cases; privacy marker scan; Share; a uses-left gate run with 5 single and 2 batch downloads; an at-0 run; Quick Buy; keyboard; 10-device / 11-locale / 6-geo / axe matrix.
  - **pikepdf/pypdf verification** of every downloaded file.
- **Starting counts (display-only):** the first fresh context had 10 left and was used for the gate run; the others loaded at 0. Trial uses spent: **4**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (stopped at the Day Pass email prompt and Stripe Checkout; session id redacted), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first", $4.99/month 1 GB). Open from Google Drive not clicked.
- **Pending:** nothing needs the 7:00 PM ET reset, so no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Owner context: Santosh decided (Nov 20) that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision, and so would full-quality previews at 0. Both are P1 gate gaps. This tool has the first problem but not the second.

Code to look at:
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI` with the set `Kt` (`evidence/js/index-B1CTyGtY.excerpt-usage.js`). `DI` (used by `ToolPage.vt`, which BatchRunner calls for per-file and ZIP downloads) skips the gate once the tool id is in `Kt`. The single-file Download button (`ToolPage` `ql`) uses the same set through `logUsageNow`.
- **`PdfPassword-CSuI9QpX.pretty.js`:** Protect makes no usage call; Download goes through the gated `D` button; there's no preview of the result (good).
- **`operations-B4LtHhm8.pretty.js` `kn`/`vn` (~2880–2970):** pdf-lib `encrypt` AES-256; permissions are `undefined` when no box is ticked (output /P −3904 with owner = user password).
- **FAQ/Limitations strings** live in the page's content source (not in this chunk).

After you ship, rerun `scripts/pp-gate.js` (every Download should follow the decision; at 0 every path still opens the cap dialog), `pp-live.js chromium`, `pp-unlock.js`, then `verify.py` on the downloads and test-cases.md (PW-01…PW-34).

## Intent

Someone is about to email a payslip, contract or ID scan and wants it unreadable to anyone without the password. They want:
- real protection, plus proof it worked
- no upload
- the password requirements made obvious
- several files at once
- a way in when the source PDF is already locked

The engine delivers:
- Every output is AES-256 (R6/AESV3).
- Pages, title, author, form fields, outlines and links survive.
- Unicode and exact-space passwords work.
- The "Checked: opens with your password" line is honest.
- Block options set the right flags.
- Batch of 5 works with one password.
- Already-protected inputs unlock inline.
- Neither the password nor the file leaves the tab.

Trust breaks in three places:
- **Gate:** only the first Download per page load costs a use.
- **Copy:** the FAQ and Limitations contradict the tool (unlock, block options, encrypted inputs).
- **Video:** it shows an old tool and tells viewers the encryption is "RC4 128-bit".

## Why: what the evidence says

- **P1 gate gap (conflicts with the Nov 20 decision): one trial use per page load.** `json/gate.json` (02:11:17–02:14:18 EST):
  - Download A 0 → 1, then A2, B (all blocks), C (50 pages, unicode) and D (space password) all stay at 1. That's four more protected PDFs free.
  - Reload + E 1 → 2.
  - Batch of 5: first per-file download 2 → 3, second file and the ZIP free.
  - Batch of 6 (5 kept): 3 → 4, the rest free.
- **No preview leak (PASS):** at 0, Protect still runs and shows the Checked line, but the result has no preview element. Single Download, batch per-file Download and ZIP all open the cap dialog.
- **P2: copy contradicts the tool.**
  - The FAQ says there's no unlock mode "even if you know it", yet the drop step unlocks with the password and the page links Unlock PDF.
  - Limitations say "an already encrypted PDF cannot be loaded here", but it loads after unlock.
  - The FAQ says the tool "doesn't separately restrict printing, copying, or editing", yet the block options exist and set flags (outputs B, E).
- **P2: video qBJKvkcI298** (111 s, 4 views, 2026-09-24): old single-field UI; on-screen text "real RC4 128-bit encryption"; "doesn't support removing an existing password"; "Free". Wrong cipher claim on a security tool.
- **P2: SEO/wording:** meta description 67 chars; English title/meta under 9 hreflangs; /ar 404; three names for the tool (page / video / blog); video and description say "free".
- **P2: blog** is accurate but generic: no AES-256, verification, block options or batch.
- **P2: completeness:** no owner (permissions) password, no metadata strip, no per-file passwords, no "generate a strong password" link (FDP has Password Generator).
- **P3 items:**
  - The unlock dialog says "your result won't have a password" (it will, the new one).
  - The cancel toast mentions a "list" and "row" in one-file mode.
  - A non-PDF gets the "damaged, try Repair PDF" message.
  - Owner-only restrictions are silently removed.
  - No-options outputs carry deny-all /P with owner = user password (set explicit allow-all).
  - Producer is rewritten to FreeDailyPro.
  - The cap dialog's mark claim doesn't fit this tool.
  - iPhone SE 9 px / ja 3 px overflow; eye-button label mismatch; Pixel contrast; 300+ vs 200+.

## Outcomes we want

1. Every Download (single, per-file, ZIP) is counted the way Santosh decided, with the batch rule ("5 files = one use") applied per batch run, not per page load.
2. FAQ, Limitations and How-to tell one story: the tool unlocks a protected input when you know its password, block options exist and are requests, and Unlock PDF is the tool for removing a password.
3. A new video: AES-256, confirm field, strength bar, block options, Checked line, Several files, "trial uses".
4. A richer meta description and translated head tags (or no hreflang); one tool name everywhere.
5. Premium Applications step: permissions password, metadata clean, per-file passwords, password generator link.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | AES-256 R6 on every output; content preserved; unicode/space passwords (`json/verify.json`). |
| 2 | Completeness vs competitors | PARTIAL | Verified result, batch, inline unlock; no permissions password, metadata clean, per-file passwords. |
| 3 | Ease of use | PASS | Two fields, live strength, clear disabled-state reasons, Checked line. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px, ja 3 px overflow. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; monthly → Stripe Checkout. Nothing typed. |
| 6 | Information correct | PARTIAL | FAQ "no unlock mode", "doesn't restrict printing/copying/editing"; Limitations "encrypted PDF cannot be loaded". |
| 7 | Indexing | PASS | 200; canonical self; sitemap incl. blog. |
| 8 | SEO | PARTIAL | Good title, FAQPage (13), VideoObject; meta 67 chars; English head tags under hreflang; /ar 404; generic og:image. |
| 9 | Blog exists and accurate | PARTIAL | Accurate process advice, but generic: no AES-256, Checked line, block options or batch; name "PDF Password". |
| 10 | YouTube video exists | PASS | qBJKvkcI298, 111 s, 4 views. |
| 11 | FAQ and guide correct | **FAIL** | Three FAQ/Limitations statements contradict live behaviour. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, "RC4 128-bit", "doesn't support removing", "Free". |
| 13 | Storage | PASS | Nothing stored (localStorage/session/IDB/cookies clean); Drive/cloud need sign-in (untested). |
| 14 | Sharing | PASS | Share copies only the tool URL; no password or file. |
| 15 | Downloads | PASS | `-protected.pdf` names; ZIP `protected-pdfs.zip` with 5 AES files. |
| 16 | Usage count | **FAIL (P1 gate gap)** | First Download per page load −1; four single and all later batch downloads free until reload, against the Nov 20 every-Download decision. No preview leak at 0. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (demand strong) | "password protect pdf" is an evergreen high-volume query; no AI needed. |
| 20 | Merge better? | No | Unlock PDF is the inverse; cross-link instead of merging. |
| 21 | Remove? | No | |
| 22 | Duplicates | None | |

## Severity summary
- P0: 0. Encryption, verification and privacy hold.
- P1: 1 (one use per page load, against the Nov 20 decision). Full-quality preview at 0: not present.
- P2: about 5 (copy contradictions, video RC4 claim, SEO/naming, blog, completeness).
- P3: several.
