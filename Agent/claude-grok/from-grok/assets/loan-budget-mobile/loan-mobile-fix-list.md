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
