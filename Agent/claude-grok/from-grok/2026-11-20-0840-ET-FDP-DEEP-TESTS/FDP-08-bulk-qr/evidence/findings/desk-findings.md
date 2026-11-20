Sent: 2026-11-20 08:40 ET

# FDP-08 bulk-qr: desk findings

- **Written:** 2026-11-19 12:55:01 EST (box `date`, ET). Sources: `html/tool.html`, `html/tool-visible.txt`, `js/`, `html/locales.txt`, the blog post, the sitemap and WebSearch (2026-11-19).
- **GSC data is not available.**

## Identity and indexing
- https://www.freedailypro.com/tool/bulk-qr returns 200 and is in the sitemap (lastmod 2026-11-19) with a video block (ui6-i9QUCxA, published 2026-10-16).
- Brand query "freedailypro bulk qr generator": the tool ranks #1 and the blog post #4 (WebSearch, 2026-11-19).
- Title: "Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro". H1: "Bulk QR Generator". Meta (96 chars): "Generate hundreds of QR codes at once and download them as one ZIP. Fast, right in your browser."
- JSON-LD:
  - Offer 4.99 USD with no billing period. The strip shows $1 day / $4.99 monthly.
  - FAQPage with 6 questions: tracking, naming, ZIP contents, the 500 max, EC, PNG vs SVG.
  - VideoObject.
- Category: QR Codes & Barcodes, **Professional Tool**, 10 trial uses a day.

## Copy vs code (consistent, with gaps)
- The copy matches the code on these points: the 500 cap, PNG sizes 300/600/1000/2000, EC L/M/Q/H, the 300-character warning, the duplicate count, 001- numbering, index.csv columns file,name,value, and the 4-module quiet zone. The code (BulkQr: `margin:4`) and the live file (3.99 modules) both confirm the quiet zone.
- **Guest passes** are described in Details only. Nothing says **where the guests come from**:
  - They come from the Event Suite project: Guest Manager, a Workflow Product, or an opened project file.
  - So for a normal visitor "Guest passes from my project (0)" is a dead end until they press "Try a sample".
- **The pass key lives "in this tab only, then erased".** The QR Scanner can only verify passes with the same project file.
  - Nothing near Generate tells the user to Save the project after making passes.
  - Save project is **gated by trial uses at 0** (live), so a capped user can't keep the key.
- **The saved project file holds every guest's email, dietary needs, room and arrival dates**, as well as vendors, quotes and expenses (seen in the sample file). The note warns only about the pass key.
- The Limitations say "An entry too long for a QR code can stop the run with a Generation failed message". This is true by design, but it means one bad line kills a 500-code batch, and the preview goes blank for **all** rows (live S08).
- CSV guard: `csv.js` prefixes values starting with `= + - @` with an apostrophe (formula-injection guard, good). It also changes values like "-5+3" in index.csv (cosmetic).
- File names: `S()` strips accents (NFKD) and replaces anything else with "-". So "日本" gives "code", and "Grüße" gives "Gru-e". Numbering prevents collisions.
- Name mode deduplicates by **value**. So "Table 1,…/menu" and "Table 2,…/menu" produce one file, and the second named row is dropped with "1 duplicate line skipped". This is a common table-card case.
- "OnlyName," (empty value) encodes "OnlyName," literally.

## Pass codes (passCode.js)
- `FDP1.<tag6>.<guestId>.<sig14>`:
  - tag = SHA-256("tag:"+key), first 6 base64url characters
  - sig = HMAC-SHA256(key, "FDP1.tag.id"), truncated to 14 characters (84 bits)
  - the key is 32 random bytes
- Verified offline: 5/5 downloaded passes match the saved key. "Try a sample" makes a new random key per context (2 contexts gave different tags). The codes carry no name or email, as the copy says.

## Blog
- /blog/bulk-qr-codes-from-a-url-list-as-zip (2026-10-24) is accurate on the 500 cap, sizes, EC and name,value.
- Gaps:
  - no guest passes or project
  - it suggests a "PDF proof sheet" (the tool makes none)
  - "Decorative bulk runs" (the tool has no decoration)
  - it links the custom-qr post under the old name "QR Code Designer (Logo & Colors)"
- No near-duplicate bulk-qr post (the sitemap has only this bulk-QR slug; others are bulk-image).

## C04 cluster
- custom-qr (Premium) now has a 200-code **styled** bulk ZIP, and qr-generator says "with Logo".
- bulk-qr "When not to use it" sends logo, Wi-Fi and contact users to "a single QR code generator". It doesn't name custom-qr's styled bulk, which is the natural upsell.

## Competitors (WebSearch 2026-11-19)
- BatchQRCode, FigQR, bulkqr.codes, QR-10 and Panda Toolbox all run in the browser, with no upload, no account, and "free, no limit" or 100–5,000 per batch.
- Common features bulk-qr lacks (live-verified in its controls): **CSV/XLSX file upload with column mapping**, a header row skip, JPEG, a quiet-zone option, a logo or caption, and **PDF label sheets (Avery 5160/L7160)** (bulkqr.codes).
- bulk-qr's unique angle: **signed guest passes** that the QR Scanner verifies offline, plus index.csv.

## Locales (curl, SSR)
- en 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- es 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- fr 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- de 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- pt 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- ja 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- zh 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- hi 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- ko 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- id 200 | Generate QR Codes in Bulk Online - Batch Tool | FreeDailyPro | Bulk QR Generator | 
- ar 404 | Page not found | FreeDailyPro | Every Professional Task. One Browser Platform | 
- it 404 | Page not found | FreeDailyPro | Every Professional Task. One Browser Platform | 
- The title and H1 stay English in all 9 non-English locales. /ar and /it are 404 (not in hreflang). No "gratis"-type words in the SSR HTML.

## Usage logging order (code-read, BulkQr)
- `oe()` calls `logUsageNow()` **before** building the ZIP, then `try { … } catch { "Generation failed" }`. By code, a batch that fails (e.g. one over-long line) still consumes a trial use, and nothing is downloaded. Live confirmation is battery context E (re-run).
