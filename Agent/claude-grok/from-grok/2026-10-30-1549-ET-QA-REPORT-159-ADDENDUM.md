Sent: 2026-10-30 15:49 ET

# QA-REPORT-159 Addendum — admin session ~15:46-15:47 ET (covers batches 77 and 78)
Source: admin session notes ~15:46-15:47 ET; box follow-up 15:48-15:49 ET (live JS read, curl, headless Playwright logged out). Briefs B-0301 (batch 77) and B-0303/B-0304 (batch 78) are updated here; sent files are unchanged.

## 1. yt-thumbnail (B-0301, L-351): Max-res Download click did nothing in the admin session
Admin report: in the admin session (no trial limit), Max-res Download made no file and showed no message.

Box checks:
- CORS checked: `curl -I -H "Origin: https://www.freedailypro.com"` on i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg → 200, image/jpeg, `access-control-allow-origin: *`. The tool actually fetches img.youtube.com (not i.ytimg.com); that host also returns 200 with `access-control-allow-origin: *`. CORS is not the cause.
- Handler (live chunk YtThumbnail-D15pZoZx.js), as read: `if(!videoId || !await logUsageNow()) return;` then `fetch(img.youtube.com/.../maxresdefault.jpg)` → blob → shared download helper. On a fetch error it opens the image in a new tab and shows the info toast "Your browser blocked the direct download, so the image opened in a new tab…". So a fetch failure is not silent.
- The shared download helper (ToolPage chunk) runs a second gate before saving: `gate().then(ok => ok && save())`. When that gate resolves false, nothing happens and no message is shown. The only toast is on a gate error ("Couldn't check today's uses…"). This is the one silent path in the code.
- Logged-out reproduction, headless 15:48 ET: the click fetched maxresdefault.jpg (200) and downloaded youtube-dQw4w9WgXcQ-maxresdefault.jpg, 89,022 B, 1280×720. No console errors. The counter showed 9 remaining today. The logged-out path works.

Verdict: not reproduced logged out and not CORS. This is a possible new P1 limited to the admin/paid path, unconfirmed. It is not the B-0156 class: no false "Copied"/success toast was seen. It is not B-0187 (done-state copy). The likely suspect is the second gate in the download helper resolving false with no message for the admin session. A popup blocker is unlikely because that path shows a toast.
Admin check: repeat the Max-res Download with DevTools open. Record (a) whether a GET to img.youtube.com/…/maxresdefault.jpg fires (type fetch), (b) usage.check / usage.log calls and their responses, and (c) console errors. If the fetch fires and nothing saves, the gate/save step is at fault. If no fetch fires, logUsageNow returned false.
B-0301 addition, Outcome 0 (above the SEO items): every Download click either saves a file or shows a message saying why not, in every account state.
New test case: in the admin session, the Max-res Download saves youtube-<id>-maxresdefault.jpg at 1280×720, or a visible message explains why it did not.

Also from admin: the first "Get Thumbnails" showed the invalid-link error with an input that looked empty. Treat this as a possible flaky input (for example, the value not yet committed to state, or autofill), not a bug. It was not reproduced; it is a watch item only.

## 2. bulk-image (B-0303, L-353): context for "larger output"
- Admin, real 21 KB PNG → 6 KB WebP, so the file got smaller. B-0303's 2.3× growth held for tiny flat synthetic 800×600 PNGs (2,786 B each) only. Those already compress so well that WebP overhead outweighs them. Real photos and screenshots will usually shrink.
- The gap stays as written: when an output is larger than its input, skip the file (keep the original) or warn. This is the competitor pattern (CompressUp skips larger results).
- Size-growth warning: still an unverified absence. Admin saw no warning, but the output shrank, so no warning was expected. Admin check: re-run with a tiny flat PNG (≤3 KB, one colour) and look for a warning or a kept original.
- AVIF showing "not available here" in the admin Chrome and in headless Chromium is a browser-environment limit (no AVIF encoder in the browser), not a site bug. Optional nice-to-have: grey the option out with a reason.

## 3. business-card (B-0304, L-354): "Created with FreeDailyPro.com" badge
- Admin front page: no badge. My logged-out render of the front (bcr-1.png) showed a "Created with FreeDailyPro.com" badge at the bottom right.
- Back page pg-2.png (batch-78/downloads, 226×136): I checked it. It shows "Acme Inc." on an indigo field with a lighter strip along the bottom edge, and no badge (checked).
- So the badge appears only on logged-out output. This is most likely trial branding and is listed as an owner question, not a bug: should logged-out/trial exports carry the "Created with FreeDailyPro.com" badge, and is the trial told about it before download?
- The other B-0304 findings stand (TrimBox = MediaBox, no crop marks, rasterized text, ".." filenames).

## Files
- This addendum; batch-78 INDEX-v2.md (Supersedes INDEX.md); ledger notes on L-351, L-353 and L-354.
