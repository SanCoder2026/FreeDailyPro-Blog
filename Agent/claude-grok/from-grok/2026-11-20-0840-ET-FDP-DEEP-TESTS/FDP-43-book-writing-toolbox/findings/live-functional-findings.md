Sent: 2026-11-21 05:21 ET

# FDP-43 Book Writing Toolbox: live functional findings (guest, 2026-11-21 04:25–04:49 EST)

**Raw data:**
- `evidence/json/`: cases-chromium.json (B01–B14), cases2-*.json (C01–C08, Chromium plus Firefox/WebKit subsets), cases3-chromium.json (D01–D03), probe.json, verify.json.
- `evidence/outputs/`: the preview files this browser received.
- The counter is `fdp-usage-v1.usageToday`, which is display-only evidence.

**Context:** this is a Workflow Product ($29.99 a month, 7-day trial, sign-in first).
- Clean downloads need the subscription.
- Previews are advertised as "unlimited and watermarked".
- Pre-flight is advertised as "Unlimited … no charge".
- ONIX export is advertised as "no subscription needed".

## Gate and trial uses
1. **Owner question (v2; not a bug, the watermark is intentional per owner rule): how strong the Book preview watermark should be.** The facts are below.
   - **Book PDF preview** (B01/B02/C01, at 0 = counter 10/10): the full typeset book, with fonts embedded and exactly the paid render.
     - The "PREVIEW" mark is a single tiling-pattern fill painted *under* the page content. It isn't text or an annotation.
     - Emptying that one pattern object gives a clean book (`evidence/screens/cases/B01-pattern-emptied-pages.png`, made offline from our own preview, not distributed).
     - The same mechanism is used on the manuscript PDF preview and the print-cover preview (`verify.json`: every preview PDF is `tiling_pattern_pages == pages`, with no "PREVIEW" text).
     - In Chromium the preview PDF is also a blob in an iframe, and headless Chromium saved it as a file (`B05-pdf-….pdf`). Ordinary users can save it from the viewer.
   - **Manuscript .docx preview:** a complete Shunn manuscript in an editable Word file. The only watermark is one red line in the page header ("PREVIEW COPY -- download the full, watermark-free edition at FreeDailyPro.com"), which is deleted in one step (`verify.json`: `word/header1.xml`, `word/header2.xml`; body clean).
   - **Options if Santosh wants it stronger:** draw the mark *over* the content as part of each page's content stream, rasterise previews (or lower their resolution), and put the docx mark in the body (e.g. a diagonal text box in every section, plus a short sample instead of the full manuscript).
2. **P1: per-page-load charging of "unlimited" previews.**
   - The manuscript .docx preview and the ONIX export save through ToolPage's shared download helper (`ToolPage d → vt → Sa`), which takes a **Professional trial use** once per page load.
   - D02 (with uses left, 04:47–04:49 EST): preview #1 went 0→1/10, preview #2 and ONIX in the same load stayed 1/10, then after a reload the next preview went 1→2/10. C08 confirms (0→1 on the manuscript preview; `POST usage.log`).
   - The copy says "Preview is unlimited" and "ONIX … no subscription needed". The Professional quota isn't part of this product's offer ("The $1 Day Pass and the $4.99 plan do not cover it").
   - Book PDF preview, cover preview and Pre-flight never charged (they use an iframe, not the helper).
   - **Fix:** pass `{free: true}` (or the product's own rule) to the helper for previews and ONIX.
3. **P1: at 0 trial uses, the manuscript .docx preview and ONIX export silently do nothing** (D01, 04:47 EST).
   - The server still renders the .docx (`POST bookMaker.renderManuscriptDocx`), but no file, dialog, message or offer appears (`evidence/screens/cases/D01.png`).
   - A guest who has used the Professional trial uses elsewhere can't get the "unlimited" manuscript preview or the "free" ONIX file, and doesn't learn why.
4. **Checkout path (stopped at sign-in):**
   - Download, Export Manuscript (.docx/.pdf), Download print cover and Export EPUB all open the same dialog: "Book Writing Toolbox: $29.99 a month … 7-day trial … The $1 Day Pass and the $4.99 plan do not cover it" (B03/C02).
   - The "Start 7-day trial · $29.99/mo" strip button opens the same dialog (B04).
   - Its button took the guest to **/profile "Sign In to Your Account"** (Google or emailed code). **Stopped there; nothing typed. The trial/Stripe step is untested (sign-in).**
   - On /profile, a display ad sat on top of the left part of the sign-in card at 1366×900 (`B03b.png`). Give that page a reserved ad slot outside the form.

## Core features
| Case | Result |
|---|---|
| B01/C01 Write + Preview | Typeset 6×9 PDF with title, copyright, chapter, running heads, folios and a drop cap, in about 9–12 s. Headless Chromium/Firefox/WebKit can't show PDFs in the iframe ("This PDF can't be displayed here" in Firefox), so we inspected the file itself. The preview dialog has **two close (X) buttons** (P3). |
| B02/C07 Pre-flight | Trim, page count (min 24), gutter, ISBN and cover resolution checks are clear and correct (300×450 → warning, 1800×2700 → pass). **But the EPUB checks never appear**: the EPUB build returns 500 and Pre-flight still says "complete" (P1, see below). |
| **EPUB** | **P1: `bookMaker.renderEpub` returned HTTP 500 "Couldn't generate the EPUB right now" on 11 of 11 calls** (04:26–04:47 EST; Chromium, Firefox, WebKit; with or without cover/author). Preview EPUB gives no file. The paid Export EPUB uses the same mutation (`preview: false`), which is unverified behind sign-in but very likely broken too. |
| B05/D02 Manuscript | .docx and .pdf previews are a correct Shunn format (legal name, word count "about 100 words", running head "Tester / THE HARBOUR TEST / 2"). The legal-name requirement is enforced. |
| B07 Covers | Front/back upload, the Cover Preview dialog (wraparound with the spine at the 24-page minimum, explained), Measure page count, and the print-cover preview (one 12.26×9.25 in page with bleed) all work. |
| B08/C06 Import | .docx: chapter, image, table, bullets and accents kept, scene break kept. Splitting by Heading 1 and by "Chapter 1 / Chapter Two: The Fog / Chapter 3 - The End" lines matches the blog. Text before the first chapter becomes its own chapter (documented). A .md file forced through the picker imports as plain text with literal `#`/`**` (it isn't offered by the picker; fine). |
| B09 CJK | Blocked before rendering with a precise named-script message, "Nothing was used or charged". **P2 copy conflict:** the toast says Bengali, Tamil, Telugu, Gujarati, Kannada and Malayalam **are** supported; the FAQ and Limitations say they are **not available yet**. |
| C04 Arabic | "Auto" detected right-to-left; the Arabic was shaped correctly and set RTL. P3: the English copyright boilerplate is set RTL, so its punctuation flips ("All rights reserved 2026 ©."), and the default heading "Chapter 2" stays English. |
| B13 Long book | 400 paragraphs → 257-page preview in about 9 s. PASS. |
| C03 Platforms | 8 platform choices. Ebook (Draft2Digital) switches to Ebook only and hides Spine/Back Cover (PASS). **P3/unverified:** the trim list is the same 18 sizes for Use default and IngramSpark, although the copy says the platform "filters the trim size list down to sizes that platform actually supports". Needs a check with a clean selection. |
| B11/C05 Projects | My Books lists books and starts new ones; the chapter text survives a reload (D03 PASS). "Clear everything" warns clearly. Invalid project file: "That file is not a saved FreeDailyPro book project." PASS. **P2:** "Save book project" saves **only metadata** (title, trim, platform: 423 bytes, no chapters). Next to "Clear everything … there is no other copy", writers can mistake it for a backup. Add a full local backup (chapters + images) or rename it "Save book details". |
| B11 ONIX | Valid ONIX 3.0 skeleton built from the entered fields. |

## Privacy
- The draft stays in IndexedDB.
- Preview, Pre-flight and export POST the book to first-party `/api/trpc/bookMaker.*` only, as the page says.
- No third-party request carried book content in our logs (only first-party tRPC calls were logged; ad and analytics traffic is the usual page traffic).

**Size note:** the 257-page long-book preview (B13) is cut to its first 6 pages (`…-first6of257pages.pdf`). The full file's check result is in `evidence/json/verify.json`.
