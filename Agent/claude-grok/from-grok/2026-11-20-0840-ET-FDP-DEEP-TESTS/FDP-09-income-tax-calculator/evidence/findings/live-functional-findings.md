Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: live functional findings

- **Written:** 2026-11-19 13:20 EST (box `date`, ET). Guest, headless Playwright 1.65.1 (Chromium). No sign-in, no card or email entered, no ad clicks.
- **Reference:** `scripts/ref_federal.py`, an independent 2026 model. It uses brackets from Rev. Proc. 2025-32 and the following figures:
  - standard deduction 16,100 / 32,200 / 16,100 / 24,150
  - SS wage base 184,500
  - Additional Medicare thresholds 200k / 250k / 125k
  - SE base 92.35%
  - §199A QBI with threshold 201,750 / 403,500 (MFS 201,775), a $75k / $150k phase-in range, no W-2 wages, and the $400 minimum.
- **Raw results:**
  - `json/cases-T01-T34.json` and `json/cases-T35-T40.json` (inputs, every result box, notes and alerts)
  - `json/gate*.json` (trial cost of copy/save/print)
  - `json/flat.json` (Custom Flat Rate mode)

## 1. Federal and FICA math: PASS for employees and for SE below the QBI threshold
- **T01–T09 (employees):** all statuses, 0 income, exactly the standard deduction, 250k, 800k, MFS 400k, MFJ 300k, 401(k) 10k and 60–63 catch-up, biweekly view. Every case matches the reference within $1 (federal, SS cap, Additional Medicare).
- **T10–T14 and T40 (self-employed):** 100k, 230k, 232k, 300, MFJ 250k, and 100k with 20k pre-tax. These also match within $1, with QBI shown in the note ("…and the $39,876 qualified business income deduction").

## 2. BUG (P1): self-employed QBI cliff, so earning more shows less take-home
The tool drops the QBI deduction to $0 as soon as taxable income before QBI passes the top of the 24% bracket (201,775 single / 403,550 MFJ, from bundle `z()`). The law (§199A) has a phase-in over the next $75k ($150k MFJ). For a sole proprietor with no W-2 wages it falls linearly, and the threshold is 201,750 / 403,500 for 2026.

| Case (single, SE, no state) | Tool federal | Reference federal | Overstated by | Tool take-home |
|---|---|---|---|---|
| T12 SE 232,000 | $31,258 | $31,258 | 0 | $171,522 |
| T35 SE 240,000 | $43,415 | $33,082 | **$10,333** | $167,085 |
| T36 SE 245,000 | $44,994 | $34,780 | $10,214 | — |
| T37 SE 246,000 | $45,309 | $35,123 | $10,186 | — |
| T38 SE 260,000 | $49,729 | $40,060 | $9,669 | — |
| T39 SE 300,000 | $62,725 | $60,519 | $2,206 | — |

- Going from 232k to 240k profit, the shown take-home falls by **$4,437**.
- The thresholds are off by $25 (single) and $50 (MFJ). The tool also lacks the $400 minimum QBI deduction (for at least $1,000 of QBI), a minor issue.
- The UI does not say whether the business is a specified service (SSTB). For no-W-2-wage sole proprietors the phase-in is the same either way.
- The blog `/blog/estimate-us-self-employment-tax-2026` says "The Income Tax Calculator does not model … the qualified business income deduction". It does, so the blog is stale.

## 3. State results (code read plus live)
- **P1 local income taxes silently omitted:**
  - `stateTaxData` defines `localNote`/`localAvg` for MD, NY (NYC/Yonkers), IN, OH, PA, MI and KY. No code in the tool reads them, and the live notes for MD, NY, IN, OH and PA show no local-tax note.
  - **Maryland:** every resident pays county tax of 2.25–3.30% (DLS 2026 table; 3.20% in most counties). For T17 MD $85k single, the tool shows state $3,674, which matches the state-only schedule. The missing county tax is about $1,765–$2,589 (3.2% → **$2,510**), and nothing on the page says it's missing.
  - **NYC residents:** about 3.1–3.9% city tax, also not mentioned.
- **P1 head of household uses single state brackets and the single standard deduction:**
  - T19 CA HoH $85k shows state $3,660, the same as single (T15).
  - The FTB 2025 Schedule Z with the $11,412 standard deduction gives about **$1,636**, so the tool overstates by about $2,024.
  - The same code path is likely used for every state with a separate HoH schedule (by code read; CA verified).
- **P2 Pennsylvania:** 401(k) deferrals reduce PA taxable income in the tool. T18: $2,303 = (85,000 − 10,000) × 3.07%. PA taxes deferrals, so the correct figure is $2,609.50 ($307 understated).
- **P2:** CA uses the 2025 schedule. This is disclosed in the state note.
- **NY:** the SDI/PFL note is present. TX (no tax) is correct. SC, NJ, IN and OH were checked for plausibility only.

## 4. Inputs and validation: PASS
- "abc", "85k" and "1e12" give "Enter an income as a number". Negatives are rejected. "1,000,000" is parsed. Decimals are accepted.
- A 401(k) above the limit gives an IRS-cited error, and the age group changes the limit (24,500 / 32,500 / 35,750 for 60–63).
- Pre-tax larger than income gives an error.
- The income input is `inputmode=decimal`.

## 5. Not modelled (disclosed or partly disclosed)
- Credits and itemised deductions are disclosed as not included.
- **P2, not disclosed:** the extra standard deduction for age 65+/blind and the 2025–2028 senior deduction ($6,000). The only age select is "Age group for the 401(k) limit".
- **P2:** "Effective rate" includes FICA (19.3% at $85k), and the label doesn't say so.

## 6. Trial cost of Copy / Save as text / Print (P0: contradicts the Terms and FAQ)
- **Terms** (`/terms`): "Text utilities, calculators and simple converters take no trial use at all."
- **FAQ** (`/faq`, also in the FAQ schema): "Text, calculator and converter tools (word counter, case converter, unit and tax calculators and similar) never use a trial use."
- **Tool page** (and the saved text file): "Reading results never uses a trial use. Copying, saving or printing uses 1 per visit." The SE-tax blog says the same.
- **Live, context with 10 left** (`json/gate2.json`, 13:07 EST): Copy result → toast "Result copied", strip 10 → **9**. Copies 2 and 3 on the same visit cost nothing.
  - In `gate.json` (13:06), Save as text, Print and Ctrl+C after the first copy cost nothing more.
  - The saved .txt ends "Calculated with FreeDailyPro.com" (intentional mark).
- **Live, contexts at 0** (`gate2.json`, `gate3.json`):
  - Copy result → cap dialog "Today's trial uses are done … copying needs a pass … Monthly for $4.99 … Day Pass for $1"; the clipboard is empty.
  - Save as text → the dialog ("downloading needs a pass"); no download.
  - Print → the dialog ("printing needs a pass"); `window.print` is not called.
  - Selecting the visible "$68,628" and pressing **Ctrl+C** → the same dialog, and the clipboard is empty.
  - Screenshots: `screens/live/gate-copy-at-zero.png`, `gate-print-at-zero.png`, `gate-ctrlc-at-zero.png`.
- **Mechanism (by code):**
  - `useLogToolUsage` wraps `navigator.clipboard.writeText` and listens for `copy` events inside `main`; either one calls `tryUse`.
  - Any page script's clipboard write counts too. Our own test sentinel write triggered the dialog, so the scripts now avoid it.
- **Starting state (display-only):** of 15 tracked fresh contexts today (13:03–13:18 EST), **13 loaded at "0 remaining today"** and 2 at 10 (more context loads are in the matrix). A new guest therefore usually cannot copy, save or print a result, or even Ctrl+C a number on screen, although the Terms and FAQ promise calculators never use a trial use.
- **Not yet observed (re-run):** whether Save as text or Print, as the *first* action of a visit with uses left, costs 1. Six fresh contexts at 13:18 EST all loaded at 0. See RERUN row #9.

## 7. Custom Flat Rate mode (P2)
- Currencies: $, €, £, ₹, ¥, A$, C$. The math is correct.
- **No rate validation:** 150% gives "Estimated Take-Home Income $-50,000", and −5% gives "Tax at -5% $-5,000" with no alert. `$-50,000` is also an unusual format.
- The currency `<select>` had no `aria-label` or `<label>` in a DOM read (axe was not run in this mode).

## 8. Keyboard and a11y (default mode)
- The tab order is logical: income → filing status → state → pre-tax → per → age → SE checkbox → source link → Copy / Save / Print. Focus is visible.
- **axe** (main): 0 violations in the gate run.
  - Matrix: desktop `label-content-name-mismatch` serious ×1 (`.right-2`, the header) and `region` moderate ×1.
  - Pixel 7: `color-contrast` serious ×2 on the ad label text.
- The result has no `aria-live` or `role=status`, so screen-reader users get no announcement when the numbers change (P2).
