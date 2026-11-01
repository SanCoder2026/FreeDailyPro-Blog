Sent: 2026-11-01 16:42 ET
Source: owner (Santosh approved the 4 Compress PDF mobile fixes, Nov 1 4:41 PM ET, relayed by the Web Design bot).

## Intent
Make Compress PDF on phones (375/390px) as fast and clear as the best competitors.

## Why
Compress PDF is a top tool. On mobile, the action button and level choices are hard to reach and tap, which causes drop-off.

## Outcome wanted
1. A pinned Compress button that turns into "Download (size)" when it's done.
2. Compression levels shown as stacked rows with 44px buttons.
3. Full file names visible.
4. The rest of the ranked list in the spec.
Ads follow rule 0d501a1 (smart placement, nothing turned off). Pricing is unchanged (Professional Tool).

## Spec

# Compress PDF mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | After a PDF is added: sticky bottom bar "2.41 MB · Balanced" + 48px **Compress PDF**; after compressing it becomes **Download (40.0 KB)**. Fold "What is making this file big" into a one-line `<details>` ("Why is it 2.41 MB? Pictures 100%") and the mode description into the same pattern. One buy link "Ads-free: $1 day pass · $4.99/month" replaces the two Quick Buy rows (keeps monthly beside day pass) | High: action from y1068 to always visible | S |
| 2 | Level rows: stack on mobile — description full width, Compare + Download side by side underneath at 44px. Level 1 drops from ~15 lines to ~5 | High: readable results, ~400px shorter | XS |
| 3 | File name: wrap the full name; move the "Compressed: 40.0 KB" badge onto its own line under "Original" so the name isn't cut to "Annual-rep…" | Med | XS |
| 4 | Remaining 44px targets: mode chips, One file/Several files, Compare (also 14px text), New File, compare-page input; Download Compressed PDF 48px | Med | XS |
| Shared | Header 2px overflow (S1), back/home floaters hidden (S2), 44px (S3), S4 smart ad placement ("Try Office Apps" anchor kept; sticky bar lifted above it so bar and breakdown are clear) | — | — |
| — | Wording: no change needed (no "Free" in title/meta; 300+; monthly beside day pass) | — | — |

## 1. Sticky bar + folded detail
```html
<div class="fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] sm:hidden">
  <div class="flex-1 text-[13px] text-muted-foreground">{origSize} · {mode}</div>
  <button class="min-h-[48px] rounded-lg bg-primary px-5 font-bold text-[#0A0E17]">{done ? `Download (${outSize})` : 'Compress PDF'}</button>
</div>
<details class="sm:open rounded-lg border border-[#232B3D]"><summary class="min-h-[44px] px-3.5 flex items-center">Why is it {origSize}? Pictures {pct}%</summary>…breakdown…</details>
```
Add ~80px bottom padding to main while the bar shows.

## 2–4. CSS
```css
@media(max-width:639px){
 .compress-level{flex-direction:column;align-items:stretch;gap:8px}
 .compress-level .actions{display:flex;gap:8px;width:100%}
 .compress-level .actions>*{flex:1;min-height:44px;font-size:14px}
 .compress-file p.truncate{white-space:normal;overflow-wrap:anywhere;text-overflow:clip}
 .compress-file .badge-compressed{display:block;margin-top:2px}
 main button,main input[type=number]{min-height:44px}
}
```
(Class names illustrative; Claude maps them to the real components.)


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.

Images: assets/compress-pdf-mobile/. Web Design will verify at 375px once live.
