Sent: 2026-11-21 16:05 ET

# FDP-71 Audio Speed Changer (audio-speed-changer): deep test report for Claude

- **Written:** 2026-11-21 16:03 EST (box `date`, ET). Testing ran 2026-11-21 15:53–16:02 EST.
- **Tool:** https://www.freedailypro.com/tool/audio-speed-changer
  - TEST-ORDER row 71: **Professional Tool**, Audio Tools. Plan note "test-plan (unranked): GSC top-50 SEO backfill 13". No duplicate group.
  - Trial strip "Trial: 10 uses/day"; Quick Buy Day Pass $1 / Monthly $4.99 (all 6 geo contexts).
  - Video GtmKMHN9lrs (embedded, 89 s, uploaded 2026-09-23). Blogs /blog/audio-speed-changer "Review a 54-Minute Training Recording at 1.25x, Pitch Intact" (200) and /blog/free-audio-tools-voice-memos-podcast-cleanup (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `AudioSpeedChanger-Dgf8DX20.js`, shared ToolPage player/save code):**
  - Drop one audio file (drop zone `gateAtDownload`, 500 MB note). Pick a Speed (slider 0.5–4x in 0.05 steps, 9 presets) and an optional Pitch (−12…+12 semitones).
  - **Change Speed** runs ffmpeg.wasm (`@ffmpeg/core@0.12.10` from cdn.jsdelivr.net, 7.28 MB wasm transfer) in the browser. There is **no usage call**.
  - The result appears as "Listen to the result (0:05.0 long)", with the copy "Playing it here costs nothing; a trial use is only taken when you download". It plays in a native `<audio controls>` on a blob URL with **no `controlsList="nodownload"`** (ToolPage-result-player-excerpt).
  - **Download** (gated), **Save to Google Drive** (gated), **Save to my cloud storage** (sign-in + $4.99/month add-on), **New**.
  - Output format follows the input family (WAV→WAV, FLAC→FLAC, M4A/AAC/MP4→M4A, OGG→OGG, other→MP3); the name is `speed_<x>x[_pitch±n]_<name>`.
- **Testers:**
  - Desk: page copy (9 FAQs, how-to, when/when not, tips, limitations, privacy), JSON-LD, blog, JS.
  - Playwright, guest contexts. Test audio was generated in testfiles/ (make-testfiles.py): a 10.000 s 440 Hz tone with a 1 kHz click every 1.000 s as a tempo marker, in WAV/MP3/FLAC/OGG/M4A; a 48 kHz stereo WAV; a 5 s MP4 with picture; and a non-audio file.
    - `zero.json` (at 10/10), `cases.json` (at 10/10; outputs read from the player blob), `extra.json` (player menu Download at 10/10, Drive/cloud buttons), `left-firefox.json` (start 0/10), `quickbuy.json`, `drive.json`.
    - Every output was checked with ffprobe + numpy (px71-analyze.py): container, codec, sample rate, channels, duration, dominant frequency and click spacing.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe; the cloud storage dialog stopped at "Sign in"). No ad clicks. No site or repo changes. Downloads parsed, never executed.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); Save to my cloud storage (sign-in + add-on); Save to Google Drive with uses left (at the cap it opens the cap dialog); paid-pass output. Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none needed.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for someone speeding up a lecture or slowing a clip to transcribe it, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1:**
1. **The result player's own Download saves the full file at 0 trial uses.**
   - At 10/10 (extra.json): Change Speed → the native player shows a ⋮ menu with **Download** (X-player-menu.png). Choosing it saved `…wav` (441,710 B) with no usage POST, no dialog, and the counter still at 10.
   - That file is **byte-identical (md5 fd2505d99762)** to the paid Download of the same 2x WAV in the left run (L05-speed_2x_tone-10s-44k.wav).
   - Other player blobs fetched at 10/10 match paid downloads too: FLAC 2x `ac96f6c26aa7` = L08. Right-click "Save audio as" is also allowed (contextmenu not prevented).
   - Only the page's Download / Save to Google Drive buttons are gated.
   - **Fix direction:** add `controlsList="nodownload"` and block the context menu on the result `<audio>` (the shared ToolPage player). Better still, play a reduced preview (e.g. the first 15–30 s, or a lower bitrate) until a use is taken.
2. **Charging happens once per page load; after it, everything in that page is free.**
   - left-firefox.json (start 0/10): the first Download sends one `usage.log` POST (0→1/10). Then in the same page, these were all saved with no POST: the same file again, a **new 2x result**, a **new MP3** at 0.5x (via New), and a **new M4A** at 1.25x +12 semitones.
   - After a reload, one more POST (1→2/10), then the next download was free. That is 7 files from 4 different source files for 2 uses.
   - **Fix direction:** charge per download of a new result, not per page load.

**Owner question (pending):**
- **The full-quality result plays at 0 by design.** The page says "Playing it here costs nothing; a trial use is only taken when you download" (also in the FAQ and how-to).
  - The Oct 30 rule says viewing results counts. Here a guest at 10/10 hears the complete processed file (any length, any speed/pitch), so the page and the rule disagree.
  - Owner to decide: keep free full playback (then fix P1.1 so it can't be saved), or count Change Speed, or limit the preview.

**P2 — where to look:**
- **Blog is out of date:**
  - "If you want a higher or lower voice at the same pace, that is a pitch tool, not this one": the tool now has a Pitch slider.
  - "The Change Speed button stays disabled at exactly 1x": it is enabled at 1x when the pitch moves.
  - "A run counts toward your 10 trial usages a day": only downloads count.
  - "The output matches your input format": MP4/AAC/Opus/other types change family.
  - Its timing maths (54:00 → 43:12 at 1.25x, 30:51 at 1.75x, 21:36 at 2.5x) is correct.
- **Video GtmKMHN9lrs** shows an older UI: presets only to 2x, no Pitch slider, no result player, "What is this tool?" layout, "Search 200+ tools". Title "Free Step-by-Step Walkthrough", "Try … free", tags "free online tools", "PDF tools", end card "200+ Free Productivity Tools". Wording should be Professional Tools / trial uses.
- **Non-audio file:** `not-audio.mp3` is accepted (no duration in the label). Change Speed runs about 75 s, then the toast says "Something went wrong processing this audio file. **Check the browser console (F12)** for the specific error…". Reject it at upload (the duration read already fails) and drop the F12 advice.
- **Locale pages** (es screenshot): H1, breadcrumb and strip translated; tagline, "Runs on your device", the engine line, "HOW IT WORKS" steps, drop zone, "Ad-free: …" and the FAQ stay English.
- **SEO:** title "Change Audio Speed Without Pitch Change | FreeDailyPro" is good. Meta (84 chars) "Fast, right in your browser." misses the 0.5–4x range, pitch slider and formats. Blog slug contains "free-audio-tools".

**P3:**
- iPhone SE: the drop zone is below the fold (strip, engine line and HOW IT WORKS card come first); 9 px horizontal overflow (header button). ja desktop 1369 px.
- Drop zone on phones reads "Tap to choose an audio file / or tap to choose" (duplicate line).
- The page says the engine is "around 25 MB"; the measured transfer is 7.28 MB wasm + small JS (compressed). "Around 25 MB unpacked" would be accurate.
- axe desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×2 on the ad caption (keep reserved ad slots; fix the caption colour).
- de-DE/fr-FR consent banner over the bottom of the fold (screenshot).

## Intent

Someone wants a recording faster or slower without chipmunk voices, sometimes with a pitch shift, in the original format. The processing is exact; the trial gate leaks through the result player and charges once per page.

## What works (verified, numpy + ffprobe)

- **Speed exact, pitch held:** WAV 2x → 5.007 s, 440 Hz, clicks every 0.50 s. 1.5x → 6.668 s / 0.67 s. 4x → 2.505 s / 0.25 s. FLAC 2x → 5.007 s. OGG 3x → 3.342 s / 0.33 s. M4A 0.5x → 19.992 s / 2.0 s. MP3 0.5x → 19.982 s. All stayed at 440 Hz.
- **Pitch slider:** +12 at 1x → 880 Hz, 9.979 s; +12 at 1.25x (M4A) → 880 Hz, 8.011 s; −12 at 1.25x (48 kHz stereo) → 220 Hz, 8.001 s, **48 kHz stereo kept**.
- **Formats/names:** WAV→pcm_s16le WAV, FLAC→FLAC, OGG→Vorbis, M4A→AAC M4A, MP3→MP3, MP4 video → audio-only M4A (as the FAQ says). Names like `speed_1.25x_pitch+12_tone-10s.m4a`.
- **UI:** label shows old → new length; Change Speed disabled at 1x with pitch 0; slider End/Home = 4x/0.5x. Engine loads once (about 2.3 s per 10 s file after that).
- **Gate on a fresh page at 10/10:** Download and Save to Google Drive open the cap dialog. Quick Buy: Day Pass → email dialog (stopped), Monthly → Stripe (stopped).
- **Layout:** 10 devices 200; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Tempo 0.5–4x, pitch ±12, format kept. |
| 2 | Completeness | PASS (minor) | Whole file only (documented). |
| 3 | Ease of use | PASS (minor) | Clear; non-audio fails late with F12 advice. |
| 4 | Layout | PASS (minor) | SE drop zone below fold, 9 px overflow. |
| 5 | Payment process | PASS | Strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | PARTIAL | Blog outdated; engine size. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PARTIAL | Meta thin. |
| 9 | Blog | PARTIAL | Pitch / 1x / "a run counts" / format lines outdated. |
| 10 | YouTube video | PASS | GtmKMHN9lrs embedded. |
| 11 | FAQ / guide correct | PASS | Page FAQs match the live tool. |
| 12 | Video shows current capability | FAIL | Old UI; "free" wording. |
| 13 | Storage | N/A (sign-in) | Cloud storage needs sign-in + add-on. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | Exact, correct format and name. |
| 16 | Usage count | **FAIL (P1)** | Player Download free at 0; one charge per page load. |
| 17 | Categorization in section | PASS | Audio Tools / Professional. |
| 18 | Correct section of site | PASS | Related links 200 (audio-to-subtitles, extract-audio, audio-trimmer). |
| 19 | AI need and demand | PASS | "change audio speed without changing pitch", "speed up audio". |
| 20 | Merge better? | No | Pairs with video-speed-changer but distinct. |
| 21 | Remove? | No | GSC top-50 backfill; working tool. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `px71-extra.js` (player menu should have no Download at 10/10) and `px71-live.js zero`.
- `TRIES=40 px71-live.js left` (each new result's download charged).
