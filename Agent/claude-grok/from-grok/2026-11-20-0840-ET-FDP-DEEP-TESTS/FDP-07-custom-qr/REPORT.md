Sent: 2026-11-20 08:40 ET

# FDP-07 QR Code Generator with Logo (custom-qr): deep test report for Claude

- **Written:** 2026-11-19 12:36:05 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/custom-qr. Row 7 of TEST-ORDER.md (grouped with test-plan rank 8), cluster C04 with qr-generator (Professional Tool), bulk-qr, qr-scanner and barcode-generator.
- **Classification:** Premium Application, QR Codes & Barcodes. **2 trial uses a day**, $3 day pass / $9.99 a month. Previewing is free; each Download (PNG, SVG, vector PDF, bulk ZIP) says "Download uses 1 trial use".
- **Testers:**
  - Desk review: curl, JS bundles, FAQ and Details, the two blog posts, the sitemap, 10 locale URLs plus /ar and /it, WebSearch competitors and the brand query.
  - YouTube video: metadata and 21 frames, with the QR codes in the frames decoded.
  - Headless Playwright: 29 scenarios (28 canvases saved; 27 distinct), decoded from the live canvas with zxing-cpp.
  - **A live download battery:** 7 fresh contexts, 15 files downloaded, usage recorded per download. Then inspection of every file (pixel size, margins, mark, decode; PDFs rendered at 150 and 600 dpi).
  - Also: cap dialogs, keyboard, axe, phone layout, and the matrix (10 profiles, 10 locales plus /ar, 6 geos, axe).
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the cap dialog), no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** the tool has no Drive, cloud or account features. **Nothing was blocked by sign-in.**
- **Fresh contexts:** all six battery contexts (A–F) loaded at 2 remaining. Later fresh contexts loaded at 0 or 2 (16 matrix and geo contexts: 10 at 0, 6 at 2). Display-only.
- **Needs re-run after midnight UTC (7:00 PM ET):**
  - B2 (bulk ZIP after a frame and logo) and D2 (gradient PNG at 2000 px), which did not download because of script steps
  - one more confirmation of the counting pattern
  - real-phone scans
  - These are listed as row #7 in `/workspace/deep/RERUN-AFTER-RESET.md` (a copy is in `scripts/`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work. The components to look at:
- CustomQr (download handlers, the PDF builder, the frame text sanitizer, the bulk `Math.min(size,1000)`)
- the trial gate in UsageAndUpgradeStrip / the usage router
- the "Created with FreeDailyPro.com" PDF stamp
- qrHelpers `p()`
- the qr-code-styling text encoding
- the page's content entry (Details, FAQ, blog)

After you ship, rerun `test-cases.md` (CQ-01…CQ-48).

## Intent

A brand owner wants **a good-looking code that still scans in print**: a cafe table card, packaging, a badge. They pick shapes, colours and a logo, and download an SVG or a print-sized PDF for the printer. They should:

1. **Trust it.** The engine is strong:
   - every type decodes
   - WiFi escaping is correct
   - EC H with a logo
   - wide logos keep their aspect
   - contrast and inversion warnings
   - PNG at an exact 1000/2000 px; SVG with the logo embedded
2. **Feel "wow":** 6 dot styles, gradients, a label frame, a PDF in millimetres, and 200 styled codes in one ZIP with an index.csv. That is more than most of the competitors that advertise "free, no watermark".
3. **Meet an honest, consistent offer.** 2 trial uses a day must mean the same thing for every visitor and every click, and what a trial use buys must scan.

## Why: what the evidence says

**Strong:**
- 23 of 27 distinct preview scenarios decode exactly (the failures are listed below).
- PNG/SVG downloads are exact in size, carry **no** mark, and decode (A1, A2, D1, E1–E4, F2).
- The bulk ZIP holds a correct index.csv.
- The cap dialog is clear ("Your input stays where it is"). No ad overlaps on 10 profiles.

**What breaks the intent:**
1. **The trial gate is inconsistent (P0, display-only).**
   - After the first counted download, further downloads on the same page load go through even at "0 remaining today" (C2, F2), and three new codes in E were never counted.
   - One click cost 1 (A, B, E) or 2 (C, D, F) uses.
   - Fresh contexts start at 0 or 2 at random.
   - So this one session leaks revenue, while another visitor loses both uses on one click or never gets any.
2. **The trial vector PDF doesn't scan (P0).**
   - The "Created with FreeDailyPro.com" badge is drawn as a dark pill over the bottom-right modules, and over the frame text.
   - Neither zxing-cpp nor OpenCV decodes A3 or B1, even at 600 dpi with an added white border. The PNG/SVG outputs carry no mark.
   - So a user spends a trial use on the "print-ready" format and may print a dead code. (Decoders only; a real-phone scan is a re-run item.)
3. **Two encoding bugs and a crash (P1):**
   - Text beyond Latin-1 is corrupted: "Grüße 日本 👍" → "Grüße å, =M". The FAQ promises "the exact text".
   - The PDF frame turns non-ASCII into "?" ("Escan?ame ??").
   - 2,400+ characters crash the whole page and lose the input.
   - vCard ";" is unescaped (shared with qr-generator).
4. **The page argues against itself (P1).**
   - "When not to use it" tells users to skip Wi-Fi, contacts, email and SMS, which the tool has.
   - The Details describe a single "Content box" and PNG/SVG only.
   - The blog says "not a bulk engine" and "Professional Tools trial usage".
   - The video shows the old UI, "10 uses/day" and $1/$4.99.
5. **The quiet zone is 4% of the width (about 1.4 modules), against the 4-module spec (P1).** It decoded here, but print layouts that crop to the art will fail on some scanners.

## Outcomes we want

- Every fresh visitor sees the same allowance. Each download costs exactly what the button says, and nothing downloads at 0 remaining.
- Every file a trial use buys scans: the mark sits outside the code and the quiet zone, or it isn't on the code at all.
- Any text the user types is encoded exactly, or the user gets a clear message. The page never crashes on long input.
- The page, FAQ, blog and video describe today's tool: 7 types, frame, PDF, bulk, 2/day, $3/$9.99.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 23/27 distinct previews exact. FAIL: Unicode (CQ-03), vCard ";" (CQ-05), fake logo blanks the canvas (CQ-21), long text crash (CQ-10). Trial PDFs don't decode (CQ-33). `findings/live-functional-findings.md`, `json/decoded.json`, `downloads/`, `pdf-renders/` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Ahead: frame label, gradient, mm PDF, styled bulk with CSV, contrast warnings. Missing (live-verified in the controls): transparent background, EPS, eye colour, calendar/location types. Competitors stress "no watermark, unlimited". `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Instant preview and good defaults. On phones the preview is below Download. The fake logo fails silently. Empty content gives a " " code. The 1000 px bulk cap is silent. File names are fixed. |
| 4 | Layout attractiveness | **PARTIAL** | MEDIUM | Desktop/tablet: clean two-column layout. Phones: canvas y≈1342 vs Download y≈1029 (Pixel 7). iPhone SE 329 > 320; ja +3 px. No ad overlaps. `screens/devices/`, `screens/live/phone-pixel-7-full.jpg` |
| 5 | Payment process | **FAIL** | HIGH | The cap dialog is clear and the test stopped there. But the gate lets downloads through at 0 within a page load and charges 1 or 2 per click (display-only). The mark is disclosed only inside the dialog. `json/battery-*.json`, `screens/live/capped-png-click.png` |
| 6 | Information correct | **FAIL** | HIGH | "When not to use it" denies 4 of the 7 types. Details: "Content box", "single-line", PNG/SVG only. FAQ "exact text" is false for non-Latin-1. `html/tool-visible.txt` |
| 7 | Indexing | **PASS** | — | 200, self canonical, in the sitemap with a video block; #1 for the brand query. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title and meta (105 chars); FAQPage with 7 questions. The Offer has no billing period. "with Logo" competes with qr-generator's title. 9 locales keep the English title and H1. |
| 9 | Blog post | **PARTIAL** | MEDIUM | Two near-duplicate posts. The branded post is stale ("QR Code Designer", PNG/SVG only, "PNG 1200 px", "not a bulk engine", "Professional Tools trial usage"). |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | -YoQA8K6x8I, 62 s, 9 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | 7 useful FAQs (contrast, logo, gradient, PDF). Missing: what a trial use buys, the PDF mark, the bulk 1000 px cap, the Unicode limit. The Details contradict About. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old UI (no tabs, frame, PDF or bulk), "Trial: 10 uses/day", $1/$4.99; the description says "10 trial usages every day". `findings/video-findings.md` |
| 13 | Storage | **PASS** (by design) | — | Local only. No cloud or Drive. The privacy claim was not network-audited. |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only; no copy-image or share-the-code (unverified absence beyond the visible controls). |
| 15 | Downloads | **FAIL** | HIGH | PNG/SVG: exact size, decode, no mark. PDF: 50 mm correct, but the badge over the code means it doesn't decode; the frame non-ASCII becomes "?". ZIP: 1000 px when 2000 is chosen. Quiet zone about 1.4 modules. B2/D2 need a re-run. `json/downloads-inspection.json` |
| 16 | Usage count | **FAIL** | HIGH | Previews are free (usageToday unchanged). Downloads: 1 or 2 per first click; then uncounted, including at 0. Start state 0 or 2. Display-only. |
| 17 | Categorization | **PASS** | — | QR Codes & Barcodes, Premium Application. |
| 18 | Location in site | **PASS** | — | Breadcrumb; "Part of: Creating and Verifying QR Codes"; the C04 links. P2: add a "Test it with QR Scanner" link next to Download. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic. Demand is shared with qr-generator (rank 8 group). GSC data is not available. |
| 20 | Merge? | **PARTIAL**: keep, sharpen | MEDIUM | Keep it as the Premium "design and print" tool. Make qr-generator's title stop saying "with Logo", and position custom-qr bulk as "styled" vs bulk-qr "plain, 500, EC choice". |
| 21 | Remove? | **N/A: keep** | — | It is the Premium differentiator in C04. |
| 22 | Duplicates | **PARTIAL** | MEDIUM | Title overlap with qr-generator; bulk overlap with bulk-qr; two near-duplicate blog posts. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles (Chromium, Firefox, WebKit).
- No ad overlaps; CLS 0.
- Desktop and tablet preview above the fold.
- Keyboard: Enter on tabs; selects work.

**FAIL / PARTIAL:**
- The phone preview is below Download (MEDIUM).
- iPhone SE 329 px; ja +3 px.
- 9 locales keep the English title and H1 (MEDIUM for SEO); /ar and /it are 404 (not in hreflang).
- USD only in every geo. The starting allowance is 0 or 2 regardless of geo (display-only).
- axe critical ×5 (button-name ×4, label ×1); the canvas has no alternative; no arrow keys or aria-controls on the tabs; Pixel 7 colour contrast serious ×2.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the preview and the Download buttons.

## Suggested direction (interpret freely)

1. **Trial gate (P0).**
   - Decrement exactly once per download click, re-check the remaining count on every click (not once per page load), and block at 0.
   - Make the starting allowance deterministic for a new visitor.
   - Verify server-side; the evidence here is display-only.
2. **Scannable trial PDF (P0).** Place the badge outside the code and its quiet zone (e.g. a strip under the code or frame, as split-pdf does on pages), and grow the page to fit. Add a test that renders the PDF and decodes it.
3. **Encoding and crash (P1).**
   - Encode text as UTF-8 bytes (with an ECI if your library supports it), as qr-generator already does.
   - Embed a Unicode font in the PDF frame, or warn instead of "?".
   - Catch the overflow and show qr-generator's "Too long" message.
   - Escape ";" in `p()`.
   - Report unreadable logos, and hide Download when the content is empty.
4. **Copy truth pass (P1).** Rewrite "When not to use it", the Details How-to and Limitations, the branded blog post and the video description. Add FAQs on the trial use, the PDF mark and the bulk size. Re-record or trim the video to show tabs, frame, PDF and bulk.
5. **Quiet zone (P1).** Default to a 4-module margin (or offer it as an option), and say so in Limitations.
6. **Phone layout and a11y (P2).**
   - Preview above Download on narrow screens.
   - Name the select triggers; label the logo input; give the canvas an aria-label.
   - Arrow-key tabs.
   - Fix the iPhone SE overflow.
7. **Nice-to-have (P2):**
   - disclose the bulk 1000 px cap (or lift it)
   - descriptive file names
   - transparent background
   - localized titles and H1s
   - Offer billing period in JSON-LD
   - merge the two blog posts

## Constraints

- Say "Premium Applications", "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy claim ("Runs on your device"). It was not network-audited here.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect CustomQr, the gate, the PDF stamp and qrHelpers → restate → propose → implement → verify with `scripts/` and `test-cases.md` (the remaining downloads after midnight UTC).
