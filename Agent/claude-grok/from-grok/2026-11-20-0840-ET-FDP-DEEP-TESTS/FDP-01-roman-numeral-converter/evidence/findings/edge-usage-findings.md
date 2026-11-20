Sent: 2026-11-20 08:40 ET

# Roman Numeral Converter: edge inputs, usage counting, downloads (Step A)

- **Written:** 2026-11-19 09:44:26 EST (box `date`, ET).
- **Runs:**
  - `edge-usage.js`: 09:40:43 to 09:42:28 EST.
  - `edge-date-vinculum-probe.js`: about 09:43 to 09:45 EST.
  - `edge-copy-table-probe.js`: about 09:46 EST.
  - All runs used headless Chromium 159, desktop 1366×900, a fresh guest context each time, and no sign-in.
  - `window.print` was stubbed. No ads, pass or checkout buttons were clicked.
- **Raw:** `edge/edge-usage-results.json`, `edge/copy-table-clipboard.json`, the downloaded CSVs and the screenshots in `edge/`.
- **Counters** (trial strip text and localStorage `fdp-usage-v1`) are display-only evidence. No backend claim is made.

## 1. Edge inputs (verbatim)

### Number → Roman Numeral box

| Input | Output / message shown |
|---|---|
| `1` | I |
| `3999` | MMMCMXCIX |
| `4000` | I̅V̅. The result renders as `<span class="overline">I</span><span class="overline">V</span>` (CSS overline), and the note reads "A bar over a letter multiplies it by 1,000: I̅V̅." See `edge/result-4000.png`. |
| `3999999` | M̅M̅M̅C̅M̅X̅C̅I̅X̅CMXCIX (barred via CSS), with the note "A bar over a letter multiplies it by 1,000: M̅M̅M̅ + C̅M̅ + X̅C̅ + I̅X̅ + CM + XC + IX." See `edge/result-3999999.png`. |
| `4000000` | "Roman numerals here go from 1 to 3,999,999: above 3,999 a bar over the letters multiplies by 1,000, and three barred M's is the limit." |
| `0` | "Roman numerals start at 1. There is no symbol for zero and no negative numbers." |
| `-5` | Same message as `0`. |
| `12.5` | "Roman numerals have no decimals. Use a whole number." |
| *(empty)* | "—" (no error) |
| `mmxxvi`, `IIII`, `VX`, `MMMM`, ` XIV `, `ABC` | "Enter a whole number from 1 to 3,999,999." There is no hint to use the Roman → Number box instead (UX, LOW). |

### Roman Numeral → Number box

| Input | Output / message shown |
|---|---|
| `1`, `3999`, `4000`, `3999999`, `4000000`, `0`, `-5`, `12.5`, `ABC` | "Use only the letters I, V, X, L, C, D and M." |
| *(empty)* | "—" |
| `mmxxvi` | 2026 (lowercase accepted) |
| `IIII` | 4, with "IIII is the clock-face way of writing 4 (the standard form is IV)." |
| `VX` | "Not a valid Roman numeral. VX is not allowed: only I before V or X, X before L or C, and C before D or M can be subtracted (99 is XCIX, not IC). Did you mean V (5)? Plain letters go up to MMMCMXCIX (3,999)…" |
| `MMMM` | "Not a valid Roman numeral. Four M in a row would be 4,000; plain letters stop at 3,999, so write thousands above that with a bar. Plain letters go up to MMMCMXCIX (3,999); a bar over a letter multiplies it…" |
| ` XIV ` | 14 (trimmed) |
| `IIX` | "Not a valid Roman numeral. Did you mean X (10)? …" |
| `IC` | "…IC is not allowed… Did you mean XCIX (99)? …" |
| `(V)` | 5000, with "The barred letters are multiplied by 1,000." |
| `(XII)CCCXLV` | 12345, same note |
| `I̅V̅` (U+0305) | 4000, same note |

**Verdict:** PASS. The range, errors and hints are accurate and friendly. The only gap is that the Number box doesn't say "this looks like a Roman numeral, use the box on the right".

### Date mode

The three boxes have aria-labels **Day, Month, Year** in that DOM and visual order (x = 235, 323, 411) in **both** order modes. They have no visible labels or placeholders. inputmode is numeric.

| Case | Heading | Result / error |
|---|---|---|
| Day.Month.Year, 31 / 02 / 2026 | "Date → Roman numerals (day, month, year)" | "—" and "That date does not exist in the calendar." PASS |
| D.M.Y, 29 / 02 / 2024 (leap) | same | XXIX.II.MMXXIV. PASS |
| D.M.Y, 19 / 11 / 2026 | same | XIX.XI.MMXXVI. PASS |
| D.M.Y, year 4000 | same | "Year must be between 1 and 3999." PASS |
| Switch to **Month.Day.Year (US)** with boxes still 19 / 11 / 2026 | changes to "(month, day, year)" | XI.XIX.MMXXVI (output reordered) |
| **US mode: first box 11, second box 19, 2026** (a US user typing Nov 19 in heading order) | "(month, day, year)" | **"—" and "Month must be between 1 and 12."** **BUG CONFIRMED** (`edge/us-order-11-19-error.png`) |
| US mode: 7 / 4 / 1776 (the FAQ says "7.4.1776 becomes VII.IV.MDCCLXXVI") | "(month, day, year)" | **IV.VII.MDCCLXXVI**, which contradicts the FAQ |
| US mode: 4 / 7 / 1776 | "(month, day, year)" | VII.IV.MDCCLXXVI |

**Bug (MEDIUM-HIGH):** in US mode the heading promises month, day, year, but the first box is still the Day box. The mode only reorders the output. A US user who types in the order the heading shows gets an error, or a silently wrong date for days ≤ 12 (7/4 becomes April 7). The FAQ example also fails as written.

**Separators** (date 19/11/2026, D.M.Y): dot → `XIX.XI.MMXXVI`; middle dot → `XIX·XI·MMXXVI`; slash → `XIX/XI/MMXXVI`; hyphen → `XIX-XI-MMXXVI`; space → `XIX XI MMXXVI`. All PASS.

## 2. Usage counting (2 fresh contexts)

| Step | Run 1: strip / `usageToday` | Run 2: strip / `usageToday` |
|---|---|---|
| On load, no action | none / 0 (limit 10, tier professional, isPro false) | none / 0 |
| After typing 1994 | none / 0 | none / 0 |
| After **Copy Roman numeral** (clipboard = "MCMXCIV", toast "Copied!") | none / **0** | none / **0** |
| After **Download CSV** (1 to 100) | none / **0** | none / **0** |
| After **Print or save as PDF** (`window.print` called once; no new window) | none / **0** | none / **0** |
| After Download CSV (Years tab) | n/a | none / **0** |
| After **Copy table** | n/a | none / **0** |
| After reload | none / 0. Values reset to 2026 / MMXXVI | none / 0 |

- In run 2, five exports in one visit left `usageToday` at 0, and the trial strip ("Trial: 10 uses/day · N remaining today") **never rendered** in either context.
- **No action is counted** on this tool by any display evidence.
- This contradicts both the owner policy (copy and results count) and the page's own FAQ text: "copying or downloading it uses one of your trial uses for the visit."
- It also matches the desktop tester's run (usageToday 0 after Copy, CSV, Print and reload).
- The desk JS read suggested Copy should go 10 → 9. It did not.
- Effect: the tool currently behaves as unlimited for guests, and there is no visible upgrade nudge. Severity **HIGH** (monetization and policy). Whether the backend counts anything is not claimed.

## 3. Downloads, copy, share, FAQ, links, video

- **Download CSV, 1 to 100:** `roman-numerals-1-100.csv`, 918 bytes.
  - It has a UTF-8 BOM, a header `Number,Roman numeral`, and 100 rows (`1,I` … `100,C`). PASS.
- **Download CSV, Years tab:** `roman-numerals-years.csv`, with a header and 101 rows (`1950,MCML` … `2050,MML`). PASS.
- **Copy table:** the clipboard holds the table title, then an **unrelated "Working for 2,026" step-by-step block**, then the tab-separated table (1,228 and 1,704 characters).
  - The working block pollutes a pasted table. **Bug, LOW** (`edge/copy-table-clipboard.json`).
- **Copy Roman numeral:** the clipboard gets exactly "MCMXCIV", with a "Copied!" toast. PASS.
- **Print or save as PDF:** calls `window.print()` once. Output layout was not inspected here; the native dialog was stubbed.
- **Share this tool** (in-page button, `navigator.share` unavailable): copies `https://www.freedailypro.com/tool/roman-numeral-converter` to the clipboard, and no dialog opens.
  - The link carries no value or state, so a friend can't open your conversion.
  - Share did not change `usageToday`.
- **Storage:** "Recent calculations" shows entries such as "3,999,999 = M̅M̅M̅C̅M̅X̅C̅I̅X̅CMXCIX" and "2,026 = MMXXVI".
  - It carries a **Clear** button and the note "Kept only while this page is open. Nothing is saved on our servers or in your browser."
  - After a reload, inputs reset to the defaults (2026, MMXXVI, today's date). This works as designed: session-only.
- **FAQ (11 questions, visible, and the same in JSON-LD):**
  - How do I convert a number to Roman numerals?
  - How do I convert Roman numerals back to numbers?
  - How do I write a date or year in Roman numerals?
  - How do I write numbers above 3,999 in Roman numerals?
  - How do I see the working for a Roman numeral?
  - What do I, V, X, L, C, D and M stand for?
  - How do you write 2026 in Roman numerals?
  - How do you write 4 in Roman numerals?
  - What is the largest Roman numeral?
  - Is there a zero in Roman numerals?
  - Is what I type sent anywhere?
- **"Guides and next steps" links:**
  - Watch on YouTube (`watch?v=Jrmgcqn_jJw`)
  - Subscribe for new tutorials
  - Blog "Roman Numerals for Chapters, Copyright Years and Old Dates" → `/blog/roman-numeral-converter`: **HTTP 200**
  - Blog "Convert Binary and ASCII for Homework and Debug Checks" → **200**
  - Related tools: Unit Converter, Currency Converter, Time Zone Converter (all **200**)
  - The related tools are generic. Number to Words, Age & Date Calculator, or Add Page Numbers (Roman page numbers) would fit Roman-numeral users better.
- **Video embed:** YouTube id **Jrmgcqn_jJw**, found in the thumbnail `i.ytimg.com/vi/…`, `/embed/` and `watch?v=`. The play button label is "Play video: How to Convert Numbers to Roman Numerals Online".

## Scripts (rerunnable)

- `scripts/edge-usage.js [url] [outDir]`: edge inputs, two usage runs, downloads, FAQ, links and share.
- `scripts/edge-date-vinculum-probe.js`: verbatim date-mode errors and the vinculum render.
- `scripts/edge-copy-table-probe.js`: full Copy table clipboard on both tabs.
