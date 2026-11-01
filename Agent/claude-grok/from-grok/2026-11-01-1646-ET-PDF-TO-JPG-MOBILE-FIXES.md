Sent: 2026-11-01 16:46 ET
Source: owner (Santosh approved all 5 PDF to JPG mobile fixes, Nov 1 4:45 PM ET, relayed by the Web Design bot).

## Intent
Make PDF to JPG on phones (375/390px) quick to finish while keeping ad revenue.

## Outcome wanted
1. A full-width "Download all N pages" button with a "uses 1 trial use" note. This builds on fcbeec2, which fixed the overflow.
2. Ads rule 0d501a1: do NOT turn off auto-ads. Keep them out of the tool area, and place a pinned "Convert N pages" bar offset above the anchor ad.
3. A save button on each page, plus Save to Photos.
4. One buy link, "$1 day pass · $4.99/month" (pricing unchanged), and bigger option buttons.
5. Tell users clearly that trial downloads carry a "Created with FreeDailyPro.com" badge.

## Spec

# PDF to JPG mobile: ranked fix list (proposals that need Santosh's approval; nothing sent to Claude)
Audited Nov 1 2026 ~2:30 PM ET at 375×812 and 390×844. Test file: generated 4-page PDF with a long name. Measurements are in pdf-to-jpg-mobile-audit.md.

| # | Fix | Problem (measured) | Why / competitor reference | Effort | Impact |
|---|---|---|---|---|---|
| 1 | **Done state: Download fits the screen.** Make it a full-width 56–60px button that wraps text: "Download all 4 pages (ZIP)", with the subtitle "4 × JPG 1224×1584 · 541 KB · uses 1 trial use". Put the file name in the subtitle, not the label. "Convert More" becomes a 44px text link "Convert another PDF". | Button is 469×36 with `white-space:nowrap`, so scrollWidth is 486 (375) / 485 (390). The page scrolls ~111px sideways and the label is cut off. After the download the page stayed shifted left. Download used 1 trial (10→9) without saying so | This is a layout bug at the money moment. Mockup fix2: scrollWidth back to 377 (the shared header 2px), button 343×60 | XS | High |
| 2 | **Ready state: smart ad placement and a sticky Convert.** Keep the side-rail/anchor ("Try Editing Apps") with the Convert bar offset above it; exclude in-text chips from the subtitle/tool area (they stay in About/footer); move the "Discover more" block from under the drop zone to a reserved slot below the result (shared S4 smart placement, ad settings). Add a sticky 52px bottom bar "Convert 4 pages" with "4 pages · High 144 dpi · JPG" and a "Choose a different PDF" link (replaces Reset). | Convert 132×36 at y784, bottom 820 below the 812 fold. The fixed Google rail at viewport y751–801 (299×50) covers Page range and Convert at 375; at 390 it sits at y778–828, also on Convert. A "Discover more" block (375px) sits right under the drop zone at y666. Chips are in the subtitle y187, About y1263 and footer y2274 | iLovePDF: sticky 48px Convert in the fold, nothing else on screen. Mockup fix1 | S (ad settings) + S | High |
| 3 | **Per-page control on the result cards** (Rule 1 gap). Each thumbnail gets a select checkbox (all on by default) and a 44px "save this page" button. Add "Download selected (N)" and "Select all / none". On iOS/Android, a "Save to Photos / Share" via the Web Share API (`navigator.share({files})`) is the most-wanted mobile action. Show "Page 1…4" instead of cut-off file names. | Cards have 0 buttons. The only output is the ZIP, and phones can't easily open a ZIP into Photos. Names are cut to "Product-catalog-autum…" | No competitor does on-device select + share. iLovePDF/Smallpdf give a ZIP only | M | High |
| 4 | **One buy link plus 44px controls, and remove duplicates.** Replace the two Quick Buy rows with "Ads-free: $1 day pass · $4.99/month". Quality and format chips to 44px. Page input to 44px with the placeholder "All 4 pages (or e.g. 1, 3-4)". Show the page count before converting ("4 pages → 4 JPGs"). Drop the "🔒 Runs entirely in your browser" card (the chips already say it) and the second drop-zone line "or tap to choose". Clearer success line: "✓ 4 pages ready". | Quick Buy 28px with 12px text ×2. Chips and JPG/PNG 32px. Input 36px with a clipped placeholder. Privacy said 3× in one screen | Apple/Google 44–48px guidance. iLovePDF tells you "4 JPG will be created" | XS | Med |
| 5 | **Disclose the trial badge (or confirm the intent).** Each downloaded JPG carries two "Created with FreeDailyPro.com" badges (top-right and bottom-right), and the page never says so. If this is intended, add one line under Download: "Trial downloads carry a small FreeDailyPro badge. Ads-free pass removes it." That also sells the pass. Plus the JSON-LD question: `offers.price "0"` (and "Free…" alternateNames). Remove it or replace it with the real offer. | Found in the downloaded ZIP (evidence-downloaded-page-01-badges.jpg). The word "watermark" isn't in the tool UI | Surprise watermarks drive 1-star reviews; disclosure turns it into an upsell. The JSON-LD question is the same one open on Split/Rotate PDF and Morse | XS | Med |
| 6 | Capability gaps to beat iLovePDF (Rule 1, never basic). (a) "Extract embedded images" mode next to "Page to JPG". (b) A JPG quality slider (60–95%) with a live size estimate next to the DPI choice. (c) Custom width presets: 1080 px Instagram, 1920 HD, A4 300 dpi. (d) Long-image mode: stitch all pages into one tall JPG (popular for sharing on chat apps). (e) WebP output. (f) Remember the last DPI/format. (g) A "Next: compress images / JPG to PDF" chain into Premium Applications | iLovePDF has Extract images + Normal/High quality. Nobody offers stitch/long-image or social sizes on-device | M–L | High (usage) |
| Shared | Header 2px sideways overflow at 375 (S1). Back/home floaters 40×88 at x325 y657 (S2). Footer "All Tools" summary is 20px tall even though it has `min-h-[44px]` | — | — | XS | Low |
| — | OK as is: no "free tools" wording. "Trial: 10 uses/day · N remaining today". Footer "300+ professional tools". All Tools `<details>` closed with 361 links in the server-rendered HTML. Inputs 16px. Contrast ≥ 9.43:1. Convert does not spend a trial (only Download does). ZIP naming `…-page-01.jpg` | — | — | — | — |

Benchmark: iLovePDF has a 752px page, one 80px CTA at y222, and after upload says "4 JPG will be created" with a sticky 48px Convert. Smallpdf uploads files to its server and has a 10,089px page. Adobe returned Access Denied on adobe.com and a sign-in wall on acrobat.adobe.com. Our edge to keep and promote: on-device processing, 4 DPI levels up to 300, PNG, page range, multi-PDF folders, real thumbnails.

## Crops
- fix1-ready-sticky-convert-before-after.png (crop1-ready-before.png / crop1-ready-after.png)
- fix2-done-download-overflow-before-after.png (crop2-done-before.png / crop2-done-after.png). The "after" also shows the proposed per-page ✓ and save buttons (fix 3) and the badge note (fix 5).
Note: the "after" mockups also hide the Feedback/back floaters. That's a side effect of the mockup, not a proposal.

## Code sketch (class names illustrative; Claude maps them)
```html
<!-- done -->
<button class="w-full min-h-[56px] rounded-xl bg-primary text-[#0A0E17] whitespace-normal">
  <b class="text-[17px]">Download all {n} pages (ZIP)</b>
  <span class="block text-xs">{n} × {fmt} {w}×{h} · {size} · uses 1 trial use</span></button>
<p class="text-[13px] text-muted-foreground text-center">Trial downloads carry a small FreeDailyPro badge. Ads-free pass removes it.</p>
<button class="min-h-[44px] underline text-muted-foreground">Convert another PDF</button>
<!-- ready: sticky bar (mobile only) -->
<div class="sm:hidden fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 pt-2.5 pb-[max(14px,env(safe-area-inset-bottom))]">
  <div class="flex-1 text-[13px] text-muted-foreground">{n} pages · {dpiLabel} · {fmt}</div>
  <button class="min-h-[52px] rounded-xl bg-primary px-5 font-bold text-[#0A0E17]">Convert {n} pages</button></div>
```


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.
