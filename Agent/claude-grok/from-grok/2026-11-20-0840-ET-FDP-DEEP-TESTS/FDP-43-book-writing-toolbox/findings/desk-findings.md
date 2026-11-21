Sent: 2026-11-21 05:21 ET

# FDP-43 Book Writing Toolbox: desk findings (2026-11-21 EST)

## SEO and indexing
- Title "Write & Format a Book Online - KDP Ready | FreeDailyPro" (59 characters); meta 134 characters; canonical self; 10 hreflang + x-default; one H1.
- JSON-LD: SoftwareApplication with Offer $29.99/month (UnitPriceSpecification), VideoObject, FAQPage (9), BreadcrumbList (Home › Workflow Products).
- P3:
  - **OG image is `/blog/book-maker-launch.webp`** (the old "Book Maker" name).
  - VideoObject name "How to Make a Complete Book from Chapters PDF Word Online" (2026-09-22) describes the old tool.
- Locales /es /pt /fr /de /ja /hi /zh /ko /id: all 200, but the title and meta stay English.
  - P3: the translated **H1s translate the old name "Book Maker"** ("Creador de Libros", "Buch-Ersteller", "बुक मेकर", "图书制作工具" and so on), not "Book Writing Toolbox".
  - /ar returns 404. Price shows $29.99 in every locale and geo.
- Site placement (SITE-MAP): this is one of 2 of 11 Workflow Products not listed on its category page (Publishing & Print Makers). The blog says "The rest of the group sits under PDF tools". P3: list it on /category/publishing-tools.

## Copy accuracy
1. **P2:** the FAQ and Limitations say Bengali, Tamil, Telugu, Gujarati, Kannada and Malayalam are "not available in PDFs yet", but the live checker message says they are supported. One must be updated (the code says supported).
2. **P1 (copy vs behaviour):** "Previews are unlimited", "Preview is unlimited (watermarked)" and "ONIX … no subscription needed" are contradicted by the Professional trial-use charge and the silent block at 0 (live findings 2–3).
3. "Pre-flight … builds a real EPUB to check its actual file size and accessibility": the EPUB build fails, and Pre-flight drops those checks without saying so.
4. Blog `/blog/book-writing-toolbox` (Oct 25, 2026) is accurate on import splitting, front/back matter, pre-flight checks, the print-cover formula and the sign-in reason.
   - Minor: the lead says export happens "from the browser", while the body correctly says the server typesets.
   - Minor: "The rest of the group sits under PDF tools".
5. Page header "Draft stays in your browser" / "Preview and export use our server" is accurate.

## Code notes
- `BookMaker-0ysxrwOr.js`:
  - Download `Fi` needs sign-in (`s`) and an entitlement (`de`) or credits (`J`), otherwise the subscribe dialog `V(!0)`.
  - Previews call `bookMaker.render* {preview:true}`; manuscript/EPUB/ONIX files are saved with `bt` = ToolPage export `d` (`vt`), which runs the Professional usage wrapper `Sa` unless `{free:true}`. That is why previews charge per page load and go silent at 0.
  - The client chooses `preview: !1` on Download. The server must enforce the entitlement; that's untested here (no API testing).
- `index-B1CTyGtY.js` `Ps["book-writing-toolbox"] = ["gated","desk","Workflow Product (project desk); has its own pricing and rules"]`.
- `BookProjectBar`: the project file is metadata only (`fdp-book-project`, sessionStorage + .book.json).

## Duplicates (C38) and placement
- C38: book-interior-maker, manuscript-formatter, epub-maker, copyright-page-maker (Premium Applications); epub-checker, low-content-interior-maker (Professional Tools); print-publication-studio (Workflow).
- The Toolbox already contains manuscript-formatter, epub-maker and copyright-page and interior features.
- Suggestion: keep the Premium Applications, but cross-link each one to the Toolbox as the "whole book" path, and say on each which plan covers what. The Toolbox isn't covered by the Premium plan, and that's easy to miss.
- No removal.
