Sent: 2026-11-20 08:40 ET

# Live functional findings: Grammar Checker (FDP-13)

- **Run window:** 2026-11-19 14:13–14:17 EST (box `date`). Guest contexts only. Scripts: `scripts/gc-probe.js`, `scripts/gc-live.js`, `scripts/gc-kbd.js`; offline twin `scripts/gc-offline.js`.
- **Starting counts (display-only, localStorage `fdp-usage-v1`):** probe, cases and kbd desktop contexts loaded at 10 used of 10 (0 remaining); the kbd iPhone SE context at 10 used; the kbd Pixel 7 context at 0 used. Counts never moved during any run.

## 1. Gate / trial uses: POLICY QUESTION for Santosh (not PASS)

- At 0 remaining (10 of 10 used), **Check Grammar** ran with no dialog and the count stayed 10 (`json/probe.json`: start 10, afterCheck 10, dialog null).
- **Copy** at 0 remaining: toast "Copied!", clipboard held the corrected text, count still 10, no dialog (`json/live-cases.json` → `copy`).
- 28 + 15 Check runs plus a 10,801-word run in one context: count 10 → 10.
- No trial strip on the page (`strip: []`). The header badge reads "Runs on your device" (the video's "10 free uses daily" badge is gone).
- **Why this is a question, not a bug or a PASS:** the owner policy relayed on 2026-11-19 (dated Oct 30) says copy and results count as trial uses in all tools. This tool charges neither. /terms says text utilities take no trial use, and the page is consistent with /terms. The blog says "stay aware of 10 trial usages a day", which matches neither. Santosh to decide: gate Check/Copy (then update /terms) or keep it ungated (then fix the blog line and the policy note).
- Code: the component calls `gateShare` (useShareGate) on Copy and ToolPage `logUsageNow()` on Check, but neither charged in this state (display-only observation; no backend claim).

## 2. Core defect: auto-applied "fixes" rewrite correct English into wrong English (P0)

28 correct sentences (FP01–FP28). **23 of 28 were changed into errors** and the changes are applied to the output text, not offered as suggestions. Live results are identical to the offline harness (same engine).

| Case | Correct input | Live output |
|---|---|---|
| FP01 | Does she have time to meet tomorrow? | Does she **has** time… |
| FP02 | Did it work after the update? | Did it **works**… |
| FP03 | Can he go to the meeting on Friday? | Can he **goes**… |
| FP04 | Would it help if I sent the file again? | Would it **helps**… |
| FP05 | Why does she want to leave early? | Why does she **wants**… |
| FP20 | Should she have called first? | Should she **has** called… |
| FP21 | I watched it fly over the hill. | I watched it **flies**… |
| FP06 | …your right to vote matters. | …**you're** right to vote matters. |
| FP07 | Your welcome email is on its way. | **You're** welcome email… |
| FP08 | They visited their late father's house. | They visited **they're** late father's house. |
| FP19 / FP24 / FP25 | their doing / Their being late / gave their all | **they're** doing / **They're** being late / gave **they're** all |
| FP09 / FP22 | its very best engineer / Its hard shell | **it's** very best / **It's** hard shell |
| FP10 / FP18 | a URL / a USB / a UI kit | **an** URL / **an** USB / **an** UI kit |
| FP13 | plan a or plan b | plan **an** or plan b |
| FP12 | We flew to Bora Bora | We flew to **Bora** (repeated-word removal) |
| FP17 | Priya and Rahul reviewed the webhook payload. | **Oriya** and Rahul reviewed the **webfoot** payload. |
| FP26 | Santosh reviewed it. | **Santos** reviewed it. |
| FP27 | kubectl applies the config. The webhook fires. | Kubectl … The **webfoot** fires. |
| FP28 | (i) first item; (ii) second item. | **(I)** first item; (ii)… |

Unchanged (correct): FP11 researches, FP14 iPhone/eBay, FP15 ASP.NET, FP16 "that that", FP23 UK spellings.

**Root causes in `evidence/js/gc.pretty.js`:**
- L466–476: `(he|she|it) + base verb` → 3rd-person -s, with no check for a preceding auxiliary (does/did/can/will/would/should/could/may/might/must) or perception verbs (watch/see/hear + object + bare infinitive).
- L505–509: `(he|she|it) have` → `has`, same missing auxiliary check.
- L516, L526, L531: `their/its/your` + word lists that include adjectives/gerunds that are very often possessive (late, very, hard, right, welcome, doing, being, all).
- L556: a→an by first letter, so initialisms read with a consonant sound (URL, USB, UI, UX, UN…) and single letters ("plan a") are broken. L546 has an `[A-Z]{2}` guard for an→a but L556 has none.
- L589–590: words at sentence start are spellchecked and auto-replaced (capitalised words elsewhere are skipped), so names and tech terms that open a sentence get "corrected". Mid-sentence "webhook" also gets replaced because the dictionary lacks it and has one close suggestion.
- L439: repeated-word removal with no allowance for reduplicated names (e.g. "Bora Bora").
- L619–621: every standalone `i` becomes `I`, including roman numerals.

**Scale:** a 10,801-word paste ran in about 2.5 s with 1,801 fixes, of which 600 were the wrong "she have → she has" (the sample repeats "Does she have…"). `screens/live/result-long.jpg`.

## 3. Recall on real errors (FX01–FX15)

- **Fixed (10/15):** dont/their going/i (FX01), have went + He have (FX02), She go / every days (FX03), should of (FX04), Its a / your welcome (FX05), recieve/alot/informations (FX06), a apple / an banana (FX07), doubled words (FX09), alot/definately (FX14), spacing (FX15).
- **Suggestion only:** FX08 taller then → than; FX11 less → fewer (and "There is" is not flagged).
- **Wrong suggestion (P1):** FX10 "Me and him was late." → suggests **"him and I were"**; correct is "He and I were". Code L637–640 keeps the object pronoun.
- **Missed:** FX12 "Who's book" (whose), FX13 "could care less".

## 4. Copy claims vs behaviour (P1, wording and behaviour)

| Where | Claim | Observed |
|---|---|---|
| Intro ("What is this tool") and meta | "Anything it is not sure about is listed as a suggestion and left unchanged." / "lists doubtful cases as suggestions" | Unsure grammar rules are applied silently (section 2). |
| Details ("How it works") | "highlights each one … Review each flagged issue and accept or ignore it as you see fit; nothing is changed automatically without your review." | Fixes are applied to the output immediately; there is no accept/ignore control (live-verified: buttons list in `json/probe.json`). |
| Details ("limits") | "it doesn't catch subject-verb agreement … full grammar (like "This are a test") isn't detected at all" | It rewrites verbs for agreement (FX03 and the FP cases) and flags "he/she/it are" as a suggestion. |
| FAQPage (JSON-LD) | catches "misplaced commas, subject-verb mismatches" | No comma rule exists in the GrammarChecker component (`rg -i comma` finds none); agreement handling is partial and harmful. |
| Details | "dictionary of common misspellings, not … a complete dictionary" | It loads a full Hunspell en_US dictionary (`/dict/en_US.dic`, 551,762 bytes); tip text says "real English dictionary". The two sections contradict each other. |
| Intro | "Web addresses, e-mail addresses, file names and version numbers are never touched." | Holds in our checks (puma.com, no-reply@…, index.html, ASP.NET untouched). |

## 5. Other behaviour

- UK variant: "color/center/gray/organized" left as written with no note (`json/live-cases.json` → `uk`), consistent with "Correct UK and US spellings are never changed". Auto mode reported "US spelling (detected)" in the footer.
- Output is a read-only textarea with a Copy button; no download (none promised).
- Keyboard: textarea → Tab → Check Grammar → select → links; Enter on the button runs Check; focus stays on the button after Check; no aria-live/status region announces the result (`json/kbd.json`).
- Network (filtered list in `json/probe.json`): page/telemetry calls only (auth.me, usage.check, funnel.hit, insight.hit, GA, ads); no request carrying the text was seen in that filtered list. Not a full network audit.
