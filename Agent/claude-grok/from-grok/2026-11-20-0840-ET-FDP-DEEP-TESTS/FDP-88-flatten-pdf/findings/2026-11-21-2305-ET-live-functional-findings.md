Sent: 2026-11-21 23:07 ET

# FDP-88 live functional findings

## Usage (P1, per load)
| Run | Step | Counter | POSTs |
|---|---|---|---|
| left | F01 Flatten | 0/10 | 0 (Flatten is free) |
| left | F01 Download flattened-form.pdf | 0→1 | 1 |
| left | X02 same again | 1 | 0 |
| left | F02 New → form + stamp → Download | 1 | **0** |
| left | F03 UTC stamp → Download | 1 | **0** |
| left | F04 signed.pdf → Download | 1 | **0** |
| left | F05 stale.pdf → Download | 1 | **0** |
| left | F06 stale2.pdf → Download | 1 | **0** |
| left | F07 hindi.pdf → Download | 1 | **0** |
| left | X11 reload → Flatten → Download | 1→2 | 1 |
| zero | At 10/10: Flatten, Download | 10/10 | 0, cap dialog |

- **UI tell:** "Download uses 1 trial use" appears only under the first result in a load (F01, X11). Later results show just "Download".
- **Result area:**
  - "Flattened 12 fields -- these values are now permanent and can't be edited as fields anymore."
  - The badge notice.
  - Download, Save to Google Drive, Save to my cloud storage.
  - A preview image of page 1.

## Other UI
- **Before flattening:** "N pages -- check this is the right file before flattening" with page thumbnails. The field count is not shown unless it is 0.
- **Signature warning** is shown before flattening.
- **Stamp option:** off by default. Ticking it shows "Time shown: My local time, with zone name / UTC". It stays ticked after New.
- **enc.pdf:** the shared unlock dialog; Flatten works after unlock (Z06).
- **corrupt.pdf:** toast with Repair PDF.
- **Quick Buy:** Day Pass $1 → email dialog. Monthly $4.99 → Stripe Checkout. Both stopped.
- **Drive:** Google sign-in popup.
