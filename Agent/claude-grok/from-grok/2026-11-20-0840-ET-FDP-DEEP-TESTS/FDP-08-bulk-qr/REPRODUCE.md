Sent: 2026-11-20 08:40 ET

# FDP-08 Bulk QR Generator (bulk-qr): reproduce

- **Written:** 2026-11-19 13:02:21 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks. Stop at the cap dialog.
- **Automation:** `cd /workspace/deep/tools-env`. The scripts write to `/workspace/deep/08-bulk-qr/live/`.

## R-01: fresh contexts load at 0 remaining
- Run `node scripts/bq-probe.js` several times, or the matrix.
- **Seen 2026-11-19 12:37–13:05 EST:** every matrix and geo context (16/16) was at 0. Only the two battery D contexts loaded at 10.
- Display-only; verify server-side.

## R-02: the pass key can't be saved at 0
1. Use a context at 0 remaining. Press "Try a sample", then "Guest passes from my project (8)". 5 pass previews appear.
2. Press "Save project". The cap dialog appears: "Today's trial uses are done | Your input stays where it is, but downloading needs a pass" (`json/kbd.json` → save).
3. In a context with uses left, Save was free (`json/battery-1795110828068.json`, D2: 9 → 9).
4. The project bar says "Kept in this tab only, then erased". No prompt to save appears after Generate.
5. The saved sample file holds the key plus guest emails, dietary needs, rooms, vendors and expenses (`downloads/…REDACTED.json`).

## R-03: one long line
1. Paste `https://ok.example` plus one line with 3,000 characters.
2. The preview shows 0 images, the counter says "2 QR codes will be generated" and Generate is enabled (`json/explore-*.json` S08).
3. By code (BulkQr `oe()`): `await logUsageNow()`, then the build, then catch → "Generation failed". Re-run battery E to see whether the strip drops.

## R-04: name-mode duplicates
- Tick "Lines are name,value". Paste "Table 1,https://example.com/menu" and "Table 2,https://example.com/menu".
- Result: "… (1 duplicate line skipped)", and only one preview (S04).
- Code: qrHelpers `D()` deduplicates on the value.

## R-05: guest passes "(0)"
On a fresh page, "Guest passes from my project (0)" switches to an empty passes view. Nothing explains how to add guests.
