Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: desk findings (2026-11-21 00:17–00:25 EST)

## Page and SEO
- 200; canonical self; in the sitemap with `/blog/uuid-generator`. Title "UUID Generator Online - Bulk & Instant | FreeDailyPro"; H1 "UUID Generator"; meta "UUID generator: make up to 1,000 random UUIDs per batch, with or without hyphens, in lowercase or uppercase. Copy one or the whole list. In your browser." (accurate). "v4" / "GUID" not in title or meta (common queries).
- JSON-LD: WebSite, SoftwareApplication (Offer 4.99), VideoObject, FAQPage (6), BreadcrumbList. Thumbnail img has no alt.
- Locales: es has a translated title/H1 ("…en línea gratis…") with an English body; de/ja/pt/fr/hi/zh/ko/id are English under their lang + hreflang; `/ar/tool/uuid-generator` 404.

## Copy vs behaviour
- **Contradiction (P2):** Details › Tips: "Output is in the standard lowercase hyphenated form… so uppercase it yourself if a system insists." The tool has an Uppercase checkbox (and the FAQ, Limitations and meta say so).
- **Contradiction (P2, trial):** blog "Each press of the button counts as one of your 10 trial usages for the day" vs live at 0 (not blocked, 10 → 10).
- Blog closing: "Would you like to see other UUID versions, uppercase output…?" — uppercase already exists (stale).
- What-is-it says UUIDs are used for "session tokens"; "When not to use it" and the blog say not to use them as session tokens (P3 mixed message).
- Tips "Keep the Count at 100 if you need a quick pool" while the default is 5 (odd, P3).
- FAQ/Details validation text matches live (blank/0/negative/decimal → message; >1,000 → note and 1,000). Privacy text ("No UUID is requested from a server or stored remotely") matches the network scan.

## Blog `/blog/uuid-generator` ("Generate Five UUIDs for a Database Seed Migration", Oct 17, 2026)
- Practical and technically correct (v4 structure, the sample's version/variant digits check out, 122 random bits, collision odds, regex check, unique constraint advice). Issues: the trial-use sentence above; the stale "uppercase output" request.

## Completeness vs competitors (desk; uuidgenerator.net, uuidtools.com — general knowledge, not re-verified live)
- Missing: versions 1, 3/5 (name-based), 7 (time-ordered, now common for DB keys) and nil/max; braces / quotes / comma-separated / SQL / JSON array formats; Download .txt/.csv for large batches; a UUID validator/decoder (version, variant, v1/v7 timestamp); a seeded/reproducible option is not expected. v7 + formats + download are the natural Professional Tools / Premium Applications step.
- Tagged `absorbable:dev-text`; not a duplicate; correct category.

## Code notes (`evidence/js/`)
- `UuidGenerator-CmXHafTq.pretty.js`: `D()` validation (cap 1,000), `E()` formatting, `b` = Generate → `await logUsageNow()` then `crypto.randomUUID()`; per-row copy and Copy All → `gateShare(...)`.
- `useShareGate-BYBawloP.pretty.js` / `useExportGate-BU4jIFHF.pretty.js`: counted only when `known && !paid`; `checkExport` can open the cap dialog ("download" reason). At 0 nothing blocked live.
