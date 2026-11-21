Sent: 2026-11-21 11:32 ET

# FDP-56 Password Generator (password-generator): deep test report for Claude

- **Written:** 2026-11-21 10:58 EST (box `date`, ET). Testing ran 2026-11-21 10:39–10:55 EST.
- **Tool:** https://www.freedailypro.com/tool/password-generator
  - TEST-ORDER row 56: **Professional Tool**, Developer & Security Tools.
  - Plan note: "test-plan (unranked): SEO backfill 7 (GA top)". Duplicate group C50 (password-strength, hash-generator).
  - Video: LrkYLI-EnRs. Blog: /blog/password-generator-new-accounts (found in the sitemap, **not linked from the tool page**).
  - **GSC data is not available.** No API/MCP testing.
- **Offer on this page:** none visible. There is no trial strip, no Quick Buy and no prices on the page (verified live, all 10 locales and 6 geo contexts). The FAQ and How-to say "Seeing or copying a password never takes a trial use."
- **How it works:** in the browser, `crypto.getRandomValues` with rejection sampling (no modulo bias). The whole password is redrawn until every chosen group appears. Passphrases use the EFF large list (7,776 words, fetched from `/dict/eff-large-wordlist.txt`). Copy goes through `useShareGate.gateShare`.
- **Testers:**
  - Desk: copy (8 FAQs, How-to, Limitations, Privacy), JSON-LD, the blog, JS (`PasswordGenerator-BODnXk3M.js`, `useShareGate`, `useExportGate`, ToolPage).
  - Node: the site's own generator functions, copied verbatim, run 100,000 times. Entropy count checked by brute force (`px56-stats.js` → `desk/stats.json`).
  - Playwright probe in Chromium (clipboard read back) and Firefox: Generate ×5, Copy at the cap, How many 10, look-alike exclusion over 500 passwords, symbol-box edge cases, length 4/64, the one-type lock, Hide + Copy, passphrase variants.
  - Fresh contexts for a with-uses run: Firefox 8, WebKit 6 and Chromium 6 tries; all were at 10/10.
  - Video checked frame by frame. Matrix: 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
  - **Visual findings were checked against the screenshots.**
- **Constraints kept:** guest only, no sign-in, card or email; no ad clicks; no site or repo changes.
- **Sign-in:** nothing on this page needs sign-in. There is no Drive, cloud or download; verified live.
- **RERUN-AFTER-RESET:** one row. Copy and Generate with trial uses left were not observed, because every fresh context was at 10/10. Rerun `px56-live.js left` after midnight UTC (7:00 PM ET; tonight's 7:15 PM ET re-run, listed in /workspace/deep/RERUN-AFTER-RESET.md) to confirm Copy takes no use and sends no `usage.log`.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context:**
- Copy and results count as trial uses.
- Only Unit Converter, Grammar Checker and Word Counter are uncounted on purpose. Any other uncounted tool is a policy question.

**Where to look:**
1. **Uncounted tool (policy question).**
   - At 10/10, Copy worked in Chromium and Firefox. The clipboard held the exact password, the toast said "Copied!", there was no cap dialog and no `usage.log` POST.
   - Generate never charges. Ten results at a time can each be copied.
   - Copy is wired through `gateShare` (→ `useExportGate.checkExport`, which opens the cap dialog when `known && !paid` and the check returns "blocked"), but the live gate never fired. So the tool is effectively uncounted, which the FAQ states.
   - Password Generator is **not** in the Nov 20 list of intentionally uncounted tools, so the owner needs to decide.
   - If it should count, Copy at the cap is a **P1 gate gap** (full result at 0 trial uses).
2. **Privacy text contradicts the FAQ and the behaviour (P2).**
   - Privacy says: "A usage count is recorded when you copy a password, not when one is shown."
   - FAQ and How-to say: "Seeing or copying a password never takes a trial use."
   - Live at the cap, Copy sent no POST at all.
3. **Symbols box with only spaces (P2 bug).**
   - The alert says "The symbols box is empty, so the default symbols are used." That check uses `!N.trim()`.
   - Generation uses `symbolSet || default`, and "   " is truthy, so the space becomes the only symbol.
   - Ten of ten passwords contained a space (one leading: `" l6yUmYFA0zhsUY1"`, others trailing, invisible in the UI). Entropy drops to 93.4 bits.
   - Leading or trailing spaces are often trimmed by sign-up forms, which risks lockouts.
   - Fix: trim the set (and drop whitespace) before use, so the message matches what happens.
   - Evidence: `screens/cases/P07-*`, `json/probe.json` P07, `desk/stats.json`.
4. **Video is stale and uses "free" wording (P2).**
   - The title is "How to Use Password Generator – **Free** Step-by-Step Walkthrough". The description says "Try Password Generator free" and "Free daily uses".
   - Frames show the old UI: breadcrumb "Text & Writing", a "10 free uses daily" chip and a "Pro" chip, no Password/Passphrase toggle, no entropy maths, no look-alike or symbol options, and "Search 200+ tools".
   - The recording shows the creator's personal bookmarks bar.
   - The JSON-LD VideoObject name ("How to Generate Strong Secure Passwords Online") doesn't match the YouTube title.
5. **Guides point to unrelated posts (P2).** The "Guides and next steps" links are chmod and cURL posts. The matching post `/blog/password-generator-new-accounts` exists but isn't linked from the page.

**After you ship:** rerun `px56-live.js probe` (P07 should show no spaces) and `left` (Copy behaviour with uses left).

## Intent

Someone opening a new account or resetting a weak password wants a truly random secret that meets the site's rules, with a clear sense of how strong it is, without sending it anywhere. The page delivers that very well.

## What works (verified)

- **Randomness:**
  - Rejection sampling for the index (no modulo bias), then a whole-password redraw until every chosen group appears. That makes every qualifying password equally likely, as the FAQ says.
  - 100,000 site-function passwords: digits run at 13.2% against 11.4% under naive uniform. That is the expected effect of "must contain a digit" with uniform choice over qualifying passwords, not a bias bug. Shares within a group are even.
  - The UI line "no bias towards any character" is slightly loose wording (P3).
- **Entropy maths:**
  - The exact count matches brute force (length 4, digits + "!@": 10,720 = 10,720).
  - The displayed figures are right: 103.1 bits default; 101.1 with look-alikes off (81 chars); 22.0 at length 4 ("Weak"); 13.3 for 4 digits; 413.4 at 64.
  - Passphrase: 5 words + number = 73.6 (FAQ "about 74"); 3 words, no number = 38.8 "Weak"; 10 words + number = 139.2.
- **Exclude look-alikes:** 500 passwords and 8,000 characters contained none of `I l 1 O 0 o |`.
- **Controls:**
  - The last remaining type is locked: "(the last one is locked)" shows and the switch is disabled.
  - Length runs 4–64 and words 3–10. How many 1/3/5/10 gives distinct results.
  - Switching mode clears results, as the FAQ says.
  - Hide masks to at most 40 dots, and Copy still copies the real text.
- **Privacy:** the only network request from the tool was the word-list GET, with no POSTs (ad and analytics traffic excluded).
- **Devices and engines:** the page renders on all 10 devices. Chromium, Firefox and WebKit behave the same.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Page loads | PASS | 200; a password shows on load. |
| 2 | Core function | PASS | Passwords and passphrases correct; clipboard matches. |
| 3 | Edge cases | PARTIAL | A spaces-only symbol box injects spaces (P2). Letters typed into the symbol box are accepted as "symbols" (P3). |
| 4 | Error messages | PARTIAL | The empty-box alert is wrong for whitespace; the others are fine. |
| 5 | Mobile/devices | PASS (minor) | iPhone SE: the Feedback button covers "Hide" at the fold. ja desktop flagged overflowX (as on #55). |
| 6 | Information correct | PARTIAL | The Privacy "usage count when you copy" line contradicts the FAQ and the behaviour. |
| 7 | Indexing | PASS | Canonical is self; hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title "Generate a Secure Random Password Online \| FreeDailyPro"; meta from the registry; og-default; SoftwareApplication, VideoObject, FAQPage (8), Breadcrumb. |
| 9 | Blog exists and accurate | PARTIAL | The post exists and is generally accurate. It isn't linked from the tool, doesn't mention passphrase mode or the symbols box, and its closing sentence is garbled. |
| 10 | YouTube video exists | PASS | LrkYLI-EnRs embedded. |
| 11 | FAQ and guide correct | PASS (minor) | Numbers verified; the "empty box → default" claim fails for whitespace. |
| 12 | Video shows current capabilities | **FAIL (P2)** | Old UI, old category, "free" wording, personal bookmarks bar. |
| 13 | Storage | N/A | Nothing is stored (by design). |
| 14 | Sharing | N/A | No share or export of the result (verified live). |
| 15 | Downloads | N/A | Copy only. |
| 16 | Usage count | **Policy question** | Uncounted (Copy works at 10/10 with no POST); not on the Nov 20 exempt list. P1 if the owner wants it counted. |
| 17 | Categorization in section | PASS | Developer & Security Tools. |
| 18 | Correct section of site | PASS | The breadcrumb matches (the video still says Text & Writing). |
| 19 | AI need/demand | PASS (note) | The registry tag says "absorbable … a chat assistant does this for free", but a chat model can't give CSPRNG output with exact entropy. Keep. |
| 20 | Merge better? | No | Distinct job from password-strength. See 22. |
| 21 | Remove? | No | GA-top page (SEO backfill 7). |
| 22 | Duplicates | C50: keep both, fix the overlap | password-strength's own registry/meta description is "Generate strong passwords and check strength", which competes with this page. Rewrite that description to "check" only. The pages already cross-link. hash-generator is unrelated in job. |

## Owner questions

1. Should Password Generator stay uncounted (like Unit Converter, Grammar Checker and Word Counter)? If yes, delete the Privacy "usage count … when you copy" line. If no, Copy at the cap needs to open the cap dialog (P1).
2. The page shows no offer or trial strip at all. Is that intended for this tool?
