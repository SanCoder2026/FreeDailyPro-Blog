# PDF to Word mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)
Audited Nov 1 2026 ~1:20 PM ET at 375×812 and 390×844, test files fw9.pdf (6 pages, text + tables) and an image-only 2-page invoice (OCR path).

| # | Fix | Problem (measured) | Why / competitor reference | Effort |
|---|---|---|---|---|
| 1 | Smart ad placement (shared S4): keep the "Try Office Apps" chips but exclude them from the subtitle/tool area, move the "Discover more" block from under the drop zone to a reserved slot below the result, keep the bottom anchor with sticky actions offset above it | Chip injected mid-sentence into the subtitle ("Word files[Try Office Apps]") and the About text; "Discover more" list (5 rows) sits directly under the drop zone before the tool is used; anchor bar (~60px) covers the preview at y~950–1010 | Looks like part of our UI and pulls users off-site at the moment of intent. iLovePDF shows nothing but one 80px "Select PDF file" button; Smallpdf one 54px "Choose files" | S (ad settings) |
| 2 | Ready state: one buy link "Ads-free: $1 day pass · $4.99/month" replaces the two Quick Buy rows; language + page range fold into one 48px "Options · All 6 pages · OCR: English" row; Convert to Word full-width 52px; Reset becomes a 44px text link "Choose a different PDF"; optional trial line under Convert | Convert 140×36; Reset 36px; Quick Buy 28px with 12px text; page-range input 192px wide cuts its placeholder ("All pages, or like 1-3,6" → "1-3,6" clipped); OCR language label is 2 lines for an option most PDFs never need | Mockup fix1: Convert sits at y~695, fully in the fold, with nothing competing | S |
| 3 | Done state: one full-width 56px "Download fw9.docx" with "6 pages · 5 tables · uses 1 trial use" as its subtitle (replaces the separate "Converted:" card); "Convert another" as a 44px text link | Download Word File 182×36 at y554 (in the fold — keep); generic label; stats card above adds a row | Users see what they get (file name, tables found) at the money moment. Smallpdf/iLovePDF use one dominant download button | XS |
| 4 | Remaining 44px targets and drop-zone copy: select and page input 44px; How to use it 32→44px; drop-zone text "Tap to choose a PDF to convert to Word / or tap to choose" says the same thing twice — drop the second line | 32–36px controls; duplicate line | Apple/Google 44–48px guidance | XS |
| 5 | Preview fidelity (QA hunch, verify): fw9 page 1 "Part I" heading renders white-on-white (1.0:1) in the preview — the black heading band isn't drawn. Check whether the .docx has the same loss | Contrast scan of preview | Preview is the trust moment; a missing heading looks like lost content | XS–S |
| Shared | Header 2px sideways overflow at 375 (scrollWidth 377; 390 is fine) — S1; back/home floaters (40×88 at right, y657) — S2 | — | — | — |
| — | Wording OK: title/meta say "PDF to Word Converter - Editable .docx, OCR", no "Free", no "free tools"; footer count "300+" OK; contrast OK on our UI (lowest 9.43:1); inputs 16px OK; result above the fold OK | — | — | — |

Observed: after Convert, the counter still read "10 remaining today", so Convert didn't use a trial; Download wasn't clicked, so the "Download uses 1 trial use" line must be confirmed before shipping.
Benchmark: iLovePDF page height 752px with one 80px CTA at y242; Smallpdf 54px CTA at y415 but a 9,794px page; Adobe serves a desktop layout (scrollWidth 980) on mobile. Our edge to keep: on-device, OCR per page, tables/form fields count, page range, and the inline preview — none of the three show a preview before download.

## Crops
- fix1-ready-state-before-after.png (crop1-ready-before/after.png)
- fix2-done-state-before-after.png (crop2-done-before/after.png)
Note: the "after" mockups also hide the Feedback floater; that's a mockup side-effect, not a proposal.

## Code sketch (class names illustrative; Claude maps them)
```html
<details class="rounded-lg border border-[#232B3D] bg-[#121826] px-3.5">
  <summary class="flex min-h-[48px] items-center">Options <span class="ml-2 text-[13px] text-muted-foreground">{range} · OCR: {lang}</span></summary>
  …language select + page range input (min-h-[44px], w-full)…
</details>
<button class="w-full min-h-[52px] rounded-xl bg-primary text-[17px] font-bold text-[#0A0E17]">Convert to Word</button>
<button class="min-h-[44px] underline text-muted-foreground">Choose a different PDF</button>
<!-- done -->
<button class="w-full min-h-[56px] rounded-xl bg-primary text-[#0A0E17]"><b>Download {name}.docx</b><span class="block text-xs">{pages} pages · {tables} tables · uses 1 trial use</span></button>
```


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.
