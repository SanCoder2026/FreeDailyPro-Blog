Sent: 2026-11-21 06:49 ET

# FDP-47 Screenshot Capture & Editor: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: after the first charged Download, 6 more results (crop Download, Copy, editor PNG + JPG, stitched page, new capture) in the same page load with no dialog, while the strip said "0 remaining today"; the cap dialog only appears after a reload | json/main.json, outputs/C0*, screens/cases/C05-editor.png | Charge per new result (hash of the canvas/blob) and check the cap on every Download and Copy. Shared ToolPage/useShareGate fix (FDP-44/45/46) |
| P1 | Android phones (Chrome, Samsung Internet, Firefox for Android) have no `getDisplayMedia`: the page shows Take Screenshot, the delay buttons and the $3/$9.99 offer, and only says "Screen capture isn't supported in this browser" after a tap. How-to says "especially on mobile"; JSON-LD "Any (Web Browser)" | json/mobile.json, screens/cases/M-*.png, caniuse (2026-11-21) | Feature-detect on load: show a short note in place of the buttons ("Screen capture needs a computer or iPhone/iPad with iOS 27+. On Android, take a screenshot with your phone, then use Resize & Crop"), and hide/soften the pass offer there. Fix the copy and JSON-LD |
| P2 | Video is from an older version: light UI, "Screenshot Tool", pencil/highlighter only, "10 free uses daily"; title/description say "Free" | video/sheet01-03.png, v.info.json | Re-record the current editor (arrow, text, pixelate, whole page) with "trial uses" wording |
| P2 | Locale pages: tool controls, title, meta, How to use, FAQ headings in English (H1 translated) | json/matrix-results.json, screens/locales | Translate tool strings and meta |
| Owner Q | Two badges on every download; on small crops they cover the subject | outputs/K-download-*.png | Owner decision (badge is intentional): one badge, or size/position relative to the image |
| Owner Q | Copy gives an unbadged image; Download is badged | outputs/K-copy-clipboard.png | Owner decision |
| P3 | Counter jumped 0→2 after one action in 2 of 5 fresh contexts (one usage.log POST) | json/main.json, json/check-copy.json | Check the server-side device match; display-only evidence |
| P3 | Highlighter overlap dots; rotate clears undo | outputs/C05-edited-*.png, json/main.json C05rot | Draw the highlighter stroke as one path on a temp layer; keep undo across rotate |
| P3 | Meta/subtitle undersell; og-default; FAQ silent on phones; pixelate minimum 6 px blocks (add a solid redact option) | html/, js/ | Copy + small feature |
| P3 | iPhone SE 9 px / ja 3 px overflow; axe label-content-name-mismatch; "Download Template Free" ad creative beside the tool (WebKit run) | matrix-results.json, screens/cases/S01-webkit.png | Layout/aria fixes; keep the slot, block download-lookalike ad categories |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:** paid-pass behaviour (no badge, unlimited). No Drive/cloud features exist on this tool.
