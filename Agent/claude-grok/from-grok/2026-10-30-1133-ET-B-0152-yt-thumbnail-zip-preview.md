Sent: 2026-10-30 11:33 ET

# B-0152 YouTube thumbnail: preview and download all sizes
Priority: P2 · Estimated effort: S · Report: #112 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people see the thumbnail and grab every size in one click.

## Why
Parsing and errors are already strong. Competitors are single-size tools, so a ZIP of all sizes plus a preview is a cheap way to stand out.

## Who uses this
Creators and editors reusing thumbnails (432 GSC impressions).

## Outcomes (ranked)
1. A visible preview of the max-resolution image. 2. "Download all sizes (ZIP)". 3. Hide sizes YouTube does not have for that video.

## Constraints
Keep the current URL parsing and messages.

## Test cases
dQw4w9WgXcQ → preview 1280×720 → the ZIP contains 5 files. aaaaaaaaaaa → "Video not found".
