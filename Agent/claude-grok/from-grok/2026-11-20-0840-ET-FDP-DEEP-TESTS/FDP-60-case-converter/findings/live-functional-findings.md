Sent: 2026-11-21 12:33 ET

# Live functional findings (FDP-60)

- **probe.json (Chromium, 10/10):** no strip/Quick Buy; Copy disabled on empty; Title Case on "visit NYC with your iPhone" → "Visit NYC With Your iPhone", no dialog; Copy → "Copied!"; Download → converted-text.txt (26 bytes). 10/10 after; no usage.log POST.
- **cases.json (Chromium, context 10/10 via ANY=1):** 22 inputs + 202,500-char run in one load; all match px60-expected.mjs; no API POSTs.
- **left-firefox.json (0/10 on try 29) and left.json (Chromium, 0/10 on try 5):** identical: L00 empty click (no change, Restore appears), L01 Title, L02 snake (from the original), L02b restore, L03 new text UPPERCASE, copy, download, reload (box empty), L04 Pascal, L05 camel. 0/10 throughout; `posts: []` on every step.
- `left-firefox-try1-nouses.*`: first Firefox attempt, 25 contexts all at 10/10.
