Sent: 2026-10-30 13:13 ET

# QA Report #125 — Addendum: admin-session output checks + owner decision
The admin session ran about 13:10–13:12 ET. Files are in `batch-44/downloads/` and inputs in `batch-44/inputs/`. Frames were extracted by QA with ffmpeg. This adds to report #125, which itself is unchanged.

## Owner decision applied (Santosh, 13:12 ET, via Orchestrator; see from-grok B-0156-v2)
- The trial limit stays. Copying and viewing results count against trial uses in every tool, Emoji included.
- B-0142 and B-0149 are marked "limit kept by owner (closed)".
- From batch 45 on, free copy or free results are not raised as a gap or bug.
- Still counted as bugs under B-0156, to be retested only after Claude marks B-0156 done:
  - false "Copied" toasts
  - blank output
  - dropped inputs
  - the paywall shown together with a success toast
  - wrong paywall wording (e.g. "download" on a copy action)
  - counters that don't match

## subtitle-adder (L-262) — output verified with one rendering bug (admin session)
- `subtitled_v.mp4` (63,496 B): 320×240, 3.02 s, video + audio.
- Frames at 1.0 s and 2.5 s (`downloads/frame-1.0s.png`, `frame-2.5s.png`): the captions are burned in at the bottom, centred, in white ✓. The timings match (caption 1 at 1.0 s, "Line two" at 2.5 s) ✓
- "É" renders correctly ✓. The `<i>world</i>` tags are removed (no literal tags), but there's **no visible italics**.
- **Bug: the 👋 emoji renders as an empty box (tofu).** The burn-in font has no emoji glyphs. Added to B-0200 here: use a font fallback with emoji, or strip the emoji with a warning. Italics should be honoured or the note should say they aren't supported.
- Still no success text after the render → B-0187.

## rotate-video (L-263) — output verified (admin session)
- `v-rotated.mp4` (45,683 B). ffprobe shows stream 320×240 with a display-matrix rotation of **-90** (= 90° clockwise display), plus audio. Not re-encoded, so the page's message was honest ✓

## csv-converter formula protection (L-259) — verified, minor copy note
- Input `=1+1,+2,-3,@x` → output (BOM, CRLF) `'=1+1,'+2,-3,'@x`.
- The numeric `-3` isn't prefixed. That's sensible and in line with OWASP practice for numeric cells, but the label says it covers "cells starting with =, +, - or @". **Minor copy/consistency note for B-0195:**
  - make the label say "(numbers like -3 are left as numbers)"; or
  - prefix `+2` consistently with `-3`. Today `+2` is prefixed but `-3` isn't. Pick one rule and state it.
- **Open check:** is a non-numeric `-cmd` cell prefixed?

## Add Page Numbers ads (L-004 / B-0041) — closed
- At 1920×1072 after upload, ads do **not** cover the Add button (the skyscraper sits to its left). The check is closed.
