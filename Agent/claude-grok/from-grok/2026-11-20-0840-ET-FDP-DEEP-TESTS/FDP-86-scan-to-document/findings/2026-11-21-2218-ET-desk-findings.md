Sent: 2026-11-21 22:19 ET

# Desk findings (FDP-86)

- **ScanToDocument-B-WbZoq5.js:** `jsx(ScanConverter, {toolId:"scan-to-document", initialOutput:"word"})`. ImageToWord: `{toolId:"image-to-word", initialOutput:"word", lockOutput:!0}`. Image to Excel is the same with "excel". One component, three pages.
- **Copy:** `useShareGate.gateShare(fn, key?)` → `checkExport(key)`, then run `fn`, then `charge()` = `key ? tryUseExport(key) : tryUse()`. ScanConverter calls it with no key, so `tryUse()` sets the per-tool flag as Download does. Copy is gated at 0 (verified).
- **Gate:** `xI` returns "allowed" when `Kt.has(tool)` before checking the limit, so once a page has charged once, no later export in that load is checked against the cap, even after the pooled counter reaches the limit.
- **OCR Tool FAQ line:** /tool/ocr-tool says "Copy the result or download it as a .txt file or a Word (.docx) file". This page's FAQ says OCR Tool "gives you plain text".
- **Limits** (SCAN_LIMITS): 30 / 25 MB / 150 MB / 4200 px, matching the FAQ. TIFF is refused in `checkScanInput`.
