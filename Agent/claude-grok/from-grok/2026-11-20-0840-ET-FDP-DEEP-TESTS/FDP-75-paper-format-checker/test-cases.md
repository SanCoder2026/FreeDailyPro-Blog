Sent: 2026-11-21 17:13 ET

# FDP-75 test cases

Row order: margins, page, font, size, spacing, gap, indent, ref hanging indent, page number. Live = Firefox left run; harness = the tool's `De` under node. Live and harness agree on every paper tested live.

| ID | Paper / action | Expected | Result |
|---|---|---|---|
| Z01 | 10/10: drop apa-good | Cap dialog, no report | PASS (0 POSTs) |
| Z02 | 10/10: drop old.doc | Inline .docx error | PASS |
| Z03 | Open from Google Drive | Google sign-in | Popup (closed; sign-in row) |
| L01 | apa-good, APA/MLA/Chicago | All PASS; 1 use | All PASS; 0→1/10, 1 POST |
| L02 | word-default (Cambria 11, 1.15, 8 pt after, 1.25" sides) | Most FAIL | FAIL margins/font/size/spacing/gap/indent/pageno; refs WARN. MLA font PASS; Chicago font WARN, size PASS. **0 POSTs (P1)** |
| L03 | a4-narrow | Margins + page FAIL | PASS (as expected); 0 POSTs |
| L04 | direct-format (Normal APA, runs Arial 10 single) | FAQ: not caught | **Caught**: size FAIL 10 pt, spacing FAIL 1× (FAQ wrong, P2) |
| L05 | mixed-fonts | Font FAIL with % | "TNR (50%), Arial (50%) — body text mixes fonts" |
| L06 | exact-24pt | Counts as double | PASS |
| L07 | two-sections (2nd left 1.5") | Margins FAIL | "1 of 2 sections differ" |
| L08 | refs-no-hanging | Hanging FAIL | "0 of 3 … set Special to Hanging, 0.5"" |
| L09 | georgia-11 | APA PASS; MLA size FAIL; Chicago font WARN | As expected |
| L10 | no-page-number | Page number FAIL | As expected |
| L11 | empty | No-text message | 4 WARN "No body text", 3 PASS; no overall message (P3) |
| L12 | long-60p (220 paragraphs) | All PASS | "220 of 220" |
| L13 | minimal (document.xml only) | Undetermined font | Font FAIL "unknown" (P3) |
| L14 | not-docx (renamed PDF) | Clear error, no charge | PASS |
| L90 | Reload, drop apa-good | 1 use | 1→2/10, 1 POST |
| L91 | Same file again | No charge | No charge |
| H | footer-pageno (harness) | APA wants header top right | PASS (P3) |
| Q | Quick Buy Day / Monthly | Email / Stripe | Stopped at both |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locale body English (P2) |
