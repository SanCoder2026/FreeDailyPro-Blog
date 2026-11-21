Sent: 2026-11-20 22:45 ET

# Test cases: Bulk QR Generator (bulk-qr)

- **Tool:** https://www.freedailypro.com/tool/bulk-qr (Professional Tool, 10 trial uses a day).
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 13:01:06 EST (box `date`, ET).
- **Checking codes without downloading:** the preview `<img>` tags (first 12) are data URLs. Save them and decode with zxing-cpp (`scripts/bq-explore.js` does this). Previewing is free.
- **Checking downloads:** `python3 scripts/bq-inspect.py <qr-codes.zip> [project.json] <out.json>`.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the cap dialog / Stripe), no ad clicks.
- **Results:** "Today" is the live result on 2026-11-19, 12:37–13:00 EST. "Currently: FAIL" should pass after the fix. "**Re-run**" needs a context that shows uses remaining (after midnight UTC, 7:00 PM ET), using `scripts/bq-battery.js`.

## A. List mode (preview)

| ID | Input | Expected | Today |
|---|---|---|---|
| BQ-01 | Empty | 0 codes, Generate disabled | PASS |
| BQ-02 | 3 lines (2 URLs + "Hello World") | 3 previews decode exactly | PASS |
| BQ-03 | Duplicates + blank lines | "2 … (2 duplicate lines skipped)" | PASS |
| BQ-04 | "Grüße 日本 👍", Arabic, Cyrillic | exact | PASS |
| BQ-05 | 510 lines | 500 + cap notice + "+488 more" | PASS |
| BQ-06 | One 301-character value | long-value warning; decodes | PASS |
| BQ-07 | One 3,000-character value + one valid line | the bad line is named, the valid preview stays, Generate is blocked or skips the bad line | **Currently: FAIL** (all previews vanish; counter still "2"; Generate enabled) |
| BQ-08 | Code #cccccc | low-contrast warning | PASS (1.6:1) |
| BQ-09 | White on black | inverted warning | PASS |
| BQ-10 | SVG | PNG size disabled | PASS |
| BQ-11 | WiFi/vCard/mailto/formula payload lines | encoded literally | PASS |
| BQ-12 | EC H | preview EC H | PASS |

## B. Name mode

| ID | Input | Expected | Today |
|---|---|---|---|
| BQ-13 | Shop,https://example.com/shop | name Shop, value URL | PASS (preview) |
| BQ-14 | ,https://example.com/nocomma | no name, comma not encoded | PASS |
| BQ-15 | "Table 1,…/menu" and "Table 2,…/menu" | two files (or a clear choice) | **Currently: FAIL** (Table 2 dropped as a duplicate) |
| BQ-16 | "OnlyName," | a warning (empty value) | **Currently: FAIL** (encodes "OnlyName,") |
| BQ-17 | Names with accents or CJK | readable file names | **Re-run** (by code: "Gru-e", "code") |

## C. Guest passes and project

| ID | Action | Expected | Today |
|---|---|---|---|
| BQ-18 | Guest passes with no project | explains where guests come from | **Currently: FAIL** (just "(0)") |
| BQ-19 | Try a sample → passes | 5 confirmed/attended passes, FDP1 format | PASS |
| BQ-20 | Two fresh contexts → sample | different pass keys | PASS |
| BQ-21 | Generate passes ZIP | 1 use; 5 PNGs decode; signatures verify | PASS (D1: 10 → 9, 5/5 valid) |
| BQ-22 | After generating passes | a prompt to save the project (key) | **Currently: FAIL** (no prompt) |
| BQ-23 | Save project at 0 remaining | always allowed (it is the user's own data) | **Currently: FAIL** (cap dialog) |
| BQ-24 | Save project with uses left | free | PASS (D2) |
| BQ-25 | Open broken JSON / text / wrong shape | clear toast | PASS |
| BQ-26 | Note before saving | mentions guest personal data, not only the key | **Currently: FAIL** |

## D. Downloads and trial uses (display-only)

| ID | Action | Expected | Today |
|---|---|---|---|
| BQ-27 | Fresh context starting strip | 10 remaining | **Currently: FAIL** (about 34/36 at 0) |
| BQ-28 | Generate ZIP | costs 1 | PASS (D1) |
| BQ-29 | Generate the same list again; then SVG | the cost is stated | **Re-run** (A) |
| BQ-30 | PNG files: size and quiet zone | chosen size; 4 modules | PASS at 600 (3.99 modules); 2000 **re-run** (B) |
| BQ-31 | Trial PNG mark | none (or disclosed) | PASS (none) |
| BQ-32 | index.csv | BOM, file,name,value, formula guard | PASS (D1); formula rows **re-run** (B) |
| BQ-33 | 500 codes at 300 px | completes; numbering 001–500 | **Re-run** (C) |
| BQ-34 | Batch with one too-long line | no use consumed, or the bad line is skipped | **Re-run** (E). By code a use is logged before "Generation failed". |
| BQ-35 | Cap dialog text | matches this tool | **Currently: FAIL** (promises mark removal; there is no mark) |

## E. Layout, a11y, locales, content

| ID | Check | Expected | Today |
|---|---|---|---|
| BQ-36 | Phone order | list → preview → Generate | PASS |
| BQ-37 | iPhone SE overflow | ≤ 320 | **Currently: FAIL** (329) |
| BQ-38 | axe critical | 0 | **Currently: FAIL** (button-name ×3) |
| BQ-39 | Locales title and H1 | localized | **Currently: FAIL** (English in 9) |
| BQ-40 | Video | current UI | PASS (it omits passes) |
| BQ-41 | Offer JSON-LD | billing period | **Currently: FAIL** |

---

## Updates from the 2026-11-20 re-run (see RERUN-FINDINGS.md)

| ID | 2026-11-20 result |
|---|---|
| BQ-33 | PASS (500 at 300 px, 8.7 s, 2.33 MB, 001–500, 500/500 decode, 4.05 modules, −1) |
| BQ-34 | **Currently: FAIL (display-only):** nothing downloaded, no error shown, counter 0 → 10 |
| BQ-07 | **Currently: FAIL** (unchanged) |
| BQ-29 | Still pending (A loaded at 0 twice) |
| BQ-17, BQ-30 (2000), BQ-32 formula rows | Still pending (B loaded at 0 twice) |
