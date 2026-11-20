Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | Print specs: quiet zones 5X on all formats (need 7–10X); ITF-14 no bearer bars; fixed bar height (truncated); FAQ size advice ≈212% (> GS1 200% max) and "don't shrink below" | `findings/live-functional-findings.md`, `testfiles/outputs/downloads/`, codeGeneration L77–87 | Spec quiet zones per format, bearer bars for ITF-14, proportional height; state 100% size and the 80–200% range |
| 2 | P1 (policy question) | One trial use per page visit unlocks unlimited different downloads incl. 200-barcode ZIPs; reload charges again | `json/dl-spend.json`, `json/privacy.json` | Santosh decides: per result / per ZIP / per visit; then make the gate match and say so on the page |
| 3 | P2 | Sample value downloadable and charged | dl-spend s1 | Disable Download until the user changes the sample, or don't charge it |
| 4 | P2 | Captions wider than the bars are cut on both sides | `screens/live/box-cap-C2.png`, `box-B30.png` | Widen the canvas to the caption, wrap, or warn |
| 5 | P2 | Phones: choosing Code 128 widens the Format box to ≈453 px; page scrolls sideways (iPhone 13, Pixel 7, SE) | `screens/live/overflow-iphone13-webkit.png`, `json/browsers.json` | Truncate the trigger label (min-w-0 / truncate) |
| 6 | P3 | Stale "Prints … wide" under an error; no length guard (400 chars → 118 in); index.csv value mixes forms; canvas no text alternative; SVG size/live font; FAQ "almost any text"; cap dialog "mark" wording | battery, dl-spend, ui.json | Small fixes |
| 7 | P3 | Video lacks ZIP mode, number toggle, bar height; 21 s end card; /blog/barcode-generator 404 | `findings/video-findings.md` | Refresh video when convenient |
