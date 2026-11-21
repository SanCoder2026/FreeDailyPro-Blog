Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: live functional findings

Run: 2026-11-20 22:40–22:57 EST (box `date`). Guest, fresh Chromium contexts from the box IP. No sign-in, no payment, no email or card typed. Counters (strip and `fdp-usage-v1`) are display-only evidence; no backend claims.

## 1. Calculation cases (`live/cases.json`, 45 cases, 22:42–22:44 EST, script `bmi-live.js`)

Reading results only. The context loaded at "0 remaining" (`usageToday` 10) and every result still rendered: reading is never gated.

| Case | Input | Shown | Check |
|---|---|---|---|
| B01 | 70 kg, 170 cm | 24.2 Normal; range 53.5–72.0 kg; Prime 0.97; Ponderal 14.2; WHO Normal range | PASS (70/2.89 = 24.22) |
| B02 | 50 kg | 17.3 Underweight; "gain about 3.5 kg"; WHO Mild thinness | PASS |
| B03 | 90 kg | 31.1 Obese; "lose about 18.0 kg"; WHO Obese class I | PASS |
| B04 | 72.25 kg | 25.0 Overweight; lose 0.3 kg | PASS (exact 25.0) |
| **B05** | 72.2 kg | **25.0 Overweight**, "lose about 0.2 kg" | Exact BMI 24.98 is Normal under WHO (< 25). The tool classifies the rounded value (P2) |
| **B06** | 53.4 kg | **18.5 Normal**, with "Healthy range: 53.5 kg to 72.0 kg" on the same card | Exact 18.48 is Underweight. The weight sits below the range shown, but the label says Normal (P2) |
| **B07** | 70 kg + Asian | "Overweight (Asian cut-offs)", range to 66.2 kg, "lose about 3.8 kg". **Target weight under it: "A BMI of 24.9 at your height is 72.0 kg, which is gain 2.0 kg."** WHO table: Normal range | **Contradictory advice on one screen (P1).** The table difference is disclosed |
| B08 | 65 kg + Asian | 22.5 Normal (Asian); target "gain 7.0 kg" | Same target issue |
| B09 | 80 kg + Asian | 27.7 Obese (Asian); "lose 13.8 kg" vs target "lose 8.0 kg" | Two different "lose" figures (P1) |
| B10 / B36 | age 15 (± female) | BMI 24.2 shown, category hidden, CDC note | PASS. The note names "the CDC child BMI percentile tool" but gives no link (P2) |
| B11 | age 1 | "BMI is not used for children under 2…" | PASS |
| B12–B14 | age 25.5 / 130 / abc | "Enter a whole age between 0 and 120…". Category still shown; extras (Prime, WHO, target, steps, exports) silently disappear | P2 |
| B15 | height 1.7 | "That looks like metres. Enter your height in centimetres (for example 170)." | PASS |
| B16–B19, B22 | 99 / 251 cm, 29 / 301 / −5 kg | Range messages, no result | PASS |
| B20, B21 | "abc", empty | "Numbers only, please." / "Enter your weight." | PASS |
| B23 | "70,5" | 24.4 (comma decimal accepted) | PASS (good for de/fr/es users) |
| B24 | "1,000" | read as 1000 → range error | PASS |
| B25–B27 | waist 85 / 60 / 110 cm | WHtR 0.50 "At or above…", 0.35 "Below 0.4…", 0.65 "0.6 or more…" | PASS |
| B28 | waist 5 | "Enter a **length** between 10 and 250 cm." | P2 wording ("waist") |
| B29 | target 22 | 63.6 kg, "which is lose 6.4 kg" | Number PASS; grammar "which is lose/gain" (P2) |
| B30 | target type Prime (1) | 72.2 kg (BMI 25.0) | PASS |
| B31 | target 5 | "Enter a target BMI between 10 and 60." | PASS |
| B32 | target "abc" | **no message, no result** | P2 (silent) |
| B33 | 300 kg / 100 cm | 300.0, Obese class III; gauge pinned at the right edge (`case-extreme-300.png`) | PASS (in range by design) |
| B34 | 30 kg / 250 cm | 4.8, Severe thinness | PASS |
| B35 | sex female, adult | "Sex does not change adult BMI categories; it is only used for child percentile charts." | The tool has no child percentile chart, so the field does nothing (P2) |
| I01 | 154 lb, 5 ft 7 in | 24.1 Normal; 118–159 lb | PASS (69.85 kg / 1.7018² = 24.12) |
| I02 | 200 lb, 6 ft 0 in | 27.1 Overweight; lose 16 lb; 136–184 lb | PASS |
| I03 / I04 | 5 ft 12 in / ft empty + 67 in | "Inches must be between 0 and 11.9. Put whole feet in the feet box." | PASS / acceptable |
| I05 | 50 lb | "Enter a weight between 66 and 661 lb." | PASS |
| I06 | waist 34 in | WHtR 0.51 | PASS |
| I07 | 5.5 ft, 0 in | 24.9 Normal; target "which is **gain 0 lb**" | P2 (0.05 kg difference shown as "gain 0 lb") |

The URL mirrors the inputs (`?kg=…&cm=…&u=imperial`). Age, sex, waist and the Asian option are not kept. See Privacy below.

## 2. Trial uses (`live/gate.json`, 22:45–22:46 EST, script `bmi-gate.js`)

6 fresh contexts: #0 loaded at 0 remaining, #1–#4 at 0 (skipped), #5 at 10 remaining.

| Context | Actions in order | Count | Dialog |
|---|---|---|---|
| #0, **at 0 remaining** (`allowed:false`, `usageToday` 10) | Download CSV, Copy result (export bar), Print or save as PDF, Copy result (result card), Save as text, Print | 10 → 10 | **None.** All six exports worked: CSV and .txt downloaded, clipboard filled, print called |
| #5, 10 remaining | same six | **0 → 0**, still 0 after reload | None |

**Result: the BMI Calculator takes no trial uses for any action, and nothing is gated at the cap.** There is no trial strip, pass button or Quick Buy anywhere on the page (`live/misc.json` `trialMentions` is empty apart from the footer). The site bundle tags this tool `absorbable` (site-map/DUPLICATES.md, C29), like grammar-checker, which is uncounted on purpose. The owner's Nov 20 decision names only Unit Converter, Grammar Checker and Word Counter as intentionally uncounted, so this is a **policy question for Santosh** (not PASS). The blog says the opposite: "copying, saving or printing uses one trial use per visit."

## 3. Export content

- **Copy result (export bar):** "BMI calculation / BMI 25.9, Prime 1.04, Ponderal Index 14.5, Pre-obese (overweight)", the 5 worked steps, the WHO class list with "<- you", and "Calculated with FreeDailyPro.com". It does not include the weight, height or date.
- **Copy result (result card) = Save as text** (`bmi-calculator-result.txt`): "Your BMI 25.9 Overweight", the **gauge's screen-reader sentence** ("BMI gauge from 15 to 40…"), the healthy range, "lose about 3.1 kg" and "Calculated with FreeDailyPro.com". It does not include the inputs or date. Two "Copy result" buttons copy different texts (P2).
- **Download CSV** (`bmi-who-classes.csv`, UTF-8 BOM, formula guard in code): only the 8-row WHO table with "Your class = yes". **No BMI value, weight, height or date** (P2: low value).
- **Print or save as PDF / Print** (`live/print-preview.pdf`, `printprev-1.png`; Chromium print media, A4): prints **only** the extras block (Prime, Ponderal, WHO table, Target weight with its input boxes, the collapsed "Formula and worked example" summary, and "Recent calculations" with its Clear button). **The BMI value, category, gauge, healthy range, inputs and date are not printed.** (P1)

## 4. Share, favourites, storage (`live/share.json`)

- "Share this tool" → toast "Link copied to clipboard" with `…/tool/bmi-calculator?kg=82&cm=178` (works at 0 remaining). Opening that link reproduces 25.9. Age and the Asian option are dropped, so the recipient sees "Overweight" without "(Asian cut-offs)".
- "Add to favorites" → `freedailypro-favorites` in localStorage (local only; no sign-in prompt).
- Recent calculations: in memory only, up to 10 rows, Clear works; localStorage holds no numbers. The claim "Nothing is saved on our servers or in your browser" is true for storage, but see Privacy.

## 5. Privacy (`live/privacy.json`, 22:56–22:57 EST, script `bmi-privacy.js`)

The page says: "They are not stored, tied to an account or sent anywhere" (Details › Privacy) and "never stored or uploaded" (FAQ). Live:

- After typing 87.3 kg / 179.5 cm and scrolling (no reload), a Google Analytics `POST analytics.google.com/g/collect` carried `page_location=…/tool/bmi-calculator?kg=87.3&cm=179.5`.
- On reload, or when opening a shared link: `GET www.freedailypro.com/tool/bmi-calculator?kg=87.3&cm=179.5` (server), 4 × `googleads.g.doubleclick.net/pagead/ads` with the URL, `pagead2.googlesyndication.com/pagead/ping` body with the URL, and 3 more GA collects.

So weight and height (health data) reach the server logs, Google Analytics and the ad network. **This contradicts the privacy copy (P0).** The ads were only observed, never clicked.

## 6. Keyboard and accessibility

- The tab order is logical: units, weight, height, age, sex, waist, Asian checkbox, the WHO table (scrollable region, focusable), target, the steps summary, then the six export buttons.
- axe (matrix): heading-order (h3 inside the result before any h2), label-content-name-mismatch (`.right-2`, serious), region; on Pixel 7, colour contrast of the ad label text. The video thumbnail `img` has no alt.
