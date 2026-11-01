Sent: 2026-11-01 16:30 ET
Source: owner (Santosh approved the Loan Calculator and Budget Planner mobile fixes, Nov 1 4:29 PM ET, relayed by the Web Design bot). Merge PDF items are NOT approved; skip them.

## Intent
Make the Loan Calculator and Budget Planner feel best-in-class on phones (375/390px). Benchmarks are NerdWallet, Bankrate, Calculator.net and Ramsey, and the answer should show without scrolling or sideways overflow.

## Why
Mobile is most of our traffic. A result that's hidden below the fold, a page that scrolls sideways, or totals that disappear all make people leave before they reach the trial or upgrade.

## Outcome wanted
Loan: the monthly payment sits above the fold; the 16px horizontal overflow from the amortization button is gone; the comparison table fits or scrolls inside its own box, not cut off.
Budget: totals are sticky while scrolling; expense rows fit at 375 without wrapping or clipping; inputs autosave locally so a refresh never loses data.
Pricing: no changes (Budget's pricing question is still open with Santosh).

## Specs (full detail, measurements, before/after images)

### Loan
# Loan calculator mobile — ranked fix list (needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | Result above fold: fold Quick Buy rows into one link; put Interest method, First payment date (+help text), Extra payment behind "More options" | High (y949 → **y712**, inside 812 fold) | S |
| 2 | Page-specific 16px sideways scroll: let the "Show full amortization schedule" button wrap / shorten label | High (391 → 377; 375 after shared header fix) | XS |
| 3 | Compare-extra-payments table → stacked cards on phones (or drop the repeated "vs No extra payment" sublines) | Med | S |
| 4 | De-duplicate: one export row (Copy · CSV · Print), one "How this was calculated", collapse "Loan workbench" into a `<details>` so its 2nd chart/schedule/export only appear when opened | Med (≈ -1,000px) | S |
| 5 | Shorten Quick Buy copy (if not done by #1): "Ads-free: $1/day · $4.99/month" | Low | XS |
| Shared | Header 2px, floating back/home `max-sm:hidden`, 44px controls — already approved | — | — |

## 1. Result above fold (fix1-result-above-fold-before-after.png)
```html
<p>Trial: 10 uses/day · 10 remaining today</p>
<a href="/pricing" class="inline-flex min-h-[44px] items-center text-primary underline sm:hidden">Ads-free: $1 day pass · $4.99/month</a>
<!-- keep the two Quick Buy rows for ≥640px: add class="max-sm:hidden" -->
<!-- after Loan Term row -->
<details class="text-sm text-muted-foreground">
  <summary class="min-h-[44px] flex items-center">More options: interest method, first payment date, extra payment</summary>
  …Interest method select, First payment date + help, Extra monthly payment…
</details>
```
Open the `<details>` automatically if any of those fields has a non-default value (or ?extra= in URL).

## 2. Schedule button overflow (crop2-table-overflow-before/after.png, fix2-compare-table-before-after.png)
```html
<button class="… w-full whitespace-normal min-h-[44px] text-left">Full schedule (360 payments)</button>
```
or CSS: `@media(max-width:639px){ .calc-print-area button{white-space:normal;max-width:100%} }`. Measured after: scrollWidth 377 (only the shared header 2px left).

## 3. Compare table → cards (<640px)
```css
@media(max-width:639px){
 .compare-table thead{display:none}
 .compare-table tr{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;padding:8px 0}
 .compare-table td:first-child{grid-column:1/-1;font-weight:600}
 .compare-table td span.block{display:none} /* drop "+$100 vs No extra payment" lines; show Interest saved row instead */
}
```
## 4. Duplicates
Wrap the workbench: `<details class="mt-6"><summary class="min-h-[44px]">Loan workbench: payment frequency, solve for, fees/APR, compare two loans</summary>…</details>`; keep one export row at the bottom of the main result; delete the second "Copy result / Save as text / Print" row.

### Budget
# Monthly budget planner mobile — ranked fix list (needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | Sticky totals bar (Income · Spent · Saved · **Left over**) pinned under the header on phones, so the total updates in view while typing; fold Quick Buy rows into one link | High (Left over visible at all times vs y1508) | S |
| 2 | Row layout: name full width + trash on line 1, amount + category on line 2, period 44px — no more truncated names | High | S |
| 3 | Save UX: auto-save the budget in this browser (localStorage, opt-out "Don't keep on this device"), move Back up/Restore next to the totals; update the "Nothing is saved…" line | High | M |
| 4 | Collapse the "Budget lines" table behind `<details>` on phones (it repeats the rows); merge the 3 export areas into one row; show the trial counter once | Med | S |
| 5 | Small donut/stacked bar for Needs/Wants/Savings/Left over in the 50/30/20 view | Med | M |
| 6 | 301 `/tool/budget-planner` → `/tool/monthly-budget-planner` | Low (SEO) | XS |
| Ask | Confirm pricing here: "2 uses/day, $3 day / $9.99 month" vs site standard "10 trial uses/day, $1 / $4.99" | — | Santosh |
| Shared | Header 2px, back/home `max-sm:hidden` (covers trash icons here), 44px — already approved | — | — |

## 1. Sticky totals (fix1-sticky-totals-before-after.png)
```html
<div class="sm:hidden sticky top-16 z-30 flex justify-between rounded-xl border border-[#232B3D] bg-[#121826] px-3 py-2 text-[13px] text-muted-foreground">
  <div>Income<b class="block text-[17px] text-foreground">{income}</b></div>
  <div>Spent<b class="block text-[17px] text-foreground">{expenses}</b></div>
  <div>Saved<b class="block text-[17px] text-foreground">{saved}</b></div>
  <div>Left over<b class="block text-[17px] text-primary">{leftover}</b></div>
</div>
```
Place it just above the "Income" heading; bind to the same totals state as "Monthly totals". Turn "Left over" red (#FF6B6B) and label it "Short by" when negative. Quick Buy → one link: `Ads-free: $3 day pass · $9.99/month` (or the standard prices if Santosh confirms).

## 2. Row layout (fix2-row-layout-before-after.png)
```css
@media (max-width:639px){
 .budget-row{grid-template-columns:1fr 1fr 44px}
 .budget-row>:nth-child(1){grid-column:1/3;grid-row:1}   /* name */
 .budget-row>:nth-child(4){grid-column:3;grid-row:1;min-height:44px} /* trash */
 .budget-row>:nth-child(2){grid-column:1;grid-row:2}     /* amount */
 .budget-row>:nth-child(3){grid-column:2;grid-row:2}     /* category */
 .budget-row input,.budget-row select,.budget-period{min-height:44px}
}
```
(current class `grid grid-cols-[1fr_96px_84px_36px]` → add `budget-row`.) Better still: put the period select inline as a "/mo · /yr" segmented toggle on line 2 to save a line per row.

## 3. Save
```js
const KEY='fdp-budget-v1';
useEffect(()=>{ if(keep) localStorage.setItem(KEY, JSON.stringify(rows)) },[rows,keep]);
// on load: const saved=localStorage.getItem(KEY); if(saved) setRows(JSON.parse(saved));
```
Copy: "Saved on this device only — never on our servers. [Don't keep on this device]". Keep Back up / Restore (file) for moving between devices.

Images: assets/loan-budget-mobile/. Web Design will verify at 375px once live.
