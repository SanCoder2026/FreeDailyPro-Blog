# hero-full-site-audit-report
Date and time: 2026-11-13 13:05
Type: AUDIT (report only — no image replacements in this folder)

## Method
1. Sitemap → **382** blog URL slugs (2 non-posts: `page`, `topic` 404)
2. Download `https://www.freedailypro.com/blog/<slug>.webp` → **380** heroes OK
3. Technical checks: size, bytes, teal fraction, skin proxy, luminance variance, bottom strip darkness
4. Re-check of prior Nov-10 high-risk **34** slugs (PENDING-LIST from 1255 pack)
5. Visual sample of ~20 titles vs images (SQL, real-estate tools, logo maker, invoice, BMI, HEIC, robots/sitemap, etc.)

## Technical results (live 2026-11-13)
| Check | Result |
|-------|--------|
| Heroes downloadable | 380 / 380 post slugs |
| Exactly 1200×630 | **380 / 380** |
| Under 150 KB | **380 / 380** |
| Duplicate image reuse (md5) | **0** groups |
| Prior abstract/teal 34 list still tech-failing | **1** (`make-srt-vtt-subtitles-from-audio` low skin only) |
| Strict risk≥4 auto score | **0** |
| Strict risk 2–3 | **~0–1** |

**Conclusion (tech):** Live heroes largely **meet size + branding geometry**. Prior abstract/teal crisis from Nov-10 appears **already fixed on production**.

## Topic relevance (human sample)
Sampled heroes for diverse titles mostly show **person + tool UI/props** matching the job (merge PDF pages, BMI chart, invoice UI, logo canvas, SQL IDE, HEIC conversion, robots/sitemap draft). No mass return of pure teal abstract panels.

### Weakest outliers (lowest skin / dark studio scenes — candidates for next FIX pack)
These are **not** abstract teal failures; they are dark or low-face-area scenes that may still feel off-brand or weak at glance:

1. `make-srt-vtt-subtitles-from-audio`
2. `run-stage-countdown-and-focus-rounds`
3. `audio-comparer`
4. `play-video-clip-backwards-for-effects`
5. `sprite-sheet-tool`
6. `convert-curl-to-fetch-and-python`
7. `mesh-3d-viewer`
8. `free-audio-tools-voice-memos-podcast-cleanup`
9. `http-status-reference`
10. `regex-tester`
11. `css-js-minifier`
12. `connect-the-freedailypro-mcp-server-to-claude-desktop` (also in API regenerate pack)

**Next FIX pack proposed:** `2026-11-13-1300-hero-topic-weakest-12` (Imagine generation ready on user confirm — blocked mid-turn this session).

## Also note for Claude
- Folder `2026-11-13-0745-hero-image-fixes-3-api-posts` has 3 API hero replacements (MCP/TTS/Paycheck) with no invented on-screen numbers/text.
- Folder `2026-11-13-0800-wishlist-batch3-premium-flagships` is **new posts** batch 3 (5 Premium apps), not a hero audit.

## Files in this report pack
- SUMMARY.md / all.tsv / strict_*.tsv (from automated scan)
- NOTE.md (this file)

## Anything Grok could not verify without more time
- Full 380 visual topic review (only sample + heuristics)
- Cache/CDN lag if owner still sees old abstract images in browser
