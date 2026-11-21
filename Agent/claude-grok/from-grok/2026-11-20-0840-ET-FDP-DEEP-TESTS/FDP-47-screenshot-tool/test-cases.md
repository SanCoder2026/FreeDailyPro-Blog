Sent: 2026-11-21 06:49 ET

# FDP-47 Screenshot Capture & Editor: test cases (rerun after fixes)

Guest, fresh profile. "Now" is what we saw on 2026-11-21 (stub screen in headless runs; see README).

| ID | Case | Expected | Now |
|---|---|---|---|
| SC-01 | Capture (delay None) | Cropping view with the image; no charge | PASS (0 used) |
| SC-02 | First Download | +1; badge | PASS (+1 in clean checks) |
| SC-03 | Same load: crop Download, Copy, editor PNG/JPG, stitched page, new capture | +1 each; dialog at the cap | **P1 FAIL** (no charge, no dialog) |
| SC-04 | Reload at the cap: Download / Copy / editor Download | Cap dialog | PASS |
| SC-05 | Day Pass / Quick Buy | Email prompt / Stripe (stop) | PASS |
| SC-06 | Drag selection → Download / Copy / Crop | Exactly the selection | PASS (590×109 all three) |
| SC-07 | Editor: pencil, highlighter, arrow, box, text (Hindi/Arabic/CJK), pixelate, rotate, undo | All render; undo after rotate | PASS; highlighter dots, undo cleared on rotate (P3) |
| SC-08 | Pixelate a name | Unreadable | PASS |
| SC-09 | Whole page: scroll a 3,120 px page | Correct stitched image + note | PASS (11 frames, rows 0–51 in order) |
| SC-10 | Whole page without scrolling | Plain screenshot + note | PASS |
| SC-11 | Delay 5s, stop sharing during countdown | Back to start with an error | PASS (back to start; toast not captured) |
| SC-12 | Picker denied / unsupported | Clear toast | PASS |
| SC-13 | Android (no getDisplayMedia) | Upfront note before capture or pass offer | **P1 FAIL** (toast only after tap) |
| SC-14 | Firefox | Same as Chromium | PASS (subset-firefox.json) |
| SC-15 | WebKit | Same as Chromium | Untested in headless (stub not accepted; denied-path toast correct). Test Safari by hand |
| SC-16 | Privacy | No image data in requests | PASS |
| SC-17 | Copy vs Download badge | Owner decision | Copy unbadged (owner Q) |
