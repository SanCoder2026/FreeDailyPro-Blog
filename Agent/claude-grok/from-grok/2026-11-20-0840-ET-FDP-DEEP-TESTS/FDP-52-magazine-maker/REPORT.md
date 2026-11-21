Sent: 2026-11-21 09:19 ET

# FDP-52 Magazine Maker (magazine-maker): deep test report for Claude

- **Written:** 2026-11-21 09:17 EST (box `date`, ET). Testing ran 2026-11-21 08:44–09:14 EST.
- **Tool:** https://www.freedailypro.com/tool/magazine-maker
  - Row 52 of TEST-ORDER.md: **Premium Application** in Publishing & Print Makers (breadcrumb: Premium Applications).
  - Plan note: "test-plan (unranked): GA top-traffic".
  - Duplicate group C40 (catalog-maker, print-publication-studio, user-manual-writer).
  - Video: AEV2y69z1t0. Blogs: /blog/assemble-magazine-or-newsletter-pdf-with-toc and /blog/edition-ledger-and-print-and-web-pdfs-for-a-catalog-series.
  - **GSC data is not available.** The API side was not tested (no API/MCP testing).
- **Offer:**
  - 2 Premium trial uses a day, $3 Day Pass / $9.99 monthly.
  - Building and previewing cost nothing. Each *new* export is charged at Download (`logExportNow(contentKey)`). Re-downloading the same build is free.
  - Trial PDFs carry the intentional "Created with FreeDailyPro.com" badge on every page, and the result area says so before you download.
- **Two modes, both built in the browser with pdf-lib:**
  - **Write articles:** articles with Markdown, one picture each, 1–3 columns, Letter/A4, accent colour, cover with an optional image, "In this issue" page, column templates, contents styles, logo, brand profile, and save/open issue (.issue.json).
  - **Combine files:** PDF, .docx, .txt and images assembled with a cover, masthead, contributors, TOC and a list of images, all on US Letter pages.
- **Testers:**
  - **Desk review:** copy (14 FAQs), Details, JSON-LD, the two blogs, JS (`MagazineMaker-BxIyBOvc.js`).
  - **Headless Playwright runs:**
    - At the cap: zero.json (both modes, templates, files, dialogs, passes).
    - Fresh contexts with uses left: left-run2, left3 (per-export check), left4 (Combine download).
    - focus.json: result area, templates, WebP.
    - Firefox and WebKit subsets, plus a WebKit gate and crash isolation run (wk-checks-webkit.json).
    - Phone overflow probe.
  - **Outputs:** every PDF checked with pdfinfo, pdffonts, pdfimages and pdftotext, and rendered to PNG for visual review.
  - **Video:** frame by frame.
  - **Matrix:** 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Premium Day Pass email prompt and at Stripe Checkout.
  - No ad clicks, no API/MCP calls, no site or repo changes.
  - The only password typed was the test PDF's own (u123).
- **Sign-in (untested):**
  - Save to Google Drive: Google popup with uses left; cap dialog at 0.
  - Save to my cloud storage: "Sign in with your email first", $4.99/mo add-on.
  - Open from Google Drive (Combine): Google popup.
  - Paid-pass output without the badge.
- **RERUN-AFTER-RESET:** none. Nothing is pending a usage reset; both modes were downloaded with uses left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:**
- Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. **Neither happens here.** Charging is per export and correct, and only "Preview first page" is visible at 0.
- The badge is intentional.

**Code to look at:**
- **Combine files, accepted types:**
  - The `accept` list includes `image/webp,.heic,.heif`, but assembly rejects WebP with "isn't a supported file type — use PDF, Word (.docx/.txt), or an image".
  - The FAQ says WebP and HEIC work, and even notes that the warning text disagrees.
- **`imagePdf-Dtz8PQyf.js` `normalizeImageFile`** (Combine path): a WebKit tab crash on JPG. It reproduced in two separate WebKit runs. The same JPG in Write articles mode works in WebKit. FDP-48 (Image to PDF) crashed the same way.
- **"Contents page style" select trigger:** `whitespace-nowrap` on a 409 px label makes every phone page 442 px wide.
- **Non-Latin text:** Devanagari, CJK and Arabic are drawn as outlines via fontkit. They look right, but they aren't selectable or searchable. Arabic is left-aligned, with the final period at the wrong end.

**After you ship:**
- Rerun `px52-live.js left3` (expect +1 per new export) and `left4`.
- Run `px52-wk.js webkit`. Combine with a JPG should no longer crash.
- Rerun `px52-overflow.js` (expect scrollWidth = viewport).
- Run Combine with img_wide.webp: it should assemble.

## Intent

A club secretary, school office, HR or comms person wants a real-looking issue (cover, contents, page numbers, consistent header) from articles they already have, without learning InDesign and without uploading staff content. The Premium price ($3 day / $9.99 month) has to feel worth it the first time they see the PDF.

The core earns that:
- **Write articles gives a credible magazine in under a second:**
  - Dark accent cover with the title over the cover photo, and the logo on every page.
  - An "In this issue" page with correct page numbers, and titles cut cleanly at 60 characters.
  - Two-column body text with Markdown headings, bold, italic, bullets and numbers.
  - A full-width picture under each headline, and a running header with the title.
- **Templates** (Feature issue / Photo feature / Report) pre-fill sensible section names, placeholders, columns and page size.
- **Save issue → reopen** restores everything, including pictures (185 KB JSON).
- **Errors are clear:** bad JSON, wrong app, unknown brand file, bad image, empty issue and a damaged PDF all get specific messages. Emoji get an upfront note.
- **Combine files builds a correct 20-page issue** from a .docx, three PDFs, a JPG, a .txt and a password PDF (unlocked inline):
  - Masthead (ii), Contributors (iii), TOC and List of Images (v).
  - TOC page numbers match the real pages (1, 3, 6, 7, 11, 12, 13).
- **Trial use is fair:**
  - Build and preview are free.
  - Re-download is free.
  - Each new export is +1 (E01 0→1, E02 edited 1→2).
  - At the cap, the dialog is consistent in Chromium, Firefox and fresh WebKit contexts.
- **Privacy:** no POST carries document content. The only GETs are font files and chunks from the site's own domain.

What undercuts it:
- **WebP:** a WebP file is accepted and listed, then blocks the whole Combine assembly.
- **Safari risk:** WebKit crashes on a JPG in Combine.
- **Phones:** every phone gets a 442 px wide page (iPhone SE scrolls 122 px sideways).
- **Old video:** it shows a different, upload-only "Pro/PDF Tools" tool with "10 free uses daily" and a personal macOS file picker.
- **Weak Combine cover:** it's a plain white page, with no cover image even though the blog tells users to upload one.

## Why: what the evidence says

- **No P0/P1 confirmed.** The gate and trial counting behave as the FAQ promises:
  - left3: E01 0→1, then E02 (edited) 1→2, with 2 `usage.log` POSTs.
  - left-run2: L01b re-download was free. L02/L03 (edited) at 2/2 opened the cap dialog.
  - Fresh WebKit contexts at 2/2 got the cap dialog 3 out of 3 times.
- **P2, Safari risk (WebKit tab crash in Combine with a JPG):**
  - subset-webkit crashed while assembling (.docx + PDF + JPG).
  - Isolated in wk-checks-webkit.json: memo PDF, .docx and .txt each assemble; img_wide.jpg alone crashes the tab.
  - Treat this as P1 if a real Safari/iOS check reproduces it. This box runs Playwright WebKit, not Safari.
- **P2, WebP breaks Combine.**
  - The picker accepts .webp and the file appears in the list (title "img wide").
  - Assemble then shows the toast "img_wide.webp isn't a supported file type — use PDF, Word (.docx/.txt), or an image". The button stays at "Assemble Issue" with no output, even when other valid files are present (Z-C01, F-C03).
  - The FAQ says WebP and HEIC are taken. HEIC is unverified (no HEIC test file).
- **P2, phone layout.**
  - The Contents-page-style trigger ("List: Title and author, page number on the right.", nowrap, 409 px) makes scrollWidth 442 on iPhone SE (vw 320), iPhone 14 Pro Max, Pixel 7 and Galaxy S9+.
  - Chromium phones zoom the page out (innerWidth 442), so all text gets smaller (overflow.json).
- **P2, video (check 12 FAIL):**
  - Old UI: breadcrumb "PDF Tools", a "Pro" badge, "10 free uses daily", "0 free uses remaining today", and Combine-only (no Write articles, no templates).
  - Overlay "Download your magazine as a PDF — 10 free uses daily!".
  - Wording: "FREE · PRIVATE · NO LOGIN", the "200+ Free Productivity Tools" end card, and the title "How to Use Magazine Maker – Free Step-by-Step Walkthrough".
  - Description: "Try Magazine Maker free … Free daily uses … no account needed".
  - A personal macOS file picker shows a home-folder name, colour tags and personal file names (f34crop.png). The result is opened in Adobe Acrobat.
  - The page's VideoObject name ("How to Make a Magazine PDF Online – Cover, TOC & Articles") doesn't match the YouTube title.
- **P2, Combine-mode cover and blog accuracy.**
  - The Combine cover is a white page with the title and editor in serif type (K01 page 1).
  - There's no cover image control in Combine mode (verified control list). The blog says "Upload the cover image. Upload articles as PDF, Word, or images".
  - The blog's "drag them into reading order" is unverified; the FAQ and UI describe arrow buttons.
- **P2, locale pages:** the H1 is translated (e.g. "Magazin-Ersteller"). These stay English on all 10 locales: the title, meta, subtitle, "Premium application · 2 trial uses a day · $3 day pass or $9.99 a month", "Day pass $3 / Monthly $9.99", the breadcrumb "Premium Applications" and the builder labels.
- **P3 items:**
  - **Non-Latin text:** Hindi, Japanese and Arabic render correctly but as shapes, not text (pdftotext returns blank lines), so they aren't searchable or accessible. Arabic is left-aligned, with the period on the right.
  - **Front-matter folios:** the TOC page has no number, so the sequence goes ii, iii, —, v.
  - **Combine file titles:** they default to "column letter 3p"-style file names (the blog advises renaming them; a "Use first heading" option would help).
  - **Hero image:** on desktop 1366×900 the large hero image pushes the builder below the fold.
  - **SEO:** og-default image. Meta is 158 characters (long). Title 60.
  - **axe:** label-content-name-mismatch (1), region (1), Pixel 7 ad-label contrast (2).
  - **WebKit subset:** one context showing 2/2 downloaded without a dialog (S01-webkit). A fresh-context recheck showed the gate correctly, so this is likely server-side count drift (unverified; seen in FDP-50 too).
  - **Strip display:** after one download the strip sometimes jumped 0→2 (left-run2, left4) with a single `usage.log`. This is display sync with a server count from earlier contexts (unverified).

## Outcomes we want

1. WebP (and HEIC, if it's claimed) work in Combine. Otherwise the picker and FAQ stop offering them, and a bad file never blocks the others.
2. Combine with JPGs works in Safari/iOS.
3. Phones render at device width.
4. A re-recorded video of the current two-mode tool, with no "free" wording and a clean profile.
5. Combine mode gets the same accent/cover-image treatment as Write articles, and the blog matches the UI.
6. Locale pages translate the subtitle, offer line and builder labels.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (minor) | Write: 7-page issue in 0.46 s; Combine: 20 pages in 9 s, TOC correct; WebP fails. |
| 2 | Completeness vs competitors | PARTIAL | Compared with Canva, Adobe Express, Lucidpress/Marq and FlipHTML5: no free-form layout, captions, pull quotes or spreads (documented), but real auto-TOC, Markdown, local privacy and file assembly. Combine cover is weak. |
| 3 | Ease of use | PASS | Clear modes, templates, inline errors, emoji note, save/reopen. |
| 4 | Layout attractiveness | PARTIAL | Polished desktop; phones forced to 442 px; hero pushes the builder down. |
| 5 | Payment process | PASS / stopped | Cap dialog → Premium Day Pass $3 email prompt (stopped); Quick Buy monthly → Stripe (stopped). |
| 6 | Information correct | PARTIAL | WebP claim false; blog cover-image step wrong; the rest matches (60-char TOC, columns, templates, privacy). |
| 7 | Indexing | PASS | 200, index, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 60; meta 158 (long); og-default; VideoObject name ≠ YouTube title. |
| 9 | Blog exists and accurate | PARTIAL | Two linked posts; the assemble post describes a Combine cover image that doesn't exist. |
| 10 | YouTube video exists | PASS | AEV2y69z1t0 embedded. |
| 11 | FAQ and guide correct | PARTIAL | 14 detailed answers; the WebP/HEIC answer contradicts behaviour (and admits the warning mismatch). |
| 12 | Video shows current capabilities | **FAIL** | Old Combine-only UI, "10 free uses", "free / no login", personal file picker. |
| 13 | Storage | PASS / sign-in untested | Save issue to device + reopen works; cloud storage needs email sign-in + $4.99. |
| 14 | Sharing | PASS / sign-in untested | Share this tool present; Save to Google Drive needs Google sign-in. |
| 15 | Downloads | PASS (minor) | Valid PDFs, badge as intended, fonts embedded for non-WinAnsi; Helvetica not embedded (standard 14). |
| 16 | Usage count | PASS | Per export (+1 per new content, re-download free); consistent across browsers. |
| 17 | Categorization in section | PASS | Publishing & Print Makers / Premium Applications. |
| 18 | Correct section of site | PASS | Publishing hub + Premium hub; ladder to Print & Publication Studio shown. |
| 19 | AI need/demand | PASS | GA top-traffic; a chat assistant can't hand back a paginated PDF issue with a TOC locally. |
| 20 | Merge better? | No | Combine overlaps Document Assembler/Merge PDF (per the blog), but the issue framing (cover, TOC, list of images) is distinct. |
| 21 | Remove? | No | Top traffic. |
| 22 | Duplicates | C40: keep | catalog-maker (products), user-manual-writer (manuals) and print-publication-studio (Workflow wrapper) are a ladder, not duplicates. Make the ladder explicit (already in the CTA). |
