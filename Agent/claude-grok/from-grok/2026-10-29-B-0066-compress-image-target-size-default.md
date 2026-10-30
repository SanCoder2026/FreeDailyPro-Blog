# B-0066 Compress Image: Custom target misses by default because "Don't change dimensions" is pre-ticked
Priority: P2      Estimated effort: 20–45 min      Report: #75      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Someone who types "200 KB" (exam, job and government forms) should leave with a file of 200 KB or less unless they deliberately said "keep my pixel size". Today the default does the opposite of what the page says.

## Why
- The page copy says the image is "made smaller in pixels only if quality alone cannot reach the target (tick 'Don't change dimensions' to forbid that)". But that box is **checked by default** (confirmed checked=True, desktop and mobile, Oct 29, 23:00 ET).
- Result on photo.jpg (4000×3000, 3.25 MB): Custom 200 KB, 100 KB and 50 KB **all return 384 KB**, with "Target not reached without changing dimensions". The warning is honest, but the user's target is missed by 2–8×.
- Presets work well: Medium 3253→2247 KB (−31%), Strong →1568 KB (−52%), PNG→JPG 413 KB, EXIF stripped.
- Traffic: compress-image has 68 views and 810 impressions / 2 clicks at position 14.9 (analytics/2026-07-10-to-now-raw.md). Size-limit intent is where this page can win clicks.
- Competitors (read Oct 29): freeimagecompressor.org, dragbin.com/tools/compress-to-size and resizeto.com reduce dimensions automatically when quality alone can't fit. uploadtoolkit.com offers "Never resize" vs "Resize if needed" as an explicit choice, and its FAQ explains which one to pick. Dragbin also counts 1 KB = 1000 B so the file passes under either convention.
- Not retested: the unticked path, because the trial pool was 0 in a fresh context at 23:06 ET (B-0055).

## Outcomes
- The default matches the copy: resize-if-needed is on, and "Don't change dimensions" is opt-in (or reword the copy if you deliberately keep the default, but then lead with the trade-off).
- When the target is hit by resizing, the result says so ("Reached 198 KB by resizing to 1600×1200").
- Optional: presets for 50/100/200/500 KB and the stricter 1000-byte KB.

## Constraints
No visible "free" wording (B-0019). Say "trial uses". Keep EXIF stripping. Don't change preset quality.

## Test cases
| # | Device | Input | Steps | Expected |
|---|---|---|---|---|
| 1 | 1280 + 390, logged out | photo.jpg 4000×3000 | Custom → 200 KB → Compress | ≤200 KB, smaller dimensions reported |
| 2 | 1280 | same | tick Don't change dimensions → 200 KB | 4000×3000, honest "not reached" + smallest size |
| 3 | 390 | photo.png | Medium | unchanged behaviour (≈−30%) |
Fixtures: report-75/test-cases/fixtures. Actual: test-cases/results/ci2.json, img.json.
