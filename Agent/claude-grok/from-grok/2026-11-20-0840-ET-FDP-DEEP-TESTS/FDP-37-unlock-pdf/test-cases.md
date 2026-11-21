Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: test cases

Inputs: `scripts/make-locked.py` (needs FDP-36 `make-pdfs.py` sources: P01, P02, P03). Passwords: U01/U02 `old123`, U03 `rc4pass`, U04 `rc4old`, U06 `Pässwört-日本語-42`, U07 `space pw 42 ` (trailing space), U08 `same123`, U09 owner `ownerX1`. Scripts: `ul-live.js`, `ul-gate.js`, `ul-handoff.js`, `ul-privacy.js`, `verify.py`, `run-matrix.js`.

| ID | Area | Input / action | Expected | Result 2026-11-21 |
|---|---|---|---|---|
| UL-01 | Unlock | AES-256 user password, right password | Password removed; download unencrypted, matches source | PASS (K01, A) |
| UL-02 | Unlock | AES-128 | same | PASS (K02, B) |
| UL-03 | Unlock | RC4-128 | same | PASS (K03, E) |
| UL-04 | Unlock | RC4-40 | unlocked | PASS (K04) |
| UL-05 | Unlock | owner-only restrictions | unlocks without prompt; download unrestricted | PASS (K05, C) |
| UL-06 | Unlock | unicode password, 50 pages | unlocked; 12 thumbnails + note | PASS (K06) |
| UL-07 | Unlock | trailing-space password, trimmed then exact | trimmed rejected, exact accepted | PASS (K07) |
| UL-08 | Unlock | user = owner password | unlocked | PASS (K08) |
| UL-09 | Unlock | open with owner password | unlocked | PASS (K09) |
| UL-10 | Unlock | wrong case, wrong, right | retry message twice, then unlocked | PASS (K10) |
| UL-11 | Input | unprotected PDF | labelled pass-through, byte-identical, free | PASS (K11, D) |
| UL-12 | Input | corrupt / text renamed .pdf | clear 'couldn't be read as a PDF… Nothing was used' | PASS (K12, K13) |
| UL-13 | Input | Cancel the dialog | Skipped toast, back to drop zone | PASS (K14) |
| UL-14 | Gate | Unlock | no use (charge at Download) | PASS (0→0) |
| UL-15 | Gate | second+ unlocked Download in same page load | −1 each (Nov 20 decision) | FAIL P1 (B, C stayed 1) |
| UL-16 | Gate | Download after reload | −1 | Observed 1→10 display jump (P2) |
| UL-17 | Gate | at 0: thumbnails | no full-quality output | PASS (244×316, ≤12) |
| UL-18 | Gate | at 0: Download | cap dialog | PASS |
| UL-19 | Gate | at 0: hand-off to Compress PDF, run, Download | cap dialog | PASS |
| UL-20 | Gate | at 0: unprotected pass-through Download | free by design; no stale 'not done' banner | PARTIAL P3 (stale banner) |
| UL-21 | Payment | cap → Buy Day Pass; Quick Buy day/monthly | email prompt / Stripe (stop) | PASS |
| UL-22 | Privacy | unicode password marker | not in requests, storage, cookies | PASS |
| UL-23 | Share | Share this tool | URL only | PASS |
| UL-24 | Sign-in | Save to Google Drive / my cloud storage | sign-in (untested) | UNTESTED |
| UL-25 | Keyboard | Tab to drop zone + Enter | chooser opens | PASS |
| UL-26 | Content | blog / video | exist and match | FAIL P2 (none) |
| UL-27 | Devices | 10 devices | no overflow | PARTIAL (iPhone SE 9 px) |
| UL-28 | Locales | 10 + /ar | translated H1/title, no overflow | PARTIAL (H1/title English, ja 3 px, /ar 404) |
| UL-29 | axe | desktop + Pixel 7 | no serious | FAIL P3 (label mismatch, ad caption contrast) |
| UL-30 | Firefox | K01, K05, K11 | same as Chromium | PASS |
