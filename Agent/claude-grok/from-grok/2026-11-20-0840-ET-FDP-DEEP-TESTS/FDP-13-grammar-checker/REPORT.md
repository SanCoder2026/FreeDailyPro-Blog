Sent: 2026-11-20 08:40 ET

# FDP-13 Grammar Checker (grammar-checker): deep test report for Claude

- **Written:** 2026-11-19 14:25:07 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/grammar-checker. Row 13 of TEST-ORDER.md (Pro, Text & Writing; test-plan rank 11: "8,397 impr pos 21", cluster C47, quoted from TEST-ORDER and not re-verified). **GSC data is not available.**
- **Classification:** Professional Tool, Text & Writing. **Takes no trial use in practice:** Check Grammar and Copy both work at 0 remaining with no dialog and no count change. Under the owner policy dated Oct 30 (copy and results count in all tools) this is a **POLICY QUESTION for Santosh**, not a PASS (see check 16).
- **Testers:**
  - **Desk review:** curl of the tool, 9 locales and /ar, the blog; the GrammarChecker chunk prettified (`evidence/js/gc.pretty.js`) and the site's Hunspell dictionary; WebSearch for competitors and the brand query.
  - **Offline harness:** the site's own rule engine (`evidence/js/me-engine.js`, extracted verbatim) run in Node with nspell and the site dictionary; no browser, no trial use.
  - **YouTube video:** metadata, 31 frames, contact sheets, crops.
  - **Headless Playwright:** probe, 28 correct-sentence cases + 15 error cases, UK variant, Copy at 0, a 10,801-word paste, keyboard/axe/phones, and the matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** none needed. **No URLs were blocked by sign-in.**
- **Nothing pending:** the gate was observed at 0 remaining. No RERUN-AFTER-RESET row was added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real component, restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **GrammarChecker rule engine** (`me()` in the GrammarChecker chunk; line numbers below refer to `evidence/js/gc.pretty.js`): the auto-apply rule list `U` (L487–560), the he/she/it agreement rule (L466–476), sentence-start spell replacement (L587–608), standalone `i` (L619–621), the "me and him" suggestion (L636–640).
- **The page copy** (intro "what", Details sections, FAQPage JSON-LD, meta) and the blog.
- **The output textarea** (label, aria-live) and the trial-use wiring (`gateShare` on Copy, `logUsageNow()` on Check), pending the policy decision.

After you ship, rerun `test-cases.md` (GC-01…GC-24) and `node scripts/gc-offline.js` (no browser, instant).

## Intent

Someone pastes an email or post and copies the "corrected" text straight back. The whole value of this tool is trust: what comes out must be at least as correct as what went in. Today the opposite often happens. Common, correct questions ("Does she have…", "Did it work…", "Can he go…") come back wrong, possessives turn into contractions, "a URL" becomes "an URL", and names at the start of a sentence are "corrected" (Santosh → Santos, Priya → Oriya). The page promises that anything uncertain is only suggested and nothing changes without review, so a user has no reason to double-check. That combination quietly sends errors into people's emails under their name.

## Why: what the evidence says

- **P0: harmful auto-fixes.** 23 of 28 correct sentences were changed into incorrect ones; live output = offline engine output. Causes are specific regexes without context guards (auxiliaries, possessive adjectives, initialisms, sentence-start names). A 10,801-word paste produced 1,801 fixes, 600 of them "she have → she has" after "Does". `evidence/findings/live-functional-findings.md` §2.
- **P1: copy contradicts behaviour.** "nothing is changed automatically without your review", "anything it is not sure about is listed as a suggestion", "doesn't catch subject-verb agreement" (it rewrites verbs), FAQ "misplaced commas" (no comma rule), "dictionary of common misspellings, not a complete dictionary" (it loads full en_US Hunspell). §4.
- **P1: wrong suggestion.** "Me and him was late." → suggests "him and I were" (should be "He and I were").
- **P1: trial-use policy question.** Ungated at 0 remaining; /terms says text utilities take no trial use; owner policy says copy and results count; the blog says "10 trial usages a day".
- **Recall is decent for a rule engine:** 10 of 15 real errors fixed; then/than and less/fewer are suggestions (as promised); whose/who's and "could care less" missed.
- **P2:** no label on the output textarea (axe critical) and no aria-live; 9 English locale copies under foreign `lang`; old video showing an old bug and personal bookmarks; blog overclaims (comma splice, missing article); single-question FAQPage.

## Outcomes we want

1. Correct English goes in, the same English comes out. Any rule that can be wrong in normal usage becomes a suggestion, not an edit.
2. Names, brands and technical terms are never silently replaced; unknown words are suggestions.
3. Every claim on the page, FAQ, meta, blog and video matches what the tool does.
4. The trial-use behaviour matches Santosh's decision, and /terms, the blog and the page say the same thing.
5. Screen-reader users hear the result; both textareas are labelled.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **FAIL** | CRITICAL | 23/28 correct sentences corrupted by auto-applied fixes; 10/15 real errors fixed. `findings/live-functional-findings.md`, `json/live-cases.json`, `json/offline-auto.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Covers contractions, a/an, doubled words, spacing, common misspellings, UK/US. No per-issue accept/ignore (LanguageTool, QuillBot have it), no explanations panel per change, misses whose/who's. Competitor tests penalise introduced errors. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | HIGH | One box, one button, instant, Copy. But the user can't see what changed inline or reject a change; on a 568 px phone the output starts at the fold. |
| 4 | Layout attractiveness | **PARTIAL** | LOW | Clean. iPhone SE: 9 px header overflow (site-wide) and a very pale "Auto-detect" select in WebKit; ad container between controls and output on mobile. `findings/devices-locales-findings.md` |
| 5 | Payment process | **N/A (policy question)** | — | No trial strip, no cap dialog at 0, no pass buttons on the page; nothing to pay through. Depends on check 16's decision. |
| 6 | Information correct | **FAIL** | HIGH | Intro/meta/Details/FAQ contradict behaviour and each other (auto-change vs review; agreement "not caught" vs rewritten; commas; dictionary). `findings/live-functional-findings.md` §4 |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in sitemap with the blog. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title/meta/H1. FAQPage has 1 question (and it overclaims); 9 English locale copies with foreign `lang`; default og image. Test plan pos 21 on 8,397 impressions. |
| 9 | Blog post | **PARTIAL** | MEDIUM | /blog/grammar-checker (Oct 17): sound workflow advice; overclaims "subject-verb issues", "missing article", "comma splice"; "10 trial usages a day" line. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | bMWHXqeygUg, 92 s, 2 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | Guide text is detailed but wrong in places (see 6); the FAQ has one question. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old UI (no UK/US select, "10 free uses daily" badge), demo shows the old "Puma. Com" domain bug, personal bookmarks bar visible, ~30 s outro, "Free" wording. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Local processing as stated; no account storage. Filtered network list showed no request carrying the text (not a full network audit). |
| 14 | Sharing | **N/A** | — | No share-result feature (only "Share this tool"); none promised. |
| 15 | Downloads | **N/A** | — | Copy only; no download promised. Copy works ("Copied!"). |
| 16 | Usage count | **POLICY QUESTION for Santosh (not PASS)** | HIGH | Check and Copy at 0 remaining: no dialog, count 10 → 10 (observed 14:13–14:15 EST). Consistent with /terms ("text utilities take no trial use"), contrary to the Oct 30 owner policy (copy and results count in all tools); blog says "10 trial usages a day". Counters are display-only. Starting counts: probe/cases/kbd desktop at 10 used; kbd Pixel 7 at 0. |
| 17 | Categorization | **PASS** | — | Text & Writing. |
| 18 | Location in site | **PASS** | — | Breadcrumb, category, Book Writing Toolbox link, blog. |
| 19 | AI need / demand | **PARTIAL** | MEDIUM | High demand (rank 11). A rule engine can be safe if conservative; the current aggressive auto-apply is the problem, not the lack of AI. An optional AI pass could be a Premium Application later, but not as a fix for this. |
| 20 | Merge? | **N/A: keep** | — | No other C47 tool does grammar/spelling. |
| 21 | Remove? | **N/A: keep, fix** | — | High demand; fix the auto-apply rules first. |
| 22 | Duplicates | **PASS** | — | No duplicate tool found; same checker is listed as an API on RapidAPI (not tested). |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`. All 10 profiles 200; input and button above the fold everywhere; output just below the fold on 568–584 px phones. Locales are English copies. Geo contexts identical (en, no prices).

**Ads:** keep them in reserved fixed-height slots after the results block; never between the Check button and the corrected text.

## Suggested direction (interpret freely)

1. **P0: make the engine conservative.**
   - Agreement (L466–476) and have→has (L505–509): skip when the preceding word is an auxiliary/modal (do/does/did/can/could/will/would/shall/should/may/might/must/let/make/help) or a perception verb + object (see/watch/hear/feel/saw/watched); or move both rules to suggestions.
   - their/its/your → contraction (L516, L526, L531): auto-apply only when followed by a verb form that cannot follow a possessive (e.g. "their going to", "its been", "your welcome." at clause end); everything else → suggestion. Remove adjectives (late, very, hard, right, all, doing, being) from the auto lists.
   - a→an (L556): skip all-caps tokens and single letters (or use a small consonant-sound list: URL, USB, UI, UX, UN, UK, US, EU…), mirroring the existing `[A-Z]{2}` guard in the an→a rule.
   - Spelling (L587–608): never auto-replace a capitalised word, even at sentence start; unknown words → suggestion. Consider a tech-word allowlist (webhook, kubectl, config…).
   - Repeated word (L439): skip capitalised repeats (Bora Bora). Standalone `i` (L619): skip "(i)" and roman-numeral lists.
   - Add the 28 FP sentences as a regression test; the target is 0 changes.
2. **P1: rewrite the copy to match** (after 1): what is auto-fixed, what is suggested, what isn't covered; drop "nothing is changed automatically" unless you add per-change accept/ignore; fix the FAQ (no commas claim), dictionary wording, meta.
3. **P1: "Me and him was" suggestion** → "He and I were" (map him→he, her→she, them→they).
4. **P1: policy question:** Santosh decides whether Check/Copy take trial uses; then align /terms, the blog line and the page.
5. **P2:** label both textareas and add `role="status"`/aria-live for "N fixes made"; scroll or focus to the output on small screens; inline diff highlighting with per-change undo would be a strong differentiator; expand the FAQPage with accurate Q&As; re-record the video in a clean profile with the current UI; fix the blog overclaims; translate or de-list the 9 locale alternates.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Don't change the trial-use behaviour until Santosh answers the policy question.
- Counters are display-only evidence.

## Process

Inspect GrammarChecker `me()` → restate → propose → implement → verify with `scripts/gc-offline.js` (engine only), `scripts/gc-live.js` (live page), `scripts/gc-kbd.js` (a11y/phones) and `test-cases.md`.
