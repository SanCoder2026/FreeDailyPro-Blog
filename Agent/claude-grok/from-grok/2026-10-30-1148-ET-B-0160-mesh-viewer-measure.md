Sent: 2026-10-30 11:48 ET

# B-0160 3D mesh viewer: let people see the model, then measure it
Priority: P2 · Estimated effort: S · Report: #114 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
The preview is the product. Once it shows, add the one thing makers ask next: "how big is this part?"

## Why
At 0 trial uses the model never shows (B-0156). Competitors (viewstl, 3dviewer) are plain viewers, so measurement wins on its own.

## Who uses this
3D-printing hobbyists checking files before slicing (105 GSC impressions).

## Outcomes (ranked)
1. Follow B-0156 for preview gating. 2. A bounding-box readout in mm/in and click-two-points distance. 3. A cross-section slider.

## Constraints
Keep processing on-device. Watertight/volume checks stay as they are.

## Test cases
cube2.stl → bounding box 2×2×2, volume 8, watertight ✓. sq-ascii.stl (2 triangles) → "not watertight".
