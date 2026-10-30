Sent: 2026-10-30 14:19 ET

# B-0255 PowerPoint Accessibility Checker: report works before the gate; add language/contrast checks and a fixed-file download; brand the title
Priority: P3 · Estimated effort: M · Report: #143 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:16–14:18 ET. L-243: no untested tools remain behind live ApyHub APIs, so alphabetical (first 3 untested). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A teacher or staff member should see every fixable accessibility problem in their deck, per slide, and leave with a fixed file or a clear list.
## Why (repro: t.pptx, 3 slides; 1280 px; 0 trial uses)
- **Works before the gate:** "29.2 KB · 3 slides · 0 problems to fix, 0 items to check, 1 tip", the tip "The file has no document title", and an inline "Document title" box to fix it. Only "Download the report (CSV)" is gated ("0 remaining today · Get a Day Pass to download") — owner's decision.
- Honest limits shown: "cannot judge colour contrast, the quality of alt text, text inside pictures or captions."
- Checks: missing/file-name alt text, missing/empty/repeated slide titles, text under 12 pt, table header row and merged cells, "click here" links, reading order, media, document title.
- **Missing vs competitors (~14:17 ET):** slide-text language (accessibility.build, WCAG 3.1.1); colour contrast for text in solid shapes/tables (Microsoft's built-in checker); WCAG criterion per issue (accessibility.build); Word .docx in the same tool (accessibility.build); a fixed .pptx with the typed alt text/titles written back (the meta says "fix the gaps with your own words"; admin to confirm a fixed file is saved).
- Unnamed controls → B-0155. No overflow at 390 px. Ad text "Compare Browsers" glued to copy → L-004.
## Who uses this
Teachers, university staff and public-sector teams who must publish accessible slides.
## Outcomes (ranked)
1. Confirm, and say on the page, whether fixes are saved into a new .pptx.
2. Add slide-language and solid-shape contrast checks.
3. Show the WCAG criterion with each issue.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**. Site-wide → **B-0209**.
  - Title "PowerPoint Accessibility Checker Online - Alt Text, Free" (56): ends on "Free", no brand.
  - Meta 154 ✔. H1 "PowerPoint Accessibility Checker".
- **Keywords:** "powerpoint accessibility checker", "pptx accessibility check", "check alt text in powerpoint", "accessible slides".
- **Suggested:**
  - Title: `PowerPoint Accessibility Checker – Alt Text | FreeDailyPro` (58)
  - Meta: keep current (154).
  - H1: `Check a PowerPoint for Accessibility Problems`
  - FAQ: "Does it check colour contrast?" → "Not yet; use PowerPoint's own checker." · "Can I fix alt text here?" · "Is my file uploaded?" → "No."
## Constraints
Keep the CSV download gated per the owner's decision.
## Test cases
1. Deck with an image without alt text → 1 problem listed on its slide.
2. Admin: type a document title → downloaded .pptx (if offered) has it in docProps/core.xml.
3. Title ≤ 60, no "Free".
