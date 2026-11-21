Sent: 2026-11-21 18:39 ET

# FDP-81 Silence Remover (silence-remover): deep test report for Claude

- **Written:** 2026-11-21 18:37 EST (box `date`, ET). Testing ran 2026-11-21 18:22–18:37 EST.
- **Tool:** https://www.freedailypro.com/tool/silence-remover
  - TEST-ORDER row 81: **Pro**, Audio Tools, "test-plan (unranked): GSC top-50 SEO backfill 17". No duplicate group.
  - Strip, Quick Buy $1 / $4.99, "Open from Google Drive". Video z5CAZByzcc4 (92 s). Blog /blog/silence-remover "Tighten a 28-Minute Interview by Cutting Dead Air" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** the browser decodes the file; JavaScript finds quiet 20 ms windows below the threshold that last ≥ Minimum Duration; each pause is listed and can be un-ticked; Remove completely keeps ~15 ms per side, Shorten keeps 0.3/0.5/1 s; "Preview the result" builds a WAV on the page; Remove Silence encodes with FFmpeg WASM to the source family at the file's own rate; Download `desilenced_…`.
- **Testers:** desk (page, 11 FAQs, blog, JS); generated tone-burst files so every cut can be measured; Playwright guest: `zero.json` (10/10), `left.json` (0/10, try 16), `cases.json` (23), Quick Buy, Drive; video frames; matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes. Stripe ID and OAuth params redacted.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); paid pass (Day Pass email step, Monthly Stripe), incl. 50–200 MB files.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to a podcaster or teacher tightening a recording.

**Owner context:** downloads count as trial uses. Per-page-load charging is P1. A real way to save a byte-identical result at 0 uses is P1 (#62, #80).

**P1:**
- **One use per page load.** 6 files (same file twice, new MP3, new FLAC, reload + two new files) for 2 uses. Same `logUsageNow` per-load behaviour as #78 and #80. Fix once in the shared download button: charge per new result blob.
- **The free Preview is the full product.** "Preview the result — Plays here, costs nothing" renders the complete edit as a 16-bit WAV (PCM identical to the paid Download; lossless even for MP3 sources), and the result player after Remove Silence is byte-identical to the paid file. Both are `<audio controls>` without `controlsList="nodownload"`, so ⋮ → Download / "Save audio as" works at 0. Fix: `controlsList="nodownload"` + no context menu on both, or make the free Preview a short or lower-quality excerpt.

**P2 — where to look:**
- **Blog** says Remove completely keeps "about 0.15 seconds of quiet on each side" and computes ~22:12 from it; the tool (and the page FAQ) keep ~15 ms, measured 0.02–0.03 s pauses. The blog also misses the pause list, un-ticking and the free Preview.
- **Video** shows the two-slider UI and demonstrates on music, which the page advises against; "Free" title.
- **Locale pages:** H1 translated, everything else English.

**P3:**
- Gaps exactly at the minimum are found ~50% of the time (550 of 1,100 at 0.5 s), from window alignment. Consider sliding windows or a 1-window tolerance.
- "New" keeps the Pauses choice while resetting the sliders; shorten modes keep half-pause lead/trail; cap dialog mentions PDFs; iPhone SE 9 px; ja 3 px; axe desktop label-content-name-mismatch + region.

## Intent

Someone wants dead air gone without chopping words, and to hear it before paying. The detector is accurate on every test (thresholds, minimums, shorten options, un-ticked pauses, stereo, 22–48 kHz, four codecs), Auto threshold does exactly what the FAQ says, and empty or too-quiet files get clear messages. The issue is that "hear it before paying" hands over the whole file.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | All 23 cases correct. |
| 2 | Completeness | PASS | List, un-tick, Auto, shorten, Preview. |
| 3 | Ease of use | PASS | Clear messages. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | PASS | Day Pass → email; Monthly → Stripe. Stopped. |
| 6 | Information correct | PASS (minor) | Page accurate; PDF wording in dialog. |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PASS | Title 52 chars. |
| 9 | Blog | PARTIAL | 0.15 s claim and maths. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PASS | Matches code and measurements. |
| 12 | Video shows current capability | FAIL | Old UI, music demo. |
| 13 | Storage | PASS | Local only. |
| 14 | Sharing | N/A | — |
| 15 | Downloads | PARTIAL | Correct files; saveable at 0 via players. |
| 16 | Usage count | **FAIL (P1)** | Per page load. |
| 17 | Categorization in section | PASS | Audio Tools. |
| 18 | Correct section of site | PASS | Next: Audio Volume Normalizer. |
| 19 | AI need and demand | PASS | "remove silence from audio"; chat AIs can't edit audio. |
| 20 | Merge better? | No | — |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px81-live.js left` (1 POST per new result), `zero` (players not downloadable / Preview limited), `cases ONLY=M01` if the detector changes.
