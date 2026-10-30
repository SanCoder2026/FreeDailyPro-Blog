Sent: 2026-10-30 11:10 ET

# QA Report 107 Addendum — calorie-calculator (L-206), admin session
Adds results to #107 and does not change it. The parent's admin session ran these cases; I re-checked each one by hand with Mifflin-St Jeor.

| Case | Inputs | Site result | Hand check | Verdict |
|---|---|---|---|---|
| A | F, 60, 155 cm, 50 kg, Sedentary | maintain 1209; both loss targets '—' "Not recommended for you"; gain 1709/2209; BMI 20.8; 1200-cal safe-minimum warning shown | 1007.75×1.2=1209 ✓; 50/1.55²=20.8 ✓ | PASS floor check |
| B | F, 30, 165 cm, 60 kg, Moderately active | maintain 2046; moderate loss 1546; aggressive 1535 (cap); both ~1.0 lb/week | 1320.25×1.55=2046 ✓; 25% cap 1534.5→1535 ✓ | math OK; UX: "Aggressive" only 11 cal below moderate → added to B-0138 (v2) |
| C | imperial 5'5", 132 lb | 2045 / 1545 / 1534; BMI 22.0 | 165.1 cm / 59.87 kg → 2045.3 ✓ | OK (unit rounding) |

Screenshots (admin session): test-cases/calorie-case-A-admin.png, -B-, -C-.
Ledger: L-206 → verified (output, admin session). Ledger grep showed no existing row for the aggressive≈moderate issue, so it goes into B-0138-v2 as UX evidence, not a new bug.
