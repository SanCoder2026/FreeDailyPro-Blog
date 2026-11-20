Sent: 2026-11-20 08:40 ET

# FDP-01 Roman Numeral Converter: priorities

- **Written:** 2026-11-19 09:46:50 EST (box `date`, ET).
- **Ordering:** by user and revenue outcome. Each item links to its check number in REPORT.md and its repro ID in REPRODUCE.md.

## P0: ship first

1. **Make the trial meter real on this tool (checks 5, 16; R-01).**
   - **Outcome:** a guest sees "Trial: 10 uses/day · N remaining today" with the $1 / $4.99 options. The first Copy or export of a visit spends one trial use, as the FAQ already promises, and reloads keep the display and storage in agreement.
   - **Why:** today the highest-demand tool is effectively unlimited, with no upgrade nudge.
2. **Fix US-order date entry (checks 1, 3, 6, 11; R-02).**
   - **Outcome:** in Month.Day.Year mode, the user types the month first and gets a correct date. 11/19/2026 gives XI.XIX.MMXXVI, and 7/4/1776 gives VII.IV.MDCCLXXVI, matching the FAQ.
   - **Why:** today US users get an error or a silently wrong date. That is the opposite of "wow" for wedding and tattoo dates.
3. **Stop advertising untranslated pages through hreflang (check 8; R-03).**
   - **Outcome:** each hreflang target serves a translated title, meta, H1, UI, H2s and FAQ, or it is removed from the cluster until it does.
   - **Why:** 8 language pages are duplicates of the English page.

## P1: next

4. **Rewrite the blog post** so it matches the live tool: 3,999,999 with bars, date validation, separators and US order (check 9; R-04).
5. **Re-record or re-edit the video**, then retitle it and rewrite its description. Use trial uses wording, not "free". Show dates, bars, working and the charts. Sync the YouTube title with the JSON-LD and sitemap titles (checks 10, 12; R-05).
6. **Fix the 320px header overflow** so iPhone SE and Galaxy S9+ get no sideways scroll (check 4; R-06).
7. **Tablet touch comfort:** copy buttons and title icons at least 44px, and inputs at least 16px at sm and up, so iPad gets no zoom-on-focus (checks 3, 4; R-07, R-08).
8. **Correct the date copy:** the "4 July 1776" H2 sentence should label both orders (check 6; R-09).
9. **Make Copy table paste a clean table** without the "Working for…" block (check 15; R-10).

## P2: enhancements and polish

10. **Share with the value:** `?n=1994` or `?r=MCMXCIV`, with a prefilled page and a share toast. This is the viral loop for tattoo and wedding dates (check 14; R-11).
11. **Date order by locale:** en-US defaults to M.D.Y, and add a Year.Month.Day option for ja, zh, ko and ISO (R-12). Use locale number grouping on translated pages (R-13).
12. **Better related links:** Number to Words and Add Page Numbers (Roman page numbers) instead of Unit, Currency and Time Zone converters. Mention the 1–3,999,999 range in the meta. Add a tool-specific OG image and the video-thumbnail alt. Give the JSON-LD Offer a billing period (check 8).
13. **Guide the user in the Number box:** when it gets letters, hint "Looks like a Roman numeral, use the box on the right" (check 3).
14. **iPhone SE fold:** shorten the H1 or badges on narrow screens so the first result is visible without scrolling (R-14).
15. **Smaller fixes:**
    - Feedback FAB covering chart cells on iPad (R-15).
    - WebKit select and radio contrast in dark mode; verify on real Safari (R-16).
    - The 2 desktop axe violations (R-17).
    - Guard `adsbygoogle.push` so it only runs when the reserved slot exists (`no_div`, R-18).
16. **Consent:** verify from a real EU IP that personalised ad requests wait for consent. Not testable from the US box.
