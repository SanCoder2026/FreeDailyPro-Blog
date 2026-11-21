Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator (thumbnail-gen): deep test report for Claude

- **Written:** 2026-11-21 01:24 EST (box `date`, ET). Testing ran 2026-11-21 00:57–01:21 EST.
- **Tool:** https://www.freedailypro.com/tool/thumbnail-gen. Row 33 of TEST-ORDER.md: Pro, Video Tools. Plan note "L-243 rule 1 (ApyHub billable/live)"; tools.csv tag `gated:file-job`. Duplicate group C42 (name collision with `yt-thumbnail`). **GSC data is not available.**
- **Classification:** Professional Tool (Premium Applications step: paid passes remove the badge). Runs fully in the browser; no ApyHub or other API call was seen in any run (the "ApyHub billable" note doesn't apply to what the page does today).
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD, 10 locales + /ar, the blog, sitemap. JS chunks: `ThumbnailGen`, `ffmpegEngine`, `operations`, `timeParse`, `utils`.
  - **YouTube video:** yt-dlp, 14 frames, 2 sheets and a zoom.
  - **Headless Playwright:** 6 synthetic videos/files run (H.264 1080p, portrait, VP9 WebM, HEVC, .txt, fake .mp4; a black clip is shipped but was not run); every size/shape, title, JPG, time box, frame steps, Suggest frames; HEVC fallback; request scan; gate with uses left and at 0; Quick Buy; Share; print; keyboard; 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** one fresh context loaded with 10 remaining (`usageToday` 0, day key 2026-11-21); all others at 0 remaining. Trial uses spent: **1** (one per-image Download).
- **Constraints kept:** guest only, no sign-in, no email or card typed (stopped at the Day Pass email prompt and at Stripe Checkout), no ad clicks, no API/MCP, no site or repo changes. The Stripe session id is redacted.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first", $4.99/month 1 GB), Open from Google Drive (not clicked; presumed Google sign-in, unverified).
- **Pending:** confirm the ZIP result in a second uses-left context → **RERUN-AFTER-RESET row 33** (`tg-gate.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/ThumbnailGen-BeEuZmFi.pretty.js`):
- **Sizes list `te`:** includes `yt4k` and `short4k` labelled "(recommended)"; the page copy still lists four sizes.
- **Download all as ZIP (`pe`):** builds the ZIP and calls the generic download helper `be(...)`. Live it was blocked at 0 but not charged with uses left, while the per-image gated Download (`xe`, "Download uses 1 trial use") charged one. Check which usage call the ZIP path makes.
- **Capture `me`:** native `<video>` seek, ffmpeg.wasm fallback (`ffmpegEngine`) for unplayable files; the error text for every failure is the HEVC one.
- **Step buttons:** fixed 1/30 s.

After you ship, rerun `scripts/tg-gate.js` (expect ZIP to change `usageToday` the way you decide), `tg-live.js testfiles/V3_720p.webm`, `tg-drain.js`, then test-cases.md (TG-01…TG-34).

## Intent

A creator has a video and needs a thumbnail for YouTube, Shorts/Reels or a square post. They want to:
- scrub to a sharp, expressive frame (or have the tool suggest one)
- get it at the exact size the platform expects, optionally with a bold title
- download it quickly, with the video never leaving their device

The engine delivers this well:
- Frame-exact capture at every size; Fill/Fit maths correct; Devanagari/emoji titles wrap cleanly; JPG option.
- Suggest frames finds 10 candidates in ~1.3 s; the time box accepts "1:05.5" and rejects junk with a clear toast.
- HEVC files that Chromium can't play still capture via ffmpeg.wasm from jsDelivr, exactly as the Privacy copy says.
- Nothing is uploaded; Share gives the plain URL.
- The download gate works at 0: both Download and ZIP open the cap dialog → Day Pass $1 email prompt; Quick Buy monthly reaches Stripe Checkout.

Trust breaks in four places:
- **Policy:** "Download all as ZIP" handed over 2 badged frames for 0 trial uses while one single Download costs 1.
- **Promise vs page:** the page says four sizes; the tool has six and calls 4K "recommended" even when it upscales a 720p clip 3×.
- **Video:** a 29 s old-UI clip with a personal bookmarks bar.
- **Error message:** a broken or non-video file with a video extension is blamed on "iPhone HEVC".

## Why: what the evidence says

- **P1, policy question / loophole for Santosh:**
  - With uses left (`json/gate.json`, 01:08:33–01:09:37 EST): Capture ×2 0 → 0; per-image Download 0 → 1; **Download all as ZIP (2 frames) 1 → 1**, no dialog; still 1 after reload. The ZIP contained both images, badged (`testfiles/outputs/zipx/`).
  - At 0 (`json/drain.json`, 01:10 EST): Download and ZIP both open the cap dialog; Capture and Suggest still work (results free, download gated).
  - Nov 20 decision: Barcode/Invoice charge per Download; this tool isn't in the uncounted list. A batch export that costs nothing while a single costs one is a policy question; one observation, pending RERUN row 33.
- **P2: page copy is behind the tool.** FAQ, Details and Limitations ("There are four output sizes") omit YouTube 4K 3840×2160 and Shorts 4K 2160×3840. Those options say "(recommended)" and upscale a 720p source 3× with no warning (`testfiles/outputs/V3_720p__yt4k_fill.png`). Nothing tells the user that ZIP and single Download differ in cost.
- **P2: video wGXvbaUKqQI (29 s, 2 views, 2026-09-07):** old UI (Capture/Download/Reset only; no sizes, title, Suggest, ZIP, trial strip); full-desktop capture with the personal bookmarks bar (Gmail, Netflix, Prime Video…) and taskbar; "Free Step-by-Step", "200+ Free Productivity Tools".
- **P2: meta description is generic** (68 chars, no YouTube/Shorts sizes or title text); title/meta/section headings English under 9 locale URLs; /ar 404.
- **P2: completeness:** no title position/alignment, second line, text box, logo overlay, subject-aware vertical crop, colour adjustments, templates or "under 2 MB" export (desk; competitors not re-verified live).
- **P3 items:**
  - Non-video file renamed .mp4 → "often iPhone HEVC" message, then "Could not read that frame from the video".
  - Time past the end clamps to the end but the box keeps the typed time.
  - Fixed 1/30 s frame step on 24/25/50/60 fps video.
  - Header says "the first use downloads a processing engine"; live, playable videos never load it.
  - Blog says "keep the title toward the left" (the title is always centred near the bottom; the page itself says there is no position control).
  - Both strip buttons named "Quick Buy"; iPhone SE 9 px overflow; 16 px icon targets; axe label-content-name-mismatch, region, ad-caption contrast; thumbnail alt; JSON-LD Offer 4.99.

## Outcomes we want

1. Santosh decides how Download and ZIP count (e.g. ZIP = N uses, or 1 use per batch), and the code, labels and page copy say the same thing.
2. The page lists all six sizes; 4K is "recommended" only when the source is big enough, or the tool warns "upscaled from 720p".
3. A current, clean video: drop a clip → Suggest frames → YouTube size + title → Download, with "trial uses" wording.
4. Error messages that match the cause (not a video / damaged file vs HEVC).
5. A Premium Applications step: title position and a second line, logo overlay, a size target.
6. P3 polish: time box shows the clamped time, frame step from the real frame rate, labelled Quick Buy buttons, mobile overflow.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | All sizes, titles, JPG, Suggest, HEVC fallback work (`json/cases-*.json`, `testfiles/outputs/`). |
| 2 | Completeness vs competitors | PARTIAL | Strong core; no title position, logo, templates, colour tweaks, size target (desk; not re-verified live). |
| 3 | Ease of use | PASS (minor) | Clear steps, drop zone keyboard reachable, Suggest frames. Time box keeps an out-of-range time; misleading HEVC error for broken files. |
| 4 | Layout attractiveness | PASS (minor) | Clean on all engines; iPhone SE 9 px overflow; small icon targets. |
| 5 | Payment process | PASS (stopped) | Quick Buy day / cap dialog → "Day Pass, $1" email prompt; Quick Buy monthly → Stripe Checkout. Nothing typed. |
| 6 | Information correct | PARTIAL | "Four output sizes" (six live); 4K "(recommended)" while upscaling; "first use downloads an engine"; ZIP cost not stated. Privacy copy correct. |
| 7 | Indexing | PASS | 200; canonical self; in the sitemap with the blog. |
| 8 | SEO | PARTIAL | Good title, FAQPage (6), VideoObject. Generic 68-char meta; English title/meta under 9 hreflangs; /ar 404; thumbnail alt; Offer 4.99. |
| 9 | Blog exists and accurate | PASS (minor) | `/blog/thumbnail-gen` (Oct 17) accurate on six sizes and maths; "keep the title toward the left" and "non-video rejected" are off. |
| 10 | YouTube video exists | PASS | wGXvbaUKqQI, 29 s, 2 views, 2026-09-07. |
| 11 | FAQ and guide correct | PARTIAL | Size FAQ lists four sizes. Others accurate. |
| 12 | Video shows current capabilities | **FAIL** | Old UI (no sizes/title/Suggest/ZIP), personal bookmarks bar, "Free" wording. |
| 13 | Storage | PASS | Nothing uploaded or stored; no big POSTs; files stay on device. |
| 14 | Sharing | PASS | Share copies only the tool URL (`json/share.json`). |
| 15 | Downloads | PASS | PNG/JPG per image and ZIP; correct names and sizes; badge "Created with FreeDailyPro.com" (intentional). Drive/cloud: sign-in, untested. |
| 16 | Usage count | **Policy question** | Download 0 → 1; ZIP of 2 frames 1 → 1 (uncharged); Capture/Suggest uncounted; gate enforced at 0. Pending second observation (RERUN row 33). |
| 17 | Categorization in section | PASS | Video Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Video Tools. |
| 19 | AI need/demand | PASS (demand steady) | "video thumbnail from frame" / "YouTube thumbnail size" are evergreen; Suggest frames already covers the "pick a good frame" need. |
| 20 | Merge better? | No | C42 `yt-thumbnail` downloads an existing YouTube cover; this makes one from your video. Clearer names would help. |
| 21 | Remove? | No | |
| 22 | Duplicates | Name collision only (C42) | Page already points to the YouTube thumbnail tool under "When not to use it". |

## Severity summary
- P0: 0. Privacy holds: no video data in any request.
- P1: 1 (ZIP exports N badged frames for 0 trial uses while one Download costs 1; policy question).
- P2: about 4 (copy behind the six sizes and 4K upscaling, video, meta/locales, completeness).
- P3: several.
