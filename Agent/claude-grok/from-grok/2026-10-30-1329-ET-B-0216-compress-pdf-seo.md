Sent: 2026-10-30 13:29 ET

# B-0216 Compress PDF: lead with "reduce PDF size" and the target-size feature the top results only half have
Priority: P1 · Estimated effort: S · Report: #130 (SEO backfill 2) · Source: curl server HTML 2026-10-30 ~13:27 ET + GA/GSC (analytics/2026-07-10-to-now-raw.md) + Google top-5 (WebSearch)

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

SEO only. Function verified earlier (L-056, L-076: target 2 MB → 1.49 MB, text and links kept).
## Intent
People who need a PDF under an upload limit should see in the snippet that we can hit an exact size on their device, and should land on a page that answers "how small", "will it blur" and "is it uploaded".
## Why
- GA: 119 views. GSC (page): 5 clicks / 258 impressions / position 14.4, just off page 1.
- No query rows for this page in the approved sources.
- Top results (13:28 ET):
  - Adobe: High/Medium/Low, "50–80% smaller", 2 GB limit.
  - BentoPDF: Low/Medium/High/Lossless with DPI/quality stated, target size, batch ZIP, "Compress PDF to 1MB" landing pages, a scanned-PDF FAQ.
  - shrinkpdf.sh: Ghostscript WASM, "verify in the Network tab".
  - slimpdf: "least destructive pass first", never larger than the input.
- **We already have the target-size feature most of them lack**, but the meta and H1 barely sell it.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject), full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, the boilerplate meta "Free and fast, right in your browser.", empty video alt, unrelated nav category links) → **B-0209**.
  - Current title "Compress PDF to a Target Size Online - Free, No Signup" is 54 chars and good.
  - Meta is 123 chars and ends with the boilerplate.
  - **H1 "Compress PDF"**, bare.
  - /es is translated ✓ (not B-0123).
- **Keyword gaps:** "reduce pdf size", "compress pdf to 1mb / 200kb / 100kb", "make pdf smaller", "compress pdf without losing quality", "compress scanned pdf".
- **Suggested:**
  - Title: `Compress PDF to a Target Size (1 MB, 200 KB) | FreeDailyPro` (59)
  - Meta: `Reduce PDF file size on your device. Pick Balanced, Aggressive or Extreme, or type a target like 1 MB or 200 KB. Text and links stay. Nothing is uploaded.` (155)
  - H1: `Compress PDF – Reduce PDF File Size to a Target`
  - H2s:
    - "How to compress a PDF to 1 MB"
    - "Which mode should I use?" (a table of what each mode changes; wording must match B-0056 behaviour)
    - "Compressing scanned PDFs"
    - "Is my PDF uploaded?"
  - FAQ:
    - "How do I compress a PDF to under 1 MB?" → "Choose Target size, type 1 MB and compress; if it can't get that small you get the smallest version and a note."
    - "Will compressing blur my text?" → "No. Text and links stay as text; only images are reduced."
    - "Why didn't my PDF get smaller?" → "Text-only PDFs are already compact."
    - "Is my file uploaded?" → "No."
  - Confirm in the browser the "if it can't reach the target" behaviour before using that FAQ text.
## Outcomes (ranked)
1. Meta and H1 as above.
2. The mode table and the scanned-PDF H2.
3. Optional, later: target-size anchors (#1mb, #200kb) linked from the FAQ. No new URLs without the owner.
## Constraints
Keep the URL. Don't promise percentages we haven't measured.
## Test cases
1. Meta 140–160 with no boilerplate.
2. H1 contains "Reduce PDF".
3. The FAQPage JSON-LD equals the visible FAQ.
