Sent: 2026-10-31 00:23 ET

# B-0314 Expense Tracker: entries vanish on tab close, no receipt image, recurring entries, date filter or chart; event wording on a business tool
Priority: P2 · Estimated effort: M · Report: QA-REPORT-171 · Source: live probe 2026-10-31 ~00:17-00:23 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A freelancer or small business keeps a running expense log they can come back to all month and hand to their bookkeeper at tax time.

## Why
No GSC row for this page in the analytics raw files (checked).
Checked live: Cost 100 at 10% tax (not included) → $110.00 ✔; Cost 100 at 10% included → $100.00 ✔; Income 500 → +$500.00, category "Sales" ✔; Costs $210.00, Income $500.00, Net $290.00 ✔; "Costs by category" ✔; Budget 150 → "Over Budget By $60.00 … $210.00 spent of your $150.00 budget" ✔; empty amount → "Enter an amount." ✔; Export as CSV and Delete all my data appear after the first entry ✔. 24 currencies, relabel only (stated) ✔. 390 px no overflow ✔.
Persistence: "erased when you close the tab" (page and FAQ). Competitors keep data across visits (local storage) by default.
Wording: this business tool shows "Project: My event" and a warning about a pass key that "signs the QR codes on guest passes" (checked). That copy belongs to the event suite and confuses a freelancer.
Capability (checked on the controls list): no receipt image attach, no recurring entry, no date-range or month filter, no chart, no Excel/PDF export (CSV only), no mileage.
Competitors (live search): TrackMyExpense (receipt OCR, recurring bills, budgets, reports, PDF/Excel/CSV), Scanomy (receipt AI, charts, filters, CSV/Excel/PDF), Receeto (offline on-device receipt scan, monthly budgets, CSV or ZIP with receipt images), Awesome Receipts (subtotal/tax/tip split, project codes, image kept with record).
Unnamed amount and vendor inputs (checked) → B-0155. No shared done state after Add → B-0187.

## Who uses this
Freelancers, sole traders and households tracking spend.

## Outcomes (ranked, demand × effort)
1. Keep entries on this device between visits (local storage, opt-out "Delete all my data" already exists) (S).
2. Neutral project wording on this page ("My expenses"), and show the pass-key warning only on tools that make passes (S).
3. Attach a receipt photo or PDF per entry; export ZIP of CSV + receipts (M).
4. Month / date-range filter and a by-category chart; Excel and PDF export (M).
5. Recurring entries (monthly rent, subscriptions) (M).

## SEO
- Now: title "Track Business Expenses Online - Expense Tracker | FreeDailyPro" (63); meta 37 "Track and categorize expenses simply." (too short); H1 "Expense Tracker"; JSON-LD SoftwareApplication, FAQPage (6 Q), BreadcrumbList, VideoObject ✔; canonical ✔
- Keywords: expense tracker, business expense tracker, expense tracker online, track expenses, expense log template
- Suggested Title: "Expense Tracker: Log Costs, Income and Tax | FreeDailyPro" (57)
- Suggested Meta: "Log business or personal expenses and income by category with tax, vendor and budget left, then export a CSV for your bookkeeper." (129)
- Suggested H1: keep
- FAQ: keep; add: Can I attach receipts? · Can I see spending by month?

## Constraints
Exports count against the trial (owner rule). Keep "nothing uploaded".

## Test cases
1. Add 3 entries, close and reopen the tab → entries still there; Delete all my data clears them.
2. Logged out on this page → no "My event" or guest-pass wording.
3. Attach a JPG to an entry → thumbnail; ZIP export has CSV + image.
4. Filter October → only October rows and totals.
5. Recurring monthly $50 from Aug 1 → rows for Aug, Sep, Oct.
