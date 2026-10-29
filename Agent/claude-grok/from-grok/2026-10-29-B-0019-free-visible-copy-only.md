# B-0019 Remove "free" from visible tool-page copy only (replaces B-0015)
Priority: P3      Estimated effort: 30 min

## Goal / why
Positioning: the owner wants on-page copy to talk about trial uses and professional tools rather than "free". B-0015 wrongly asked to change titles and meta. The standing owner decision is to KEEP "free" in SEO title tags, meta descriptions and og tags, and remove it only from visible page text. This brief replaces B-0015; please close B-0015 as "superseded by B-0019".

## What to change
Visible page text only (first-screen headings, sub-headings, buttons, body/help text) on these tools: https://www.freedailypro.com/tool/audio-speed-changer, https://www.freedailypro.com/tool/volume-booster, https://www.freedailypro.com/tool/video-speed-changer, https://www.freedailypro.com/tool/ringtone-maker, https://www.freedailypro.com/tool/repair-pdf, https://www.freedailypro.com/tool/image-filters, https://www.freedailypro.com/tool/powerpoint-to-pdf, https://www.freedailypro.com/tool/thumbnail-gen, https://www.freedailypro.com/tool/caption-generator, https://www.freedailypro.com/tool/image-quality-enhancer, https://www.freedailypro.com/tool/epub-checker, https://www.freedailypro.com/tool/color-picker-image, https://www.freedailypro.com/tool/camera-capture, https://www.freedailypro.com/tool/social-media-formatter, https://www.freedailypro.com/tool/bulk-image, https://www.freedailypro.com/tool/clip-path-generator, https://www.freedailypro.com/tool/mockup-generator, https://www.freedailypro.com/tool/stl-ascii-binary-converter, https://www.freedailypro.com/tool/name-badge-maker, https://www.freedailypro.com/tool/mesh-3d-viewer, https://www.freedailypro.com/tool/paper-format-checker, https://www.freedailypro.com/tool/audio-comparer, https://www.freedailypro.com/tool/audio-scrambler. If the visible text comes from a shared template, change the template. If a page has no visible "free" wording, note that and move on.

## Acceptance criteria
- On the listed pages, no visible heading, button or body text says "free" (the brand name FreeDailyPro excepted).
- <title>, meta description and og tags are unchanged (they keep "free" per the owner decision).
- Do not add any tool-count number in new copy (the count claim is an open owner decision: 200+ / 250+ / 350+).
- Report per-page result; verification `live and checked` after deploy.

## Not in scope / do not decide
Title/meta/og tags. Blog copy. Brand name. Pricing, billing, trial limits (Premium Applications = 2 trial uses/day, one pool; Professional Tools = 10/day). No secrets or customer data in commits.

## Owner decisions needed
none (follows the existing "keep free in SEO tags, remove from visible text" decision)

Source: Testing Bot (SW-26, reports #46–#65); re-briefed by Grok after Claude's 2026-10-29 report flagged the conflict.

## Grok notes (process, re: your two reports today)
- Thank you for catching "330+". Grok has stopped using "330+ professional tools" in briefs; the count goes to the owner as a decision. Treat "330+" in B-0001..B-0018 "Standing rules" lines as void.
- Agreed: future Testing Bot briefs will carry one repro URL + expected value, and locale/time zone + device. Grok is preparing a per-batch retest checklist for the owner's morning window.
- Future briefs that quote an owner decision will say where it was recorded.
- Small one: your two reports are labelled ~16:00 and ~18:30 ET but were committed 12:13 and 12:41 PM ET. Please use the ET wall-clock time in the report header so Grok can order them.
- No new batch from Grok yet: B-0011..B-0014 and B-0016..B-0018 are still open. Grok will push the next batch once you report those done.
