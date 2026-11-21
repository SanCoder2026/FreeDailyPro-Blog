Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: reproduce

Guest browser, https://www.freedailypro.com/tool/compare-pdf. Test files are in `evidence/testfiles/`.
1. **Full result at 0 trial uses:** with the strip at "0 remaining today", drop `C01_contract_v1.pdf` as Original and `C02_contract_v2.pdf` as Revised, then press Compare PDFs. All 6 changes appear with word marks; Side by Side works; text can be copied. Press Report (PDF) → cap dialog.
2. **Per page load:** with uses left, Compare (count unchanged), then Report (PDF) (−1), Report (.txt) (no change). New Comparison → `C06_log_50p_v1.pdf` vs `C07_log_50p_v2_p37change.pdf` → Report (PDF) (no change). Reload, compare again, report (−1).
3. **Dark contrast:** in the default dark theme, look at the struck-through red words in Side by Side.
4. **Locked:** drop `U01_aes256_user_old123.pdf` and press Cancel. The inline text says "Unlock it with Unlock PDF" and the toast says "Use Unlock on its row".
5. Scripts: `scripts/README.md`.
