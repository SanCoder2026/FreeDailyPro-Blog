Sent: 2026-10-30 08:37 ET
# B-0119 Audio Comparer: visual diff, A/B listening, loudness/metadata table, share link (capability gap)
Priority: P2      Estimated effort: 2–3 days      Report: #97      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
This is the #1 tool page by traffic. Make it at least as good as WaveDiff, Tembrica and SoundYak: a visitor should see, hear and read where two files differ.

## Why
- Demand (analytics file): /tool/audio-comparer GA 258 views (175 users, 1.47 views/user, 19s avg), the top tool page. GSC page 122 clicks / 2,427 impressions / 5% / pos 11.2. Queries: "compare audio" 2/24/pos 11.9, "compare audio files online" 1/11/7.5, "compare audio files" 1/9/6.3.
- Still open, not repeated here: B-0050 (0% match for an offset or MP3 re-encode; sample-rate label) and B-0051 (trial use counted on file select). Report #97 could not re-run them because trial uses are at 0 and selecting a file uses one (L-023). They go to the admin carry-over.
- Live competitor fetch (08:34 ET):
  - **WaveDiff**: 5 views (waveform, overlay, spectrogram, difference, spectral diff); A/B toggle; normalize levels; time-offset alignment; loop regions; share link; export the difference as WAV; local processing.
  - **Tembrica**: auto-alignment by cross-correlation; bit-identical detection with a per-second difference map; LUFS, true peak, spectral cutoff, phase; ABX blind test.
  - **SoundYak**: stacked waveforms, Play A/B, and a Same/Different table (duration, sample rate, channels, size). It warns that browsers resample, so the sample-rate row is unreliable (directly relevant to B-0050).
- FreeDailyPro (static read #97): two drop zones and "Compare Audio" only. Both file inputs are hidden with no accessible name. No waveform, playback, table or share link is visible before a run.

## Who uses this
Podcasters and musicians checking which take or export is final, editors checking whether a file was altered, and people deduplicating music libraries.

## Outcomes (ranked)
1. Auto-alignment plus the B-0050 fix, so the percentage means something. This comes first, because the other outcomes build on it.
2. Stacked waveforms with a difference overlay and a timeline of where they differ.
3. A/B instant toggle playback with loudness match.
4. A properties table (duration, channels, LUFS, peak, file size; sample rate labelled "as decoded").
5. A local-only share or export of the result.
6. Accessible names on both file inputs / drop zones.

## Constraints
Keep everything in the browser. Say "trial uses". Charge only on completed results (B-0051).

## Test cases (ET)
- 08:33 TC-1: page 200 at 1280/390; 2 drop zones + Compare. PASS
- 08:33 TC-2: file inputs have no accessible name (2). FAIL
- 08:33 TC-3: compare run (B-0050/B-0051 recheck). BLOCKED (0 trial uses; file select consumes one) → admin carry-over
