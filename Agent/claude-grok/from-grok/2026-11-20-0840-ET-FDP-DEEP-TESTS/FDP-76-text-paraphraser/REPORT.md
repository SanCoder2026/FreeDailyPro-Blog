Sent: 2026-11-21 17:25 ET

# FDP-76 Paraphraser / Rewriter (text-paraphraser): deep test report for Claude

- **Written:** 2026-11-21 17:40 EST (box `date`, ET). Testing ran 2026-11-21 17:13–17:36 EST.
- **Tool:** https://www.freedailypro.com/tool/text-paraphraser
  - TEST-ORDER row 76: **Pro**, Text & Writing. Plan note "test-plan (unranked): GSC top-50 SEO backfill 15". Duplicate group **C47** (Text clean-up and rewriting: grammar-checker #13, find-replace #42, case-converter #60, reading-level-checker, text-cleaner, ai-prompt-optimizer).
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, every device). JSON-LD Offer $4.99. `fdp-usage-v1` exists (tier professional, 10/day).
  - Video 4NQaC_Th79E (embedded, 94 s, uploaded 2026-09-24). Blog /blog/text-paraphraser "Tighten Your Own Draft With Light, Medium and Strong Rewrites" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (`TextParaphraser-BDp9aeKR.js`, pretty copy `TP.pretty.js`):**
  - Textarea, Strength Light / Medium / Strong, Paraphrase, Rewrite again, click-to-restore highlights, Copy. All rule-based in the browser: 30 phrase rules (Light), +24 word rules (Medium), + sentence openers, contraction flips and a "because" reorder (Strong).
  - Each replacement is wrapped in private-use marker characters: `U+E000 new U+E001 U+E002 original U+E003`. Later rules skip a match only if it contains U+E000 or U+E001, so **they can still rewrite the stored original between U+E002 and U+E003**. That nesting is the root of the main bug.
  - Paraphrase calls `logUsageNow("generate")` and shows "Nothing was paraphrased because today's trial uses are used up" if it returns false. No-change and non-English inputs return early with "no trial use was counted". Rewrite again, restore and Copy don't call it (Copy goes through `gateShare`).
  - In ToolPage, `logUsageNow` returns **true without charging when the tool isn't `known`** to the usage system. That fits with the missing strip.
- **Testers:**
  - Desk: page copy (8 FAQs, how-to, when / when not, tips, limitations, privacy), JSON-LD, blog, JS.
  - **Offline harness** (`scripts/px76-harness.js`): the tool's rule engine copied verbatim from the bundle, run under node on 30 cases + the blog's sample paragraph (`evidence/harness/`). Every case also checked live matches it exactly.
  - Playwright, guest:
    - `zero.json`: Chromium at 10/10. Paraphrase ×2, no-change, French, Rewrite again, Copy (clipboard read back).
    - `left-firefox.json`: Firefox at 0/10 (try 6 of 30). 15 Paraphrase presses on 10 different texts, Rewrite again ×2, Copy ×2, strength switch, restore click, then a reload + 2 more. All `usage.log` POSTs were logged and checked for the text.
    - `clip.json`: Chromium. The bug cases were copied and the clipboard read back for private-use characters. Tooltips and the restore click were checked.
    - The Chromium uses-left search was stopped (no charge was observed anywhere, so it added nothing).
  - Video frame sheet + frames; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. There's no Drive, cloud, account feature or paid path on this page.
- **RERUN-AFTER-RESET:** none. Behaviour was observed both at 10/10 and at 0/10.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to someone polishing their own email or report who will paste the result straight into a message, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20; #68 and #74 filed the same way). Per-page-load charging is P1. A full-quality result at 0 is a pending owner question (Nov 21, corrected 1:19 PM).

**P0:** none found.

**P1 — the output corrupts text and can invert its meaning (nested rule rewrite):**
- "Don't forget to call me." on **Medium** → **"Remember to to call me."** On **Strong** → **"Remember to forget to call me. I cannot wait."** "Please don't forget the keys." on Strong → "Please remember forget the keys." (harness H07/H08/H28; live L05/L07, C01).
  - Cause: "don't forget to" → "Remember to" is applied first. The later rule "don't forget" (Light list), and on Strong the "don't → do not" flip, then match **inside the stored original** and nest a second marker. The parser (`/\uE000([^\uE001]*)\uE001\uE002([^\uE003]*)\uE003/`) then closes early and spills the rest of the original into the output.
- Strong with sentence openers: "But we stayed. So we won. Also, it rained." → **"That said,But we stayed. As a result, we won. In addition,, it rained."** ("However," inserted for "But" is itself rewritten by the Medium "however" rule.) The tooltips read "Original: However" and "Original: As wellAlso" (C02).
- **Invisible private-use characters reach the clipboard**: Copy of the Medium case contains U+E003; the Strong case contains U+E000 U+E001 U+E002 U+E003 U+E003 (`clip.json`). The output box draws a visible box glyph (`C01-dontforget-hover.png`). Pasted into an email, CMS or code, these are hidden junk.
- Clicking the highlight to restore gives **"RememberDon't forget to call me."** with four marker characters left (C03).
- "Don't forget" is one of the most common phrases in the emails this tool targets. The page promises "so the grammar stays intact" and "hand-checked" swaps.
- Fix direction: apply each rule list to the visible text only (tokenise segments, or skip any match that falls inside a U+E002…U+E003 span), and strip U+E000–U+E003 before Copy and before render.

**Owner question:**
- **The tool takes no trial use at all**, though the page, the blog and the code all say Paraphrase counts.
  - At 10/10 (Chromium): full results, Rewrite again and Copy, no dialog, 0 `usage.log` POSTs.
  - At 0/10 (Firefox): 15 Paraphrase presses on 10 texts, plus a reload → still 0/10, 0 POSTs.
  - The code calls `logUsageNow("generate")` and has a "today's trial uses are used up" message. The blog says "Pressing Paraphrase counts as one of your 10 trial uses". The FAQ and Privacy text say "a plain usage tick … is recorded". None of this happens, because the tool isn't `known` (no strip or Quick Buy rendered).
  - It's not on the uncounted-on-purpose list. Decide: register it so Paraphrase is counted (then Copy too, per policy), or list it as uncounted and update the FAQ, Privacy text, blog and JSON-LD Offer.

**P2 — where to look:**
- **Grammar breaks on the most common swaps:** articles aren't adjusted. "a problem" → "a issue", "a method" → "a approach", "an idea" → "an concept", "an important" → "an significant", "an easy" → "an straightforward", "a goal" → "a aim / a objective", "a huge problem" → "a enormous issue" (harness H01–H03, H30; live L01). Also "get started on" → "begin on", "a few left" → "a handful of left", "However hard we try" → "That said hard we try", "I also want" → "I as well want", "Main Street" → "Primary Street". The page says "so the grammar stays intact".
- **The blog presents a bug as expected behaviour:** it attributes "In addition,," to "the replacement carried its own comma" and suggests Find & Replace to fix double commas. It's the nested-rule bug above. The blog's counts (8 / 11 / 12 changes) are accurate.
- **Video 4NQaC_Th79E is out of date:** the old UI has no strength buttons, highlights, Rewrite again or restore. It shows a "Free: 10 uses/day -- 9 remaining today" strip and Quick Buy (neither appears now; "Free" wording too). The old About text says it helps with rephrasing a sentence "too similar to a source you're referencing", which the current "When not to use it" (don't disguise someone else's writing) contradicts. The title says "Free Step-by-Step Walkthrough". No personal tabs seen.
- **Rewrite again rarely changes anything:** most rules have one alternative. In live runs, Rewrite again on the article sentence returned the identical text (L02, L03). Strong's "because" reorder fires only on alternate seeds. The FAQ explains this, but against free AI paraphrasers the "wow" is thin. See check 2 and 19.

**P3:**
- Locale pages (es…id) are served for an English-only tool. Only the navigation is translated; the controls and copy are English, which is arguably right for an English tool, but then hreflang alternates add little.
- The non-English notice toast stacks with the previous "No safe changes" toast (Z03, L12).
- iPhone SE 9 px overflow (329/320, header button); ja desktop overflows a few px. axe desktop: label-content-name-mismatch (serious, `.right-2`) + region (moderate). Pixel 7: color-contrast (serious, `.text-muted-foreground/50`).

## Intent

Someone wants a quick, controllable polish of their own email or report: see every change, keep or undo it, paste it out. Highlighting, restore, no-change and non-English handling all work, and the text never leaves the browser. But a very common phrase ("Don't forget to…") comes out wrong or inverted, hidden characters ride along on Copy, and simple article errors ("a issue") undercut the "grammar stays intact" promise. Those would make a user distrust the tool at first use. Separately, the tool is not counted at all.

## What works

- Phrase swaps on clean input: "Please send the report prior to Friday in the event that it is ready." → "…before Friday if it is ready." "Due to the fact that it rained" → "Because it rained". "Thank you very much for" → "Thank you so much for". Caps preserved ("IN ORDER TO WIN" → "TO WIN").
- Strong "because" reorder: "We left early because the road was icy." → "Because the road was icy, we left early." (seed 0).
- Contraction flips both ways ("We do not know. I will call you." → "We don't know. I'll call you.").
- Highlights + hover original + click-to-restore (4 → 3 marks, original words back, L14). The stale notice appears when the strength or text changes.
- No-change text → "No safe changes found … so no trial use was counted". French and Hindi → "This looks like it is not English…". Mixed lines pass non-Latin lines through.
- Privacy: no text in any network request (0 POSTs at all).

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | **FAIL (P1)** | Common phrase corrupted/inverted; hidden chars on Copy. |
| 2 | Completeness | PARTIAL | ~54 fixed rules; Rewrite again mostly identical; far below AI paraphrasers (documented). |
| 3 | Ease of use | PASS | Highlights, restore, clear notices. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | N/A | No strip, prices or Quick Buy on the page. |
| 6 | Information correct | FAIL | "Grammar stays intact"; "usage tick is recorded"; blog says Paraphrase counts. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS | Title "Paraphrasing Tool: Rewrite Sentences" (58); meta ~160. |
| 9 | Blog | PARTIAL | Accurate counts; mislabels the "In addition,," bug as expected. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PARTIAL | Privacy/usage-tick claim false; otherwise accurate. |
| 12 | Video shows current capability | FAIL | Old UI, "Free" strip, "too similar to a source" copy. |
| 13 | Storage | N/A | None. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Copy only. |
| 16 | Usage count | **OWNER QUESTION** | Never counts (0 POSTs, 15 presses with uses + cap runs). |
| 17 | Categorization in section | PASS | Text & Writing. |
| 18 | Correct section of site | PASS | Related: Word Counter, Case Converter, Grammar Checker; next step Reading Level Checker. |
| 19 | AI need and demand | PARTIAL | "paraphrasing tool" is high demand but met by AI rewriters; this rule set is a light polish. |
| 20 | Merge better? | Maybe | C47: could be a "Polish" mode beside Grammar Checker / Text Cleaner. |
| 21 | Remove? | No | GSC top-50 backfill; fix the bug first. |
| 22 | Duplicates | C47 group | Overlaps Grammar Checker (#13) and Text Cleaner as "clean-up"; not a strict duplicate. |

## After fixes, rerun

- `node scripts/px76-harness.js` (H07, H08, H12, H28 must have no `[PUA LEFT]` and read correctly; H01–H03 articles) and `px76-live.js clip` (clipCodes empty).
- `px76-live.js zero` and `left firefox` if the owner decides Paraphrase should count.
