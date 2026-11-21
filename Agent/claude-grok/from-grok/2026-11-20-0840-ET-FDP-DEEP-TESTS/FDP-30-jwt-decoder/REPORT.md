Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder (jwt-decoder): deep test report for Claude

- **Written:** 2026-11-21 00:20 EST (box `date`, ET). Testing ran 2026-11-20 23:55 – 2026-11-21 00:14 EST.
- **Tool:** https://www.freedailypro.com/tool/jwt-decoder. Row 30 of TEST-ORDER.md: Pro, Developer & Security Tools, test-plan rank 23 ("wave-1 APIs"); no duplicate group. **GSC data is not available.**
- **Classification:** Professional Tool, tagged `absorbable:dev-text`. Live, at 0 remaining every result action still works with no cap dialog.
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD, 10 locales + /ar, both blog posts, sitemap. JS chunks: `JwtDecoder`, `utf8`, `copyText`, `useLogToolUsage`.
  - **YouTube video:** yt-dlp, 40 frames, 4 sheets and a zoom.
  - **Headless Playwright:**
    - 23 synthetic token cases (J01–J23), with a request scan for token fragments.
    - Gate run (contexts at 0) incl. selection copy.
    - Print rendering; keyboard order; head tags.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** every fresh context loaded at "0 remaining" (`usageToday` 10 of 10, day key 2026-11-21). Trial uses spent: **0**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (no prompt appeared), no ad clicks, no API/MCP, no site or repo changes. All tokens are synthetic (dummy secret "fdp-test-secret").
- **Sign-in:** nothing on this tool needs it. No URL was blocked by sign-in.
- **Pending:** the "context with uses left" count → **RERUN-AFTER-RESET row 30** (`jd-gate.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/`):
- `JwtDecoder-4zWjWHdb.pretty.js`:
  - Line ~93: `new Date(claim * 1e3)` for iat/nbf/exp; line ~204 renders `n.date.toISOString()` with no validity guard → the whole page crashes on an out-of-range claim.
  - Lines ~40–47: every decode failure (including strict UTF-8) becomes "not valid Base64URL".
- `utf8-C8MzR3N4.pretty.js`: `TextDecoder("utf-8", { fatal: true })`.
- `useLogToolUsage-BdvvKW0n.pretty.js`: shared usage hook; nothing was charged at 0 remaining.

After you ship, rerun `scripts/jd-live.js` (J13 must show an "invalid date" line instead of the error page; `leaks` must stay empty), `jd-gate.js` and `jd-misc.js`, then test-cases.md (JD-01…JD-32).

## Intent

A developer or QA engineer with a failing login or a 401 wants to paste a token and in seconds see:
- what it claims (alg, kid, iss, aud, sub, scope, roles)
- whether it has expired or is not yet valid, in UTC and local time
- a clear reason when the token is malformed

They must trust that the token (a credential) never leaves the browser. Ideally they can also check the signature without going to jwt.io. That is the natural Professional Tools / Premium Applications step up.

What works well:
- Decoding is correct for every normal shape: Bearer prefix, line breaks, padding, unicode, RS256 with kid and an aud array.
- The Expired / Not yet valid markers are right, and the alg "none" warning is excellent.
- Errors are specific (part count, which part, Base64URL vs JSON).
- **Privacy holds:** no request carried any token fragment, and the token is not mirrored into the URL. Unlike FDP-27/28/29, there is no leak here.
- The 2-page print includes the result.

Trust breaks in a few places:
- One malformed claim crashes the whole page.
- Millisecond timestamps are shown as year 57856 and "Not expired".
- Page copy and the blog contradict the tool about "Bearer" and quote error messages that no longer exist.
- There is no signature verification, encoder or per-part copy, compared with jwt.io.
- The video shows the old UI, "10 free uses daily" and the recorder's personal bookmarks bar.

## Why: what the evidence says

- **P1: an out-of-range claim crashes the whole page.**
  - A token with `exp: 1e17` throws `RangeError: Invalid time value`.
  - The tool and the page are replaced by "An unexpected error occurred… Reload page" (`screens/live/case-J13.png`, `json/cases.json` J13, 2026-11-20 23:59 EST).
  - Corrupt or hostile tokens are exactly what people paste into a debugger.
- **P1, policy question for Santosh (not a PASS):**
  - At 0 remaining, Copy result, Save as text, Print and a second Copy result all worked with no cap dialog. The count stayed 10 → 10, also after reload (`json/gate.json`, 2026-11-21 00:00:52–00:01:35 EST).
  - Selection copy (Ctrl+C) of the payload: same.
  - No strip or pass appears on the page.
  - This tool is not in the Nov 20 uncounted list. With uses left: pending.
- **P2 items:**
  - No signature verification (HS secret / RS-ES public key / JWKS), no encoder, signature segment hidden, no per-part copy or claim hints (desk vs jwt.io). The copy is honest about it.
  - Millisecond timestamps (J14) → "+057856-…" and "Not expired" with no hint; string `exp` (J15) silently ignored. The blog documents both pitfalls; the tool doesn't flag them.
  - **Copy contradictions:**
    - Tips: "Remove a leading word such as Bearer first… the extra word would corrupt the header". The blog says the same. The tool strips it (J06), and the meta / How-to copy say so.
    - FAQ, Details and the blog quote "Failed to decode JWT" / "Invalid JWT format (expected 3 parts)". Those strings don't exist; the live messages differ.
  - **Video OhUnKjmiP48 (80 s):**
    - Shows the old badges ("10 free uses daily", "Security & Developer").
    - Full-desktop capture: the text is barely legible, and the personal bookmarks bar and taskbar are visible.
    - The title says "Free"; the embed name differs from the YouTube title.
  - Two overlapping blog posts. The older one says "YouTube walkthroughs … are on the way".
  - Locales: es is half-translated (title "gratis"); 8 others are English under their lang/hreflang; /ar 404.
- **P3 items:**
  - iPhone SE 9 px overflow (a button at right=329).
  - The 2-line textarea on mobile clips the placeholder.
  - "UTCNot yet valid" has no space.
  - Messages: "Authorization: Bearer" and quoted tokens get the generic Base64URL message; invalid UTF-8 is called "not valid Base64URL"; a 5-part JWE gets the generic message; an array header gets no warning.
  - The printout repeats the full token.
  - Result actions stay visible after an error.
  - Thumbnail alt; axe label-content-name-mismatch and region; JSON-LD Offer 4.99; "Files never stored" badge on a text tool.

## Outcomes we want

1. No input can crash the page. Invalid or out-of-range time claims show "invalid date", and ms-looking or string values get a one-line hint.
2. Santosh decides the trial-use policy for this tool; the page and the JSON-LD Offer reflect it.
3. The copy, FAQ and blog match the tool exactly: Bearer is stripped, and the quoted error messages match what the tool shows.
4. A clear Premium step: local signature verification (secret / PEM / JWKS), the signature segment, per-part copy and relative expiry ("expires in 2 h").
5. A current, cropped, clean-profile video using "trial uses" wording. Consolidate the two blog posts.
6. P2/P3 polish per PRIORITIES.md.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PARTIAL | 18 of 23 cases behave correctly. J13 crashes the page; J14/J15 mislead. `json/cases.json`, `cases-extra.json`. |
| 2 | Completeness vs competitors | PARTIAL | Decode only. No verify, encoder, signature view, per-part copy or claim hints (desk vs jwt.io/token.dev; not re-verified live). |
| 3 | Ease of use | PASS (minor) | Paste-and-read, no button. Specific errors. Mobile textarea only 2 lines. |
| 4 | Layout attractiveness | PASS (minor) | Clean side-by-side JSON. iPhone SE 9 px overflow; error page on J13. |
| 5 | Payment process | N/A (untested) | No cap dialog, pass or Stripe appeared, even at 0 remaining. |
| 6 | Information correct | PARTIAL | Decoded values and time markers are correct. Copy contradicts the tool on Bearer and quotes old error strings. |
| 7 | Indexing | PASS | 200; canonical self; no robots meta or X-Robots-Tag; in the sitemap. |
| 8 | SEO | PARTIAL | Strong title and meta, H1, FAQPage (6), VideoObject. English pages under 8 hreflangs, es mixed, /ar 404, thumbnail alt, Offer 4.99. |
| 9 | Blog exists and accurate | PARTIAL | `/blog/jwt-decoder` is accurate and practical (its example reproduces exactly) except the Bearer and "Failed to decode JWT" lines. `/blog/jwt-decoder-debug-tokens` is generic and stale on the video. |
| 10 | YouTube video exists | PASS | OhUnKjmiP48, 80 s, 20 views, uploaded 2026-09-23. |
| 11 | FAQ and guide correct | PARTIAL | 6 FAQs, good topics; the error strings and the UTF-8 answer don't match live. |
| 12 | Video shows current capabilities | PARTIAL | Core flow is the same. Old badges ("10 free uses daily"), illegible full-desktop capture, personal bookmarks visible; no time lines or errors shown. |
| 13 | Storage | PASS | Favorites in localStorage. Token not in the URL. Token persistence in storage not inspected (unverified). |
| 14 | Sharing | PASS | With a token pasted, Share copied only `https://www.freedailypro.com/tool/jwt-decoder` (no token; `json/share.json`, 00:15 EST). Right for a credential. |
| 15 | Downloads | PASS | Copy result and Save as text (.txt with the intentional "Calculated with FreeDailyPro.com") work; print is 2 pages with the result. |
| 16 | Usage count | **Policy question** | At 0 remaining, all result actions and selection copy work, 10 → 10. With uses left: pending (RERUN row 30). |
| 17 | Categorization in section | PASS | Developer & Security Tools with Base64, Password Generator, Password Strength. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Developer & Security Tools. |
| 19 | AI need/demand | PASS (demand steady) | "jwt decoder" is a steady developer query. AI is not needed to decode; an optional "explain these claims" would be a nice-to-have. |
| 20 | Merge better? | No | Distinct. Could later host a JWT encoder/verifier as tabs. |
| 21 | Remove? | No | |
| 22 | Duplicates | None | Two blog posts overlap (consolidate); no duplicate tool. |

## Severity summary
- P0: 0. Privacy holds: no token fragment in any request.
- P1: 2 (page crash on an out-of-range claim; trial-use policy question).
- P2: about 6.
- P3: several.
