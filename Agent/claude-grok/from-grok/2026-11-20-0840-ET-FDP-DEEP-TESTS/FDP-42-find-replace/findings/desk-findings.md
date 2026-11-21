Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace: desk findings (2026-11-21, box ET)

## SEO and indexing
- Title: "Find and Replace Text Online – .docx & Regex | FreeDailyPro". Meta description: 156 characters, specific (.docx, regex, "No upload").
- Canonical is self; 10 hreflang + x-default; one H1; the accordion H2s and H3s are sensible.
- JSON-LD (rendered DOM): SoftwareApplication, VideoObject, FAQPage (11), BreadcrumbList. The static HTML also carries them.
- P3:
  - The VideoObject name "How to Find and Replace Text with Regex Online" doesn't match the YouTube title "How to Use Find & Replace – Free Step-by-Step Walkthrough".
  - OG image is the generic `og-default.png`.
- Locales:
  - The title, meta, **H1**, tagline, drop-zone text, labels and switches all stay English on /es /pt /fr /de /ja /hi /zh /ko /id. Only the breadcrumb, chips and "Open from Google Drive" are translated (seen on /de).
  - /ar/tool/find-replace returns 404.

## Copy accuracy
1. **P2: FAQs contradict each other on .docx split runs.** "Why might a replacement be missing in my .docx file?" says a term spanning a formatting change "won't be found". "Is my Word formatting kept…?" and the About tip say it **is** found. Live T20 confirms it's found, so delete or rewrite the first FAQ.
2. **P3:** "A .doc file is refused with advice to save it as .docx…" and "any other extension gets a message listing the supported types". Live, both get the shared drop zone's generic "can't be used here. Check the file type this tool accepts." The specific messages in `FindReplace` never run.
3. **P2:** "Preserve case… a Capitalized match gives a replacement with a capital first letter". This is true only for single words: "Acme Corp" → "globex". The blog explains the catch; the FAQ and Tips don't. The tool's headline use case is renaming a product.
4. Everything else matches live behaviour: regex `$1`/`$&`/`$<name>`, `\n`/`\t`, whole word Unicode, JSON/XML warning, `_edited` names, one-step Undo, no live counter for .docx, headers/footers untouched, privacy.

## Blog
- `/blog/find-replace`, "Rename a Product Across a 40-Page Draft Without Breaking It" (Oct 17 2026), is accurate, practical, and honest about the title-case limitation. **Check 9: PASS.**
- **P3 (SEO / no-JS readers): prerender artefact.** In the static HTML the sentence about `$&` reads `<code><div id="root"></div>amp;</code>`. The `$&` in the post body was expanded by a JavaScript `String.replace` during prerender, inserting the matched `<div id="root"></div>`. After hydration the page reads correctly (`blog-render.json`), but crawlers and no-JS readers see a stray root div and "amp;". Any post containing `$&`, `` $` ``, `$'` or `$$` is affected. Use a replacer function in the prerender step.

## Duplicates and placement (C47)
- C47: text-paraphraser, grammar-checker, reading-level-checker, text-cleaner, find-replace, case-converter (all "absorbable"), plus ai-prompt-optimizer.
- Find & Replace is distinct: it's the only one with file round-trips, .docx in place, and regex.
- Overlap: find-replace-powerpoint (gated, PowerPoint category) does the same job for .pptx.
- Suggestion: cross-link both ways and consider one "Find & Replace in documents" entry that accepts .docx and .pptx. No removal.
- Text & Writing placement is correct.

## Code notes
- `FindReplace-DrPESoBx.js`:
  - Replace All `q` calls `logUsageNow` only when no file is loaded (`!a && !(await Z())`). Files skip it.
  - Download `G` uses ToolPage `d` (plain save), not the gated `D`, so there's no Drive/cloud and no cap.
  - Matching lives in `utils-CRM_dY3d` (`le` count, `me` replace, `ce` docx). `M()` is the preserve-case rule.
- `index-B1CTyGtY.js`: `Ps["find-replace"] = ["absorbable","text","Text utility on pasted text; a chat assistant does this for free"]`. `TA()` → uncounted. 99 tools are absorbable (excerpt included).
