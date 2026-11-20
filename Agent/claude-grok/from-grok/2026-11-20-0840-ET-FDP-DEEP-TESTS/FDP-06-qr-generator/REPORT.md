Sent: 2026-11-20 08:40 ET

# FDP-06 QR Code Generator (qr-generator): deep test report for Claude

- **Written:** 2026-11-19 12:04:41 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/qr-generator. Row 6 of TEST-ORDER.md (test-plan rank 8), cluster C04 with custom-qr (a Premium Application), bulk-qr, qr-scanner and barcode-generator.
- **Classification:** Professional Tool, QR Codes & Barcodes. 10 trial uses per day. **Previewing is free; Download PNG/SVG is gated.** $1 day pass / $4.99 monthly.
- **Testers:**
  - Desk review: curl, JS bundles, the FAQ and Details sections, related blog posts, sitemap, 10 locale URLs, WebSearch competitors.
  - YouTube video: metadata, captions, 16 frames, with the QR codes in the frames decoded.
  - Headless Playwright: 31 preview scenarios covering all 7 types, EC levels, colours, logos and limits. **Every code was decoded with zxing-cpp and OpenCV straight from the live preview canvas** (no download).
  - Also: cap dialogs, keyboard, axe, phone layout, and the matrix (10 profiles, 10 locales plus /ar, 6 geos, axe).
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls (the API notes in TEST-ORDER are out of scope), no site or repo changes.
- **Sign-in:** the tool has no Drive or cloud buttons, so nothing in the tool was blocked by sign-in.
- **Not observable today:** downloads. **All 22 readable fresh contexts loaded at "0 remaining today".**
  - So these are marked **needs re-run after midnight UTC (7:00 PM ET)**:
    - PNG/SVG pixel size, quiet zone and decode
    - whether trial downloads carry the "Created with FreeDailyPro.com" mark
    - whether PNG + SVG cost one use or two
    - logo parity between PNG and SVG
  - `scripts/qr-battery.js` and `scripts/inspect-qr-downloads.py` are ready. The tool is listed in `/workspace/deep/RERUN-AFTER-RESET.md` (a copy is in `scripts/`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components (QrGenerator, qrHelpers `P()`/`p()` vCard escaping, the canvas logo draw, the SVG logo injection, the download stamp, UsageAndUpgradeStrip and the tool's content entry: Details, FAQ, title/meta, and the C04 upsell card), then:

- Restate the problem.
- Challenge anything that looks wrong.
- Pick the fix that fits how FreeDailyPro has shipped similar work.

After you ship, rerun `test-cases.md` (QR-01…QR-42).

## Intent

People need **a code that scans, first time, in print**: a menu link, guest WiFi, a business card. They want to see exactly what's encoded, adjust size and colours, and download a PNG or SVG they can hand to a printer. They should:

1. **Trust it.** The engine is already excellent:
   - every type decodes exactly
   - WiFi escaping is correct even for `;,:"\`
   - there is a live byte-capacity meter, and over-limit and contrast warnings
   - EC H is applied with a logo
2. **Feel "wow":** instant preview, 7 types, colours, logo, 2,000 px or vector.
3. **Meet an honest offer.**
   - Free competitors advertise "no watermark, unlimited".
   - So FreeDailyPro must say plainly what a trial use buys and whether the image carries a mark, and keep it scannable.

## Why: what the evidence says

**Strong:**
- 27 of 31 preview scenarios pass (3 fail; 1 is deferred to the re-run).
- Correct WiFi, mailto, SMSTO and tel formats.
- A bare domain gets https://.
- Clear, quantified messages: "Too long for a QR code: 2,400 bytes, and level M holds at most 2,331…" and "Low contrast (2.5:1)…".
- A 2,900-byte code decodes even from the 300 px preview.
- The video's on-screen codes decode correctly.

**What breaks trust:**
1. **Fresh visitors can't download** (P0, shared). 22 of 22 readable contexts were at 0 (display-only). On phones the preview is below the Download buttons, so users may hit the gate before they even see the code.
2. **The page tells users the tool can't do what it does.**
   - "When not to use it" says it "encodes plain text and URLs only, not [WiFi/vCard]" and that SVG needs another tool.
   - Live, WiFi and vCard work (decoded) and Download SVG exists.
   - Details "How to use" mentions PNG only. There is one FAQ.
   - Google shows this text in the snippet.
3. **Two real encoding/rendering bugs:**
   - **vCard ";" is not escaped.** "Smith; Jones & Co, LLC" becomes `ORG:Smith; Jones & Co\, LLC`, so the org is split on the phone. The cause is a one-character no-op in `p()`.
   - **Logos are stretched to a square.** An 800×200 logo's circle becomes a 15×54 ellipse. The SVG keeps the aspect ratio by default, so the two formats likely differ (verify).
4. **The Pro/Premium story is muddled.**
   - The title "QR Code Generator Online - Instant, **With Logo**" competes with the Premium custom-qr "QR Code Generator with Logo".
   - The "Next step" card sells Premium with "Put your logo in the middle", which this Pro tool already does.
   - /es says "gratis". The other 8 locales have an English title **and** an English H1, even client-side.
5. **Accessibility:**
   - axe finds 3 critical issues: the two unnamed select triggers and the unlabelled logo input.
   - The canvas has no text alternative.
   - The tabs don't respond to arrow keys.

## Outcomes we want

- A new visitor sees 10 remaining, sees the code before the Download button on a phone, and knows what one download costs and whether it carries a mark. Any mark keeps the quiet zone and the scan intact.
- Every sentence on the page, in the FAQ and in the video matches the 7 types, PNG and SVG.
- Contacts with ";" in a name or company import correctly. Logos keep their shape in PNG and SVG alike.
- Pro and Premium each have a distinct promise and title. Locales are localized and say "trial uses".

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | MEDIUM | 27/31 preview scenarios PASS (decoded). FAIL: vCard ";" (QR-07), logo aspect (QR-18), broken logo accepted silently (QR-20). Q17 (download size) deferred. Downloads **need re-run after midnight UTC**. `evidence/findings/live-functional-findings.md`, `json/decoded.json`, `json/explore-*.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | On par for types, logo and PNG/SVG; ahead on the capacity meter and contrast warnings. Missing (live-verified in the controls): transparent background, calendar/location/WhatsApp types, frame label. Competitors stress "no watermark, unlimited". `desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Instant preview and clear limits. On phones the preview is below Download; a broken logo fails silently; file names are fixed (qrcode.png); no note for javascript: links. |
| 4 | Layout attractiveness | **PARTIAL** | MEDIUM | Desktop and tablet: clean two-column layout with the preview above the fold. Phones: preview at y≈1094–1185 below Download; iPhone SE 329 > 320; ja +3 px. No ad overlaps; CLS ≤ 0.013. `screens/live/phone-pixel-7-full.jpg`, `screens/live/desktop-tool.png` |
| 5 | Payment process | **PARTIAL** | MEDIUM | The cap dialog is clear for PNG and SVG ("Your input stays where it is"). The mark is mentioned only in the dialog, not next to Download (split-pdf does this right). The upsell card's promise overlaps the Pro features. `screens/live/capped-png-click.png` |
| 6 | Information correct | **FAIL** | HIGH | "When not to use it" denies WiFi/vCard/SVG; the Details How-to mentions PNG only; the meta omits 3 types. `html/tool-visible.txt` |
| 7 | Indexing | **PASS** | — | 200, indexable, self canonical, in the sitemap (lastmod 2026-11-19) with a video block; ranks first for the brand query. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | HIGH | The title's "With Logo" cannibalizes custom-qr; 75-char meta; FAQPage with 1 question; /es "gratis"; 8 locales with English title and H1; Offer without a billing period; generic OG. |
| 9 | Blog post | **FAIL** | MEDIUM | No dedicated post found (QR sitemap slugs and the topic page; another slug is an unverified absence). Two near-duplicate custom-qr posts. Gap: WiFi/vCard how-tos. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | OwklDj1Z5_w, 67 s, 6 views, consistent title, embedded. |
| 11 | FAQ / usage guide | **FAIL** | MEDIUM | One FAQ entry. The Details section contradicts About. The expiry, WiFi, PNG/SVG and mark questions are unanswered. |
| 12 | Video shows current capabilities | **PASS** (minor) | LOW | Current UI; codes decode. Shows the Link type only; "200+"; outro says "next free tool". |
| 13 | Storage | **PASS** (by design) | — | Local only. No cloud or Drive on this tool. |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only; no copy-image or share of the code (unverified absence beyond the visible controls). |
| 15 | Downloads | **N/A today (needs re-run after midnight UTC)** | — | Both formats gated at 0. Size, quiet zone, mark, decode, logo parity and file names go to the re-run. |
| 16 | Usage count | **PARTIAL** | HIGH | Preview, all types and all options never changed `usageToday` (display). Per-format cost **needs re-run**. 22/22 fresh contexts at 0 (display-only). |
| 17 | Categorization | **PASS** | — | QR Codes & Barcodes, Professional Tool. |
| 18 | Location in site | **PASS** | — | Breadcrumb; "Part of: Creating a Restaurant Menu"; next step Banner & Sign Maker (Premium); More from QR: custom-qr, bulk-qr, scanner. P2: a "Test it with QR & Barcode Scanner" link next to Download would fit the "test-scan it" step. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic. Demand: rank 8, 685+588 impressions in the site map (GSC not available). |
| 20 | Merge? | **PARTIAL**: keep, but sharpen | MEDIUM | It overlaps the Premium custom-qr on the logo. Keep Pro as "fast, all types, logo"; reserve shapes, gradients and PDF for Premium, and retitle. |
| 21 | Remove? | **N/A: keep** | — | Core, high-demand tool. |
| 22 | Duplicates | **PARTIAL** | MEDIUM | Within C04: custom-qr overlap (title and logo); bulk-qr is distinct (lists). Two near-duplicate blog posts. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles.
- No ad overlaps.
- Desktop and tablet preview above the fold.
- Phones don't overflow, except iPhone SE.
- Keyboard: Enter on tabs; selects work.

**FAIL / PARTIAL:**
- The phone preview is below Download (MEDIUM).
- iPhone SE 329 px; ja +3 px.
- /es "gratis"; 8 locales with English title and H1 (HIGH for SEO).
- /ar 404; USD only.
- axe critical ×3, plus a serious mismatch; the canvas has no alternative; no arrow keys on the tabs.

**Ads:** keep them, in reserved fixed-height slots below the tool (as now). Never between the preview and the Download buttons.

## Suggested direction (interpret freely)

1. **Trial meter (P0, shared)** as in FDP-02 to FDP-05. Also state the per-download cost next to the buttons.
2. **Copy truth pass (P1).**
   - Rewrite "When not to use it" and the Details How-to from the real UI.
   - Expand the FAQ: expiry, WiFi, vCard, PNG vs SVG, logo size, trial uses and the mark.
   - Lengthen the meta.
3. **Bugs (P1).**
   - Escape ";" in `p()`. Add a unit test with `;`, `,`, `\` and a newline.
   - Draw the logo with contain-fit (keep the aspect ratio) in the canvas. Keep the SVG consistent.
   - Error on an unreadable logo.
4. **C04 positioning and locales (P1).** Drop "With Logo" from the Pro title, or restate what Premium adds. Make the upsell card name shapes, gradients and PDF. Localize the 8 locales and remove "gratis".
5. **Phone layout and a11y (P2).**
   - Put the preview above Download on narrow screens, or make it sticky.
   - Name the select triggers and label the logo input.
   - Give the canvas a label, e.g. aria-label "QR code for <content>".
   - Arrow-key tabs.
6. **Disclosure and re-run (P1, after the re-run).**
   - If trial downloads are marked, say so next to Download and make sure the mark sits outside the 4-module quiet zone.
   - Then decide whether a mark is appropriate on a QR at all (a reserved, documented area is better than a surprise).
7. **Nice-to-have (P2):** transparent background, calendar/location types, descriptive file names, a "Test with QR Scanner" link, and a dedicated WiFi/vCard blog post plus a 15 s WiFi video segment.

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy claim ("Runs on your device"). It was not network-audited here.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.

## Process

Inspect QrGenerator, qrHelpers, the download stamp, the usage router and the content entry → restate → propose → implement → verify with `scripts/` and `test-cases.md` (downloads after midnight UTC).
