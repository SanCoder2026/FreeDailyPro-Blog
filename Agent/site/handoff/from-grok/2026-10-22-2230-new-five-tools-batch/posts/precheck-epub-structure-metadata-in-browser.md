---
title: "Pre-Check an EPUB for Structure and Metadata"
subtitle: "Catch missing files, navigation gaps, cover issues, and accessibility notes before store upload"
description: "Use EPUB Checker to pre-check an .epub in the browser for structure, metadata, navigation, cover, and accessibility problems."
date: 2026-10-22
author: "FreeDailyPro Team"
topic: file-tools
tools: [epub-checker, book-writing-toolbox, word-counter, compress-pdf]
personas: [content-writer, student]
workflows: []
tags: ["EPUB checker", "EPUB validation", "ebook preflight", "accessibility", "metadata", "FreeDailyPro", "self publishing", "EPUB 3"]
image: "../images/precheck-epub-structure-metadata-in-browser.webp"
imageAlt: "Author reviewing an EPUB validation checklist on a laptop with an e-reader nearby"
draft: false
---

![Author reviewing an EPUB validation checklist on a laptop with an e-reader nearby](../images/precheck-epub-structure-metadata-in-browser.webp)

*Catch missing files, navigation gaps, cover issues, and accessibility notes before store upload*

[FreeDailyPro.com](https://www.freedailypro.com) -- Before Sam Okonkwo uploads a novella to a store, he wants a browser-side structural pre-check that does not send the manuscript to a random server. [EPUB Checker](https://www.freedailypro.com/tool/epub-checker) opens an `.epub` in the browser and reports structure, metadata, navigation, missing files, alt text, cover, and accessibility problems.

This guide covers one job only: run a practical pre-check, fix fails first, then still run official EPUBCheck before store submit.

## Pre-check vs EPUBCheck

This is a **practical pre-check**, not the official EPUBCheck validator. A pass here does **not** guarantee a store will accept the file. Run EPUBCheck (or the store’s own checker) as well before you publish. Use FreeDailyPro’s checker to catch obvious ZIP/structure and metadata issues early while the file never leaves your tab.

Writing and packaging: [Book Writing Toolbox](https://www.freedailypro.com/tool/book-writing-toolbox). Chapter length checks: [Word Counter](https://www.freedailypro.com/tool/word-counter). Category: [file tools](https://www.freedailypro.com/category/file-tools).

## Worked example: novella proof, Atlanta GA

- File: `Title_v3_proof.epub` (~8 MB)
- Goal: zero fails on structure/mimetype/navigation; warnings reviewed intentionally
- Next: official EPUBCheck, then store upload
- Done definition: report saved as text note, fails fixed, rebuilt EPUB re-checked

## Steps on EPUB Checker

1. Keep a copy of the EPUB; never overwrite your only master mid-fix.
2. Open [EPUB Checker](https://www.freedailypro.com/tool/epub-checker).
3. Drop the `.epub` (files over about 100 MB may be slow or hit browser memory).
4. Read fails first—missing files, broken navigation, mimetype problems.
5. Review warnings separately (for example empty alt attributes may warn even when intentional).
6. Fix sources (chapters, package, cover) and rebuild the EPUB from your maker/export path.
7. Re-run the checker until fails are clear.
8. Run official EPUBCheck or the store validator before publish.
9. Open the file on a real reader for human proof.
10. Archive report notes with the version number that passed.

## What the mimetype file is about

EPUB is a ZIP with rules. The `mimetype` entry must meet packaging rules (location and content). When the checker flags mimetype, fix packaging rather than ignoring the line—stores are picky about the container.

## Warnings vs fails

Fails block confidence for upload. Warnings mean “look carefully.” An empty alt attribute might be a warning because accessibility reviewers care; decide whether the image needs real alt text. Do not mass-ignore warnings without reading them.

## Common mistakes

- Treating a browser pre-check as a store acceptance certificate.
- Uploading a 120 MB illustrated EPUB and expecting instant results on a low-memory laptop.
- Fixing the report in a text editor instead of rebuilding the package correctly.
- Skipping real-device reading after the structural report looks green.
- Closing the tab and losing the report without notes—the file is not stored by FreeDailyPro.

## Limits and good to know

- The EPUB is opened with a ZIP reader entirely in your browser; not uploaded, stored, or logged; gone on close/reload.
- Large files may stress memory—close other heavy tabs.
- Among FreeDailyPro’s 200+ professional tools, this is the browser EPUB structural pre-check.
- Not a substitute for store-specific packaging rules (Amazon, Apple, Kobo each have extras).

## Accessibility discipline

If your book has images, plan alt text early. The checker surfaces empty alts so you do not discover the gap after a store accessibility review. Text-only books still benefit from clean navigation and language metadata.

## Rebuild loop that saves weekends

Sam’s loop: export EPUB → FreeDailyPro pre-check → fix → official EPUBCheck → Kindle/Apple sample → publish. Skipping the first browser pass often means learning the same mimetype lesson inside a slower store queue.

## Version naming

`Title_v3_proof.epub`, `Title_v4_store.epub`. Keep the checker notes next to each version so you know which issues were already closed.

## Navigation and TOC failures

If the checker reports navigation problems, open the EPUB in a reader that shows the NCX/nav document. Missing chapter links often come from export settings that skip headings. Fix heading levels in the source, re-export, and re-check before you touch CSS.

## Cover presence

Stores still reject packages with missing or poorly linked covers. Confirm the cover is both in the package and referenced correctly. A pretty JPEG sitting outside the EPUB does not count.

## Team handoff

When a formatter owns the EPUB and an author owns the text, send the checker report as a bullet list of fails only. Authors do not need ZIP jargon—they need “Chapter 4 missing from TOC” in plain language.


## Browser memory tips

Close other tabs before dropping a large illustrated EPUB. If the tab freezes, split the problem: validate a text-only build first, then reintroduce images. A green report on a slim build tells you the structure is sound before art weight is added.

## FAQ

**Is this EPUBCheck?** No—practical pre-check; still run EPUBCheck before stores.

**Is the book uploaded?** No—browser-side only.

**What about warnings?** Read them; fix or document intentional exceptions.

## Closing next step

Catch structure problems before the store queue does. Open [EPUB Checker](https://www.freedailypro.com/tool/epub-checker), drop the file, clear fails, then run official validation.

Need a pre-publish checklist for EPUB + store dual submit? [https://www.freedailypro.com/contact](https://www.freedailypro.com/contact).
