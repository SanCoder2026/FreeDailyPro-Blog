Sent: 2026-11-20 08:40 ET

# Desk findings: Grammar Checker (FDP-13)

- **Written:** 2026-11-19 (box `date`, ET). Sources: curl of the tool page and headers (`html/tool.html`, `html/headers-tool.txt`), 9 hreflang locales and /ar, the blog, the GrammarChecker chunk (`js/GrammarChecker-C8oR9yRI.js`, prettified `js/gc.pretty.js`), the site dictionary (`js/dict/`), WebSearch.
- **Test plan (quoted from TEST-ORDER.md, not re-verified):** row 13, Pro, Text & Writing, "test-plan rank 11: 8,397 impr pos 21", cluster C47. **GSC data is not available.**

## Page and SEO
- Title "Grammar & Spell Checker Online | FreeDailyPro"; H1 "Grammar Checker"; meta: "Check grammar and spelling online: fixes typos, don't/dont, their/they're, its/it's and spacing, lists doubtful cases as suggestions. Text stays local." Self-canonical, 200; in the sitemap (tool and blog).
- JSON-LD: FAQPage with **one** question, which claims the tool catches "misplaced commas, subject-verb mismatches" (see live findings §4). Offer 4.99. og image is the site default.
- The visible "Common questions" section is not mirrored in a fuller FAQPage; position 21 on 8,397 impressions (test plan) suggests the page ranks for the head term but is not competitive; a fuller, accurate FAQ and a sample "before/after" would help.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko, id all return 200 with English content under a non-English `<html lang>` (curl and matrix); /ar returns 404 (no hreflang for ar, so that is consistent). The tool is English-only by design ("English only"), so these locale URLs are English duplicates with a wrong `lang`.

## Engine (code review, `js/gc.pretty.js`)
- Rule-based: regex rules + nspell with the Hunspell en_US dictionary loaded from `/dict/`. Not AI (as stated).
- Masks URLs, e-mails, file names, version numbers before rules (confirmed: puma.com, no-reply@email-in.puma.com, index.html, ASP.NET untouched).
- The harmful rules are listed with line numbers in `live-functional-findings.md` §2.
- Suggestions block (L636–660) is the right home for the risky rules: the code already has a suggestion channel for than/then, fewer/less and agreement.

## Blog (/blog/grammar-checker, Oct 17, 2026)
- "stay aware of 10 trial usages a day" (L91 of `html/blog.txt`): matches neither the live tool (ungated) nor /terms. Policy question first; wording follows the decision.
- "flags two subject-verb issues and one missing article" (L62) and "flags one article error and one comma splice" (L97): the tool has no missing-article or comma-splice rule; agreement handling is the harmful part. Overclaims.
- Good advice otherwise (freeze content, check names and numbers by hand, don't accept blindly). Ironically the blog warns about "fixing" product codenames and names, which the tool does at sentence start.
- Uses "professional tools, premium applications" wording correctly.

## Competitors (WebSearch, 2026-11-19)
- Scribbr's 20-error test: QuillBot 20/20, LanguageTool 19/20, Grammarly free 11/20; reviewers also deduct for **new errors introduced**, the exact failure here. (scribbr.com/language-rules/best-grammar-checker/)
- LanguageTool and QuillBot run free without an account; LanguageTool shows each issue with a one-line explanation and lets the user accept each one (two clicks), which is the review model this page's copy describes but the tool doesn't implement.
- An aialleyway.com 2026 test weights "no false flags on a clean paragraph" as heavily as catch rate; here 23 of 28 clean sentences were altered.
- Differentiator this tool can honestly claim: fully local (text stays in the browser), instant, no sign-up, URL/e-mail/file-name safe.
- Brand query "freedailypro grammar checker" (WebSearch, 2026-11-19): the tool page is result 1 and the blog result 5. Result 2 is a RapidAPI listing of the same checker ("Text and Developer Utilities API", Grammar checker) whose description promises the same agreement and their/its/your rules and "leaves everything else alone". The API was **not tested** (out of scope: no API/MCP testing); if it shares this engine, the same false rewrites would reach API users. Flag for the owner, not verified.

## Cluster C47 / duplicates
- Test plan cluster C47 lists paraphraser, reading-level, text-cleaner, find-replace, case-converter, ai-prompt-optimizer; DUPLICATES tag "absorbable". None of those does grammar/spelling correction, so no duplicate of this tool's function was found; keep as its own tool.
