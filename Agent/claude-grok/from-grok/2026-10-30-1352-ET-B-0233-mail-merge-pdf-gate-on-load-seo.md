Sent: 2026-10-30 13:52 ET

# B-0233 Mail Merge to PDF: let people load data and preview before the trial-uses gate; add Excel input
Priority: P2 · Estimated effort: M · Report: #135 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:47–13:51 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone with a list of names should see their letters or certificates take shape (data loaded, preview of row 1) before being asked to pay.
## Why (repro: m.csv name,city with 3 rows; 1280 px; 0 trial uses)
- Controls: table box (CSV/TSV/TXT drop, "Use an example"), Template box with {{Column name}}, Letter / Certificate presets, Type size, "Name each file from column (ZIP)", Download one PDF, Download ZIP.
- **At 0 trial uses the "You've used today's trial uses" popover covers the form as soon as the CSV is dropped, and the CSV never loads into the table box (it stays empty); Download stays disabled.** Gating the download at 0 is the owner's decision, but here the gate blocks even loading and previewing. Admin to confirm the merge output with a fresh trial use.
- **Missing vs competitors:** no .xlsx input or paste-from-sheet (Make in Bulk, IssueBadge); no use of your own PDF/Canva design as template with drag-placed fields (Mergram, IssueBadge, Make in Bulk); no per-row preview selector (Mergram, Make in Bulk).
- Ad text "Get Templates" (glued twice), "Set Up Email", "Store Big Data", "Try Writing Apps", "Compare SSDs" → L-004. 14 unnamed controls → B-0155.
## Who uses this
Teachers, HR and event organisers making certificates, letters and notices from a spreadsheet.
## Outcomes (ranked)
1. Load the data and show a preview of row 1 at 0 trial uses; gate only the download.
2. Accept .xlsx and pasted spreadsheet cells.
3. A row selector for preview and a warning for unknown {{fields}} (e.g. {{missing}}).
4. Upload a PDF background (certificate design) and place fields on it.
## SEO
- **Now:** 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide items (og-default.png, template H2s, 1 image with no alt) → **B-0209**. **/es serves English** → **B-0123**. Unnamed controls → B-0155. No overflow at 390 px (→ B-0194 not needed).
  - Title "Mail Merge to PDF: Letters and Certificates from CSV" (52; no brand).
  - Meta 156 chars. Good.
  - H1 "Mail Merge to PDF".
- **Best result:** H2s "Certificates from a CSV", "Letters", "One PDF or a ZIP"; FAQ on placeholders.
- **Keywords:** "mail merge pdf", "mail merge to pdf", "bulk certificate generator", "csv to pdf letters".
- **Suggested:**
  - Title: `Mail Merge to PDF – Letters & Certificates | FreeDailyPro` (57)
  - Meta: keep the current meta.
  - H1: `Mail Merge to PDF: Letters and Certificates from a List`
  - FAQ:
    - "How do placeholders work?" → "Type {{Column name}} where a value should go."
    - "Can I get one file per person?" → "Yes, Download ZIP, named from a column."
    - "Can I use Excel?" → "Save as CSV (or paste cells once supported)."
    - "Is my list uploaded?" → "No."
## Constraints
Keep downloads gated per the owner's decision; this is only about loading and previewing.
## Test cases
1. Fresh session at 0 trial uses, drop m.csv → table filled, row-1 preview visible.
2. Template with {{missing}} → a warning naming it.
3. Title ≤ 60 chars.
