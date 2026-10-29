# B-0012 Outdated platform presets (ringtone 40s, YouTube thumbnail, Facebook cover)
Priority: P2      Estimated effort: 40 min

## Goal / why
Correctness vs official platform rules; users get rejected/cropped outputs.

## What to change
- https://www.freedailypro.com/tool/ringtone-maker: iPhone M4R offers 40 s; Apple Support says ringtones are up to 30 s. Cap M4R at 30 s and update About/meta (Android MP3 may keep 40 s).
- https://www.freedailypro.com/tool/thumbnail-gen: presets 'YouTube 1280x720' / 'Shorts 1080x1920'; YouTube Help now recommends 3840×2160 / 2160×3840. Add 4K presets, keep 1280×720 as 'HD'.
- https://www.freedailypro.com/tool/social-media-formatter and https://www.freedailypro.com/tool/banner-sign-maker: Facebook Cover exports 820×312 (display); recommended upload 851×315. Export 851×315 or label both.

## Acceptance criteria
- M4R exports ≤30.0 s; copy says 30 s for iPhone.
- Thumbnail menu shows 4K presets producing exact sizes.
- FB cover export is 851×315 (or two clearly labelled options) in both tools.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing other presets.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #46, #47, #50, #53)
