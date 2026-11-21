Sent: 2026-11-20 22:45 ET

# Test cases: Compare Two Audio Files (audio-comparer)

- **Tool:** https://www.freedailypro.com/tool/audio-comparer
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 10:27:01 EST (box `date`, ET).
- **Files:** in `evidence/testfiles/`, or regenerate them with `scripts/make-testfiles.sh` (ffmpeg). The 67 MB oversized WAV is not shipped; the script makes it.
- **Source of expected results:** the live run on 2026-11-19 plus `CompareAudio-7uCBcun0.js`.
  - "Currently: FAIL" marks a case that fails today and should pass after the fix.
- **How to run:** use a guest or fresh temp profile only. No sign-in, no payment (stop at the email prompt or the Stripe page), no ad clicks.
  - Each Compare spends 1 trial use.
  - If the strip shows "0 remaining today" on load, open a new fresh context, or retest after midnight UTC (7:00 PM ET).
- **Trial uses:** the strip reads `Trial: 10 uses/day · N remaining today`. Counter values are display-only evidence.

---

## A. Comparison accuracy

| ID | File 1 | File 2 | Expected | Today |
|---|---|---|---|---|
| AC-01 | a440_10s.wav | a440_10s_copy.wav | 100%, "Identical audio" | PASS |
| AC-02 | a440_10s.wav | a440_10s.mp3 | 100%, "Same audio, different encoding" | PASS |
| AC-03 | a440_10s.wav | a440_10s.ogg | 100%, "Same audio, different encoding" | PASS |
| AC-04 | a440_10s.wav | a440_10s.m4a | 100%, "Same audio, different encoding" | PASS |
| AC-05 | a440_10s.wav | a440_10s.flac | 100%, "Identical audio" | PASS |
| AC-06 | a440_10s.wav | a440_10s_48k_stereo.wav | 100%, same audio; the table shows a rate/channel difference | PASS |
| AC-07 | a440_10s.wav | a440_10s_quiet.wav (−12 dB) | 100%, "Same recording, possibly a different format or quality"; LUFS differs by about 12 | PASS |
| AC-08 | a440_10s.wav | a440_8s_trim.wav | Score/verdict states that file 2 covers only 0:00–0:08 (80%) of file 1, not a plain "Same recording" | **Currently: FAIL** (100%, no coverage message) |
| AC-09 | a440_10s.wav | a440_offset05.wav | ~100%, "file 2 starts 0.50 s later", "aligned by +0.50 s" | PASS |
| AC-10 | a440_10s.wav | b880_10s.wav | 0%, "Different audio", "Differs at 0:00–0:10" | PASS |
| AC-11 | melody_12s.wav | melody_12s.mp3 | 100% | PASS |
| AC-12 | melody_12s.wav | melody_12s_edit5to7.wav | ~96–97%, "Partly the same…", "Differs at 0:05–0:07 in file 1.", red cells at 5–7 | PASS |
| AC-13 | melody_12s.wav | noise_pink_10s.wav | 0%, Different audio | PASS |
| AC-14 | a440_10s.wav | mix_440then880_10s.wav | **~50%**, "Partly the same", "Differs at 0:05–0:10"; the score agrees with the strip (5 green, 5 red) | **Currently: FAIL** (0.0% "Different audio" while the strip shows 5 green) |
| AC-15 | mix_440then880_10s.wav | a440_10s.wav | Same as AC-14, with the files swapped | **Currently: FAIL** (seen in v14c) |
| AC-16 | a440_10s.wav | long_300s.mp3 | Verdict flags the 30× length difference (e.g. "file 1 matches the first 0:10 of file 2"); 4-minute note shown | **Currently: PARTIAL** ("Same audio, different encoding") |
| AC-17 | melody_12s.wav | melody_then_noise_72s.wav | Coverage stated (file 1 = the first 12 s, about 17% of file 2); never a bare "100% Same recording" | **Currently: FAIL** |
| AC-18 | melody_12s.wav | noise20_then_melody_32s.wav | "File 1 found in file 2 at 0:20" plus coverage; offset +20.03 s | **Currently: FAIL** (100% "Same recording; file 2 starts 20.03 s later") |
| AC-19 | melody_then_noise_72s.wav | melody_12s.wav | ≤ ~17%, or "Differs at 0:12–1:12"; strip cells 12–72 red or "no counterpart", **not grey "silence"** | **Currently: FAIL** (observed 10:11 EST: 100%, 60 grey cells) |
| AC-20 | corrupt.mp3 | a440_10s.wav | Toast "Couldn't analyze one or both files…"; no trial use spent; ideally names which file | PASS (naming the file: enhancement) |
| AC-21 | notaudio.wav | a440_10s.wav | Same as AC-20 | PASS |
| AC-22 | empty.wav | a440_10s.wav | Same as AC-20 | PASS |
| AC-23 | oversized_380s_stereo.wav (67 MB) | a440_10s.wav | Warning toast with the correct size; still works; "Only the first 4 minutes…" | PASS (the toast says 64MB: MiB vs MB) |

## B. Result controls

- **AC-24, Play and switch.**
  - Steps: after AC-12, press Play file 1, then Play file 2 while it is playing, then Stop.
  - Expected: playback switches at the same moment; the buttons show the playing state; no console errors.
- **AC-25, Match loudness.**
  - Steps: the checkbox is on by default; click it.
  - Expected: it turns off; the note "Loudness match turns the louder file down by N dB" is consistent.
- **AC-26, Download the difference.**
  - Steps: after AC-12, press "Download the difference (WAV)".
  - Expected:
    - `audio-difference.wav`, 12.0 s, PCM.
    - Energy ≈ −45 dB except seconds 5–7 (≈ −10 to −12 dB).
    - Toast "Difference saved".
    - The trial count is unchanged.
- **AC-27, Copy result summary.**
  - Expected:
    - The clipboard has the file names, "Match: 96.6% - Partly the same…", "Differs at 0:05–0:07 in file 1.", the 6-row property table, and the privacy line.
    - Toast "Summary copied (text only, no audio)".
    - The count is unchanged.
- **AC-28, Share this tool.**
  - Today: it copies the bare tool URL and shows the toast "Link copied! Share it with anyone." The count is unchanged.
  - Enhancement target: an option to share a result summary link.
- **AC-29, Compare another pair / reload.**
  - Expected: both drop zones clear; no history persists; the count persists across the reload.
- **AC-30, Keyboard.**
  - Steps: Tab to drop zone 1 and press Enter, which opens the chooser; Space on zone 2 opens the chooser; Enter on Compare Audio.
  - Expected: a result is announced ("Comparison complete!").
  - **After the fix:** focus moves to the result heading, not to \<body\>.
- **AC-31, Time axis.**
  - Expected: under the waveforms, the axis reads 0:00 · mid-time · end (e.g. 0:00 · 0:06 · 0:12).
  - **Currently: FAIL** (it reads 0:00 · 0:00 · 0:12).

## C. Trial uses and upgrade path

- **AC-32, Counting.**
  - Steps: fresh context. Note the strip, add 2 files, then press Compare.
  - Expected:
    - Exactly **−1** ("10 → 9 remaining").
    - Play, Match loudness, Download, Copy, Share and Another pair leave it unchanged.
    - A reload keeps 9.
  - **Currently: intermittent FAIL.** In run 2 at 10:15:05 EST and in v21r3, one Compare went 10 → 0.
- **AC-33, Fresh device starts with 10.**
  - Steps: 5 fresh contexts in a row.
  - Expected: each shows "10 remaining today" on load.
  - **Currently: FAIL** from this box IP. Most showed "0 remaining today" with a new `dev:` scope. Retest from a residential IP too.
- **AC-34, Cap behaviour.**
  - Steps: at 0 remaining, press Compare.
  - Expected:
    - The dialog "You've used today's trial uses" with Monthly $4.99 / Day Pass $1 / access code / Compare plans / Maybe tomorrow.
    - The inline note "…Your input is still here and nothing was lost. Trial uses start again at midnight UTC…".
    - The files are still loaded.
- **AC-35, Quick Buy $1.**
  - Expected: the in-page dialog "Day Pass, $1 – Enter your email…". **Stop. Type nothing.**
- **AC-36, Quick Buy $4.99.**
  - Today: it goes straight to checkout.stripe.com. **Stop. Type nothing.**
  - Expected after the fix: the same email-first step as the Day Pass, or a deliberate, documented difference.
- **AC-37, Failed decode is free.**
  - Steps: run AC-20 and read the strip.
  - Expected: unchanged.

## D. Content, SEO and locales

- **AC-38, FAQ and Details accuracy.**
  - Expected: no text says "equal time segments / normalized time basis". The FAQ explains alignment, silence trimming, the 4-minute cap, different lengths and the strip colours.
  - **Currently: FAIL.**
- **AC-39, Blog link and accuracy.**
  - Expected:
    - The tool page links /blog/audio-comparer.
    - The blog no longer tells users to trim lead-in silence "so segments line up".
    - The blog shows the strip, waveforms and diff WAV.
  - **Currently: FAIL.**
- **AC-40, Video.**
  - Expected: the embedded video shows the current UI (strip, waveforms, A/B, diff WAV, trial strip); no "free" wording; one title across YouTube, JSON-LD and the sitemap.
  - **Currently: FAIL.**
- **AC-41, Locale pages** (/es, /pt, /fr, /de, /ja, /hi, /zh, /ko, /id).
  - Expected: `<title>`, meta, subtitle, badges, stepper, drop-zone text, the Compare Audio button and the accordion headers are translated, also in the server HTML.
  - **Currently: FAIL** (mixed).
- **AC-42, 320 px phone.**
  - Steps: iPhone SE (320×568).
  - Expected: no horizontal scroll (scrollWidth = 320); drop zone 1 starts above the fold, or the stepper collapses.
  - **Currently: FAIL** (329 px; input at y=632).
- **AC-43, Contrast.**
  - Steps: axe on the result view.
  - Expected: 0 color-contrast violations (the 11 px waveform captions are at least 4.5:1).
  - **Currently: FAIL** (9 nodes).
- **AC-44, Feedback FAB vs. ads.**
  - Steps: Firefox 1440×900.
  - Expected: the floating Feedback button does not cover any part of the right-rail ad (a reserved clear zone).
  - **Currently: FAIL.**

---

## Updates from the 2026-11-20 re-run (see RERUN-FINDINGS.md)

| ID | 2026-11-20 result |
|---|---|
| AC-19 | **Currently: FAIL** (re-confirmed 4/4 at 22:12–22:16 EST; 100%, 60 grey "silence" cells; `evidence/screens/AC19-v23r1-crop-1120.png`) |
| Usage trace | Compare −1 (10 → 9); Play, Match loudness, Download difference WAV, Copy summary, Share and reload free. PASS |
