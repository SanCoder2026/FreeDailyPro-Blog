Sent: 2026-11-20 08:40 ET

# FDP-03 Merge PDF: priorities

- **Written:** 2026-11-19 10:51:32 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the watermark promise and the output agree (checks 6, 11, 15, 5; R-01).**
   - **Outcome:** what the page says about marks equals what the downloaded PDF contains, and it is stated before Download.
   - **Why:** the meta, FAQ and H3 say "no watermark… no logo or text is added", but every page of every trial-use download has a "Created with FreeDailyPro.com" badge (11/11, 3/3, 503/503). Users find out after spending a use. That is a trust and complaint risk on a top-5 tool.
2. **Make the trial meter honest for a new visitor (checks 5, 16; R-02).**
   - **Outcome:** a fresh device shows 10 remaining and each download spends exactly 1.
   - **Why:** 16 of 17 fresh matrix and geo contexts and 6 of 7 probe contexts loaded at "0 remaining today". They can merge but must pay to download. This is display-only evidence from one box IP and the same pattern as FDP-02; verify server-side.

## P1: next

3. **Bookmarks match the FAQ (checks 6, 11; R-03).** Per-file bookmarks for every merge (including Arrange output), or a bookmark option. Fix the "What doesn't carry over… Bookmarks do:" answer.
4. **Re-record the video** on the current UI with trial-uses wording; use one title on YouTube, JSON-LD and the sitemap; fix the literal "\u2013" in sitemap video titles (24 lines site-wide) (checks 7, 10, 12; R-04).
5. **Update the blog:** remove "Bookmarks may drop" and "must be unlocked first"; show Arrange, Choose pages, pictures, the blank page, and trial uses (check 9; R-05).
6. **Locales:** server-side title, meta and UI strings for pt, fr, de, ja, hi, zh, ko, id (or drop them from hreflang); remove "gratis" from the /es title (checks 8, 16; R-06).

## P2: enhancements and polish

7. **Specific errors for non-PDFs:** "isn't a PDF / is a PNG renamed / is empty" instead of "damaged, try Repair PDF" (check 3; R-07).
8. **Forms:** keep fields fillable (rename clashes) as competitors do, or at least remove the orphan widgets (checks 2, 15; R-08).
9. **Owner-restricted PDFs:** show that a restriction was present instead of a plain "Unlocked" (R-09).
10. **Mobile:** fix the 329 px header overflow at 320 px; use a compact stepper so the drop zone is above the fold on small phones (check 4; R-10).
11. **A11y:** keep focus on the moved card's button and move focus to Download after Merge; use `li` instead of `figure role=listitem`; fix the "Advertisement" caption contrast and the desktop label mismatch (R-11).
12. **SEO polish:** JSON-LD Offer billing period; tool OG image; video thumbnail alt; matching VideoObject uploadDate.
13. **Ideas:** duplicate page in Arrange; sort by name/reverse; auto-order by detected date (optional AI, P2).
