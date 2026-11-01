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
