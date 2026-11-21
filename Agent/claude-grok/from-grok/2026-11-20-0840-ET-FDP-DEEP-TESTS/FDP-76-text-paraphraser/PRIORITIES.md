Sent: 2026-11-21 17:25 ET

# FDP-76 priorities

**P0:** none found.

**P1**
1. Nested-rule corruption: "Don't forget to call me." → Medium "Remember to to call me."; Strong "Remember to forget to call me." (meaning inverted). Strong openers: "That said,But we stayed… In addition,, it rained." Copy puts hidden U+E000–U+E003 characters on the clipboard; restore gives "RememberDon't forget…". Later rules rewrite the stored original inside the marker span. (`harness/harness.json` H07/H08/H12/H28, `json/clip.json`, `json/left-firefox.json` L05/L07/L08.)

**Owner question**
1. Paraphraser takes no trial use: results, Rewrite again and Copy at 10/10, and 15 presses at 0/10, all with 0 `usage.log` POSTs. The code calls `logUsageNow`, the blog says Paraphrase counts, and the FAQ says a usage tick is recorded; the tool isn't `known` (no strip). Count it, or list it as uncounted and update the copy and Offer.

**P2**
1. Articles not adjusted: "a issue", "a approach", "an concept", "an significant", "a aim", "a enormous issue"; also "begin on", "a handful of left", "That said hard", "I as well want". The page claims the grammar stays intact.
2. The blog explains "In addition,," as a comma quirk and suggests Find & Replace; it's the P1 bug.
3. Video 4NQaC_Th79E: old UI, "Free: 10 uses/day" strip + Quick Buy, "too similar to a source you're referencing" copy.
4. Rewrite again usually returns identical text; thin value next to AI rewriters (C47 merge candidate).

**P3**
1. English-only tool served on 9 locale URLs with English controls.
2. Notice toasts stack.
3. iPhone SE 9 px; ja desktop overflow; axe label-content-name-mismatch + region (desktop), color-contrast (Pixel 7).
