Sent: 2026-11-20 22:15 ET

# FDP-26 Invoice Generator (invoice-generator): deep test report for Claude

- **Written:** 2026-11-20 22:11:25 EST (box `date`, ET). Testing ran 2026-11-19 18:42–18:56 EST (cut off before packaging when usage ran out) and the money paths were re-run after the trial reset on 2026-11-20 22:06–22:09 EST.
- **Tool:** https://www.freedailypro.com/tool/invoice-generator. Row 26 of TEST-ORDER.md: Premium, Business & Documents, test-plan rank 21 ("API returns totals only, no PDF (false title)" — the API was not tested: no API/MCP testing), duplicate group C32. **GSC data is not available.**
- **Classification:** Premium Application (2 trial uses a day, $3 Day Pass / $9.99 month). No on-page preview: the only result is the downloaded PDF / Word / Excel, so the gate is at generate — not flagged. Trial PDFs carry the intentional "Created with FreeDailyPro.com" badge.
- **Site changed overnight:** the Nov 20 build renamed `InvoiceGenerator` (`-6vPLHGvC` → `-CcQb7dIX`), `ProfileBar`, `invoiceAssets`, `logoFile`; a prettified diff shows only import/chunk-name changes. All P1s were re-verified live on Nov 20.
- **Testers:**
  - **Desk review:** page (expanded), JSON-LD, /es, /ar, /blog/invoice-generator, /category/business-tools; `InvoiceGenerator`, `invoiceCalc`, `invoiceAssets`, `numberInput`, `money`, `pdfText`/`pdfFonts`, `ProfileBar`.
  - **YouTube video:** metadata + 34 frames.
  - **Headless Playwright:** 12 calculation scenarios (live Total box vs hand maths), 10 validation cases, rich multi-script INR invoice → PDF + Word (Chromium, WebKit, Firefox), Excel, 23-line / 4-rate A4 PDF, AED/Arabic invoice ×2 + Excel, Save/Load profile, client CSV import (formula/HTML rows), gate and dialogs, privacy, keyboard, axe, phones, matrix (10 profiles, 10 locales + /ar, 6 geos, axe). Outputs parsed with pdftotext/pdfinfo, python-docx, openpyxl and rendered; never executed.
- **Starting counts:** Nov 19 most fresh contexts loaded at 2/2 used (e.g. 18:43:08 EST), about 1 in 7 with 2 left; Nov 20 after the reset fresh contexts loaded with 2 left (22:06:49 EST). Counters are display-only evidence. Trial uses spent: 6 on Nov 19 + 4 on Nov 20.
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts, no ad clicks, no API/MCP, no site/repo changes.
- **Sign-in:** none required by the tool (profile is a local file). Day Pass stops at the email prompt. See INSTRUCTIONS.md.
- **Pending:** none. No RERUN-AFTER-RESET row needed (the Nov 19 gaps were re-run on Nov 20).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships its Premium Applications.

Code to look at (`evidence/js/InvoiceGenerator-CcQb7dIX.pretty.js`):
- PDF layout: totals rows `N(...)` up to L300 (no page-break check after the single 110 pt reserve) and the footer `Page ${h + 1} of ${q.length}` at L356.
- Download flow `be` from L731: the invoice number is advanced after every file (toast at L797), so PDF then Word of one invoice get different numbers.
- `numberInput-5hjoxJ5z.pretty.js`: "1.500" → 1.5 while "1,500" → 1500.
- Notes drawing in `pdfText`/`pdfFonts`: mixed RTL + digits runs are reordered.
- The shared download gate: one charge unlocks every later download in the same visit.

After you ship, rerun `scripts/ig-spend.js A`, `B`, `C` (set OUTDIR; `PWB=firefox|webkit` for other engines), `ig-ui.js`, `ig-profile.js`, then `test-cases.md` (IG-01…IG-22).

## Intent

A freelancer or small business owner needs to bill a client today: a correct, professional invoice in their currency and language, with tax lines, a pay link and their own number sequence, sent as a PDF (or Word/Excel for their accountant). They need every number on it to be right and readable, and the invoice number to match across the files they send, because a client or tax office will query any mismatch. They need to trust their client data never leaves their device. They should leave impressed and see Premium as worth $3 / $9.99.

The engine is strong: all 12 calculation scenarios exact (discounts, multi-rate tax, credits, paid > total, rounding, ₹/¥/AED/CA$), clear field-level validation, Hindi and Arabic drawn correctly, logo and pay-link QR embedded, late-fee wording, Word and Excel with live formulas, client CSV import that treats formulas/HTML as text, a local profile file, nothing uploaded, and identical PDFs in Chromium, Firefox and WebKit.

Trust is lost on longer invoices, where the page footer prints over the Balance due amount, and when someone downloads the PDF and the Word copy and gets two different invoice numbers for one bill.

## Why: what the evidence says

- **P1: "Page 1 of 2" is printed over the Balance due amount** on a 23-line / 4-rate A4 invoice ("$471.55"), Nov 19 and again Nov 20 22:08 EST. Totals rows never check for a page break; more tax rates push rows off the page (code-derived). (`screens/live/balance-overlap-1120.png`, `testfiles/outputs/2026-11-20/B-pdf-long-INV-002.pdf`)
- **P1: One invoice, two numbers.** PDF → INV-001.pdf, then Word of the same invoice → INV-002.docx (toast "Next number: INV-003"); Excel would be INV-003. Re-verified Nov 20 22:08 EST. (`json/spend-1120/spend-A.json`)
- **P1: Video misleads on price and features.** 9XjEtjnQ9YY (Oct 1, 102 s) says "free" four times ("Create professional invoices free online", "Free daily uses … no account needed") for a Premium Application and shows an old form without profile, tax, currency, discount, late fee, pay link or Word/Excel. (`findings/video-findings.md`)
- **P1 — policy question for Santosh (not a PASS):** one trial use per page visit unlocks every later download in that visit (PDF + Word; PDF + PDF + Excel; Save profile), each with a new invoice number; a reload charges again (Nov 20: Excel 0 → 1, reload, PDF 1 → 2). Owner policy (Oct 30): results count.
- **P2:** mixed-script notes are reordered in all three engines ("IFSC HDFC0000001 · شكرا" → "IFSC HDFC · شكرا · 0000001Ευχαριστώ" — a bank code broken on a payment instruction); "1.500" is read as 1.50 (EU users typing 1.500 for 1,500); at the cap "Save profile" opens the cap dialog while every download toast says "Save your profile to keep it".
- **P3:** Excel single tax row vs PDF per-rate rounding (2.31 vs 2.32, code-derived); FAQ "discount above 100 is treated as 100" vs validator error; emoji toast says it may not show but it's drawn; tax column header always "Tax"; negative totals hide subtotal/tax lines; focus doesn't move to a bad line item; locale titles English; currency default ignores locale; iPhone SE 9 px overflow (site-wide).

## Outcomes we want

1. Every invoice, however many lines and tax rates, prints its totals and Balance due cleanly, with the page footer never touching them.
2. The PDF, Word and Excel of one invoice carry the same number; the sequence moves on only when the user starts a new invoice.
3. The video and its description match today's Premium tool and pricing.
4. Trial counting follows Santosh's decision on the per-visit unlock.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | Calculations exact; footer over Balance due on long invoices; notes bidi reorder. `findings/live-functional-findings.md` |
| 2 | Completeness | **PASS** | LOW | PDF/Word/Excel, multi-rate tax, discount, credit, shipping, paid, late fee, pay link + QR, logo, profile, clients CSV, paper size. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Excellent validation; number jumps between formats; no preview; "1.500" parsing; Save profile blocked at cap. |
| 4 | Layout | **PASS** | LOW | 10 profiles 200; iPhone SE 9 px (site-wide header); ja desktop 3 px. |
| 5 | Payment process | **PASS** | — | At 0: PDF/Word/Excel → "You've used today's trial uses" ($9.99 / $3) → Buy Day Pass → "Premium Day Pass, $3 | Enter your email…" (stopped). Form kept. Re-verified Nov 20. |
| 6 | Information correct | **PARTIAL** | MEDIUM | Discount >100 FAQ vs validator; emoji toast; "Save your profile" at cap. Privacy claim verified. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, 10 hreflang. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Good title/H1/FAQPage/VideoObject; locale titles English; /ar 404 (not in hreflang). |
| 9 | Blog | **PASS** | — | /blog/invoice-generator 200, linked under Guides; tools.csv: 25 posts link here. |
| 10 | YouTube video | **PASS (low reach)** | LOW | Embedded; 102 s, 3 views. |
| 11 | FAQ / guide | **PARTIAL** | LOW | Thorough; two claims contradict behaviour. |
| 12 | Video shows current tool | **FAIL** | HIGH | Old UI, "free" ×4 for a Premium Application. `findings/video-findings.md` |
| 13 | Storage | **N/A** | — | Profile saved as a local `.fdp-profile.json`; no Drive/cloud (live-verified). |
| 14 | Sharing | **N/A** | — | No share/copy/print on the result (live-verified) although tools.csv lists them. |
| 15 | Downloads | **PARTIAL** | HIGH | PDF/Word/Excel correct and match memory; badge intentional; footer overlap; number mismatch. |
| 16 | Usage count | **POLICY QUESTION** | HIGH | 1st file 0 → 1; later files in the visit free (new numbers); reload → charged. Counter display-only evidence. |
| 17 | Category placement | **PASS** | — | Business & Documents. |
| 18 | Site section | **PASS** | — | Premium Applications. |
| 19 | AI need / demand | **PASS** | — | Test-plan rank 21. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Core of C32; receipt/quote/PO share the engine (`tradeDoc`) — keep separate entry points, cross-link. |
| 21 | Remove? | **N/A (keep)** | — | Flagship Premium Application. |
| 22 | Duplicates | **PARTIAL** | LOW | C32: receipt, quote, PO, packing slip, pay stub, timesheet, AI invoice extractor, Freelancer Desk — make the ladder explicit on the page. |
