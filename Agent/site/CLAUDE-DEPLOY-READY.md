# Claude — posts ready for freedailypro.com import

**Updated:** 2026-10-15 (B015–B021 added)  
**Rules:** `site-blog-pack/` on main

## READY for import (all under Agent/site/)

### Job A COMPLETE (REPLACE)
| Batch | Folder | Rows |
|-------|--------|------|
| R001–R007 | [rewrite-20261015](https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261015) | resume-builder, random-number-generator, image-to-pdf, document-scanner, remove-background, screenshot-tool, binary-ascii-converter |
| R008–R015 | [rewrite-20261015b](https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261015b) | shipping-cost-estimator, cost-of-living-comparison, text-similarity-checker, diff-checker, audio-comparer, college-529-calculator, csv-converter, markdown-html-converter |

### Job B NEW posts
| Batch | Folder | Rows |
|-------|--------|------|
| B001–B007 | [rewrite-20261016](https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016) | rotate-pdf, slug-generator, receipt-maker, yt-thumbnail, mesh-3d-viewer, rmd-calculator, profit-margin |
| B015–B021 | [rewrite-20261016c](https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016c) | favicon, teachers worksheets, event packs, local QR, fillable forms, ascii banners, NDA |
| B008–B014 | [rewrite-20261016b](https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016b) | citation-generator, hashtag-generator, travel-packing-list, heic→convert-image, json-formatter, percentage-calculator, video-to-gif |

Each folder: `posts/<slug>.md`, `images/<slug>.webp` (1200×630, bottom stripe, <150KB), `INDEX.md`.

## Still in progress (Grok continuing, no owner action needed)
- Job B B022–B062
- Job C legacy 74 upgrades  
- Job D tools with no post yet

## Import notes for Claude
- Mode REPLACE: keep existing URL/date; replace body+image from these files.
- Mode NEW: use frontmatter `date` for schedule.
- Validator rules from site-blog-pack already applied (no free in titles, no AI, 10 trial usages, 200+ tools, contact close).
- Tool id fixes already applied (convert-image not heic-to-jpg; video-to-gif not gif-maker).
