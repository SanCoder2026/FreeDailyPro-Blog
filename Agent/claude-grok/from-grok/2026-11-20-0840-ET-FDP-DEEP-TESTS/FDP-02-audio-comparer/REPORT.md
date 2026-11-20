Sent: 2026-11-20 08:40 ET

# FDP-02 Compare Two Audio Files (audio-comparer): deep test report for Claude

- **Written:** 2026-11-19 10:28:15 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/audio-comparer. The slug is from TEST-ORDER.md row 2 and tools.csv.
- **Classification:** Professional Tool, Audio Tools. It has 10 trial uses per day, a $1 day pass and a $4.99 monthly pass.
- **Testers:**
  - Desk review: curl, JS bundle read, blog, sitemap, competitors.
  - YouTube video: metadata, captions and 15 sampled frames. It was **not** watched with sound.
  - Headless Playwright:
    - 23 audio pairs made with ffmpeg
    - all result controls, with the downloaded WAV analysed by ffmpeg
    - trial-use counting in fresh contexts
    - paywall and Quick Buy paths
    - keyboard and axe on the result view
    - matrix: 10 device/browser profiles, 10 locales plus an /ar probe, 6 country contexts, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the email prompt and the Stripe page), no ad clicks, no API/MCP calls, no site or repo changes.
- **Not tested:** "Open from Google Drive". It needs a Google login, at https://www.freedailypro.com/tool/audio-comparer.
- **Box restore note:** the box was restored from a snapshot at about 10:10 EST. Runs affected by it were repeated. One observation (AC-19) could not be re-captured because every fresh context was capped afterwards; it is marked.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components (CompareAudio, its fingerprint/alignment and verdict logic, UsageAndUpgradeStrip, the usage router), then:
- Restate the problem.
- Challenge anything that looks wrong.
- Pick the fix that fits how FreeDailyPro has shipped similar work.

After you ship, rerun the test cases in this zip.

## Intent

People arrive asking "are these two recordings the same?". Typical cases: the same take, a re-encode, an edited version, or a clip from a longer file. They should:
1. Get a **trustworthy** verdict in seconds, where the big number agrees with the per-second strip, the waveforms and the length facts.
2. Feel "wow". The tool already found an offset, pinpointed "Differs at 0:05–0:07", and let them A/B the two files and download the difference.
3. Meet an honest trial-uses meter: 1 Compare = 1 trial use, and the full allowance for a new visitor. Heavy users (podcasters, editors, archivists, QA) should move to the $1 or $4.99 pass because they see the value, not because the meter misfired.

## Why: what the evidence says

**The engine and the result UI are strong:**
- Re-encodes (MP3/OGG/M4A/FLAC/48k stereo/−12 dB) gave 100%.
- A 0.5 s and a 20 s offset were found automatically.
- A 2-second edit scored 96.6% with "Differs at 0:05–0:07 in file 1.".
- The difference WAV's energy sits exactly at 5–7 s.
- The text summary is excellent.
- Bad files fail cleanly, without spending a use.

**What breaks trust:**
1. **The score disagrees with the evidence when lengths or halves differ.**
   - Half-identical audio scores **0.0% "Different audio"**.
   - A 12 s clip vs. a 72 s file that is 83% unrelated noise scores **100% "Same recording"**.
   - With the long file as file 1, 60 s of loud noise is drawn grey, which the legend calls "silence".
2. **The trial meter can misfire (display evidence from one busy box IP).**
   - One Compare took a fresh device from 10 to **0 remaining**.
   - Most fresh contexts loaded **already at 0**.
3. **The packaging describes the old tool.** The FAQ, Details, blog and video describe the old "equal segments" method and the old single-percentage UI, with "free" wording. The tool page doesn't link its own blog post.
4. **The locale pages are half-English,** and their titles and meta are English.

## Outcomes we want

- The percentage, verdict, strip and "Differs at" always tell the same story.
  - Partial matches read "Partly the same" with a proportional score.
  - Length mismatches state coverage, e.g. "file 1 matches 0:00–0:12 of file 2 (17%)".
  - Unmatched non-silent audio is never grey "silence".
- A new visitor sees "10 remaining today" and loses exactly 1 per Compare. Downloads, copy, share, play and failed decodes stay free (they already are).
- The FAQ, Details, blog and video match today's tool, use trial-uses wording, and cross-link (tool ↔ blog).
- The locale pages are translated end to end (title, meta, stepper, drop zones, button, accordions), or they leave hreflang until they are.
- 320 px phones have no sideways scroll, the result view passes contrast, and the Feedback button never overlaps an ad.

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 17 of 23 pairs correct, including offset detection and localisation of the edit. **FAIL:** AC-14 (half match → 0.0%) and AC-17/18/19 (clip vs. a mostly different longer file → 100% "Same recording"). PARTIAL: AC-08 and AC-16 (no length or coverage statement). `evidence/findings/live-functional-findings.md` §1, `evidence/screens/live/v14b-full.png`, `v21r2-full.png`, `v22r1-full.png` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | It has more than most free-tier rivals: strip, offset, A/B, loudness match, LUFS/peak table, diff WAV, text summary. Live-verified gaps: no clip-in-file coverage, no result share link, a 4-minute cap with no window choice, no spectrogram. Tempo tolerance is an *unverified absence*. `desk-findings.md` (Competitors) |
| 3 | Ease of use | **PARTIAL** | MEDIUM | A clear stepper and drop zones, keyboard-operable, with useful toasts. Problems: contradictory score vs. strip; the grey-cell legend is wrong for unmatched audio; the time axis reads "0:00 · 0:00 · 0:12"; the bad-file toast doesn't say which file; focus is lost after Compare. `live-functional-findings.md` §1–2 |
| 4 | Layout attractiveness | **PARTIAL** | LOW-MEDIUM | Clean dark result card with three waveforms. No ad overlaps the tool. CLS ≤ 0.018. Issues: iPhone SE overflows 329 > 320 px and the drop zones sit below the fold; Firefox 1440 has the Feedback FAB over the right-rail ad's button. `evidence/screens/devices/` |
| 5 | Payment process | **PARTIAL** | MEDIUM | The strip shows $1 / $4.99 Quick Buy from first paint, and the cap dialog is clear and on-brand. Day Pass opens an email-first dialog, while Monthly goes **straight** to checkout.stripe.com. The flows are inconsistent. (Stopped at both; nothing typed.) `evidence/screens/live/quickbuy-day.png`, `quickbuy-monthly.png`, `capped-paywall-dialog.png` |
| 6 | Information correct | **FAIL** | HIGH | FAQ #2 and "Details" describe "equal time segments… normalized time basis", which is the old algorithm. They contradict "How to use it" on the same page. Verdict text claims "Same recording" for mostly-different files. JSON-LD Offer 4.99 has no period. The cap dialog promises removing a mark this tool doesn't show. `desk-findings.md` (FAQ), `live-functional-findings.md` §5 |
| 7 | Indexing | **PASS** | — | 200, indexable, self canonical, in the sitemap (lastmod 2026-11-19) with a video block. WebSearch: tool first, blog third. Locale URLs are not in the sitemap. **GSC data not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Title (64), H1 and JSON-LD (5 blocks) are fine. Issues: meta is short (125) and generic; only 2 FAQ items; **every locale has an English title and meta**; generic og-default.png; video thumbnail `alt=""`; 3 different video titles; the tool page doesn't link /blog/audio-comparer. `desk-findings.md` (SEO) |
| 9 | Blog post | **FAIL** | MEDIUM | /blog/audio-comparer (200, Sept 18 2026) teaches the old segment method. It tells users to trim lead-in silence "so the segments line up", which the tool now does automatically. It omits the strip, waveforms, A/B and diff WAV, and isn't linked from the tool. |
| 10 | YouTube video exists | **PARTIAL** | LOW | KZVe2ILAUD4 (77 s, 14 views), embedded on the tool and blog. Tags are off-topic ("PDF tools"). `evidence/findings/video-findings.md` |
| 11 | FAQ / usage guide | **FAIL** | MEDIUM-HIGH | Two descriptions of the method conflict, and there are only 2 questions. Missing: different lengths, the 4-minute cap, strip colours, formats and size, the diff WAV, trial uses. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | It shows the old single "Similarity 62.8%" card, none of today's features, "free" wording throughout, and "200+ Free Productivity Tools". Frames: `evidence/video/` |
| 13 | Storage | **PASS** (by design) | — | Nothing persists. Reload and "Compare another pair" clear the inputs, localStorage holds only the usage key, and the input survives a blocked Compare. Consistent with "Files never stored". |
| 14 | Sharing | **PARTIAL** | LOW-MEDIUM | "Share this tool" copies the bare URL and doesn't spend a use. There is no result share. "Copy result summary" is a good text substitute. |
| 15 | Downloads | **PASS** | — | `audio-difference.wav`: PCM, 12.0 s, energy exactly at the edited 5–7 s. The 48 kHz export is explained by the page footnote. No trial use is spent. `evidence/json/usage-results.json` |
| 16 | Usage count | **FAIL (intermittent)** | HIGH | Correct path: Compare −1 and nothing else counts (run 1). **But** one Compare went 10 → 0 (run 2, v21r3) and 7 → 10 used (pairs 8 and 16). Fresh contexts loaded "0 remaining" (pool probe 4/4, matrix 7/10, geo 6/6). Display-only evidence, from one heavily used box IP. `live-functional-findings.md` §4 |
| 17 | Categorization | **PASS** | — | Audio Tools card, Professional Tool. |
| 18 | Location in site | **PASS** | — | Breadcrumb Home › Audio Tools › Compare Two Audio Files. Related tools: Transcribe, Extract Audio, Audio Trimmer. |
| 19 | AI need / demand | **PASS** (no AI needed for the core) | — | Deterministic DSP is right for trust. An optional "explain what changed" or speech-aware comparison could be a P2 Premium idea. Demand: 122 GSC clicks but 19 s engagement (test-plan, old). |
| 20 | Merge? | **PASS: keep standalone** | — | C24 (diff-checker, text-similarity, compare-pdf, audio-comparer) have different inputs. |
| 21 | Remove? | **N/A: keep** | — | Unique on the site, with search demand. |
| 22 | Duplicates | **PASS** | — | This is the only audio comparison tool. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10/10 profiles (iPhone SE and 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11, desktop Chrome 1366/1920, Firefox and WebKit 1440).
- No ad overlaps the tool controls.
- CLS ≤ 0.018.
- html `lang` is correct on 10 locales.
- The EU-timezone consent banner offers Accept all / Reject non-essential / Choose.
- Keyboard operation works end to end.
- Waveforms are labelled images, and results are announced.

**FAIL / PARTIAL:**
- iPhone SE overflows 329 px and its drop zones are below the fold (MEDIUM).
- Every locale has an English \<title\> and meta, and the subtitle, badges, stepper, drop-zone text, Compare button and accordions are English (MEDIUM-HIGH, SEO).
- ja desktop overflows by 3 px (LOW).
- `/ar/` returns 404, so RTL is N/A.
- Prices are USD-only in all 6 countries (by design?).
- Result view: 9 contrast failures on 11 px captions (MEDIUM).
- Focus is lost after Compare (LOW).
- The strip cells are title-only and colour-only (LOW).
- The Feedback FAB overlaps the right-rail ad CTA (LOW).

**Ads:** keep them. Use reserved, fixed-height slots below the tool and in the side rails (as now), with a clear zone around floating buttons. Never put an ad between the drop zones and the result.

## Suggested direction (interpret freely)

1. **Verdict integrity.**
   - Compute the headline score over the *union* of both files' non-silent time. Or report two numbers: "match over the overlap" and "coverage".
   - Derive the verdict from the same per-second cells the strip shows.
   - Mark unmatched non-silent seconds as "no counterpart" (a distinct colour), not as silence.
   - Add a length/coverage sentence whenever durations differ by more than about 5%.
   - Fix the middle axis label.
2. **Trial meter.**
   - Check why a fresh `dev:` scope can inherit `usageToday:10`, and why one `usage.log` can move the count by more than 1. A likely suspect is a per-IP pool merged with the device scope; verify in code.
   - Make the cap dialog's "You've used today's 10 trial uses" true for the visitor.
3. **Packaging.**
   - Rewrite FAQ #2 and Details to the current method.
   - Add FAQs (different lengths, the 4-minute limit, colours, formats and size, the diff WAV, trial uses).
   - Update the blog and link it from the tool.
   - Re-record the video on the current UI with trial-uses wording.
   - Use one video title everywhere.
4. **Locales.** Translate the remaining UI strings, the title and the meta, including the server HTML, or pull the locales from hreflang.
5. **Polish.**
   - 320 px header overflow and a compact stepper on phones.
   - Contrast of the 11 px captions.
   - Focus to the result after Compare.
   - Name the failing file in the error toast.
   - Consistent Quick Buy flows.
   - JSON-LD Offer period.
   - Clear zone for the Feedback FAB.

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy honesty ("Files never stored", "Runs on your device", "no audio was uploaded").
- Don't change pricing in this work.
- The counters here are display-only evidence. Verify backend behaviour in code.

## Process

Inspect CompareAudio (alignment, cell classification, score, verdict), UsageAndUpgradeStrip and the usage router → restate → propose → implement → verify with `scripts/` and `test-cases.md` (AC-01…AC-44).
