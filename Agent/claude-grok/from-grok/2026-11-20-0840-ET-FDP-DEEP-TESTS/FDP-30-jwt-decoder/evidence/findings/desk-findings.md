Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: desk findings (2026-11-20 23:55 – 2026-11-21 00:10 EST)

## Page and SEO
- 200, canonical self, no robots meta / X-Robots-Tag; tool and two blog posts are in the sitemap (`/blog/jwt-decoder`, `/blog/jwt-decoder-debug-tokens`).
- Title "Decode a JWT Online - JSON Web Token Debugger | FreeDailyPro"; H1 "JWT Decoder"; meta description "JWT decoder: paste a token (a leading Bearer is removed) to read the header and payload, see exp and iat times and whether it has expired. In your browser." (good, matches behaviour).
- JSON-LD: WebSite, SoftwareApplication (Offer price 4.99), VideoObject "How to Decode JWT Tokens Online", FAQPage (6 questions), BreadcrumbList. The Offer 4.99 sits on a page with no visible price or trial strip (same as earlier tools).
- Thumbnail `<img>` (i.ytimg.com hqdefault) has no alt.
- Locales: es has a translated title/H1 and one FAQ in Spanish; the rest of es is English (mixed page). de/ja/pt/fr/hi/zh/ko/id serve the English title/H1 under their `lang` and hreflang. `/ar/tool/jwt-decoder` → 404. es title says "gratis".

## Copy vs behaviour (all checked live)
- **Contradiction (P2):** Details › Tips says "Remove a leading word such as Bearer first: the tool counts dot-separated parts, and the extra word would corrupt the header." The meta, "How to use it" and the live tool (J06) all strip a leading "Bearer " automatically. Blog `/blog/jwt-decoder` › Common mistakes also says "Bearer eyJ… … ends in Failed to decode JWT" (wrong for a leading Bearer).
- **Error names (P2/P3):** the FAQ, Details and the blog quote "Failed to decode JWT" and "Invalid JWT format (expected 3 parts)". The live messages are "The header/payload is not valid Base64URL text, so it could not be decoded.", "…not valid JSON." and "Invalid JWT format: expected 3 parts separated by dots, found N." The string "Failed to decode" does not occur in the tool chunk (`js/JwtDecoder-*.js`).
- FAQ "Can it show a payload with non-English characters? … If the bytes are not valid UTF-8, the tool reports Failed to decode JWT" → live J22 says "not valid Base64URL text" (misleading).
- "The tool shows each as a UTC time" — it also shows local time (fine, copy is just incomplete). "Expires line carries a red Expired or green Not expired marker" — PASS; "Not yet valid" for nbf is not mentioned.
- Privacy section: "The token text is not sent to the site's servers. The only request tied to this tool is a usage record holding the tool name and a device identifier" — no token fragment was seen in any request (PASS for the token claim). The usage-record request itself was not separately observed (display-only; no backend claims).
- Limitations "an encrypted token with five parts is rejected" — PASS (generic message).

## Blogs
- `/blog/jwt-decoder` "Read a JWT's Claims and Expiry From a Staging 401" (Oct 17, 2026): accurate and practical; its worked example decodes exactly as described (J21). Errors: the Bearer claim and the "Failed to decode JWT" wording above. It already documents the ms-timestamp and string-exp pitfalls the tool doesn't flag.
- `/blog/jwt-decoder-debug-tokens` "Decode JWTs Instantly in Your Browser for Auth Debugging" (Sep 3, 2026): generic marketing; says "YouTube walkthroughs for developer tools are on the way" (a video exists since 2026-09-23) and invites requests for "signature verification helpers, JWKS explorers". Two posts compete for the same query; consider merging or linking the older to the newer.

## Completeness vs competitors (desk; jwt.io, token.dev, jwt.ms — from general knowledge, not re-verified live)
- Missing vs jwt.io: signature verification (HS secret, RS/ES public key, JWKS URL), an encoder/signer, the signature segment display, colour-coded parts, per-part copy buttons, claim explanations on hover, relative time ("expires in 3 h"). The page states plainly that it does not verify (honest). Verification with a pasted public key/JWKS done locally would be the natural Professional Tools / Premium Applications hook.
- Tagged `absorbable:dev-text` in tools.csv; not a duplicate. Fits Developer & Security Tools next to Base64 / Hash / UUID.

## Code notes (`evidence/js/`)
- `JwtDecoder-4zWjWHdb.pretty.js`: line ~93 builds `new Date(claim * 1e3)` and line ~204 renders `n.date.toISOString()` with no range guard → J13 crash; no unit heuristic → J14. Lines ~40–47: any decode failure (including UTF-8) is reported as "not valid Base64URL".
- `utf8-C8MzR3N4.pretty.js`: strict `TextDecoder(…, {fatal:true})`; its exception is reported with the Base64URL message (J22).
- `useLogToolUsage-BdvvKW0n.pretty.js`: shared usage hook; no gate fired at 0 remaining for Copy/Save/Print/selection copy.
