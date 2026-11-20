Sent: 2026-11-20 08:40 ET

# FDP-08 Bulk QR Generator (bulk-qr): priorities

- **Written:** 2026-11-19 13:02:21 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the trial meter honest for a new visitor (checks 15, 16; R-01).**
   - **Outcome:** a fresh device shows 10 remaining.
   - **Why:** about 34 of 36 readable fresh contexts loaded at 0. This is display-only evidence from one box IP, and the same pattern as FDP-02 to FDP-06. Verify server-side.

## P1: next

2. **Protect the pass key and the project (checks 13, 16; R-02).**
   - Save project is blocked by the cap dialog at 0 (it was free with uses left).
   - There is no save prompt after generating passes.
   - The project is "kept in this tab only, then erased", so printed passes become unverifiable once the tab closes.
   - Also say that the file holds guest emails, dietary needs and rooms.
3. **One too-long line breaks the batch (checks 1, 3, 16; R-03).**
   - All previews vanish, the counter is unchanged and Generate stays enabled.
   - By code, `logUsageNow` runs before the build, so "Generation failed" still costs a use (confirm in re-run E).
   - Name the bad line, and charge only on success.
4. **Name mode drops named rows that share a URL (check 1; R-04).** "Table 1/Table 2 → same menu" gives one file. Dedupe by name+value, or ask the user. Warn on "Name," with an empty value.

## P2: later

5. **Guest passes dead end (check 3; R-05).** "(0)" with no hint that guests come from Event Suite's Guest Manager or a project file.
6. **Cap dialog copy (check 5).** It promises to remove a mark that this tool's trial PNGs don't have.
7. **Competitive gaps (check 2):**
   - CSV/XLSX upload with column pick
   - label-sheet PDF
   - a quiet-zone option
   - non-ASCII file names
8. **SEO / locales / a11y (checks 8, 4):**
   - Offer billing period
   - English title and H1 in 9 locales
   - iPhone SE overflow
   - axe button-name ×3
