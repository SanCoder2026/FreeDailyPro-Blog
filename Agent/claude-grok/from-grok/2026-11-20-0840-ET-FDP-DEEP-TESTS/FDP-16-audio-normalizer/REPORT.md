Sent: 2026-11-20 08:40 ET

# FDP-16 Audio Volume Normalizer (audio-normalizer): deep test report for Claude

- **Written:** 2026-11-19 15:25:45 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/audio-normalizer. Row 16 of TEST-ORDER.md: Pro, Audio Tools, cluster C20. Test-plan rank 15: "65 views; 32 clicks pos 28; API ignores bitrate" (quoted from TEST-ORDER, not re-verified; the API was not tested). **GSC data is not available.**
- **Classification:** Professional Tool, Audio Tools. Trial-gated at Download (`gateAtDownload`). Normalizing and the full preview are not charged.
- **Testers:**
  - **Desk review:** page, locales, blog, category, the AudioNormalizer / operations / ffmpegEngine code, and Auphonic docs.
  - **YouTube video:** metadata, 37 frames, crops.
  - **Headless Playwright:**
    - 26 file × target cases, each output measured with ffmpeg (LUFS, true peak, sample peak, codec, bit depth)
    - the gate and dialogs; keyboard; axe; phones; Firefox
    - matrix: 10 profiles, 10 locales + /ar, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, nothing typed into the email or card prompts, no ad clicks, no API or MCP calls, no site or repo changes. No downloaded file was executed.
- **Sign-in:** "Save to my cloud storage" stops at a sign-in dialog on https://www.freedailypro.com/tool/audio-normalizer (feature untested). Google Drive save was gated at 0, so its Google sign-in was never reached.
- **Pending:** every context loaded at 10/10 used, so what Download costs with uses left is still unobserved. **Needs re-run after midnight UTC (7:00 PM ET).** RERUN-AFTER-RESET row 16 has been added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real code, restate the problem, push back where we're wrong, and pick the fix that fits how FreeDailyPro ships audio tools.

Code to look at (`evidence/js/`):
- `operations-DLxdtd8A.pretty.js`:
  - targets `Le` L659–702
  - gain/limiter `oe` L749–754
  - normalize `Oe` L755–849 (sample-peak `alimiter`; `volumedetect` for the Peak target; lossy margin 0.3 dB)
  - output format `he`/`Y`/`G` L141–210 (WAV = `pcm_s16le`; matched bitrate `M`)
- `ffmpegEngine-DH91Xnxx.pretty.js` L216–231: 50 MB / 200 MB limits.
- `AudioNormalizer-yjsJqUSR.pretty.js`:
  - the summary builder L95–106
  - the error handler `de`
  - the step state `targetChosen` L123
  - the target buttons (no `aria-pressed`)
  - the summary `<p>` (not live)

After you ship, rerun `scripts/an-battery.js` and `scripts/an-gate-kbd.js`. Measure the outputs with the ffmpeg lines in `scripts/README.md`, then work through `test-cases.md` (AN-01…AN-24).

## Intent

A podcaster or video maker drops a file and needs it at a platform's loudness, without clipping and without uploading it. They should leave trusting the numbers and see a clear reason to buy a pass for the download.

The core already earns that:
- Results land on target to ±0.02 LU on WAV/FLAC/MP3: −16.00, −23.00, −20.00.
- The summary is honest, measured on the saved file.
- Unreachable targets and >12 dB boosts are explained.
- ACX output is right (192 kbps CBR, 44.1 kHz).
- Processing is local, and each job takes 1–4 s.
- The 50 MB message is a good upsell.

Trust breaks where the page promises more than the engine does:
- peak ceilings broken by the "limit peaks" option
- "evens out volume" when the tool deliberately doesn't
- dead-end errors that tell users to open F12

## Why: what the evidence says

- **P1: true-peak ceilings broken.**
  - With "Limit loud peaks…" on, a −32 LUFS file with one click reaches −16.00 LUFS but **−0.51 dBTP**, against a −1.5 dB podcast ceiling (N09). `alimiter` limits sample peaks, not true peaks.
  - "Peak to −1 dB" uses sample peak: loud.wav came out at **−0.07 dBTP** (N22).
  - Platforms measure dBTP, so lossy re-encoding there can clip.
  - Without the limiter the tool *does* respect true peak (N01 −1.98, N08 −1.55), so this is a gap in one path only.
- **P1: "Even out volume levels" contradicts the tool.**
  - The subtitle, drop zone, schema description, category card and video title promise evening out, and so do About ("volume drifts up and down") and How to use ("evens out the loudness automatically").
  - The guide's own "When not to use it" says it "does not even out loud and quiet moments inside a recording".
  - Users who want a leveler will feel misled. Users who want loudness compliance won't find "LUFS" in the tagline.
- **P1: failures are dead ends.**
  - Silence, a 0.3 s clip, a non-audio file and stereo ~45 kbps Opus all show "Something went wrong… Check the browser console (F12)…" (N14, N18–N20).
  - The code already has "could not measure the loudness of this file", but it is swallowed.
  - The Opus case is a real bug: the matched bitrate becomes 32 kbps stereo 48 kHz Vorbis, which libvorbis rejects. The copy promises "OGG and Opus become OGG". Mono voice notes and 128 kbps Opus work (N25, N26).
- **P1: phone first screen (iPhone SE).** The drop zone starts at y=724 against a 584 px viewport. Normalize is at y=1166 after a file is chosen. The same pattern was P1 in FDP-14.
- **P2 (selected; full list in PRIORITIES.md):**
  - "Large files (over 500 MB)" vs the real 50 MB trial / 200 MB Pro caps.
  - 24-bit WAV saved as 16-bit while the FAQ says "a WAV stays lossless".
  - AAC overshoot: −15.67 with a "couldn't reach −16" message, and TP −1.11 against a −1.5 ceiling.
  - "first four / five of six / five" target counts.
  - Step 2 never marked done for the default target.
  - Target buttons lack `aria-pressed`; the summary isn't announced; focus drops to body.
  - The blog's wrong targets and "each normalization counts".
  - The video shows the old UI, a wrong "video" caption, a personal file list and "Free" wording.
  - English titles, meta and steps on all 9 locales.
  - The VideoObject name doesn't match YouTube.
  - The 320 px header overflows by 9 px.
  - Volume Booster / ACX Checker overlap.
- **Policy note for Santosh (not a defect):** the full normalized result plays in the preview at 0 remaining. Only Download and Drive are gated. The Oct 30 policy says results count; please confirm that "preview free, download counts" is intended for audio tools.

## Outcomes we want

1. Every target's ceiling holds in **true peak** on every path (limiter on/off, Peak target, lossy formats), and the summary reports dBTP.
2. The page, schema, category card and video describe what the tool does: loudness normalization with a constant gain. Any "even out within a file" promise is removed, or backed by a real leveler.
3. Every failure tells the user what happened and what to do, without dev tools. Common Opus files save.
4. On a small phone the drop zone is visible without scrolling, and screen-reader users hear the LUFS result.
5. Limits, bit depth and counts stated on the page match the engine.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 17 of 26 cases PASS with on-target LUFS; limiter/Peak paths break true peak; stereo low-bitrate Opus fails; silence/short/corrupt give a generic error. `findings/live-functional-findings.md`, `json/live-cases.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Six presets, honest summary, local processing, limiter, ACX format. Missing a true-peak limiter, custom LUFS, batch / multi-file matching and a within-file leveler (Auphonic has all four). |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Four clear steps, sensible default, 1–4 s jobs, good 50 MB upsell. Generic F12 errors; step 2 state; long target labels. |
| 4 | Layout attractiveness | **PARTIAL** | MEDIUM | Clean desktop. iPhone SE drop zone below the fold; 9 px header overflow at 320 px (site-wide). |
| 5 | Payment process | **PASS** | — | Download → cap dialog → "Buy Day Pass — $1" → email prompt; stopped there (`dlg-download.png`, `dlg-daypass.png`). Focus moves into the dialog. |
| 6 | Information correct | **FAIL** | HIGH | "Even out" tagline vs constant gain; promised ceilings broken (limiter/Peak/AAC); 500 MB vs 50/200 MB; "WAV stays lossless" vs 16-bit; "Opus becomes OGG" fails; target counts disagree. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, no robots block, tool and blog in the sitemap. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong LUFS title and meta, 8-Q FAQPage. VideoObject name ≠ YouTube; schema description is the contradicted tagline; generic OG image; English titles on 9 locales. |
| 9 | Blog post | **PARTIAL** | MEDIUM | /blog/audio-normalizer is a useful workflow, but "five targets", "Podcast / Spotify is -16 LUFS" and "each normalization counts" are wrong. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | WG-hQcqm-as, 111 s, 14 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | Most answers verified (before/after line, measured-on-saved-file, quieter-than-target). "first four targets" is wrong; How to use ("evens out automatically") contradicts the guide. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old UI with no targets, limiter, summary or preview; caption "Upload the video"; personal Downloads list; "Free" wording. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Local processing verified by network. Save to Google Drive gated at 0; "Save to my cloud storage" needs sign-in. **Untested: sign-in required.** |
| 14 | Sharing | **PARTIAL (unverified)** | LOW | "Share this tool" showed nothing in headless Chromium; there is no share-result feature. Check on a phone. |
| 15 | Downloads | **PARTIAL** | MEDIUM | The output blob (= Download blob) was verified for format and loudness; the file name `normalized_quiet.wav` was seen on the hand-off. The actual download with uses left **needs re-run after midnight UTC (7:00 PM ET)**. |
| 16 | Usage count | **PARTIAL / pending** | MEDIUM | Starting count 10/10 in every context. Normalize never charged (10 → 10); Download and Drive gated at 0. Cost per download **needs re-run after midnight UTC (7:00 PM ET)** (RERUN row 16). Policy note: full preview free at 0. Counters are display-only. |
| 17 | Categorization | **PASS** | — | Audio Tools; Podcast Cleanup bundle. |
| 18 | Location in site | **PASS** | — | Breadcrumb, category card, "Next: Audio Compressor" hand-off works (carries the file). |
| 19 | AI need / demand | **PASS (no AI needed)** | — | Deterministic DSP; podcast/streaming demand (test-plan rank 15). |
| 20 | Merge? | **Suggest** | LOW | Fold Volume Booster in as a "Fixed gain (dB)" mode; cross-link or route Audiobook to ACX Audiobook Checker. |
| 21 | Remove? | **N/A: keep** | — | Core is accurate and in demand. |
| 22 | Duplicates | **PARTIAL** | LOW | C20: volume-booster is a subset; the ACX target overlaps ACX Audiobook Checker. |

## Devices, platforms, countries and languages

Details: `evidence/findings/devices-locales-findings.md`.
- All 10 profiles return 200.
- Chromium and Firefox process correctly.
- **WebKit/iOS processing is unverified.** Playwright WebKit on this box crashes on any `<audio>` blob, even a blank control page (`json/webkit-control.txt`). Please check on a real iPhone/Mac.
- Locales translate the H1, breadcrumbs and strip, but the title, meta, subtitle, steps and drop zone stay English. /ar is a 404 (not in hreflang).
- **axe:** 0 on `main`; matrix: 1 serious label/name mismatch on desktop, and ad-label contrast on Pixel 7.

**Ads:** keep them in reserved fixed-height slots below the tool and in side rails. Never put one between the result and Download.

## Suggested direction (interpret freely)

1. **P1: true peak.**
   - Make the limiter true-peak aware: oversample around `alimiter` (e.g. `aresample=192000,alimiter…,aresample=<orig>`), or verify with a second loudnorm pass and trim gain until `output_tp ≤ ceiling`.
   - For the Peak target, measure true peak (`loudnorm` `input_tp` or `ebur128=peak=true`).
   - Widen the lossy margin for AAC.
   - Add "true peak X dBTP" to the summary.
2. **P1: copy.**
   - Change the tagline to something like "Set loudness to a platform target (LUFS)", and align the About, How to use, schema, category card and video title.
   - Point "even out loud and quiet parts" users to a compressor or leveler, or build one.
3. **P1: errors and Opus.**
   - Show the specific error ("This file is silent or too short to measure (needs 0.4 s+)", "This file isn't readable audio").
   - Remove "Check the browser console (F12)".
   - For Vorbis output, floor the stereo bitrate at about 64 kbps, or encode Opus input back to Opus.
4. **P1: phone.** On small screens, compress the trial strip, pass buttons and the "How it works" stepper so the drop zone is visible on load.
5. **P2:**
   - Say "Up to 50 MB on trial uses, 200 MB with a pass".
   - Keep 24-bit WAV (`pcm_s24le`), or say "saved as 16-bit".
   - Fix the AAC overshoot wording.
   - Fix the target counts.
   - Mark step 2 done for the default target.
   - Add `aria-pressed`, a polite live summary and focus on the result.
   - Fix the blog facts and trial-use line.
   - Re-record the video.
   - Translate locale titles, meta and UI, or de-list them.
   - Match the VideoObject to YouTube.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Don't change what counts as a trial use until Santosh answers the policy note.
- Counters are display-only evidence.

## Process

Inspect operations `Oe`/`oe`/`he` and AudioNormalizer → restate → propose → implement → verify with `scripts/an-battery.js` + ffmpeg measurements (true peak!), `scripts/an-gate-kbd.js`, `test-cases.md`, and, after a reset, `scripts/an-reset.js`.
