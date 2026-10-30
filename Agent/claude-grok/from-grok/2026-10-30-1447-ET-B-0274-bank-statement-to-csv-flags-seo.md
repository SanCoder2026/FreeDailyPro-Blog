Sent: 2026-10-30 14:47 ET

# B-0274 Bank Statement to CSV: balance check works and catches a bad row; add flags in export, bank presets and statement period checks
Priority: P3 · Estimated effort: M · Report: #149 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:44–14:47 ET. L-243: next 3 untested tools alphabetically after avatar-builder. No GA/GSC rows for these pages in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A bookkeeper should turn a statement into rows they can trust, and know which rows to look at.
## Why (1280 px; 0 trial uses)
- "Trial: 10 uses/day", $1 / $4.99. Drop a text PDF (scans not supported, stated) or paste lines; year, date order and number style (Detect / 1,234.56 / 1.234,56); "Card statement: flip signs".
- Pasted 4 rows with opening/closing balance → editable table (2026-03-01 Coffee Shop −4.50 … Grocery −95.25) and **"Check passed. All 4 running balances follow from the rows."** ✔
- Broke one balance → **"Check: 1 row does not match the printed balance. Check rows 2."** ✔
- Download CSV/Excel open the trial-uses dialog at 0 (owner's decision).
- **Missing vs competitors (~14:46 ET):** carry a Flags column for unsure rows into the export (Tickvouch); check dates run forward and sit inside the statement period (Tickvouch); QuickBooks/Xero export presets (SheetParse, StatementSheet); password-protected PDFs and batch files (StatementRipper); summary sheet in Excel (StatementSheet).
- No overflow at 390 px. Ad text "Hire Accountants"/"Track Investments" stuck to copy → L-004. /es English title → **B-0123**.
## Who uses this
Bookkeepers, freelancers and small-business owners importing into accounting tools.
## Outcomes (ranked)
1. Flags column in CSV/Excel for rows that fail the check.
2. Date-order and period check.
3. QuickBooks/Xero presets.
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD. Title "Bank Statement PDF to CSV or Excel, Checked | FreeDailyPro" (58) ✔. Meta 154 ✔ (ends "Free and fast, right in your browser"). H1 "Bank Statement to CSV".
- **Keywords:** "bank statement pdf to excel", "bank statement to csv", "convert bank statement to excel", "credit card statement to csv".
- **Suggested:**
  - Title: `Bank Statement PDF to CSV or Excel – Checked | FreeDailyPro` (59)
  - Meta: `Turn a text-based bank or card statement PDF into a table, check every running balance against the rows, fix anything, then save it as CSV or Excel.` (148)
  - H1: `Bank Statement PDF to CSV or Excel`
  - FAQ: "Is my statement uploaded?" → "No." · "Does it work with scans?" → "No." · "What does the balance check do?"
## Constraints
Do not upload statements; keep the trial-uses rule.
## Test cases
1. Paste the 4-row sample → "Check passed"; change one balance → "Check rows 2".
2. Admin: CSV columns, sign of amounts, ISO dates; Excel numbers are numeric.
3. Title ≤ 60; meta 140–160.
