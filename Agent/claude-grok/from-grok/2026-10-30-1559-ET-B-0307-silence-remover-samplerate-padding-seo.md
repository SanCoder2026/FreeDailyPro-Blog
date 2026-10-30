Sent: 2026-10-30 15:59 ET

# B-0307 Silence Remover: position 36, 48 kHz output from 44.1 kHz input, no padding control
Priority: P2 · Estimated effort: M · Report: QA-REPORT-160 · Source: live probe 2026-10-30 ~15:52-15:58 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A podcaster gets tighter audio in the same format and sample rate they gave, with control over how much breath is left.

## Why
GSC: /tool/silence-remover 2 clicks / 281 impressions / 0.7% CTR / position 35.9 (page 4).
Checked live (15:56 ET), 3.500 s WAV at 44.1 kHz (1 s tone, 1.5 s digital silence, 1 s tone), defaults (-35 dB, Remove them completely, Minimum 0.5 s) → desilenced_sil.wav, 2.300 s, 48 kHz mono. Page said "0:03 → 0:02, 1 pause removed".
- The 0.3 s kept is now explained by the FAQ ("keeps about 0.15 seconds of quiet beside the speech on each side"). L-223's "bug" now matches documented behaviour; not marked fixed (no Claude fix claim checked).
- The 44.1 → 48 kHz change is still there and the FAQ does not mention it ("WAV stays WAV").
- Durations are floored (3.5 s shown 0:03, 2.3 s shown 0:02), same as L-229.
Controls seen: threshold slider, Auto threshold, Pauses select (remove / shorten to 0.3, 0.5, 1 s), Minimum Duration, Remove Silence, Reset. Padding control: not offered (checked). Waveform preview of cuts, cut list, A/B play: not seen (checked).
Competitors (live search): johnmcm (threshold, shortest silence, padding, shaded waveform, before/after length), ToolsDeck (padding slider, cut-list CSV, filler words, A/B), audiojs (shorten/remove/trim-ends modes, crossfades), airtape (preset levels).
Title 52 without "| FreeDailyPro" and with "Free"; meta 92 (Free, short). /es title English (H1 "Eliminar Silencios") → L-189.

## Who uses this
Podcasters, teachers and voice-over makers cleaning recordings.

## Outcomes (ranked)
1. Keep the input sample rate (44.1 kHz in → 44.1 kHz out), or state the change.
2. Snippet below, to move off page 4.
3. A padding control (default 0.15 s), and show duration to 0.1 s ("3.5 s → 2.3 s").
4. Highlight the found silences before processing.

## SEO
- Now: title "Remove Silence From Audio Online - Free, Auto-Detect" (52, no brand, Free); meta 92; H1 "Silence Remover"
- Keywords: remove silence from audio, silence remover, cut pauses podcast, remove dead air, trim silence
- Suggested Title: "Silence Remover: Cut Pauses From Audio | FreeDailyPro" (53)
- Suggested Meta: "Remove or shorten long pauses in a voice recording or podcast. Set the dB threshold or let Auto pick it, choose the minimum pause, and download in your browser." (160)
- Suggested H1: "Silence Remover: Cut Pauses From Audio"
- FAQ: keep current; add: Does it change the sample rate? · How much pause is left?

## Constraints
Results count against the trial; do not change that. Keep Auto threshold.

## Test cases
1. 3.5 s WAV 44.1 kHz (1 s tone, 1.5 s silence, 1 s tone), defaults → output 44.1 kHz, about 2.3 s, and the page shows 3.5 s → 2.3 s.
2. Shorten to about 0.5 s → output about 2.5 s.
3. A file with no pause → "no silence was found" message, no download.
4. View source → title and meta as suggested.
