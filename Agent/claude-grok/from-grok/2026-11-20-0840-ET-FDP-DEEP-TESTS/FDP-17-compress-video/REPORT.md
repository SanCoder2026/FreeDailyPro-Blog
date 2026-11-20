Sent: 2026-11-20 08:40 ET

# FDP-17 Compress Video (compress-video): deep test report for Claude

- **Written:** 2026-11-19 15:54:46 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/compress-video. Row 17 of TEST-ORDER.md: Pro, Video Tools. Test-plan rank 16: "52 views; API returns same GIF regardless of settings" (quoted from TEST-ORDER; the API was not tested). **GSC data is not available.**
- **Classification:** Professional Tool, Video Tools. Trial-gated at Download (`gateAtDownload`). Compressing and both previews are not charged; "Keep original" is a free download.
- **Testers:**
  - **Desk review:** page, es, /ar, blog, category, the CompressVideo / utils / megabytes / ffmpegEngine code, and the Discord, WhatsApp and Gmail help pages.
  - **YouTube video:** metadata, 31 frames, crops.
  - **Headless Playwright:**
    - 20 file × mode cases, outputs measured with ffprobe
    - gate and dialogs, the Keep-original path, keyboard, axe, phones, Firefox
    - matrix: 10 profiles, 10 locales + /ar, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, nothing typed into the email or card prompts, no ad clicks, no API or MCP calls, no site or repo changes. No downloaded file was executed; the one free "Keep original" download was deleted after its size was checked.
- **Sign-in:** "Save to my cloud storage" stops at a sign-in dialog on https://www.freedailypro.com/tool/compress-video (untested). Google Drive save was gated at 0, so its Google sign-in was never reached.
- **Pending:** every context loaded at 10/10 used, so the cost of Download with uses left is unobserved. **Needs re-run after midnight UTC (7:00 PM ET).** RERUN-AFTER-RESET row 17 has been added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships video tools.

Code to look at (`evidence/js/`):
- `CompressVideo-DWmAzbV6.pretty.js`:
  - the presets `Fe` L90–96
  - the default mode L99
  - the info copy `O`
  - the result line and Keep-original branch
  - mode buttons (no `aria-pressed`) and the unnamed slider
- `utils-qgqMjnRG.pretty.js` `V`: target encode, fixed 128 kbps audio, 100 kbps floor, up to 3 passes, no cap at the source bitrate.
- `ffmpegEngine-DH91Xnxx.pretty.js` L216–231: 50 MB / 200 MB.

After you ship, rerun `scripts/cv-battery.js`, `scripts/cv-gate-kbd.js` and `scripts/cv-keep.js`, then `test-cases.md` (CV-01…CV-22).

## Intent

Someone's video is too big for Discord, WhatsApp, email or a portal. They want it to fit on the first try, look as good as the limit allows, and stay on their device. They should leave impressed and see the pass as the obvious way to download.

The engine delivers:
- Every size target landed just under (9.65/9.67, 6.40/6.45, 7.99/8.00, 1.91/2.00).
- Phone rotation, HEVC MOV, WebM, MKV and no-audio files all work.
- Trim + target works.
- Damaged files are caught before encoding.
- About 30 s for 10 s of 1080p.
- Honest "not reached" and "made it bigger, keep your original" messages.
- A clear 50 MB upsell.

Trust is lost in the words around it:
- presets tuned to old platform limits
- a "Light" option the page, blog and video describe but the tool doesn't have
- targets larger than the source that make files bigger while saying "Target reached"

## Why: what the evidence says

- **P1: platform presets are outdated.**
  - "8 MB (Discord)": Discord's FAQ, updated 2026-09-30, says "For non-Nitro subscribers, the maximum file upload is 20MB" (up from 10 MB in August 2026).
  - "16 MB (WhatsApp)": WhatsApp Help says the default video limit is 100 MB (fast) or 64 MB (slow).
  - Users who trust the label throw away half or more of the quality they were allowed. The meta description sells "WhatsApp and email presets", and the blog repeats "8 MB (the Discord figure)".
- **P1: copy describes a different tool.**
  - FAQ: "costs more than Light". Blog: "Light, Medium and Strong… 10, 25 or 50 percent". YouTube description: "Light/Medium/Strong". The video shows a Light button. There is no Light button live.
  - The guide says "Manual Quality, which is selected when the tool opens"; Medium is selected.
  - Passes are described as "adjusts once", "two full encoding passes" and "repeats up to twice"; the code allows 3.
  - The drop zone says "over 200 MB may take longer", while trial uses stop at 50 MB.
- **P1: targets above the source make files bigger.**
  - Custom "100 MB" on a 12.9 MB clip spent 46 s and produced 97 MB: "652.4% larger… Target reached (100.00 MB)".
  - The 50 MB and 100 MB shortcut buttons make this one click away for any smaller video.
  - The Keep-original fallback saves the user, but the "Target reached" text and the wasted wait undercut the "wow".
- **P2 (selected; full list in PRIORITIES.md):**
  - Small-target misses: audio is fixed at 128 kbps; the advice "Try Strong or 720p" is wrong for a 720p source.
  - Manual 50% grew a 10 Mbps file 4.4% despite the "caps near 90%" FAQ.
  - "Get a Day Pass to download" shows under the free Keep-original button.
  - The non-video error points to phone codecs and F12.
  - MiB vs MB units.
  - iPhone SE drop zone just below the fold (615 vs 584).
  - No `aria-pressed` on modes; the slider has no name; the result isn't announced; focus drops to body.
  - The video shows the old UI, never shows a result, has a 40 s outro, personal bookmarks and "Free" wording.
  - English titles and UI on locales.
  - VideoObject name ≠ YouTube.
  - 9 px header overflow at 320 px.

## Outcomes we want

1. Preset buttons match each platform's current published limit (with a small safety margin) and say where the number comes from.
2. Page, FAQ, blog, YouTube description and video describe the same four modes, the real default and the real pass count.
3. A target at or above the source never produces a bigger file: the tool caps it or says "already under your target", with no encode.
4. Misses explain the real reason (length × audio + minimum video bitrate) and offer a fix that works (lower audio, 480p, trim).
5. Small-phone users see the drop zone on load; screen-reader users hear the result.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS (with gaps)** | MEDIUM | 16 of 20 cases PASS; every target reached when possible; rotation, HEVC, WebM, MKV, trim, 720p all work. Above-source target grows the file (C15); small-target misses keep 128 kbps audio (C07). `findings/live-functional-findings.md` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | More modes than most; damaged-file pre-check. Missing current platform presets, a pre-encode estimate, audio/480p options. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Sensible default, clear result line, Keep original. Bigger-than-source "Target reached"; generic miss advice; Day Pass text under a free button. |
| 4 | Layout attractiveness | **PASS (minor)** | LOW | Side-by-side previews. iPhone SE drop zone just below the fold; 9 px header overflow at 320 px. |
| 5 | Payment process | **PASS** | — | Download → cap dialog → Buy Day Pass $1 → email prompt (stopped). |
| 6 | Information correct | **FAIL** | HIGH | Outdated Discord/WhatsApp presets; phantom Light option; wrong default; pass count; 200 MB vs 50 MB; Manual 90% cap claim. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, sitemap (tool and blog). **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong "target size (MB)" title and meta; 11-Q FAQPage. Thin H1 "Compress Video"; VideoObject mismatch; English locale titles; generic OG. |
| 9 | Blog post | **PARTIAL** | MEDIUM | Strong worked example; Light, 8 MB Discord, 26,214,400-byte arithmetic, missing 16 MB preset. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | j2eUOdBo3bk, 92 s, 13 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | Most answers match (output MP4/H.264/AAC, naming, trim, not-reached). Light, default mode and pass count are wrong. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old UI with Light; no result shown; personal bookmarks and files; "Free". `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Local processing; Drive gated at 0; cloud storage needs sign-in. **Untested: sign-in required.** |
| 14 | Sharing | **N/A** | — | No share button after a result (live button list: Download, Get a Day Pass, Save to Google Drive, Save to my cloud storage, New). "Share this tool" is site-wide. |
| 15 | Downloads | **PARTIAL** | MEDIUM | Output blobs verified (MP4 H.264/AAC, faststart). Keep original downloads free (correct name and bytes). Paid download with uses left **needs re-run after midnight UTC (7:00 PM ET)**. |
| 16 | Usage count | **PARTIAL / pending** | MEDIUM | Start 10/10 everywhere; Compress free (10 → 10); Download, larger-anyway and Drive gated; Keep original free (fits "your file, not a result"). Download cost pending (RERUN row 17). Counters are display-only. |
| 17 | Categorization | **PASS** | — | Video Tools; Video Edit Desk bundle. |
| 18 | Location in site | **PASS (minor)** | LOW | Breadcrumb and category card; no "Continue with" hand-off after the result. |
| 19 | AI need / demand | **PASS (no AI needed)** | — | Deterministic encode; strong demand (upload caps). |
| 20 | Merge? | **N/A: keep** | — | Distinct; cross-link Video Converter and GIF compressor. |
| 21 | Remove? | **N/A: keep** | — | Core is solid. |
| 22 | Duplicates | **PASS** | — | None. |

## Devices, platforms, countries and languages

See `evidence/findings/devices-locales-findings.md`.
- All 10 profiles return 200.
- Chromium and Firefox compress correctly.
- **WebKit/iOS processing is unverified:** Playwright WebKit on this box crashes on any `<video>` blob, even a blank control page. Check on a real iPhone/Mac.
- Locales translate the H1 only; titles and most UI stay English. /ar is a 404.
- **axe:** 0 on `main`; 1 serious name mismatch on desktop; ad-label contrast on Pixel 7.

**Ads:** keep them in reserved fixed-height slots; never between the result and Download.

## Suggested direction (interpret freely)

1. **P1: presets.** Discord 20 MB (aim about 19), WhatsApp 64 MB (aim about 60; mention "send as document for larger"), email 25 MB (aim about 18–20 for encoding overhead). Add a "last checked" note. Update the blog.
2. **P1: copy.** Remove Light everywhere (or add it back). State "Medium is selected", "up to 3 encodes" and "Up to 50 MB on trial uses, 200 MB with a pass". Update the YouTube description.
3. **P1: above-source targets.** If the target is ≥ the source size (or the source bitrate), skip the encode and say "Your video is already under X MB". Otherwise cap `-b:v` at the source video bitrate.
4. **P2:**
   - Scale audio with the target (96/64 kbps, mono) and offer 480p.
   - Make the miss advice data-driven.
   - Hide "Get a Day Pass" under Keep original.
   - Use non-video error copy without F12.
   - Use one MB unit everywhere.
   - Compact the phone header.
   - Add `aria-pressed`, a slider label and a live result line.
   - Re-record the video in a clean profile, showing a result.
   - Translate locale titles.
   - Match the VideoObject to YouTube.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Counters are display-only evidence.

## Process

Inspect CompressVideo + utils → restate → propose → implement → verify with `scripts/cv-battery.js` (+ ffprobe), `scripts/cv-gate-kbd.js`, `scripts/cv-keep.js`, `test-cases.md`, and after a reset `scripts/cv-reset.js`.
