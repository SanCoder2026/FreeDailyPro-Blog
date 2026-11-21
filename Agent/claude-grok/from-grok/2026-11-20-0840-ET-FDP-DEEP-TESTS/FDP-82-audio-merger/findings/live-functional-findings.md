Sent: 2026-11-21 18:56 ET

# Live functional findings (FDP-82)

- Zero (10/10): Merge Audio and the result player work; Download ×6 → cap dialog; 0 POSTs.
- Left (0/10): 6 Downloads, 2 POSTs (first per page load).
- Byte checks: result player at 10/10 = paid Download (`cmp`, WAV and MP3).
- Order, reorder, remove, gaps, crossfades and their caps, Total length, resampling, formats, duplicate skip and file names are all correct.
- Cover-art MP3 first → 320 kbps instead of ≤ 128. Mono-first folds a stereo clip to mono. Corrupt clip → generic toast.
- 57.2 MB combined (two files) → blocked for a guest with "a file over 50.0 MB".
