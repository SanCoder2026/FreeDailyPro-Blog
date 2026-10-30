Sent: 2026-10-30 13:21 ET

# QA Report #127 — Addendum: admin-session results
Everything here is from an **admin session, ~13:18–13:21 ET**. Adds to report #127, B-0206–B-0208 and (for text-sorter) report #126 / B-0203. No sent file is edited.

## B-0206 text-reverser (L-268) — output verified (admin session, ~13:18–13:21 ET)
- Input `héllo 👋🏽 café`:
  - Reverse Text → `éfac 👋🏽 olléh` ✓
  - Reverse Each Word → `olléh 👋🏽 éfac` ✓
  - Reverse Words → `café 👋🏽 héllo` ✓
  - Reverse Lines → unchanged (single line) ✓
- The skin-tone modifier stays attached and the accents stay intact, so B-0206 outcome 1 (grapheme-safe) is **already met**. Claude can drop that outcome; test cases 1–2 should pass as is.
- There's no success state after an action → B-0187.

## NEW P1 — audio-to-subtitles: "make subtitles" does nothing (L-274; admin session, ~13:18–13:21 ET)
**Not a B-0156 or trial-uses issue.** It happens with unlimited use.
- **Steps:** /tool/audio-to-subtitles → choose `a.wav` (0:03, 440 Hz tone; in report-127/test-cases) → click "Download model (about 100 MB) and make subtitles", 4 times over ~60 s.
- **Expected:** a download progress bar, then SRT/VTT (or a clear "no speech found" message).
- **Actual:** nothing happens. No progress, no error, no console output, no network activity seen, no SRT/VTT.
- **Impact:** the tool's core feature is broken for everyone.
- **Ask for Claude** (added to B-0207 as outcome 0, above the others):
  - The button must start the model download with visible progress, or show a clear error.
  - A file with no speech must end with "No speech found", not silence.
- **Test cases:**
  1. Click once → progress shows within 1 s.
  2. 3 s tone → "No speech found" message.
  3. A short English speech clip → SRT and VTT download, text correct.
- The previous L-269 note (file dropped at 0 trial uses) stays a separate B-0156 item.

## B-0208 image-splitter (L-270) — verified (admin session, ~13:18–13:21 ET; tiles checked by QA with PIL)
- `ima.png` 1280×3622, 3×2 → `ima-tiles.zip` (896,283 B, in `batch-46/downloads/`) with 6 PNGs (RGBA):
  - r1c1 427×1811, r1c2 426×1811, r1c3 427×1811
  - r2c1 427×1811, r2c2 426×1811, r2c3 427×1811
- Widths add up: 427 + 426 + 427 = 1280 ✓. Heights: 2 × 1811 = 3622 ✓. No pixels lost; the uneven-split notice is accurate.
- **Note for B-0208 test case 3:** the extra pixel goes to the outer columns, with the middle one narrower. The brief said "the last tile takes the remainder". Either way works; just say so on the page.
- Names follow row-column order (r1c1…).

## B-0203 text-sorter (L-265) — open question closed (admin session, ~13:18–13:21 ET)
- Sorting in place in the single textarea is **by design**: it shows "3 lines → 3", a "Sorted!" toast and an Undo button. Closed.
- The earlier "Copy shows no toast" note (B-0187) is about Copy, not Sort, and stays.
