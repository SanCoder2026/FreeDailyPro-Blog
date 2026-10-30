Sent: 2026-10-30 14:47 ET

# B-0275 Banner & Sign Maker: good print DPI warning; add text sizing, layout choices and a safe-zone guide; fix meta
Priority: P3 · Estimated effort: M · Report: #149 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:44–14:47 ET. L-243: next 3 untested tools alphabetically after avatar-builder. No GA/GSC rows for these pages in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A shop owner should make a readable sign or web banner at the right size and print it sharp.
## Why (1280 px)
- "Trial: 2 uses/day", $3 / $9.99. 12 size presets (Web Banner, Social Post, Storefront Sign, Large Poster, Instagram Story, YouTube Thumbnail 1280×720 ✔, YouTube Channel Banner, Facebook Cover, X Post, LinkedIn Post, Yard Sign 24×18 in, Flyer A4), custom W×H, heading, subheading, footer, colour, font, background photo, logo, extra info points. Download PNG and print PDF with finished width and 0.125" bleed.
- **Print DPI warning works:** "1280 × 720 px printed 24 in wide = 53 DPI — below 150 DPI will look soft in print" ✔.
- Download PNG opened "Your result is ready… needs a pass" (owner's decision).
- **Trial counter mismatch:** the 1280 probe at ~14:44 showed "2 remaining today"; fresh logged-out sessions at ~14:46 showed "0 remaining" → **B-0156**.
- **Missing vs competitors (~14:47 ET):** templates to start from (Canva, Stickerine); free text placement and size (all); safe zone and bleed lines on the preview (Stickerine, MagnifyPrints templates); QR code element (Stickerine); grommet/hem margins for vinyl banners (Stickerine, MagnifyPrints).
- Unnamed "text"/"submit" controls → **B-0155**. No overflow at 390 px. Ad text "Hire Developers"/"Edit Photos" stuck to copy → L-004. /es English title → **B-0123**.
## Who uses this
Small shops, event hosts and creators making signs, posters and social banners.
## Outcomes (ranked)
1. Safe-zone and bleed guides on the preview.
2. Text size control per line; 2–3 layout choices.
3. QR code element.
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD. Title "Make a Banner or Sign Online - Custom Sizes | FreeDailyPro" (58) ✔. **Meta 75.** H1 "Banner & Sign Maker".
- **Keywords:** "banner maker", "sign maker online", "yard sign maker", "youtube banner maker".
- **Suggested:**
  - Title: `Banner & Sign Maker – Custom Size, Print PDF | FreeDailyPro` (59)
  - Meta: `Make a web banner, storefront sign, yard sign or poster at any size: add a heading, logo and photo, then save a PNG or a print PDF with bleed and a DPI check.` (158)
  - H1: `Make a Banner or Sign at Any Size`
  - FAQ: "What DPI do I need for print?" · "Can I add bleed?" · "Which social sizes are included?"
## Constraints
Keep the trial-uses rule.
## Test cases
1. YouTube Thumbnail preset → 1280×720; 24 in width → "53 DPI" warning.
2. Admin: PNG size and print PDF page size with bleed.
3. Title ≤ 60; meta 140–160.
