Sent: 2026-11-21 06:06 ET

# FDP-45 HTML to PDF: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: 16 downloads (13 different documents) for 1 trial use in one page load; +1 only after a reload | json/left.json, outputs/ | Charge per new result (key on the output hash or input+options) and check the limit on every Download. Shared ToolPage fix (see FDP-44) |
| P1 | WebKit (Safari engine): HTML with an external (cross-origin) image never finishes. It sits at "Rendering page 1 of 3… keep this tab open" for 5+ min (two runs), and **Stop doesn't recover** (still rendering 8 s after Stop, no Convert button). The same invoice without the external image converts in 6 s; Chromium and Firefox load the external image fine | json/hang-webkit.json, json/subset-webkit.json, screens/cases/WK-H02_invoice-stuck.png, WK-H02_invoice-afterstop.png | Put a timeout on the html-to-image capture (and on per-image fetches), fall back to the blank placeholder the FAQ promises, and make Stop abort the in-flight capture. Confirm on real Safari/iOS |
| P2 | Download file name sticks to the first document's title or dropped file name ("Invoice INV-2026-045.pdf" for 5 later documents) | outputs/L03–L07, L11–L15 | Recompute the name on every conversion: dropped name if the content is unchanged, otherwise `<title>`, otherwise "document" |
| P2 | Blank first page when the first element has page-break-before | outputs/L03-*.pdf, screens/cases/L03-pages.png | Ignore breaks above the first content (or within the top margin) |
| P2 | `#anchor` and relative links resolve to freedailypro.com in the PDF | outputs/L02 (Annots) | Inject `<base href="about:blank">` or keep only absolute http(s)/mailto hrefs as written; internal anchors → GoTo or skip |
| P2 | windows-1252 .html read as UTF-8 ("Caf� cr�me") | outputs/L09, previews/H09 | Sniff `<meta charset>` / BOM and decode with TextDecoder, or warn |
| P2 | A third-party ad creative styled as a "Start Download (Free) / Add Extension" button sat directly under Convert to PDF (Firefox run), right where the real Download appears | screens/cases/S08-firefox.png | Keep the reserved slot. Block deceptive download/extension creatives in AdSense (Ad review center / blocking controls) and keep clear spacing from the tool's action buttons |
| P2 | Video: old UI, "10 free uses daily", personal Chrome downloads list, extension badge | video/ | Re-record on a clean profile |
| P3 | FAQ duplicates (URL ×2, JavaScript ×2); meta 70 chars; og-default; English locale titles | html/tool-expanded.txt | Merge the FAQs; fuller meta; OG image |
| P3 | Table header doesn't repeat; wide tables shrink to unreadable with no warning | outputs/L02, L07 | Repeat `<thead>` per page; warn when the scale is below ~60% |
| P3 | iPhone SE 9 px / ja 3 px overflow; Margin label vs aria-label mismatch | matrix-results.json, js | Layout/aria fixes |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:**
  - Save to Google Drive (accounts.google.com popup).
  - Save to my cloud storage (email sign-in).
  - Open from Google Drive.
  - Paid-pass behaviour.
