# Review of 2026-10-15-1935-fix-feedback1-uniquify

Reviewed 2026-10-15. PARTLY ACCEPTED.

## Accepted and live (replaced the old versions)
- diff-checker
- resume-builder
I added the tool video to both (new rule, see VIDEOS.md).

## Not accepted, 8 posts: fix and send a new folder `YYYY-MM-DD-HHMM-fix-feedback1-uniquify-2`
Important: only diff-checker, resume-builder and csv-converter already exist on the site. The other 7 (word-counter, merge-pdf, compress-pdf, redact-pdf-remove-sensitive-data, hash-generator, grammar-checker, unit-converter) have no post and no hero image on the site, and you sent no images. A post without a hero is rejected.

1. Hero images: send a 1200x630 WebP (under 150 kB) in `images/<slug>.webp` for each of those 7, as you do for new posts.
2. Near-duplicates (the site rejects over 30% shared wording between posts):
   - grammar-checker vs diff-checker: 32%
   - redact-pdf-remove-sensitive-data vs compress-pdf (30%) and merge-pdf (33%)
   - unit-converter vs csv-converter: 32%
   Rewrite the overlapping parts with different scenarios, examples and section content. Different structure, not just different words.
3. csv-converter is 893 words; the site needs 900+, you need 1000+.
4. Frontmatter/embeds: add `{{youtube ID | caption}}` for the primary tool (ids in `site-blog-pack/tool-videos.txt`). Required now.
5. Trailing double spaces and paragraphs over 100 words in all 10: fix them.
6. Check before pushing: send only posts that are new slugs or exact replacements of existing slugs, and run the site's rules checklist.
