Sent: 2026-10-30 15:27 ET

# B-0294 Paper Format Checker: FAQ contradicts the checker, add an overall result line
Priority: P2 · Estimated effort: S · Report: QA-REPORT-156 · Source: live probe 2026-10-30 ~15:23-15:26 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A student uploads a paper and knows in five seconds whether it is ready to hand in, and trusts what the page says it checks.

## Why
GSC: 3 clicks / 174 impressions / 1.7% CTR / position 16.1.
Checked live (15:24 ET, fresh session, 9 trial uses left): apa-good-v2.docx against APA 7 → Margins 1.00" all sides; Page size 8.50×11.00; Font Times New Roman (100%); 12 pt (100%); double-spaced 100%; no extra paragraph space; 5 of 5 paragraphs 0.5" indent; page-number field found ✔ (matches L-217). Styles offered: APA 7th, MLA 9th, Chicago 17th.
Checked live: the results list has no overall verdict line (still as in L-217).
Contradiction (checked live): the FAQ, and the FAQPage JSON-LD, say "No — this checks your document's default formatting (margins and the Normal style's font, size, and spacing). If you've manually formatted individual paragraphs differently, those won't be caught". The note shown after a check says it reads "direct paragraph and run formatting … weighted by how much body text each setting covers", and results show percentages. One of them is wrong; the search snippet (seen in live search) repeats the FAQ version.
Competitors (live search): DocxShuttle lists each failing paragraph with expected vs actual and checks heading alignment/weight per APA level; Veermat and Mentur also check title page and references; Veermat fixes the .docx (paid download).
FreeDailyPro: per-paragraph location of failures and heading-level checks — unverified absence (the passing fixture produced no failures, so failure detail was not seen); admin to check with a failing file.
Title has "Free"; meta 122. /es title English → L-189. Ad text ("Get Writing Tools", "Stock Your Desk") → L-004.

## Who uses this
Students submitting APA, MLA or Chicago papers.

## Outcomes (ranked)
1. Correct the FAQ and JSON-LD to match what the checker reads.
2. An overall line ("8 of 8 checks pass" / "2 need fixing").
3. Snippet as below; /es localised.

## SEO
- Now: title "Check APA/MLA/Chicago Format Online - Free | FreeDailyPro" (57, has Free); meta 122; H1 "Paper Format Checker"
- Keywords: APA format checker, MLA format checker, check paper format, APA 7 margins font checker
- Suggested Title: "APA, MLA & Chicago Paper Format Checker | FreeDailyPro" (54)
- Suggested Meta: "Upload a .docx and check margins, page size, font, size, line spacing, indents and page numbers against APA 7, MLA 9 or Chicago 17, read as Word applies them." (158)
- Suggested H1: "APA, MLA & Chicago Paper Format Checker"
- FAQ: Does it read formatting I set by hand? · Is my file uploaded? · Which fonts does APA 7 allow? · Does it check references?

## Constraints
Keep the file local. Trial gating unchanged.

## Test cases
1. apa-good-v2.docx, APA → all 8 pass; overall line says 8 of 8 (regression + new line).
2. Body paragraphs set by hand to Arial 10 over a Times Normal style → font check fails with a percentage; FAQ wording agrees.
3. MLA on the same file → MLA header/heading expectations shown.
4. FAQ visible text equals FAQPage JSON-LD text.
5. Title ≤60, meta 140–160; 390 px no overflow.
