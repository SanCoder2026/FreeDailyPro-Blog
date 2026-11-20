Sent: 2026-11-20 08:40 ET

# FDP-05 Split PDF (split-pdf): deep test report for Claude

- **Written:** 2026-11-19 11:46:13 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/split-pdf. Row 5 of TEST-ORDER.md, cluster C09 (with extract-pdf, remove-pdf-pages, rotate-pdf and organize-pdf, the last a Premium Application).
- **Classification:** Professional Tool, PDF Tools. 10 trial uses per day. **Split is free; Download is gated.** $1 day pass / $4.99 monthly.
- **Testers:**
  - Desk review: curl, JS bundles, FAQ and Details, blog, sitemap, 10 locale URLs, WebSearch competitors.
  - YouTube video: metadata, captions and 16 frames.
  - Headless Playwright:
    - 14 generated inputs (bookmarks and links, mixed sizes and /Rotate, single page, password, owner-restricted, 300 pages, non-Latin, form, 5 bad files, a JPG)
    - 12 split scenarios
    - 13 range-field inputs
    - the cap dialog for row and ZIP downloads, and the cloud dialog
    - keyboard, focus and axe on the result view
    - matrix: 10 device/browser profiles, 10 locales plus /ar, 6 countries, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls (the RapidAPI split endpoint is out of scope), no site or repo changes.
- **Not tested (sign-in):** Open from Google Drive, Save to Google Drive and Save to my cloud storage (email sign-in, a $4.99 add-on), all on https://www.freedailypro.com/tool/split-pdf.
- **Not observable today: downloaded outputs.**
  - 21 of the 22 fresh contexts whose count was readable loaded at "0 remaining today". The one at 10 (geo hi-IN) was a matrix page load.
  - So every output-file check is marked **needs re-run after midnight UTC (7:00 PM ET)**: page order, sizes and /Rotate, bookmarks, links, forms, non-Latin text, unlocked = unencrypted, the badge, the 300-file ZIP, and the cost per file vs. per ZIP.
  - `scripts/sp-battery.js` is ready to run, and the tool is listed in `/workspace/deep/RERUN-AFTER-RESET.md` (a copy is at `scripts/RERUN-AFTER-RESET.md`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components (SplitPdf, PdfPageThumbnails, the range parser, the result row and download stamp, UsageAndUpgradeStrip and the tool's content entry: FAQ, Details, Limitations, blog links), then:

- Restate the problem.
- Challenge anything that looks wrong.
- Pick the fix that fits how FreeDailyPro has shipped similar work.

After you ship, rerun `test-cases.md` (SP-01…SP-47).

## Intent

People arrive with one combined PDF (a scan of several contracts, a statement bundle, a book) and need **the right pages in the right separate files** to send or file, without uploading it. They should:

1. **Get it right first time.**
   - Type ranges, see exactly which pages land in which file, and download one file or one ZIP.
   - The engine already does this very well: 300 pages split in 1.1 s; bookmarks and form fields reported as kept; clear inline errors.
2. **Feel "wow":**
   - live range validation
   - "every N pages" auto-fill
   - combine-and-reorder
   - per-file summaries
   - inline unlock of password PDFs
3. **Meet an honest offer.** A trial use is spent at download, and the mark is stated before download (this tool already does that).

## Why: what the evidence says

**Strong:**
- **The range parser is excellent.**
  - Errors are inline with aria-invalid: start after end, out of range, not a number, empty.
  - It tolerates en dashes, "8-" open-ended, double commas, semicolons and spaces.
- **Fast.** 300 pages → 300 files in 1.1 s.
- **Clear results.** Each row says "pages 1-3 · 3 pages · 1.8 KB · 3 bookmarks kept" and "2 form fields kept". A single-page PDF gets a clear explanation.
- **The mark is disclosed per file before download.** That's better than merge-pdf and compress-pdf.
- **No layout problems on the phone result view** (Pixel 7 at 412 px), and axe finds 0 violations on the result view.

**What breaks trust:**
1. **Fresh visitors can't download** (P0, shared). 21 of 22 readable fresh contexts loaded at 0 remaining (display-only, one busy box IP). Users split, see the result, then get "Get a Day Pass to download".
2. **The page copy contradicts the tool:**
   - Limitations says "Password-protected PDFs need their password removed first". The FAQ and the live tool unlock inline.
   - The Details section is generic template text ("you typically have two ways… checkboxes on thumbnails… often as a zip archive"). The thumbnails are not selectable.
   - WebSearch shows this text in the snippet.
3. **The blog promises a feature that doesn't exist.**
   - /blog/split-pdf-multi-contract-client-packets tells users to "name the output" per range (ClientA-purchase-….pdf). There is no name field; outputs are auto-named.
   - It also implies testing ranges spends trial uses (only download does).
   - The tool page doesn't link to this post at all.
4. **Locales:** all 9 locale URLs serve the English title and meta (even /es), and the client UI is half translated.
5. **Small-screen empty state and result rows:**
   - iPhone SE overflows to 329 px, and the drop zone is below the fold on SE and Galaxy S9+.
   - On desktop the file names in rows are truncated to about 100 px, so the parts look identical.
   - Focus drops to BODY after Add and after Split.

## Outcomes we want

- A new visitor sees 10 remaining and spends a clear, stated amount per download (per file or per ZIP; say which).
- Every sentence in About, How to use, Details, Limitations, the FAQ, the blog and the video describes this tool as it is today: inline unlock, typed ranges, Every page, every-N, Combine, auto-names, ZIP.
- The tool page links its own guide. The blog's steps can be followed exactly, or the tool gains per-range naming.
- Locale pages have localized titles and meta, or they leave hreflang.
- Result rows lead with what the user needs to tell the parts apart (the range), and focus lands on the result.

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PASS** (UI); outputs **need re-run** | MEDIUM | All 12 split scenarios behave as documented (SP-01…SP-12). Output content (order, rotation, bookmarks, forms, text, encryption, badge) **not verified: needs re-run after midnight UTC**. `evidence/findings/live-functional-findings.md`, `json/explore-*.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Ranges, Every page, every N, combine-and-reorder, inline unlock, bookmarks and forms kept, per-file summaries. Missing vs FormatDesk, HerePDF and SplitPDF.io: **split by bookmarks** (named per chapter), **split by size** (email-sized parts), odd/even, tap-to-select pages, per-range file names. Live-verified absent in the UI: per-range naming and thumbnail selection. The other modes are an unverified absence beyond the visible controls. `desk-findings.md` |
| 3 | Ease of use | **PASS** (minor) | LOW | Best-in-class range validation and hints. Minor: two identical split buttons; overlapping or duplicate ranges accepted silently; non-PDFs called "damaged, try Repair"; focus lost after Add and Split; no owner-restriction notice. |
| 4 | Layout attractiveness | **PARTIAL** | MEDIUM | Clean dark UI, no ad overlaps, CLS ≤ 0.027, Pixel 7 result view fine. iPhone SE 329 > 320; drop zone below the fold on SE and S9+; file names truncated at about 100 px on desktop rows; ja overflows by 3 px. `screens/devices/iphone-se-fold.png`, `screens/live/kbd-result-view.jpg` |
| 5 | Payment process | **PASS** (as observed) | LOW | The mark is stated per row before download. The cap dialog ("Your input stays where it is", $4.99 monthly / $1 day pass, access code) appears for row and ZIP downloads. Quick Buy is the same strip as FDP-02 to FDP-04 (not re-clicked). `screens/live/capped-zip-click.png` |
| 6 | Information correct | **FAIL** | HIGH | Limitations ("password removed first") contradicts the FAQ and the live inline unlock. Details claims thumbnail checkboxes (not present). The blog claims per-range naming (not present) and implies splitting spends uses. `html/tool-visible.txt` lines 61–82, `html/blog-visible.txt` lines 53–62, `json/kbd.json` thumbClick |
| 7 | Indexing | **PASS** | — | 200, indexable, self canonical, in the sitemap (lastmod 2026-11-19) with a video block; WebSearch ranks the tool first for "freedailypro split pdf". **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title intent ("by page range or every page"), 137-char meta, 9-question FAQPage, VideoObject, breadcrumb. Issues: no brand suffix; bare H1 "Split PDF"; 9 locales with an English head (self canonical); generic OG image; Offer without a billing period; 1 empty alt. |
| 9 | Blog post | **PARTIAL** | HIGH | /blog/split-pdf-multi-contract-client-packets (2026-10-17) is a strong use case with the video embedded. But: **not linked from the tool page**; per-range naming promised; "10 trial usages if you are testing ranges" is misleading. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | 0jI1pCsuiqI, 82 s, 1 view, embedded on the tool and blog, on-topic tags, one consistent title across YouTube, JSON-LD and the sitemap. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | The 9 FAQ answers held live, including inline unlock and Every page. The Details/How-to-use text is generic and inaccurate, and Limitations is stale. The open-ended "8-" and the semicolon syntax are undocumented. |
| 12 | Video shows current capabilities | **PASS** (minor) | LOW | It shows today's dark UI, ranges, Every page, every-N, Combine and the ZIP. Minor: "200+ professional tools" on the card (now 300+), and the narration "the next **free tool**" (off-brand). `evidence/video/frames/`, `video/video-0jI1pCsuiqI.en.vtt` line 215 |
| 13 | Storage | **PASS** (by design) | — | Local-only processing; nothing persists on reload. Cloud storage is a $4.99 sign-in add-on (untested). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" is present. No result share (fine for private files). Save to Google Drive needs sign-in (untested). |
| 15 | Downloads | **N/A today (needs re-run after midnight UTC)** | — | Every context that could act was capped, so nothing could be downloaded. Row and ZIP Download both open the cap dialog. Per row: "This download will carry a small 'Created with FreeDailyPro.com' badge…". |
| 16 | Usage count | **PARTIAL** | HIGH | Split, Every page, Combine, unlock and the 300-page split never needed a use (all ran at 0). Per-file vs per-ZIP counting **needs re-run after midnight UTC**. 21 of 22 readable fresh contexts at 0 (display-only). |
| 17 | Categorization | **PASS** | — | PDF Tools, Professional Tool. |
| 18 | Location in site | **PARTIAL** | LOW | Breadcrumb Home › PDF Tools › Split PDF; "Part of: Splitting and Sharing a Large PDF"; next step Rotate PDF; related Delete Unwanted Pages and PDF-to-Excel guides. Missing: its own blog post. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic ranges are right. P2 idea: "split by bookmarks/text" covers the multi-contract use case without AI. Demand: rank 7, 94 views in the site map (GSC not available). |
| 20 | Merge? | **PASS: keep standalone** | — | It overlaps Extract Pages & Text, Remove PDF Pages and Organize PDF (Premium), but About already points single-page and text needs to Extract. Cross-link the C09 set. |
| 21 | Remove? | **N/A: keep** | — | Core tool. |
| 22 | Duplicates | **PARTIAL** | LOW | Functional overlap within C09 (see 20). No exact duplicate page found. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles (Chromium, Firefox, WebKit; phones, tablets, desktops).
- No ad overlaps.
- Compact phone strip.
- Correct `lang` per locale.
- The Pixel 7 result view has no overflow.
- Keyboard: Enter opens the chooser; Split works by keyboard.
- Result view axe clean.

**FAIL / PARTIAL:**
- iPhone SE overflow and the drop zone below the fold on small phones (MEDIUM).
- English title and meta on 9 locales; mixed UI headings (MEDIUM-HIGH).
- ja overflows by 3 px; /ar 404; USD only in 6 geos.
- axe on the empty page: desktop label-content-name-mismatch (serious, 1); Pixel 7 "Advertisement" caption contrast (serious, 2).
- Focus lost after Add and after Split.

**Ads:** keep them, in reserved fixed-height slots below the tool and between sections (as now). Never between the result rows and their Download buttons.

## Suggested direction (interpret freely)

1. **Trial meter (P0, shared).** Same investigation as FDP-02 to FDP-04: why fresh `dev:` scopes from this IP show `usageToday 10`. Verify server-side. Then state in the strip or rows whether a ZIP costs one use.
2. **Copy truth pass (P1).**
   - Rewrite Details/How to use from the real UI.
   - Fix Limitations (inline unlock).
   - Document "8-", semicolons and every-N.
   - Fix the blog's naming step: remove it, or ship per-range names (a name field per range, or a "Name pattern" box).
   - Change "testing ranges" to "downloading".
   - Link the post from "Guides and next steps".
3. **Locales (P1, shared).** Server-side title, meta and H1 for es…id, translated section headings, or drop the locales from hreflang.
4. **Rows and small screens (P2).**
   - Lead each row with "Pages 1–3" and wrap or shorten the base name.
   - Fix the 320 px overflow, and get the drop zone above the fold.
   - Move focus to the result summary.
   - Remove the duplicate split button.
5. **Product (P2).**
   - Split by bookmarks and by size (the competitors' main differentiators, and a fit for the blog's use case).
   - An overlap/duplicate note.
   - Specific errors for non-PDFs.
   - An owner-restriction notice.
   - Video: "Professional Tool" in the outro, "300+".

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy claim ("Runs on your device"). It was not network-audited here.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect SplitPdf, the range parser, the result row, the download stamp, the usage router and the content entry → restate → propose → implement → verify with `scripts/` and `test-cases.md` (the downloads part after midnight UTC).
