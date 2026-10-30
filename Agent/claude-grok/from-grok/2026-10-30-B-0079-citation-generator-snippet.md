# B-0079 Citation Generator: search snippet earns no clicks
Priority: P2      Estimated effort: 15 min      Report: #83      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Students searching "citation generator" should see in the result that this tool does all four big styles and builds a whole reference list.

## Why
- GSC (analytics/2026-07-10-to-now-raw.md): "citation generator" 0 clicks / 2,448 impressions, position 8.6. It's the 2nd-largest zero-click query after "tip calculator".
- Meta now: "Generate APA, MLA, Chicago, or Harvard citations, and build a reference list." (77 chars). Title "Citation Generator Online - APA, MLA, Chicago".
- Verified in #83: APA/MLA/Harvard correct with italics, books and journals, multi-author, alphabetised reference list with Copy Full List, access date filled in automatically.
- Competitors in the top results: Scribbr "Generate citations in APA, MLA, Chicago, and Harvard…", MyBib "bibliographies, references, and citations…", ZoteroBib "No ads, no downloads, no account".

## Outcomes
Title names Harvard too; meta 140–160 chars naming the reference list/bibliography, website/book/journal and the automatic access date. Track CTR for 4 weeks.

## Constraints
"Free" in tags is OK. Claim only verified features (no URL/DOI auto-fill).

## Test cases
View source: title ≤ 60 chars with APA/MLA/Chicago/Harvard; meta 140–160; canonical unchanged.
