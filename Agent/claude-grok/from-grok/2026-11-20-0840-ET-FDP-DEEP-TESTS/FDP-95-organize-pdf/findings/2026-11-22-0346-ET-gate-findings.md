Sent: 2026-11-22 03:49 ET

# FDP-95 findings: Premium gate and usage

| Run | Start | Downloads in one load | POSTs | End | Note |
|---|---|---|---|---|---|
| core | 0/2 (13th fresh profile) | 9 (O01–O09) | 1 | 1/2 | **per load (P1)** |
| err | 0/2 (26th) | 2 (300 p, 73.6 MB) | 1 | 2/2 | first download 0→2/2 (pool jump); **heavy delivered at 2/2** with no dialog |
| capload | 2/2 (no 0/2 in 40) | 0 of 3 + 2 reloads | 0 | 2/2 | every Download → "Today's trial uses are done … Monthly for $9.99, or a Day Pass for $3. Either pass also unlocks every Professional Tool and removes the 'Created with FreeDailyPro.com' mark" ✓ |
| capx | 2/2 | 0 | 0 | 2/2 | Save works; **Preview first page shows the result (Q1)**; Save to Google Drive → cap dialog ✓; Save to my cloud storage → "Cloud storage, $4.99 per month, 1 GB … Sign in with your email first" |
| encx | 2/2 | 0 | 0 | 2/2 | unlock + Save OK; cap dialog |
| mobile ×2 | 2/2 | 0 | 0 | 2/2 | cap dialog |

- Strip: "Trial: 2 uses/day · N remaining today". At 0: "Today's trial uses are used up, so downloading was not done. Your input is still here and nothing was lost."
- localStorage `fdp-usage-v1`: `tier: premium`, scope `dev:[REDACTED]:premium`. The Premium count is shared across Premium Applications for this device.
- Quick Buy: Day → "Premium Day Pass, $3" email dialog (stopped); Monthly → Stripe Checkout "Subscribe to Premium Applications - Monthly $9.99" (stopped; Stripe ID redacted).
- Drive (guest): "Open from Google Drive" → accounts.google.com sign-in popup (parameters redacted), closed.
