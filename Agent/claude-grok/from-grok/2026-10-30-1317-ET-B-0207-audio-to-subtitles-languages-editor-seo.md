Sent: 2026-10-30 13:17 ET

# B-0207 Audio to Subtitles: keep the file at the paywall, add languages and a cue editor
Priority: P2 · Estimated effort: M · Report: #127 · Source: QA sweep + SEO curl check + live Google top-3 (WebSearch) 2026-10-30 13:14 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should get publishable SRT/VTT from their recording, in their language, without losing their file along the way.
## Why
- At 0 trial uses, **choosing a file opens the trial-uses dialog right away**, so the file is dropped before any work. Under the owner decision the limit stays, but **dropped inputs remain a B-0156 bug**; this is recorded as evidence there.
- English only, with a ~100 MB in-browser model.
- Top Google results (13:14 ET):
  - AudioScribe: SRT/VTT/TXT/PDF/Word, speaker labels.
  - Scribiz: SRT/VTT, word-level timing.
  - AudioSRT: Whisper in the browser, editor, styling, burned MP4, 100+ languages in the cloud.
  - formatter.org and earscribe: language choice or auto-detect, a cue editor with listen-back, and a subtitle QA check for long, fast or overlapping cues.
- Injected "Compare Browsers" appears twice in the tool area → L-004.
## Who uses this
Creators, teachers and podcasters captioning videos.
## Outcomes (ranked)
1. Keep the chosen file when the paywall shows, so it's there after the user buys or returns (B-0156 dropped-input rule).
2. Choose a language, or auto-detect (multilingual Whisper-tiny/base in the browser).
3. A cue editor: click a cue to hear it, edit the text and times, then export.
4. A readability check (cue too long or too fast, overlap).
5. "Burn into video" hands off to Subtitle Adder (B-0200).
## SEO
- **Now:**
  - Title "Audio to Subtitles: Make SRT and VTT in Your Browser" (52), which is good.
  - Meta is 157 chars and good, but ends in the boilerplate "Free and fast, right in your browser."
  - H1 "Audio to Subtitles". No VideoObject. JSON-LD otherwise valid.
  - (site-wide items: generic OG image, generic H2s, boilerplate meta, empty video alt → B-0209; English metadata on locale pages → B-0123/L-189)
- **Best results** use "Audio to SRT" as the H1 and keyword ("Convert Audio to SRT", "SRT Generator"). Their FAQs: "How do I make SRT from MP3?", "Where does the SRT file work?", "Is my file uploaded?"
- **Suggested:**
  - Title: `Audio to SRT – Free Subtitle Generator, No Upload | FreeDailyPro` (60)
  - Meta: `Turn speech in MP3, WAV or MP4 into SRT or VTT subtitles on your device. Nothing is uploaded. Edit the captions, then use them in YouTube, Premiere or VLC.` (156)
  - H1: `Audio to SRT Subtitle Generator`
  - FAQ: "How do I make SRT from MP3?" / "Where can I use the SRT file?" / "Which languages work?"
## Constraints
Processing stays on the device.
## Test cases
1. Choose a file at 0 trial uses → paywall; after closing it, the file is still selected.
2. A Spanish clip with language Auto → Spanish cues.
3. Edit cue 2's text → the export contains the edit.
