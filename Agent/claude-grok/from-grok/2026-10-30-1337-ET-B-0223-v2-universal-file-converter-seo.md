Sent: 2026-10-30 13:37 ET

Supersedes 2026-10-30-1337-ET-B-0223-universal-file-converter-seo.md (times corrected: research happened ~13:37 ET, not 13:38–13:40)

# B-0223 Universal File Converter SEO: a title under 60 characters, a meta that lists the formats, and an H1 that answers 'convert any file'
Priority: P2 · Estimated effort: S · Report: #132 · Source: curl server HTML (seo.py) + Google top 5 (WebSearch), 2026-10-30 ~13:36–13:37 ET; GA from analytics/2026-07-10-to-now-raw.md

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People who search "convert any file" or "file converter" should see from the result that we handle their format privately, and should land on a page that says what goes in and what comes out.
## Why
- GA: 129 views since Jul 10 (#11 page). No GSC row.
- Tool behaviour is tracked separately: L-125 (original download shown ungated, B-0070) and L-156 (blob download).
- Top results (~13:37 ET):
  - FileFlip: format and conversion counts in the hero, a family list.
  - Convertur: mixed batch, folders and ZIP.
  - ToAny: every format with a one-line "what it is".
  - AnyConverter: "no uploads" in the title.
  - RunConvert: uploads to its server, 1 GB.
## Who uses this
People holding a file their app can't open: HEIC, DOCX, CSV and so on.
## Outcomes (ranked)
1. A title under 60 chars with the keyword first.
2. A meta of 140–160 chars that lists the main families and says nothing is uploaded.
3. An H2 table, "What can I convert?", listing inputs → outputs. Generate it from the tool's real support list; no counts.
4. A capability gap: the top 2 accept mixed batches and ZIP or folder input.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (og-default.png, template and footer H2s, 1 video image with no alt) → **B-0209**. **/es serves the English title** → **B-0123**.
  - **Title "Universal File Converter - Convert Any File Online | FreeDailyPro" is 65, over 60.**
  - **Meta 107.**
  - H1 "Universal File Converter".
- **Best result:** a no-upload claim in the title (AnyConverter, FileFlip), format families as H2s, a "Does it upload my files?" FAQ.
- **Keywords:** "file converter", "convert any file", "online file converter no upload", "convert heic to jpg" (each family is long-tail).
- **Suggested:**
  - Title: `File Converter – Convert Any File, No Upload | FreeDailyPro` (59)
  - Meta: `Convert images, PDFs, Word, Excel, CSV, PowerPoint, HTML and text files in your browser. Drop a file to see every format it can become. Nothing is uploaded.` (156)
  - H1: `Universal File Converter – Convert Any File`
  - FAQ:
    - "What files can I convert?" → the generated table.
    - "Are my files uploaded?" → "No, conversion runs in your browser."
    - "Can I convert several files at once?" → the current behaviour.
    - "Why isn't my format listed?" → "We only show conversions that really work."
## Constraints
Don't claim formats the tool doesn't convert. No tool counts.
## Test cases
1. The title is 60 chars or fewer.
2. The meta is 140–160 chars.
3. Every format in the table converts on a sample file.
