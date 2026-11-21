Sent: 2026-11-21 08:14 ET

# Instructions for Claude: FDP-50 PDF to Excel

1. Read REPORT.md ("How to work with us" first), then PRIORITIES.md.
2. Fix the shared Download trial-use wrapper: charge per new result and check the cap every time. It's the same fix as FDP-44 to FDP-49, so verify all of them.
3. In `tablesToExcel` (`H()` number parser, `J()` column typing, header regex `X`):
   - Stop header words from blocking money columns.
   - Infer decimal and thousands separators per column (including spaces).
   - Parse CR/DR and ISO currency codes.
   - Add notes for columns kept as text.
4. Add an OCR money fix for "(5" → "($" in currency columns.
5. Re-record the video.
6. Make the owner call on the preview at 0.
7. Verify with test-cases.md, then run `scripts/check-xlsx.py` on fresh downloads of T02, T03, T04, T12 and T08.
8. No sign-in in automated tests and no real payments. Use "Professional Tools" / "trial uses" wording. Keep the reserved ad slots.
