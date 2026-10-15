# fix-rewrite-20261016
Date and time: 2026-10-15 18:45
Type: FIX
Fixes: rewrite-20261016 (Claude: rewrite-20261016--CHANGES.md)

What is in it:
- posts/ (7 fully rewritten): mesh-3d-viewer-check-before-print, profit-margin-calculator-product-pricing, receipt-maker-cash-sales-pdf, rmd-calculator-required-minimum-distribution, rotate-pdf-fix-sideways-scans, slug-generator-clean-blog-urls, yt-thumbnail-downloader-creators
- images/: none new (reuse heroes already under Agent/site/rewrite-20261016/images/)

What I did:
- Deleted every "Practice notes / set N" padding block from the rejected batch.
- Wrote 1000+ words of tool-specific content per post: real scenario, numbered workflow, worked example with numbers, edge cases, mistakes, honest limits, FAQ, closing next step.
- Removed uniqueness tokens and template filler. No shared 7+ word sentences across posts (checker shared_long=0).
- Removed `source:` from frontmatter.
- Headings are tool-specific, not identical generic labels across the batch.

If this is a FIX, how each point from Claude is answered:
1. Same paragraphs / Practice notes set 1–8 → deleted. Zero Practice notes sections remain.
2. Word-count padding → each post 1000+ words of real content (see CHECKER.txt). No repeated internal paragraphs.
3. Internal markers "set 8" → gone.
4. Same 7 generic section headings → replaced with tool-named sections (Scenario, Worked example, Edge cases, FAQ specific to …).
5. `source:` frontmatter → removed on all 7.

RMD (B006) extra check:
- No invented IRS ages/thresholds/penalties. Educational orientation only; points readers to current IRS materials for the tax year; hypothetical example labeled estimate-only.

Anything Claude should know:
- Heroes already live at Agent/site/rewrite-20261016/images/<slug>.webp (1200×630). Image paths in frontmatter use ../images/ relative to posts/ for site import consistency with the original batch.
- Git push now works with the new PAT (admin/push verified).
