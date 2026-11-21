Sent: 2026-11-21 06:49 ET

# FDP-47: live functional findings (2026-11-21 EST)

**Method:** stubbed `getDisplayMedia` (test browser only) because headless browsers here can't open a real picker (st-probe*.js: NotSupported / NotReadable with every flag tried, also under Xvfb).

## One page load (main.json, 06:28–06:30 EST)
- Start 0/2 ("2 remaining today"). Keyboard reaches Take Screenshot (32 Tabs).
- C01 capture → cropping view, 1280×720, no charge.
- C02 Download → 1280×720 PNG with two badges; counter 0→2 (see the counter note).
- C03–C09 in the same load, all without a dialog: Download (C03, same image because my first drag missed the off-screen image; selection verified separately), Copy (1280×720 PNG in the clipboard), editor PNG (64,736 B) and JPG, rotate (720×1280), whole page (11 frames → 1,280×3,120, note shown), blank whole page ("Only one frame was captured…"), 5 s countdown with sharing stopped (back to start), new capture + Download. **P1.**
- After a reload at 2/2: Download, Copy and the editor Download all open the cap dialog ("Today's trial uses are done… Monthly $9.99 / Day Pass $3 … removes the 'Created with FreeDailyPro.com' mark"). Day Pass → email prompt (stopped). Quick Buy monthly → Stripe Checkout (stopped).

## One action per fresh context (check-3kinds-console.txt, check-copy.json)
- Download, Copy and editor Download each: one `usage.log` POST, counter 0→1. A second Copy run went 0→2 with one POST (display sync, P3).
- Selection 412×76 css px → 590×109 px in the file, the clipboard and the editor canvas.

## Outputs
- Badge: two "Created with FreeDailyPro.com" badges (top right, bottom right) on every download; Copy has none.
- Pixelate made "Jane Doe 555-0134" unreadable; text tool shaped Devanagari, Arabic and CJK correctly.
- Highlighter overlap dots; rotate clears undo.
- Stitched page: rows 0–51 in order, no duplicates or gaps.

## Mobile (mobile.json)
- With `getDisplayMedia` removed (as on Android): delay buttons and Take Screenshot shown, toast "Screen capture isn't supported in this browser" after the tap; no upfront note.

## Real picker / other engines
- Real `getDisplayMedia` in headless Chromium, Firefox, WebKit → toast "Screenshot wasn't taken (permission denied or cancelled)".
- Firefox subset: capture, editor (Copy to Clipboard present), stitching (12 frames → 1,280×3,120) same as Chromium; Download at 2/2 → cap dialog.
- WebKit: the stub wasn't accepted, so only the error path was seen (S01-webkit.png). Test Safari by hand.
- **Privacy:** no request carried image data or large bodies (net.hits empty).
