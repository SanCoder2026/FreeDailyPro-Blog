Sent: 2026-11-01 16:47 ET
Source: owner (Santosh approved the Image to PDF bugs and proposals, Nov 1 4:46 PM ET, relayed by the Web Design bot). This extends 60b5b8b.

## Outcome wanted
Bugs:
- File names wrap instead of being cut off.
- Controls sit in a 2×2 grid of 44px buttons.
- /tool/jpg-to-pdf redirects with a 301 to /tool/image-to-pdf, including all 9 language versions.
- The trial note says "bottom-right badge", not "footer".

Proposals:
- A sticky Convert bar, offset above the anchor ad.
- A full-width 56px Download button with "uses 1 trial use".
- 44px controls, and one buy link "$1 day pass · $4.99/month" (pricing unchanged).
- Add "JPG" to the title and H1.

Ads follow rule 0d501a1: auto-ads stay on but out of the tool area and subtitle.
NOT approved: fix 8 (new features). Leave it out.

## Spec

# Image to PDF mobile: ranked fix list (nothing sent to Claude; BUG = broken behaviour, PROPOSAL = needs Santosh)
Audited Nov 1 2026 ~3:00 PM ET at 375×812 / 390×844 with 4 long-named JPGs. Measurements in image-to-pdf-mobile-audit.md.

| # | Tag | Fix | Problem (measured) | Ref | Effort | Impact |
|---|---|---|---|---|---|---|
| 1 | **PROPOSAL (needs Santosh)** | **Ready state: sticky Convert bar + files before settings.** After the first upload, shrink the drop zone to a 48px "+ Add images" button (camera stays as a second 44px button), move the file list directly under it, fold Page setup into a 48px `<details>` "Page setup · US Letter · Portrait · Fit ▾". Pin a 52px bottom bar "4 images → 4 pages · uses 1 trial use on download" + "Convert to PDF". Clear all becomes a small text link. | Convert 132×36 at y1671 (375) / y1647 (390) = ~2 screens below the fold; after upload the fold doesn't change at all | iLovePDF sticky 48px Convert at y740, Smallpdf sticky Finish y756. Mockup fix1 | S | High |
| 2 | **BUG** | **File names clipped to a 49px column.** Let the name wrap (2–3 lines, `overflow-wrap:anywhere`, 14px) and move rotate into the ↑ ↓ ✕ cluster as a 2×2 grid of 44px buttons so the name column gets ~120px. | "Recei…", "Whit…", "Pass…", "IMG_…" at 375 (49px col; 64px at 390) — files are indistinguishable | Mockup fix2 | XS | High |
| 3 | **BUG** | **301 /tool/jpg-to-pdf → /tool/image-to-pdf** (and /es,/pt,/fr,/de,/ja,/hi,/zh,/ko,/id variants). Stop the 404 template from emitting og:url/hreflang for the missing URL. | /tool/jpg-to-pdf = HTTP 404 "Tool Not Found"; its HTML still advertises itself in og:url + 10 hreflang links | "JPG to PDF" is the head search term competitors rank on | XS | High (SEO) |
| 4 | **BUG** | **Trial copy mismatch.** Pre-convert line says "footer on each page"; done state and actual PDF = small badge bottom-right. Use one line everywhere: "Trial PDFs get a small FreeDailyPro badge in the corner · Go ads-free to remove it". Make both links 44px tall. | Output checked: badge bottom-right on all 4 pages | — | XS | Low |
| 5 | **PROPOSAL (needs Santosh)** | **Done state: full-width 56px "Download PDF (4 pages · 196 KB)" with sub-line "uses 1 trial use"**; "Continue with OCR PDF" becomes a secondary 44px row. | Download 115×36; Download spent a trial 10→9 with no mention | Same as PDF to JPG fix 1 | XS | Med |
| 6 | **PROPOSAL (needs Santosh)** | **44px controls + one buy link.** Orientation/Margin/Fit chips, camera, Clear all, Preview → 44px; Pair toggle 44px hit area. Replace two Quick Buy rows with "Ads-free: $1 day pass · $4.99/month" (keeps monthly beside day pass). Remove duplicate "or tap to choose". | Chips 32px, toggle 24, Quick Buy 28 ×2, camera 36 | Apple/Google 44–48px | XS | Med |
| 7 | **PROPOSAL (needs Santosh)** | **SEO wording:** title "JPG to PDF – Convert Images & Photos to PDF | FreeDailyPro", H1 "JPG / Image to PDF". JSON-LD `offers.price "0"` → remove or list $1 / $4.99 (open "Free" question, same as Split/Rotate/Morse/PDF to JPG). | "JPG" absent from title/H1; price 0 in schema | — | XS | Med |
| 8 | PROPOSAL (needs Santosh) | Capability gaps (never basic): compress-images-in-PDF size option with estimate, "Save to Files/Share" via Web Share API, auto-crop/deskew for document photos (receipt/whiteboard scanner mode), password option, remember last settings. | — | Smallpdf/iLovePDF lack on-device scanner mode | M–L | High |
| S | shared | S1 header 2px overflow (377 at 375). S2 back/home floaters x325 y657. S3 44px targets. **S4 smart ad placement**: exclude auto-ads from the subtitle/tool area (chip moves to content), keep the "Try Office Apps" anchor with the sticky Convert bar offset above it, keep the "Discover more" blocks but in reserved slots below the result and before the footer | — | — | — | — |
| ✔ | OK | Upload/rotate/reorder/page size/convert/download all correct; output 4-page Letter PDF, order + rotation honoured; Convert doesn't spend a trial; badge disclosed before + after; no overflow in done state; 16px inputs; 300+ count; monthly beside day pass; ↑ ↓ ✕ rotate 44px | | | | |

## Mockups
- fix1-ready-sticky-convert-before-after.png (crop1-ready-before.png / crop1-ready-after.png) — after: Convert in fold at 375 (was y1671).
- fix2-file-rows-full-names-before-after.png (crop2-rows-before.png / crop2-rows-after.png).
Mockups are DOM edits in a local headless browser with Google ads blocked; not live code.

## CSS / code sketch (class names illustrative)
```css
/* Fix 2: file row names */
.i2p-row .name{white-space:normal;overflow-wrap:anywhere;font-size:14px;line-height:1.3;min-width:0;flex:1}
.i2p-row .controls{display:grid;grid-template-columns:44px 44px;gap:2px;flex:none} /* rotate, up, down, remove */
/* Fix 1: sticky bar (mobile only) */
@media (max-width:639px){
 .i2p-bar{position:fixed;inset:auto 0 0 0;z-index:50;display:flex;align-items:center;gap:10px;background:#121826;border-top:1px solid #232B3D;padding:10px 16px max(14px,env(safe-area-inset-bottom))}
 .i2p-bar button{min-height:52px;border-radius:12px;padding:0 18px;font-weight:700}
 main{padding-bottom:84px}
 .i2p-dropzone.has-files{display:none} .i2p-add{min-height:48px}
}
/* Fix 6 */
.i2p-chip,.i2p-secondary{min-height:44px}
```
```
# Fix 3 (next.config / middleware)
{ source: '/:lang(es|pt|fr|de|ja|hi|zh|ko|id)?/tool/jpg-to-pdf', destination: '/:lang?/tool/image-to-pdf', permanent: true }
```


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.
