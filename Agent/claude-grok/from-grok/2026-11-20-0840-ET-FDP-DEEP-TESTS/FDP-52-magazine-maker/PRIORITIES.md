Sent: 2026-11-21 09:19 ET

# FDP-52 Magazine Maker: priorities (2026-11-21 EST)

No P0/P1 confirmed. Gate and trial counting are correct (per export).

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P2 (P1 if real Safari repeats it) | WebKit tab crash: Combine files with a JPG | iPhone/iPad users lose the page and their work. | Check `normalizeImageFile` on real Safari; decode via createImageBitmap with a size cap, or fall back to pdf-lib embedJpg directly. |
| P2 | WebP accepted, then blocks Combine assembly | A supported-looking file stops the whole issue; contradicts the FAQ. | Convert WebP/HEIC through canvas like other images, or remove them from `accept` and the FAQ; skip a bad file instead of failing the issue. |
| P2 | Phones forced to 442 px wide (Contents page style select, nowrap) | iPhone SE scrolls 122 px sideways; Android zooms the page out. | Let the trigger wrap or truncate (`min-w-0`, `truncate`), with the description under it. |
| P2 | Video out of date | Old Combine-only UI, "10 free uses daily", "free/no login" wording, personal file picker, Acrobat. | Re-record both modes on a clean profile; use Premium wording and trial uses; match the VideoObject name. |
| P2 | Combine-mode cover is a plain white page; the blog promises a cover image | First impression of a Premium output. | Reuse the Write-articles cover (accent block, optional image, logo) in Combine; fix the blog steps. |
| P2 | Locale pages: subtitle, offer line, builder labels English | Translated H1 next to English body. | Translate them. |
| P3 | Non-Latin text drawn as outlines (not searchable); Arabic left-aligned, period flipped | Accessibility/search; RTL polish. | Embed a subset font with ToUnicode instead of outlines; right-align RTL paragraphs. |
| P3 | TOC page has no folio (ii, iii, —, v) | Looks like an error. | Number the TOC page. |
| P3 | Combine titles default to file names | Contents page reads like a folder. | Offer "use first heading / PDF title". |
| P3 | Hero image pushes the builder below the fold (desktop) | Slower start. | Smaller hero or put it beside the tabs. |
| P3 | Meta 158 chars; og-default | Snippet cut; weak share card. | Shorter meta; tool OG image. |
| P3 | axe: label-content-name-mismatch (1), region (1), ad-label contrast (2) | A11y polish. | Fix the label; caption contrast (reserved ad slots kept). |
| Note | Strip sometimes jumps 0→2 after one download; one WebKit context at 2/2 downloaded | Display/server sync (unverified); the fresh-context gate held. | Watch in RUM; no action needed unless it reproduces. |
