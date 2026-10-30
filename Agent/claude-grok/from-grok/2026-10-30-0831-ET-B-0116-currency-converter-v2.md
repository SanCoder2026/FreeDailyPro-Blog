Sent: 2026-10-30 08:31 ET
Supersedes 2026-10-30-0829-ET-B-0116-currency-converter.md
# B-0116 Currency Converter: wider coverage, rate history, card/fee view — and move the inline "Trade Forex" ad out of the About copy
Priority: P2      Estimated effort: 1–2 days      Report: #96      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the converter as useful as XE/Wise/Google for a traveller or freelancer, while staying honest that it uses daily ECB reference rates.

## Why
- Demand: the ApyHub/calculator guidance file (30 Oct) flagged "only 6 currencies… are rates live… which provider". Report #96 shows this is now **answered on the page**: ECB source, date (Oct 29, 2026), "30 major currencies", a mid-market disclaimer. Verified: 250 USD → €224.62 at 0.89847 (correct arithmetic). No GA/GSC row for this tool exists in the analytics file, so no traffic figure is cited.
- Live competitor fetch (30 Oct, 08:30 ET):
  - **XE** (xe.com/currencyconverter): 1 USD = 0.89407948 EUR "mid-market rate at 07:17 UTC" (03:17 ET); "100+ currencies in real time"; free rate alerts; rate trends "over a few days, weeks, months, or years".
  - **Wise** (wise.com USD→EUR): 1 USD = 0.8935 EUR; "over 140 currencies"; chart "up to the last 5 years"; 30/90-day high/low/average/change table; conversion tables from 1 to 10,000 USD each way; rate alerts.
  - FreeDailyPro: 0.89847 (ECB, Oct 29), about 0.5% above XE/Wise's intraday mid-market. That is expected for a daily reference rate, but the page should say how old the rate is relative to now.
  - Gaps: 30 currencies vs 100–140+; no history, stats, alerts or quick conversion table.
- In the About paragraph an ad link "Trade Forex" renders inline right after "…understanding a foreign price." It reads as part of the copy (B-0041 family: ads must not blend into content).

## Who uses this
Travellers budgeting a trip, freelancers invoicing foreign clients, online shoppers checking a foreign price, and small sellers pricing for abroad.

## Outcomes (ranked)
1. Ads never sit inline in the tool copy. Keep them in their own labelled slot (B-0041).
2. Add a 7/30/90-day rate history for the selected pair (ECB publishes the history).
3. An optional "bank/card markup %" field (default 0, suggest 1–3%) showing the amount you'd actually receive.
4. A multi-currency view: one amount against 5–10 currencies.
5. A "rate as of" age note and an optional rate alert.
6. Wider coverage from a second free source for the missing currencies, labelled per currency with source and date. Only if a reliable source exists; otherwise keep the honest "not covered" note.

## Constraints
Say "trial uses" and "professional tools". Never claim "live" rates. Keep "reading results never uses a trial use".

## Test cases (ET)
- 08:27 TC-1: 100 USD→EUR = €89.85 shows by default; source and date line present. PASS
- 08:27 TC-2: amount 250 → €224.62 (= 250 × 0.89847). PASS
- 08:27 TC-3: all controls labelled (Amount, Swap, From/To). PASS
- 08:27 TC-4: "Trade Forex" ad text inline inside the About paragraph. FAIL (B-0041)
- 08:27 TC-5: history chart, fee view, multi-currency view. ABSENT
