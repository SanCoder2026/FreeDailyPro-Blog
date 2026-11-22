Sent: 2026-11-21 19:08 ET

# FDP-83 reproduce

1. **Paywall only (context):** guest window → https://www.freedailypro.com/tool/file-conversion-studio → `workflow-paywall`, no file input, no strip/Quick Buy.
2. **Start trial:** press "Start 7-day trial · $29.99/mo" → /profile sign-in (`returnTo=…autoBuy=workflow:file-conversion-studio`). Stop.
3. **No preview (P2):** scroll the page: no video, screenshot or sample file; YouTube channel has no Studio video (`video/channel-videos.txt`).
4. **Locales (P2):** open /de/tool/file-conversion-studio → English except nav.
5. **Meta (P2):** view-source → `<meta name="description">` ends "your own file."
6. **Guest confirm message (P3):** open `…/file-conversion-studio?checkout=success` → "Thank you. We are confirming your payment…"; after ~60 s it disappears.
