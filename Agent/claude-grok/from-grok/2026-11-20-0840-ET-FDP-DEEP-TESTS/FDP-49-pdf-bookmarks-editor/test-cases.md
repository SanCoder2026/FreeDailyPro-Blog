Sent: 2026-11-21 07:48 ET

# FDP-49 test cases (guest; run after fixes)

| ID | Input / steps | Expected | Today (2026-11-21) |
|---|---|---|---|
| T01 | B01: rename, delete CONFIDENTIAL, add p10 → Download | +1 use; outline matches the edit; Unicode titles intact | PASS (L01: 0→1; tree correct) |
| T02 | Same load: New file → B02 + 2 bookmarks → Download | +1 use | FAIL (stays at 1) |
| T03 | Download the same result again | no extra use | PASS (L01b) |
| T04 | At 2/2 in the same load: new PDF → Download | cap dialog | FAIL (L15 downloaded) |
| T05 | Fresh context at 2/2 → Download | cap dialog $3/$9.99 | PASS (Z01) |
| T06 | Remove all → Download → list objects with /Title+/Parent | none | FAIL (9 titles remain, L16) |
| T07 | Delete one bookmark → Download → search objects | deleted title absent | FAIL (L01, L13) |
| T08 | B03 named dests | pages resolved (3 and 5) | FAIL (empty page, saved as headings) |
| T09 | B03 URI bookmark | link kept or explicit warning | FAIL (silently dropped) |
| T10 | B03 XYZ zoom bookmark | page kept, Fit (documented) | PASS |
| T11 | B04 user password: wrong then right password | "That password didn't work…", then loads; result unencrypted | PASS (M02) |
| T12 | B05 owner-only password | loads (owner question: restrictions dropped) | Loads with "Unlocked" toast |
| T13 | B06 not a PDF / B12 truncated | "can't be read — it looks damaged… Repair PDF" | PASS (M06, M12) |
| T14 | B07 300 pages / 300 bookmarks | loads < 5 s; Remove all → no outline | PASS (3.5 s) / orphan issue T06 |
| T15 | B08 move/indent/outdent | tree correct; colour/bold/closed kept | PARTIAL (tree correct; styles lost) |
| T16 | B10 form, link, metadata | all preserved | PASS (L09) |
| T17 | B11 cyclic outline | loads without hang; 2 items | PASS (L10) |
| T18 | Page 13 on a 12-page file | error, Download disabled | PASS (L11) |
| T19 | Empty title / no page | warnings; saved as "Untitled" heading | PASS (L11) |
| T20 | Add with page 99 / empty title | "Enter a page number from 1 to 12." / "Type a title…" | PASS |
| T21 | Insert position | after the selected bookmark at same level, hint updates | PASS |
| T22 | Open from Google Drive | sign-in required | Untested (sign-in) |
| T23 | Network during the whole flow | no PDF bytes POSTed | PASS (0 PDF-bearing POSTs) |
| T24 | Firefox / WebKit subset | same as Chromium | see subset-*.json |
