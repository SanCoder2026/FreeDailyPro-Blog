Sent: 2026-10-30 14:53 ET

# B-0277 Sprite Sheet Tool: metadata exports and a stronger snippet
Priority: P3 · Estimated effort: M · Report: QA-REPORT-150 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~14:50 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make the sprite sheet tool a full step in a game developer's pipeline (sheet plus engine data), and give it a meta that earns the click.

## Why
GSC page: 6 clicks / 488 impressions / 1.2% CTR / avg position 25.2. Meta is only 76 chars. Top-5 competitors (Sprite Sheet Builder, SpritePilot, SpritePacker, Final Parsec, Sprite Sheet Maker) all export JSON/XML/CSS coordinates alongside the PNG; FreeDailyPro exports the PNG only (L-211 gap).

## Who uses this
Indie game developers and animators using Phaser, Unity, Godot or CSS sprites.

## Outcomes (ranked)
1. Atlas metadata export: TexturePacker-style JSON (Phaser/PixiJS) and CSS background-position — present at all five competitors.
2. Animation preview with FPS control before export (4 of 5 competitors).
3. Padding/spacing control and GIF-in → frames (Sprite Sheet Builder, SpriteSheetMaker).
4. Meta rewritten to 140–160 chars; /es title localised (L-189).

## SEO
- Now: title 59 chars; meta 76; H1 "Sprite Sheet Generator & Splitter"; /es English.
- Keywords: sprite sheet generator, sprite sheet maker, split sprite sheet, sprite sheet to frames.
- Suggested Title: "Sprite Sheet Generator & Splitter Online | FreeDailyPro" (55)
- Suggested Meta: "Combine frame images into a sprite sheet grid or split a sheet back into frames. Runs in your browser, built for game developers and animators. Try it now." (155)
- Suggested H1: "Sprite Sheet Generator & Splitter"
- FAQ: Which engines can use the output? · Are my images uploaded? · How do I split a sheet into frames? · Max sheet size?

## Constraints
Premium gating (2 trial uses/day) unchanged. Keep existing PNG output identical (128×32 for four 32×32 frames, order f0–f3).

## Test cases
1. Combine four 32×32 frames → PNG 128×32, order f0–f3 (regression of L-211).
2. Same run → JSON with 4 frames whose x/y/w/h match the PNG.
3. Split a 128×32 sheet with 4 columns → four 32×32 frames.
4. Meta 140–160 chars; /es Spanish title.
5. 390 px: no horizontal overflow.
