Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: how to reproduce

- **Common setup:** a guest, fresh browser profile, https://www.freedailypro.com/tool/income-tax-calculator, mode **US Federal Brackets**.
- Scripts are in `scripts/` (run from a folder that has `playwright` installed). Counters are display-only.

## R-1: copy/save/print cost and the block at 0 (P0)
1. Read https://www.freedailypro.com/terms. Under trial uses it says "Text utilities, calculators and simple converters take no trial use at all." The /faq says "never use a trial use".
2. **In a profile showing "10 remaining today":** click **Copy result**.
   - The toast says "Result copied" and the strip goes to **9**.
   - Copying again on the same visit costs nothing.
3. **In a profile showing "0 remaining today":**
   - **Copy result:** dialog "Today's trial uses are done … copying needs a pass"; the clipboard is empty.
   - **Save as text:** dialog "… downloading needs a pass"; no file.
   - **Print:** dialog "… printing needs a pass".
   - **Select the take-home figure and press Ctrl+C:** the same dialog; nothing is copied.
4. **Scripts:** `node scripts/it-gate2.js`, `node scripts/it-gate3.js`. Note that any `navigator.clipboard.writeText` on the page also triggers the gate.

## R-2: QBI cliff (P1)
1. Single, no state, tick **I'm self-employed**.
2. Enter 232000: federal $31,258, take-home $171,522, and the note includes the QBI deduction.
3. Enter 240000: federal **$43,415**, take-home **$167,085**, and the note has no QBI.
4. Reference: `python3 scripts/ref_federal.py 240000 single 0 se` gives a federal of $33,082.
5. Script: `node scripts/it-live.js T11_se_230k,T12_se_232k,T35_se_240k,T36_se_245k,T37_se_246k,T38_se_260k,T39_se_300k`.

## R-3: Maryland county tax omitted (P1)
1. Single, $85,000, state **Maryland**. State tax is $3,674, which is the state schedule only.
2. The notes show only the source note. There is no mention of county tax (2.25–3.30%, DLS 2026 table; 3.20% in most counties gives about $2,510 more).
3. NY, IN, OH and PA likewise show no local note.

## R-4: CA head of household (P1)
1. HoH, $85,000, California. State tax is $3,660, the same as Single.
2. FTB 2025 Schedule Z with std $11,412: taxable 73,588 → $1,788.63 − $153 credit ≈ **$1,636**.

## R-5: PA 401(k) (P2)
Single, $85,000, Pennsylvania, pre-tax 10,000. State tax is $2,303 = 75,000 × 3.07%. The expected figure is $2,609.50 (PA taxes deferrals).

## R-6: flat rate (P2)
Custom Flat Rate, 100000 at 150% gives "$-50,000". At −5% it gives "Tax at -5% $-5,000". There is no alert. Script: `node scripts/it-flat.js`.
