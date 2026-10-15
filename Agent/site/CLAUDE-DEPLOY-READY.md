# Claude — posts ready for freedailypro.com import

**Updated:** 2026-10-15  
**Rules pack:** `site-blog-pack/` on main  
**Owner action:** Import READY folders below into the site; Grok continues Job C/D.

## READY for import

### Job A COMPLETE (REPLACE mode — same slug)
| Rows | Folder |
|------|--------|
| R001–R007 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261015 |
| R008–R015 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261015b |

### Job B COMPLETE (NEW mode — plan B001–B062)
| Rows | Folder |
|------|--------|
| B001–B007 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016 |
| B008–B014 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016b |
| B015–B021 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016c |
| B022–B028 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016d |
| B029–B045 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016e |
| B046–B062 | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261016f |

Each folder contains `posts/<slug>.md`, `images/<slug>.webp` (1200×630, bottom stripe, <150KB), `INDEX.md`.

## Import notes
- REPLACE: keep URL + original date; swap body + hero from these files.
- NEW: use frontmatter `date` for schedule.
- Messaging already applied: 200+ professional tools, 10 trial usages, no AI mentions, avoid “free” in titles/body (brand name OK).
- Tool ids from `site-blog-pack/tool-ids.txt` (fixes: convert-image, video-to-gif, qr-generator, trim-video, compress-video, sign-pdf).
- Last paragraph → contact form question.

### Job C STARTED (REPLACE legacy)
| Batch | Folder |
|-------|--------|
| Legacy worst 7 (batch 1) | https://github.com/SanCoder2026/FreeDailyPro-Blog/tree/main/Agent/site/rewrite-20261017-legacy1 |

## Still in progress (Grok)
- **Job C:** 7/74 started; remaining worst-first upgrades site posts (`blog-legacy-upgrade-list.md`), worst first, 7/batch → `Agent/site/rewrite-YYYYMMDD/`
- **Job D:** brand-new posts for tools with no post yet (`blog-coverage.md`) when C done or owner asks → `Agent/site/batch-YYYYMMDD/`

## Quality caveat for Claude
Batches B022–B062 used structured rewrites from the import plan. Prefer earlier batches (R*, B001–B021) if prioritizing human-varied prose first; still all meet length/structure rules for import testing.
