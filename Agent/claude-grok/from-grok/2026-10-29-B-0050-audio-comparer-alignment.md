# B-0050 Audio Comparer: same recording scored "0% Different audio" when shifted or re-encoded
Priority: P1      Estimated effort: 120 min      Report: #66      Source: Testing Bot (retest cycle 2)

**How to work with us:** you are the implementation partner, not an order-taker. Inspect the real code and past deploy patterns, challenge anything weak, choose the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID (done | partial | blocked, live and checked).

## Intent
The Audio Comparer must give an honest answer to the question people search for ("compare two audio files", "voice similarity checker", "compare two songs for similarity" — GSC, raw.md): are these the same recording?

## Why
- It is our best search page: /tool/audio-comparer 121 clicks / 2,390 impressions, pos 11.3 (GSC 3 mo, analytics/2026-10-29-raw.md); 150 views, 17 s avg engagement (GA 28d).
- Live Oct 29 9:40 PM ET: the same 3 s 440 Hz tone with 0.5 s of leading silence → **0.0% Different audio**; the same tone exported to MP3 128 kbps → **0.0% Different audio**. Real-world pairs are almost always offset or re-encoded, so the tool tells users two copies of one song are unrelated. That is a false claim (P1).
- File info shows "48 kHz" for a 44.1 kHz WAV (it prints the decoding AudioContext rate).
- Competitors: WaveDiff, MKDiff, Tembrica handle offset alignment (cross-correlation) and say so in their FAQ.

## Outcomes
- Identical audio with leading silence or a start offset up to a few seconds scores high (≥90%), and the result says "aligned by +0.50 s".
- Same audio re-encoded (MP3/AAC/WAV, different sample rates) scores high and is labelled "same audio, different encoding".
- Truly different audio still scores low (440 vs 880 Hz stays ~0%).
- File info shows the file's real sample rate (or omits it).

## Suggested direction (interpret freely)
Cross-correlate on a downsampled mono envelope or spectral features to find the offset, then compare aligned, loudness-normalised frames; trim leading/trailing silence. Nice to have after the fix (from competitors, cheap): "Try a sample pair", A/B play buttons, one-line "why this score".

## Constraints
Runs in the browser, nothing uploaded. Professional tool trial = 10 uses/day; don't change pricing. No invented accuracy figures in copy.

## Test cases (fixtures in report-66/test-cases/fixtures)
| ID | File 1 | File 2 | Expected | Actual Oct 29 |
|---|---|---|---|---|
| R66-AUD-03 | a440.wav | a440-shift.wav (+0.5 s silence) | ≥90%, offset shown | 0.0% Different |
| R66-AUD-04 | a440.wav | a440.mp3 (128 kbps) | ≥90% | 0.0% Different |
| R66-AUD-05 | a440.wav | any | "44.1 kHz" | "48 kHz" |
| R66-AUD-01/02 (regression) | a440/a440b; a440/a880 | 100% / ~0% | PASS today, must stay |
Desktop 1280 + mobile 390, logged out. Screenshots: fn-audio-*.png.

## Acceptance
All four rows pass live on desktop and mobile; report "live and checked".
Owner decisions needed: none.
