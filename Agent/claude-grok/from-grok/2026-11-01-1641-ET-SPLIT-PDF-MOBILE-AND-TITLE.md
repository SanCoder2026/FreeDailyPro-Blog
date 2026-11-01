Sent: 2026-11-01 16:41 ET
Source: owner (Santosh approved both Split PDF items, Nov 1 4:39 PM ET, relayed by the Web Design bot).

## Intent
Make Split PDF on phones (375/390px) clear and quick, and remove "Free" from its title and meta.

## Why
On mobile the pages and the Split action are hard to reach, and result names are cut off. "Free" in the title contradicts the trial model (owner wording rule).

## Outcome wanted
(a) Fixes 1-5 in the spec: a swipeable page strip, a pinned "Split into N files" button, full result file names, the watermark note shown once, and the rest of the list.
(b) Title and meta description: replace "Free" / "Free and private" with "Private, on-device" wording that mentions 10 trial uses a day (Split PDF is a Professional Tool). Update all languages consistently.
Ads: follow ads rule 0d501a1 (smart placement, none turned off). Pricing unchanged.

## Spec

# Split PDF mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | After a PDF is added: replace the 288px nested-scroll preview grid with one horizontal page strip (60px thumbs, swipe sideways), and add a sticky bottom bar "12 pages · 3 files from 1-3, 4-8, 9-12" + 48px **Split into 3 files** (live count from the ranges). After splitting the bar becomes **Download all (ZIP)**. One buy link replaces the two Quick Buy rows | High: action from y966 to always visible; no scroll trap | S |
| 2 | Result rows: wrap the full file name (it's the only thing telling files apart), 44px icon Download button, and show the watermark note once above the list ("Trial downloads carry a small badge. Remove it with the $1 day pass") instead of on every row | High: readable results, ~300px less clutter for 3 files | XS |
| 3 | Tap pages to pick them (idea; competitor post-upload flows not tested this run): tapping thumbnails toggles them into the range field, so people don't have to type "1-3, 4-8" on a phone keyboard | High | M |
| 4 | Remaining 44px targets: ranges input, split-every input, Apply, Every page, checkbox row (whole label tappable), Reset, Download all (48px) | Med | XS |
| 5 | Wording (Santosh to confirm): title/og/meta "…, Free" and "Free and private" to e.g. "Split PDF by Page Range or Every Page — Private, On-Device" and "…Runs on your device; 10 trial uses a day." | Med (rule + SEO) | XS |
| Shared | Header 2px overflow (S1), back/home floating buttons hidden (S2), 44px (S3), S4 smart ad placement (anchor stays; sticky Split bar offset above it so the ranges label is clear) | — | — |

## 1. Page strip + sticky bar
```html
<div class="flex gap-2 overflow-x-auto snap-x sm:grid sm:grid-cols-4 md:grid-cols-6 sm:max-h-72">…60px thumbs…</div>
<div class="fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] sm:hidden">
  <div class="flex-1 text-[13px] text-muted-foreground">{pages} pages · {n} files from {ranges}</div>
  <button class="min-h-[48px] rounded-lg bg-primary px-5 font-bold text-[#0A0E17]">{done ? 'Download all (ZIP)' : `Split into ${n} files`}</button>
</div>
```
Add ~80px bottom padding to main while the bar shows. On mobile drop `max-h-72 overflow-y-auto` from the grid.

## 2. Result rows
```css
@media(max-width:639px){
 .split-result p.truncate{white-space:normal;overflow-wrap:anywhere;text-overflow:clip}
 .split-result button{min-height:44px;min-width:44px}
}
```
Render the badge note once under "Download all", not inside each row.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.

Images: assets/split-pdf-mobile/. Web Design will verify at 375px once live.
