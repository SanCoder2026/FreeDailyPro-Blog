Sent: 2026-11-21 15:35 ET

# Live functional findings (FDP-69)

- P1: Split into Frames ungated; tiles byte-identical to ZIP entries and saveable at 0 (zero.json Z05–Z06, ctx.json, left-b L10).
- P1: one charge per page load; new Generate and split ZIP free after it, even at 2/2 (left-b.json).
- Outputs exact (sheet, padded/extruded sheet, JSON atlas, split frames). Gate on a fresh page at the cap works for Generate and ZIP.
- P2: silent split on non-image; "Use more columns" advice. P3: invalid grid → 1×1.
