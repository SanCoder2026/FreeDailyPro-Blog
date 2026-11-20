Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: how to reproduce

- **Setup:** a guest, fresh profile, https://www.freedailypro.com/tool/state-tax-calculator.
- Scripts are in `scripts/`. Counters are display-only.

## R-1: HoH = single (P1)
1. Income 75000, California, **Single**: $2,774.57.
2. Switch to **Head of household**: still $2,774.57.
3. Expected (FTB 2025 Schedule Z, std $11,412): taxable 63,588 → $828.87 + 4% × 11,058 = $1,271.19 − $153 = **$1,118.19**.
4. North Carolina HoH $75k: $2,483.78 (= single). Expected (75,000 − 19,125) × 3.99% = **$2,229.41**.
5. Script: `node scripts/st-live.js S01_CA_single_75k,S02_CA_hoh_75k,S27_NC_hoh_75k,S28_NC_single_75k,S04_NY_single_85k,S05_NY_hoh_85k`.

## R-2: Utah (P1)
1. Income 75000, Utah, Single: **$2,621.05** (= 4.45% × 58,900).
2. Expected (2026 TC-40): 4.45% × 75,000 = 3,337.50. The credit is 6% × 16,100 = 966, minus 1.3% × (75,000 − 18,696) = 731.95, so 234.05. Tax = **$3,103.45**.
3. Script: `node scripts/st-compare.js 75000 single` (Utah row).

## R-3: silent $0 (P1)
Type `85k` (or `abc`) as income. The result is "$0.00" with no message (`evidence/screens/live/input-85k-shows-zero.png`). Compare: the Income Tax Calculator shows "Enter an income as a number".

## R-4: video (P1)
Play the embedded video (uRiqzi4ARPY) at about 0:22 (frame f008). It shows "Estimated State Tax $9975.00 at 13.3% (top marginal rate)" for $75,000 California. The live tool gives $2,774.57.

## R-5: trial wording (P1, wording only)
- /terms: "Text utilities, calculators and simple converters take no trial use at all."
- Tool, with 10 left: Download CSV → 9 left. Other exports on the same visit cost nothing.
- At 0: all six exports open the cap dialog.
- Script: `node scripts/st-gate.js`.

## R-6: notice with a city (P2)
New York, then City or county = New York City. The NYC line is added ($2,859.69 at $85k), but the notice reads "State tax only: local income tax is not included, so your total is likely higher."
