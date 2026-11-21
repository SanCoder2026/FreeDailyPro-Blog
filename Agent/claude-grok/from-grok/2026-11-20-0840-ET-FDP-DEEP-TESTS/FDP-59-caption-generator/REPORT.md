Sent: 2026-11-21 12:34 ET

# FDP-59 Social Caption Generator (caption-generator): deep test report for Claude

- **Written:** 2026-11-21 12:14 EST; **-v2 correction 2026-11-21 12:15 EST** (P1 usage items moved to Owner questions) (box `date`, ET). Testing ran 2026-11-21 11:52–12:12 EST.
- **Tool:** https://www.freedailypro.com/tool/caption-generator
  - TEST-ORDER row 59: **Professional Tool**, Design & Marketing. Plan note "test-plan (unranked): L-243 live ApyHub API" — the live tool makes **no** external API call; captions come from fixed templates in the page JS.
  - Site-map tag `absorbable:text`. Duplicate group C42 (social-media-formatter, social-carousel-maker, hashtag-generator, yt-thumbnail, thumbnail-gen, ai-social-publisher).
  - Video OGI6yqaI1oU (embedded, 106 s, 2026-09-24). Blog /blog/caption-generator (Oct 17, 2026).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** topic + optional detail + platform (Instagram/TikTok/X/LinkedIn) + tone (Fun/Professional/Bold/Gen-Z) + optional call to action → three drafts from 3 fixed frames per platform×tone, with a character count and a Copy button. Hashtags are built from the topic words (`textUtils` `h()`), 5/4/3/0 for IG/TikTok/LinkedIn/X. Deterministic.
- **Testers:**
  - Desk: copy (6 FAQs, How to, Limitations, Privacy), JSON-LD, blog, JS (`CaptionGenerator-C4DMCLiD.js`, `textUtils-DaDvKhN-.js`, `ToolPage-DwLoDncN.js`).
  - Playwright: `probe.json` (Chromium, 10/10 context: Generate + 2 Copies), `cases.json` (Chromium context at 0/10: 14 input cases in one load), `left-firefox.json` (Firefox context at 0/10 after 17 tries: 6 generations, 4 copies, 1 reload).
  - `px59-expected.mjs` recomputes every case from the site's own template code: **all 14 cases match live output and character counts** (`expected-compare.json`).
  - Video frame sheet and crops reviewed. Matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only; no sign-in, card or email; no ad clicks; no site or repo changes.
- **Sign-in (untested):** none needed. No Drive, cloud or account feature on this tool (verified live). No pass/Quick Buy entry point on the page (verified live), so the payment flow can't be reached from here.
- **RERUN-AFTER-RESET:** none. Both behaviours (with uses left and at the cap) were observed today.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context (Nov 20):** copy and results count as trial uses. Only Unit Converter, Grammar Checker and Word Counter are uncounted on purpose. A tool that takes no trial use and isn't one of those three is a **policy question held for Santosh, not a P1 fix order** (corrected in -v2).

**Where to look:**
- **The tool never charges and never stops (owner policy question, held for Santosh; see Owner questions 1–2). Don't change charging until he decides.**
  - At 10/10 (probe.json, Chromium): Generate gave all three drafts, both Copy clicks gave "Copied!" and the right text on the clipboard; no cap dialog, no `usage.log` POST, count stayed 10/10.
  - With uses left: cases.json (Chromium, 14 generations) stayed 0/10 with no `usage.log` POST; left-firefox.json (6 generations, 4 copies, a reload) stayed 0/10, no `usage.log` POST.
  - The page has **no trial strip and no Quick Buy** (verified live in both states), so there is also no route to a pass from this tool.
  - The Generate handler awaits `logUsageNow()` and Copy goes through `useShareGate.gateShare`, but both returned "allowed" without logging. Likely tied to the `absorbable` tag or the usage "known" check in ToolPage `nr()`/`la()`; please confirm.
  - Copy contradicts the behaviour: the blog says "Pressing it counts as one of your 10 trial usages for the day"; Privacy says the site "may log that the tool was used… to count daily uses"; SoftwareApplication JSON-LD shows a 4.99 USD offer.
  - Decide: (a) counted like other Professional Tools (charge on Generate and Copy, show the strip, cap dialog at 10/10), or (b) uncounted on purpose (add to the owner's uncounted list and drop the "counts as a trial usage" copy).
- **"AI" positioning on a template tool.** The thumbnail says "AI CAPTIONS"; the VideoObject and the blog's embedded clip are titled "How to Generate AI Social Media Captions"; the video shows the old subtitle "AI-powered social media captions". The FAQ says "Nothing is composed from scratch." Retitle the video/JSON-LD, or link users who want AI drafts to **AI Social Publisher** (C42, AI tier) — a natural paid upsell that this page doesn't offer today.
- **Hindi (and other Indic) hashtags are broken:** "दिवाली सेल शुरू" gives `#दवलसलशर #दव #वल #लस #सल` (C14, screenshot). `h()` matches `[\p{L}\p{N}]+`, so combining vowel signs (`\p{M}`) split words. Add `\p{M}` to the word pattern. The site has a /hi locale.
- **Punctuation-only topic:** "!!!" enables Generate and yields "Today's little joy:  ✨" (C08). Treat a topic with no letters/digits as empty.
- **Filler hashtags not disclosed:** after topic words, `h()` pads with first-word+Tips/Life/Daily… ("#BigTips #BigLife", C07). The FAQ says hashtags "are cut from the words in your topic". Disclose or drop the padding for this tool.
- **Blog accuracy:** the X example claims "#OatMilkLatteNowMenu #Oat"; X drafts never have hashtags (C03, FAQ). "Whatever you type is kept exactly as written" — trailing .!?… are stripped (C07). "The rest of the family lives in the SEO tools category" — the tool is in Design & Marketing.
- **Video (OGI6yqaI1oU) is outdated:** old UI (breadcrumb "SEO Tools", "10 free uses daily" and "Pro" badges, no detail field, fixed #fyp #viral #trending tags), title "Free Step-by-Step Walkthrough", description "Try … free", "Free daily uses", tags "PDF tools" and "#SEOTools", end card "200+ Free Productivity Tools", ~35 s of 106 s is outro. The recording shows a personal browser bookmarks bar and taskbar.

**After you ship:**
- Rerun `px59-live.js left firefox` and `probe`: with policy (a), expect +1 per Generate and Copy and the cap dialog at 10/10.
- Rerun `cases` + `px59-expected.mjs` (C14 hashtags, C08 empty topic).

## Intent

A small-business owner or social media manager has a post idea and needs a first draft for each network fast, in the right tone, with sensible hashtags. They should leave with a usable draft — and, for a Professional Tool, see why a pass (or the AI tier) is worth it.

## What works (verified)

- **Templates as documented:** 14 cases match the site's own code exactly; detail on its own line with a full stop added; CTA lines per platform ("Link in bio.", "Follow for more.", "What do you think?", none on X); TikTok gets #fyp first; LinkedIn Gen-Z falls back to the Fun frames (disclosed).
- **X limit:** a 300-char topic shows "350 characters - over the 280 limit, shorten the topic" (C04); X drafts carry no hashtags.
- **Hashtags:** CamelCase from non-stopwords; C++ → Cplusplus, & → and, .NET → Dotnet (C11); accents kept (C10); 100-char cap (C13).
- **Safety:** `<img src=x onerror=alert(1)>` is shown as text; no dialog (C12).
- **Button:** disabled for an empty or spaces-only topic. Copy toast "Copied!"; clipboard text equals the draft.
- **Determinism:** the same inputs gave identical drafts (L03b), as the FAQ says.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Drafts, counts and Copy work. |
| 2 | Completeness | PARTIAL | Fixed 3 frames per pair; no emoji/length controls, no regenerate variety, no hashtag research. Competitors (Hootsuite, Later, Canva, Copy.ai caption tools) use AI. |
| 3 | Ease of use | PASS (minor) | Simple form; "!!!" topic gives empty drafts. |
| 4 | Layout | PASS (minor) | Clean on 10 devices; axe button-name critical on the two selects; locales mostly English. |
| 5 | Payment process | N/A — no entry point | No trial strip or Quick Buy on this page (verified live). |
| 6 | Information correct | PARTIAL | Blog "counts as one of your 10 trial usages" (never counted); blog X hashtags; "kept exactly as written"; "SEO tools category"; AI wording in video/JSON-LD. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default, in sitemap. |
| 8 | SEO | PARTIAL | Title 53; **meta 70 chars** ("Social media caption templates and ideas. Fast, right in your browser."); og-default; JSON-LD SoftwareApplication, VideoObject ("…AI…"), FAQPage (6), Breadcrumb. |
| 9 | Blog exists and accurate | PARTIAL | Exists, mostly accurate; 4 errors above. |
| 10 | YouTube video exists | PASS | OGI6yqaI1oU embedded. |
| 11 | FAQ and guide correct | PASS (minor) | Accurate except undisclosed filler hashtags; Privacy "count daily uses" vs no counting. |
| 12 | Video shows current capabilities | **FAIL (P2)** | Old UI, old category, fixed tags, "AI"/"free" wording. |
| 13 | Storage | N/A | None (verified live). |
| 14 | Sharing | PASS | Copy works; "Share this tool" present. |
| 15 | Downloads | N/A | Text only. |
| 16 | Usage count | Owner question | Takes no trial use at all (Generate and Copy, with uses left and at 10/10); no strip. Not on the exempt list, so held for Santosh. |
| 17 | Categorization in section | PASS | Design & Marketing. |
| 18 | Correct section of site | PASS (minor) | Breadcrumb Design & Marketing; blog still says SEO tools. |
| 19 | AI need/demand | High | Users expect AI captions; templates feel generic. Route to AI Social Publisher. |
| 20 | Merge better? | Consider | Absorbable: could become a free step of AI Social Publisher or merge with Hashtag Generator. |
| 21 | Remove? | No | Search demand for "caption generator" is high. |
| 22 | Duplicates | C42: keep, cross-link | Pairs with Hashtag Generator (linked as next step); add an AI Social Publisher link. |

## Owner questions

1. **Policy (held for Santosh):** caption-generator takes no trial use — Generate and Copy work with uses left (20 generations + 4 copies = 0 uses) and at 10/10, with no cap dialog and no `usage.log` POST. It isn't one of the three exempt tools. Count it, or add it to the exempt list? Either way the blog line "counts as one of your 10 trial usages" and the Privacy "count daily uses" line must match the decision.
2. **Follows from 1:** the page shows no trial strip or Quick Buy (verified live). If counted, show the standard strip; if exempt, consider an AI Social Publisher or pass CTA so the page still leads somewhere paid.
3. Keep "AI" in the video/JSON-LD titles, or reserve "AI" for AI Studio tools?
