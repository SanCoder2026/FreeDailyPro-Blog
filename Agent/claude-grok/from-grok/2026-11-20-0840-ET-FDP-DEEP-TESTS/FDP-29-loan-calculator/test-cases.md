Sent: 2026-11-20 23:58 ET

# FDP-29 Loan / EMI Calculator: test cases

- **URL:** https://www.freedailypro.com/tool/loan-calculator, guest.
- **Defaults:** 100,000 USD, 5%, 30 years, reducing balance, extra 0.
- **"Live"** = 2026-11-20 23:34–23:46 EST.
- **Scripts:** `scripts/lc-live.js` (L*/W* ids), `lc-gate.js`, `lc-privacy.js`, `lc-misc.js`, `lc-share.js`.
- **Expected values** come from an independent amortisation.

## A. Main calculator
| ID | Input | Expected | Live |
|---|---|---|---|
| LC-01 | default (L01) | $536.82; total $193,255.78; interest $93,255.78; payoff Nov 2056 | PASS |
| LC-02 | rate 0 (L02) | $277.78 | PASS |
| LC-03 | 60 months (L03) | $1,887.12 | PASS |
| LC-04 | flat 10%, 5 y (L04) | $2,500.00; interest $50,000 | PASS |
| LC-05 | extra 200 (L05) | 201 payments, last Aug 1, 2043; interest $47,708.25 | PASS |
| LC-06 | INR 500000 / 9% / 20 y (L06) | ₹4,498.63; interest ₹5,79,671.15 | PASS |
| LC-07 | JPY 3,000,000 / 1.5% / 35 y (L07) | ¥9,186 | PASS |
| LC-08 | EUR 25000 / 7% / 5 y (L08) | €495.03 | PASS |
| LC-09 | amount 0 / abc; rate 101; term 0; term 101 y; extra −5 (L09–L14) | The matching message, results "—" | PASS |
| LC-10 | extra 200000 (L15) | "paid off in month 1" note | PASS |
| LC-11 | term 0.5 y (L16) | $16,910.56 | PASS |
| LC-12 | amount "400.000" (L17) | Warning or confirmation | **Currently: FAIL** ($2.15) |
| LC-13 | term 2.5 months (L18) | Message, or a visible rounding note | PARTIAL (silently 3) |
| LC-14 | extra 200, then flat (L19) | $694.44 and a note that extra is ignored | PARTIAL |
| LC-15 | 35,000 / 6.9% / 72 mo (L20) | $595.04 | PASS |
| LC-16 | Scenario table defaults | +$100 → 256 months; +$250 → 182 months | PASS |

## B. Loan workbench
| ID | Input | Expected | Live |
|---|---|---|---|
| LC-17 | Frequency monthly / weekly / biweekly (W01, W02, default) | $536.82 / $123.80 / $247.64 | PASS |
| LC-18 | Biweekly, compounding monthly / daily (W03, W04) | $247.49 / $247.77 | PASS |
| LC-19 | Solve rate 600 / 200; amount 600; term 600 / 400 (biweekly) (W05–W09) | 15.4463% / 3.2192%; $242,283.04; 202 / 342 payments | PASS |
| LC-20 | Solve for, untouched (W18) | Shows the user's own rate (5%) for their current payment | **Currently: FAIL** (13.7277%) |
| LC-21 | Amount 50000, then Solve for (W17) | Target follows the new payment | **Currently: FAIL** (27.9079%) |
| LC-22 | Fee 2000 / 300 / 100000 (W10–W12) | APR 5.1784% / 5.0264% (nominal); error at ≥ amount; label matches the metric | PARTIAL (label says "effective") |
| LC-23 | Deferred, zero-coupon (W13, W14) | $432,194.24 due; price $23,137.74 | PASS |
| LC-24 | Compare B 4.5% / 15 y, fee 0 / 3000 (W15, W16) | $764.99; APR 4.5% / 4.959% | PASS |

## C. Exports, trial uses, sharing, privacy, content
| ID | Steps | Expected | Live |
|---|---|---|---|
| LC-25 | At 0 remaining: all 9 actions | Per Santosh's decision | **Policy question** (all work, 10 → 10) |
| LC-26 | With uses left: lc-gate orders, then reload | Per decision | **Pending** (RERUN row 29) |
| LC-27 | Print or save as PDF / Print | Summary first (inputs, payment, totals, payoff, date); no controls or overlaps | **Currently: FAIL** |
| LC-28 | Copy result / Save as text | Includes amount, rate, term, method, date; no help text | **Currently: FAIL** |
| LC-29 | Download CSV (main + workbench) | Inputs header + dated rows | PARTIAL (rows OK, no inputs) |
| LC-30 | Type values, reload; watch the network | No host receives the values | **Currently: FAIL** |
| LC-31 | Share, then open the link | Same result (incl. workbench state if the user shares numbers) | PARTIAL (workbench not kept) |
| LC-32 | Favorites, history, Clear | Local only; in memory | PASS |
| LC-33 | /blog/loan-calculator | A post exists and matches the tool | **Currently: FAIL** (404) |
| LC-34 | Video | Current UI incl. workbench; "trial uses" | **Currently: FAIL** |
| LC-35 | Locales /es … /id, /ar | Translated, or not advertised through hreflang | **Currently: FAIL** |
| LC-36 | Details copy (fees, extra payments) | Consistent with the features | **Currently: FAIL** |

(Generated 2026-11-20 23:46:10 EST.)
