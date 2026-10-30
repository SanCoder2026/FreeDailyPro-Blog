Sent: 2026-10-30 13:47 ET

# B-0229 Book Writing Toolbox SEO: an H1 people search for, a meta that names KDP, EPUB and PDF, and the old book-maker URL handled cleanly
Priority: P2 · Estimated effort: S · Report: #134 · Source: curl server HTML (seo.py) + Google top 5 (WebSearch), 2026-10-30 ~13:46–13:47 ET; GA/GSC from analytics/2026-07-10-to-now-raw.md

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Authors who search "write a book online" or "format a book for KDP" should land on a page that says plainly: write here, see real typesetting, export files Amazon accepts.
## Why
- GA (Jul 10–now): /tool/book-maker had 106 views (#16) and /tool/book-writing-toolbox 79 (#20). /tool/book-maker now **301s** to /tool/book-writing-toolbox, so this one page carries both.
- book-maker is correctly out of the sitemap ✓. The OG image is a real blog image (book-maker-launch.webp, 200) ✓, not og-default.
- Tool issues tracked separately: L-175 (DOCX import flattens a table and drops an image, P1), L-176, L-177 (ads overlay buttons). The Book preview watermark is by design.
- Top results (~13:47 ET):
  - Reedsy Studio: free, auto front matter and table of contents, trim sizes, EPUB 3 + PDF/X-1a, needs an account.
  - bookformatter.app: Word/Markdown in, EPUB 3 + KDP print PDF out, 8 designs, no upload.
  - KDP: Kindle Create, manuscript templates.
## Who uses this
First-time self-publishers writing a novel, memoir or workbook for Amazon KDP.
## Outcomes (ranked)
1. An H1 with the keyword phrase ("Write and Format a Book…") instead of the internal name.
2. A 140–160 char meta naming the KDP-ready exports (state only formats the tool really exports; admin to confirm EPUB).
3. H2s that answer: "Is it KDP-ready?", "Which trim sizes?", "Can I import my Word manuscript?"
4. Keep the 301; make sure internal links point to the new URL, not book-maker.
## SEO
- **Now:** Passes: 200, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (template and footer H2s, 1 video image with no alt) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Write & Format a Book Online - KDP Ready | FreeDailyPro" (55, good).
  - **Meta 134** (under 140).
  - H1 "Book Writing Toolbox" (no search intent).
- **Best result:** bookformatter.app: "Your manuscript, typeset like a real book", in/out formats listed in the hero, a 3-step flow, a "Does my manuscript get uploaded?" FAQ.
- **Keywords:** "write a book online", "book formatting software free", "format book for kdp", "kdp manuscript template".
- **Suggested:**
  - Title: `Write & Format a Book Online – KDP Ready | FreeDailyPro` (55)
  - Meta: `Write your book in a real editor, see it typeset as you go, and export a KDP-ready print PDF. Pick a trim size, add chapters and front matter. No install.` (154)
  - H1: `Write and Format Your Book for KDP`
  - FAQ:
    - "Is the PDF ready for Amazon KDP?" → state the trim sizes and margins used.
    - "Can I import my Word manuscript?" → "Yes, but tables and images may need re-adding" (until L-175 is fixed).
    - "Do I need an account?" → state the current behaviour.
    - "Is there a watermark?" → "The preview is watermarked; the paid download is clean."
## Constraints
Name only real export formats. Don't hide the preview watermark.
## Test cases
1. The H1 contains "Book", "Write" and "Format"/"KDP".
2. The meta is 140–160 chars.
3. /tool/book-maker → one 301 to the new URL; no internal links to book-maker.
