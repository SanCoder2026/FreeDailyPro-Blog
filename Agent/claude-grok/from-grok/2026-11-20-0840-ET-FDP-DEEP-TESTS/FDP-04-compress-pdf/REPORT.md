Sent: 2026-11-20 08:40 ET

# FDP-04 Compress PDF (compress-pdf): deep test report for Claude

- **Written:** 2026-11-19 11:25:23 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/compress-pdf. The slug is from TEST-ORDER.md row 4 and tools.csv.
- **Classification:** Professional Tool, PDF Tools. 10 trial uses per day, **spent at Download** (Compress, Compare and the batch run are free), $1 day pass / $4.99 monthly.
- **Testers:**
  - Desk review: curl, JS bundle read, FAQ and Details, blog, sitemap, 9 locales, WebSearch competitors.
  - YouTube video: metadata, captions and 17 frames. **Not** watched with sound.
  - Headless Playwright:
    - 17 generated inputs (photo-heavy, text-only, grey scan, links/bookmarks/form, password, owner-restricted, non-Latin, mixed sizes and rotation, CMYK, 72 MB, already-small, 5 bad files, a JPG)
    - 31 compress, target, validation and batch scenarios
    - input validation, Run anyway, Compare
    - cap dialog, Quick Buy and the cloud dialog
    - keyboard, focus and axe on the result view
    - matrix: 10 device/browser profiles, 10 locales plus /ar, 6 countries, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API/MCP calls (the /developers compress endpoints are out of scope), no site or repo changes.
- **Not tested (sign-in):** Open from Google Drive, Save to Google Drive and Save to my cloud storage (email sign-in, $4.99 add-on), all at https://www.freedailypro.com/tool/compress-pdf.
- **Not observable today:** downloaded outputs. **28 of 31 fresh contexts loaded at "0 remaining today"**, and the 3 uncapped ones were matrix page loads. Every output-file check (structure kept, text, the mark, ZIP, true bytes vs. target, per-download counting) is marked **needs re-run after midnight UTC** (7:00 PM ET), with `scripts/cp-battery.js` ready.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components (CompressPdf, its level runner and scan/CMYK classifier, imageRecompress, target, BatchRunner, PdfBeforeAfter, useDownloadedResult, UsageAndUpgradeStrip, and the branding stamp on downloads), then:
- Restate the problem.
- Challenge anything that looks wrong.
- Pick the fix that fits how FreeDailyPro has shipped similar work.

After you ship, rerun `test-cases.md` (CP-01…CP-43).

## Intent

People arrive with a PDF that is too big for an email or a portal ("under 2 MB", "under 200 KB"). They want it under the limit **in one go, still readable**, without uploading it. They should:
1. Hit their size target with the gentlest result that fits. The engine already does this impressively: 18 MB → 327 KB in 5 s with text intact; 72 MB → 1.3 MB in 18 s; honest "couldn't reach" messages.
2. Feel "wow": the size breakdown before compressing, every level downloadable, page-by-page Compare, a batch of 5 for one use.
3. Read results without fighting the layout, and meet an honest offer. A trial-use download is one use; any mark on the file is stated before download; the pass is the clear upgrade.

## Why: what the evidence says

**Strong:**
- Balanced on the photo PDF: 93% then 98% smaller, text still selectable.
- Target 1 MB → 1002.6 KB and 200 KB → 193.7 KB.
- Unreachable targets explain exactly why (including the per-page budget) and how to go further.
- A text-only file is "tidied" honestly; an already-small file is left alone.
- Aggressive and Extreme stop early when further steps would destroy text, and offer **Run anyway**.
- Batch of 5 → one use.
- Over 50 MB works.
- axe on the result view: 0 violations.
- Compressing never spent a use in any context.

**What breaks trust:**
1. **The result list is hard to read: level rows don't wrap.**
   - On a 1366 px desktop the level label ("Level 1: Pictures inside made smaller… — 1.34 MB (93% smaller)") is squeezed into a 48 px column, one word per line.
   - On Pixel 7 the page widens to **958 px** after Compress, and Compare overlaps the label.
   - This is the moment users decide which level to download (and whether to pay).
2. **Fresh visitors can't download.** 28 of 31 fresh contexts loaded at 0 remaining (display-only, one busy box IP; same pattern as FDP-02 and FDP-03). They can compress and compare, then hit "Get a Day Pass to download".
3. **A wrong diagnosis on CMYK files.** A 10.26 MB PDF of CMYK JPEG photos (verified DCTDecode/DeviceCMYK) is called "a scan… stored as scanner pictures (JBIG2 or JPEG 2000)… nothing was changed". The breakdown right above says "Balanced should shrink it a lot". In the batch it comes back at 10.26 MB.
4. **Extreme doesn't do what it says.** "Every page becomes grey at 70 dpi, then pure black and white", but after Run anyway it ended at a colour 70 dpi level with no grey or B/W step and no explanation.
5. **Packaging:**
   - The video shows the old modes (Light/Medium 25%/Strong 50%) and "10 free uses daily", with 0 views and 3 different titles.
   - The blog never mentions Target size or levels, and still says "unlock first".
   - /es says "gratis"; 8 locales have English title, meta and H1.
   - The "Created with FreeDailyPro.com" mark on trial-use downloads is only disclosed in the cap dialog.

## Outcomes we want

- The level list reads cleanly on a 320–430 px phone and on desktop: label first, buttons wrapped under it, no horizontal scroll.
- A new visitor sees 10 remaining and spends exactly 1 per download (or per batch).
- Every "nothing was changed" message names the true cause (CMYK, masks, JBIG2/JPX, already optimised). Ideally CMYK photos shrink too.
- Extreme either produces its grey and B/W steps or says why it stopped.
- The video, blog and locales describe today's four modes, Target size and levels, with trial-uses wording. The mark (if kept) is stated next to Download.

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | MEDIUM | 14 of 16 compression cases behave as documented, including target fit, the honest unreachable-target notes and 72 MB. FAIL: CMYK misdiagnosed (CP-11), Extreme incomplete (CP-03). Output files not verified (capped): **needs re-run after midnight UTC**. `evidence/findings/live-functional-findings.md` §3, `json/explore-*.json`, `json/capped2.json` |
| 2 | Completeness vs. competitors | **PASS** (minor gaps) | LOW | Ahead of SquashTools, PDFWrangle, pdfnex, ToolRush and CLEKARA on the size breakdown, downloadable levels, page Compare, batch and inline unlock. Gaps: no "split into parts that fit" when a target is unreachable (unverified absence); no destination presets (Gmail, portal); no statement of MB = 1,000,000 vs 1,048,576; trial-use outputs carry a mark. `desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Excellent copy, hints and stop/Run anyway logic. Problems: the unreadable level list; focus lost after Add and Compress; non-PDFs called "damaged, try Repair"; invalid target is a toast only. |
| 4 | Layout attractiveness | **FAIL** | HIGH | Result view: level labels 48 px wide on desktop, page 958 px wide on Pixel 7 (`screens/live/desktop-level-rows-crop.png`, `phone-level-rows-crop.jpg`, `phone-result-view.jpg`). Empty state: iPhone SE overflow 329 > 320, drop zone below the fold on iPhone SE and Galaxy S9+. No ad overlaps; CLS ≤ 0.022. |
| 5 | Payment process | **PARTIAL** | MEDIUM | The cap dialog is clear ("Your input stays where it is"). Day Pass opens an email dialog while Monthly goes straight to Stripe (inconsistent, as in FDP-02). The mark is disclosed only in the cap dialog. `screens/live/quickbuy-*.png`, `capped-download-click.png` |
| 6 | Information correct | **PARTIAL** | MEDIUM | Copy is accurate and detailed except: the CMYK message cites JBIG2/JPEG 2000; Extreme's grey/B/W steps did not appear; the "links, bookmarks and form fields are untouched" claim is unverified (needs re-run). |
| 7 | Indexing | **PASS** | — | 200, indexable, self canonical, in the sitemap (lastmod 2026-11-19) with a video block; WebSearch ranks the tool first. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong title (60) and meta (155), "compress to 1 MB / 200 KB" intents, 8-Q FAQPage, breadcrumb. Issues: /es "gratis"; 8 locales English title, meta and H1 in the server HTML; three video titles (one with "Free"); Offer has no billing period; generic OG; empty video alt. |
| 9 | Blog post | **PARTIAL** | MEDIUM | /blog/compress-pdf (2026-10-17) embeds the video, uses trial-uses wording and has good portal/notary content. It never mentions Target size, the levels, Compare or batch; "Unlock… first" is stale. `html/blog-visible.txt` |
| 10 | YouTube video exists | **PARTIAL** | LOW | XZDDliVHrLY, 87 s, **0 views**, embedded on the tool and blog; generic tags. |
| 11 | FAQ / usage guide | **PASS** (minor) | LOW | 8 Qs plus Details; nearly every claim held live. Exceptions: the Extreme description, and the CMYK/scan wording in the result message. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old Light/Medium/Strong modes, light UI, "10 free uses daily", "200+ Free Productivity Tools". `evidence/video/frames/f08.jpg` |
| 13 | Storage | **PASS** (by design) | — | Local-only processing; nothing persists on reload. Cloud storage is a sign-in $4.99 add-on (untested). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" copies the URL. No result share (fine for private files). Save to Google Drive needs sign-in (untested). |
| 15 | Downloads | **N/A today (needs re-run after midnight UTC)** | — | Every fresh context that could act was capped, so no output could be downloaded. The cap dialog says passes remove the "Created with FreeDailyPro.com" mark, so trial-use downloads are marked. |
| 16 | Usage count | **PARTIAL** | HIGH | Compress, Run anyway, Compare and batch never changed `usageToday` (display). Download is gated. Per-download counting **needs re-run after midnight UTC**. 28 of 31 fresh contexts at 0 (display-only). |
| 17 | Categorization | **PASS** | — | PDF Tools, Professional Tool. |
| 18 | Location in site | **PASS** | — | Breadcrumb Home › PDF Tools › Compress PDF; 3 bundles, paralegals; 38 blog posts link in; next step Add Password to PDF; batch offers "Continue with Merge PDF". |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic levels are right. P2 idea: pick the target from words like "for Gmail". Demand high (rank 6; GSC not available). |
| 20 | Merge? | **PASS: keep standalone** | — | No other PDF compressor. |
| 21 | Remove? | **N/A: keep** | — | Core tool. |
| 22 | Duplicates | **PASS** | — | None. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles.
- No ad overlaps.
- The phone strip collapses to a compact "$1 day pass · $4.99/month" link.
- Correct `lang`; EU consent banner (Berlin screenshot).
- Keyboard: drop zone and modes.
- Result view axe clean.

**FAIL / PARTIAL:**
- Result-view overflow (HIGH).
- iPhone SE overflow and drop zone below the fold on small phones (MEDIUM).
- /es "gratis"; 8 locales with English server HTML and a mixed UI (MEDIUM-HIGH).
- ja overflows by 3 px; /ar 404; USD only.
- axe: desktop label-content-name-mismatch (serious, 1); Pixel 7 "Advertisement" caption contrast (serious, 2).

**Ads:** keep them, in reserved fixed-height slots below the tool and in the rails (as now). Never between the level list and its Download buttons.

## Suggested direction (interpret freely)

1. **Level list layout (P1).** Stack the label above a wrapping button group, or move Drive/Cloud into a "More" menu per level. Keep the cap note on its own line. Test at 320, 412 and 1366 px, capped and uncapped.
2. **Trial meter (P0, shared).** Same investigation as FDP-02 and FDP-03: why fresh `dev:` scopes from this IP show `usageToday 10`. Verify server-side.
3. **Classifier honesty.** Distinguish CMYK DCT, masks, JBIG2, JPX and "already optimised" in the "nothing was changed" message. Consider converting CMYK photos to RGB JPEG in Balanced (competitors skip CMYK too, so this could be a differentiator).
4. **Extreme.** Make Run anyway continue to the grey and B/W steps, or explain why they were skipped (e.g. "grey would not be smaller").
5. **Disclosure.** If trial-use downloads keep the mark, say so next to "Download" (as merge-pdf's report also asks), and in the FAQ.
6. **Packaging.** Re-record the video; update the blog (Target size, levels, Compare, batch, inline unlock); one video title; drop "free/gratis"; translate the 8 locales in the server HTML.
7. **Polish.** Focus management; specific messages for non-PDFs; an inline invalid-target message; a decimal-MB note or margin; owner-restriction notice; consistent Quick Buy flows; JSON-LD Offer period.

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy honesty ("Runs on your device"). It was not network-audited here.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect CompressPdf (level runner, classifier, Run anyway), the result-row component, the download stamp and the usage router → restate → propose → implement → verify with `scripts/` and `test-cases.md`.
