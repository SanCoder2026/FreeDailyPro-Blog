Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: test cases

- **URL:** https://www.freedailypro.com/tool/jwt-decoder, guest.
- **Tokens:** `evidence/testfiles/tokens.json` (synthetic; HS256 with the dummy secret "fdp-test-secret").
- **"Live"** = 2026-11-20 23:58 – 2026-11-21 00:15 EST.
- **Scripts:** `scripts/jd-live.js` (J ids), `jd-gate.js`, `jd-misc.js`, `jd-share.js`, `run-matrix.js`.

## A. Decoding
| ID | Input | Expected | Live |
|---|---|---|---|
| JD-01 | J01 HS256 valid | Header/payload JSON; iat 2025-11-20T00:53:20Z; exp 2100-01-01; Not expired; UTC + local | PASS |
| JD-02 | J02 expired | Expires 2020-09-13T13:26:40Z, red Expired | PASS |
| JD-03 | J03 nbf in 2100 | Not before … Not yet valid | PASS ("UTCNot yet valid" has no space, P3) |
| JD-04 | J04 alg none | Unsigned-token warning | PASS |
| JD-05 | J05 unicode | José Müller 日本 🚀 / São Paulo intact | PASS |
| JD-06 | J06 "Bearer " + token | Prefix removed, decodes | PASS |
| JD-07 | J07 "Authorization: Bearer …" | Decodes or a targeted hint | FAIL (P3): generic header Base64URL error |
| JD-08 | J08 line breaks | Decodes | PASS |
| JD-09 | J09 2 parts | "expected 3 parts … found 2" | PASS |
| JD-10 | J10 JWE 5 parts | A JWE note | PARTIAL (P3): generic "found 5" |
| JD-11 | J11 bad Base64URL | Names the part | PASS |
| JD-12 | J12 payload not JSON | "not valid JSON" | PASS |
| JD-13 | J13 exp 1e17 | "invalid date" on that line; page alive | **FAIL (P1)**: whole page crashes |
| JD-14 | J14 ms timestamps | Hint "looks like milliseconds" | FAIL (P2): year 57856, Not expired |
| JD-15 | J15 string exp | Note that exp is a string | FAIL (P2): silently ignored |
| JD-16 | J16 RS256 kid, aud array | Correct display | PASS |
| JD-17 | J17 header is an array | Warning | PARTIAL (P3): no warning |
| JD-18 | J18 padded | Decodes | PASS |
| JD-19 | J19 ~8 KB payload | Decodes quickly | PASS |
| JD-20 | J20 "bearer" only | Empty / no crash | PASS |
| JD-21 | J21 blog example | Matches the blog text | PASS |
| JD-22 | J22 invalid UTF-8 payload | A UTF-8 message (per the FAQ) | FAIL (P3): says "not valid Base64URL" |
| JD-23 | J23 token in quotes | A hint to remove quotes | PARTIAL (P3): generic error |

## B. Privacy, trial, outputs
| ID | Step | Expected | Live |
|---|---|---|---|
| JD-24 | Network scan during all cases | No token fragment in any request; URL unchanged | PASS (`leaks: []`) |
| JD-25 | At 0 remaining: Copy result / Save as text / Print / Copy again | Per policy (Santosh) | **Policy question**: all work, 10 → 10 |
| JD-26 | At 0: select the payload, Ctrl+C | Per policy | Policy question: works, 10 → 10 |
| JD-27 | With uses left: decode + each action | Per policy | **PENDING** (RERUN row 30) |
| JD-28 | Save as text content | Header, payload, time lines, "Calculated with FreeDailyPro.com" | PASS |
| JD-29 | Print (J16) | Result present, no controls | PASS (2 pages; repeats the full token, P3) |
| JD-30 | Share with a token pasted | Plain tool URL only | PASS |

## C. Layout, locales, a11y
| ID | Step | Expected | Live |
|---|---|---|---|
| JD-31 | 10 devices | No overflow, usable input | PARTIAL: iPhone SE 9 px overflow; 2-line textarea |
| JD-32 | 10 locales + /ar; axe | Translated or no hreflang; no serious axe issues | PARTIAL: es mixed, 8 English, /ar 404; label-content-name-mismatch (serious, 1) |
