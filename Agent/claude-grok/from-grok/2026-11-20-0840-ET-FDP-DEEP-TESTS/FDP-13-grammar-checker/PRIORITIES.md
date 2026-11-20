Sent: 2026-11-20 08:40 ET

# Priorities: FDP-13 Grammar Checker

- **Written:** 2026-11-19 14:25 EST (box `date`, ET). Repro steps: REPRODUCE.md (R-numbers).

## P0
1. **Auto-applied fixes corrupt correct English** (R1–R4). 23 of 28 correct sentences changed: auxiliary questions ("Does she has", "Did it works", "Can he goes"), possessives → contractions ("you're right to vote", "they're late father's", "it's very best"), "an URL / an USB / an UI", "plan an or", "Bora Bora" → "Bora", sentence-start names and tech words replaced (Santosh → Santos, Priya → Oriya, webhook → webfoot), "(i)" → "(I)". Users copy the output straight into email. Outcome: correct text comes out unchanged; doubtful rules become suggestions.

## P1
2. **Page copy contradicts behaviour** (R5). "Nothing is changed automatically without your review", "anything it is not sure about is listed as a suggestion", "doesn't catch subject-verb agreement", FAQ "misplaced commas", "dictionary of common misspellings, not a complete dictionary". Fix after P0 so the copy describes the new behaviour.
3. **Trial-use POLICY QUESTION for Santosh** (R6). Check and Copy cost nothing at 0 remaining; /terms agrees; the Oct 30 owner policy says copy and results count in all tools; the blog says "10 trial usages a day". Decide, then align page, /terms and blog. Not a PASS.
4. **Wrong suggestion** (R7). "Me and him was late." → "consider 'him and I were'"; correct "He and I were".

## P2
5. Output textarea unlabeled (axe critical after Check); no aria-live for "N fixes made"; input has only a placeholder (R8).
6. Output starts at the fold on 568–584 px phones; no scroll/focus to result; ad container between controls and output on mobile (keep ads in reserved slots after results) (R8).
7. Video: old UI, shows the fixed "Puma. Com" bug, personal bookmarks bar, ~30 s outro, "Free" wording.
8. Blog: overclaims (two subject-verb issues, missing article, comma splice) and the trial-usage line.
9. FAQPage has one (overclaiming) question; 9 hreflang locales serve English under a foreign `lang`.
10. Misses: whose/who's, "could care less", "There is less people" (only less→fewer suggested).
11. iPhone SE: 9 px header overflow (site-wide); pale "Auto-detect" select text in WebKit.
12. Unverified: the RapidAPI "Grammar checker" listing may share this engine (API not tested by rule).
