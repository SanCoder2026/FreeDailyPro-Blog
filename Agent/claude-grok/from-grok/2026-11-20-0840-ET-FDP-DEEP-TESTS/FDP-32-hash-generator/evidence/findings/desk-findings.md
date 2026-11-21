Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: desk findings (2026-11-21 00:38–00:46 EST)

## Page and SEO
- 200; canonical self; in the sitemap with `/blog/hash-generator`. Title "Generate a Hash Online - MD5, SHA-1, SHA-256 | FreeDailyPro"; H1 "Hash Generator"; meta "Hash generator: get MD5, SHA-1, SHA-256, SHA-384 and SHA-512 for text or a file, and compare with an expected checksum. Runs in your browser." (accurate). "checksum" / "file" not in the title.
- JSON-LD: WebSite, SoftwareApplication (Offer 4.99), VideoObject, FAQPage (6), BreadcrumbList. Thumbnail img has no alt.
- Locales: es translated title/H1 (title "Generador de hash en línea: MD5, SHA-1, SHA-256 gratis", without the brand suffix), English body; de/ja/pt/fr/hi/zh/ko/id English under their lang + hreflang; `/ar/tool/hash-generator` 404.

## Copy vs behaviour
- Accurate: five algorithms at once, 4 MB chunks with a percentage, compare trims/lowercases/strips spaces, file takes priority (Limitations), privacy (no upload — confirmed by the request scan).
- "the text box hashes exactly what you typed" — CRLF is converted to LF by the browser (P3).
- "Matching ignores letter case and spaces, so you can paste a checksum exactly as copied from a web page" — `sha256:`-prefixed values and `sha256sum` output lines fail (P3).
- "click the underlined line Or choose a file to hash" — not reachable by keyboard (P1 a11y, see live findings).
- Nothing warns that results go stale when the text changes (P1, live findings).

## Blog `/blog/hash-generator` ("Checksum a File With a Hash Before You Call It Identical", Oct 17, 2026)
- Sound advice (trusted reference digests, full hex, line endings, re-saved files, incident template). Long and repetitive ("300+ professional tools…" twice). Says "remember 10 trial usages a day—prepare the file path and algorithm choice first": the tool computes all five algorithms at once, and live at 0 nothing was blocked. It never mentions the Compare box, the tool's best feature for its own use case.

## Completeness vs competitors (desk; e.g. emn178 online-tools, CyberChef, hash-file.online — general knowledge, not re-verified live)
- Missing: SHA-3 / SHA-224 / SHA-512/256, BLAKE2/3, CRC32, xxHash; HMAC with a key (explicitly excluded in Limitations); Base64 output; multiple files / drag-and-drop / a checksum manifest (`.sha256` file) verification; hashing the empty string. HMAC + SHA-3 + multi-file manifest verify are the natural Professional Tools / Premium Applications step.
- C50 (DUPLICATES.md) groups it with Password Generator / Password Strength; the merge suggestion there is between the two password tools. Hash Generator is distinct — keep.

## Code notes (`evidence/js/`)
- `HashGenerator-B91DxNzs.pretty.js`: `_()` hashes with hash-wasm in 4 MB slices; `U()` compare; textarea `onChange` → `s(value), l("")` (results `r` not cleared → stale); file `onChange` clears results; `H` → `await logUsageNow()` before hashing; Copy uses `copyText` (no gate); file input `className: "hidden"`.
