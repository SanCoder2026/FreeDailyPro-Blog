Sent: 2026-11-01 16:31 ET
Source: owner (Santosh approved all 6 Merge PDF mobile fixes, Nov 1 4:30 PM ET, relayed by the Web Design bot).

## Intent
Make Merge PDF on phones (375/390px) as easy to use as the best competitors: add files, see them clearly, tap Merge, and download, with nothing covering the controls.

## Why
Merge PDF is a top tool. On mobile, the big upload box pushes Merge below the fold, file names get cut off, and floating buttons or ads cover controls, so users drop off before they merge or buy.

## Outcome wanted
1. Once files are added, the upload box shrinks to an "Add more files" button, and Merge stays pinned at the bottom.
2. Full file names are visible, with bigger reorder and remove buttons.
3. Floating buttons no longer cover content. The "Try Office Apps" ad part depends on the open ads decision (S4), so only do the floating-button part until Santosh decides.
4. One buy link replaces the two Quick Buy rows. No price changes.
5. A clearer, full-width Download button.
6. All tap targets are at least 44px.

## Spec (measurements, before/after images)

# Merge PDF mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)
Audited Nov 1 2026, 10:05–10:20 AM ET, at 375×812 and 390×844, with 3 test PDFs (9 pages) added and merged.

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | After files are added: shrink the 208px dropzone to a 48px "+ Add more files" button, hide "Take photo with camera", and show a sticky bottom bar with "3 files · 9 pages" and a 48px **Merge 3 PDFs** button | High: Merge button goes from y1315 (375) / y1232 (390), about 500px below the fold, to always visible | S |
| 2 | File rows: full file name on its own line (now cut to ~13 chars, e.g. "Invoice-Oc…", 85px wide with 262px of text), then one control line: page range, Pick pages, up, down, remove, all 44px | High: users can tell files apart and reorder reliably | S |
| 3 | Overlaps: floating back/home/chat stack (x325–365) sits over "Clear All" and the result buttons; the Google anchor ad ("Try Office Apps", class google-anno-skip) covers the file list and the Merge area. Hide back/home under 640px (already approved site-wide) and turn off anchor/auto-anchor ads on tool pages (or at least while files are loaded) | High: no covered buttons during the money moment | XS |
| 4 | One buy link instead of two Quick Buy rows (same pattern already approved on calculators): "Ads-free: $1 day pass · $4.99/month" | Med: dropzone moves up ~45px (top y412 now; iLovePDF's CTA is at y222, Smallpdf's at y213) | XS |
| 5 | Result block: make **Download Merged PDF** full-width 48px primary; put "Continue with Add Page Numbers / Add Watermark" as a smaller "Next steps" row below; move "Clear All" away from Download (now side by side under floating buttons). Make "Go paid to avoid the mark" a 44px link to /pricing | Med: clearer primary action + upgrade path | S |
| 6 | Tap targets under 44px: Quick Buy 28, Take photo 36, drag handle 32, page-range input 28, Choose pages 28, Arrange all pages 32, blank-page checkbox 24, Merge 36, Clear All 36, Download 36, Continue buttons 36, related-tool chips 30 | Med | XS |
| Shared | 2px sideways scroll at 375 (scrollWidth 377) comes from the shared header, already approved | — | — |

Checks that passed: inputs are 16px (no iOS zoom); wording is clean (no "free tools"; trial copy reads "Trial: 10 uses/day"); no exact public counts on the page; dropzone is above the fold before upload; trust chips ("Files never stored", "Runs on your device") are a real edge over iLovePDF/Smallpdf, which upload files to their servers.

Benchmark (375px): iLovePDF shows one 80px red "Select PDF files" button at y222 and nothing else above the fold; Smallpdf a 300px dropzone at y213. Ours: dropzone at y412 after two Quick Buy rows. Our feature depth (page ranges, page picker, arrange-all-pages, blank-page for duplex, camera) beats both; the gap is only layout after files are added.

## Code sketch
```html
<!-- when files.length > 0, under 640px -->
<button class="w-full min-h-[48px] border border-dashed border-primary rounded-xl text-primary sm:hidden">+ Add more files</button>
<div class="fixed inset-x-0 bottom-0 z-50 bg-[#121826] border-t px-4 py-2.5 pb-[calc(10px+env(safe-area-inset-bottom))] flex items-center gap-2.5 sm:hidden">
  <div class="flex-1 text-[13px] text-muted-foreground">3 files · 9 pages</div>
  <button class="min-h-[48px] px-5 rounded-lg bg-primary text-[#0A0E17] font-bold">Merge 3 PDFs</button>
</div>
<!-- file row -->
<li class="rounded-2xl border p-3">
  <div class="flex items-center gap-2.5"><span class="drag min-h-[44px] min-w-[24px]">⠿</span><img class="w-10 h-13"><div class="min-w-0"><div class="break-words">{name}</div><div class="text-xs text-muted">{size} · {pages} pages</div></div></div>
  <div class="mt-2 grid grid-cols-[1fr_1fr_44px_44px_44px] gap-1.5 [&>*]:min-h-[44px]">
    <input placeholder="All pages" class="text-base"><button>Pick pages</button><button aria-label="Move up">↑</button><button aria-label="Move down">↓</button><button aria-label="Remove">✕</button>
  </div>
</li>
```
Add bottom padding to main (~80px) while the bar shows so the last row isn't hidden.

Images: assets/merge-pdf-mobile/. Web Design will verify at 375px once live.
