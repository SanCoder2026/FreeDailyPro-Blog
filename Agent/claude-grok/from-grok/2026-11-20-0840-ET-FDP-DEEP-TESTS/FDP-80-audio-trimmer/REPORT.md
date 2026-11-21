Sent: 2026-11-21 18:23 ET

# FDP-80 Audio Trimmer (audio-trimmer): deep test report for Claude

- **Written:** 2026-11-21 18:21 EST (box `date`, ET). Testing ran 2026-11-21 18:03–18:21 EST.
- **Tool:** https://www.freedailypro.com/tool/audio-trimmer
  - TEST-ORDER row 80: **Pro**, Audio Tools, "test-plan (unranked): GSC top-50 SEO backfill 17". No duplicate group.
  - Strip "Trial: 10 uses/day", Quick Buy $1 / $4.99, "Open from Google Drive". Video pc4DDk1feTg (80 s). Blogs /blog/audio-trimmer and /blog/make-srt-vtt-subtitles-from-audio (both 200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** drop audio or video → browser player + waveform → range slider (0.1 s) and Start/End boxes → Keep or Remove selection, fades, Ringtone (30 s) → FFmpeg WASM (~25 MB from jsDelivr) re-encodes in the same format family → "Listen to the result" player → Download (`trimmed_` / `cut_`). Guest file limit 50 MB, paid 200 MB.
- **Testers:** desk (page, 11 FAQs, JSON-LD, 2 blogs, JS); generated beep files (`make-testfiles.py`) so every output's cut points can be measured (`analyze.py`); Playwright guest: `zero.json` (Chromium 10/10), `left.json` (Chromium 0/10, try 25), `left-firefox.json` (40 tries, none), `cases.json` (29 cases), Quick Buy, Drive; video frames; matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes. Stripe ID and OAuth params redacted.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); paid pass (Day Pass email step, Monthly Stripe) incl. the 200 MB limit.
- **RERUN-AFTER-RESET:** none (uses-left observed in Chromium).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to a podcaster, teacher or creator cutting a clip to the exact moment.

**Owner context:** downloads count as trial uses. Per-page-load charging is P1. A real way to save a byte-identical result at 0 uses is P1 (#62 "Save video as" precedent).

**P1:**
- **One use per page load.** At 0/10: the first Download charged (1 POST). Then a re-trim, a Remove-section result, a new WAV and a repeat Download were all free; after a reload one charge, then free again. 7 files, 2 uses. Likely the page-level "already logged" flag from `logUsageNow`. Fix: charge per Download of a new result (blob), or per trim.
- **Result saveable at 0 uses.** At 10/10 Trim runs and the result player appears. It's `<audio controls>` on a blob URL without `controlsList="nodownload"`; Chrome's ⋮ menu offers Download and right-click offers "Save audio as". Its bytes equal the gated Download exactly (`cmp`: `zero-X06-player.mp3` = `left-cut_beeps20.mp3`). Fix: `controlsList="nodownload"` + `onContextMenu` prevent (limits casual saving), or gate Trim itself at 0 / play a preview only.

**P2 — where to look:**
- **Hundredths of a second are silently lost.** Type Start 3.25 + Enter: the box redisplays "0:03.3" while the state is 3.25 (summary "Keeping 0:04.3"). Pressing Trim blurs the box, `TimeRangeFields` re-parses the rounded text and the cut starts at 3.3 s: every output is 4.2 s with the first beep at 0.70 s instead of 0.75 s (7 formats; also when End is typed first, T10). The FAQ promises "any decimal value" and an exact cut. Fix: don't re-parse on blur unless the text changed, or format the box with 2–3 decimals.
- **Size limit copy.** Drop zone: "Large files (over 500 MB) may take longer". Guests are blocked above 50 MB (63 MB WAV: "trial use supports up to 50.0 MB… Upgrade to Pro for up to 200.0 MB", Trim disabled). The blog says 50/200 correctly.
- **Blog /blog/audio-trimmer** predates Remove selection: "it cannot delete a cough from the middle"; "Selected: 1:30 of 52:10" (now "Keeping…"); "puts the old value back" (FAQ: keeps what you typed).
- **Video pc4DDk1feTg:** old UI, no waveform/Keep-Remove/fades/Ringtone; "Free" title.
- **Locale pages:** H1 and buttons translated; title, meta, section heads and all FAQ English.

**P3:**
- "0:05:10" is read as 5 s (only two `:` parts) with the confusing "end (0:05) must be after the start (0:05)"; long podcasts are where people type h:mm:ss. "2,5" → 2 silently.
- A 0.05 s selection shows "Keeping 0:00.0" and outputs 0.1 s.
- Remove mode saves `cut_…` (FAQ/blog: `trimmed_`); the mode stays on Remove after "New".
- The cap dialog here says a pass removes the mark "from your PDFs".
- iPhone SE 9 px; ja desktop 3 px; axe desktop label-content-name-mismatch + region.

## Intent

Someone needs one exact slice of a recording, fast and private. The engine delivers: cuts land on the right sample at tenths in WAV, MP3, FLAC, M4A, OGG, Opus and MP4, Remove-section joins cleanly, fades and caps work, tags and cover art survive, and every bad input gets a clear message that says no trial use was taken. The gaps are the gate (one use per page load, and the result player is the file) and the quiet loss of hundredths that the FAQ promises.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Exact at 0.1 s in 7 formats; remove + join. |
| 2 | Completeness | PASS | Keep/Remove, fades, ringtone, waveform, video input. |
| 3 | Ease of use | PARTIAL | Hundredths lost; h:mm:ss misread. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | PASS | Day Pass → email dialog; Monthly → Stripe. Stopped. |
| 6 | Information correct | PARTIAL | "any decimal value"; 500 MB text; PDF mark in dialog. |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PASS | Title 58 chars. |
| 9 | Blog | PARTIAL | Pre-Remove-selection claims. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PARTIAL | See 6; `trimmed_` name. |
| 12 | Video shows current capability | FAIL | Old UI. |
| 13 | Storage | PASS | Local only; engine from jsDelivr. |
| 14 | Sharing | N/A | Download + share sheet only. |
| 15 | Downloads | PARTIAL | Correct files; saveable at 0 via player. |
| 16 | Usage count | **FAIL (P1)** | Per page load. |
| 17 | Categorization in section | PASS | Audio Tools. |
| 18 | Correct section of site | PASS | Next: Audio Merger. |
| 19 | AI need and demand | PASS | "trim audio online", "cut mp3"; chat AIs can't edit audio files. |
| 20 | Merge better? | No | Ringtone Maker is the M4R variant; keep separate. |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px80-live.js left` (1 POST per new result's Download), `zero` (player not downloadable), `cases` with `ONLY=F01|T10` → `analyze.py` first beep 0.75 s.
