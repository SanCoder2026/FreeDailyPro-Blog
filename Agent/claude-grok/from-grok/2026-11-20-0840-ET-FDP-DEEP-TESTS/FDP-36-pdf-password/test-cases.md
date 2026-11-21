Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: test cases

Inputs: `scripts/make-pdfs.py`. Scripts: `pp-live.js [chromium|firefox] [ids]`, `pp-unlock.js`, `pp-gate.js`, `pp-privacy.js`, `pp-share.js`, `verify.py`, `run-matrix.js`. Passwords used: `Tr1al-Horse-42!`, `Pässwört-日本語-42`, `space pw 42 ` (trailing space).

| ID | Area | Input / action | Expected | Result 2026-11-21 |
|---|---|---|---|---|
| PW-01 | Encrypt | P01 3-page form PDF, strong password | AES-256 R6; opens only with password; pages/title/fields/outlines/links kept; Checked line | PASS (A, L01) |
| PW-02 | Encrypt | P03 50 pages, unicode password | opens with exact unicode password; 50 outlines/links | PASS (C, L02) |
| PW-03 | Encrypt | P02, password with trailing space | space note shown; opens only with exact password | PASS (D) |
| PW-04 | Blocks | all three block boxes | print/copy/modify off, accessibility on, random owner password | PASS (B /P −3392) |
| PW-05 | Blocks | Printing only | print off, others on | PASS (E /P −2056) |
| PW-06 | Blocks | no boxes | full rights for password holder (explicit allow-all) | PARTIAL P3 (/P −3904, owner = user) |
| PW-07 | Batch | B1–B5 one password | 5 AES files + ZIP, one use per batch run | PASS output; charging see PW-19 |
| PW-08 | Batch | B1–B6 on trial | 6th left out with clear toast | PASS |
| PW-09 | Input | P04 AES user-password PDF, wrong then right password | error, then Unlocked, then protect with new password | PASS |
| PW-10 | Input | P09 RC4 user-password PDF | unlock then protect | PASS |
| PW-11 | Input | P04 then Cancel | clear one-file message | PARTIAL P3 (toast mentions list/row) |
| PW-12 | Input | P05 owner-only restricted PDF | disclose that restrictions are removed | PARTIAL P3 (silent) |
| PW-13 | Input | corrupt PDF / text renamed .pdf | clear error | PASS / P3 wording for non-PDF |
| PW-14 | Input | 52 MB PDF | soft warning, completes | PASS (4.7 s) |
| PW-15 | Password | 5 chars / mismatch | button disabled with reason | PASS |
| PW-16 | Password | 'letmein', 'aaaaaaaa' | Weak (very common) | PASS |
| PW-17 | Password | Show/Hide, Reset | both fields toggle; Reset clears | PASS |
| PW-18 | Gate | Protect | no use (charge at Download) | PASS (0→0) |
| PW-19 | Gate | second+ Download of other files in same page load | −1 each (Nov 20 every-Download decision) | FAIL P1 (stayed 1, four times) |
| PW-20 | Gate | Download after reload | −1 | PASS (1→2) |
| PW-21 | Gate | batch per-file 2 / ZIP after per-file 1 | per decided batch rule | FAIL P1 (free) |
| PW-22 | Gate | at 0: result preview | no full-quality copy | PASS (no preview element) |
| PW-23 | Gate | at 0: Download / batch file / ZIP | cap dialog | PASS |
| PW-24 | Payment | cap dialog → Buy Day Pass; Quick Buy day/monthly | email prompt / Stripe (stop) | PASS |
| PW-25 | Privacy | marker password | not in any request, storage or cookie; gone after reload | PASS |
| PW-26 | Share | Share this tool | URL only | PASS |
| PW-27 | Sign-in | Save to Google Drive / my cloud storage | sign-in (untested) | UNTESTED |
| PW-28 | Keyboard | Tab to drop zone + Enter | chooser opens | PASS |
| PW-29 | Copy | FAQ unlock / block / Limitations encrypted input | match behaviour | FAIL P2 |
| PW-30 | Video | qBJKvkcI298 | current UI, AES-256 | FAIL P2 (RC4 128-bit) |
| PW-31 | Devices | 10 devices | no overflow | PARTIAL (iPhone SE 9 px) |
| PW-32 | Locales | 10 + /ar | translated head, no overflow | PARTIAL (English title/meta, ja 3 px, /ar 404) |
| PW-33 | axe | desktop + Pixel 7 | no serious | FAIL P3 (label mismatch, contrast) |
| PW-34 | Firefox | L01, L09, L15 | same as Chromium | PASS |
