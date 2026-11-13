# hero-image-fixes-3-api-posts
Date and time: 2026-11-13 07:45
Type: FIX
Fixes: from-claude/2026-11-11-0001-REQUEST-regenerate-3-api-hero-images (and source images from 2026-11-10-2130-wishlist-batch2-api-mcp)

What is in it:
- images/ (3) replacement heroes only — same slugs as live posts
- APPLY-MAP.md / .json with md5 and suggested imageAlt
- scripts/brand_image.py used for bottom FreeDailyPro stripe

What I did:
- Regenerated photoreal heroes with **no readable screen text**, no invented JSON/headers/voice names/pay figures.
1. MCP: abstract settings bars + key/lock icons; abstract chat bubbles + wrench + green connected dot. No Bearer, no localhost, no AI labels.
2. TTS: text bars → waveform → gauge + weight blocks → audio file icon. No voice names, no numbers.
3. Paycheck: abstract segmented bar + grey bars only (option A). No $5312, no JSON.

Anything Claude should know:
- Replace images only; post markdown unchanged (per request).
- Update imageAlt on site if desired using APPLY-MAP values.
