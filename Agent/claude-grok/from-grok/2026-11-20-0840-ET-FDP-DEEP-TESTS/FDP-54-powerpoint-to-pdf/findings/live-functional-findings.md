Sent: 2026-11-21 10:12 ET

# Live functional findings (2026-11-21 EST, guest)

## At the cap (probe*.json, 10/10, Chromium/Firefox/WebKit)
- **Accept list:** .pptx,.ppt,.pps,.pot,.ppsx,.potx,.pptm,.odp,.otp,.key.
- **Bad files:** "This is not a .pptx file. It may be damaged, or another kind of file renamed to .pptx." A .txt gets the toast "can't be used here … takes .pptx, .ppt, .odp or .key files".
- **.ppt / .odp:** POST presentation.convert (955 KB / 335 KB JSON) → preview "8 slides (1 hidden)". This happens at 10/10, before the gate.
- **.ppsx:** POST, then the alert "already PowerPoint (.pptx). Pick a different format to convert to."
- **Convert at 10/10:** cap dialog "You've used today's 10 trial uses. Monthly for $4.99 … Day Pass for $1 … removes the 'Created with FreeDailyPro.com' mark".
- **Quick Buy:** Day → email dialog (stopped). Monthly → Stripe Checkout (stopped).

## With uses left
- **left.json:**
  - L01 rich: 0→1 at Convert, one usage.log POST. Downloads don't charge (twice).
  - L02 4:3 in the same load: no change.
  - Reload → L03 picture-only: 1→2. "no text found to make searchable".
- **cases.json (one load, 1 use):**
  - K01: 7 pages, 893 KB.
  - K02 Sharp + hidden: 8 pages, 1.37 MB, 2560 px.
  - K03 Fast, no text layer: 307 KB, 1280 px.
  - K04: 4:3, 720×540.
  - K05: 60 slides, 8.56 MB, 6.3 s.
  - K06 .ppt / K07 .odp: server path, 7 pages.
  - K08 .ppsx: refused.
  - Note: "Make the text searchable" stays as last set for the next file (K04–K07 ran without it); "Include hidden" resets, as the FAQ says.
- **cases-r2.json (new load, 1 use):** K05 with the text layer took ~51 s. K06 and K07 with the text layer: "searchable text added".

## Output checks
- Page sizes are exact. JPEG pages at 1280/1920/2560 px.
- Fonts: FreeSans and DejaVuSans subsets for the text layer.
- Hyperlink annotation kept (example.org). Badge link on every page.
- No speaker-note text. The hidden slide appears only with the option on.
- Hindi is garbled in the text layer; Japanese and Arabic are absent from it (as stated).
- Visual: charts, table, gradient and full-bleed picture are faithful. Kana use a different fallback font. The .ppt output has a pale link colour and the caption moves to the centre.

## Other
- **drive.json:** Open from Google Drive → accounts.google.com sign-in popup (closed). 7 Tabs to the drop zone.
- **ext.json:** .pptm, .potx, .pps and .key copies (renamed .pptx) are uploaded and get the same "already PowerPoint" refusal.
