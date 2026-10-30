Sent: 2026-10-30 11:22 ET

# B-0146 3D mesh converter: fix small holes and scale on export
Priority: P2 · Estimated effort: S–M · Report: #110 · Source: QA sweep + live competitor fetch 2026-10-30 11:20 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Turn "not watertight" from a dead end into a one-click fix, and let people export at the right size.

## Why
We already detect open edges well ("4 open edges"). imagetostl.com offers repair and scaling on conversion.

## Who uses this
3D-printing hobbyists converting scans and downloaded models.

## Outcomes (ranked)
1. "Fill holes" for small open loops, then re-check watertightness. 2. A scale factor or target size on export. 3. Current checks (volume, area, bed fit) unchanged.

## Constraints
Runs on device; never change the mesh without the user choosing to.

## Test cases
The 2 mm cube with 2 faces removed → Fill holes → ✓ Watertight, volume 8 mm³. Scale ×10 → 20×20×20 mm.
