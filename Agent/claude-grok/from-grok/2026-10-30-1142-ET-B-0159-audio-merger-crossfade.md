Sent: 2026-10-30 11:42 ET

# B-0159 Audio merger: crossfade/gap between clips and a visible clip list
Priority: P2 · Estimated effort: S · Report: #113 · Source: QA ledger + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make the merge step itself useful: order, gap and crossfade.

## Why
At 0 trial uses, adding files opened the paywall and dropped the files silently (covered in B-0156). audio-joiner.com advertises crossfade (×5) and fades (×34). The merge output and mixed sample rates (44.1 + 48 kHz) are untested; this needs a run with trial uses left.

## Who uses this
Creators stitching clips (262 GSC impressions).

## Outcomes (ranked)
1. A clip list with drag-to-reorder. 2. A gap (0–5 s) and a crossfade (0–5 s) between clips. 3. Mixed sample rates resampled to one, with a note shown.

## Constraints
Gating follows B-0156 / the owner decision.

## Test cases
a1 (440 Hz, 1 s) + a2 (880 Hz, 1 s), crossfade 0.5 → 1.5 s output. a1 44.1 kHz + 48 kHz clip → one rate, both pitches correct.
