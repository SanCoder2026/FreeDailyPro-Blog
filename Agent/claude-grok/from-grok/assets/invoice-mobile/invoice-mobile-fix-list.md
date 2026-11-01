# Invoice Generator mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Problem (measured) | Why / competitor reference | Effort |
|---|---|---|---|---|
| 1 | Sticky bottom bar on mobile once any amount is entered: "Total · 3 items  $3,085.09" + 48px **Preview** + 48px **Download PDF** (Download = existing Generate). Preview opens the same PDF in a full-screen sheet (blob URL / iframe) — no trial use. One buy link "Ads-free: $3 day pass · $9.99/month" replaces the two Quick Buy rows (keeps monthly beside day pass) | Total y1595 / Download y1761 (375), ~2 screens below fold; no preview anywhere; Generate button 36px | Live total + action always visible; Invoice Simple has a Preview tab at y128, Invoice-Generator.com's Download is at y2569 — we'd beat both | S |
| 2 | Line items as stacked cards on mobile: full-width 2-line description, labelled Qty / Price / **Amount** row, Credit + Remove 44px; Add Line Item full width 44px | Description 167px shows ~19 of 46 chars; no labels once filled; no line amount; checkbox 24px | Readable rows and visible per-line math; Zoho cuts descriptions to 110px, Invoice-Generator.com 289px | S |
| 3 | Autosave the draft to localStorage (debounced 500ms) + "Saved on this device · Start new" line; keep "Your business" details for the next invoice and auto-increment INV-002 | Reload loses everything | Invoice-Generator.com keeps invoices in the browser; stays on-device (matches "Files never stored") | S |
| 4 | Logo upload (PNG/JPG/SVG, ≤1 MB, kept on device), shown top-left of the PDF | No file input | Invoice-Generator.com and Zoho both have it; most-asked invoice feature | M |
| 5 | Remaining 44px: inputs/selects 44, Try a sample / Clear 44, signature checkbox 24→ 44px row, How to use it 44 | 36/40/32/24px controls | Apple/Google 44–48px | XS |
| 6 | Optional hint under Download: "Download uses 1 trial use · Preview doesn't use one" | Download silently counts (2 → 1) | Clear trial rules | XS |
| Shared | Header 2px overflow (S1), back/home floaters hidden (S2 — cover field edges here), 44px (S3), S4 smart ad placement ("Try Billing Tools" anchor kept; sticky total/Download bar offset above it) | — | — | — |
| — | Wording OK: no "Free" in title/meta/schema (Offer 9.99); counts 300+; 16px inputs; monthly beside day pass. Pricing tier ($3/$9.99, 2 uses) = correct Premium Application tier (answered Nov 1 2026) | — | — | — |

## 1. Sticky bar + preview
```html
<div class="fixed inset-x-0 bottom-0 z-50 flex items-center gap-2.5 border-t border-[#232B3D] bg-[#121826] px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] sm:hidden">
  <div class="flex-1 leading-tight"><div class="text-[12px] text-muted-foreground">Total · {items.length} items</div>
    <div class="text-xl font-extrabold text-primary">{fmt(total)}</div></div>
  <button onClick={openPreview} class="min-h-[48px] rounded-lg border border-primary px-3.5 font-bold">Preview</button>
  <button onClick={generate} class="min-h-[48px] rounded-lg bg-primary px-3.5 font-bold text-[#0A0E17]">Download PDF</button>
</div>
```
Preview: build the same jsPDF doc, `URL.createObjectURL(doc.output('blob'))` into a full-screen `<iframe>` sheet (iOS: fall back to rendering page 1 to canvas). Don't count a trial use. Add ~90px bottom padding to main while the bar shows.

## 2. Line-item cards — CSS
```css
@media(max-width:639px){
 .inv-row{display:grid;grid-template-columns:72px 1fr 1fr;gap:8px;padding:10px;border:1px solid #232B3D;border-radius:12px;background:#121826}
 .inv-row .inv-desc{grid-column:1/-1}            /* make it a 2-row textarea */
 .inv-row .inv-desc textarea{min-height:48px;font-size:16px}
 .inv-row label.sr-only{position:static;width:auto;height:auto;clip:auto;font-size:13px;color:#9AA4B8} /* show Qty / Price labels */
 .inv-row .inv-amount{text-align:right;font-weight:700;line-height:44px}
 .inv-row .inv-credit,.inv-row .inv-remove{min-height:44px}
 .inv-add{width:100%;min-height:44px}
}
```
(Class names illustrative; Claude maps them to the real components. Add an Amount cell = qty×price, negative when Credit.)

## 3. Autosave
```js
useEffect(()=>{const t=setTimeout(()=>localStorage.setItem('fdp-invoice-draft',JSON.stringify(state)),500);return()=>clearTimeout(t)},[state]);
// on mount: hydrate from 'fdp-invoice-draft'; "Start new" keeps seller fields, clears client/items, invoiceNo++
```

## 5. Targets
```css
@media(max-width:639px){ main input,main select,main textarea{min-height:44px} main button{min-height:44px} }
```


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.


---
**Changelog — Nov 1 2026 (pricing tier rule):** Santosh's rule: Professional Tools = 10 trial uses/day, $1 day pass, $4.99/month; Premium Applications = 2 trial uses/day, $3 day pass, $9.99/month; Workflow Products = own plan $29.99 or $49.99/month, not covered by passes. Pricing marked answered.
