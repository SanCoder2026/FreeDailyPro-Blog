Sent: 2026-11-21 06:22 ET

# FDP-46 Mail Merge to PDF: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: 9 downloads (incl. a 500-file ZIP) for 1 trial use in one page load; +1 only after a reload | json/left.json, outputs/ | Charge per new result (key on table+template+options hash) and check the limit on every Download. Shared ToolPage fix (FDP-44/45) |
| P2 | Hidden Excel rows are merged (M03: hidden José row becomes record 2 of 5) | json/next-at0.json, screens/cases/N-M03-hiddenrow.png, testfiles/M03 | Skip rows with `ws['!rows'][i].hidden` (and filtered rows), say "1 hidden row skipped", offer to include |
| P2 | Devanagari drawn as unshaped text: "प्रिया शर्मा" → "प्रयिा शर्‍मा"; the copy says non-Latin text is drawn as pictures | outputs/L07, screens/cases/L07-hindi-zoom.png | Route Indic scripts through the picture path (or shape with HarfBuzz); fix the Limitations line. Shared drawTextAnywhere (FDP-44) |
| P2 | Locale pages: tool labels, About/FAQ, title and meta in English on 10 locales | json/matrix-results.json, screens/locales | Translate tool strings and meta |
| P3 | Fixed names "merged-documents.pdf/.zip" (collides with Merge PDF output) | outputs/ | e.g. "mail-merge-<n>-records.pdf" |
| P3 | ZIP-name placeholder "First Name" looks filled; empty → record-N | outputs/L01z | Placeholder "Pick a column (optional)" or default to the first column |
| P3 | Starter template only when the table box was empty (FAQ says "as soon as the table is in") | json/left.json L05, js | Also make it when the template is empty |
| P3 | Braces header → "Dear {{{{Name}}}}" plus a contradictory note | outputs/L13 | Strip braces from headers or warn |
| P3 | CON.pdf in ZIP; "Dear  Blank-First" double space | outputs/L08, next-at0.json | Prefix reserved names; collapse spaces |
| P3 | iPhone SE 9 px overflow; axe label-content-name-mismatch; ad-label contrast | matrix-results.json | Layout/aria fixes (keep the ad slot) |
| Owner Q | Overflow message ("the tool tells you which rows did") not captured | outputs/L09 (4 pages for 3 records) | Recheck by hand |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:** Open from Google Drive; paid-pass behaviour.
