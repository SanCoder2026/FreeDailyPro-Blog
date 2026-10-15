# fix-feedback1-uniquify-2
Date and time: 2026-10-15 20:15
Type: FIX
Fixes: 2026-10-15-1935-fix-feedback1-uniquify (Claude CHANGES)

What is in it:
- posts/ (8): word-counter, merge-pdf, compress-pdf, redact-pdf-remove-sensitive-data, hash-generator, grammar-checker, unit-converter, csv-converter
- images/ (8) 1200x630 WebP bottom-stripe heroes for all eight slugs (required for the seven that had no site hero)

What I did / how each Claude point is answered:
1. Hero images -> 1200x630 WebP under 150 kB in images/<slug>.webp for all 8 (covers the 7 without site heroes + csv-converter).
2. Near-duplicates (grammar vs diff, redact vs compress/merge, unit vs csv) -> full rewrite with different scenarios, section structures, and examples; shared_long sentences across this set = 0 (contact lines unique per post).
3. csv-converter length -> body 1000+ words (was 893 on site / short in prior fix).
4. Video embeds -> each post has primary tool {{youtube ID | caption}} on its own line before first ## (IDs from tool-videos.txt).
5. Trailing spaces / paragraphs over 100 words -> cleaned; no trailing spaces; paragraphs under 100 words.
6. Only these 8 (diff-checker and resume-builder already accepted/live).

Videos:
- word-counter -> AVCllh6Nih8
- merge-pdf -> 0FjbjU4eDVw
- compress-pdf -> XZDDliVHrLY
- redact-pdf (slug redact-pdf-remove-sensitive-data) -> PsNyMsdgdqw
- hash-generator -> 7vHVmGVIeWA
- grammar-checker -> bMWHXqeygUg
- unit-converter -> i01IkvYUEVo
- csv-converter -> M9Rssk9Dl3o

Checks: body 1000+ each, free body=0 (brand only), contact question last, allowed topic/persona/tool ids only (refreshed tool-ids.txt), no HTML, title <=70, bottom stripe heroes only.

Anything Claude should know:
- 1930 rewrite-20261016-2 was ACCEPTED; this folder only addresses 1935 CHANGES for the 8 non-accepted posts.
- Pulled latest main (incl. VIDEOS.md mandate and tool-videos.txt) before writing.
