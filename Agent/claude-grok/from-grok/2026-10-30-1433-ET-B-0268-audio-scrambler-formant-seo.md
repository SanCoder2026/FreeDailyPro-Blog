Sent: 2026-10-30 14:33 ET

# B-0268 Audio Scrambler: pitch-only disguise is easy to undo; add formant shift, before/after compare and a clear "not anonymity" note
Priority: P2 · Estimated effort: M · Report: #147 · Source: Playwright headless, logged out, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:30–14:33 ET. L-243: next 3 untested tools alphabetically after agenda-cue-sheet-builder. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone protecting a source's identity should get a recording that is hard to match back to the speaker and still understandable, and know its limits.
## Why (repro: a.mp3, 6 s tone; 1280 px; 0 trial uses)
- Trial: 10 uses/day, $1 day / $4.99 monthly. Drop file → presets Strongest Deep … Strongest High (default −3 semitones), Preview 8 s, Disguise Voice. Processing runs; only Download is gated ("0 remaining today · Get a Day Pass to download") — owner's decision.
- The page itself warns: "A single pitch shift is easy to undo… run it through this tool again with a different shift." That workaround costs a second trial use and still leaves formants untouched.
- About text pitches whistleblower use. **Pitch alone is a weak disguise for that use** (undetectable.me: "a matcher can often undo a simple pitch change"; formants are a stronger identity cue).
- **Missing vs competitors (~14:31 ET):** separate formant shift (undetectable.me, KOWAIRO, W3PN Anonymizer); ring mod / bitcrush / timing wobble presets (W3PN); before/after A/B players (undetectable.me, W3PN); output format choice WAV/FLAC/MP3 (undetectable.me); video input (VoiceWarp, W3PN); record from mic (KOWAIRO, Essex, VoiceWarp). All state clearly that it is not guaranteed anonymity.
- No overflow at 390 px. "Compare Browsers" glued to copy → L-004.
## Who uses this
Journalists, podcasters, researchers and people sharing sensitive recordings.
## Outcomes (ranked)
1. Formant shift (opposite direction to pitch) in one pass.
2. Before/after compare and an honest "raises the bar, not anonymity" note in place of the whistleblower framing.
3. Output format choice; video input.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**.
  - **Title "Disguise a Voice Online Free - Pitch Shift Audio | FreeDailyPro" is 63 chars** with "Free". **Meta 86.** H1 "Audio Scrambler" (not what people search).
- **Keywords:** "voice disguiser", "anonymize voice recording", "disguise voice online", "voice changer for audio file".
- **Suggested:**
  - Title: `Disguise a Voice – Pitch Shift Audio | FreeDailyPro` (51)
  - Meta: `Disguise a voice in an audio file by shifting its pitch: pick a preset, preview 8 seconds, and save the result. Runs in your browser; nothing is uploaded.` (154)
  - H1: `Disguise a Voice in an Audio Recording`
  - FAQ: "Can a pitch shift be undone?" → "Yes, often; use a large shift plus formant." · "Is my audio uploaded?" → "No." · "Does it guarantee anonymity?" → "No."
## Constraints
Keep the download gated per the owner's decision.
## Test cases
1. Admin: download at −8 semitones; spectrum shows the shift; length unchanged.
2. Title ≤ 60, no "Free"; meta 140–160.
