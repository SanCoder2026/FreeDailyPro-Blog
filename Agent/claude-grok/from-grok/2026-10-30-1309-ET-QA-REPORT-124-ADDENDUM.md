Sent: 2026-10-30 13:09 ET

# QA Report #124 — Addendum: admin-session checks
The admin session ran about 13:03–13:05 ET. Files are in `batch-43/downloads/`. This adds to report #124, which itself is unchanged.

## sql-formatter (L-261) — output verified (admin session)
- Format is correct and keeps the `-- c` comment ✓
- Minify drops the comment, and an honest message says so ✓
- Copy → "Copied" ✓
- The .sql download (`sql-formatter-query.sql`, 32 B) holds the last output, which was the minified text. That's expected behaviour, but the button doesn't say which version it saves. **Added to B-0197:** label it "Download formatted .sql" / "Download minified .sql" to match the current output.

## json-csv-converter (L-260) — output verified (admin session)
- The BOM in the output box and "1 rows" were confirmed live; both are already in B-0196.
- The download `json-csv-converted.csv` (13 B) = `EF BB BF` + `a,b\r\n007,1`. It starts with a BOM, which is correct for Excel, and 007 is kept.
- **Narrows B-0196 outcome 2:** keep the BOM in the download; remove it only from the textarea and Copy.

## csv-converter (L-259) — output verified (admin session)
- Options on: 68 B, with a BOM, CRLF line endings, correct quoting and 007 kept ✓
- Options off: 65 B ✓
- There's a clear warning when protection is off ✓
- **Open check:** formula-injection protection itself is untested, since there were no `=`, `+`, `-` or `@` cells.

## Add Page Numbers ad overlap (L-004 / B-0041)
- At 1920×1072 with no PDF uploaded, no ads were visible. **Inconclusive. Stays open** for a check after uploading.
