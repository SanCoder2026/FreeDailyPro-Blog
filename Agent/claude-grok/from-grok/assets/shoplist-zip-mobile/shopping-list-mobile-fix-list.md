# Shopping List Planner mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | Compact totals strip (List total · Bought · Left in budget) directly under the budget field, `position:sticky` under the header on phones; replaces the 150px cards. One buy link replaces the two Quick Buy rows | High: totals always visible while adding items (today they drop off-screen after ~4 items) | S |
| 2 | Item rows as cards: 44px checkbox hit area, name + line total + ✕ on line 1, labelled "Price ($)" and a − / qty / + stepper on line 2 | High: clear fields, no mis-taps | S |
| 3 | Remaining controls to 44px: Add item input + button, Copy List, Back up/Restore/Clear, related-tool chips | Med | XS |
| 4 | "Left in budget" turns red and reads "Over by $X" when negative; strike-through bought items and move them to the bottom | Med | S |
| 5 | Auto-save in this browser (localStorage, "Don't keep on this device" opt-out) instead of "erased when tab closes" — same as budget B3 | Med | M |
| ✔ Answered | Pricing "2 uses/day, $3 / $9.99" is correct: Shopping List is a Premium Application (D1 answered by Santosh, Nov 1 2026). Keep it. Drop the alternate "$1 · $4.99" mockup variant. | — | — |
| Shared | Header 2px (S1), back/home hidden <640px (S2, covers totals), 44px (S3), S4 smart ad placement (keep all ads; anchor offset above sticky bars; auto-ads excluded from tool area; reserved slots below result/after download/between sections — see ads-plan-standard.md) | — | — |

## 1. Totals strip
```html
<a href="/pricing" class="inline-flex min-h-[44px] items-center text-primary underline sm:hidden">Ads-free: $3 day pass · $9.99/month</a>
<!-- keep Quick Buy rows ≥640px: class="max-sm:hidden" -->
<div class="sm:hidden sticky top-16 z-30 my-2.5 flex justify-between rounded-xl border border-[#232B3D] bg-[#121826] px-3 py-2 text-[13px] text-muted-foreground">
  <div>List total<b class="block text-[17px] text-foreground">{total}</b></div>
  <div>Bought<b class="block text-[17px] text-foreground">{bought}</b></div>
  <div>Left in budget<b class="block text-[17px] text-primary">{left}</b></div>
</div>
```
Place right after the "Budget for this trip" input; hide the 3 big cards under 640px (`max-sm:hidden`).

## 2. Item rows
```css
@media(max-width:639px){
 .shop-row{display:grid;grid-template-columns:44px 1fr auto 44px;row-gap:4px;border:1px solid #232B3D;background:#121826;border-radius:14px;padding:8px 12px}
 .shop-row .price,.shop-row .qty{grid-row:2}
 .shop-row .price{grid-column:2}.shop-row .qty{grid-column:3/5;display:flex;gap:4px}
 .shop-row input,.shop-row button{min-height:44px}
 .shop-row label.check{min-width:44px;min-height:44px;display:flex;align-items:center;justify-content:center}
}
```
Add visible `<label>`s "Price ($)" and "Qty"; show `{price*qty}` as the line total next to the name.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.


---
**Changelog — Nov 1 2026 (pricing tier rule):** Santosh's rule: Professional Tools = 10 trial uses/day, $1 day pass, $4.99/month; Premium Applications = 2 trial uses/day, $3 day pass, $9.99/month; Workflow Products = own plan $29.99 or $49.99/month, not covered by passes. Pricing question answered; only the $3/$9.99 buy link stands.
