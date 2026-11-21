Sent: 2026-11-20 23:25 ET

# FDP-28 Mortgage Calculator: test cases

- **URL:** https://www.freedailypro.com/tool/mortgage-calculator, guest.
- **Defaults:** Conventional, $400,000, 20% down, 6.5%, 30 y, tax 1.1%/yr, insurance $100, HOA 0, PMI 0.6%, closing 3%.
- **"Live"** = 2026-11-20 23:03–23:20 EST.
- **Scripts:** `scripts/mc-live.js` (M*/B* ids), `mc-gate.js`, `mc-privacy.js`, `mc-misc.js`, `mc-share.js`.
- **Expected values** come from an independent amortisation (P&I = L·i/(1−(1+i)^−n)).
- "Currently: FAIL" rows should pass once the fix ships.

## A. Calculation
| ID | Input (changes from default) | Expected | Live |
|---|---|---|---|
| MC-01 | default (M01) | Total $2,489.28 (P&I $2,022.62 + tax $366.67 + ins $100); loan $320,000; interest $408,142.36; cash to close $92,000; payoff Nov 2056 | PASS |
| MC-02 | down 10% (M02) | $2,922.11; PMI $180.00 for about 109 months | PASS |
| MC-03 | down $ 100,000 (M03) | $2,362.87 | PASS |
| MC-04 | rate 0 (M04) | $1,355.56 | PASS |
| MC-05 | term 15 (M05) | $3,254.21 | PASS |
| MC-06 | FHA 3.5% (M06) | $3,126.06; MIP $176.92, life of loan | PASS |
| MC-07 | FHA 3% (M07) | "FHA needs at least 3.5% down." | PASS |
| MC-08 | VA 0% first / subsequent / 10% (M08–M10) | $3,049.30 / $3,078.37 / $2,770.55 | PASS |
| MC-09 | USDA 0% (M11) | $3,136.89; annual fee $116.67, life of loan | PASS |
| MC-10 | tax $6000/yr; tax $400/mo + HOA 250 (M12, M13) | $2,622.62; $2,772.62 | PASS |
| MC-11 | extra $200/mo (M14) | 6 y 7 m sooner, $105,429 less interest, payoff Apr 2050 | PASS |
| MC-12 | one-time $10,000 at month 12 (M15) | 2 y 5 m sooner, $50,537 less; "Payment #12 is due Nov 1, 2027" | PASS |
| MC-13 | yearly $5,000 (M16) | 10 y 7 m sooner, $162,649 less | PASS |
| MC-14 | income 10000 + debts 500 (M17) | 24.9% / 29.9%, "Within 28/36" | PASS |
| MC-15 | income 6000 (M18) | 41.5% / 41.5%, "Above both" | PASS |
| MC-16 | biweekly on (M19) | 628 payments, payoff Dec 13, 2050, $93,996.57 saved | PASS |
| MC-17 | first payment 2027-03-15 (M20) | Last payment Feb 15, 2057 | PASS |
| MC-18 | price 0 / abc; down ≥ price; rate 101 / −1; term 0 / 51; closing 25; growth 30; one-time month 0 (M21–M28, M39, M43) | The matching validation message, no total | PASS |
| MC-19 | income "abc" (M29) | Income message; payment still shown | PASS |
| MC-20 | rate "6,5"; price "$400,000" (M30, M44) | Same as default | PASS |
| MC-21 | price "400.000" (M31) | Warning or confirmation (implausible price / ambiguous separator) | **Currently: FAIL** ($400 home, $102.39) |
| MC-22 | term 20 (M32) | $2,852.50; comparison includes the user's term | PARTIAL (table stays 15/30) |
| MC-23 | $10M at 25% (M33) | $176,032.96 | PASS |
| MC-24 | down 19.99% / 5% (M34, M35) | $2,649.56 with PMI; $3,058.53, PMI 135 months | PASS |
| MC-25 | tax growth 3, insurance growth 5 (M36) | Cost-growth table appears; Limitations copy consistent | PARTIAL (copy says costs are flat) |
| MC-26 | maintenance 300 + income 10000 (M37) | $2,789.28; DTI excludes maintenance (24.9%) | PASS |
| MC-27 | FHA 10% on 15 y; USDA 5% (M41, M42) | $3,702.53, MIP $45 for 11 years; $3,003.38 | PASS |
| MC-28 | Blog scenarios B01–B04 ($450k, ins $110) | $3,284.88 / $2,797.94 / 15 y $4,252.98; 45000 in % → error | PASS |

## B. Exports, trial uses, sharing, privacy, content
| ID | Steps | Expected | Live |
|---|---|---|---|
| MC-29 | At 0 remaining: all 6 exports | Per Santosh's decision: cap dialog → Day Pass → email prompt (stop), or uncounted on purpose and shown as such | **Policy question** (all work, 10 → 10) |
| MC-30 | With uses left: A_csv_first and B_save_first orders, then reload | Per decision | **Pending** (RERUN row 28) |
| MC-31 | Download CSV | Inputs block, dated yearly and monthly rows, cost columns | PARTIAL |
| MC-32 | Print or save as PDF / Print (schedule closed and open) | One-page summary with inputs, breakdown, totals, payoff, date; schedule appendix; no blank pages; no controls | **Currently: FAIL** |
| MC-33 | Copy report vs Copy result | One consistent text with inputs and date | **Currently: FAIL** (differ) |
| MC-34 | Type price/income/debts, scroll, reload; watch the network | No request to any host carries the values | **Currently: FAIL** (GA, doubleclick, server) |
| MC-35 | Share this tool, then open the link | Link opens to the same result incl. biweekly (only when the user chooses to share numbers) | PARTIAL (biweekly dropped) |
| MC-36 | Favorites, Recent calculations, Clear | Local only; history in memory; Clear empties it | PASS |
| MC-37 | Locales /es … /id, /ar | Translated, or not advertised through hreflang; /ar not linked | **Currently: FAIL** |
| MC-38 | Video at 0:20–0:56 | Current UI, realistic numbers, no "free" | **Currently: FAIL** |
| MC-39 | iPhone SE 320 px | No horizontal scroll | **Currently: FAIL** (+9 px) |
| MC-40 | axe on desktop and Pixel 7 | No serious violations (keep ad slots; fix caption contrast) | **Currently: FAIL** |
