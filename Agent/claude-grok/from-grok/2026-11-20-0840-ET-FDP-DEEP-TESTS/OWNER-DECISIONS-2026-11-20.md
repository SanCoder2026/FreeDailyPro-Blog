Sent: 2026-11-20 22:25 ET

# Owner decisions on trial counting (Santosh, Nov 20 2026, 10:23 PM ET)

These answer the trial-count policy questions raised in the deep tests. They are Santosh's own decisions.

## 1. Barcode Generator (FDP-25): every Download uses a trial

**Why:** today, one trial use per page visit unlocks every later download in that visit, including ZIPs of up to 200 barcodes, and only a reload charges again. That gives away the paid value of the tool.

**Outcome we want:** each Download (single image, PDF or ZIP batch) uses one trial use. When trials run out, the user sees the normal day-pass and monthly options, never a broken or blank state. The counter on screen must match what is actually charged.

**Same pattern in Invoice Generator (FDP-26):** one trial use unlocks every later download in that visit, each with a new invoice number. Apply the same rule there: each download uses a trial. Keep the separate P1 fix that all formats of one invoice share one invoice number. (Santosh: correct this line if Invoice should differ.)

## 2. Unit Converter (FDP-12), Grammar Checker (FDP-13) and Word Counter (FDP-15): keep uncounted

These intentionally use no trial uses. Do not add trial counting. Treat the "no trial counted" findings in those three reports as working as intended, not bugs.

Please look at the code before changing anything, and push back if there is a better way to reach this outcome.
