# B-0015 Remove 'Free' from tool page titles and meta descriptions
Priority: P3      Estimated effort: 40 min

## Goal / why
Positioning: standing rule is trial uses / professional tools, not 'free'. Titles/meta still say Free.

## What to change
Titles/meta (often the template 'Free and fast…') on: https://www.freedailypro.com/tool/audio-speed-changer, https://www.freedailypro.com/tool/volume-booster, https://www.freedailypro.com/tool/video-speed-changer, https://www.freedailypro.com/tool/ringtone-maker, https://www.freedailypro.com/tool/repair-pdf, https://www.freedailypro.com/tool/image-filters, https://www.freedailypro.com/tool/powerpoint-to-pdf, https://www.freedailypro.com/tool/thumbnail-gen, https://www.freedailypro.com/tool/caption-generator, https://www.freedailypro.com/tool/image-quality-enhancer, https://www.freedailypro.com/tool/epub-checker, https://www.freedailypro.com/tool/color-picker-image, https://www.freedailypro.com/tool/camera-capture, https://www.freedailypro.com/tool/social-media-formatter, https://www.freedailypro.com/tool/bulk-image, https://www.freedailypro.com/tool/clip-path-generator, https://www.freedailypro.com/tool/mockup-generator, https://www.freedailypro.com/tool/stl-ascii-binary-converter, https://www.freedailypro.com/tool/name-badge-maker, https://www.freedailypro.com/tool/mesh-3d-viewer, https://www.freedailypro.com/tool/paper-format-checker, https://www.freedailypro.com/tool/audio-comparer, https://www.freedailypro.com/tool/audio-scrambler. Best fix: change the shared meta-description template and title generator, then spot-check. Keep the brand name FreeDailyPro.

## Acceptance criteria
- None of the listed pages has 'Free'/'free' in <title>, meta description or og tags (brand name excepted).
- Replacement copy fits the '330+ professional tools' / trial-uses positioning; no truncation over ~60/155 chars.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Blog post copy (Claude blog wave). Brand name.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #46–#54, #65)
