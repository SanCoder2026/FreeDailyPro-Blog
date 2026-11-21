Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 (policy question) | At 0 remaining, Generate, per-row copy, Copy All and selection copy work with no cap dialog (10 → 10, also after reload). The code calls `logUsageNow()` on Generate and `gateShare` on each copy. The blog says "Each press of the button counts as one of your 10 trial usages for the day". The video shows "8 free uses left today". Not in the Nov 20 uncounted list. With uses left: pending. | `json/gate.json`, `json/try.json`, `js/UuidGenerator-*.pretty.js`, `html/blog.txt`; RERUN row 31 | Santosh decides (count one use per Generate, or declare uncounted). Then align the code, blog, page and the JSON-LD Offer (4.99). Avoid charging a separate use for each per-row copy of an already generated batch. |
| 2 | P2 | Only v4. No v7/v1/v5/nil-max; no braces/quotes/CSV/SQL/JSON formats; no Download; no validator/decoder. | `findings/desk-findings.md` | v7 plus format presets plus Download .txt/.csv as the Professional Tools / Premium Applications step; a "Validate a UUID" box. |
| 3 | P2 | Tips: "Output is in the standard lowercase hyphenated form… so uppercase it yourself if a system insists". An Uppercase checkbox exists. The blog asks if readers want "uppercase output". | `html/tool-expanded.txt`, `html/blog.txt` | Rewrite the tip; update the blog. |
| 4 | P2 | Video CuyJw3t7968: old UI ("10 free uses daily", "8 free uses left today", "Security & Developer"), no Hyphens/Uppercase toggles, "FREE" title card and title; the embed name differs. | `findings/video-findings.md`, `video/z20-tl.png` | Re-record with the toggles and Copy All; use "trial uses". |
| 5 | P2 | Large batches: 1,000 cards with 1,000 copy buttons. Copy All sits at the very bottom (keyboard users tab through 1,000 buttons). | `screens/live/case-1000.png`, `json/misc.json` | Copy All and Download above the list; a compact textarea view for batches over ~20. |
| 6 | P2 | Locales: es is half-translated ("gratis" in the title); 8 English pages under their lang/hreflang; /ar 404. Title and meta lack "v4" and "GUID". | matrix, `html/es.html`, `html/ja.html` | Translate or drop hreflang; add "v4 / GUID" to the title or meta. |
| 7 | P3 | iPhone SE 9 px overflow (button right=329, same as FDP-30); ja desktop 3 px. Mobile checkboxes 24 px; Count/Generate 36 px. | `json/matrix-results.json` | Wrap the action row; 44 px targets. |
| 8 | P3 | The stale list stays visible under an invalid count. "1e3" is accepted. "session tokens" in What-is-it vs "do not use as session tokens". The "Keep the Count at 100" tip vs the default of 5. | `json/cases.json`, `html/tool-expanded.txt` | Clear or dim the list on invalid input; align the copy. |
| 9 | P3 | Thumbnail alt; axe label-content-name-mismatch (desktop), region, color-contrast on ad captions (Pixel 7); JSON-LD Offer 4.99. | matrix | Polish. Keep ad slots reserved; fix the caption colour. |
