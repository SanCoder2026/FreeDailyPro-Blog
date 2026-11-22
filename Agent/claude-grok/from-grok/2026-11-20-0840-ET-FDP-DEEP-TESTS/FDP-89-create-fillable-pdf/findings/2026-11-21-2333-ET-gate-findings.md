Sent: 2026-11-21 23:35 ET

# Gate and usage

- `checkExport` (useExportGate) → ToolPage `Ys`: check only, no POST. Runs before `qe`, so at 0 uses nothing is built.
- Charge: `ui.s(bytes,name,type)` → ToolPage `d` → registered `logUsageNow("download")` → `tryUse` → per-tool flag (cleared on unmount). One POST per page load.
- left.json load 1: L03b first success 1 POST; then L03c, L01, X01, L02, L04, L05, L05b, L05c, L06, L08, L11 = 12 more files, 0 POSTs.
- charge-2.json: server usage.check 0 → 1 after one download; reload shows 1.
- left2.json: M02 0→1 (1 POST), M07 same load 0 POSTs, M08 new load 1→2 (1 POST).
- First run's badge 0/2→2/2 on one POST: treated as pooled-device noise (not reproduced).
- Failed build (Cyrillic starting value): 0 POSTs, no charge.
- Z14 at cap: cap dialog "Today's trial uses are done | Your input stays where it is, but downloading needs a pass…", 0 POSTs, no file.
