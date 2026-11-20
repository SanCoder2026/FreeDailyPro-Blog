Sent: 2026-11-20 08:40 ET

# FDP-04 Compress PDF: priorities

- **Written:** 2026-11-19 11:25:23 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the trial meter honest for a new visitor (checks 5, 16; R-01).**
   - **Outcome:** a fresh device shows 10 remaining and each download (or batch) spends exactly 1.
   - **Why:** 28 of 31 fresh contexts loaded at "0 remaining today". Visitors compress, see a great result, then can't download without paying. This is display-only evidence from one box IP and the same pattern as FDP-02 and FDP-03; verify server-side. One fix covers every tool.

## P1: next

2. **Fix the level-list layout (checks 3, 4; R-02).**
   - **Outcome:** labels are readable and there is no horizontal scroll on phones.
   - **Why:** desktop labels are 48 px wide; Pixel 7 widens to 958 px. This is the decision point for download and upgrade.
3. **Correct the "nothing was changed" diagnosis for CMYK files, and ideally shrink them (checks 1, 6; R-03).** Today a 10 MB CMYK photo PDF is called a JBIG2/JPEG 2000 scan and returned unchanged, while the breakdown says Balanced should shrink it a lot.
4. **Make Extreme match its description (checks 1, 6, 11; R-04):** grey and B/W steps after Run anyway, or a note explaining why they were skipped.
5. **Disclose the trial-use mark before Download (checks 5, 15; R-05).** The cap dialog says passes remove "Created with FreeDailyPro.com"; nothing on the page says trial downloads carry it. Verify what is stamped after the midnight-UTC re-run.
6. **Re-record the video** (old Light/Medium/Strong modes, "10 free uses daily"); use one title on YouTube, JSON-LD and the sitemap (checks 10, 12; R-06).
7. **Locales:** server-side title, meta and H1 for pt, fr, de, ja, hi, zh, ko, id (or drop them from hreflang); remove "gratis" from /es (checks 8, 16; R-07).

## P2: enhancements and polish

8. **Blog:** add Target size, levels, Compare and Several files; remove "unlock first" (check 9; R-08).
9. **Messages:** specific errors for non-PDFs and empty files instead of "damaged, try Repair" (R-09); inline aria-invalid for a bad target; an owner-restriction notice.
10. **Target bytes:** state whether MB means 1,000,000 or 1,048,576 bytes, or aim under the decimal value (1 MB → 1002.6 KB today). Verify bytes on re-run (R-10).
11. **Mobile empty state:** fix the 329 px overflow at 320 px; get the drop zone above the fold on small phones (R-11).
12. **A11y:** focus to the file card after Add and to the result summary after Compress; ad-caption contrast; desktop label mismatch (R-12).
13. **Payments:** consistent Quick Buy flows (both email-first, or document why Monthly goes straight to Stripe); JSON-LD Offer billing period.
14. **Ideas:** "split into parts that fit" when a target is unreachable; destination presets (Gmail 25 MB, a typical 5 MB portal); auto-target from words (optional AI).
