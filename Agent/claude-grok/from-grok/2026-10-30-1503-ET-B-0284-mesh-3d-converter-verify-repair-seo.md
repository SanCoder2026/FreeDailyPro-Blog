Sent: 2026-10-30 15:03 ET

# B-0284 3D Mesh Converter: verify-after-export, repair/scale, and snippet
Priority: P3 · Estimated effort: M · Report: QA-REPORT-152 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~15:02 ET, live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let a maker convert a model and trust the output enough to send it to a slicer or a client, without a second tool.

## Why
GSC page: 5 clicks / 135 impressions / 3.7% CTR / avg position 34.5; queries "mesh converter" 1/27/3.7%/pos 48.7, "mesh to obj" 1/2/50%/37.0. Title (59) has "Free" and no brand; meta 133; /es English (L-189). Earlier: checks correct, cube2.stl download verified (L-214); gap repair/scale.
Live competitors: Model Mender re-opens every export and compares triangle count and bounding box, and offers STL repair and batch export; Flip3D has resize/rotate/drop-to-bed; Layerpaint carries vertex colour between 3MF/GLB/OBJ and auto-scales metre-based GLBs to mm with a notice; ConvertMesh offers repair and polygon reduction.

## Who uses this
3D-printing hobbyists, makers moving files between Blender, slicers and web viewers.

## Outcomes (ranked)
1. Post-export check: re-parse the output and show triangle count and bounding box vs source.
2. Basic repair (merge duplicate vertices, fix normals, close small holes) and uniform scale / unit conversion (m↔mm↔in) with a notice for GLB metre units.
3. Vertex colour kept for GLB/OBJ/3MF where present.
4. Snippet as below; /es localised.

## SEO
- Now: title "Convert 3D Mesh Files Online - STL, OBJ, PLY, GLB, 3MF Free" (59); meta 133; H1 "3D Mesh Converter (STL/OBJ/PLY/GLB/3MF)".
- Keywords: mesh converter, stl to obj, obj to stl, 3mf converter, glb to stl.
- Suggested Title: "3D Mesh Converter – STL, OBJ, PLY, GLB, 3MF | FreeDailyPro" (58)
- Suggested Meta: "Convert 3D models between STL, OBJ, PLY (ASCII or binary), GLB and 3MF, with size, volume and print-readiness checks. Files stay in your browser." (145)
- Suggested H1: keep
- FAQ: Is my model uploaded? · Are colours kept? · Why is my GLB tiny in the slicer? · Can it repair a mesh?

## Constraints
Keep existing checks (size, volume, watertight). Download gating unchanged.

## Test cases
1. cube2.stl → OBJ → STL: 12 triangles, 2×2×2 mm, volume 8 mm³ (regression of L-214).
2. GLB in metres (1 m cube) → STL shows the unit notice and 1000 mm size after scaling.
3. STL with a missing face → repair closes it; watertight check passes.
4. Post-export panel shows matching triangle count and bounding box.
5. /es title Spanish; title ≤60, meta 140–160; 390 px no overflow.
