Sent: 2026-11-20 23:58 ET

# Live functional findings: loan-calculator (2026-11-20 23:34–23:46 EST, guest, headless Chromium)

## Main calculator (cases.json, cases-extra.json)
- I ran 20 main cases (L01–L20). Every numeric result matches an independent Python amortisation:
  - 100k / 5% / 30 y → $536.82, interest $93,255.78
  - rate 0 → $277.78
  - 60 months → $1,887.12
  - flat 10% / 5 y → $2,500.00, interest $50,000
  - extra $200 → 201 months (Aug 2043), interest $47,708.25
  - INR 5 lakh / 9% / 20 y → ₹4,498.63 (en-IN grouping ₹5,79,671.15)
  - JPY → ¥9,186 (0 decimals)
  - EUR → €495.03
  - car loan 35,000 / 6.9% / 72 mo → $595.04
  - term 0.5 y → $16,910.56
- Validation is visible under the inputs (`loan-error`): "Enter a loan amount greater than 0.", "The term can be at most 100 years." and so on. The workbench says "Fix the loan amount, rate and term above…".
- An extra payment larger than the balance shows a note ("paid off in month 1"). Good.
- **"400.000" → a $400 loan ($2.15/month), no warning** (European thousands separator). P2.
- Term "2.5" months is silently rounded to 3 payments (P3). Switching to flat rate hides the extra-payment input, and the extra is silently dropped (P3).
- The scenario table (no extra / +$100 / +$250, editable) is correct (−104 / −178 months).

## Loan workbench (W01–W19)
- Frequency: monthly $536.82; weekly $123.80 (1,560 payments); biweekly $247.64. Compounding monthly / daily → $247.49 / $247.77. Correct (independent).
- Solve for: rate (600 → 15.4463%, 200 → 3.2192%), amount (600 → $242,283.04), term (600 → 202 payments, 400 → 342). The 400 is rejected only if it doesn't cover interest. Maths correct.
- **P1: default Solve-for result is misleading.**
  - The Target payment defaults to the hard-coded "536.82" (the monthly payment of the default loan), but the shared Payment frequency defaults to **Every 2 weeks**.
  - So opening "Solve for" on the default 100k / 5% loan shows "Interest rate 13.7277%" (W18).
  - After changing the loan to $50,000 it shows 27.9079% (W17); the target does not follow the loan.
  - A user checking "what rate am I paying?" gets a wrong-looking answer.
- Fees and APR: fee $2,000 → APR 5.1784%; $300 → 5.0264%; fee ≥ amount → error. The value equals the nominal APR (periodic rate × 26), but the label says **"APR (effective annual cost)"**; the effective annual rate would be 5.31% (P2 label).
- Deferred and zero-coupon: 100k at 5% annual for 30 y → $432,194.24 due; zero-coupon price $23,137.74. Correct.
- Compare two loans: Loan B 4.5% / 15 y → $764.99, interest $37,698.79; with a $3,000 fee, APR 4.959%. Correct.

## Exports / trial uses (gate.json, 23:42–23:43 EST)
- All 6 fresh contexts loaded at 0 remaining (`usageToday` 10 of 10, day key 2026-11-21, display-only).
- At 0, all 9 actions worked with no cap dialog; the counter stayed 10 → 10, also after reload:
  - Main bar: Download CSV `loan-schedule.csv`, Copy report, Print or save as PDF.
  - Workbench bar: Download CSV `loan-freq.csv`, Copy result, Print or save as PDF.
  - Result actions: Copy result, Save as text `loan-calculator-result.txt`, Print.
- No trial strip, pass or Quick Buy on the page.
- A context with uses left could not be observed → **RERUN-AFTER-RESET row 29**. **Policy question for Santosh**: this tool is not in the Nov 20 uncounted list.
- Exports:
  - "Copy result" / "Save as text" start with the first-payment-date help paragraph and omit the loan amount, rate and term (only the totals) (P2).
  - "Copy report" includes inputs and steps.
  - The CSVs have no input header (P2).
  - Three export bars plus result actions, with two "Copy result" buttons that copy different things (P2).

## Print (misc.json, print-preview.pdf, 6 pages)
- Page 1 starts with "Loan workbench" overlapping "How this was calculated". It prints the workbench select controls; two balance-chart lines overlap the scenario table.
- **The main result (Monthly Payment, inputs, Total, Interest, Payoff) is not printed.**
- Pages 2–6 hold a schedule with a garbled duplicated header ("Payment Payment Date date…"). **P1.**

## Privacy (privacy.json, 23:40 EST)
- Typed amount 48725, rate 7.37 and extra 613 → `?amt=48725&rate=7.37&xm=613`.
- Without any reload: GA `/g/collect` carried the URL.
- On reload or a shared link it also went to the server GET, 5 × googleads.g.doubleclick.net/pagead/ads, 3 × pagead2.googlesyndication.com/pagead/ping (body) and GA.
- Copy: "nothing about the loan amount, rate, or term you enter is transmitted or stored anywhere"; "Nothing is saved on our servers or in your browser". **P0.**

## Share / storage (share.json)
- Share copies the URL; currency, amount, rate, term and extra round-trip (INR ₹16,120.43).
- Workbench state (tab, fee) is not shared (P3).
- Favorites go to localStorage. History is in memory and also logs workbench results automatically.
