Sent: 2026-11-21 06:22 ET

# FDP-46 Mail Merge to PDF: test cases (rerun after fixes)

Guest, fresh profile; test files in `evidence/testfiles`. "Now" is what we saw on 2026-11-21.

| ID | Case | Expected | Now |
|---|---|---|---|
| MM-01 | At 0: example, preview, Next/Previous | Works; text preview only | PASS |
| MM-02 | At 0: Download one PDF / ZIP | Cap dialog | PASS |
| MM-03 | Day Pass / Quick Buy | Email prompt / Stripe (stop) | PASS |
| MM-04 | Uses left: Download | +1, badge on each page | PASS |
| MM-05 | Same load: Download 5 new results | +1 each | **P1 FAIL** (no change) |
| MM-06 | Reload, Download | +1 | PASS |
| MM-07 | M02: {{ course }}, {{Frist}}, blank cell | Matches; {{Frist}} visible + note; "Empty value in rows: 6" | PASS |
| MM-08 | M03 hidden row | 4 records (or ask) | **P2 FAIL** (5, José included) |
| MM-09 | M03b hidden first sheet | Reads "Visible" sheet with a toast | PASS |
| MM-10 | M04 BOM + semicolon | Parsed, no BOM in the first header | PASS |
| MM-11 | Pasted Excel cells into a filled box, template empty | Starter template | P3 (none) |
| MM-12 | M06 501 rows | Download disabled + "Split the table" | PASS |
| MM-13 | M07 scripts, Certificate | All names correct | **P2 FAIL** (Hindi unshaped) |
| MM-14 | M08 ZIP names | Safe, deduped, blank → record-N, no reserved names | PASS (CON.pdf P3) |
| MM-15 | M09 long/unbroken text | Wraps, continues, rows reported | Wraps (4 pages); report unverified |
| MM-16 | Type size 5 / 73 / 12 | Error + disabled / OK | PASS |
| MM-17 | M11 corrupt xlsx | Clear error | PASS ("Couldn't read that file…") |
| MM-18 | M12 .docx | Clear error | PASS |
| MM-19 | M13 braces header | Braces stripped or warned | P3 |
| MM-20 | M14 500 rows ZIP | 500 named PDFs | PASS (2.5 s, 850 KB) |
| MM-21 | Privacy | No table data in requests | PASS |
| MM-22 | Firefox/WebKit subset | Same as Chromium | see json/subset-*.json |
