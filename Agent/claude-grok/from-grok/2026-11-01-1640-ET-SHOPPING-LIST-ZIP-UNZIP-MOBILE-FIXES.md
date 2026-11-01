Sent: 2026-11-01 16:40 ET
Source: owner (Santosh approved the Shopping List and Zip/Unzip mobile design fixes, Nov 1 4:38 PM ET, relayed by the Web Design bot).

## Intent
Make Shopping List and Zip/Unzip on phones (375/390px) feel best-in-class: the main action and the totals are always reachable, and file names are readable.

## Why
On phones, totals that scroll away and a Create ZIP button below the fold cause drop-off before users finish the task or upgrade.

## Outcome wanted
Shopping List: totals stay pinned while scrolling, plus the other ranked fixes in the spec. Pricing is unchanged: it's a Premium Application at 2 trial uses a day, $3 day pass, $9.99/month.
Zip/Unzip: a pinned Create ZIP button, full file names, plus the rest of the spec.
Ads: follow the ads rule (0d501a1). Never remove ads; place them per /workspace/web-design/ads-plan-standard.md, and keep sticky bars clear of the anchor ad.

## Specs

### shopping-list-mobile-fix-list.md
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

### zip-unzip-mobile-fix-list.md
# ZIP / UnZIP mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | After files are added: shrink the 290px dropzone to a 48px "+ Add more files" button and show a sticky bottom bar "3 files · 78 KB" + 48px **Create ZIP** (or **Extract ZIP** when a .zip is added); after zipping the bar becomes **Download ZIP**. One buy link replaces the two Quick Buy rows | High: action from y960 → always visible | S |
| 2 | File rows: wrap full file names (or middle-truncate keeping the end, "Quarterly-fin…final-1.txt"), × to 44px; show only the button that fits the files (hide Extract ZIP when no .zip; hide Create ZIP when only one .zip) | High: users can tell files apart; no dead button | XS |
| 3 | Empty state copy: one line "Choose files to ZIP, or a ZIP to extract" + two clear chips "Create a ZIP" / "Extract a ZIP" (ezyZip pattern); drop "or tap to choose" and the repeated subtitle | Med | XS |
| 4 | Result: full-width 48px Download ZIP with size ("Download ZIP · 61 KB"); archive name defaults to "files-2026-11-01.zip", not the first file's name | Med | XS |
| 5 | Remaining 44px: archive-name input, compression select, Clear, related-tool chips | Med | XS |
| Shared | Header 2px (S1), back/home hidden (S2), 44px (S3), S4 smart ad placement (anchor kept; sticky Create/Download bar offset above it so the file list is clear) | — | — |

## 1. Sticky action bar
```html
<button class="w-full min-h-[48px] rounded-xl border border-dashed border-primary text-primary sm:hidden">+ Add more files</button>
<div class="fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] sm:hidden">
  <div class="flex-1 text-[13px] text-muted-foreground">{n} files · {size}</div>
  <button class="min-h-[48px] rounded-lg bg-primary px-5 font-bold text-[#0A0E17]">{hasZip ? 'Extract ZIP' : done ? 'Download ZIP' : 'Create ZIP'}</button>
</div>
<a href="/pricing" class="inline-flex min-h-[44px] items-center text-primary underline sm:hidden">Ads-free: $1 day pass · $4.99/month</a>
```
Add ~80px bottom padding to main while the bar shows.

## 2. File rows
```css
@media(max-width:639px){
 .zip-file-name{white-space:normal;overflow-wrap:anywhere;text-overflow:clip;min-width:0}
 .zip-file-row [aria-label^="Remove"]{min-width:44px;min-height:44px}
 .zip-actions button{min-height:44px}
}
```
JS: `extractBtn.hidden = !files.some(f=>/\.zip$/i.test(f.name))`.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.

Images: assets/shoplist-zip-mobile/. Web Design will verify at 375px once live.
