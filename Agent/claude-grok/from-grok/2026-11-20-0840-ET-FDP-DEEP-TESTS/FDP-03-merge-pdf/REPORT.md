Sent: 2026-11-20 08:40 ET

# FDP-03 Merge PDF (merge-pdf): deep test report for Claude

- **Written:** 2026-11-19 10:51:19 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/merge-pdf. The slug is from TEST-ORDER.md row 3 and tools.csv.
- **Classification:** Professional Tool, PDF Tools. 10 trial uses per day, **spent at Download** (Merge is free), $1 day pass / $4.99 monthly.
- **Testers:**
  - Desk review: curl, JS bundle read, FAQ, blog, sitemap, WebSearch competitors.
  - YouTube video: metadata, captions and 17 frames. **Not** watched with sound.
  - Headless Playwright:
    - 19 generated inputs (sizes, orientations, bookmarks, 500 pages, non-Latin, rotated, form, user-password, owner-restricted, 5 corrupt or renamed, JPG/PNG)
    - 8 merge scenarios downloaded and inspected with pikepdf and poppler (page order and count, sizes, /Rotate, outline, AcroForm, encryption, metadata, stamped text)
    - every list, Arrange and Choose-pages control
    - trial-use counting
    - cap dialog and cloud dialog
    - keyboard and axe on the result view
    - matrix: 10 device/browser profiles, 10 locales plus /ar, 6 countries, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API/MCP calls (the /developers merge API and B-0040 are out of scope), no site or repo changes.
- **Not tested (sign-in):** "Open from Google Drive", "Save to Google Drive" and "Save to my cloud storage" (the email sign-in step and the $4.99 add-on). All are at https://www.freedailypro.com/tool/merge-pdf. "Take photo" was not exercised (headless).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components (MergePdf, operations, pdfBookmarks, pdfMetadata, ReorderableFileList, PdfPageStrip, imagePdf, and **whatever stamps the "Created with FreeDailyPro.com" badge**: it is *not* in those bundles, so it is probably the shared download/branding path), then:
- Restate the problem.
- Challenge anything that looks wrong.
- Pick the fix that fits how FreeDailyPro has shipped similar work.

After you ship, rerun `test-cases.md` (MP-01…MP-39).

## Intent

People want to turn several PDFs (contracts, signed pages, scans, receipts) into **one tidy file in the right order**, privately, in seconds, and to trust what the page promises about the result. They should:
1. Get a correct merge every time: order, sizes, rotation, bookmarks and text kept. The engine already does this very well.
2. Feel "wow": Arrange all pages, page ranges, pictures, inline password unlock and the duplex blank page are better than most rivals.
3. Meet an **honest** offer. If trial-use downloads carry a mark, the page says so up front, and the $1 / $4.99 pass is the clear way to a clean file. Never a contradiction discovered after download.

## Why: what the evidence says

**Strong:**
- 8/8 scenarios produced exactly the expected page sequence: a 503-page merge in 0.34 s; mixed A4, Letter, A3, landscape and square pages kept; /Rotate kept; Japanese, Cyrillic, Greek and Arabic text extractable.
- Nested original bookmarks kept under per-file entries.
- Ranges, Arrange (move, rotate, delete) and Choose pages are all reflected exactly in the output.
- Password files unlock in-browser and the output is unencrypted.
- Damaged files are rejected with a toast and never break the merge.
- Clear warnings for duplicates and forms.
- Merge doesn't spend a use; "Download uses 1 trial use" is shown before the click; exactly −1 per download.

**What breaks trust:**
1. **The "no watermark" promise is false for trial-use downloads.** Every output page carries a bottom-right "Created with FreeDailyPro.com" badge with the logo: 11/11, 3/3 and 503/503 pages. Meanwhile:
   - the meta says "download a clean PDF, with no watermark"
   - the FAQ says "Does merging add a watermark? No… nothing stamped on them"
   - the H3 says "No upload, no watermark… no logo or text is added"

   Only the cap dialog mentions that a pass "removes the 'Created with FreeDailyPro.com' mark". The intentional book watermark is a separate thing; this is about the copy contradicting the output.
2. **Fresh visitors load at "0 remaining today"** from this box IP: 16 of 17 matrix and geo contexts, and 6 of 7 probe contexts. It is display-only evidence and the same pattern as FDP-02. A new visitor can merge but cannot download without paying.
3. **The packaging is outdated:** the video shows the old light UI, a "0 free uses remaining" banner and "10 free uses daily"; the blog says bookmarks drop and files must be unlocked first. "Free" wording appears in the video, the sitemap video title and the /es title ("gratis").
4. **Locales are half-English:** 8 locales have English title and meta and an English stepper, drop zone and FAQ.
5. **Smaller correctness gaps:**
   - Bookmarks are added only when some file has its own; arranged output has none, although the FAQ says per-file bookmarks are kept.
   - Form fields are flattened to not-fillable (warned, but competitors keep them).
   - Non-PDFs renamed .pdf are called "damaged, try Repair PDF".

## Outcomes we want

- The page copy and the downloaded file agree. Either trial-use downloads are clean, or the meta, FAQ and H3 say plainly "trial-use downloads carry a small 'Created with FreeDailyPro.com' mark; a Day Pass or Monthly removes it", shown next to "Download uses 1 trial use".
- A new visitor sees 10 remaining and spends exactly 1 per download.
- Bookmark output is predictable and matches the FAQ (per-file bookmarks always, or an option).
- The video, blog and locales describe today's tool with trial-uses wording.

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | S1–S8 all exact: order, count, sizes, /Rotate, ranges, blank page, arrange, choose pages, images, password, 503 pages. `evidence/json/output-inspection.json`, `evidence/findings/live-functional-findings.md` §3 |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Ahead on in-merge page arranging, ranges, pictures, duplex blank page, inline unlock. Live-verified gaps: form fields not kept fillable (EmbedPDF, docMentis etc. keep them), no bookmark options, no result share. Unverified absences: duplicate page, sort by name, link preservation. `desk-findings.md` (Competitors) |
| 3 | Ease of use | **PASS** (minor) | LOW | Stepper, per-card ↑↓✕, range field with precise errors, labelled Arrange grid, "Start over/Done". Minor: non-PDF files told "damaged, try Repair"; focus lost after Move/Merge; owner-restricted file silently "Unlocked". `screens/live/ui-*.png`, `json/ui-probe.json` |
| 4 | Layout attractiveness | **PARTIAL** | LOW-MEDIUM | Clean dark UI, no ad overlaps, CLS ≤ 0.021. iPhone SE overflows 329 > 320; drop zone below the fold on iPhone SE, 14 Pro Max and Galaxy S9+; 16×16 icons. `devices-locales-findings.md`, `screens/devices/` |
| 5 | Payment process | **PARTIAL** | HIGH | The strip and cap dialog are clear ("Download uses 1 trial use"; "Your input stays where it is"). But the watermark is only disclosed **inside the cap dialog**, and fresh visitors meet the cap with 0 uses (check 16). `screens/live/bat-*.png`, `json/battery-*.json` |
| 6 | Information correct | **FAIL** | **HIGH (P0)** | "no watermark… no logo or text is added" vs. a badge on 100% of output pages (`screens/live/s1-page1-01.png`, `s5-page1-1.png`). Arrange-bookmark FAQ claim false; "What doesn't carry over… Bookmarks do:". `desk-findings.md` (FAQ), `live-functional-findings.md` §2 |
| 7 | Indexing | **PASS** | — | 200, indexable, self canonical, in the sitemap (lastmod 2026-11-19) with a video block; WebSearch ranks the tool first. **GSC data is not available.** Sitemap video title has a literal "\u2013" (24 lines site-wide, LOW). `html/sitemap-2026-11-19.xml` |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title (55), H1, 13-Q FAQPage, breadcrumb, 5 JSON-LD types. Issues: false "no watermark" in meta; /es title "gratis"; 8 locales English title and meta; three different video titles; Offer without billing period; generic OG; empty video thumbnail alt. |
| 9 | Blog post | **PARTIAL** | MEDIUM | /blog/merge-pdf (2026-10-17) is linked from the tool and is a good workflow angle, but says "Bookmarks may drop on merge" and "Encrypted parts must be unlocked first" (both now false). No video; no Arrange, Choose pages or pictures. `html/blog-visible.txt` |
| 10 | YouTube video exists | **PARTIAL** | LOW | 0FjbjU4eDVw, 86 s, 5 views, embedded on the tool (not the blog), generic tags. `video-findings.md` |
| 11 | FAQ / usage guide | **PARTIAL** | HIGH | 13 detailed Qs; most are confirmed live (password, duplicates, forms, sizes, rotation, images, ranges, name). Wrong: the watermark answer, the arrange-bookmarks answer, and the "doesn't carry over" wording. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old light UI, "0 free uses remaining today" banner, "Works with any file size", "10 free uses daily!", "200+ Free Productivity Tools"; none of ranges, Arrange, Choose pages, pictures, password. `evidence/video/frames/` |
| 13 | Storage | **PASS** (by design) | — | Local-only processing, list cleared on reload, localStorage holds only the usage key. Cloud storage is a sign-in $4.99 add-on (untested). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" copies the URL (no use spent). No result share (by design for private files; acceptable). Save to Google Drive needs sign-in (untested). |
| 15 | Downloads | **PARTIAL** | HIGH | Files are valid PDF 1.7, named `<first>-merged.pdf`, metadata sane (Title, Author, Producer FreeDailyPro). **Badge stamped on every page** contrary to the copy (see 6). AcroForm dropped (2 orphan widgets remain; text visible). `evidence/downloads/`, `json/output-inspection.json` |
| 16 | Usage count | **PARTIAL** | HIGH | Uncapped context: Merge free, Download −1 exactly (8 downloads, 0→8 used), reload persists, Share free. **But** fresh contexts load at 0 remaining (16/17 matrix and geo, 6/7 probes; display-only, same IP pattern as FDP-02). A second fresh-context trace was skipped to save contexts: **needs re-run after midnight UTC**. |
| 17 | Categorization | **PASS** | — | PDF Tools, Professional Tool. |
| 18 | Location in site | **PASS** | — | Breadcrumb Home › PDF Tools › Merge PDF; linked from many hubs and 28 blog posts; next steps to Add Page Numbers, Watermark, Compress, Split. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic merge is right. P2 idea: auto-order by detected date or name. Demand high (test-plan rank 5, 235 views; GSC not available). |
| 20 | Merge? | **PASS: keep standalone** | — | C10 (document-assembler, mail-merge-pdf) serve different jobs; the Document Assembler upsell card is a good bridge. |
| 21 | Remove? | **N/A: keep** | — | Core high-demand tool. |
| 22 | Duplicates | **PASS** | — | No duplicate plain-merge tool. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles (Chromium, Firefox, WebKit; phones, tablets, desktop).
- No ad overlaps the tool.
- Phone ad slots sit below the drop zone.
- CLS ≤ 0.021.
- Correct `lang`.
- EU consent banner (Berlin, Paris).
- Keyboard: drop zone, list and Arrange controls operable and labelled.

**FAIL / PARTIAL:**
- iPhone SE overflow 329 px; drop zone below the fold on 3 phones (MEDIUM).
- /es fully localized but "gratis" in the title; 8 locales English title and meta with a mixed UI (MEDIUM-HIGH, SEO).
- ja desktop overflow (LOW).
- /ar 404 (RTL N/A).
- USD-only prices in 6 countries (by design?).
- axe: desktop label-content-name-mismatch (serious, 1); Pixel 7 contrast of the "Advertisement" caption (serious, 2); result view aria-allowed-role ×5 (minor).
- Focus lost after Move and Merge (LOW).

**Ads:** keep them, in reserved fixed-height slots below the tool and in the rails (as now). Never between the file list and the Download button.

## Suggested direction (interpret freely)

1. **Watermark honesty (P0).** Decide the product truth, then make all surfaces agree: meta, FAQ "Does merging add a watermark?", the H3 "No upload, no watermark", tools.csv, the result card next to "Download uses 1 trial use", the video and the blog. If the mark stays for trial uses, say "small 'Created with FreeDailyPro.com' mark on trial-use downloads; a pass removes it" *before* the user downloads. Verify in code that a pass really removes it (not verified here: no payment).
2. **Trial meter.** Same investigation as FDP-02: why fresh `dev:` scopes show `usageToday ≥ allowed` from this IP. Verify server-side; counters here are display-only.
3. **Bookmarks.** Always add per-file bookmarks (or a "Bookmarks: per file / keep originals / none" option), including for Arrange output, so the FAQ is true. Fix "What doesn't carry over… Bookmarks do:".
4. **Forms (enhancement).** Consider keeping fields fillable (rename clashing names), as competitors do; at least drop the orphan widgets.
5. **Packaging.** Re-record the video on the current UI; update the blog; one video title; fix the sitemap's literal "\u2013"; remove "free/gratis".
6. **Locales, mobile, a11y.** Server-side translations for the 8 locales (or remove them from hreflang); 320 px header; compact stepper so the drop zone is above the fold; focus management; specific messages for non-PDFs; a notice for owner-restricted files.

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy honesty ("Your files never leave your device"). It was not network-audited in this test.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect MergePdf, operations, the stamping or branding module, the usage router, pdfBookmarks → restate → propose → implement → verify with `scripts/` and `test-cases.md`.
