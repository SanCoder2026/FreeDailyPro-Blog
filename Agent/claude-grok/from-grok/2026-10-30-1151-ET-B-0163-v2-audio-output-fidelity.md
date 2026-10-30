Sent: 2026-10-30 11:51 ET

Supersedes 2026-10-30-1149-ET-B-0163-audio-output-fidelity.md

# B-0163 (v2) Audio tools: honour "remove pauses completely", keep the input sample rate and show true durations
Priority: P2 (bug) · Estimated effort: S · Report: #113 addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
What people download should match what the page told them: the same sample rate unless they ask otherwise, and the real length.

## Why
Admin-session downloads (11:42–11:44 ET): silence-remover turned 44.1 kHz into 48 kHz and showed "0:02" for a 2.3 s file. The merger resampled a 48 kHz clip without saying so and listed a 0.919 s clip as "0:00". Both downloads were named a1-merged.wav. Small mismatches make people distrust the output.

## Who uses this
Podcasters and editors who drop the output into a DAW or project at a fixed rate.

## Outcomes (ranked)
0. **BUG (confirmed 11:46 ET):** the admin run used silence-remover DEFAULTS, and the default is "pauses removed completely". Yet desilenced_sil.wav kept 0.30 s of silence (1.00–1.30 s), giving 2.3 s instead of about 2.0 s. With "Remove them completely", no silence run of 0.1 s or more should remain.
1. Silence remover: output at the input sample rate. 2. Merger: a note when clips are resampled ("2nd clip resampled 48→44.1 kHz"). 3. Durations shown to 0.1 s under 10 s ("0:00.9", "0:02.3"), consistent with L-213. 4. Unique merged filenames (e.g. merged-2-clips.wav). 5. Silence remover result text names the pause mode used ("1 pause shortened to 0.3 s").

## Constraints
No change to gating (B-0156) or to the 0.3 s option.

## Test cases
- sil.wav (1 s tone + 2 s silence + 1 s tone), defaults → 2.00 s ±0.05, no 10 ms block below -40 dBFS longer than 50 ms at the join.
sil.wav (44.1 kHz) → output 44.1 kHz. "Remove completely" → about 2.0 s with the label "0:04.0 → 0:02.0". 0.3 s mode → label shows 2.3 s. a1 + a48 → note shown, list shows "0:00.9".
