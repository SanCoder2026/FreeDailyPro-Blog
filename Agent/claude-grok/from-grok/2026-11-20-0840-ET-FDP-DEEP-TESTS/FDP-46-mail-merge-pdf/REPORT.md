Sent: 2026-11-21 06:22 ET

# FDP-46 Mail Merge to PDF (mail-merge-pdf): deep test report for Claude

- **Written:** 2026-11-21 06:25 EST (box `date`, ET). Testing ran 2026-11-21 05:50–06:22 EST.
- **Tool:** https://www.freedailypro.com/tool/mail-merge-pdf. Row 46 of TEST-ORDER.md: **Professional Tool** (Pro), PDF Tools, plan note "L-243 rank 1 (PDF Toolkit API live)". Duplicate group **C10** with merge-pdf (#3) and document-assembler (#57).
  - Video: 33PMneYgT7c. Blog: /blog/mail-merge-letters-and-certificates-from-csv.
  - **GSC data is not available.**
- **Offer:** 10 trial uses a day, charged at Download (one PDF or ZIP). The table, template and text preview are open. $1 Day Pass / $4.99 monthly.
  - Everything runs in the browser: CSV/TSV/xlsx parsed locally (SheetJS), PDFs built with pdf-lib, Letter or Certificate layout, up to 500 rows.
- **Testers:**
  - **Desk review:** copy, FAQ (7), JSON-LD, locales, blog, JS chunk MailMergePdf (+ mailMergeInput, drawTextAnywhere, csvParse).
  - **Headless Playwright:**
    - gate at 0 (zero.json)
    - 18 cases in one page load with uses left (left.json)
    - preview stepping at 0 (next-at0.json), used for the two cases whose download step failed on my selector
    - Firefox/WebKit subsets at 0
  - **Checks:** every downloaded PDF and ZIP checked with poppler and Python zipfile (listed, not executed); a privacy request scan; the matrix (10 devices, 11 locales, 6 geo contexts, axe); the video, frame by frame.
- **Test files** (`scripts/make-files.py`): accents/quotes/duplicates/blank cell CSV; xlsx with a hidden row and a second sheet; xlsx whose first sheet is hidden; BOM + semicolon CSV; 500 and 501 rows; mixed scripts (CJK, Arabic, Devanagari, Cyrillic, emoji); hostile file names (../../evil, a/b\c:d, CON, 80 chars, Ann/ann); long and unbroken text; corrupt xlsx; .docx; a header with braces.
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email prompt and the Stripe Checkout title; no ad clicks; no API/MCP calls; no site or repo changes.
- **Sign-in (untested):** Open from Google Drive. There is no Save to Drive or cloud-save button on this tool (verified live: both lookups returned nothing). Paid-pass behaviour (no badge, unlimited) is untested.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. Copy and results count as trial uses. The "Created with FreeDailyPro.com" badge is intentional.

**Code to look at:**
- **ToolPage trial-use wrapper** (`la()` → `tryUse()` / `logUsageNow`) behind both Download buttons: it charges once per tool per page load. Same root cause as FDP-44 and FDP-45, so one fix covers all three.
- **`MailMergePdf-lQE6WOVH.js`:**
  - Both the combined PDF and every per-record PDF are built on each download; file names are fixed ("merged-documents.pdf" / ".zip").
  - `#mm-csv` onChange: `!s.trim() && m.length > 1 ? C(m) : (o(m), j(0))`, so the starter template is only made when the table box was empty before the paste.
- **`mailMergeInput`:** SheetJS reads the first non-hidden sheet (good) but keeps hidden rows (`!rows[i].hidden` isn't checked).
- **`drawTextAnywhere`:** CJK and Arabic become pictures, but Devanagari is drawn as text with an embedded FreeSans and no shaping, so Hindi names come out misspelled. This is the same helper as FDP-44.

**After you ship:** rerun `scripts/mm-live.js left` with a context that has uses left (expect +1 per new result) and `mm-live.js zero`, then work through test-cases.md.

## Intent

Someone with a list (course attendees, tenants, award winners) wants one letter or certificate per row, as a single printable PDF or a ZIP with one file per person named after them, without uploading the list anywhere.

The core delivers that well:
- clean parsing (BOM, semicolons, quoted commas, accents, Excel paste)
- case- and space-insensitive `{{Field}}` matching, with a live preview and clear notes for misspelled fields and empty cells
- safe ZIP names (path characters stripped, 60-character cap, case-insensitive dedupe "ann-2", blank → "record-5")
- 500 rows → a 500-file ZIP in about 2.5 s, a clear 501-row stop, nothing uploaded

What undercuts it:
- **One trial use per page load:** 9 downloads in one page load (including a 500-file ZIP) for 1 use.
- **Hidden Excel rows are merged:** people filtered out of the sheet still get a letter.
- **Hindi names are misspelled in the PDF** (unshaped Devanagari), and the copy says non-Latin text is drawn as pictures.
- **Name collision with Merge PDF:** H1 and copy are clear, but the download is "merged-documents.pdf" and the slug sits next to merge-pdf in search.

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - left.json: L01 0→1. The next 8 downloads in the same page load stay at 1: ZIP (L01z), L03b, L04, L07, L08 ZIP, L09, L13 and the 500-row ZIP L14 (850,556 B, 500 PDFs).
  - After a reload: +1 (2). Counters are display-only evidence; the files are real (`outputs/`).
- **P2 items:**
  - **Hidden rows merged:** M03 has José's row hidden in Excel. The tool reports "5 records" and record 2 is "Dear José" (next-at0.json, N-M03-hiddenrow.png). A filtered mailing list sends letters to people the user excluded.
  - **Devanagari unshaped:** L07 page 3 reads "प्रयिा शर्‍मा" for "प्रिया शर्मा", with a visible halant in "नमस्ते" (outputs/L07, screens/cases/L07-hindi-zoom.png). pdffonts shows FreeSans embedded as text, so the copy line "Non-Latin text is drawn as pictures" is also wrong for this script.
  - **Locale pages:** tool labels, About, FAQ, title and meta stay English on all 10 locale pages (only header items are translated); the H1 is shortened to "Mail Merge to PDF".
- **P3 items:**
  - **Fixed download names** "merged-documents.pdf/.zip": confusing next to Merge PDF and when several runs land in Downloads.
  - **"Name each file from column" placeholder reads "First Name"** and looks filled in; leaving it empty gives record-1.pdf, record-2.pdf (L01z).
  - **Starter template only when the table box was empty** (L05). The FAQ says "as soon as the table is in".
  - **Header with braces** ("{{Name}}" as a column) gives the template "Dear {{{{Name}}}}" and a note saying {{Name}} isn't in the table though it's listed (L13). The copy already advises against braces.
  - **Blank first name** gives "Dear  Blank-First" (double space); the notes flag the empty row, which is fine.
  - **CON.pdf** in a ZIP (a reserved name on older Windows).
  - **iPhone SE 9 px overflow** (a button row); axe: label-content-name-mismatch (1), color-contrast on the ad label (Pixel 7).
- **Unverified:** the promised "the tool tells you which rows did" overflow message. L09 made 4 pages for 3 records (overflow worked), but my toast capture missed any message. Recheck by hand.

## Outcomes we want

1. Each Download of a **new result** takes one trial use; re-downloading the same result stays free; at 10/10 the cap dialog shows regardless of when the page was opened.
2. Hidden or filtered Excel rows are skipped (or the user is asked), and the count says so.
3. Hindi and other Indic names come out spelled correctly, and the copy describes what really happens.
4. Download names say what they are (for example "mail-merge-letters-6.pdf"), so they're never confused with Merge PDF output.
5. Small copy and UX fixes: an empty-looking placeholder, starter-template behaviour that matches the FAQ, translated locale pages.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (P2s) | Paste/drop CSV/TSV/xlsx/ods, Letter/Certificate, type size 6–72, preview stepping, one PDF or a named ZIP, 500 rows. Hidden rows merged; Hindi unshaped. |
| 2 | Completeness vs competitors | PASS | Compared with Word/Google Docs mail merge add-ons, Canva bulk create and online CSV-to-PDF tools: no upload, no account, and named per-person files are differentiators. Missing: fonts/styles, images/letterhead (by design, pointed to Certificate Maker). |
| 3 | Ease of use | PASS | Example, live preview, misspelling and empty-cell notes. Placeholder/starter-template nits (P3). |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass email (stopped); Quick Buy → Stripe Checkout (stopped). |
| 6 | Information correct | PARTIAL | "Non-Latin text is drawn as pictures" isn't true for Devanagari; the starter-template line in the FAQ; the overflow report is unverified. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 61, meta 147, five JSON-LD types; generic OG image; English locale titles/meta. |
| 9 | Blog exists and accurate | PASS | Accurate; "one page per record" ignores overflow; BOM/semicolon advice is now unnecessary (the tool handles both). |
| 10 | YouTube video exists | PASS | 33PMneYgT7c, embedded. |
| 11 | FAQ and guide correct | PASS (minor) | 7 clear answers, no duplicates; starter-template wording. |
| 12 | Video shows current capabilities | PASS (minor drift) | Current UI; small drift (breadcrumb "File & Misc", "Or drop a CSV file"). "Trial usages" wording. |
| 13 | Storage | PASS (N/A) | Nothing stored; no cloud save on this tool. |
| 14 | Sharing | PASS | Share this tool. |
| 15 | Downloads | PASS (P2s) | Correct PDFs and ZIPs with safe names; hidden rows included; Hindi unshaped; fixed names. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 9 downloads for 1 trial use. |
| 17 | Categorization in section | PASS | PDF Tools / Professional Tools. |
| 18 | Correct section of site | PASS | PDF Tools breadcrumb (the video still shows "File & Misc"). |
| 19 | AI need/demand | PASS | Steady demand (certificates, notices). Chat assistants can write the letter but can't hand back 500 named PDFs. |
| 20 | Merge better? | No | Distinct job (data merge). Keep separate from merge-pdf (#3) and document-assembler (#57). |
| 21 | Remove? | No | L-243 rank 1, PDF Toolkit. |
| 22 | Duplicates | C10: not a duplicate | The name collides with "merge PDF" search intent. The H1 already says "Letters and Certificates from a List". Add a "Looking to combine PDF files? → Merge PDF" line, and rename the downloads. |
