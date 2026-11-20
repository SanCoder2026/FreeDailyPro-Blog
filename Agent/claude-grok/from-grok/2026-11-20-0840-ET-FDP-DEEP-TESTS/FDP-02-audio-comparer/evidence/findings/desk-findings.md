Sent: 2026-11-20 08:40 ET

# Compare Two Audio Files (audio-comparer): desk findings

- **Written:** 2026-11-19 10:15:24 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/audio-comparer. Slug from TEST-ORDER.md row 2 and tools.csv.
- **Classification:** Professional Tool, Audio Tools. It has 10 trial uses per day, a $1 day pass and a $4.99 monthly pass.
- **TEST-ORDER note:** test-plan rank 3, with 258 views, top GSC clicks 122 and 19 s engagement (bounce). These are cited, not refreshed. **Current GSC data is not available.**
- **Method:** read-only curl of the tool, `/es`, blog, category, sitemap and robots; the tool's JS bundles (`evidence/js/`); YouTube metadata and auto-captions via yt-dlp, plus 15 frames sampled at 1 every 5 s; WebSearch for competitors and indexing.
- **The video was not watched with audio.** The summary below comes from captions, metadata and sampled frames.

## SEO (check 8)

| Element | Live value | Note |
|---|---|---|
| Title | Compare Two Audio Files Online - Similarity Check \| FreeDailyPro (64) | OK |
| Meta | "Compare two audio files and see a similarity percentage for the two recordings. Audio compare tool that runs in your browser." (125) | Short. It doesn't sell the per-second strip, waveforms, A/B play or difference WAV, which competitors advertise |
| H1 | Compare Two Audio Files | OK |
| H2 | How it works · Watch… · About… · How to use it · Common questions · Details: when to use it, limits, privacy · Guides and next steps | No question-style H2 such as "How to check if two audio files are the same" |
| Canonical | self | OK |
| hreflang | 11 (en, es, pt, fr, de, ja, hi, zh, ko, id, x-default) | Every locale serves the **English \<title\> and meta description**. The server HTML for /es has an English H1 and FAQ; the H1 and part of the UI are translated client-side only. See `devices-locales-findings.md` |
| robots | no meta robots; robots.txt allows / (disallows /api/) | indexable |
| OG/Twitter | full set, image og-default.png | generic image |
| JSON-LD | WebSite, SoftwareApplication (Offer 4.99 USD, no billing period), VideoObject ("How to Compare Two Audio Files Online – Similarity Percentage"), FAQPage (**2** questions), BreadcrumbList | All parse |
| Images | YouTube thumbnail `alt=""` | LOW |
| Internal links | Breadcrumb → /category/audio-tools; "More from Audio Tools": Transcribe Audio to Text, Extract Audio, Audio Trimmer; Guides → /blog/free-audio-tools-voice-memos-podcast-cleanup (200; the slug contains "free") | **The tool page does not link its own post /blog/audio-comparer** (0 occurrences in the HTML) |

## Indexing (check 7)

- Tool URL in sitemap.xml: lastmod 2026-11-19, with a `video:video` block titled "How to Compare Two Audio Files Online **Free** – Similarity Percentage".
- Blog in the sitemap: lastmod 2026-09-18.
- WebSearch "freedailypro compare two audio files" (2026-11-19): the tool ranks first, the blog third, and a freedailypro.blogspot.com post second. Indexed. No rank or impression data (GSC not available).
- Locale URLs are not in the sitemap.

## FAQ and usage guide vs. real behaviour (check 11)

The page describes **two different algorithms**:
- **"How to use it"** (current, matches the JS and the live run): fingerprint over time, leading and trailing silence ignored, aligned by start offset, loudness evened out, per-second strip, waveforms, A/B, property table, difference WAV, and a 4-minute cap (JS `Te=240` s; live note "Only the first 4 minutes of each file were compared.").
- **FAQ #2 and the "Details" section** (old): "divided into equal time segments… normalized time basis… each divided into the same number of segments proportionally". This is no longer true.
- Only 2 FAQ questions. Missing: formats, size limit, 4-minute limit, different-length files, what the strip colours mean, the difference WAV, privacy, and trial uses.

## Blog (check 9)

- /blog/audio-comparer returns 200, self canonical, "Are These Two Audio Files the Same Recording? How to Check", dated September 18, 2026. It links the tool and embeds KZVe2ILAUD4.
- **Stale:**
  - It describes "the same number of equal time segments".
  - It advises "If one clip starts with ten seconds of silence, trim it with Audio Trimmer so the segments line up". The tool now aligns automatically: live, a 0.5 s and a 20 s lead-in were both detected.
  - It omits the strip, waveforms, A/B, difference WAV and 4-minute cap.
- Its "Reading the percentage" guidance conflicts with live results: half-matching audio scored 0.0%, and a clip vs. a mostly-different longer file scored 100%.

## YouTube video (checks 10 and 12)

- **Id and metadata:** KZVe2ILAUD4, 77 s. Uploaded 2026-09-23 08:26:54 EDT. 14 views.
- **Title:** "How to Use Compare Two Audio Files – Free Step-by-Step Walkthrough".
- **Tags:** generic (FreeDailyPro, free online tools, PDF tools…).
- **Description:** "Try Compare Two Audio Files free", "Free daily uses in your browser".
- **Burned-in captions:**
  - "How to Compare Two Audio Files Online Free – Similarity Percentage"
  - "Follow along — free in your browser"
  - "Subscribe for the next free tool"
- **Frames:**
  - Thumbnail art: "AUDIO COMPARE 98% MATCH Wow."
  - The screen recording shows the **old UI**: a single "Similarity 62.8% — Similar" card.
  - None of the following appear: the per-second strip, "Differs at", waveforms, A/B, loudness match, property table, difference WAV, Copy summary, or the trial-use strip.
  - Outro: "200+ Free Productivity Tools", while the site header now says 300+.
- **Verdict:** the video exists (check 10 PARTIAL), but it shows an outdated tool and off-brand "free" wording (check 12 FAIL).

## Competitors and user expectations (check 2)

From WebSearch on 2026-11-19:
- **Equivl:** offset plus tempo alignment; a clip found inside a longer file, with coverage; per-second strip; worst moments; up to 300 MB / 30 min.
- **WaveDiff:** spectrogram, A/B, manual offset, loop regions, **share link**, diff WAV export.
- **DiffALL:** per-second score, spectrogram diff, auto offset, LUFS/clipping, real-bandwidth check.
- **audiocomparer.com:** fingerprint map, up to 200 MB / 20 min, share link.
- **SongTools.ai:** AI summary and history (sign-in, credits).

**FreeDailyPro has** most of the core: score, verdict, strip, offset, waveforms, difference, A/B, loudness match, properties, diff WAV, and a text summary.

**Gaps:**
- Live-verified: no shareable result link; no clip-coverage reporting; a 4-minute cap with no window choice; no spectrogram in the result view.
- Unverified absence: tempo tolerance.

## Category, placement, duplicates, AI and demand (checks 17–22)

- **Placement:** Audio Tools category and breadcrumb. Correct.
- **Duplicates:** DUPLICATES.md cluster C24 (diff-checker, text-similarity-checker, compare-pdf, audio-comparer) has different inputs, so keep all four. No other audio compare tool.
- **AI fit:** the core comparison is deterministic DSP, which is right for trust. An optional AI layer ("explain what changed", or speech-aware comparison via transcription) could be a P2 Premium idea. It is not needed.
- **Demand:** an active competitor set. Test-plan data shows 122 GSC clicks but 19 s engagement, i.e. people arrive and leave fast.
  - That is consistent with an empty first screen (no sample result).
  - On phones the drop zones sit below the fold behind the stepper and an ad slot.
  - The verdicts are hard to trust when lengths differ.
- **Remove or merge:** no.
