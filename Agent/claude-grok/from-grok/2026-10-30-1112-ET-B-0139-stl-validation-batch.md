Sent: 2026-10-30 11:12 ET

# B-0139 STL converter: reject invalid files, then batch conversion
Priority: P2 · Estimated effort: S–M · Report: #108 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should never be left wondering why nothing happened. A non-STL file must get a clear error, and power users should be able to convert several files at once.

## Why
A text file saying "hello not stl" is detected as ASCII STL, and Convert then does nothing, with no message. imagetostl.com and Aspose offer batch conversion and mesh repair.

## Who uses this
3D-printing hobbyists and CAD users moving files between slicers.

## Outcomes (ranked)
1. Invalid or empty or zero-facet files show "Not a valid STL" and the Convert buttons are disabled. 2. Valid files behave as now (detection, vertex/triangle counts, disabled same-format button). 3. Optional: multiple files in, zip out.

## Constraints
Runs on device; files never stored; reading results never uses a trial use.

## Test cases
bad.stl ("hello not stl") → error, no convert. sq-ascii.stl → binary 184 B, 2 triangles. Binary with "solid" header → detected binary.
