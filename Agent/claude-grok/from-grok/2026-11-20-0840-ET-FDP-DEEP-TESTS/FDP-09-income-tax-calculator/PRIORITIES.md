Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: priorities

- **Written:** 2026-11-19 13:21:55 EST (box `date`, ET).
- Each item points to a repro in REPRODUCE.md (R-n) and to test cases in test-cases.md.

## P0
1. **The trial cost of Copy / Save / Print / Ctrl+C contradicts the Terms and FAQ, and blocks guests at 0** (R-1; IT-30…IT-36).
   - /terms says calculators "take no trial use at all", and the FAQ says tax calculators "never use a trial use".
   - The tool charges 1 per visit and blocks all four at 0, including Ctrl+C of a visible number.
   - 13 of 15 fresh contexts loaded at 0 (display-only; shared trial-meter P0 from FDP-02 to FDP-08).
   - **Fix:** one rule everywhere. Never intercept a plain text copy.

## P1
2. **Self-employed QBI cliff** (R-2; IT-12…IT-17). QBI drops to $0 above the 24%-bracket top (201,775 / 403,550) instead of phasing in over $75k / $150k from 201,750 / 403,500.
   - At $240k profit (single), federal tax is $43,415 vs $33,082.
   - Take-home falls by $4,437 from $232k to $240k profit.
3. **Local income taxes silently omitted** (R-3; IT-20, IT-21). Maryland county tax (2.25–3.30%, about $2,510 at $85k) applies to every resident, and NYC/IN/OH/PA/MI/KY local taxes exist too.
   - `localNote` and `localAvg` are in the data but never used.
   - The page gives no warning.
4. **Head of household uses single state brackets and the single standard deduction** (R-4; IT-22). CA HoH $85k shows $3,660 instead of about $1,636 (FTB 2025 Schedule Z, std $11,412).

## P2
5. **PA:** the 401(k) reduces state tax ($307 at $85k with 10k deferral). PA taxes deferrals. (IT-23)
6. **No 65+ extra standard deduction or 2025–2028 senior deduction.** The only age select is for the 401(k). Add it, or name it in the disclaimer. (IT-26)
7. **"Effective rate" includes FICA** without saying so. (IT-27)
8. **Custom Flat Rate accepts 150% and −5%**, showing "$-50,000". The currency select has no label. (IT-40, IT-41)
9. **The blog** `/blog/estimate-us-self-employment-tax-2026` says the tool doesn't model QBI, but it does.
10. **The video** UvcrEE6Swwc shows the old UI, "free" wording and older figures, plus the recorder's personal bookmarks bar. Re-record it. The sitemap video title says "Online Free".
11. **Locales:** the es title says "gratis". pt, fr, de, ja, hi, zh, ko and id are English-only with a shorter H1. The Offer has no billing period.
12. **Layout and a11y:**
    - iPhone SE overflows (353 > 320 px).
    - The income field is below the first screen on small phones.
    - There is no aria-live on the result.
    - Header label-content-name-mismatch; the ad-label contrast is low.
13. **QBI details:** thresholds are off by $25 / $50, and the $400 minimum is missing.

## Re-run after midnight UTC (7:00 PM ET)
- Does Save as text or Print, as the **first** action of a visit with uses left, cost 1 use? (IT-34, IT-35; `scripts/it-gate4.js`; RERUN row #9)
