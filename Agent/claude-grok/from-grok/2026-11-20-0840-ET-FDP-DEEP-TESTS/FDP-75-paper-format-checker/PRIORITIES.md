Sent: 2026-11-21 17:13 ET

# FDP-75 priorities

**P0:** none found.

**P1**
1. Per-page-load charging: in one Firefox load from 0/10, 14 different papers were fully checked for 1 trial use (1 `usage.log` POST; counter 1/10). A reload charged once more (2/10). The cap dialog never comes within a load. At 10/10 the gate holds (dialog, no report). Charge per new document and re-check the cap on every drop. (`json/left-firefox.json` L01–L14, L90, L91.)

**P2**
1. The only FAQ says formatting applied to individual paragraphs isn't caught; the tool reads direct paragraph/run formatting (direct-format.docx → Arial 10 single flagged), and the page's own About text says so.
2. Video f4VPRP4U4iM: old 4-check version, demo file gets "Couldn't detect" warnings, old "default formatting only" note; personal bookmarks bar visible throughout (0:17).
3. Locale pages: H1, subtitle, controls, drop zone and FAQ English.

**P3**
1. "Page numbers in the header (top right)" passes a centred footer page number (footer-pageno.docx).
2. Empty .docx: no overall "no text" message; minimal.docx font "unknown" is FAIL rather than undetermined.
3. Cap dialog promises removing a PDF/image mark; this tool has no output.
4. Blog TOC literal `&#39;`; 300+ vs 200+ tools; subtitle lists 3 of 9 checks.
5. iPhone SE 9 px; ja desktop overflow; CLS 1.0 boot shift at 1366; axe label-content-name-mismatch + region.
