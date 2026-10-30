Sent: 2026-10-30 13:47 ET

# B-0228 Find & Replace SEO: trim the 64-char title, take 'Free' out of it, and write a real meta
Priority: P2 · Estimated effort: S · Report: #134 · Source: curl server HTML (seo.py) + Google top 5 (WebSearch), 2026-10-30 ~13:46–13:47 ET; GA/GSC from analytics/2026-07-10-to-now-raw.md

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People who search for find and replace, especially in a Word file, should see in the result that we change their .docx in place, keep its formatting, and never upload it.
## Why
- GA: /tool/find-replace has 112 views since Jul 10 (#15 page). GSC: 2 clicks / 24 impressions, 8.3% CTR, position 26.6.
- In a live Google search (~13:47 ET), our page ranks **#1** for "find and replace text online regex docx". The snippet is strong there, so the title and meta are what decide the click.
- Tool issue tracked separately: L-139 (.docx stored uncompressed, B-0076).
- Top results:
  - Toolulah: batch up to 100 files, rule lists, CSV of rules, preview before replace, headers and footnotes.
  - iXam: batch, body + headers + footers + comments, a replacement log CSV.
  - Aspose, GroupDocs: upload-based, with regex.
## Who uses this
Writers renaming a character, admins updating a company name across a document, developers editing JSON or CSV.
## Outcomes (ranked)
1. A title of 60 chars or fewer, keyword first, without "Free".
2. A 140–160 char meta that names .docx, regex and "formatting kept".
3. An H1 that says "Find and Replace".
4. A capability gap (separate brief if prioritised): .docx headers, footers and footnotes are not edited (the page states this), and there's no multi-rule or batch mode.
## SEO
- **Now:** Passes: 200, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (template and footer H2s, 1 video image with no alt) → **B-0209**. **/es serves the English title** → **B-0123**.
  - **Title "Find and Replace Text Online - Free, .docx & More | FreeDailyPro" is 64, over 60, with "Free".**
  - **Meta 79** ("…Free and fast, right in your browser." boilerplate).
  - H1 "Find & Replace".
  - og-default image.
- **Best result:** our own body copy is the best on the page 1 (limits stated honestly). Toolulah's rule table and preview are the feature bar.
- **Keywords:** "find and replace", "find and replace in word document online", "regex replace online", "bulk replace text".
- **Suggested:**
  - Title: `Find and Replace Text Online – .docx & Regex | FreeDailyPro` (59)
  - Meta: `Find and replace text in pasted text or a .docx, .txt, .csv, .json or .md file, with regex, case and whole-word options. Word formatting is kept. No upload.` (156)
  - H1: `Find and Replace Text – Including Word Files`
  - FAQ:
    - "Can I find and replace in a Word document?" → "Yes. Drop the .docx; formatting is kept."
    - "Does it support regex?" → "Yes, JavaScript syntax, with $1 groups."
    - "Are headers and footnotes changed?" → "Not yet; only the main body."
    - "Is my file uploaded?" → "No."
## Constraints
Keep the honest limits section; don't drop the #1 snippet copy.
## Test cases
1. The title is 60 chars or fewer with no "Free".
2. The meta is 140–160 chars.
3. GSC 28-day recheck: position and CTR.
