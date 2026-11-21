Sent: 2026-11-21 17:13 ET

# FDP-75 reproduce

1. **Per-page-load charge (P1):** a guest window whose `fdp-usage-v1` shows uses left → https://www.freedailypro.com/tool/paper-format-checker → drop `evidence/testfiles/apa-good.docx` (strip goes down by 1, one `usage.log` POST) → "Check another file" → drop word-default.docx, a4-narrow.docx, mixed-fonts.docx… → every report appears, no POST, strip unchanged. Reload → drop one → charged again.
2. **Gate at the cap:** a window at 10/10 → drop apa-good.docx → cap dialog, no report.
3. **FAQ vs direct formatting (P2):** drop `direct-format.docx` with APA → Font size FAIL "10 pt", Line spacing FAIL "1×". Compare with the FAQ "Does this catch formatting I applied to individual paragraphs? No…".
4. **Footer page number (P3):** `node scripts/px75-harness.js APA evidence/testfiles/footer-pageno.docx` (NODE_PATH with @xmldom/xmldom + jszip) → pageno PASS though the field is centred in the footer.
5. **Video:** https://www.youtube.com/watch?v=f4VPRP4U4iM at 0:17 (bookmarks bar) and 0:52 ("Couldn't detect" rows).
