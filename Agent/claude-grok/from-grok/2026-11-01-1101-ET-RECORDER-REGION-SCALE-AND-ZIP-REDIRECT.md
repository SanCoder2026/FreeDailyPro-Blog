Sent: 2026-11-01 11:01 AM ET

# Screen Recorder region size bug, and a /tool/zip redirect

**Intent:** The Screen Recorder is about to be promoted as a "no install" tool. When a user records a region, they should get exactly the region they selected.

**Why:** QA-399 (commit 27871a7) found the region recording is cropped to the wrong size. About 540x353 was selected but 386x362 was recorded, so the aspect ratio is wrong. This looks like a mix-up between screen pixels and video pixels when the region is scaled. A tab also crashed after Stop. Separately, /tool/zip returns 404.

**Outcome:**
1. The recorded video matches the selected region's size and aspect ratio on high-resolution (HiDPI) screens and when the browser is zoomed.
2. Stop never crashes the tab. Release the media streams and the canvas cleanly.
3. Add a 301 redirect from /tool/zip to /tool/zip-unzip.
4. Mark it done so the Testing Bot can retest.

Source: owner
