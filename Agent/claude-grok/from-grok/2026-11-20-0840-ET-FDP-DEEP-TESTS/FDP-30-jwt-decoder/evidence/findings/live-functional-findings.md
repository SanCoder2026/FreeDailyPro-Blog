Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: live functional findings (guest, headless Chromium, 2026-11-20 23:58 – 2026-11-21 00:05 EST)

Tokens: `testfiles/tokens.json` (J01–J23, synthetic, HS256 signed with the dummy secret "fdp-test-secret"; no real credentials). Results: `json/cases.json`, `json/cases-extra.json`.

## Works (PASS)
- J01/J06/J08/J18: standard HS256 token, with a leading "Bearer ", with line breaks, and with "=" padding: header and payload decode; iat/exp shown in ISO UTC plus local time; "Not expired".
- J02 expired → red "Expired"; J03 nbf in the future → "Not yet valid".
- J04 alg "none" → a clear warning that the token is unsigned.
- J05 unicode payload (José Müller 日本 🚀, São Paulo) displays correctly.
- J16 RS256 with kid and an aud array displays correctly.
- J19 large payload (~8 KB) decodes; J21 the blog's worked example decodes exactly as the blog describes (iat/nbf 2025-10-09T08:53:20Z, exp 09:53:20Z, Expired).
- Errors: 2 parts → "Invalid JWT format: expected 3 parts separated by dots, found 2."; bad Base64URL → "The payload is not valid Base64URL text…"; non-JSON payload → "…decoded to text, but it is not valid JSON."

## Defects
- **P1 J13 crash:** payload `exp: 1e17` (out of the JS Date range) → `RangeError: Invalid time value` in `toISOString`. The whole page is replaced by the error boundary "An unexpected error occurred… Invalid time value / Reload page" (`screens/live/case-J13.png`). Any token with a corrupt or hostile numeric claim takes the tool down instead of showing "invalid date".
- **P2 J14 millisecond timestamps:** iat/exp in ms → "+057856-04-05T00:53:20.000Z", "Not expired", no hint. The blog itself names this mistake; the tool could detect values > 1e11 and say "looks like milliseconds".
- **P2 J15 string exp:** `"exp":"1763603600"` → no time lines and no notice (documented in the blog, not in the tool).
- **P3 J07:** "Authorization: Bearer eyJ…" → "The header is not valid Base64URL text" (only a leading "Bearer " is stripped). J23 a token in quotes → same message. A targeted hint ("remove the quotes / the header name") would help.
- **P3 J10:** a 5-part JWE gets the generic "found 5" message; the FAQ explains JWE but the tool does not.
- **P3 J22:** a payload that is valid Base64URL but not valid UTF-8 → "The payload is not valid Base64URL text" (misleading; the FAQ promises "Failed to decode JWT").
- **P3 J17:** a header that is a JSON array `[1,2]` is shown with no warning.
- **P3 spacing:** "2100-01-01T00:00:00.000Z UTCNot yet valid" (no space before the marker) in the page text.
- After an error, Copy result / Save as text / Print stay visible.

## Privacy (PASS)
- During every case, no request to any host carried any payload fragment or the token (`leaks: []` in `json/cases.json`). The token is not mirrored into the URL (no `history.replaceState` in `JwtDecoder-*.js`). This matches the Privacy copy ("The token text is not sent to the site's servers"). Unlike FDP-27/28/29, there is no URL-mirroring leak here.

## Trial use (policy question)
- `json/gate.json` (2026-11-21 00:00:52–00:01:35 EST): the context loaded at 0 remaining (10/10). Copy result, Save as text (`testfiles/outputs/Z_at_zero-jwt-decoder-result.txt`, ends with "Calculated with FreeDailyPro.com", intentional), Print and Copy result again all worked with no dialog; count 10 → 10, also after reload. Selecting and copying the payload text (Ctrl+C) at 0: no dialog, clipboard filled, 10 → 10.
- No usage strip, cap dialog, pass or Stripe appeared, so the payment path was not reachable.
- Not in the Nov 20 uncounted list → **policy question for Santosh**. With uses left: pending (RERUN-AFTER-RESET row 30).

## Print (PASS)
- `testfiles/outputs/print-preview.pdf` (2 pages): breadcrumb, H1, the full token, Header and Payload side by side, the time lines, then "Watch: JWT Decoder in Action" links. The result is present. P3: the printout repeats the full token (a credential) and the video block; consider printing only the decoded parts by default.

## Share / storage
- `json/share.json` (2026-11-21 00:15 EST): with token J16 pasted, Share copied only `https://www.freedailypro.com/tool/jwt-decoder` (no token), which is correct for a credential tool. Favorites are stored in localStorage. Whether any token text lands in storage was not inspected (unverified).
