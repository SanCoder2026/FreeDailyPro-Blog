Sent: 2026-11-21 13:37 ET

# FDP-63: reproduce

All guest, fresh browser contexts. Times EST. Professional trial uses reset at midnight UTC (7:00 PM ET).

1. **Per-load charging (P1):** fresh context with uses left (`TRIES=40 env -u BROWSER node px63-live.js left`).
   - Upload `quad-800x600.png`, click the red then yellow quadrant. Copy HEX → one `api/trpc/usage.log` POST, `fdp-usage-v1` 0→1.
   - Copy RGB, HSL, CMYK, then a palette swatch: clipboard updates, no POST, count stays 1.
   - "Upload Different Image" → new image → pick → copy: no POST.
   - Reload → upload → pick → copy: POST, count 2.
2. **Values at 0 (owner question):** context at 10/10 (`px63-live.js zero`). Upload and click: all four values show. Each copy → cap dialog, clipboard empty.
3. **Copy contradictions:** expand "Details: when to use it, limits, privacy" and read the Limitations, Tips and Privacy paragraphs against the live magnifier, CMYK panel and palette. Watch the network on upload: no request.
4. **Non-image:** upload `notanimage.png`: blank canvas, no message.
5. **Keyboard:** click (395,100) on the quadrant image, focus the canvas, press → ×10: value turns red.
6. **Drive:** click "Open from Google Drive": Google sign-in popup (stop there).
7. **Quick Buy:** Day → email prompt (stop); Monthly → Stripe (stop).
