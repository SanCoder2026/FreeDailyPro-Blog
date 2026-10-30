Sent: 2026-10-30 14:29 ET

# B-0266 Color Converter: meta 78 and "Free" in title; add CMYK, OKLCH and colour names; show an error for bad input
Priority: P3 · Estimated effort: S · Report: #146 · Source: SEO backfill 10 (next top-GA tested tools after #144): curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:28–14:29 ET; GA4/GSC from analytics/2026-07-10-to-now-raw.md and testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md: GA #46 (50 views). No GSC row in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A designer or developer should paste any colour and copy it in the format their tool needs.
## Why
- Function tested earlier: all formats and WCAG contrast correct; invalid input gives blank fields and a black swatch with no message; rgb(300) is silently accepted (L-238).
- Title "Color Converter Online Free - HEX, RGB, HSL | FreeDailyPro" (58) with "Free". **Meta 78** ("Convert between color formats instantly. Free and fast…"). H1 "HEX / RGB / HSL Converter" (does not say "color converter").
- 200, sitemap, 11 hreflang, valid JSON-LD. /es English → **B-0123**.
- **Top 5 (~14:29 ET):** CMYK, Lab, OKLCH, HSV, HWB (HexaCalc, Huebert, hexrgb.com, how.box); nearest colour name (HexaCalc, how.box); shareable URL with the colour (Huebert); tints and shades row (how.box); bulk HEX list (HexaCalc); 8-digit HEX with alpha (hexrgb.com).
## Who uses this
Web designers, developers and print designers.
## Outcomes (ranked)
1. Clear error for invalid or out-of-range input (L-238).
2. Add CMYK, OKLCH and the nearest colour name.
3. Fix title, meta and H1.
## SEO
- **Keywords:** "color converter", "hex to rgb", "rgb to hex", "hex to hsl".
- **Suggested:**
  - Title: `Color Converter – HEX, RGB, HSL | FreeDailyPro` (46)
  - Meta: `Convert any colour between HEX, RGB and HSL, with alpha. Paste a code, see the swatch, check WCAG contrast and copy the format you need. Runs in your browser.` (158)
  - H1: `Color Converter: HEX, RGB and HSL`
  - FAQ: "How do I convert HEX to RGB?" · "What is HSL for?" · "Does it handle transparency?" → "Yes."
## Constraints
Keep the existing contrast check.
## Test cases
1. #FF0000 → rgb(255, 0, 0), hsl(0, 100%, 50%).
2. rgb(300,0,0) → error message, not a silent clamp.
3. Title ≤ 60, no "Free"; meta 140–160.
