Sent: 2026-11-21 08:44 ET

# FDP-51 test cases (guest; run after fixes)

| ID | Input / steps | Expected | Today (2026-11-21) |
|---|---|---|---|
| C01 | P02 16:9 → Picture → Download | +1 use; 4 slides 13.33×7.5 in, one picture each | PASS (L01) |
| C02 | Same load: new file → Download | +1 use | FAIL (stays at 1, L02–L14) |
| C03 | Re-download the same result | no extra use | PASS (L01b) |
| C04 | Reload → 2 new decks | +1 each | FAIL (L20 +1, L21 free) |
| C05 | Fresh context at 10/10 → Download / Get a Day Pass / Save to Google Drive | cap dialog $1/$4.99 | PASS (zero.json) |
| C06 | Day Pass → | email field, stop | PASS (stopped) |
| C07 | Quick Buy monthly | Stripe Checkout, stop | PASS (stopped) |
| C08 | P11 (LibreOffice deck) → Editable | all text editable, bold/italic kept, fonts mapped, background without text | PASS (M01 33/33, 13 boxes) |
| C09 | P11 slide 3 table → Editable | one box per cell (or a table) aligned to the grid | FAIL (row merged) |
| C10 | P12 memo → Editable | 23 items; text black 000000 | PARTIAL (colours 21–2C grey) |
| C11 | P08 Arabic → Editable | Arabic in logical order | FAIL (reversed) |
| C12 | P01/P02 (Type3 text) → Editable | honest "0 editable, N stayed in picture" | PASS |
| C13 | P04 scan → Editable | "1 page had no text … picture only" | PASS |
| C14 | P05 password → u123 | unlocks inline, converts | PASS (L07) |
| C15 | P06 damaged / P10 non-PDF | clear message (non-PDF says "not a PDF") | PASS / P3 wording |
| C16 | P07 60 pages, Picture / Editable | 60 slides; < 5 s | PASS (1.4 s / 2.6 s, 1.8 MB) |
| C17 | P07 Editable → Stop after 0.4 s | returns to options, no charge | PASS (M04) |
| C18 | P09 mixed sizes | slide = page 1 size; page 2 fitted | PASS (documented) |
| C19 | Network during all of the above | no POST carries document bytes | PASS |
| C20 | Firefox / WebKit at 10/10 | conversions work; Download → cap dialog | PASS (subsets) |
| C21 | /category/pdf-tools | lists PDF to PowerPoint | FAIL |
| C22 | Locales /de, /ja … | tool body translated | FAIL (English body) |
| C23 | axe desktop / Pixel 7 | 0 serious | FAIL (label mismatch, ad-label contrast) |
