Sent: 2026-11-01 6:50 AM ET (Grok Orchestrator → Claude)

# API cycles 19–21: stop billed bad data first, then make invoicing and CSV cleaning best-in-class

Source: owner (Santosh's standing order: every fix goes to Claude via from-grok; Rule 1, be best in the world and easy to use).

## Intent
Developers and AI agents paying through RapidAPI must never get silently wrong data or be billed for garbage input. Once that holds, the invoicing and CSV families should beat DueDate/Invovate/PithLab-class APIs so we can list job-named products (Mortgage & Home Finance, CSV & Spreadsheet Data Cleaning, Invoice & Getting Paid).

## Why now
Developer bot audit c21 (Nov 1, 6:15–6:22 AM ET, keyed, metering exact 21 = 21): no deploy since c20; B-API-94 (markdown XSS) and B-API-104 (silent CSV data loss) are still live on the paid RapidAPI Text listing; invoice/receipt routes bill negative or nonsense input; proposal turns € into $ and sums it. Still open from earlier briefs: B-API-14 keyless limit (13 of 14 keyless calls served this hour, no 429), B-API-94 (sent 03:15).

## Order we'd like (bugs on paid listings first)
1. B-API-94 (already sent 03:15), 2. B-API-104, 3. B-API-110, 4. B-API-112, 5. B-API-105, 6. B-API-111 maturity-date fix part, 7. B-API-103 (mark Mortgage & Home Finance group READY), then the capability items 109, 106, 107, 108, 111 (late-fee route), 113. Please report each by ID with a live probe; our Developer bot will re-verify keyed.

## Briefs (outcomes and done-when are the contract; how you build it is your call)
- **B-API-103 Put the strong home-finance routes where buyers look.** *(listing/positioning, intent-first)* Intent: people searching "mortgage calculator API", "refinance API", "affordability API" find our exact, validated routes. Why: mortgage/refinance/affordability are best-in-class here but absent from the paid RapidAPI Finance endpoint list; the MCP group is served at `/mcp/loans-mortgage` while the spec says `mortgage-loans` (B-API-88). Outcome: one slug with an alias, mortgage/refinance/affordability (+ B-API-99/100 when done) in the Finance listing endpoint list or a job-named listing (below). Done when `/mcp/mortgage-loans` and `/mcp/loans-mortgage` both answer, and the listing shows the 3 routes with examples.
- **B-API-104 CSV parser never silently corrupts data (BOM, delimiter, ragged rows).** *(medium-high; live on paid RapidAPI Text `textCsv` + MCP `text_csv`)*
  - *Intent:* a developer or agent hands us any real-world CSV export (Excel "CSV UTF-8", European `;` files, TSV) and gets the right columns back, or a clear error — never quietly wrong data.
  - *Why:* D2 keys every row `"\ufeffName"` (Excel's default UTF-8 CSV starts with a BOM); D4 turns a `;` file into one column and drops `,50`/`,00` from the amounts with a 200. Python's sniffer, PithLab and FindUtils auto-detect the delimiter; our own pptx/from-csv already does.
  - *Outcome:* strip a leading BOM; `delimiter:"auto"` default (`,` `;` tab `|`) and echo `delimiterUsed`; `skipEmptyLines` (default true); `trim` option; ragged rows reported in `warnings[]` (row number, expected vs got) and **never truncated** (extra cells kept as `_extra` or 422 with `strict:true`); unbalanced quote → 422 with line number; unquoted inner quotes kept literally.
  - *Done when:* D2 returns keys `Name…Amount`, 4 rows (blank skipped) and a warning for the Ali row; D4 with no delimiter returns `{"name":"José","city":"São Paulo","amount":"1.234,50"}` + `delimiterUsed:";"`; `a,"b` → 422 unbilled naming line 1.
- **B-API-105 CSV export is spreadsheet-safe and takes records.** *(medium, security)*
  - *Intent:* an app that exports user data to CSV for Excel/Sheets can't be turned into a formula-injection vector.
  - *Why:* D3 writes `=1+1` and `@SUM(A1)` raw; OWASP CSV Injection / CWE-1236 / ASVS 5.3.11 say neutralise cells starting `= + - @ \t \r` (apostrophe, or tab-in-quotes for Excel save/reopen). tanod.dev already offers formula-guarded CSV. Also only headers+rows are accepted; most callers have an array of objects.
  - *Outcome:* `stringify` gains `formulaGuard: "apostrophe" | "tab" | "none"` (default apostrophe; numbers like `-5` untouched when `numericSafe`), `lineEnding: "crlf"|"lf"`, `bom:true` for Excel, and `records: [{…}]` input (union of keys as headers, nested objects flattened `a.b`, arrays JSON-encoded).
  - *Done when:* D3 returns `"'=1+1"` and `"'@SUM(A1)"`, `-5` stays `-5`, and `records:[{"a":1,"b":{"c":2}},{"a":3,"d":"x"}]` → `a,b.c,d` header with 2 rows.
- **B-API-106 One-call CSV cleaner with a change report (new route).**
  - *Intent:* "clean this CSV before I import it" — trim, drop blank rows/columns, dedupe by email ignoring case/space, normalise headers, and tell me what changed.
  - *Why:* today it takes 4–5 calls (csv → sort → case-convert …) and still leaves duplicates (D6 kept `jane.doe@example.com ` vs `jane.doe@example.com`). PithLab, FindUtils, ApyHub and Apify all sell exactly this, and "CSV cleaner API / remove duplicates from CSV API" are the search terms.
  - *Outcome:* `/v1/data/csv-clean` (MCP `csv_clean`): delimiter auto, trim, removeEmptyRows/Columns, `dedupeKeys` (names or indexes) + ignoreCase + keep first/last, `headerStyle` snake/camel/title, `normalize.email` (trim+lowercase), optional `inferTypes`, `formulaGuard`; returns `cleanedCsv`, `rows` (JSON), `duplicatesCsv`, `report` (rows in/out, duplicates removed, blanks removed, ragged fixed, per-column null counts/types); 422 unbilled on unparseable input.
  - *Done when:* the D1 input with `dedupeKeys:["Email"], normalize:{email:true}, headerStyle:"snake"` returns 3 data rows (Jane, John, Ali), headers `name,email,company,notes,amount`, `" John Smith "` trimmed, and a report with duplicatesRemoved 1, blankRowsRemoved 1, raggedRows 1.
- **B-API-107 Text helpers fit data-cleaning use.** *(low-medium; live on RapidAPI Text)*
  - *Intent:* header normalisation and list dedupe give the same answer as lodash/pandas.
  - *Why:* snake/camel/kebab split acronyms per letter (`ZIP` → `z_i_p`, `USD` → `u_s_d`, D8); sort `unique` doesn't trim (D6); extract-emails returns case duplicates (D7).
  - *Outcome:* acronym-aware word split (`ZIP/Postal code` → `zip_postal_code`, `Amount (USD)` → `amount_usd`, `XMLHttpRequest` → `xml_http_request`); `perLine:true` on case-convert; `trim:true` (default) on sort; `unique` + `lowercaseDomain` on extract-emails with `count`.
  - *Done when:* D8 with `perLine` on the 4 headers returns `first_name, e_mail_address, zip_postal_code, amount_usd`; D6 returns 3 lines; D7 with `unique:true` returns 5 addresses.
- **B-API-108 Spreadsheet conversions: XLSX ↔ CSV / JSON.** *(new capability, demand-led)*
  - *Intent:* an agent or no-code flow reads an Excel attachment into JSON rows, or delivers JSON as a real .xlsx — the most common step before/after cleaning.
  - *Why:* we have no XLSX in or out (only bank-statement→CSV and CSV→PPTX), while Toolkit API, Dokmatiq, tanod.dev, Neuvon and Apify all serve "Excel to JSON API" / "JSON to Excel API" / "XLSX to CSV API".
  - *Outcome:* `/v1/data/xlsx-to-json` (sheet list, pick sheet, header row, typed or string cells, max rows) and `/v1/data/to-xlsx` (records or CSV → .xlsx with header style, column widths, freeze header, number/date formats, multiple sheets); macros never run, zip-bomb/XXE guarded, unsupported .xls/encrypted → 422 unbilled; MCP tools in a new data group.
  - *Done when:* a 2-sheet sample workbook round-trips (xlsx → json → xlsx) with identical cell values, the header row frozen, and an encrypted file → 422 unbilled.
- **B-API-109 A real invoice document, at parity with our own Invoice Generator tool (supersedes B-API-12/29).** *(high value; demand-led)*
  - *Intent:* a freelancer's app or an AI agent sends one JSON invoice and gets back a finished, sendable invoice (PDF + totals), exactly what our site tool already makes.
  - *Why:* `/v1/business/invoice-totals` returns only subtotal/discount/tax/total (F2) and silently drops `currency`/`invoiceNumber` (F3b); the site's `/tool/invoice-generator` already has invoice #, date, terms (Due on receipt/Net 15/30/60) → due date, 10 currencies, seller/buyer addresses and tax IDs, tax label, credit lines, shipping, deposit/amount paid, notes, signature line and PDF. Invovate, Alder and thelawin.dev all sell JSON→PDF in one call with an MCP tool.
  - *Outcome:* `POST /v1/business/invoice` (MCP `business_invoice`): `number`, `issueDate`, `terms` or `dueDate`, `currency` (ISO 4217, symbol + decimals), `seller`/`buyer` {name, address, email, taxId}, `lines` [{description, qty, unit, unitPrice, taxPct?, kind:"item"|"credit"}], `discountPct|discountAmount`, `shipping`, `amountPaid`, `notes`, `paymentInstructions`; per-line totals, VAT summary by rate (reuse vat-gst lines), `balanceDue`; optional `reverseCharge:true` note for validated EU B2B; `format: json|pdf|html` (PDF from the site renderer; html escaped/sanitised); deterministic, nothing stored; invalid → 400 unbilled.
  - *Done when:* the F2 lines with `currency:"EUR"`, `terms:"net30"`, `issueDate:"2026-11-01"`, `amountPaid:500` return per-line totals 1062.50/99.99/19.99, dueDate 2026-12-01, balanceDue 658.68 (1158.68 − 500) in € with a valid PDF (opens, shows those numbers); a 19%/7% line mix shows a 2-row VAT summary equal to F4.
- **B-API-110 Invoice and receipt inputs are validated before billing.** *(medium; live on paid RapidAPI Business)*
  - *Intent:* garbage in gets a free, specific 400 — never a billed negative invoice or a receipt dated "not a date".
  - *Why:* F3 (qty −3, unitPrice −50 → total −332.07, 200 billed), F3b (unknown fields dropped despite `additionalProperties:false`), F9 (`date:"not a date"` echoed, 200 billed). thelawin.dev even offers a free `/validate` before spending a credit.
  - *Outcome:* `qty > 0`, `unitPrice ≥ 0` (credits only via an explicit credit line/`kind:"credit"`), `taxPct`/`discountPct` ≤ 100, dates `YYYY-MM-DD` and real calendar dates, unknown keys → 400 naming the key (match the OpenAPI), all unbilled; receipt gains `receiptNumber`, `paymentMethod`, `currency`, `amountPaid`/`balance`.
  - *Done when:* F3, F3b and F9 each return 400 at 0 cost with the field named; F2 and F8 unchanged.
- **B-API-111 Overdue-invoice late fee and statutory interest (new route), and an exact simple-interest maturity date.** *(medium; demand-led)*
  - *Intent:* "this invoice is 45 days late — what can I add?" answered in one call, with the date maths done for you.
  - *Why:* today the only route is simple-interest with fractional `years`; F7 interest is right (27.05) but `maturityDate` is rounded to 2027-01-01 instead of 2027-01-15, and there is no due date, as-of date, grace, flat fee, cap or statutory mode. DueDate, Duebay, curatedapi and Katalis all ship exactly this.
  - *Outcome:* `/v1/business/late-fee` (MCP `business_late_fee`): `amount`, `dueDate` (or `issueDate` + `terms`), `asOf`/`paymentDate`, `terms` {flatFee, percentMonthly | percentAnnual, compound, graceDays, capAmount|capPct}, `dayCount` actual/365|actual/360, optional `statutory: "uk-late-payment" | "eu-2011-7"` (rate per half-year + £40/70/100 or €40) with source/date; returns daysLate, dailyInterest, interest, fee, totalDue, steps, "not legal advice" note. simple-interest: accept `days` or `endDate`, return the exact maturity date (drop the rounding).
  - *Done when:* 1218.76 due 2026-12-01 paid 2027-01-15 at 18%/yr → 45 days, 27.05, totalDue 1245.81; same with `graceDays:10, flatFee:25` → interest from day 11 + 25; UK preset on £5,000 due 2025-12-01 paid 2026-01-30 matches Katalis' published 98.63 + 70; F7 maturityDate 2027-01-15.
- **B-API-112 Proposal/quote handles currency and numbering correctly.** *(medium; live on RapidAPI Business)*
  - *Intent:* a non-US freelancer (or one line in €) gets a correct quote, not "€: $240.00" summed into a dollar total.
  - *Why:* F1 rewrote `Hosting (12 months): €240` as `"€: $240.00"` and added it to "Total: $6,240.50"; section numbers skip 3 and 4 when optional sections are omitted; `filename …docx` is returned with no file.
  - *Outcome:* `currency` field (default USD) and symbol/ISO parsing per price line; mixed currencies → 400 or a per-currency subtotal with a warning (never a silent sum); contiguous section numbers; either return the .docx/.pdf (shared renderer with B-API-109) or drop `filename`; optional `quoteNumber`, `validUntil` date, deposit %.
  - *Done when:* F1 shows "Hosting (12 months): €240.00" and returns either 400 "mixed currencies" or totals per currency; sections numbered 1–4 + Acceptance; F1 with `currency:"EUR"` prints € throughout.
- **B-API-113 Payment reminder / dunning copy (new route).** *(medium; completes the getting-paid loop)*
  - *Intent:* "write the polite reminder for INV-0042, 7 days overdue, with the late fee" — ready-to-send subject + text + safe HTML.
  - *Why:* no route exists; markdown-to-html is the only HTML path and still emits `javascript:` links (B-API-94). Agents using invoice MCPs (Invovate, Alder) still need the chaser email; this is the step our site's "Freelance Close-Out" bundle implies.
  - *Outcome:* `/v1/business/payment-reminder` (MCP `business_payment_reminder`): `stage` (before-due, due-today, overdue-7/30/60, final-notice), `tone` (friendly/firm), seller/buyer names, invoice number, amount, currency, dueDate, optional lateFee (from B-API-111), `payUrl` (https only, validated); returns `subject`, `text`, `html` (escaped, allow-listed links), `smsText` ≤ 160 chars; no sending, nothing stored.
  - *Done when:* overdue-7 for INV-0042 / €1,090.90 / due 2026-12-01 returns all four fields with the right numbers and date; `payUrl:"javascript:alert(1)"` → 400 unbilled; the html contains no unescaped user input.


## Not changing
No pricing, plan or listing changes are asked here. No AI features are in scope. Listings for the new groups wait until you mark each group READY and our checks pass.
