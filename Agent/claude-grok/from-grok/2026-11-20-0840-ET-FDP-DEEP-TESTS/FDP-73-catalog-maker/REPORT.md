Sent: 2026-11-21 16:53 ET

# FDP-73 Product Catalog Maker (catalog-maker): deep test report for Claude

- **Written:** 2026-11-21 16:55 EST (box `date`, ET). Testing ran 2026-11-21 16:17–16:52 EST.
- **Tool:** https://www.freedailypro.com/tool/catalog-maker
  - TEST-ORDER row 73: **Premium**, Publishing & Print Makers. Plan note "test-plan (unranked): GSC top-50 SEO backfill 14". **Duplicate group C40** (magazine-maker #52, print-publication-studio, user-manual-writer).
  - Trial strip "Trial: 2 uses/day"; Quick Buy Day Pass $3 / Monthly $9.99 (all 6 geo contexts).
  - Video HK72jnNM8yA (embedded, 125 s, uploaded 2026-09-23). Blogs /blog/catalog-maker and /blog/edition-ledger-and-print-and-web-pdfs-for-a-catalog-series are linked (both 200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `CatalogMaker-BlrB82Gj.js`, `productCatalog-CL4Qj03q.js`, shared `bookAssembly-DmpTM49o.js`):**
  - **Product list:** title, company, product cards (name, SKU, price, MOQ, category, order link → link + QR, description, photo). There are 3 templates, a paste/CSV importer, currency (10), columns (2/3), page (Letter/A4), accent colour, cover/price list/contents toggles, tax mode (none / before tax / included, with default and per-product rates), logo, brand profile, and save/open of the catalog to a file on the device.
  - **Combine files:** PDF/DOCX/TXT/images → cover, TOC, List of Images, price list page, product index, back-page QR or barcode; 17 page sizes.
  - **Build Catalog / Assemble Catalog** (no usage call) → "Download Catalog (N pages)", Save to Google Drive, Save to my cloud storage, "Preview first page".
  - **Charging:** in Product list mode the Download click logs a use once per unique content hash (`Oe`: `lt(z.current, hash)` → `He(toolId)`). Re-downloading the same build is free; an edited build is a new charge. The download carries a "Created with FreeDailyPro.com" mark on every page.
- **Testers:**
  - Desk: page copy (10 FAQs, how-to, when / when not, tips, limitations, privacy), JSON-LD, 2 blogs, JS.
  - Playwright, guest contexts. The built PDF was read from the page's own Blob (a `URL.createObjectURL` hook in the test, not a UI download) and checked with pypdf / pdftotext / pdftoppm.
  - Test files from make-testfiles.py: photos (4:3, portrait, 10 px, 4000 px, WebP, fake JPG); CSVs (24-SKU line sheet with header, no header, bad rows, quoted, BOM + semicolons, TSV, Unicode + "Call for price", long text, 300 rows); combine files (Letter + A4-landscape PDFs, DOCX, TXT, PNG, encrypted, damaged, .doc, .xlsx); JSON files.
  - Runs: `zero.json` (at 2/2, Chromium + WebKit), `cases.json` (20 cases at 2/2), `extra.json` / `extra2.json` (text price, comma prices, tax, back-page codes), `left-firefox.json` (start 0/2), `preview.json`, `quickbuy.json`.
  - Matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe. Video frame sheet + auto captions.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe; the cloud dialog stopped at "Sign in"; the Drive popup was closed). No ad clicks. No site or repo changes.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); Save to Google Drive with uses left (Google sign-in popup); Save to my cloud storage (sign-in + $4.99/month add-on); paid-pass output (no mark). Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** one row (#73) in `/workspace/deep/RERUN-AFTER-RESET.md`. It checks the 0/2 → 2/2 jump after one download (a second, edited catalog was then blocked). Only 1 of ~85 fresh contexts had uses today (Chromium 25 + 40, Tokyo time zone 10, Firefox 6, plus the cap runs), so it could not be repeated.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a small seller turning a spreadsheet into a line sheet for a buyer, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1. A full-quality result at 0 is a pending owner question. A real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1 (check):**
1. **One download moved the counter 0/2 → 2/2, and the next edited catalog was blocked.**
   - left-firefox.json, the only context with uses: L01 Download → one `usage.log` POST → strip **2/2**. Re-downloading the same build was free (correct, same hash).
   - Then Edit → price 12.50 → 13.00 → Build → Download opened the **cap dialog** (L03). L04/L05/L06 (combine) were also blocked.
   - So in this run, two trial uses gave one catalog. The same jump was seen on #57 (document-assembler, Premium). It may be the shared test IP's server count rather than a real bug, so this is display-only evidence. **Check the server count for the `…:premium` scope** after the reset (RERUN row).
   - The gate itself is right: per unique content, not per page load, and every fresh page at 2/2 is gated (Download, Save to Google Drive, Combine Download).

**Owner question:** none new.
- At 0 uses, "Preview first page" shows only the cover as a 489×633 image. Download, Save to Google Drive and the combine Download open the cap dialog. "Save catalog to this device" works at 0 (the user's own input as JSON, no POST). That looks right.

**P2 — where to look:**
- **Text prices are refused, but the page promises them.**
  - FAQ: "text such as 'Ask for quote' is left exactly as typed". Tips: "A price that is not a number, such as 'Call for price', is printed exactly as typed".
  - Live: typing "Ask for quote" or importing "Call for price" gives "Enter a number, like 12.50" and disables Build (X02, K08). A wholesale sheet with "POA" items cannot be built.
  - Either allow non-numeric prices (print as typed, leave them out of tax totals) or change the FAQ and tips.
- **An invalid back-page barcode gives a silent blank last page.**
  - Combine files → Real Barcode → EAN-13 (the default) → value "12345" → Assemble. You get "Catalog assembled!" and **page 5 is completely blank** (0 dark pixels; X10).
  - The error is only in the console: "Couldn't generate a barcode: EAN-13 needs 12 digits… You entered 5" (`bookAssembly` catches it and returns null).
  - Valid EAN-13, Code 128 and QR all render (X11–X13). Validate the value inline (the FAQ already says "must be valid"), and skip the back page instead of printing a blank one.
- **WebP is accepted, then blocks the whole Combine assembly** (K19). The drop zone accepts `image/webp` and the FAQ lists WebP. On Assemble you get the toast "lamp.webp isn't a supported file type" and no catalog is built (the page waited 120 s with no result). WebP works as a product photo (K11). This is the same as #52 (shared `bookAssembly`). Convert WebP through canvas, or drop it from `accept` and the FAQ, and skip a bad file instead of failing the catalog.
- **With an order link, 2-per-row cards fit only one row per page** (K02, 24 SKUs → 15 pages, half of each page empty). The link + QR + MOQ makes each card about 370 pt tall. The blog's worked example ("four product pages") assumes no links. Shrink the QR / photo frame so two rows fit, or warn about the page count.
- **Video HK72jnNM8yA is out of date:**
  - It shows the old Combine-only UI with a personal macOS file picker. On-screen text says "10 free uses daily"; the thumbnail says "FREE · PRIVATE · NO LOGIN".
  - The title is "How to Use Catalog Maker – Free Step-by-Step Walkthrough" and the description says "Try Catalog Maker free… Free daily uses… no account needed". The captions are only the outro.
  - VideoObject name "How to Make a Product Catalog PDF Online" doesn't match the YouTube title. Re-record Product list mode (CSV import, templates, tax) with Premium wording.
- **Locale pages:** the title, meta, builder labels, templates and FAQ headings are English under a translated H1 (es/pt/fr/de/ja/hi/zh/ko/id; englishLabels in matrix-results.json).
- **C40 overlap:** magazine-maker (#52) shares the Combine engine (`bookAssembly`). The page cross-sells print-publication-studio (Workflow). The ladder is clear; keep both page makers.

**P3:**
- The "Maker's lookbook" template also switches the page size to **A4**; the card copy says only "2 larger cards per row, no price list" (K12).
- Rupee prices use Western grouping (₹125,000.00, not ₹1,25,000.00). Yen rounds 12.50 → ¥13 (correct for 0 decimals; maybe hint it).
- Non-Latin names (Japanese, Arabic) and the Arabic/Japanese categories are drawn as outlines, so they are not searchable or copyable. They render correctly (X01). The emoji warning toast is good.
- The blog says the importer "reads five columns"; the tool reads seven (MOQ and link added).
- The brand-profile loader refused a plain `{name, primary, accent}` JSON ("not a FreeDailyPro profile or brand kit"). That's fine, but the expected format isn't documented anywhere on the page.
- Combine: section names default to file names ("sheet-letter-2p"); the List of Images page is numbered "iii" while the cover and TOC are not (same as #52).
- iPhone SE: 9 px horizontal overflow (329/320) from the Tax/brand row (logo file input, tax select). ja desktop 1369 px. iPad/desktop inputs are 14 px (fine on desktop).
- axe desktop: label-content-name-mismatch (serious, `.right-2` floating button) and region (moderate); Pixel 7 clean. de-DE/fr-FR consent banner shown.
- Keyboard: 33 Tabs from the top to Catalog Title (templates first).

## Intent

A seller has a spreadsheet and some photos and needs a clean catalog PDF for a buyer today. The PDFs are correct (grouping, contents page numbers, price list, tax maths, currency formatting, links + QR) and the gate charges per unique catalog. The rough edges are a documented feature that doesn't work (text prices), a silent blank page, and WebP in Combine.

## What works (verified in the PDFs)

- **Line sheet:** 24 rows with headers Product/Code/Cost/Group (recognised) → 24 cards. Contents lists Kitchen 3, Lighting 6, Textiles 9, Decor 12, Price list 15 (all correct). Each card has an MOQ, a clickable `example.com/p/N` link and a QR code.
- **Importer:**
  - With no header, the columns are read in order. Quoted commas and line breaks are kept. BOM + semicolons and TSV both work.
  - Bad rows are flagged in red with a summary toast: "5 imported, 1 bad price on row 3, 1 bad minimum order on row 5, 1 bad link on row 6, 1 skipped (no name) on row 7". `javascript:` links are refused.
  - "1,299.00" → $1,299.00; "12,50" → $12.50. 300 rows → 46 pages (A4, 3 per row) in 1.8 s.
- **Tax:**
  - Before tax at 8.875 %: $12.50 + $1.11 = $13.61; $34.00 + $3.02 = $37.02.
  - Included at 10 % on product 1: $12.50 → tax $1.14, excl. $11.36.
- **Currencies:** €2,200.00, ¥13, ₹12.50 (glyph renders), AED 12.50.
- **Toggles:**
  - Cover, contents and price list toggles work: all off → 2 pages. Cover on with no title → "Enter a catalog title, or turn off the cover page."
  - Empty build gives three clear alerts. A long name is cut at 2 lines and the description at 4 (as documented).
- **Photos:** 10 px, 4000 px and WebP work as product photos. A fake JPG gets "That image couldn't be read. Try a JPG or PNG."
- **Templates and saving:** templates set the layout only (no sample products, as stated). Save catalog → `.catalog.json` (29 KB, photos embedded) → reopens with title, products and 2 photos. A wrong JSON gets "That file is not a saved FreeDailyPro catalog."
- **Combine files:**
  - Letter PDF + A4-landscape PDF + DOCX + TXT + PNG → cover, TOC, List of Images, bookmarks.
  - An encrypted PDF opens a password dialog and is skipped on cancel. A damaged PDF gets a "Repair PDF" hint. `.doc` and `.xlsx` get "can't be used here".
- **Gate:**
  - On a fresh page at 2/2, Download, Save to Google Drive and the Combine Download open the cap dialog (Chromium + WebKit). Nothing is saved.
  - Trial download: 5 pages, each with "Created with FreeDailyPro.com".
  - Quick Buy: Day Pass → email dialog (stopped); Monthly → Stripe (stopped).

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Two modes, importer, tax, currencies, templates, save/open, codes. |
| 2 | Completeness | PARTIAL | Text prices promised but refused. |
| 3 | Ease of use | PARTIAL | Silent blank barcode page; WebP blocks Combine. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px overflow. |
| 5 | Payment process | PASS | Strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | **FAIL** | "Call for price"/"Ask for quote" printed as typed is false; WebP in FAQ. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS | Title "Product Catalog Maker - Create a Catalog PDF Online"; meta 120 chars. |
| 9 | Blog | PASS (minor) | 2 linked; "five columns" outdated. |
| 10 | YouTube video | PASS | HK72jnNM8yA embedded. |
| 11 | FAQ / guide correct | FAIL | Text price, WebP. |
| 12 | Video shows current capability | FAIL | Old Combine-only UI; "10 free uses"; "free / no login". |
| 13 | Storage | N/A (sign-in) | Cloud needs sign-in + add-on; save-to-device JSON works. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | PDF correct, marked on trial. |
| 16 | Usage count | **CHECK (P1)** | Per unique catalog (good); 0→2/2 after one download. |
| 17 | Categorization in section | PASS | Publishing & Print Makers / Premium. |
| 18 | Correct section of site | PASS | Workflow cross-sell to Print & Publication Studio. |
| 19 | AI need and demand | PASS | "product catalog maker", "line sheet pdf", "catalog from csv". |
| 20 | Merge better? | No | Keep separate from magazine-maker; share the engine. |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | C40 | See 20. |

## After fixes, rerun

- `px73-live.js extra` (X02 text price builds) and `extra2` (X10 shows an inline error / no blank page). Also `cases` (K19 Combine with WebP builds or refuses up front), and `TRIES=40 px73-live.js left firefox` after the reset (second edited catalog downloads).
