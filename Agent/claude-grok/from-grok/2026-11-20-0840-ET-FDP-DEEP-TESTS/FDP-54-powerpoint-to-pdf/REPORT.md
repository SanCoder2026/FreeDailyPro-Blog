Sent: 2026-11-21 10:12 ET

# FDP-54 PowerPoint to PDF (powerpoint-to-pdf): deep test report for Claude

- **Written:** 2026-11-21 10:09 EST (box `date`, ET). Testing ran 2026-11-21 09:47–10:08 EST.
- **Tool:** https://www.freedailypro.com/tool/powerpoint-to-pdf
  - TEST-ORDER row 54: **Professional Tool**, PowerPoint & Slides.
  - Plan note: "test-plan (unranked): L-243 PDF Toolkit". Duplicate group C12 (PowerPoint to other formats).
  - Video: rnjZAS1Vulg. Blogs: /blog/convert-powerpoint-slides-to-pdf-for-handouts and /blog/finish-a-deck-for-sending-fonts-size-and-notes.
  - **GSC data is not available.** No API/MCP testing.
- **Offer:** 10 trial uses a day, charged at **Convert to PDF** (`logUsageNow`). $1 Day Pass / $4.99 monthly.
  - Trial PDFs carry the intentional "Created with FreeDailyPro.com" badge, which links to freedailypro.com, on every page.
- **How it converts:**
  - .pptx is rendered in the browser, one JPEG page per slide (Fast 1280 / Default 1920 / Sharp 2560 px), with an optional invisible text layer.
  - .ppt, .odp and .key are first sent to `/api/trpc/presentation.convert`, which converts them to .pptx (this is disclosed on the page).
- **Test files:** built by `make54.py` (python-pptx plus LibreOffice).
  - **Rich 16:9 deck:** gradient title slide, speaker note, bullets with a hyperlink, column and pie charts, table, full-bleed picture, hidden slide, Hindi/Japanese/Arabic/emoji/Greek/Russian.
  - **Other decks:** 4:3 deck, 60-slide picture deck, picture-only deck.
  - **Converted copies:** .ppt, .odp, .ppsx.
  - **Bad files:** renamed text, zip that isn't a deck, truncated .pptx, .txt.
  - **Renamed copies:** .pptm, .potx, .pps, .key (renamed .pptx).
- **Testers:**
  - Desk: copy (14 FAQs), JSON-LD, two blogs, JS (`PowerPointToPdf-Cog7wXZW.js`, `pptxRasterize`, `SlideUi`).
  - Playwright: probe at the cap in Chromium, Firefox and WebKit; a trial-use run with uses left (left.json); 8 conversion cases (cases.json) plus a rerun (cases-r2.json); renamed-extension run; Drive popup check.
  - PDFs checked with pdfinfo, pdffonts, pdfimages, pdftotext and pikepdf (links), and rendered to PNG for visual review.
  - Video frame by frame. Matrix: 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
  - **Visual findings were checked against the screenshots, not just the script flags.**
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Day Pass email field and at Stripe Checkout.
  - No ad clicks, no site or repo changes.
  - Closed the Google sign-in popup I opened.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup verified), Save to Google Drive, Save to my cloud storage, and paid-pass output (badge removed).
- **RERUN-AFTER-RESET:** none. Everything was converted with uses left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context:** Santosh treats per-page-load charging as a P1 gate gap. Copy and results count as trial uses.

**Where to look:**
- **ToolPage `logUsageNow`** (called by `$` before every conversion): it charges only on the first conversion of a page load.
  - left.json: L01 went 0→1. L02 (a different deck, same page) stayed at 1. After a reload, L03 went to 2.
  - cases.json: K01–K07, seven conversions (Sharp + hidden, Fast with no text layer, 4:3, 60 slides, .ppt and .odp through the server), cost 1 trial use and one `usage.log` POST.
  - This is the same root cause as FDP-44, -45, -46 and -47.
- **Server conversion for OOXML variants:**
  - A real .ppsx (and .pptm/.potx/.pps/.key copies, which were renamed .pptx) is uploaded to `presentation.convert`.
  - It comes back as "This file is already PowerPoint (.pptx). Pick a different format to convert to." That message belongs to the converter tool, so these files can't be converted at all, though the picker accepts them.
  - Opening OOXML variants locally as .pptx would also keep them off the server.
- **Text layer:**
  - Hindi lands in the text layer as broken text ("नम ते", "िह दी"), while the FAQ says these scripts aren't in the layer. Japanese and Arabic are correctly left out.
  - With the text layer on, a 60-slide deck took about 51 s against about 6 s with it off.
- **Copy:**
  - The FAQ has three duplicated questions: hidden slides, searchable text, and old .ppt.
  - The large-file thresholds disagree: the drop zone says 50 MB, Limitations says 40 MB.
  - The meta description says "Fast, right in your browser." Non-.pptx files go to the server.

**After you ship:**
- Rerun `px54-live.js left`: expect L02 to go 1→2.
- Rerun `px54-live.js cases`: expect +1 per conversion.
- Run `px54-ext.js`: .ppsx should preview.

## Intent

Someone needs to send a deck to people without PowerPoint: a client leave-behind, an application attachment, a board pack. It has to look exactly like the slides, keep widescreen, leave out hidden slides and notes, and be searchable, without uploading confidential slides.

The conversion delivers that. It's one of the best-looking outputs tested so far:
- **Faithful pages:** gradient backgrounds, charts with their data, tables, full-bleed pictures and non-Latin scripts all render correctly. The pages are sized exactly 16:9 (960×540 pt) or 4:3 (720×540).
- **Hidden slides and notes:**
  - The hidden slide is left out, and the result says "1 hidden slide left out".
  - Ticking "Include hidden slides" gives 8 pages.
  - Speaker notes never appear.
- **Searchable text:** the text layer makes the English text searchable, and the hyperlink stays clickable.
- **Quality options:** Fast, Default and Sharp change the image sizes exactly as the FAQ says (1280 / 1920 / 2560 px).
- **Speed:** 2.7 s per deck, and 60 slides in about 6 s without the text layer.
- **Old formats:** .ppt and .odp convert through the server with only small shifts.
- **Bad files:** renamed, truncated and zip-not-deck files get a clear "This is not a .pptx file" message. A .txt gets "This tool takes .pptx, .ppt, .odp or .key files".
- **At the limit:** a Convert at 10/10 opens the cap dialog, and both passes reach the email field or Stripe.

What undercuts it:
- **One trial use covers every conversion until the page reloads.**
- **.ppsx and other OOXML variants are accepted, then refused** with a message from another tool.
- **Blog contradicts the tool:** it calls .ppt a mistake, says selectable text shouldn't be expected, and says hidden slides must be unhidden first.
- **Locale pages are half translated.**

## Why: what the evidence says

- **P1, per-page-load charging** (left.json, cases.json, cases-r2.json):
  - Conversions 2 to 7 in one load showed no counter change and no POST.
  - The cap-crossing case (does the gate re-check after 10/10 mid-session?) wasn't reached and is unverified. The FDP-44 code path suggests it doesn't re-check.
- **P2, .ppsx / OOXML variants fail:**
  - The picker accepts .pps, .pot, .ppsx, .potx and .pptm.
  - A real LibreOffice .ppsx was uploaded (40 KB) and rejected with the converter message, in all three engines.
- **P2, blog accuracy** (/blog/convert-powerpoint-slides-to-pdf-for-handouts, Oct 24). Its "Common mistakes" list says:
  - "Uploading a .ppt legacy binary when the tool expects modern .pptx". The tool converts .ppt.
  - "Expecting selectable text for copy-paste from the handout PDF". The text layer is on by default.
  - In its FAQ: "Hidden slides? Omitted unless you unhide them before export". The tool has an "Include hidden slides" checkbox.
  - It says "Upload the deck", but .pptx isn't uploaded.
  - It files the post under "PDF Tools"; the tool lives in PowerPoint & Slides.
- **P2, locales:**
  - The H1, trial strip, pass labels and Quick Buy are translated (e.g. "PowerPoint zu PDF", "Schnellkauf", "4,99 $").
  - The title, meta, subtitle, privacy note, drop zone and options stay English on all 9 locales. /ar returns 404.
- **P3, Hindi text layer broken** (pdftotext of K01 shows "नम ते", "िह दी पाठ यहाँ है"). Searching or copying Hindi gives wrong text, though the picture is right.
- **P3, text-layer speed:** 60 slides took about 51 s with the layer and about 6 s without. The progress counter keeps users informed.
- **P3, .ppt path:** the hyperlink text comes out pale lavender (hard to read) and the picture-slide caption moves to the centre (K06 sheet). The page warns that layouts can shift slightly.
- **P3, Japanese kana** render in a different, smaller fallback font from the kanji (p6-crop). This depends on the box's fonts, so check it on real devices.
- **P3, server conversion before the gate:** .ppt and .odp files are uploaded and converted at 10/10, before the cap dialog. That's a server cost for users who can't convert anyway.
- **P3, copy:** duplicate FAQs, the 40 vs 50 MB mismatch, and the "Files never stored" badge next to the server path (disclosed, "deleted right after").
- **Video (PASS, minor):**
  - Current UI: Quality buttons, Include hidden slides, searchable text, strip "10 remaining today". The description says "10 trial usages every day", with no "free" wording.
  - Stale bits: breadcrumb "PDF Tools", "Search 200+ tools", the "200+ professional tools" card, no Save to Drive/cloud buttons, a "Preview first page" button.
  - YouTube tag "pdf tools". The title matches the VideoObject.
- **Devices:** all 200. The trial strip and drop zone are above the fold on every device except iPhone SE, where the drop zone is just below. iPhone SE has the site-wide 9 px header overflow. CLS ≤ 0.041.
- **axe:**
  - Desktop: label-content-name-mismatch (1), region (1).
  - Pixel 7: ad-label contrast (2). Keep the reserved slots and fix the caption colour.
- **Geo:** $1 / $4.99 (plus $3 / $9.99 on the Premium card) in all 6 contexts. The EU consent banner shows for de-DE and fr-FR only, confirmed in the screenshots.

## Outcomes we want

1. One trial use per conversion of a new deck. Downloading the same result again stays free, and the cap is re-checked mid-session.
2. .ppsx, .potx and .pptm open locally as .pptx, or are left out of the picker. No converter-tool messages.
3. Blog rewritten to match the tool: .ppt supported, text layer, the Include hidden slides checkbox.
4. Complex scripts either kept out of the text layer cleanly, or shaped correctly.
5. Locale pages translate the subtitle, privacy note, drop zone and options.
6. FAQ de-duplicated, and one large-file threshold.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (minor) | 9 decks converted correctly; .ppsx fails. |
| 2 | Completeness vs competitors | PASS (minor) | Compared with Smallpdf, iLovePDF, Adobe online and PowerPoint's own export: matches on fidelity, keeps hidden slides out, searchable layer, quality choice, local for .pptx. Missing (verified absent in the UI): handouts with notes, N slides per page, vector text (pages are images). |
| 3 | Ease of use | PASS | Preview with slide and hidden counts, clear options, progress with Stop, thumbnail strip. |
| 4 | Layout attractiveness | PASS | Clean; on iPhone SE the drop zone is just below the fold. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $1 email prompt (stopped); Quick Buy monthly → Stripe (stopped). |
| 6 | Information correct | PARTIAL | Mostly right; Hindi text-layer claim, 40 vs 50 MB, "Fast, right in your browser" meta. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 61, meta 88 (short), og-default, VideoObject + FAQPage (14, with duplicates). |
| 9 | Blog exists and accurate | PARTIAL | Two posts; the handout post contradicts .ppt support, the text layer and the hidden-slides option. |
| 10 | YouTube video exists | PASS | rnjZAS1Vulg embedded. |
| 11 | FAQ and guide correct | PARTIAL | Accurate, but 3 duplicate questions; the Hindi text-layer claim is wrong. |
| 12 | Video shows current capabilities | PASS (minor) | Current flow; stale breadcrumb, "200+" and result buttons. |
| 13 | Storage | Sign-in untested | Save to my cloud storage needs email sign-in. |
| 14 | Sharing | Sign-in untested | Save to Google Drive / Open from Google Drive → Google sign-in. |
| 15 | Downloads | PASS | Valid PDFs, correct page sizes, links kept, badge as intended; file name reuses the deck name. |
| 16 | Usage count | **FAIL (P1)** | Charged once per page load; 7 conversions for 1 use. |
| 17 | Categorization in section | PASS | PowerPoint & Slides. |
| 18 | Correct section of site | PASS | Breadcrumb matches (the video and blog still say PDF Tools). |
| 19 | AI need/demand | PASS | Real file conversion; a chat assistant can't do this. |
| 20 | Merge better? | No | Presentation Converter (C12) covers format changes. This tool's PDF options (hidden, text layer, quality) justify a dedicated page. |
| 21 | Remove? | No | Core conversion, L-243 PDF Toolkit. |
| 22 | Duplicates | C12: keep | powerpoint-to-images, -gif, -html and -video plus presentation-converter are siblings with different outputs; already cross-linked under "Related PowerPoint tools". |
