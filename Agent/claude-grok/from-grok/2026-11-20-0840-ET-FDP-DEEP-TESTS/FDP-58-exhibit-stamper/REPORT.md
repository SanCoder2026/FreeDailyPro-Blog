Sent: 2026-11-21 11:52 ET

# FDP-58 Exhibit Stamper (exhibit-stamper): deep test report for Claude

- **Written:** 2026-11-21 11:49 EST (box `date`, ET). Testing ran 2026-11-21 11:31–11:48 EST.
- **Tool:** https://www.freedailypro.com/tool/exhibit-stamper
  - TEST-ORDER row 58: **Professional Tool**, PDF Tools.
  - Plan note: "test-plan (unranked): L-243 PDF Toolkit". Duplicate group C11 (add-page-numbers, bates-numbering, document-operations-desk, legal-production-desk, pdf-watermark).
  - Blog: /blog/stamp-pdf-exhibits-a-b-c-with-index (Oct 24, 2026). Video: bC9ON6zNcxo (70 s, uploaded 2026-11-21, **not embedded on the tool page**).
  - **GSC data is not available.** No API/MCP testing.
- **Offer:** 10 trial uses a day, charged when you press **Stamp N file(s)** (`logUsageNow`, awaited before stamping). $1 Day Pass / $4.99 monthly. Trial uses reset at midnight UTC (7:00 PM ET).
  - Trial output carries **no** "Created with FreeDailyPro.com" badge (checked in pdftotext and renders of every output). The cap dialog still says passes remove that mark. Owner question, not a bug.
- **How it works:** in the browser (pdf-lib, fontkit). Black bold label (Helvetica, or a picture for non-Latin text), optional white box, 6 positions, size 8–36 pt, letters (A…Z, AA…) or numbers, text before/after (30 chars each), first page or every page, optional ", page X of N". One file gives `<name>-exhibit.pdf` + `exhibit-index.csv`; several give `exhibits-stamped.zip` (PDFs + `exhibit-index.csv`).
- **Test files:** FDP-55 set (reportlab + pikepdf: Letter 5p, A4 3p, landscape, dark, rotated 90/270/180, offset CropBox, 12 pages, same-name duplicate, single page, renamed text). Damaged and password (u123) PDFs from FDP-52. New in `make58.py`: 28 one-page docs (A→AB wrap) and a case-header PDF with text at the top-right margin. Plus `notes.txt`.
- **Testers:**
  - Desk: copy (4 FAQs, Limitations, Tips), JSON-LD, blog, JS (`ExhibitStamper-8bvElJ2l.js`, `drawTextAnywhere-DcuP6lHH.js`).
  - Playwright: probe at the cap in Chromium and WebKit (validation, bad files, cap dialog, Quick Buy). With uses left in Firefox: `cases-firefox.json` (13 runs, E01–E13), `left-firefox.json` (4 runs, 1 reload), `save-firefox.json` (Save to Drive / cloud). Drive-open popup check.
  - Chromium and WebKit fresh contexts were all at 10/10; Firefox gave a 0/10 context after 10–22 tries.
  - Outputs checked with pdfinfo, pdftotext, pdfimages and pikepdf (Rotate), rendered to PNG, crops reviewed by eye. CSVs and ZIPs unpacked.
  - Video frame sheet reviewed. Matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, ad and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email field and at Stripe Checkout (`cs_live_REDACTED`); no ad clicks; no site or repo changes; closed the Google popups I opened; typed only the test PDF's own password (u123).
- **Sign-in (untested):** Open from Google Drive and Save to Google Drive (both open Google sign-in), Save to my cloud storage (email sign-in + $4.99/month 1 GB add-on), paid-pass output.
- **RERUN-AFTER-RESET:** none. Every case ran with uses left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context:** Santosh treats per-page-load charging as a P1 gate gap. Copy and results count as trial uses.

**Where to look:**
- **ToolPage `logUsageNow`** (awaited by the Stamp handler) charges only on the first run of a page load.
  - left-firefox.json: L01 went 0→1 (`usage.log` POST 11:45:49 EST). L02 (new prefix "Pl. Ex. ") and L03 (new file) stayed at 1 in the same load. After a reload, L04 went to 2 (POST 11:46:18 EST). 4 runs = 2 uses.
  - cases-firefox.json: E01–E13, 13 stamping runs (47 files, including a 28-file set), cost 1 trial use and one `usage.log` POST (11:35:46 EST).
  - Same root cause as FDP-44 to -47, -54 and -55 (sibling Bates Numbering).
- **Fake "Download" ad creatives next to the real buttons:** with a result on screen, a "Tap 'Download' to Start" creative with a big green **Download** button filled the in-content slot directly under **Download stamped PDF / Save to…**, and the right rail showed another red/blue "Download" creative (`screens/cases/save-cloud-firefox.png`, `E01-…-firefox.png`). Don't remove ads; suggest a reserved, labelled slot away from the result buttons and blocking download-button creatives.
- **Numbers "Start at 0" silently becomes 1** (`Ae`: `Math.trunc(Number(s.start) || 1)`). Validation accepts 0, the index preview and output show Exhibit 1, 2 (P05 num-0 and E09). Either allow 0 or show "Start at 1 or more".
- **Default position (Top right) covers a typical case header.** header_top_right.pdf ("Case No. 2026-CV-01234 | Filed 11/21/2026" at the top-right margin): the white box hides "Filed 11/21/2026" (`screens/render/crop-E05-1.png`). Limitations warns, and the preview shows the first file's first page, so it's visible before download. Consider defaulting to Bottom right or warning when the box overlaps text.
- **Non-Latin label is a picture:** "Anlage A – 証拠" renders correctly (crop-E10) but pdftotext finds nothing of the stamp, not even "Anlage". Every page embeds its own PNG (12 pages: 24 image objects, 85,785 bytes vs ~2 KB for Latin). Exhibit labels get cited and searched; add a text layer or say so in Limitations.
- **Result buttons:** a one-file result shows two rows, each with its own **Save to Google Drive** and **Save to my cloud storage** (one for the PDF, one for the CSV), with no label saying which file each saves.
- **Copy:**
  - Limitations: "Locked PDFs have to be unlocked first." Live, an inline dialog unlocks them in place (E11, u123), and a skip gives a toast. Live is better than the copy.
  - Blog "Colour vs grayscale stamps… a light teal stamp" implies a colour choice; the stamp is always black. With the box off on a dark page the label is near-invisible (crop-E06).
  - The cap dialog promises removing a mark this tool never adds.
  - The FAQ answers "How is this different from Bates Numbering?" but the page doesn't link it; related links are Merge/Split/Compress only.

**After you ship:**
- Rerun `px58-live.js left firefox`: expect L02 to go 1→2 and L03 2→3.
- Rerun `cases`: expect +1 per run.
- Re-check E09 (Start at 0) and E10 with pdftotext.

## Intent

A paralegal, claims handler or applicant has a set of PDFs to file. Each document needs a clear "Exhibit A / Pl. Ex. 1" label and an index of which file is which exhibit, without sending client files to a server. The page promises exactly that, in the browser.

## What works (verified)

- **Labels:** letters A–C on the first page (E01), numbers with "Pl. Ex. " on every page with ", page X of N" (E02: "Pl. Ex. 1, page 1 of 5" … "Pl. Ex. 2, page 3 of 3"). 28 files run A…Z, AA, AB (E07); start Z gives Z, AA (E08); lowercase "zz" is accepted as ZZ, AAA.
- **Rotated pages (90/270/180), every page, Top left:** the label lands upright in the viewed top-left corner; /Rotate values kept (hi-E03-1, sheet-cases).
- **Offset CropBox:** label inside the visible box (E04). Landscape: correct corner (E01c). Size 36 bottom-left with suffix (E13) fits.
- **Index CSV:** Exhibit, Document, Stamped file, Pages, empty Description; rows match the PDFs; CRLF; injection guard (`=HYPERLINK("x")` → `"'=HYPERLINK(""x"")A"`). Same-name files give `-exhibit.pdf` and `-exhibit-2.pdf` with distinct rows (E11).
- **Password PDF:** inline unlock dialog ("…your result won't have a password"); u123 → toast "Unlocked", stamped as Exhibit C; output unencrypted, as disclosed.
- **Validation:** letters "1"/"ABCDE", numbers "A"/"-1"/"123456", size 7/37/empty each show a clear message and disable Stamp. Text before/after capped at 30 by `maxLength`.
- **Bad files:** renamed text or damaged PDF → "can't be read — it looks damaged" toast with a Repair PDF link; notes.txt → "can't be used here. This tool takes .pdf files."; duplicate → "already in the list. Added anyway…".
- **At the cap:** Stamp at 10/10 opens the cap dialog in Chromium and WebKit; status "Today's trial uses are used up… Trial uses start again at midnight UTC"; nothing produced. Day Pass stops at the email field; Monthly reaches Stripe Checkout.
- **Downloads and saves don't charge.** Settings persist across a reload (session storage).
- **Save buttons:** Save to Google Drive → Google sign-in popup (closed; toast "Google sign-in was closed… Nothing was opened or saved"); Save to my cloud storage → "Sign in with your email first" + $4.99/month 1 GB add-on dialog (Not now).

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 13 cases, outputs correct except Start 0. |
| 2 | Completeness | PARTIAL | Covers the core (letters/numbers, prefix, every page, index). Missing vs competitors (Adobe stamps, PDFelement, Bates/exhibit tools): stamp colour, a combined exhibit binder, cover/slip sheets (copy says use other tools). Non-Latin label not searchable. |
| 3 | Ease of use | PASS (minor) | Clear index preview; duplicate Save buttons per file; default corner may cover headers. |
| 4 | Layout | PASS (minor) | Clean; fake-download ad creatives sit beside the result buttons (P2). |
| 5 | Payment process | PASS | Email prompt / Stripe; stopped there. |
| 6 | Information correct | PARTIAL | Limitations "unlock first" (inline unlock exists); cap dialog mark text; blog colour section. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default, in sitemap. |
| 8 | SEO | PARTIAL | Title 51, meta 138, og-default image; SoftwareApplication + FAQPage (4) + Breadcrumb; **no VideoObject** because the video isn't embedded. |
| 9 | Blog exists and accurate | PASS (minor) | Accurate on features; colour section implies a colour option; "Download the CSV index" (multi-file CSV is only inside the ZIP). |
| 10 | YouTube video exists | PARTIAL | bC9ON6zNcxo exists (uploaded today) but isn't on the page. |
| 11 | FAQ and guide correct | PASS (minor) | 4 FAQs accurate; Limitations line on locked files outdated. |
| 12 | Video shows current capabilities | PASS (minor) | Current dark UI and flow (letters, first page, ZIP); "200+ professional tools" (live 300+); ~22 s of 70 s is outro. |
| 13 | Storage | Sign-in untested | Save to my cloud storage → email sign-in + $4.99 add-on dialog. |
| 14 | Sharing | Sign-in untested | Open from / Save to Google Drive → Google sign-in. |
| 15 | Downloads | PASS | Valid PDFs, CSV, STORE ZIP; Producer becomes pdf-lib. |
| 16 | Usage count | **FAIL (P1)** | Once per page load: 13 runs = 1 use; 4 runs + reload = 2. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home / PDF Tools / Exhibit Stamper. |
| 19 | AI need/demand | PASS | Deterministic legal labelling; a chat assistant can't stamp PDFs. |
| 20 | Merge better? | No | Distinct intent ("exhibit stamp"); keep beside Bates. |
| 21 | Remove? | No | Core legal PDF task, L-243. |
| 22 | Duplicates | C11: keep, cross-link | Bates (page numbers) vs Exhibit (document labels) differ; legal-production-desk bundles both. Link Bates Numbering and Legal Production Desk from the page. |

## Owner questions

1. **No badge on trial output** (same as Bates Numbering). Confirm, and make the cap dialog's mark sentence conditional.
2. After the per-load fix, should a re-stamp with only changed settings charge again? Assumed yes (results count).
3. Embed video bC9ON6zNcxo on the page (adds VideoObject)?
