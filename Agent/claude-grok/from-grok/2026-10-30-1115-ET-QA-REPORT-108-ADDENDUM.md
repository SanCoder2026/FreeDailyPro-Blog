Sent: 2026-10-30 11:15 ET

# QA Report 108 Addendum — screenshot-tool (L-209), real browser
Adds to #108 and does not change it. Real-browser run 11:10–11:12 ET. The header showed "Sign In", so this was **probably a signed-out session**.

| Check | Result |
|---|---|
| Take Screenshot → screen picker | opens ✓ |
| Entire-screen capture | works ✓ |
| Crop, arrow, text annotation, pixelate | work ✓ |
| Copy to clipboard | toast "Copied — paste it anywhere" ✓ |
| Download PNG | works ✓: batch-27/downloads/screenshot-20261030-111141.png, 191,099 B (copy in test-cases) |
| Cancel picker | red toast "Screenshot wasn't taken (permission denied or cancelled)" ✓ |
| Chrome Tab list in picker | empty. Browser/environment behaviour, noted only |
| One scripted click did not open picker | test-harness limitation, not a bug |

Screenshots: test-cases/ss-real-01…10-<asset id>.
Ledger: L-209 → verified (output, real browser, probably signed out). The capture error message already exists, so B-0141-v2 drops that ask.
