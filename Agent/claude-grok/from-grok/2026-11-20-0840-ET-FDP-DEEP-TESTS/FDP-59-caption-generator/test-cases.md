Sent: 2026-11-21 12:15 ET

# FDP-59 test cases (guest). Inputs in evidence/testfiles/cases.json; expected values from px59-expected.mjs (site template code)

| ID | Input | Expected | Today |
|---|---|---|---|
| G01 | Generate with uses left | +1 use (owner rule) | **FAIL** (0) |
| G02 | Copy with uses left | +1 use (owner rule) | **FAIL** (0) |
| G03 | Generate at 10/10 | cap dialog, no drafts | **FAIL** (drafts shown) |
| G04 | Copy at 10/10 | cap dialog | **FAIL** (copied) |
| G05 | Trial strip / Quick Buy visible | shown | **FAIL** (absent) |
| G06 | Empty / spaces topic | button disabled | PASS |
| C01 | IG Fun CTA + detail (blog example) | blog draft 1 text | PASS |
| C02 | TikTok Gen-Z CTA | #fyp first, 4 tags | PASS |
| C03 | X Professional | no hashtags | PASS (blog wrong) |
| C04 | X Bold, 300-char topic | over-280 warning | PASS |
| C05 | LinkedIn Gen-Z | Fun frames fallback | PASS |
| C06 | LinkedIn Professional CTA + detail | 3 tags, "What do you think?" | PASS |
| C07 | "Big news!!!" | punctuation stripped | PASS (filler tags) |
| C08 | "!!!" | button disabled or message | **FAIL** (empty drafts) |
| C09 | Stopwords only | sensible tags | WEAK (#The #And) |
| C10 | Accents + Japanese detail | accents kept | PASS (Latin "." after Japanese) |
| C11 | C++ & .NET | Cplusplus/Dotnet | PASS |
| C12 | HTML injection | shown as text | PASS |
| C13 | 120-char word | tag cut at 100 | PASS |
| C14 | Hindi topic | whole-word tags | **FAIL** (split at vowel signs) |
