Sent: 2026-11-20 08:40 ET

# FDP-08 Bulk QR Generator (bulk-qr): deep test report for Claude

- **Written:** 2026-11-19 13:01:54 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/bulk-qr. Row 8 of TEST-ORDER.md (grouped with test-plan rank 8), cluster C04 with qr-generator, custom-qr (Premium), qr-scanner and barcode-generator.
- **Classification:** Professional Tool, QR Codes & Barcodes. 10 trial uses a day, $1 day pass / $4.99 monthly. Previewing (first 12 codes) is free; **Generate ZIP** costs a use. Save project is gated at 0.
- **Testers:**
  - Desk review: curl, JS bundles (BulkQr, qrHelpers, passCode, csv, ProjectBar), FAQ and Details, the blog post, the sitemap, 10 locales plus /ar and /it, WebSearch competitors and the brand query.
  - YouTube video: metadata and 21 frames, with the QR codes in the frames decoded.
  - Headless Playwright: 14 list scenarios plus the sample guest passes. Every preview was decoded with zxing-cpp.
  - **A real download battery in the one fresh context that loaded with uses:** the passes ZIP and Save project. Files inspected, and the pass signatures verified offline.
  - Also: cap dialogs, Open-project error handling, keyboard, axe, phone layout, and the matrix (10 profiles, 10 locales plus /ar, 6 geos, axe).
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the cap dialog), no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** nothing on the page blocked on sign-in. The Event Suite parts of the project bar (saved projects on any device, publish to Guest/Door apps, email and text invites) only appear with an Event Suite plan. They are **untested; they need sign-in and a plan** (https://www.freedailypro.com/pricing, Event Suite).
- **Needs re-run after midnight UTC (7:00 PM ET):**
  - battery contexts A (repeat and SVG cost), B (name-mode file names, 2000 px, EC H, CSV formula guard), C (500 codes) and E (a too-long line: is a use consumed?)
  - Row #8 in `/workspace/deep/RERUN-AFTER-RESET.md` (a copy is in `scripts/`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work. The components to look at:
- BulkQr (`oe()`: `logUsageNow` before the build; the preview `Promise.all`)
- qrHelpers `D()` (name-mode dedupe) and `S()` (file names)
- passCode
- ProjectBar / useProject (the Save gate, the "kept in this tab only" project)
- UsageAndUpgradeStrip and the cap dialog copy

After you ship, rerun `test-cases.md` (BQ-01…BQ-41).

## Intent

Two kinds of people come here:
- **List people**: a shop with 80 product links, a teacher with 30 lesson links, a fair with booth pages. They want one ZIP, sensible file names and a CSV map they can hand to a printer.
- **Event people**: they want a signed pass per guest that the QR Scanner can check at the door.

They should:
1. **Trust it.** The engine is good:
   - Unicode is exact
   - 4-module quiet zone
   - clean PNGs with no mark
   - a formula-safe CSV
   - a 500 cap with a clear notice
   - duplicate and long-value warnings
   - previews with alt text
   - HMAC-signed passes with a random key per project
2. **Feel "wow":** paste a list, see the codes, press one button, get a ZIP with index.csv. Passes are a genuine differentiator that no competitor we found offers.
3. **Never lose their work or their door.** The pass key is what makes printed passes verifiable, so it must not be lost.

## Why: what the evidence says

**Strong:**
- All 14 list scenarios behave as documented except two (S08, S04).
- D1: 1 use per ZIP; 600×600 at exactly 4 modules; no mark; 5/5 passes decode and verify.
- Open-project errors are clear.
- Phone order is list → preview → Generate (better than qr-generator and custom-qr).

**What breaks the intent:**
1. **Fresh visitors can't download (P0, shared).** Only 2 of about 36 readable fresh contexts loaded with uses (display-only). This is the same pattern as FDP-02 to FDP-06.
2. **The pass key can be lost (P1).**
   - The project, including its key, is "kept in this tab only, then erased".
   - Nothing after Generate tells event people to save it.
   - **Save project is blocked by the cap dialog at 0 remaining**, even though it was free with uses left.
   - So a capped organiser can't keep their own guest list, and passes already printed from that tab become unverifiable once it closes.
   - The save note warns about the key but not that the file holds guest emails, dietary needs and room details.
3. **One bad line breaks the batch (P1).**
   - A 3,000-character line blanks **all** previews.
   - The counter still says "2 QR codes will be generated" and Generate stays enabled.
   - By code the run then fails with "Generation failed" **after** a use is logged (`logUsageNow` runs before the build; to confirm in re-run E).
4. **Name mode drops named rows that share a URL (P1).** "Table 1,…/menu" and "Table 2,…/menu" give one file, because dedupe is by value. Table cards are the tool's own headline use case.
5. **Guest passes are a dead end without Event Suite (P2).** "Guest passes from my project (0)" doesn't say where guests come from.
6. **Competitors offer more (P2):**
   - CSV/XLSX upload with column mapping
   - Avery label-sheet PDFs
   - larger batches
   - "free, no limit", which they all stress

## Outcomes we want

- Every fresh visitor sees 10 uses. A ZIP costs exactly what the button says, and a failed batch costs nothing.
- Organisers can always save (or are prompted to save) the project and pass key, with an honest note about what personal data the file holds.
- A bad line is pointed out by line number, and the rest of the batch still works or is clearly blocked.
- Named rows are never silently dropped.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | MEDIUM | 12/14 list scenarios PASS; S08 (one long line blanks the batch) and S04 (named duplicates dropped) FAIL. Passes are correct and verified. `findings/live-functional-findings.md`, `json/decoded.json`, `json/explore-*.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Behind on CSV/XLSX upload, column mapping, label-sheet PDF, JPEG, logo/caption and batch size (5,000 at bulkqr.codes). Ahead on signed guest passes, formula-safe CSV and warnings. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Paste → preview → Generate is very easy. But: a long line silently blanks the preview; "(0)" passes is a dead end; no save prompt after passes; accent/CJK names become "Gru-e" or "code" (by code). |
| 4 | Layout attractiveness | **PASS** (minor) | LOW | Clean. On phones the preview sits above Generate. iPhone SE 329 > 320; ja +3 px. No ad overlaps; CLS ≤ 0.023. `screens/devices/`, `screens/live/phone-pixel-7-full.jpg` |
| 5 | Payment process | **PARTIAL** | MEDIUM | The cap dialog is clear, but on this tool it promises to remove a "Created with FreeDailyPro.com" mark that the trial PNGs don't have. Save project is gated at 0. The test stopped at the dialog. `screens/live/capped-generate.png`, `json/kbd.json` |
| 6 | Information correct | **PARTIAL** | MEDIUM | FAQ and Details match the code (500, sizes, EC, 4-module margin, numbering). Missing: where guests come from, that a failed batch may cost a use, and that the project file holds guest personal data. |
| 7 | Indexing | **PASS** | — | 200, in the sitemap with a video block, #1 for the brand query. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title; 96-char meta; FAQPage with 6 questions. The H1 "Bulk QR Generator" is short. The Offer has no billing period. 9 locales keep the English title and H1. |
| 9 | Blog post | **PASS** (minor) | LOW | /blog/bulk-qr-codes-from-a-url-list-as-zip is accurate. It omits passes, mentions a "PDF proof sheet" the tool doesn't make, and links the custom-qr post under its old name. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | ui6-i9QUCxA, 62 s, 4 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | LOW | 6 good FAQs. Missing: guest passes, saving the project/key, and long-line failure. |
| 12 | Video shows current capabilities | **PASS** (minor) | LOW | Current list UI, prices and allowance; one Generate = 1 use. It omits passes and the project bar. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL** | MEDIUM | Local only; the project is tab-only and erased. Saving a file is the only way to keep it, and that is gated at 0. Cloud save is Event Suite only (needs sign-in, untested). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only. Publish to Guest/Door apps is Event Suite (untested, sign-in). |
| 15 | Downloads | **PARTIAL** (re-run for the rest) | MEDIUM | D1 passes ZIP: 600 px, 4 modules, EC M, no mark, CSV with BOM, all decode, 5/5 signatures valid. A/B/C/E **need re-run after midnight UTC**. `json/downloads-inspection.json`, `downloads/` |
| 16 | Usage count | **PARTIAL** | HIGH | Previews are free. One ZIP = 1 use (D1; also seen in the video). Save is free with uses left but blocked at 0. 34 of about 36 fresh contexts were at 0 (display-only). By code, a failed batch is still charged. |
| 17 | Categorization | **PASS** | — | QR Codes & Barcodes, Professional Tool. |
| 18 | Location in site | **PASS** | — | Breadcrumb; "Part of: Creating and Verifying QR Codes"; "Next: QR & Barcode Scanner"; Event invite guides. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic. Demand is in the rank-8 QR group. GSC data is not available. |
| 20 | Merge? | **N/A: keep**, clarify | LOW | Keep it separate (plain, 500, EC choice, passes). Name custom-qr's styled bulk as the upgrade, and stop qr-generator claiming "with Logo". |
| 21 | Remove? | **N/A: keep** | — | Unique passes feature; clear demand. |
| 22 | Duplicates | **PARTIAL** | LOW | It overlaps custom-qr's 200-code styled bulk. One blog post, no duplicates. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles.
- No ad overlaps.
- Phones keep the list → preview → Generate order.
- Preview alt text present; progress bar has ARIA.

**FAIL / PARTIAL:**
- iPhone SE 329 px; ja +3 px.
- 9 locales keep the English title and H1; /ar 404.
- USD only.
- axe button-name critical ×3 (the select triggers); Pixel 7 colour contrast serious ×2.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the preview and Generate.

## Suggested direction (interpret freely)

1. **Trial meter (P0, shared)** as in FDP-02 to FDP-06. Verify server-side.
2. **Protect the pass key (P1).**
   - Never gate Save project; it's the user's own data and not a "download" of a result.
   - After generating passes, prompt "Save your project: without it the scanner can't check these passes".
   - Extend the note to say the file contains guest names, emails, dietary needs and rooms.
3. **Bad lines (P1).**
   - Validate each line's capacity before charging. Show "Line 7 is too long (3,000 characters)", keep the other previews, and either skip it with a note or block Generate.
   - Log the use only after the ZIP is built.
4. **Name mode (P1).** Deduplicate by name+value (or by name when names are on), or ask the user. Warn on "Name," with an empty value. Transliterate or keep Unicode in file names (most OSes accept them).
5. **Copy (P2).**
   - Say where guests come from (Event Suite Guest Manager or a project file) and grey out "(0)" with a link.
   - Fix the cap dialog's mark sentence for tools without a mark.
   - Add an Offer billing period. Localize the titles and H1s.
6. **Nice-to-have (P2):**
   - CSV/XLSX upload with column pick
   - label-sheet PDF (Avery 5160/L7160)
   - a quiet-zone option
   - naming custom-qr bulk as the styled upgrade

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy claim ("Runs on your device"). It was not network-audited here.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect BulkQr, qrHelpers, passCode, ProjectBar and the strip → restate → propose → implement → verify with `scripts/` and `test-cases.md` (battery A/B/C/E after midnight UTC).
