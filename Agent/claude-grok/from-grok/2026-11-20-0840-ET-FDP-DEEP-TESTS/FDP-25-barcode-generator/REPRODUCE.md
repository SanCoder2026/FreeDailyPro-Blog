Sent: 2026-11-20 08:40 ET

# FDP-25: reproduce

Guest, fresh profile, https://www.freedailypro.com/tool/barcode-generator.

1. **Quiet zones (P1):** Code 128, value `SKU-00042/Blue M` → Download PNG (4×). The first bar starts 40 px from the left edge at 8 px per module = 5 modules (spec 10). EAN-13: right margin 5 modules (spec 7). Read the FAQ "What size should I print?" (3.1 in) against GS1 EAN-13 100% = 37.29 mm.
2. **Usage (policy):** in a visit with uses left, Download PNG (0 → 1), then change value/format, Download SVG, switch to A list (ZIP) and Download ZIP — the count stays at 1. Reload and Download again → 2.
3. **Sample:** fresh visit with uses, press Download PNG without typing → `ean13-5901234123457.png`, 1 use spent.
4. **Caption:** EAN-13 `400638133393`, caption `Organic cotton crew-neck T-shirt, navy, size M` → preview shows "anic cotton … siz".
5. **Phone overflow:** iPhone 13 (Safari) → Format → Code 128 → page pans sideways.
6. **Gate:** at 0 remaining, Download PNG → cap dialog → Buy Day Pass → email prompt. Stop.

Automated: `cd scripts && npm i playwright axe-core`, then `node bc-battery.js`, `node bc-ui.js`, `node bc-browsers.js`, `node bc-dl.js` (add `spend` to look only for a context with uses), `node bc-privacy.js` (spends 2). Decode with `pip install zxing-cpp pillow` (see scripts/README.md). Set OUT paths.
