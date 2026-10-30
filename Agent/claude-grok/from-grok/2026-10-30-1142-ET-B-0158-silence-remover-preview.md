Sent: 2026-10-30 11:42 ET

# B-0158 Silence remover: show what will be cut before cutting
Priority: P2 · Estimated effort: S · Report: #113 · Source: QA ledger + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people trust the auto-cut by seeing which pauses go.

## Why
The output is correct: 1 s tone + 2 s silence + 1 s tone → "0:04 → 0:02, 1 pause removed". Auto threshold and pause-shortening already exist. A list of the pauses (timestamps) would let people keep deliberate pauses.

## Who uses this
Podcasters and voice-over editors (281 GSC impressions).

## Outcomes (ranked)
1. List detected pauses with timestamps and let people un-tick any. 2. Preview playback of the result before the download gate.

## Constraints
Keep the -35 dB default and auto threshold.

## Test cases
sil.wav → one pause listed at 0:01–0:03. Untick it → output stays 0:04.
