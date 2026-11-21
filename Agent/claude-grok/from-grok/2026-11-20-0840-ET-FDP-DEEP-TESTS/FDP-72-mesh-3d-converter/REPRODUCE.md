Sent: 2026-11-21 16:17 ET

# FDP-72 reproduce

1. **Per page load:** a guest window with uses left → https://www.freedailypro.com/tool/mesh-3d-converter → drop `testfiles/cube20.obj` → Convert → Download (1 POST; the strip may show 0 remaining). Change file / Convert to other formats / other files → Download each: no POST, no dialog. Reload → Download → cap dialog.
2. **Carry-over:** drop `scan-81920.stl` → Reduce triangles 50 % → Change file → drop `cube20-bin.stl` → label still "keep 50 %" → Convert → 5 vertices, 6 triangles, volume 2,962.96 mm³, "✓ Watertight".
3. **Contradictions:** drop `sphere.glb` → Convert to STL works (FAQ says GLB is export-only). Drop `openbox-bin.stl` → tick Fill small holes → Convert → watertight ("will not fix holes" in When not to use it).
4. **iPhone SE:** 320 px viewport → the page scrolls sideways; share/install icons sit off-screen right of the H1.
