Sent: 2026-10-30 14:42 ET

# B-0271 STL ASCII / Binary Converter: best GSC CTR among tools — keep it; add batch, normals report and size savings; fix title and meta
Priority: P3 · Estimated effort: S · Report: #148 · Source: curl + seo.py, Playwright headless logged out at 1280/390 px, Google top 5 (WebSearch), 2026-10-30 ~14:36–14:41 ET. SEO backfill 11: GA top-50 list (raw analytics line 29) is exhausted after user-agent-parser (#49), so the next picks follow the GSC Top 50 pages list by clicks among tested tools.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A maker with an ASCII STL that a slicer or upload service rejects should get a smaller binary STL with identical geometry.
## Why
- **GSC:** /tool/stl-ascii-binary-converter 13 clicks / 180 impr / 7.2% / pos 10.2; the slash URL /tool/stl-ascii-binary-converter/ 2 / 31 / 6.5% / pos 32.3 (raw analytics, Top 50 pages). The slash URL now 301s to the canonical ✔. These are the strongest CTR numbers among tool pages at this position, so protect the title wording ("Convert STL ASCII to Binary").
- t.stl (1 facet) → "Detected as ASCII STL", 3 vertices, 1 triangle, "0.1 KB binary size". "Convert to ASCII STL" is correctly **disabled** with the title "This file is already ASCII STL" ✔. Convert to Binary runs; Download gated at 0 trial uses (owner's decision).
- **Missing vs competitors (~14:39 ET):** batch up to 200 files + ZIP (FormatDesk, STL Editor); % size reduction shown (JAD Apps); normals report / recompute (FormatDesk, JAD Apps); solid-name kept in header and "no 'solid' header trap" (FormatDesk); attribute word (colour) preserved (FormatDesk).
- No overflow at 390 px. /es serves the English title → **B-0123**.
## Who uses this
3D-printing hobbyists, CAD users, students.
## Outcomes (ranked)
1. Show before/after size and % saved.
2. Batch conversion with a ZIP.
3. Normals check; keep the solid name.
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD. Title "Convert STL ASCII to Binary Online - Free Tool | FreeDailyPro" **61 chars** with "Free". **Meta 88.** H1 "STL ASCII / Binary Converter".
- **Keywords:** "stl ascii to binary", "convert stl to binary", "binary stl to ascii", "stl file size reduce".
- **Suggested:**
  - Title: `STL ASCII to Binary Converter – No Upload | FreeDailyPro` (56)
  - Meta: `Convert an STL file from ASCII to binary, or binary to ASCII, in your browser. The format is detected for you, the geometry is unchanged, nothing is uploaded.` (158)
  - H1: `Convert STL ASCII to Binary (and Back)`
  - FAQ: "How much smaller is binary STL?" · "Does conversion change the model?" → "No." · "Is my file uploaded?" → "No."
## Constraints
Keep "Convert STL ASCII to Binary" at the start of the title. Check in GSC 28 days after the change.
## Test cases
1. t.stl (ASCII, 1 facet) → detected ASCII; binary output must be 134 bytes (84 + 50×1).
2. Title ≤ 60; meta 140–160.
