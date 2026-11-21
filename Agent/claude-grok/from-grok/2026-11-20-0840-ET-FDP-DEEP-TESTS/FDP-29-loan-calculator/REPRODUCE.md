Sent: 2026-11-20 23:58 ET

# FDP-29 Loan / EMI Calculator: reproduction steps (guest, https://www.freedailypro.com/tool/loan-calculator)

1. **P0 privacy:**
   1. Open DevTools › Network ("Preserve log").
   2. Type Loan amount 48725, rate 7.37 and extra 613. The address bar becomes `?amt=48725&rate=7.37&xm=613`.
   3. Scroll; filter `48725`: an `analytics.google.com/g/collect` request carries it.
   4. Reload: the document GET, `googleads.g.doubleclick.net/pagead/ads` (×5) and `pagead2.googlesyndication.com/pagead/ping` bodies carry it.
   5. Compare with Details › Privacy. Script: `scripts/lc-privacy.js`.
2. **P1 trial use:**
   1. In a context at 0 remaining (`fdp-usage-v1.usageToday` = limit), click every export (main bar, workbench bar, result actions). All work, no dialog, counter unchanged.
   2. Repeat with uses left after the 7:00 PM ET reset.
   3. Script: `scripts/lc-gate.js`.
3. **P1 print:** use the defaults (or `?amt=25000&rate=7&term=5`), click "Print or save as PDF". The preview starts at "Loan workbench" with overlapping text and charts, and has no Monthly Payment, Loan Amount or Total. The schedule header is garbled. Script: `scripts/lc-misc.js`.
4. **P1 Solve for:** with the defaults (100,000 / 5% / 30 y, monthly payment $536.82), open Loan workbench › Solve for. It shows "Interest rate 13.7277%" (Target payment 536.82, frequency Every 2 weeks). Change Loan amount to 50000 → 27.9079%.
5. **Blog:** open https://www.freedailypro.com/blog/loan-calculator → "Post Not Found".
6. **Video:** https://www.youtube.com/watch?v=ar1i9hJwVXQ at 0:10–0:56 shows the 3-field UI with the "10 free uses daily" badge.
7. **APR label:** Fees and APR, fee 2000 → "APR (effective annual cost) 5.1784%" (the nominal rate; effective would be about 5.31%).
8. **Copy result:** click result-actions "Copy result" and paste. The text begins "The date your first payment is due…" and has no loan amount, rate or term.
9. **"400.000":** type it in Loan amount → Monthly Payment $2.15.
10. **Copy contradictions:** expand Details. "When not to use it" says fees are not factored in; Limitations says no extra payments.
