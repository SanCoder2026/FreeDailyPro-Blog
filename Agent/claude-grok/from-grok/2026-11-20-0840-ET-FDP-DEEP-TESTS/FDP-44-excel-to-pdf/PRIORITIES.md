Sent: 2026-11-21 05:21 ET

# FDP-44 Excel to PDF: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: 1 trial use covered 12 distinct workbooks in one page load. After the counter reached 10/10 mid-session, Downloads still went through with no cap dialog | json/gate-1.json, json/cases-chromium.json (T14, T17), outputs/ | Charge per new result (key on the output hash or file+options), and check the limit on every Download |
| P2 | Hindi drawn as unshaped text ("नमस् ते") and 🚀 as a box, under a "drawn as pictures so they look right" warning | outputs/T06-X03_scripts.pdf, screens/cases/T06-hindi-zoom.png | Route Devanagari (and all emoji) to the picture path, or shape properly |
| P2 | Copy conflict: FAQ says "?" while About/Limitations/warning say pictures | html/tool-expanded.txt | One accurate answer |
| P2 | Picture note missing for openpyxl/pandas .xlsx (prefix-only `xdr:pic` match); .xls drops chart and picture silently | T01 vs T18, T14 | Namespace-aware drawing scan; notes for .xls, or adjust the copy |
| P2 | Blog says to scroll the whole preview to the last page; the tool previews the first page only | html/blog-excel-to-pdf.html | Fix the blog line |
| P2 | .ods reject: "looks like a OpenDocument spreadsheet file, not a spreadsheet" | T15 | "This is an OpenDocument (.ods) file. Save it as .xlsx and try again." |
| P2 | Video: old UI, personal macOS Downloads, "Free … no account" | video/ | Re-record on a clean profile |
| P3 | iPhone SE 9 px / ja 3 px overflow; axe label-content-name-mismatch; ad-caption contrast | matrix-results.json | Layout/aria fixes; keep the reserved ad slots |
| P3 | Locale titles/meta English; meta 86 chars; og-default image; "EXCEL" caps on the FCS link | tool.html | Copy/asset polish |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:**
  - Save to Google Drive (accounts.google.com popup).
  - Save to my cloud storage (email sign-in).
  - Open from Google Drive.
  - Behaviour with a paid pass.
