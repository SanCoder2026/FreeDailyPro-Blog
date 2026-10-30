Sent: 2026-10-30 11:49 ET

# B-0163 Audio tools: keep the input sample rate and show true durations
Priority: P2 · Estimated effort: S · Report: #113 addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
What people download should match what the page told them: the same sample rate unless they ask otherwise, and the real length.

## Why
Admin-session downloads (11:42–11:44 ET): silence-remover turned 44.1 kHz into 48 kHz and showed "0:02" for a 2.3 s file. The merger resampled a 48 kHz clip without saying so and listed a 0.919 s clip as "0:00". Both downloads were named a1-merged.wav. Small mismatches make people distrust the output.

## Who uses this
Podcasters and editors who drop the output into a DAW or project at a fixed rate.

## Outcomes (ranked)
1. Silence remover: output at the input sample rate. 2. Merger: a note when clips are resampled ("2nd clip resampled 48→44.1 kHz"). 3. Durations shown to 0.1 s under 10 s ("0:00.9", "0:02.3"), consistent with L-213. 4. Unique merged filenames (e.g. merged-2-clips.wav). 5. Silence remover result text names the pause mode used ("1 pause shortened to 0.3 s").

## Constraints
No change to gating (B-0156) or to the 0.3 s option.

## Test cases
sil.wav (44.1 kHz) → output 44.1 kHz. "Remove completely" → about 2.0 s with the label "0:04.0 → 0:02.0". 0.3 s mode → label shows 2.3 s. a1 + a48 → note shown, list shows "0:00.9".
