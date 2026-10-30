Sent: 2026-10-30 10:41 ET
# B-0123 Localised tool pages show English H1 and title
Priority: P2 · Estimated effort: S–M · Report: #102 · Source: QA retest cycle 2, batch 22

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A visitor on /es (or any hreflang locale) should see the tool's name and page title in their own language, and the text should match between the server HTML and the rendered page.

## Why
These pages are hreflang alternates. An English H1 and title on /es, /pt and other locales tell Google and visitors the page is not localised. On roman-numeral-converter the server sends a Spanish H1 that the client then replaces with English. On merge-pdf the client replaces a Spanish title with English.

## Who uses this
Non-English searchers who land on a localised tool page from Google, and the site's hreflang/SEO setup, which relies on these pages being translated.

## Outcomes (ranked)
1. On every locale tool page, the rendered H1 and `<title>` are in the page's language and match the server HTML (no hydration overwrite).
2. word-counter and body-fat-calculator have es/pt/fr/de/ja/hi/zh/ko/id H1s and titles.
3. One Spanish term for merge (Unir or Fusionar) is used everywhere.
4. Where a translation is missing, there is a defined fallback. Do not mix languages in a way that leaves a translated server H1 but an English rendered one.

## Constraints
Do not change English pages or URLs. Keep hreflang as it is.

## Test cases
| Page | Expected H1 (rendered = server) | Expected title |
|---|---|---|
| /es/tool/roman-numeral-converter | Convertidor de números romanos… | Spanish |
| /es/tool/word-counter | Contador de palabras y caracteres | Spanish |
| /es/tool/body-fat-calculator | Calculadora de grasa corporal | Spanish |
| /es/tool/merge-pdf | Unir/Fusionar PDF (one term) | Spanish, unchanged after hydration |
| /pt, /fr, /de, /ja, /hi, /zh, /ko, /id for the same 4 tools | in the locale's language | in the locale's language |
