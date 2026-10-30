Sent: 2026-10-30 11:28 ET

# QA Report 110 Addendum — downloads checked (admin session)
Adds to #110 and does not change it. Downloads were run in the **admin session** (verified at /profile) 11:22–11:23 ET. The files are in batch-29/downloads/. I checked every file myself on the box at 11:26 ET.

| File | Size | My check | Verdict |
|---|---|---|---|
| speed_1.5x_tone4s.wav | 235,448 B | mono, 44.1 kHz, 16-bit, 117,685 frames = 2.669 s (4 / 1.5 = 2.667 ✓); FFT peak 439.93 Hz (source 440 Hz); RMS 11,578 vs source ~11,585 | pitch preserved ✓, level preserved ✓ |
| cube2.stl | 684 B | binary (header "Binary STL by FreeDa…"), 12 triangles, 84 + 12×50 = 684 ✓, bbox 0–2 mm, signed volume 8.0 mm³ ✓ (outward normals) | OK ✓ |
| sq-ascii_binary.stl | 184 B | binary, 2 triangles, 84 + 2×50 = 184 ✓, bbox 1×1×0 | OK ✓ |
| sprite-sheet.png | 704 B | 128×32; frame colours left→right red, green, blue, yellow = f0, f1, f2, f3 ✓ | order correct ✓ |

Ledger changes:
- L-213: pitch verified. Still open for the 0:02 duration display and the unlabelled slider.
- L-214: download verified.
- L-207: valid-file download OK. The invalid-file bug stays open.
- L-211: combine output verified. Split output not yet checked.
