Sent: 2026-11-21 20:39 ET

# Desk findings (FDP-84)

- **Gate code.** index-xgcQ0Xo8.js has `dI(e,t)` (same key → "free", new key → "again", otherwise "first") and `tryUseExport(key)`; ToolPage-DrleSM7T.js `la()` exposes it as `logExportNow(key)`. The DownloadButton (`ql`) still runs `se = f ? !0 : g ? At(g) : u ? (Z(), !0) : v("download")` → `logUsageNow` → `tryUse` → `xI`, which sets the per-tool `Kt` flag. It's cleared only by `wI` on unmount. So the export key is never consulted for this tool's download.
- **Deskew** (scanRun `v()`): dark-pixel projection profile over ±8°, then a 0.1° refinement. Dark corners from rotation or desk count as "ink", so the profile peak isn't the text angle.
- **Numbers** (tablesToExcel): column evidence can override the chosen date order (with a note). No equivalent rule for "1.200"-style thousands in comma-decimal tables.
- **Handoff:** document-scanner stores files under `scan-convert` and calls ``Ce(`/tools/${t}`)`` (plural). ScanConverter reads `scan-convert` on mount, so fixing the path should complete the flow.
- **Limits** (scanCore SCAN_LIMITS): 30 images, 25 MB each, 150 MB total, long side 4200 px. The page also says "over 50 MB may take longer".
- **Copy:** cap dialog text mentions "the 'Created with FreeDailyPro.com' mark from your PDFs".
- **Copy button:** exists only in text output mode (not reachable on this Excel-only page), so nothing to count.
- **FAQ** matches behaviour (3-row minimum, column gaps, codes as text, look-alike characters).
