Sent: 2026-10-30 13:09 ET

# B-0200 Subtitle Adder: preview captions and generate them from speech
Priority: P2 · Estimated effort: M · Report: #125 · Source: QA sweep + live competitor fetch 2026-10-30 13:04 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should see how their captions look before they render, and shouldn't have to type every line by hand.
## Why
- Video + SRT (with É, <i>, emoji) → the render finished and offered Download (gated at 0 trial uses → B-0156).
- After the render there's no "Added 2 captions" text → B-0187.
- A bad timing line gives a clear error: "Line 2: expected a time like … but found …" ✓
- The Premium counter showed "2 remaining" on load and "0 remaining" after one render → L-143 evidence.
- VEED mentions auto ×540, font ×458, translate ×41 (live fetch). There's no auto-caption, no font choice and no on-frame preview.
- Website tool for the "Generate Video Subtitle" paid API (first billable 27 Oct 6:02 AM ET; rule 1).
- The site already has audio-to-subtitles.
## Who uses this
Creators posting short videos with burned-in captions.
## Outcomes (ranked)
1. A live preview of a frame with the caption at the chosen size, position and colour.
2. "Generate captions from the audio" hands off to audio-to-subtitles and fills the SRT box.
3. A font choice (2–3 web-safe faces) and outline as well as box.
4. End-before-start timings caught by name ("ends before it starts").
## Constraints
Processing stays on the device. Keep the track (soft-sub) option.
## Test cases
1. Change Position to Top → the preview updates before rendering.
2. `00:00:05,000 --> 00:00:02,000` → "Caption 1 ends before it starts".
3. Generate from audio on a speech clip → the SRT box fills, editable.
