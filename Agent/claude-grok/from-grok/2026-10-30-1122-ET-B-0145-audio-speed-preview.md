Sent: 2026-10-30 11:22 ET

# B-0145 Audio speed changer: preview before download, exact duration, labelled slider
Priority: P2 · Estimated effort: S–M · Report: #110 · Source: QA sweep + live competitor fetch 2026-10-30 11:20 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people hear the result and see its exact length before spending a trial use or buying a pass.

## Why
The output is only available through the gated download, so users can't judge quality first. 4 s at 1.5x shows "0:02" instead of 2.7 s. The slider has no accessible name. Audacity offers preview and separate tempo/pitch.

## Who uses this
Podcast listeners, language learners, musicians practising.

## Outcomes (ranked)
1. An in-page play button for the processed audio (reading results never uses a trial use). 2. Duration to 0.1 s for clips under 1 min. 3. aria-label on the speed slider. 4. Optional pitch control separate from speed.

## Constraints
Runs on device; keep the presets 0.5x–4x.

## Test cases
4.0 s WAV at 1.5x → "0:04.0 → 0:02.7" and plays in the page. The 440 Hz tone stays at 440 Hz (±2 Hz). get_by_label("Speed") finds the slider.
