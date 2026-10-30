Sent: 2026-10-30 14:33 ET

# B-0269 Avatar Builder: download works within trial uses; add more parts, custom colours and platform sizes; fix title and meta
Priority: P3 · Estimated effort: M · Report: #147 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:30–14:33 ET. L-243: next 3 untested tools alphabetically after agenda-cue-sheet-builder. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone needing a profile picture should make an avatar that looks like them (or their character) and download it at the right size.
## Why (1280 px; logged out, 2 trial uses at start)
- "Trial: 2 uses/day", $3/$9.99. Randomize, PNG 256/512/1024, SVG, circle crop, transparent background, background (7), skin tone (6), face (3), hair (5), hair colour (7), eyes (8), mouth (8), glasses.
- **Download PNG worked:** avatar-512.png saved; counter went 2 → 1 remaining.
- Colour swatches and many option buttons have no accessible name ("button") → **B-0155**.
- Page is honest: head only, no beard, clothes, hats or earrings, no custom colours.
- **Missing vs competitors (~14:32 ET):** 100–300+ parts incl. brows, beard, outfits, hats, earrings (AvatarMake, Cartoonify, Face Icon Generator); 4 styles (AvatarMake cartoon/manga/monster/emoji; Face Icon Generator Cute/Professional/Funky/Minimalist); unlimited colours; shareable link that reopens the avatar (AvatarMake); 2048 px PNG (AvatarMake), WebP and presets for GitHub/Slack/Discord (Face Icon Generator). All are free with no limit.
- No overflow at 390 px. Ad text "Edit Photos" glued to copy → L-004.
## Who uses this
Students, gamers, community members and small teams wanting a non-photo profile picture.
## Outcomes (ranked)
1. Name every option button (B-0155).
2. Add brows, beard, hats, earrings and a colour picker.
3. Shareable link and platform-size presets.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD. FreeDailyPro ranks in the top 5 for "avatar maker online cartoon avatar builder". /es English → **B-0123**.
  - **Title "Build a Custom Avatar Online - No Photo Needed | FreeDailyPro" is 61 chars.** **Meta 75.** H1 "Avatar Builder".
- **Keywords:** "avatar maker", "cartoon avatar maker", "profile picture maker", "avatar builder".
- **Suggested:**
  - Title: `Avatar Builder – Cartoon Avatar, No Photo | FreeDailyPro` (56)
  - Meta: `Make a cartoon avatar without a photo: choose skin tone, face, hair, eyes, mouth and glasses, then download a PNG up to 1024 px or an SVG, with circle crop.` (156)
  - H1: `Make a Cartoon Avatar Without a Photo`
  - FAQ: "Can I use it as a profile picture?" · "PNG or SVG?" · "Is it AI?" → "No."
## Constraints
Keep the trial-uses gate per the owner's decision.
## Test cases
1. Admin: SVG download opens in a browser at the chosen size; transparent PNG has alpha.
2. Title ≤ 60; meta 140–160.
