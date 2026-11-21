Sent: 2026-11-21 10:59 ET

# Live functional findings (FDP-56)

- **Copy at the cap (Chromium, 10/10):** "Copied!", clipboard = shown password, no dialog, no POST. Same in Firefox. Repeated Copy, Copy of result #3 of 10, Copy while hidden and passphrase Copy all behave the same.
- **No trial strip or prices** on the page (`strip:null`, `quickBuyButtons:0`).
- **Network:** the only tool request was `GET /dict/eff-large-wordlist.txt` (once, on the first passphrase).
- **P07 spaces bug:** the alert "The symbols box is empty, so the default symbols are used." shows next to passwords with spaces (10/10 in both engines); entropy line "63 possible characters".
- **P08:** the symbols box "abc#" gives a 63-char alphabet (letters deduped) and 94.9 bits; the maths stays right.
- **Lock:** with one type left, "(the last one is locked)" shows and its switch is disabled.
- **Mode switch:** switching to Passphrase clears results (0 rows) until Generate.
- **Fresh contexts:** 8 Firefox, 6 WebKit and 6 Chromium tries were all at 10/10 (left*.json), so the with-uses run is pending.
