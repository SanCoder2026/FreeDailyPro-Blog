Sent: 2026-10-30 12:09 ET

# B-0174 Document scanner: never turn a plain or coloured page solid black; recorder timer should match the file
Priority: P2 · Estimated effort: S · Report: #116 addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A scan should always be more readable than the photo, never less. Timers should tell the truth.

## Why
Admin session: a solid blue page → "Couldn't find the page edges" → Skip → an all-black PDF (centre pixel 0,0,0) with the defaults Grayscale + Remove shadows. Coloured-paper documents would turn unreadable. Screen recorder: the live timer showed ~00:07 at stop, while the file and the "Recorded 00:13" label are 13.8 s.

## Who uses this
People scanning forms on coloured paper; anyone recording a quick screen demo.

## Outcomes (ranked)
1. The shadow-removal/normalisation step must not stretch a low-contrast page to black; cap the gain or skip it when the page has no real contrast. 2. When edge detection fails, say the scan is a straight copy and keep the preview readable. 3. Screen recorder: the live timer starts when recording actually starts and matches the final file length within 0.5 s.

## Constraints
Keep Grayscale + Remove shadows as defaults for normal photos.

## Test cases
blue-800x1200.png, defaults → the page is a uniform mid grey (not 0,0,0). doc.jpg (#116 fixture) → text still dark on a light page. Record ~10 s → live timer, label and ffprobe duration within 0.5 s.
