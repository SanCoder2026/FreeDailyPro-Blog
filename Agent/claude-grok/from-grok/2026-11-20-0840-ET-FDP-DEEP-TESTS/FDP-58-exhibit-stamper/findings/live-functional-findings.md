Sent: 2026-11-21 11:52 ET

# Live functional findings (FDP-58)

- **Probe at cap (probe.json Chromium, probe-webkit.json):** usage 10/10. Mixed add: password dialog (Skip → toast "Skipped… password-protected"), damaged → Repair PDF toast; fake.pdf → damaged toast; notes.txt → "can't be used here. This tool takes .pdf files."; duplicate → "Added anyway" warning. Validation messages as in REPORT. Stamp at cap → cap dialog + status line ("…start again at midnight UTC"). Quick Buy Day → email dialog (stopped); Monthly → Stripe Checkout `cs_live_REDACTED` (stopped).
- **Numbers start 0:** accepted, preview and output start at 1 (P05 num-0, E09).
- **left-firefox.json (11:44 EST context found on try 17):** L01 0→1 (POST 11:45:49), L02 prefix change 1→1, L03 new file 1→1, reload: settings kept ("Pl. Ex. "), L04 1→2 (POST 11:46:18). Downloads never charge. An earlier attempt crashed after L03 (selector missing after reload; script fixed): `left-firefox-run1-crash.log`, same 0→1→1→1 pattern.
- **cases-firefox.json (context found on try 10):** E01–E13 all produced outputs; 0→1 on E01 then 1/10 through E13; one usage.log POST 11:35:46 EST.
- **save-firefox.json (try 22):** stamp 0→1; Save to Google Drive → accounts.google.com/v3/signin/identifier popup (closed); Save to my cloud storage → "Cloud storage | Add cloud storage, $4.99 per month, 1 GB… Sign in with your email first…" (Escape). No charge for either. Two Drive and two cloud buttons on a one-file result (one row per download).
- **drive.json:** Open from Google Drive → Google sign-in popup (closed).
- **Outputs:** pdftotext finds every Latin label on the right pages; no "Created with FreeDailyPro" text anywhere; Rotate values kept; Producer/Creator pdf-lib; password output not encrypted (disclosed). E10 label is a 609×128 PNG (+ mask) per page; no text layer. CSV has no BOM, CRLF line ends.
- **Ads (screenshots):** fake-download creatives under the result buttons and in the right rail (E01, save-cloud). Not clicked.
