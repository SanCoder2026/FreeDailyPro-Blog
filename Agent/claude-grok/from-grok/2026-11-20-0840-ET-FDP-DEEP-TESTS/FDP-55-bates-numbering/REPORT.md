Sent: 2026-11-21 10:39 ET

# FDP-55 Bates Numbering (bates-numbering): deep test report for Claude

- **Written:** 2026-11-21 10:40 EST (box `date`, ET). Testing ran 2026-11-21 10:12–10:36 EST.
- **Tool:** https://www.freedailypro.com/tool/bates-numbering
  - TEST-ORDER row 55: **Professional Tool**, PDF Tools.
  - Plan note: "test-plan (unranked): L-243 PDF Toolkit". Duplicate group C11 (add-page-numbers, document-operations-desk, exhibit-stamper, legal-production-desk, pdf-watermark).
  - Video: 1u1qW4vfozE. Blog: /blog/stamp-bates-numbers-across-pdf-set.
  - **GSC data is not available.** No API/MCP testing.
- **Offer:** 10 trial uses a day, charged when you press **Add numbers to N file(s)** (`logUsageNow`). $1 Day Pass / $4.99 monthly.
  - By design, the numbered PDF has **no** "Created with FreeDailyPro.com" badge on trial (FAQ: "a production has to be clean"). That is an owner question, not a bug.
- **How it works:** everything runs in the browser (pdf-lib + fontkit). Black Helvetica Bold stamp, 0.5 in from the edge, optional white box, optional second-line legend, continuous or per-file count, auto-widen digits. One file gives `<name>-bates.pdf` plus `bates-index.csv`. Several files give `bates-numbered.zip` (PDFs plus `bates-index.csv`).
- **Test files:** made by `make55.py` (reportlab + pikepdf): Letter 5p, A4 3p, landscape, dark, footer text at the margin, rotated 90/270/180, offset MediaBox/CropBox, 12 pages, same-name duplicate, single page, renamed text file. Damaged and password (u123) PDFs reused from FDP-52.
- **Testers:**
  - Desk: copy (7 FAQs, Limitations), JSON-LD, blog, JS (`BatesNumbering-BkxVMHGO.js`, `batesNumbering-Pmx-EMyr.js`).
  - Playwright:
    - Probe at the cap in Chromium and WebKit: validation, bad files, overflow hint, cap dialog, Quick Buy.
    - Trial-use runs with uses left in Firefox: left-firefox.json (4 runs, 1 reload) and cases-firefox.json (12 runs, B01–B12).
    - Overflow-hint screenshots; Drive popup check.
    - Chromium and WebKit fresh contexts were all at 10/10. Firefox gave a 0/10 context.
  - Outputs checked with pdfinfo, pdftotext and pikepdf (Rotate, metadata), rendered to PNG, and crops reviewed by eye. CSVs and ZIPs unpacked.
  - Video checked frame by frame. Matrix: 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
  - **Banner, overflow and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Day Pass email field and at Stripe Checkout.
  - No ad clicks, no site or repo changes.
  - Closed the Google sign-in popup I opened.
  - Typed only the test PDF's own password (u123).
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup verified) and paid-pass behaviour. There is no Save to Drive or cloud button on the result, an absence verified live.
- **RERUN-AFTER-RESET:** none. Every case ran with uses left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context:** Santosh treats per-page-load charging as a P1 gate gap. Copy and results count as trial uses.

**Where to look:**
- **ToolPage `logUsageNow`** (awaited by `be()` before every run) charges only on the first run of a page load.
  - left-firefox.json: L01 went 0→1. L02 (new prefix) and L03 (new file) stayed at 1 in the same load. After a reload, L04 went to 2. That is 2 `usage.log` POSTs for 4 runs.
  - cases-firefox.json: B01–B12, 12 numbering runs (27 files, 47 pages stamped), cost 1 trial use and one `usage.log` POST.
  - Same root cause as FDP-44 to -47 and -54.
  - The FAQ ("however many files you number in the run") and the blog ("however many files you number in that visit") describe this. Once charging is fixed, the copy needs to follow.
- **In-content ad near the tool:** with the unlock dialog open, an ad creative showing a big green **"Download"** button ("Tap to Download") sat in the slot just above "Watch: Bates Numbering in Action", close to the tool's own download buttons. Screenshot: `screens/cases/add-dialog-…-firefox.png`.
  - Don't remove the ad. Suggest a reserved, clearly labelled slot and blocking fake-download-button creatives in the ad network's category/creative controls.
- **Text layer for non-Latin stamps:** a prefix like `Ü案件-` renders correctly (crop-B08), but pdftotext finds **nothing** of that stamp, not even the digits. ASCII stamps are searchable. Review platforms search Bates numbers, so either embed with a ToUnicode map or say in Limitations that non-Latin prefixes are not searchable.
- **CSV encoding:** `bates-index.csv` has no UTF-8 BOM, so Excel on Windows will likely show `Ã`-style text for non-ASCII prefixes or file names. This is a risk; it wasn't opened in Excel.
- **Copy:**
  - Limitations says "Password-protected and damaged files are left out and marked in the list." Live, they never reach the list. Password files get an inline unlock dialog, and if skipped a toast says "Skipped … it's password-protected". Damaged files get a toast with a Repair PDF link. The live behaviour is better than the copy.
  - The cap dialog says passes remove the "Created with FreeDailyPro.com" mark, but this tool never adds one.

**After you ship:**
- Rerun `px55-live.js left firefox`: expect L02 to go 1→2.
- Rerun `cases`: expect +1 per run.
- Re-check B08 with pdftotext.

## Intent

A paralegal or records officer has to send a set of PDFs out as a production. Every page needs a unique, sequential control number, sometimes a CONFIDENTIAL legend, and an index of first and last numbers per document. Client files must not go to a third-party server. The page promises exactly that, in the browser.

## What works (verified)

- **Numbering:** continuous across files (ABC000001–000005, then 000006–000008) and restart per file (DEF000001 in both). The preview list and index match the output.
- **Legend:** CONFIDENTIAL on the left and the number on the right of the same page. Putting both in the same corner is blocked with "Put the legend in a different place from the number."
- **Rotated pages (90/270/180):** the stamp lands upright in the chosen corner as viewed. The Rotate values are kept. Verified in the crops.
- **Offset CropBox:** the stamp sits inside the visible (cropped) page.
- **Footer text at the margin:** the stamp sits above it and doesn't cover it in this file. The FAQ warns it can cover margin content.
- **Overflow:**
  - With "Add digits automatically" on (the default), 999995 + 12 pages becomes OVF0999995–OVF1000006 and the hint says "Digits raised from 6 to 7".
  - With it off, the hint warns "Some numbers are longer than the digits you chose…". Screenshots in `screens/cases/overflow-*`.
- **Same-name files:** `contract_letter_5p-bates.pdf` plus `contract_letter_5p-bates-2.pdf`. The CSV shows both, with distinct ranges.
- **CSV injection guard:** a prefix `=SUM(1)` is written as `'=SUM(1)000001` in the CSV. The PDF stamp is literal.
- **Password PDF:** an inline dialog ("…never uploaded — and your result won't have a password"). Entering u123 gives "Unlocked", and the file numbers in sequence (UNL000002–000004). The output isn't encrypted, as disclosed.
- **Validation:** start <0 or a decimal, digits 0 or 11, and size 30 each show a clear message and disable the run. The prefix is capped at 30 by `maxLength`.
- **Bad files:** a renamed text file or damaged PDF gives a "can't be read — it looks damaged" toast with a Repair PDF link. A duplicate gives "already in the list. Added anyway…".
- **At the cap:** a run at 10/10 opens the cap dialog in Chromium, Firefox and WebKit, and nothing is produced. Day Pass stops at the email field and Monthly at Stripe Checkout (`cs_live_REDACTED`).
- **Downloads:** don't charge.
- **Single and ZIP results:** labels are correct. The suspected "ZIP label with one good file" case (B10) can't happen, because locked files never enter the list.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Page loads | PASS | 200; 10 devices render. |
| 2 | Core function | PASS | 12 cases, all outputs correct. |
| 3 | Edge cases | PASS (minor) | Rotated, CropBox, overflow, duplicates, password, damaged and injection all fine. Non-Latin stamp not searchable (P3). |
| 4 | Error messages | PASS | Clear, specific, with a Repair link. |
| 5 | Mobile/devices | PASS (minor) | iPhone SE header overflow is site-wide (known). ja desktop is 3 px wider (1369 px). |
| 6 | Information correct | PARTIAL | Limitations "marked in the list" is wrong. The cap dialog's mark text doesn't apply here. |
| 7 | Indexing | PASS | Canonical is self; hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 55 chars; meta "…Fast, right in your browser."; og-default image; SoftwareApplication + VideoObject + FAQPage (7) + Breadcrumb. |
| 9 | Blog exists and accurate | PASS (minor) | Accurate on features; documents per-visit charging. Two sections sit after "Closing next step". |
| 10 | YouTube video exists | PASS | 1u1qW4vfozE embedded (70 s, 2026-10-25). |
| 11 | FAQ and guide correct | PASS (minor) | Accurate; the "per run" charging wording matches today's per-load gap. |
| 12 | Video shows current capabilities | PASS (minor) | Current UI and flow; header says "200+" (live "300+"). |
| 13 | Storage | N/A | No save-to-cloud on results (verified live). |
| 14 | Sharing | Sign-in untested | Open from Google Drive → Google sign-in popup. |
| 15 | Downloads | PASS | Valid PDFs, CSV, STORE ZIP; Producer becomes pdf-lib, Title/Author kept. |
| 16 | Usage count | **FAIL (P1)** | Once per page load: 12 runs = 1 use. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home / PDF Tools / Bates Numbering. |
| 19 | AI need/demand | PASS | Deterministic legal stamping; a chat assistant can't do it. |
| 20 | Merge better? | No | Distinct legal search intent ("Bates numbering"). |
| 21 | Remove? | No | Core legal PDF function, L-243. |
| 22 | Duplicates | C11: keep, cross-link | Siblings have different outputs: add-page-numbers (plain page numbers), exhibit-stamper (A/B/C labels), legal-production-desk (full production with privilege log), pdf-watermark. The tool page's related links show only Merge/Split/Compress; suggest linking Legal Production Desk and Exhibit Stamper (the blog already does). |

## Owner questions

1. **No badge on trial output** is intentional per the FAQ. Confirm this stays, since it differs from other PDF tools.
2. After the per-load fix, should a run re-charge when only settings change (same files, new prefix)? Copy and results count as uses, so the assumption is yes.
