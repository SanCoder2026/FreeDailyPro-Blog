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
