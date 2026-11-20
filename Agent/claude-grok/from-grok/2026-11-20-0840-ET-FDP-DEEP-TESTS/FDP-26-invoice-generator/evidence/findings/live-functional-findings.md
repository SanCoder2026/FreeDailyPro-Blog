Sent: 2026-11-20 08:40 ET

# FDP-26 Invoice Generator: live functional findings (Chromium unless noted; box times ET)

Starting counts: most fresh contexts load at 2/2 used ("0 remaining today", e.g. 18:43:08 EST); about 1 in 7 loads with 2 left (18:48, 18:49, 18:50, 18:53, 18:54 EST). Counters are display-only evidence. Trial uses spent by this test: 6 (A 1, B 2, C 1, D 1, WebKit 1).

## Calculations (Total box, no trial use) — `json/ui-AB.log` / `json/ui.json`
All 12 scenarios match hand calculations: sample $1,754.46 / balance $1,654.46; three tax rates with 10% discount $243.44; credit line $70.00; credit larger than work −$33.00; EU decimals "1,5" × "1.234,56" = 1,851.84; ¥100.4 × 2 → ¥201; paid > total → balance −$50.00; discount 150% → $0.00 (capped); late fee 1.5% + $25 after 10 days → "(2026-12-29) … $40.00"; 3 × 0.335 → $1.01; ₹1,180.00; CA$1,234,567.89.
- **P2:** "1.500" is read as 1.50 (S5 total $3,053.84 instead of $4,552.34 if 1.500 meant 1,500) while "1,500" is 1500.
- **P3:** when credits make the total negative, the Total box (and PDF) show "−$33.00" with no subtotal/tax line (negative tax hidden by `tax > 0` checks).

## Validation (Generate pressed at the cap — validation runs first, no use)
Clear, field-level messages with aria-describedby: missing business/client ("Please fix 3 things… The first is marked", focus to Business name), qty 0 ("…For a refund or credit, tick Credit instead"), negative price, "ten", empty description, due date before invoice date, `javascript:alert(1)` and `www.pay.me` pay links ("must start with https://"), late fee 150%, line tax 120%.
- **P3:** for line-item errors focus does not move to the marked field (`focused: null`); "Please fix 2 things" for an empty description shows one message.

## Outputs (trial uses spent; files in `testfiles/outputs/`)
- **A — rich invoice, PDF (18:48:29 EST, 0 → 1):** INR, GSTIN, logo, Hindi/German client name, 3 GST rates, credit line, 10% discount, shipping, deposit, late fee, pay link + QR, approval line, 80-char unbroken word. 2 pages, Letter. Every number correct (₹15,500.00 / −₹1,550.00 / GST 5% ₹40.50 / GST 18% ₹1,879.20 / ₹50 / Total ₹15,919.70 / paid / Balance ₹15,819.70; late fee ₹262.30). Hindi drawn correctly as pictures (Chromium and WebKit identical), logo and QR embedded, long word wrapped, "Created with FreeDailyPro.com" badge on each page (intentional), emoji drawn although the toast warned it may not show.
  - **P2 – mixed-script notes reordered:** notes "धन्यवाद! Bank: HDFC 0001 · IFSC HDFC0000001 · شكرا · Ευχαριστώ · 🎉" print as "… IFSC HDFC · شكرا · 0000001Ευχαριστώ" — the digits of the bank code are moved past the Arabic word (same in WebKit; `screens/live/notes-bidi.png`). Arabic + numbers on their own lines (C) print correctly.
- **A — Word right after (0 → 1 → 1, free):** file INV-002.docx for the same invoice — **P1, number mismatch**. Content otherwise complete (tables, Hindi text as text, QR + logo, late fee, approval line).
- **B — Excel (18:49:40 EST, 0 → 1):** live formulas (`=B17*C17`, `SUM`, discount `ROUND`, one GST row via `SUMPRODUCT`), values match the PDF for this invoice; shipping/paid as constants; no per-rate breakdown (P3).
- **B — after reload, 23 lines / 4 tax rates, A4 PDF (1 → 2):** totals correct, but **"Page 1 of 2" is printed over the Balance due amount "$471.55"** (`screens/live/balance-overlap.png`) — **P1**. Number was INV-002 (sessionStorage kept the next number across the reload).
- **C — AED with Arabic line item and notes (0 → 1), then the same invoice again (1 → 1, INV-002) and Excel (1 → 1, INV-003):** Arabic description and notes correct; IBAN/IFSC/phone intact.
- **D — Save profile (18:53:37 EST, 0 → 1):** saving the local profile file costs a trial use; the next PDF in the same visit was free; a second Save was free and holds `numbering.invoice` + `lastInvoice` + 4 clients. "Duplicate last invoice" appeared.

## Usage (policy question for Santosh — not a PASS)
- One trial use per page visit unlocks every later download in that visit: PDF + Word, or PDF + PDF + Excel, each with a new invoice number, and Save profile. A reload makes the next one cost again. Owner policy (Oct 30): results count.
- **P2:** at the cap, "Save profile" opens the trial-cap dialog ("downloading needs a pass"), yet each download toast says "Save your profile to keep it"; a user who spent today's uses on invoices cannot save the file that holds their next number and clients.

## Gate at 0 remaining (`json/ui2.json`)
PDF / Word / Excel each → "You've used today's trial uses … Premium Applications, Monthly $9.99, Day Pass $3 … removes the 'Created with FreeDailyPro.com' mark" → Buy Day Pass → "Premium Day Pass, $3 | Enter your email…" (stopped; nothing typed). Form kept.

## Profile & clients
Bad JSON → "That isn't a business profile (it isn't valid JSON)."; CSV import: 4 imported, 1 nameless row skipped, `=HYPERLINK(...)` and `<img onerror>` names shown as plain text (no script ran); junk file → "needs a header row (name, address, email, tax id)". Save profile disabled until a name exists.

## Privacy
Generate makes only `usage.log` (POST 123 B), `usage.check`, `insight.hit` (162 B); no typed text in any request (checked for names, items, bank text). Fonts load from the site. Claims hold.

## Accessibility / keyboard
Tab order follows the form; axe on `main`: only ad-label contrast (site-wide); matrix axe: label-content-name-mismatch, region. Phones: Pixel 7 clean; iPhone SE 9 px overflow (site-wide header).
