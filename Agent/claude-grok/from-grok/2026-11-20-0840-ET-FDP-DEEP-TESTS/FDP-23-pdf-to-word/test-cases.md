Sent: 2026-11-20 08:40 ET

# FDP-23 PDF to Word: test cases (guest, fresh context)

| ID | Input (`evidence/testfiles/`) | Action | Expected after fix |
|---|---|---|---|
| PW-01 | rich.pdf | Convert | "1. Step one…3." numbers present; headings as Heading styles; table, bullets, picture, bold/italic kept |
| PW-02 | rich.pdf, pages 2 | Convert | 1 page |
| PW-03 | rich.pdf, pages 5 | Convert | "Page 5 is outside…" |
| PW-04 | scan_rich_2p.pdf | Convert (Chromium, Firefox, **Safari/WebKit**) | OCR result, no crash |
| PW-05 | C_scan_grey_4p.pdf | Convert, then Stop on a 2nd run | OCR 4 pages; Stop returns to options |
| PW-06 | G_nonlatin_2p.pdf | Convert | Scripts exact |
| PW-07 | H_rotated_p2_3p.pdf | Convert | Page 2 landscape |
| PW-08 | J_password_user123_2p.pdf | wrong, then user123 | "didn't work", then converts |
| PW-09 | K_owner_only_restricted_2p.pdf | Convert | Converts; message mentions restrictions |
| PW-10–12 | L_truncated / N_text_renamed / P_empty | drop | "looks damaged" + Repair PDF |
| PW-13 | I_form_1p.pdf | Convert | Form values written |
| PW-14 | table.pdf | Convert | Price and ZIP in separate cells |
| PW-15 | contract.pdf | Convert | Header with PAGE/NUMPAGES fields |
| PW-16 | A_a4_3p.pdf | Convert | Token-identical |
| PW-17 | F_large_500p.pdf, pages 1-3,6 | Convert | 4 pages |
| PW-18 | scan_rich_2p.pdf, Hindi | Convert | Garbage expected; ideally a hint |
| PW-19 | F_large_500p.pdf | Convert | 500 pages ~1 s |
| PW-20 | twocol.pdf | Convert | Sentences 01–60 in order |
| PW-21 | rich.pdf at 0 remaining | Download | Cap dialog → Day Pass $1 → email prompt (stop) |
| PW-22 | rich.pdf with uses | Download ×2, Convert another + Download | 0 → 1 then free; bytes = memory |
| PW-23 | any | Save to my cloud storage | Sign-in dialog |
| PW-24 | page | axe after result | No contrast / scrollable-region issues |
