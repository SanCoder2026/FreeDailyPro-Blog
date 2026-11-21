Sent: 2026-11-20 23:25 ET

# FDP-28 Mortgage Calculator: reproduction steps (guest browser, https://www.freedailypro.com/tool/mortgage-calculator)

1. **P0 privacy:**
   1. Open DevTools › Network ("Preserve log").
   2. Type Home price 487250, Gross monthly income 9137 and Other monthly debts 612.
   3. The address bar becomes `?price=487250&inc=9137&debts=612`.
   4. Scroll; filter by `9137`: a `analytics.google.com/g/collect` request carries the URL.
   5. Reload: `www.freedailypro.com/tool/mortgage-calculator?…`, several `googleads.g.doubleclick.net/pagead/ads` and GA requests carry it.
   6. Compare with Details › Privacy: "Nothing you type is sent to a server or stored." Script: `scripts/mc-privacy.js`.
2. **P1 trial use:**
   1. In a guest context that shows 0 remaining (`localStorage['fdp-usage-v1'].usageToday` = limit), click Download CSV, Copy report, Print or save as PDF, Copy result, Save as text and Print.
   2. All work, no cap dialog, the counter is unchanged.
   3. Repeat in a context with uses left (after 7:00 PM ET reset) to see whether anything is charged.
   4. Script: `scripts/mc-gate.js`.
3. **P1 print:** click "Print or save as PDF" (or Ctrl+P). The preview shows only the donut, "How this was calculated" (collapsed) and Recent calculations; the following pages are blank. The same happens with the amortization schedule open. Script: `scripts/mc-misc.js` (writes `print-preview.pdf`, `print-preview-schedule.pdf`).
4. **P1 video:** play the embedded video or https://www.youtube.com/watch?v=p5KPFr4KYm0 at about 0:20–0:56. Old UI, "10 free uses daily", price 40043 with down payment 80034 → $400.00, then tax 2953 → $3,053.00.
5. **Locales:** open `/es/tool/mortgage-calculator` (and pt, fr, de, ja, hi, zh, ko, id): `<html lang="es">`, all English. `/ar/tool/mortgage-calculator` → 404.
6. **"400.000":** type 400.000 in Home price → Estimated Monthly Payment $102.39, no warning.
7. **15/30 table:** set Loan term 20 → the table still compares 15 vs 30.
8. **CSV:** Download CSV → "Year" rows have an empty Payment date and loan-year numbers; the on-screen yearly table shows calendar years ("2026 (1 payment)"). No tax/insurance columns.
9. **Copy texts:** click Copy report, paste; then Copy result, paste. The texts differ.
10. **Limitations copy:** expand Details → Limitations says tax, insurance and HOA "do not rise over the years". Then enter Property tax increase 3 and see "How the monthly cost changes each year".
11. **iPhone SE:** at 320 px width, horizontal scroll of 9 px (culprit reported by the matrix: a `button.inline-flex…` whose right edge is at 329 px).
