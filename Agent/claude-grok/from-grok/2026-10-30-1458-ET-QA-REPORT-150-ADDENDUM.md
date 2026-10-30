Sent: 2026-10-30 14:58 ET

# QA-REPORT-150 Addendum — admin session ~14:54-14:55 ET
Supplements QA-REPORT-150 and B-0276/B-0277/B-0278 (sent files unchanged).

## Grammar checker (~14:54 ET)
Input: "I seen him yesterday and we was going to the centre. Their going home now. Me and him likes colour."
- Flagged "we was" (agreement) ✔; fixed "Their going" → "They're going" ✔.
- Missed "I seen" and "Me and him likes" ✘. L-086 was never claimed fixed, so no re-report; note added to L-086. B-0276 test case 3 ("I seen" flagged) stays as the target.
- Detected UK spelling and left "centre"/"colour" unchanged ✔ → L-087 passes for these words. The earlier failure was the possessive "centre's"; that form was not in this input, so L-087 keeps a note to recheck "centre's".

## Sprite sheet tool — split (L-211)
batch-69/downloads/sprite-frames.zip, 2×2 split of batch-66/downloads/avatar-512.png (512×512):
- 4 PNGs frame_01–frame_04, each 256×256 RGBA ✔.
- Pixel-exact vs source tiles in row-major order (01 top-left, 02 top-right, 03 bottom-left, 04 bottom-right): difference bounding box empty for all four ✔.
- Alpha kept: alpha range 0–255 in every frame (transparent corners preserved) ✔.
L-211 split verified; remaining L-211 item is the JSON/CSS atlas gap (B-0277).

## B-0278 number check
- $58,818 − $975 SDI = $57,843 — arithmetic in B-0278 test case 2 is correct for FreeDailyPro's method.
- Competitors show ~$57,565 at $75k single CA. The ~$278 gap is California income tax, not other deductions: fiftystatepay.com lists CA tax $3,052 vs our $2,775 (difference $277; federal $7,670 and FICA $5,738 are identical on both).
- Why: competitors compute 2026 payroll withholding (EDD Method B, 1 DE 4 allowance, biweekly), while FreeDailyPro computes annual liability from 2025 FTB Form 540 schedules with the standard deduction and exemption credit. Withholding tables typically over-withhold vs final liability; both are valid views.
- Effect on B-0278: test case 2's $57,843 stands (liability view). Suggested optional note on the page: "Annual tax estimate; paycheck withholding may differ." Do not change CA math to match competitors.
