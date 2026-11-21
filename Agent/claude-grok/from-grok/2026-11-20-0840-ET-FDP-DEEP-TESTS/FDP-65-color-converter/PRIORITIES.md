Sent: 2026-11-21 14:26 ET

# FDP-65 HEX / RGB / HSL Converter: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| Owner Q | Tool takes no trial use: no strip/Quick Buy, copy and Ctrl+C work at 10/10, 0 usage POSTs; blog says conversions count; code wires a gate that never activates | zero.json, left.json, alpha.json (firefoxCap); blog.html | Not on the uncounted-on-purpose list (Nov 20) | Santosh: count it or list it as uncounted; align blog |
| P2 | 8-digit/4-digit HEX alpha altered: aa→ab, 01→00 (transparent), fe→dropped (opaque) | alpha.json | FAQ promises the extra digits; designers paste these back | Keep the input alpha byte for HEX |
| P2 | Limitations say oklch is rejected (it's accepted); how-to omits LAB/OKLCH and contrast; "use Contrast Checker" though contrast is shown | tool-expanded.txt; cases.json | Undersells the tool | Update limits/how-to |
| P2 | Video Kuyt4omoYSg: old 4-row UI, "free" wording, "PDF tools" tag | video/sheet.jpg, info-min.json | Shows less than the tool does | Re-record |
| P2 | Locale pages: H1, subtitle, labels English | locales/*es* | Mixed-language page | Translate tool strings (site-wide) |
| P2 | SEO: meta 69 chars, generic OG | tool.html | CTR | Meta naming OKLCH/LAB/CMYK/alpha/contrast |
| P3 | Out-of-gamut OKLCH row shows the clipped value without saying so | cases.json oklch | Paste-back surprise | "(clipped)" label |
| P3 | Colour picker drops alpha; swatch far down on phones; iPhone SE 9 px; axe label mismatch, region, ad-caption contrast; ja 3 px | alpha.json, devices/*, matrix-results.json | Polish | Note, layout, caption colour (keep reserved ad slots) |
