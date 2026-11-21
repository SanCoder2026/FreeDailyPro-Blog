Sent: 2026-11-21 10:59 ET

# FDP-56: how to reproduce (guest)

## Policy: Copy at the cap
1. In a fresh profile, check localStorage `fdp-usage-v1` shows `usageToday: 10, limit: 10` (most fresh guest contexts on 2026-11-21).
2. Open https://www.freedailypro.com/tool/password-generator and click **Copy**. "Copied!" appears, the clipboard holds the password, and no dialog or `/api/trpc/usage.log` POST appears in DevTools.
3. Read Details → Privacy ("A usage count is recorded when you copy") against the FAQ "Is my password sent anywhere, or does it use up a trial use…" ("neither that nor copying one takes a trial use").

## P2: spaces in the symbols box
1. Clear "Symbols to use" and type three spaces.
2. Set How many to 10 and click Generate Password.
3. The alert reads "The symbols box is empty, so the default symbols are used.", yet every password contains a space (some leading or trailing, which you can't see). The entropy line says 63 possible characters.

## P2: video
Watch https://www.youtube.com/watch?v=LrkYLI-EnRs at about 0:20: breadcrumb "Text & Writing", "10 free uses daily" chip, no Passphrase toggle.

## P2: guides
Expand "Guides and next steps": "Convert chmod Octal and Symbolic Permissions" and "Convert cURL to fetch and Python Requests".

## Desk: maths
`node px56-stats.js` (the site's functions verbatim): brute-force count = site count, 100k sample shares.
