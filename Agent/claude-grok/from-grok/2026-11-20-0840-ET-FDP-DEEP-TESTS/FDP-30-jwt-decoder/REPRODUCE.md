Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: reproduction steps (guest, https://www.freedailypro.com/tool/jwt-decoder)

Tokens are in `evidence/testfiles/tokens.json` (synthetic).

1. **P1 crash:** paste token `J13_exp_huge` (payload `{"sub":"u1","exp":1e17}`). The page is replaced by "An unexpected error occurred… Invalid time value / Reload page". Script: `scripts/jd-live.js J13`.
2. **P1 trial use:**
   1. In a context at 0 remaining (`fdp-usage-v1.usageToday` = limit), paste J16.
   2. Click Copy result, Save as text, Print, then Copy result again; also select the payload and press Ctrl+C. Everything works, no dialog appears, and the counter is unchanged after reload.
   3. Repeat with uses left after the 7:00 PM ET reset.
   4. Script: `scripts/jd-gate.js`.
3. **Milliseconds:** paste `J14_exp_ms` → "Issued at (iat): +057856-04-05T00:53:20.000Z UTC", "Not expired".
4. **String exp:** paste `J15_exp_string` → no time lines, no notice.
5. **Bearer copy:** paste `Bearer <J01>` → decodes fine. Compare Details › Tips ("Remove a leading word such as Bearer first…") and `/blog/jwt-decoder` › Common mistakes.
6. **Error strings:** paste `J11_bad_base64` → "The payload is not valid Base64URL text…"; the FAQ and Details say "Failed to decode JWT".
7. **Video:** https://www.youtube.com/watch?v=OhUnKjmiP48 at 0:10–0:52 shows the "10 free uses daily" badge and the browser's bookmarks bar.
8. **Privacy (positive control):** DevTools › Network, paste J16, filter for `issuer.example` or the first 30 characters of the token: no request matches. The URL stays `/tool/jwt-decoder`. Script: `jd-live.js` (`leaks: []`).
9. **iPhone SE:** 320 px viewport → 9 px horizontal scroll; the textarea placeholder is clipped.
