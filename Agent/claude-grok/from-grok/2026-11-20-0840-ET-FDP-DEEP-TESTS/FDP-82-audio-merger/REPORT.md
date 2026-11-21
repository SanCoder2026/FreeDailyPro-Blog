Sent: 2026-11-21 18:56 ET

# FDP-82 Audio Merger (audio-merger): deep test report for Claude

- **Written:** 2026-11-21 18:55 EST (box `date`, ET). Testing ran 2026-11-21 18:41–18:52 EST.
- **Tool:** https://www.freedailypro.com/tool/audio-merger
  - TEST-ORDER row 82: **Pro**, Audio Tools, "test-plan (unranked): GSC top-50 SEO backfill 17". No duplicate group.
  - Strip, Quick Buy $1 / $4.99, "Open from Google Drive". Video 4p7PyYX44IQ (104 s). Blog /blog/audio-merger "Stitch Voice Memos Into One Clip With Natural Gaps" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** clips are listed with length and sample rate (reorder by drag or Move up/down, X removes, exact duplicates skipped). Gap (0–5 s) or Crossfade (0–5 s, capped at half of either neighbouring clip) are alternatives. FFmpeg WASM resamples everything to the first clip's rate and concatenates (or chains `acrossfade`), then encodes to "Same as first file" or MP3/WAV/OGG/M4A/FLAC. The result plays in "Listen to the result"; Download saves `merged-N-clips.ext`.
- **Testers:** desk (page, 10 FAQs, blog, JS); generated beep clips (1/2/3 kHz per clip) so the order, gaps and overlaps can be measured; Playwright guest: `zero.json` (10/10), `left.json` (0/10, try 9), `cases.json` (33), `fmtdup.json`, `big.json` (60 MB), Quick Buy, Drive; video frames; matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes. Stripe ID and OAuth params redacted.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); paid pass (Day Pass email step, Monthly Stripe), incl. the 50–200 MB combined size.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to someone joining voice memos, lecture parts or podcast takes.

**Owner context:** downloads count as trial uses. Per-page-load charging is P1. A real way to save a byte-identical result at 0 uses is P1 (#62, #80, #81).

**P1:**
- **One use per page load.** 6 files (same result twice, a new MP3 set with a 1 s gap, a new 3-clip set, then after a reload a 48 kHz set and a stereo set) for 2 uses. The FAQ promises only that the *same* result is free again in one visit. Same `logUsageNow` behaviour as #78, #80, #81. Fix once in the shared download button: charge per new result blob.
- **The free result player is the paid file.** At 10/10 Merge Audio still runs ("Merging and listening cost nothing"), and "Listen to the result" is `<audio controls>` on a blob URL with no `controlsList="nodownload"`, so ⋮ → Download / "Save audio as" works at 0. `zero-X03-result.wav` is **byte-identical** (`cmp`) to the paid `left-0-merged-2-clips.wav`; the MP3 result too (`zero-X06` = `left-2`). Fix: `controlsList="nodownload"` + no context menu (shared `Al` player), or a short or lower-quality preview.

**P2 — where to look:**
- **Bitrate claim fails with cover art.** The FAQ says MP3/OGG/M4A bitrate "never exceeds that clip". A 128 kbps MP3 with a ~1.4 MB cover picture first gives a **320 kbps** merge (`E01`), because `M()` divides the whole file size (picture included) by the length. Use the audio stream bitrate (or exclude attached pictures). The row also shows no sample rate for that MP3, so its rate is not used for resampling.
- **Blog is out of date:** "Silence between clips" with None/0.5/1/2 s (tool: Gap 0/0.25/0.5/1/2/3/5); download "01-overview-merged.m4a" (tool: `merged-3-clips.m4a`); "does not overlap them, crossfade them" (tool crossfades); "a trial use is logged when you press Merge Audio" (tool and FAQ: only at download).
- **Size copy:** drop zone says "Large files (over 500 MB) may take longer…" while a guest is blocked at 50 MB combined (`B01`), and the notice says "You've selected a file over 50.0 MB (57.2 MB)" when no single file is (two 28.6 MB files). The page never states the 50/200 MB limit; the blog does.
- **Video** shows the old UI ("Max file size: 5000MB", no gap, crossfade, format or listen step) with music demos; "Free" in the title and description.
- **Locale pages:** H1 and buttons translated; title, meta, FAQ headings and some labels English.

**P3:**
- Mono first + stereo second → mono output (the stereo clip is folded down); not documented. Stereo first upmixes mono correctly.
- A corrupt clip gives "Something went wrong… Check the browser console (F12)" without naming the clip; Merge stays enabled although that row has no length and Total length disappears.
- Cap dialog mentions "the mark from your PDFs" on an audio tool. iPhone SE 9 px overflow; ja desktop 3 px; axe desktop label-content-name-mismatch + region.

## Intent

Someone wants clips joined in the right order with a natural pause, and to hear it before spending a use. Everything measured is accurate: order, reorder, remove, every gap value (exact to 10 ms), crossfades and their half-clip cap, Total length, resampling to the first clip's rate with the note, five output formats, the duplicate skip and the file name. The issue is that "hear it first" gives away the file, and one charge covers a whole visit.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 33 cases correct except cover-art bitrate. |
| 2 | Completeness | PASS | Order, gap, crossfade, formats, preview. |
| 3 | Ease of use | PASS (minor) | Corrupt-clip message vague. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | PASS | Day Pass → email; Monthly → Stripe. Stopped. |
| 6 | Information correct | PARTIAL | 500 MB copy; "a file over 50 MB"; PDF wording. |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PASS | Title 59 chars; meta lists all features. |
| 9 | Blog | FAIL | Old options, name, "no crossfade", charge at Merge. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PARTIAL | Bitrate "never exceeds" fails with cover art. |
| 12 | Video shows current capability | FAIL | Old UI. |
| 13 | Storage | PASS | Local only. |
| 14 | Sharing | N/A | — |
| 15 | Downloads | PARTIAL | Correct files; saveable at 0 via player. |
| 16 | Usage count | **FAIL (P1)** | Per page load. |
| 17 | Categorization in section | PASS | Audio Tools. |
| 18 | Correct section of site | PASS | Next: Audio Converter. |
| 19 | AI need and demand | PASS | "merge audio files"; chat AIs can't join audio. |
| 20 | Merge better? | No | — |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px82-live.js left` (1 POST per new result), `zero` (player not downloadable), `cases ONLY=E01` (bitrate ≤ 128 kbps), `px82-big.js` (copy).
