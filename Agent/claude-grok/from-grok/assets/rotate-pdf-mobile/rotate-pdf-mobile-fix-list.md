# Rotate PDF mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Problem (measured) | Why / competitor reference | Effort |
|---|---|---|---|---|
| 1 | After a PDF is added: sticky bottom bar "12 pages · 12 turned 90° right" + 48px **Apply rotation**; after applying it becomes **Download**. One buy link "Ads-free: $1 day pass · $4.99/month" replaces the two Quick Buy rows (keeps monthly beside day pass) | Apply rotation at y2739 (375) / y2795 (390), 3+ screens below the 812/844 fold; 36px tall; anchor ad covers the first page row | The one action is never visible while choosing pages. iLovePDF and Smallpdf each show one big primary action (80px / 54px) and nothing competing | S |
| 2 | Compact page grid on mobile: 3 columns, gap 8px; ↺ page-number ↻ under each thumb; tap a thumbnail = turn 90°; hide the "+0° from current" line and the −/angle/+ row behind one "Fine-tune angle" link (opens a sheet for the chosen page) | 2 columns × 342px cards, grid 2130px for 12 pages; 5 controls per page (60 total); angle inputs 24px tall | Mockup grid height 789px (−63%); 9 pages per screen instead of ~2. Fine angle stays (our edge over iLovePDF/Smallpdf) but out of the way | S |
| 3 | Done state: Download 48px; watermark note as one short line "Trial downloads carry a small badge — remove it with the $1 day pass" with a 44px link; Compare page input and label 44px | Download 36px; "Go paid to avoid the mark" link 16px tall, 12px text; compare input 32px, label 16px | Download is the money moment; auto-scroll already puts it at viewport y393 (good — keep) | XS |
| 4 | Remaining 44px targets: One file/Several files, Rotate odd/even pages, All 90° left/right (32px each), Reset 36px, How to use it 32px; per-page rotate icons from 12px to 18px | 8 controls at 32px; icons 12px inside 44px buttons | Apple/Google 44–48px guidance | XS |
| 5 | Wording (Santosh to confirm): title/og/twitter "…, Free" → e.g. "Rotate PDF Pages — Fix Sideways or Skewed Scans | FreeDailyPro"; description "Free, no signup." → "Runs on your device; 10 trial uses a day."; VideoObject name drop "Free"; review Offer price "0" | 3 titles + 3 descriptions + JSON-LD use "Free" | Trial-uses rule; same open question as Split PDF | XS |
| Shared | Header 2px overflow (S1), back/home floaters hidden (S2), 44px (S3), S4 smart ad placement (anchor stays; sticky Apply/Download bar sits above it so it no longer covers the first page row); file name wrap instead of "…appe…" | — | — | — |
| — | Counts: OK (300+). Contrast: OK (lowest 9.43:1) | — | — | — |

## 1. Sticky bar
```html
<div class="fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] sm:hidden">
  <div class="flex-1 text-[13px] text-muted-foreground">{pages} pages · {changed} turned</div>
  <button class="min-h-[48px] rounded-lg bg-primary px-5 font-bold text-[#0A0E17]">{done ? 'Download' : 'Apply rotation'}</button>
</div>
```
Add ~80px bottom padding to main while the bar shows.

## 2. Page grid
```html
<p class="text-sm text-muted-foreground sm:hidden">Tap a page to turn it 90°. Skewed scan? <button class="min-h-[44px] text-primary underline">Fine-tune angle</button></p>
<div class="grid grid-cols-3 gap-2 sm:grid-cols-3 sm:gap-4 md:grid-cols-4">…</div>
```
```css
@media(max-width:639px){
 .rotate-card .fine-angle,.rotate-card .delta{display:none}   /* shown in the Fine-tune sheet */
 .rotate-card button svg{width:18px;height:18px}
 main button,main input[type=number]{min-height:44px}
}
```
(Class names illustrative; Claude maps them to the real components.)

## Optional: trial-use hint (added Nov 1 2026)
QA-401 confirmed the counter: **Apply rotation does not use a trial; Download does.** Optional small line under the sticky bar's Download state (and under Download in the done state):
```html
<p class="text-[13px] text-muted-foreground">Download uses 1 trial use · Apply doesn't use one</p>
```
Show only for trial users (hide with day pass / monthly). Santosh to approve with fixes 1–4.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.
