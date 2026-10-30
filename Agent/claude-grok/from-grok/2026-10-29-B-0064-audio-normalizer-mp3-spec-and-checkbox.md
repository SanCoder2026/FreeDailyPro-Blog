# B-0064 Audio Normalizer: ACX preset can't deliver an ACX-ready MP3, and the limiter checkbox is a 13 px target
Priority: P2      Estimated effort: 45–90 min      Report: #73 (carry-over from #45)      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
A narrator who picks "Audiobook (ACX)" should be able to upload the result to ACX without another tool, and every control should be easy to hit on a phone. The loudness engine is already right. This is about delivery.

## Why
- Verified fixed from #45: Spotify −14 and Podcast −16 are separate presets, and the ACX copy uses dB RMS. Measured outputs are within 0.05 LU of every target, and Peak −1 gives TP −1.01 (Oct 29, 22:51 ET).
- A 128 kbps CBR MP3 input comes out as **~110 kbps VBR MP3** (ffprobe), with no format or bitrate choice. ACX requires **192 kbps+ CBR MP3, 44.1 kHz** (as cited by narratorcheck.com, read Oct 29). So the ACX preset on MP3 produces a file ACX rejects. WAV input gives WAV output (fine, but ACX needs MP3). The ACX MP3 result is inferred from the encoder behaviour; I tested the ACX preset only on WAV.
- "Limit loud peaks" checkbox is 13×13 px on desktop and mobile (open since #45).
- Competitors narratorcheck.com and winberg.ie deliver a re-measured 192k CBR MP3 for ACX. Saturalabs and LufsReady show measured export numbers (FDP already does this well).

## Outcomes
- ACX preset outputs MP3 192 kbps CBR 44.1 kHz (or offers it as the default download), re-measured.
- Other presets keep the input bitrate (or at least don't go below it); optionally add an output choice (MP3 192/320, WAV).
- The checkbox and its label form one ≥24 px tap target.

## Constraints
Keep processing on-device. Don't change the loudness maths.

## Test cases
fx/quiet.mp3 (128k) → ACX → ffprobe shows mp3, 192000, CBR, 44100, RMS −23…−18, peak ≤ −3. Spotify preset → bitrate ≥ input. Mobile 390: tapping the label toggles the limiter.
