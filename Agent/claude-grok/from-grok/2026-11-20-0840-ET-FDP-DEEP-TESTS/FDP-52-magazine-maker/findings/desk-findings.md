Sent: 2026-11-21 09:19 ET

# Desk findings

- **Copy:** About + 14 FAQs + Details are detailed and mostly match the live tool:
  - The 60-character TOC trim, Markdown, emoji note, columns/templates/contents styles, the US Letter-only Combine, privacy (fonts from its own domain), and "trial use taken at download; same build again is free".
- **Mismatch:** "What file types does Combine files take? … PNG, JPEG, WebP or HEIC … The warning message mentions only PNG and JPEG, but the file picker also accepts WebP and HEIC." Live, WebP is rejected at assembly. The FAQ is documenting a known bug instead of the fix.
- **JSON-LD:** WebSite, SoftwareApplication, VideoObject ("How to Make a Magazine PDF Online – Cover, TOC & Articles", which differs from the YouTube title), FAQPage (14), BreadcrumbList (Home > Premium Applications > Magazine Maker).
- **SEO:** title "Magazine Maker - Design a Magazine PDF Online | FreeDailyPro" (60), meta 158 chars, canonical self, index, hreflang 10 + x-default, og-default.png.
- **Blog /blog/assemble-magazine-or-newsletter-pdf-with-toc** (Oct 24, 2026):
  - Accurate on the TOC, masthead, contributors, List of Images, titles as TOC entries, and the page count on the download button.
  - Inaccurate: "Upload the cover image" in the file-assembly flow (Combine has no cover image).
  - Unverified: "drag them into reading order" (the UI and FAQ describe arrow buttons).
  - It also describes only the Combine mode, not Write articles.
- **Blog /blog/edition-ledger…** (Nov 10, 2026): about Print & Publication Studio. It describes Magazine Maker correctly as one of the page makers it wraps.
- **Code:**
  - `logExportNow(key)` with a content hash per export (`Pe({articles, opts})`).
  - The Combine `accept` includes webp/heic.
  - Saved issue format v1, max 200 articles, accent `#rrggbb`.
- **Category:** Publishing & Print Makers (listed there and on Premium Applications). C40 ladder: catalog-maker → print-publication-studio.
