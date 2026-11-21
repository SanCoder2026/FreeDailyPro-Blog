Sent: 2026-11-21 16:05 ET

# Live functional findings (FDP-71)

- P1: the result player's native Download saves the full output at 10/10, byte-identical to the paid download (extra.json, md5 fd2505d99762; player blobs = paid files for FLAC too).
- P1: one charge per page load; 7 downloads from 4 sources = 2 uses (left-firefox.json).
- Owner question: full result playback at 0 is free by design.
- Outputs exact (tempo, pitch ±12, sample rate/channels, format family, names). P2: non-audio fails late with F12 advice.
