Sent: 2026-11-20 08:40 ET

# Split PDF: desk findings (no trial uses)

Written: 2026-11-19 11:38 EST. Captured 2026-11-19, about 11:10–11:40 EST.

## Method

- Read-only curl of these pages, with captures in this folder:
  - the tool page (`tool.html`, `tool-visible.txt`, `headers-tool.txt`)
  - 10 locale variants (`html/tool-<locale>.html` in this zip)
  - the blog post
  - sitemap.xml
- The JS bundles in `js/`.
- YouTube metadata, captions and frames (see video-findings.md).
- WebSearch.
- GSC data is not available.

## Page metadata

| Item | Value | Note |
|---|---|---|
| URL | https://www.freedailypro.com/tool/split-pdf | 200 |
| Title | "Split PDF by Page Range or Every Page - Private, On-Device" | No "\| FreeDailyPro" brand suffix (P2). |
| Meta description | 137 chars, mentions "10 trial uses a day" | OK |
| H1 | "Split PDF" | Short. The keyword variants ("by page range", "extract pages") are only in the title (P2). |
| Canonical | self | OK |
| hreflang | 11 | The locale problems are in the next section. |
| og:image | og-default | Generic; there is no tool-specific social card (P2). |
| JSON-LD | SoftwareApplication (Offer 4.99 USD, no billing period), VideoObject (uploadDate 2026-10-16), FAQPage (9 Q), BreadcrumbList Home › PDF Tools › Split PDF | The Offer should say per month (P2). |
| Images | 1 empty alt | Low |

## Locales (server HTML, curl)

| Locale | HTTP | Title / H1 / meta | Canonical |
|---|---|---|---|
| es, pt, fr, de, ja, hi, zh, ko, id | 200 | **English** title, H1 and meta on all 9 | self (e.g. /es/tool/split-pdf) |
| ar | **404** | "Page not found" | — |

- Nine self-canonical locale URLs serve the same English head. This is a duplicate-content and thin-localization risk.
- Unlike compress-pdf, /es is **not** localized here either.
- The client-rendered UI per locale is covered in devices-locales-findings.md.
- Severity P1, shared with the other tools.

## Sitemap

- The <url> entry has lastmod 2026-11-19 and a video block.
  - video title "How to Split a PDF into Separate Files with Split PDF | FreeDailyPro"
  - publication_date 2026-10-16
- These match the JSON-LD VideoObject. OK.

## Copy accuracy on the tool page (live-verified against the UI)

1. **Limitations contradicts the FAQ and the live behaviour (P1).**
   - Limitations says: "Password-protected PDFs need their password removed first, same as with merging."
   - The FAQ says: "you'll be asked for it as soon as you add the file … unlocked right in your browser."
   - Live: a password dialog appears, and the right password unlocks the file inline (SP-24).
2. **The Details / "How to use" copy is generic and partly inaccurate (P1).**
   - It says "you *typically* have two ways…", "checkboxes on thumbnails, or a text field" and "often as a zip archive".
   - Live: the thumbnails are plain `<img alt="Page N">`. They are not buttons or checkboxes, and clicking one changes nothing (kbd.json `thumbClick`).
   - It reads like template text, not a description of this tool.
3. "About" is accurate: ranges, Every page, Combine into one reordered PDF, ZIP for several files.
4. The open-ended range "8-" works (pages 8–10), and so do en dashes and semicolons. None of this is documented; documenting it would be a cheap win (P2).
5. **UI vs API range syntax differs (desk only, the API is not tested).**
   - The RapidAPI listing says commas join pages into one output and semicolons start a new file.
   - In the web UI, commas start a new file ("1-3, 5" gives 2 files).
   - Users who move from the UI to the API may get different results. This is a docs observation only (P2).

## Blog

- Post: /blog/split-pdf-multi-contract-client-packets, dated 2026-10-17, with the video embedded. /blog/split-pdf returns 404 (that's fine; it's not linked anywhere I saw).
- **The tool page does not link to its own post (P1).**
  - It has 0 references to /blog/split-pdf-multi-contract-client-packets.
  - It links to /blog/delete-unwanted-pages-from-pdf and /blog/pdf-to-excel instead.
- **The blog describes a feature that doesn't exist (P1).**
  - Its steps say "Enter range 1–12, name the output something like ClientA-purchase-2026-10-22.pdf", and the same for the other ranges.
  - Live: there is no per-range name field. The only text input in the result view is the range field, and the outputs are auto-named `<name>-pages-1-3.pdf`.
- **The blog's trial wording is misleading (P2).**
  - It says "Stay within your daily allowance of 10 trial usages if you are testing ranges".
  - Live: splitting (testing ranges) works at 0 remaining; only Download is gated. It also says "usages" instead of "uses".
- The en-dash range in the blog ("1–12") is accepted by the tool (ranges-rows.json). Good.

## Competitors (WebSearch, 2026-11-19)

- Browser-only splitters such as FormatDesk, HerePDF and SplitPDF.io also offer:
  - **by bookmarks** (one file per chapter, named after the bookmark)
  - **by file size** (e.g. parts under 10 MB for email)
  - **odd/even**
  - tap-to-select pages, or "tear" marks between thumbnails
- Smallpdf and iLovePDF offer ranges and extraction (server upload).
- FreeDailyPro already keeps bookmarks and form fields (per its UI). It is the only one seen that says up front which files will carry a mark.
- **Biggest gaps:** split-by-bookmarks and split-by-size. They fit the blog's use case (one packet per client, email-sized parts). P2 roadmap item.
- **Indexing:** "freedailypro split pdf" returns the tool page first. The snippet shows the inaccurate Details and Limitations text.
