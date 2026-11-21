Sent: 2026-11-20 23:25 ET

# Live functional findings: mortgage-calculator (2026-11-20 23:02–23:20 EST, guest, headless Chromium)

## Engine (cases.json, cases-blog.json)
- Ran 44 UI cases (M01–M44) plus 4 blog cases (B01–B04). I checked every total against an independent Python amortisation: 23/23 numeric totals match to the cent. The others are validation cases, and each showed the expected message.
- Conventional PMI: 10% down → $180.00 for 109 months; 5% → $190.00 for 135 months (independent: 109 / 135). It ends at 78% of the price.
- FHA: 3.5% down → upfront 1.75% financed and MIP 0.55% for the life of the loan ($176.92). 10% down on 15 years → 0.15% for 11 years ($45.00). Below 3.5% down → "FHA needs at least 3.5% down." These match the published HUD table (desk).
- VA: 0% first use 2.15% ($8,600); subsequent use 3.3%; 10% down 1.25%. USDA: 1% upfront and 0.35% a year for the life of the loan. Matches published 2026 rates (desk).
- Extras:
  - $200 extra a month → 6 y 7 m sooner, $105,429 less interest.
  - $10,000 one-time payment at month 12 → 2 y 5 m sooner, $50,537 less.
  - $5,000 a year → 10 y 7 m sooner, $162,649 less.
  - Biweekly → 628 payments, $93,996.57 saved.
  - All four are identical to the independent calculation.
- DTI: income 10,000 + debts 500 → 24.9% / 29.9% "Within 28/36". Income 6,000 → 41.5% "Above". Maintenance is excluded from the ratios, as stated.
- Input parsing: "$400,000" and "100,000" work. "6,5" → 6.5. **"400.000" → a $400 home, with a $102.39 payment and no warning** (European thousands separator). P2.
- Validation messages are clear for price 0/abc, down ≥ price, rate 101/−1, term 0/51, closing 25, growth 30, month 0, and a date before 1990.
- Term 20 → the "15-year vs 30-year" table still shows only 15 and 30, not the user's own term (P2).
- The total is the unrounded sum: $2,489.28, while the shown parts add up to $2,489.29 (P3 cosmetic).

## Exports / trial uses (gate.json, 23:06–23:07 EST)
- All 6 fresh contexts loaded at 0 remaining (`usageToday` 10 of 10, day key 2026-11-21, display-only).
- In the 0-remaining context, all 6 actions worked with no cap dialog, and the counter stayed 10 → 10 (also after reload):
  - Download CSV → mortgage-schedule.csv, 391 lines.
  - Copy report → "Report copied".
  - Print or save as PDF → print called.
  - Copy result → "Result copied".
  - Save as text → mortgage-calculator-result.txt.
  - Print.
- There is no trial strip, pass or Quick Buy on the page (misc.json).
- A context with uses left could not be observed → **RERUN-AFTER-RESET row 28**.
- **Policy question for Santosh:** BMI showed the same pattern on Nov 20 (0 → 0 with 10 left). Mortgage is not in the Nov 20 uncounted list.
- CSV: yearly rows have an empty "Payment date" and use loan years. The on-screen yearly table uses calendar years ("2026 (1 payment)"). There are no tax, insurance or HOA columns, and no input summary (P2).
- Copy result (lacks rate/term inputs except in the history line) and Copy report (has the worked steps) differ; two export bars with overlapping buttons (P2).

## Print (misc.json, print-preview*.pdf)
- Print media renders 4 A4 pages: page 1 holds only the donut, a collapsed "How this was calculated" and Recent calculations with a Clear link; pages 2–4 are blank.
- Missing from the print: the inputs, loan amount, total interest, cash to close, payoff, the 15/30 table and the amortization schedule (also when the schedule is open). **P1.**

## Privacy (privacy.json, 23:05 EST)
- The page URL mirrors non-default inputs, including **gross monthly income and other monthly debts** (`?price=487250&inc=9137&debts=612`).
- Without any reload: a Google Analytics `/g/collect` carried that URL.
- On reload or a shared link, it also went to the server GET and to 5 × googleads.g.doubleclick.net/pagead/ads, plus GA again.
- The copy says: "Nothing you type is sent to a server or stored" (Details › Privacy) and "Nothing is saved on our servers or in your browser" (history). **P0.**

## Share / storage (share.json)
- Share copies the current URL (the FHA type, down payment and extra payment round-trip). The biweekly checkbox is not in the URL (P3).
- Favorites go to localStorage `freedailypro-favorites`. History stays in memory only (no Storage calls in history/CalcHistory chunks).
