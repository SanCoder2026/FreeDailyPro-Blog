# Full site hero audit — 2026-11-13

## Scope
- Sitemap blog locs: 433 (includes pagination junk like `/blog/10` … not real posts)
- Real posts with heroes: **380**
- Download failures for real posts: 0 (2 fails were `page` and `topic` junk)

## Spec compliance (size/brand)
| Check | Result |
|---|---|
| 1200×630 | 380/380 |
| WebP <150KB | 380/380 |
| Bottom brand stripe present (dark bottom band) | ~380/380 |

## Abstract-teal / no-person (old high-risk)
The Nov-10 list of 33 high-risk abstract/teal heroes was re-scored on live:
- **All 33 now risk 0** on abstract-teal / size heuristics (prior packs applied).
- Residual: 5 still low skin (hands-on / dark booth) → upgraded in `2026-11-13-1330-hero-standard-upgrade-12`.

## Stricter standard pass
Even when size/brand pass, HERO-IMAGE-RULE requires **person + topic UI/props obvious at a glance**.
Lowest-skin / UI-heavy live heroes selected for upgrade (12):

1. make-srt-vtt-subtitles-from-audio
2. run-stage-countdown-and-focus-rounds
3. audio-comparer
4. sprite-sheet-tool
5. play-video-clip-backwards-for-effects
6. http-status-reference
7. convert-curl-to-fetch-and-python
8. free-audio-tools-voice-memos-podcast-cleanup
9. regex-tester
10. mesh-3d-viewer
11. css-js-minifier
12. image-filters

Apply pack: `from-grok/2026-11-13-1330-hero-standard-upgrade-12/`

## Pending Claude apply (already on main)
- `2026-11-13-0800-wishlist-batch3-premium-flagships` — 5 new Premium posts (not live until import)
- `2026-11-13-0745-hero-image-fixes-3-api-posts` — MCP / TTS / paycheck API heroes (live still has old hashes for MCP)

## Method
1. Crawl sitemap → slug list
2. Download `/blog/{slug}.webp`
3. Score size, skin proxy, teal, variance, bottom darkness
4. Visual contact-sheet QA on lowest skin + random 40
5. Regenerate strict fails with Imagine → brand_image.py

## Next
After Claude applies the 12 upgrades + 3 API heroes, re-crawl once. If owner still sees mismatches, send specific URLs (visual topic miss is hard to automate fully).
