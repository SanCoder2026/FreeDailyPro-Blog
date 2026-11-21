Sent: 2026-11-21 08:44 ET

# FDP-51 PDF to PowerPoint (pdf-to-powerpoint): deep test report for Claude

- **Written:** 2026-11-21 08:42 EST (box `date`, ET). Testing ran 2026-11-21 08:14–08:41 EST.
- **Tool:** https://www.freedailypro.com/tool/pdf-to-powerpoint. Row 51 of TEST-ORDER.md: **Professional Tool**, PowerPoint & Slides, plan note "test-plan (unranked): L-243 rank 1 (PDF Toolkit API live)". No duplicate group.
  - **Video:** none (verified absence; see check 10). **Blog:** none (verified absence; see check 9).
  - **GSC data is not available.** The API side was not tested (no API/MCP testing).
- **Offer:**
  - 10 trial uses a day, charged at Download (`gateAtDownload`). Choosing a mode, converting and the slide preview are open at 0 uses.
  - $1 Day Pass / $4.99 monthly.
- **How it works:** everything runs in the browser (`PdfToPowerPoint-DjPnFh-o.js`).
  - **Picture per slide:** pdf.js renders each page to a 1920 px JPEG (quality 0.88), which becomes the slide background.
  - **Editable text:** each page is rendered twice, once normally and once with `fillText`/`strokeText` turned off. Text items whose pixels change between the two renders become pptxgenjs text boxes (font mapped, colour measured). The other items stay in the picture.
  - The slide size comes from the first page, clamped to 4–56 in.
  - Password PDFs unlock in the browser.
- **Testers:**
  - **Desk review:** copy, FAQ (4), Details, JSON-LD, JS, category hubs.
  - **Headless Playwright runs:**
    - At the cap (zero.json).
    - One long load with uses left plus a reload (left.json, 17 cases).
    - A second context with uses left (left2.json: LibreOffice-made PDFs and Stop).
    - Firefox and WebKit subsets.
  - **Test files:** 12 PDFs:
    - Chromium-made decks and documents.
    - LibreOffice-made deck (from a .pptx) and memo (TrueType text).
    - A scan, a password file, a damaged file, a non-PDF, 60 pages, mixed page sizes, and multilingual text.
  - **Output checks:**
    - Every .pptx inspected with python-pptx (`check-pptx.py`): slide size, shapes, text, fonts, sizes and colours.
    - Editable outputs rendered with LibreOffice and compared side by side with the source.
    - Network scan.
  - **Matrix:** 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Day Pass email prompt and at Stripe Checkout.
  - No ad clicks, no API/MCP calls, no site or repo changes.
  - The only password typed was the test PDF's own (u123).
- **Sign-in (untested):**
  - Save to Google Drive: Google sign-in popup with uses left; cap dialog at 0.
  - Save to my cloud storage: "Sign in with your email first", $4.99/month add-on.
  - Open from Google Drive: Google popup.
  - Paid-pass output.
- **RERUN-AFTER-RESET:** none. Nothing is pending a usage reset.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:**
- Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps.
- The "Created with FreeDailyPro.com" badge is intentional.

**Code to look at:**
- **ToolPage DownloadButton (`gateAtDownload`):** charges once per tool per page load and never re-checks. This is the same root cause as FDP-44 to FDP-50.
- **`PdfToPowerPoint-DjPnFh-o.js`:**
  - `me()` takes pdf.js `getTextContent()` items in content-stream order and `ce()` groups them into lines and blocks. For Arabic, the glyphs are in visual order and use presentation forms, so the editable text comes out reversed (P08).
  - `ne()` measures colour from antialiased pixels, so pure black becomes #272727–#353535.
  - Table cells on one baseline merge into one run ("Region Q3 Q4") and lose their column positions.

**After you ship:**
- Rerun `scripts/px51-live.js left`. Expect +1 per new deck, and the cap dialog at 10/10 without a reload.
- Re-inspect M01/M03/L12 with `check-pptx.py`.
- Work through test-cases.md.

## Intent

A teacher, consultant or small-business owner has a PDF (a report, a handout, or a deck someone exported) and needs it in PowerPoint. Either they show the pages as they are, or they fix a heading or a figure without retyping, and they don't want to upload a client document.

The core is genuinely good:
- **Picture per slide:** exact, fast (60 pages in 1.4 s, 1.8 MB) and the right slide shape (16:9 → 13.33 × 7.5 in; Letter/A4 portrait kept).
- **Editable text on a real deck** (LibreOffice export of a .pptx):
  - 33 pieces of text in 13 text boxes. The text is removed cleanly from the background picture, so there is no ghost text.
  - Bold and italic kept. Liberation Sans/Serif mapped to Arial/Times New Roman. Unusual fonts listed honestly ("Deja Vu Sans").
  - Rendered side by side, it looks almost identical to the source.
- **Honest summary:** "N pieces became editable / M stayed in the picture / 1 page had no text (a scan)". For PDFs whose text is drawn as Type3 glyphs it correctly says 0 became editable rather than producing junk.
- **Stop and errors:** Stop works mid-run (no charge, no toast). Password PDFs unlock inline. Damaged and non-PDF files get a clear message with a Repair PDF link.
- **Privacy:** no document bytes are POSTed. Only the 126-byte `usage.log` goes out, as the Details text says.

What undercuts it:
- **Per-page-load charging:** 14 new decks for one trial use.
- **Discovery:** the tool can't be found where users look. It isn't on the PDF Tools hub next to PDF to Word/Excel/JPG, there's no video and no blog post, and "PPT" never appears in the title, meta or body.
- **Editable-text quality gaps:** a business user will notice these.
  - Arabic comes out reversed.
  - Table text bunches into one line per row.
  - Black text is slightly grey.

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - left.json:
    - L01 went 0→1. Then L01b (re-download) and L02–L14 produced 13 more new decks (picture and editable, 1 to 60 slides), all at 1.
    - After a reload, L20 went 1→2, and L21 (a new deck) still downloaded at 2.
    - There were only 2 `usage.log` POSTs in the whole run.
  - left2.json, a separate context: M01 went 0→1, then M02, M03 and M05 (new decks) downloaded at 1, with 1 POST.
- **P2, findability.**
  - **PDF Tools hub:** the rendered /category/pdf-tools (40 tool links in `<main>`) lists PDF to Word, PDF to JPG and PDF to Excel but not PDF to PowerPoint (category-hubs.json, verified live). The tool is only on PowerPoint & Slides.
  - **No video (check 10 FAIL):** the page has no embed. Channel searches for "powerpoint", "pdf to powerpoint", "pdf slides" and "pptx" return only PowerPoint→PDF videos (aaUItszftt8, rnjZAS1Vulg).
  - **No blog (check 9 FAIL):** no blog slug in the sitemap mentions PDF→slides or PowerPoint conversion in this direction. The nearest are /blog/pdf-to-jpg-slides-from-packet and /blog/convert-powerpoint-slides-to-pdf-for-handouts. The page links no post.
  - **Keywords:** "PPT" doesn't appear in the title, meta or page text (only one "pptx"). "pdf to ppt" is a high-volume query (GSC data is not available to size it).
- **P2, editable-text quality.**
  - **Arabic is reversed** (P08, cmp-P08-src-vs-editable.png). The source "هذا نص عربي للاختبار من اليمين إلى اليسار" becomes "رﺎﺴﻴﻟا ﻰﻟإ ﻦﻴﻤﻴﻟا…": word and letter order reversed, in presentation-form glyphs. The Hindi, Greek, Cyrillic and kanji lines in P08 were Type3 glyphs and stayed in the picture, so they weren't assessed. The site has no /ar locale, but Arabic PDFs are common for MENA users.
  - **Tables** (P11 slide 3, P12): each row becomes one run, "Region Q3 Q4" / "Laptops $4,800", so the text no longer sits in its cells and overlaps the drawn grid. This is disclosed ("tables are not rebuilt"), but one text box per cell would keep the look at almost no cost.
  - **Colour:** pure black text is written as #272727–#353535, #1A4FA0 as #2759A5, and #C00000 as #C92424. It looks slightly washed out. This is disclosed ("can be slightly off"); snapping near-black/near-white and anti-alias-weighted sampling would fix most of it.
- **P2, tool body English on locale pages.** On all 10 locales the following stay English: the H1, title, meta, subtitle, "Runs on your device", the drop-zone text, the mode cards, the result summary and the Premium cross-sell copy. The header/trial strip and the Drive button are translated (locale-de fold).
- **P2, owner question: preview at 0.** At 10/10 you can convert and flip through every slide of the real .pptx in the preview (Z01/Z02, M01-at-cap). Only the file is gated. For Picture mode that's no more than the PDF itself, so it's low risk. Raise it as a question, not a defect.
- **P3 items:**
  - **Copy out of date:** "How to use it" says "PDFs protected with a password need unlocking first", but the tool unlocks inline (L07: unlock dialog → 3 slides).
  - **Non-PDF message:** a non-PDF file (P10, the text "not a pdf") gets "looks damaged … Try the Repair PDF tool"; "This isn't a PDF" would be clearer.
  - **Mixed page sizes:** the slide size follows page 1, and a landscape page 2 is letterboxed in a portrait slide (documented).
  - **Picture quality:** fixed at 1920 px JPEG 0.88. Fine for projection; an "HD" option would help print handouts.
  - **Pass dialog wording:** the cap dialog says a pass "removes the 'Created with FreeDailyPro.com' mark from your PDFs and images", but trial .pptx outputs carry no mark (checked the XML and the slide images). Owner question: is that intended?
  - **SEO:** og:image is og-default. Title 63 chars, meta 134 chars. No VideoObject (no video). FAQ: 4 questions, no duplicates.
  - **Layout and axe:**
    - iPhone SE 9 px horizontal overflow; /ja desktop 3 px.
    - Pixel 7 CLS 0.081 (under 0.1).
    - axe: label-content-name-mismatch (1), region (1), Pixel 7 color-contrast on the ad label (2).
  - **Counter display:** in the WebKit subset the strip/localStorage went from 10 to 0 after S03 with no download. This display-only drift was also seen in FDP-50, and the cap dialog showed correctly (unverified cause).
- **Test-file note:** this box's headless Chromium writes text as Type3 glyphs, so P01/P02/P07 have Type3 text. The tool correctly reported "0 pieces became editable" for them. All editable-quality judgements come from the LibreOffice files P11/P12 (TrueType).

## Outcomes we want

1. One trial use per new deck downloaded, with the cap enforced without a reload.
2. Users searching "PDF to PPT" or browsing PDF Tools find the tool, and a short video plus a blog post show both modes.
3. Editable mode holds up on business PDFs:
   - Arabic (and other right-to-left text) in logical order.
   - Table cells as separate boxes (or real tables).
   - True black text.
4. Locale pages translate the tool body, not just the chrome.
5. Copy matches behaviour (inline password unlock, a non-PDF message).

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | Picture exact; editable 33/33 text items on the LibreOffice deck; 60 pages in 1.4 s / 2.6 s; Stop, password, damaged all handled. |
| 2 | Completeness vs competitors | PARTIAL | Compared with Adobe Acrobat online, Smallpdf and iLovePDF (which give editable text, native tables and OCR for scans, server-side): FDP is local-only with an honest summary, but has no OCR, no table rebuild, and Arabic is reversed. Cross-link OCR PDF for scans. |
| 3 | Ease of use | PASS | Two clear mode cards, a page strip, a progress counter with Stop, a slide-by-slide preview. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow, /ja 3 px. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $1 email prompt (stopped); Quick Buy monthly → Stripe Checkout (stopped). |
| 6 | Information correct | PASS (minor) | FAQ/Details match the code (4–56 in, fonts listed, no OCR, privacy); the password line is out of date. |
| 7 | Indexing | PASS | 200, index, canonical self, hreflang 10 + x-default, in sitemap. |
| 8 | SEO | PARTIAL | Title/H1 fine; no "PPT" keyword; og-default; no VideoObject. |
| 9 | Blog exists and accurate | **FAIL** | No post found in the sitemap or linked from the page (verified). |
| 10 | YouTube video exists | **FAIL** | No embed; channel search found only PowerPoint→PDF videos (verified). |
| 11 | FAQ and guide correct | PASS (minor) | 4 accurate answers plus a detailed guide; one stale line. |
| 12 | Video shows current capabilities | N/A | No video. |
| 13 | Storage | Sign-in untested | Save to my cloud storage needs email sign-in + $4.99 add-on. |
| 14 | Sharing | PASS / sign-in untested | Share this tool present; Save to Google Drive needs Google sign-in. |
| 15 | Downloads | PASS | Valid .pptx (python-pptx and LibreOffice open them all); correct slide counts and sizes. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 14 new decks for one use. |
| 17 | Categorization in section | PASS | PowerPoint & Slides, Professional Tools. |
| 18 | Correct section of site | PARTIAL | Missing from the PDF Tools hub, where its siblings (PDF to Word/Excel/JPG) live. Cross-list it. |
| 19 | AI need/demand | PASS | L-243 rank 1; chat assistants can't return a .pptx that keeps a private PDF's look, locally. |
| 20 | Merge better? | No | Distinct output; Universal File Converter doesn't output .pptx (site map). |
| 21 | Remove? | No | Demand rank 1, works well. |
| 22 | Duplicates | None | Keep; cross-link OCR PDF (scans) and PDF to Word. |
