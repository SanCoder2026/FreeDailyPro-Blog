Sent: 2026-11-21 10:39 ET

# FDP-55 Bates Numbering: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | One trial use per page load (12 numbering runs, 27 files = 1 use; 4 runs with 1 reload = 2 uses) | Gate gap by owner rule; a whole production costs one use | Charge per run of new content (hash the files and settings), and re-check the cap on every run. Then update the FAQ and blog "however many files… in that visit". |
| P2 | Fake "Download" button ad creative in the in-content slot next to the tool | Users may click the ad instead of the real download; trust | Keep ads. Use a reserved, labelled slot away from the result buttons and block download-button creatives in the ad network. |
| P2 | Locale pages half translated (subtitle, drop zone, FAQ English on es/de/ja…) | Mixed-language page | Translate the tool strings (site-wide pattern). |
| P3 | Non-Latin prefix/suffix (Ü案件-) stamp not in the text layer, digits included | Bates search fails in review tools | Add a ToUnicode map or text layer, or document it in Limitations. |
| P3 | bates-index.csv has no UTF-8 BOM | Excel likely mangles non-ASCII names and prefixes (not opened in Excel) | Write a BOM, or offer an .xlsx. |
| P3 | Limitations: locked/damaged files "marked in the list"; live they're toasts/unlock dialog | Copy accuracy | Reword to match (unlock prompt, skipped toast, Repair link). |
| P3 | Cap dialog promises removing a mark this tool never adds | Confusing upsell | Make the mark sentence conditional per tool. |
| P3 | Dark page with "white box" off gives a near-invisible black stamp, with no hint | Unreadable numbers | Show a hint when the box is off, or offer white text. |
| P3 | Tool page related links omit Legal Production Desk / Exhibit Stamper | C11 discovery | Add cross-links. |
| P3 | Blog: "Digit width…" and "Prefix, suffix…" sections after "Closing next step" | Structure | Move them above FAQ. |
| P3 | Video header "200+" vs live "300+" | Small staleness | Refresh at the next re-record. |
| P3 | axe: label-name mismatch, region, ad-caption contrast; ja desktop 3 px overflow | A11y polish | Fix the label and caption contrast (reserved slots kept). |
