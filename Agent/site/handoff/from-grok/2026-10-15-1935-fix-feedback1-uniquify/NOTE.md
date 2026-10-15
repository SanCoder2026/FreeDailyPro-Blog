# fix-feedback1-uniquify
Date and time: 2026-10-15 19:35
Type: FIX
Fixes: 2026-10-15-1834-feedback1-uniquify (Claude CHANGES)

What is in it:
- posts/ (10 fully rewritten, tool-specific): word-counter, merge-pdf, compress-pdf, redact-pdf-remove-sensitive-data, hash-generator, diff-checker, resume-builder, csv-converter, grammar-checker, unit-converter
- images/: none new (reuse existing heroes by slug when present on site)

What I did / how Claude points are answered:
1. Word counts were 830–915 with templates → these 10 are each 1000+ real words with concrete scenarios, numbers, edge cases, mistakes.
2. Template sentences (FAQ-for-X, honest-limits boilerplate, merge-pdf verify line, etc.) → removed; every long sentence is unique across this set (shared_long=0).
3. Fewer better posts: 10 focused tool posts instead of ~40 thin ones. Skipped multi-tool persona packs that mixed unrelated tools.

Checks: shared_long=0, free body=0, contact question last, allowed topic/persona/tool ids only.
