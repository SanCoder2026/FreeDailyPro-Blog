Sent: 2026-11-20 08:40 ET

# Compare Two Audio Files: live functional, trial-use and paywall findings

- **Written:** 2026-11-19 10:25:10 EST (box `date`, ET).
- **Tester and method:** headless Playwright, Chromium 159, guest only. Fresh contexts, no sign-in, no ad clicks, no payment.
- **Test audio:** generated with ffmpeg (`scripts/make-testfiles.sh`) and uploaded with `setInputFiles`.
- **Counter values:** read from the visible strip, localStorage `fdp-usage-v1`, and the page's own `usage.check` responses (observed passively). **They are display evidence only; no backend claims are made.**
- **Box restore.** The box was restored from a snapshot at about 10:10 EST. Some artefacts made between about 10:05 and 10:12 were lost, and their runs were repeated at 10:14–10:22. One observation (pair 23, below) could not be re-captured because every fresh context was then capped. It is marked as such.

## 1. Comparison accuracy (check 3)

Sources: `json/pairs-results.json`, `json/verify-pairs*.json` and the `live/` screenshots. Each comparison took about 0.5 s.

| # | File 1 vs File 2 | Score / verdict (live) | Expected | Result |
|---|---|---|---|---|
| 1 | a440_10s.wav vs byte copy | 100% Identical audio | identical | PASS |
| 2–4 | WAV vs MP3 / OGG / M4A | 100% Same audio, different encoding | same | PASS |
| 5 | WAV vs FLAC (lossless) | 100% Identical audio | identical samples | PASS |
| 6 | 44.1k mono vs 48k stereo | 100% Same audio, different encoding | same | PASS |
| 7 | vs −12 dB copy | 100% Same recording, possibly a different format or quality | same, quieter | PASS |
| 8 | 10 s vs its first 8 s | 100% Same recording…; the table shows Duration *Different* | should say "file 2 covers 80% of file 1" | PARTIAL (MED) |
| 9 | vs 0.5 s delayed copy | 100%, "file 2 starts 0.50 s later", "aligned by +0.50 s" | offset found | PASS (strong) |
| 10 | 440 Hz vs 880 Hz | 0% Different audio, differs 0:00–0:10 | different | PASS |
| 11 | melody WAV vs MP3 | 100% | same | PASS |
| 12 | melody vs the same with 0:05–0:07 replaced by noise | **96.6%** "Partly the same: most of it matches, but some parts differ", "Differs at 0:05–0:07 in file 1." | partial, localised | PASS (strong) |
| 13 | melody vs pink noise | 0% | different | PASS |
| **14** | 440 Hz 10 s vs 440 Hz for 0–5 s then 880 Hz | **0.0% "Different audio"**, while the strip and text say "Differs at 0:05–0:10" (first 5 s green) | ~50%, "Partly the same" | **FAIL (HIGH)**, seen 3 times (`pair14.png`, `v14b-full.png`, `v14c-full.png`) |
| 15 | melody vs sine | 0% | different | PASS |
| 16 | 10 s A440 vs 300 s A440 MP3 (same tone, 30× longer) | 100% "Same audio, different encoding", plus "Only the first 4 minutes…" and "File 2 runs longer than file 1; the extra is not drawn." | flag the 30× length difference | PARTIAL (MED) |
| 17–19 | corrupt MP3 / text as .wav / 0-byte .wav | toast "Couldn't analyze one or both files — make sure they're valid, playable audio files."; no trial use counted | clear error | PASS (LOW: doesn't say which file) |
| 20 | 67 MB, 380 s stereo WAV | 100% plus toast "This file is 64MB, larger than 50MB… It'll still work…" and the 4-minute note | warn, still works | PASS (LOW: "64MB" vs 67 MB on disk, MiB vs MB) |
| **21** | melody 12 s vs melody + 60 s pink noise (72 s) | **100.0% "Same recording, possibly a different format or quality"**, with only the small note "File 2 runs longer than file 1; the extra is not drawn." (`v21r2-full.png`, `v21r3-full.png`) | "file 1 matches the first 12 s of file 2 (17%)" | **FAIL (HIGH)**: 83% of file 2 is unrelated audio |
| **22** | melody 12 s vs 20 s noise + melody (32 s) | **100.0% "Same recording; file 2 starts 20.03 s later"** (`v22r1-full.png`) | offset found (good), but 62% of file 2 is noise | **FAIL (HIGH)**: verdict ignores coverage |
| 23 | melody + 60 s noise (72 s) as file 1 vs melody 12 s | Observed live at about 10:11 EST: **100.0% "Same recording, possibly a different format or quality"**. The strip showed 12 green cells and **60 grey cells, whose legend means "silence"**, although those 60 s are loud pink noise. The difference waveform was solid red for 0:12–1:12, and there was **no "Differs at" line**. | ≤17%, "Differs at 0:12–1:12" | **FAIL (HIGH)**. The screenshot was lost in the box restore. Ten re-runs (10:16–10:21 EST) all loaded capped, so re-verify with REPRODUCE.md step 4 after the midnight-UTC reset |

### Why 14 and 21–23 matter

- People open this tool to ask "is this the same recording or take?" and trust the big number.
- In pair 14, half the audio is identical, yet the score says 0.0% "Different audio". That contradicts the tool's own strip.
- In pairs 21–23, a 12-second clip is a 100% "Same recording" with a file that is mostly unrelated audio.
- Competitors report coverage explicitly; for example, Equivl reports a clip found inside a longer file, with coverage.
- Also seen: the time axis under every waveform reads "0:00 | 0:00 | 0:12", so the middle label is stuck at 0:00 (LOW).

## 2. Result controls (checks 3, 4, 5)

Two full runs in fresh uncapped contexts (`json/usage-results.json`, 10:14–10:15 EST): melody_12s.wav vs melody_12s_edit5to7.wav. Both runs gave identical results.

| Control | Live behaviour | Result |
|---|---|---|
| Compare Audio | 96.6%, Partly the same, "Differs at 0:05–0:07 in file 1.", toast "Comparison complete!" | PASS |
| Play file 1 / Play file 2 | Buttons "Play file 1 \| Play file 2 \| Stop"; switching works, no errors. Audible output can't be verified headless. | PASS (UI) |
| Match loudness | on by default → off on click | PASS |
| Download the difference (WAV) | `audio-difference.wav`, 1,152,044 B, pcm_s16le, 48000 Hz mono, 12.000 s; toast "Difference saved". Per-second RMS ≈ −45 dB everywhere except **seconds 5–7 (−12.2 / −9.7 / −11.8 dB)**, which is exactly the edited region. | PASS (content verified). Note: inputs were 44.1 kHz and the export is 48 kHz (browser decode rate; the page footnote explains this) |
| Copy result summary | Clipboard holds a plain-text report: file names, "Match: 96.6% - Partly the same…", "Differs at…", the property table, and "Compared in the browser at freedailypro.com/tool/audio-comparer; no audio was uploaded." Toast "Summary copied (text only, no audio)". | PASS |
| Share this tool | Copies the bare `https://www.freedailypro.com/tool/audio-comparer`; toast "Link copied! Share it with anyone." **No result link.** | PARTIAL (MED) |
| Compare another pair | Clears both drop zones | PASS |
| Keyboard | Drop zones have `tabindex=0`; Enter and Space open the file chooser; focus ring visible; Compare works by Enter. Live regions announce "Comparison complete!" and "All steps done." **Focus drops to \<body\> after Compare.** | PASS / LOW |
| Per-second strip | Cells have only a `title` tooltip ("0:00–0:01: matches"), which needs hover and does nothing on touch. Meaning is by colour only. The "Differs at…" text carries the info. Waveforms are `role=img` with labels. | PARTIAL (LOW) |
| Open from Google Drive | Needs a Google login. **Not tested**; Santosh would log in at https://www.freedailypro.com/tool/audio-comparer | NOT TESTED |

## 3. Storage and history (check 5)

- After **Compare another pair** and after a **reload**, both drop zones are empty. There is no recent-comparisons history.
- Inputs survive a blocked Compare, with the note "Your input is still here and nothing was lost".
- localStorage holds only `fdp-usage-v1`.
- This is consistent with the "Files never stored" badge.

## 4. Trial-use counting (check 6). Display evidence only.

| Step | Run 1 (10:14:37–10:14:57 EST) | Run 2 (10:15:02–10:15:22 EST) |
|---|---|---|
| on load | 10 remaining (usageToday 0) | 10 remaining (usageToday 0) |
| file 1 / file 2 added | 10 | 10 |
| **Compare Audio** | **9** (usageToday 1) | **0 (usageToday 10, allowed:false)** after ONE compare |
| Play / Match loudness / Download / Copy / Share / Another pair | 9 | 0 |
| after reload | 9 (persisted) | 0 (persisted) |

- **Intended rule (seen in run 1):** 1 Compare = 1 trial use. Downloads, copy, share, playback and failed decodes don't count.
- **Jump on a single Compare.**
  - Run 2 went from 10 remaining to **0 remaining after a single Compare**. v21r3 did the same (usageToday 0 → 10).
  - Earlier long contexts jumped 7 → 10 on one Compare (pairs 8 and 16, `pairs-results.json`).
  - A first-time user can be blocked after one use. Display-only; the cause is unverified. It may be a device scope merged with a shared per-IP pool.
- **Fresh contexts load already capped** ("0 remaining today", `usageToday:10`) with a brand-new `dev:<uuid>` scope:
  - 4/4 contexts at 09:57 (`pool-probe-*.json`)
  - 3 of 4 at 10:15 (`a11y-result.json`)
  - 7 of 10 matrix device runs and 6 of 6 geo contexts (10:14–10:22)
  - 10 of 10 re-runs of pair 23 (10:16–10:21)
- A real visitor behind a shared IP (office, school, mobile carrier NAT) **may see "0 remaining" before using the tool once**. Severity HIGH.
- Caveat: this box IP was used heavily today.
- Correction: a draft script mis-read "10 remaining" as capped (its regex was `/0 remaining/`). That was fixed before every number above.

## 5. Paywall and upgrade path (checks 6 and 13). No payment made.

- **Strip:**
  - Desktop: "Trial: 10 uses/day · N remaining today | Ads-free unlimited usage, $1 day pass [Quick Buy] | Ads-free unlimited usage, $4.99 monthly pass [Quick Buy]".
  - Mobile: "Ad-free: $1 day pass · $4.99/month".
- **Cap dialog** (`paywall.png`, `capped-paywall-dialog.png`):
  - "WE VALUE YOUR USAGE — You've used today's trial uses — You've used today's 10 trial uses. Monthly for $4.99 gives unlimited use, or a Day Pass for $1 covers 24 hours. Either pass removes the 'Created with FreeDailyPro.com' mark…"
  - Then Monthly pass $4.99/month · Buy Day Pass $1 · Have an access code? · Workflow Products note · Compare plans (/pricing) · Not today? Tell us why · Maybe tomorrow · Close.
  - Inline note: "Today's trial uses are used up, so generating was not done. Your input is still here and nothing was lost. Trial uses start again at midnight UTC…"
  - On-brand wording.
  - LOW: the mark-removal promise is generic. This tool's outputs (diff WAV, text summary) carry no visible mark.
  - The dialog says "You've used today's 10 trial uses" even when the visitor has done 0–1 compares (see 4).
- **Quick Buy $1 Day Pass:** an in-page dialog, "Enter your email and go straight to payment… Email (you@example.com) · Continue to payment · Already have an account? Sign in first" (`quickbuy-day.png`). Stopped; nothing typed.
- **Quick Buy $4.99 monthly:** goes **directly** to `checkout.stripe.com/g/pay/cs_live_…` ("Stripe Checkout") with no email step (`quickbuy-monthly.png`). Stopped; nothing typed.
  - The two flows are inconsistent. MED.
- **JSON-LD** Offer 4.99 has no billing period. LOW.
