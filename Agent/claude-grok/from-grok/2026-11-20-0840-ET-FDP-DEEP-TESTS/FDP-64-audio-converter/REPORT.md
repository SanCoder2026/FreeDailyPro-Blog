Sent: 2026-11-21 14:10 ET

# FDP-64 Audio Converter (audio-converter): deep test report for Claude

- **Written:** 2026-11-21 14:07 EST (box `date`, ET). Testing ran 2026-11-21 13:37–14:06 EST.
- **Tool:** https://www.freedailypro.com/tool/audio-converter
  - TEST-ORDER row 64: **Professional Tool**, Audio Tools. Plan note "test-plan (unranked): SEO backfill 9". No duplicate group.
  - Terms on the page: 10 trial uses a day, $1 Day Pass or $4.99 a month.
  - Video Ux4d3tMWQx4 (embedded, 76 s, uploaded 2026-09-23). Blog /blog/audio-converter "Convert a WAV Master to MP3 Without Guessing the Bitrate" (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `AudioConverter-CCPU340M.js`, `ffmpegEngine`, `BatchRunner`):**
  - One file or Several files (ZIP). Drop audio or a video. Output MP3 (default), WAV, OGG, M4A, FLAC. Quality buttons for lossy outputs: Same as original / High / Standard / Small.
  - Convert runs ffmpeg.wasm (`@ffmpeg/core@0.12.10` from cdn.jsdelivr.net) on the device. The result shows a summary line and an `<audio controls>` player, then Download, Save to Google Drive, Save to my cloud storage, Continue with Audio Trimmer, Convert again, New file.
  - Charge point: Download (`gateAtDownload`; `tryUse` once per tool per page load). Convert is never charged.
- **Testers:**
  - Desk: page copy (9 FAQs, how-to, limits, privacy), JSON-LD, blog, JS.
  - Playwright with ffmpeg-built test files (`make64.sh`: 12 s stereo WAV, tagged MP3 with cover, tagged FLAC, M4A, OGG, WMA, MP4 with/without audio, text renamed .mp3, 6 batch WAVs, noise OGGs). Outputs checked with ffprobe and md5.
    - `zero-capped.json` (Chromium) + `zero-capped-firefox.json`: at the cap (10/10). `zero-firstrun-had-uses.json`: same flow in a context that had uses left.
    - `left.json` / `left-firefox.json`: fresh contexts with 10 uses left.
    - `batch.json` (uses left) and `batch-cap.json` (at the cap); `batch-run1.json` (6-file limit check).
    - `cases.json`, `extra.json`, `big.json`, `drive.json`, `quickbuy.json`.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** "Open from Google Drive" opens Google sign-in (stopped). "Save to my cloud storage" opens a "Sign in with your email first" dialog (stopped). Paid-pass output stopped at the email prompt and Stripe. All in SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none. Behaviour with uses left and at the cap was observed today.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for someone who needs one file in the format a platform demands, and whether the tool makes them want the pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is a P1 gate gap; a full-quality result or preview at 0 trial uses is a pending owner question; a real save or download at 0 uses is P1 (Nov 21, corrected by the Orchestrator at 1:19 PM).

**P1 — where to look:**

1. **At 0 trial uses the converted file is fully saveable from the result player.**
   - At the cap (zero-capped.json, Chromium and Firefox) Convert still runs, and the result is placed in `<audio controls src=blob:>` with no `controlsList="nodownload"` and no context-menu block (`Al` in ToolPage; no `controlsList` anywhere in the bundle). Only the Download button opens the cap dialog.
   - The player's blob is **byte-identical** to the file the gated Download gives: md5 `7e24a7ecf8ff…`, 289,689 bytes, 192 kbps MP3 in both `zero-player-blob.mp3` (cap) and `tone-12s.mp3` (a real Download with uses left). Same for FLAC.
   - Chrome's player ⋮ menu has "Download", and right-click → "Save audio as…" works in Chrome and Firefox. Headless can't click the browser's own menu, so this part is code plus standard browser behaviour. A 10-second manual check confirms it (screens/cases/Z02-converted-capped.png shows the ⋮ button).
   - This is the "Save video as" case from FDP-62: a real save at 0, so P1. Options: `controlsList="nodownload"` + `onContextMenu` prevent, and/or play only a short excerpt at 0 uses.
2. **Per-page-load charging.**
   - left.json (Chromium): MP3→M4A Download → one `usage.log` POST, 0→1/10.
   - Convert again → OGG → Download: saved, **no POST**, still 1/10 (L05). New file (FLAC→MP3) → Download: saved, no POST (L07).
   - After a reload, the next Download charged (1→2/10, L09). Firefox identical (left-firefox.json).
   - Same mechanism as FDP-61/62/63. Decide on one use per converted file (batch stays one use as the copy promises).

**Owner question:** none beyond the P1 above (the playable result at 0 would be an owner question on its own; it is P1 here only because the player saves the exact file).

**P2 — where to look:**
- **Size limit copy contradicts the code:** the drop zone says "Large files (over 500 MB) may take longer or run out of browser memory", but a 60.6 MB WAV on the trial is blocked: "trial use supports up to 50.0 MB. Upgrade to Pro for up to 200.0 MB", Convert disabled (big.json, big-63mb.png; `checkFileSize` R=50 MB, g=200 MB). The blog has the right numbers. Say 50 MB on the trial / 200 MB with a pass, and use the pass names, not "Pro".
- **Video Ux4d3tMWQx4 is outdated and leaks the presenter's folder:** old UI (no One file / Several files, no player row), a Windows file dialog showing the presenter's Downloads folder with third-party "no-copyright" track names (frames f003–f004), thumbnail "FREE • IN BROWSER", title "Free Step-by-Step Walkthrough", description "Try … free", tag "PDF tools", end card "200+ Free Productivity Tools". Re-record in a clean profile with a prepared test file.
- **Locale pages:** H1, breadcrumb, trial strip, Quick Buy and the Drive button are translated. Subtitle, the on-device note, One file / Several files, drop zone text and the FAQ stay English (es screenshot).
- **SEO:** meta description 74 chars (short; no mention of video-to-audio, batch ZIP or tags). Generic OG image. Title 59 chars, fine.

**P3:**
- **Low-bitrate OGG → OGG fails:** a 32 kbps stereo OGG ("Same as original" → 32 kbps) gives "Something went wrong processing this audio file" (cases.json C06); 48 kbps mono and 112 kbps stereo OGG→OGG work (extra.json). Clamp the Vorbis bitrate to a working minimum.
- **How-to says every lossy choice shows "an approximate kbps figure and estimated size"**: for MP3/OGG only "Same as original" shows it; High/Standard/Small show nothing (extra.json). M4A shows all four (big.json). The blog explains why (VBR); align the page.
- **Cap dialog wording:** for an audio download it says "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images." Irrelevant here.
- **"Guides and next steps"** links "Text to Speech API: Weighted Calls and Trial Limits Explained", which is off-topic for a converter.
- **Phones:** drop zone reads "Tap to choose an audio file to convert / or tap to choose" (repeated). iPhone SE 9 px overflow from the header menu button (screenshot).
- **axe:** desktop label-content-name-mismatch (serious), link-in-text-block ×4 (serious), region (moderate). Pixel 7 color-contrast ×1 (ad caption; keep reserved ad slots, fix the caption colour). ja desktop 1369 px (site-wide).

## Intent

Someone has a WAV, M4A, FLAC or a video and a platform that wants MP3 (or the reverse). They want the right file in seconds, without uploading a voice memo or client audio. If it works first time, $1 for a day of batch conversions is easy.

## What works (verified)

- **Conversions (ffprobe):** WAV→MP3 192 kbps (lossless source rule), WAV→FLAC, MP3→M4A AAC 131 kbps, MP3→OGG Vorbis, FLAC→MP3, M4A→MP3 96 kbps ("matched to the original"), WMA→MP3, MP4 sound → MP3, WAV→WAV named `tone-12s-converted.wav` (bit-identical size).
- **Tags and cover:** title/artist kept in M4A, MP3, FLAC and OGG; cover kept in M4A (mjpeg), MP3 (png) and FLAC, not OGG, as the FAQ says.
- **Rejections:** text renamed .mp3 → "Couldn't read this audio file… Nothing was used from your trial", Convert off. Video without audio → "This video has no audio track… Nothing was used from your trial".
- **Batch:** 6 files → 5 kept with the toast "A batch takes up to 5 files on the trial"; Convert all; one charge for row downloads + ZIP (batch.json: 0→1/10, ZIP holds 5 MP3s); at the cap a row download opens the cap dialog (batch-cap.json).
- **Engine:** fetched from cdn.jsdelivr.net only; no audio sent anywhere (no POST except usage.log on Download).
- **Hand-off:** Continue with Audio Trimmer opens /tool/audio-trimmer with "Use the result from Audio Converter: tone-12s.mp3" (no charge; Trimmer's own gate not tested here).
- **Gate:** Download and Save to Google Drive at the cap → "Today's trial uses are done" ($4.99 / $1). Quick Buy: Day → email prompt (stopped); Monthly → Stripe (stopped).
- **Layout:** tool above the fold on desktop and phones; Firefox/WebKit/iPad load fine. Geo: same prices everywhere; consent banner in de-DE (screenshot) does not cover the tool.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 5 outputs, video sound, WMA, tags/cover, batch. |
| 2 | Completeness | PASS | Near CloudConvert/online-audio-converter basics; no sample-rate/channel options. |
| 3 | Ease of use | PASS | Clear flow; low-bitrate OGG→OGG error is vague. |
| 4 | Layout | PASS (minor) | Above the fold; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog; Day email prompt; Monthly → Stripe (stopped). |
| 6 | Information correct | PARTIAL | 500 MB drop-zone claim vs 50/200 MB limits; estimate claim. |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 74 chars, generic OG. |
| 9 | Blog | PASS | Accurate (limits, VBR, tags, -converted). |
| 10 | YouTube video | PASS | Ux4d3tMWQx4 embedded + VideoObject. |
| 11 | FAQ / guide correct | PASS (minor) | 9 FAQs match behaviour; how-to estimate line overstated. |
| 12 | Video shows current capability | FAIL | Old UI, presenter's Downloads folder, "free" wording. |
| 13 | Storage | Sign-in | "Save to my cloud storage" needs sign-in + add-on (untested). |
| 14 | Sharing | Sign-in / N/A | Save to Google Drive gated at cap; tool link share only. |
| 15 | Downloads | PASS | All outputs valid (ffprobe). |
| 16 | Usage count | FAIL (P1) | Once per page load; result saveable from the player at 0. |
| 17 | Categorization in section | PASS | Audio Tools / Professional. |
| 18 | Correct section of site | PASS | Links Extract Audio, Compressor, Trimmer, Universal File Converter. |
| 19 | AI need and demand | PASS | Very high ("wav to mp3", "m4a to mp3"). |
| 20 | Merge better? | No | Extract Audio overlaps on video sound but adds time range; keep both, cross-linked. |
| 21 | Remove? | No | Core utility. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `SUF=-capped TRIES=20 px64-live.js zero` (player should not offer a save at 0; Convert may still run).
- `TRIES=40 px64-live.js left` (expect a charge per converted file; cap after 10).
- `px64-big.js` (drop-zone text matches the limit), `px64-live.js cases` (C06 OGG→OGG).
