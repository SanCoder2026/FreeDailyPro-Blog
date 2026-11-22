Sent: 2026-11-21 21:25 ET

# Desk findings (FDP-85)

- **Same bundles as #84:** ScanConverter-Di_4PqSS.js, ToolPage-DrleSM7T.js, scanCore-B6hkUd9X.js. ImageToWord-C0JN-QFT.js only mounts ScanConverter in Word mode.
- **Gate:** the DownloadButton `ql` → `logUsageNow` → `tryUse` → `xI` sets `Kt` (cleared by `wI` on unmount). `logExportNow(key)` → `tryUseExport` → `dI` (free/again/first) exists in `la()` but this button doesn't use it. See the #84 excerpt.
- **Word builder** (scanCore `S()`): `const n = r.landscape ? o.h : o.w` with `landscape: o.widthPx > o.heightPx`, so page orientation follows the picture even when `includePicture` is off. A page with no paragraphs and a picture becomes a picture-only page with 36 pt margins. With the option on, the picture sits above the text at 40% of the page.
- **Rotation:** in scanRun, `c.read(blob, {autoRotate: true})` returns `g.rotation`. That value sets `sizeAfterRotation` and the note "Turned N° clockwise". ScanConverter passes `o.rotation` to `rotateImageBlob` for the embedded picture. A 180° picture came back as 270.
- **Handoff:** document-scanner `le("image-to-word")` stores files under `scan-convert` and then navigates ``Ce(`/tools/${t}`)``, a 404.
- **Limits:** 30 pictures, 25 MB each, 150 MB total, long side 4200 px (SCAN_LIMITS). The page says "Up to 30 pictures, 25 MB each".
- **Copy button:** text mode only, not shown on this page.
