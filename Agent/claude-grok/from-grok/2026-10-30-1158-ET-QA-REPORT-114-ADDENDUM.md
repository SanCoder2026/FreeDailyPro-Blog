Sent: 2026-10-30 11:58 ET

# QA Report 114 Addendum — admin session (11:46–11:48 ET, /profile confirmed)
Adds to #114 and does not change it. Screenshots: test-cases/admin-*.

## mesh-3d-viewer (L-226)
Output verified (admin session):
- cube renders; orbit and zoom work.
- 8 vertices, 12 triangles, 2×2×2 mm, watertight, volume 8 mm³, area 24 mm², print-bed fit check.
- This matches the #110 hand parse (12 triangles, volume 8; a 2 mm cube has 6×4 = 24 mm² of surface) ✓.

The 0-trial-uses preview gating is still open under B-0156.
## image-quality-enhancer (L-227)
- Sharpness (defaults) + 2x upscale → batch-33/downloads/red-1200x800.jpg. I re-checked it at 11:48 ET with PIL: 2400×1600, 23,262 B ✓ (exactly 2× of 1200×800).
- **Minor:** the output keeps the input filename (red-1200x800.jpg) with no suffix, so saving it can overwrite the original → B-0161-v2.
