Sent: 2026-10-30 13:19 ET

# B-0211 Audio Comparer: match "compare audio files online" and show what the score means
Priority: P2 · Estimated effort: S · Report: #128 (SEO backfill) · Source: curl server HTML 2026-10-30 ~13:19 ET + GSC (analytics/2026-07-10-to-now-raw.md) + live Google top-5 (WebSearch)

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

SEO follow-up for audio-comparer. Feature gaps stay in B-0119, scoring bugs in B-0050/B-0122.
## Intent
People searching "compare audio" or "compare two audio files" should see, in the snippet and the page, that we give a similarity score and say where the files differ.
## Why
- GSC (page): 122 clicks / 2,427 impressions / 5% / position 11.2. That's the site's top click page after the homepage, but just off page 1.
- Queries:
  - "audio comparer" 6/71, position 9.2
  - "audio compare online" 3/35, position 6.8
  - "compare audio" 2/24, position 11.9
  - "compare audio files online" 1/11, position 7.5
  - "compare audio files" 1/9, position 6.3
- GA: 258 views, 19 s engagement (bounce).
## SEO
**Now** All checks pass except where listed: HTTP 200, 0 redirects; in sitemap; no robots noindex; self canonical; 11 hreflang; valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject); full OG/Twitter set. Generic og-default.png, template/footer H2s, boilerplate meta, empty video alt → **B-0209** (not repeated).
- Title "Compare Two Audio Files Online - Free Similarity Check" (54). Good keyword, but no brand.
- Meta is 130 chars and ends "Free audio compare tool that runs in your browser."
- H1 "Compare Two Audio Files" (good).
- **/es/tool/audio-comparer serves the English title and H1** → B-0123 evidence (es has 0 clicks).

**What the top results do** (13:19 ET: audiotoggle, formatter.org, WaveDiff, MKDiff, DiffALL):
- They promise "hear the difference": A/B toggle, ABX blind test, volume match.
- Visual views: waveform, overlay, spectrogram, difference.
- "Export difference WAV", share link.
- A clear table of "what the similarity % means" (WaveDiff: cross-correlation; a 0% caused by misalignment, so use the offset).
- MKDiff has a "what to check" table and a built-in sample pair.
- Formats listed (WAV, MP3, FLAC, OGG, M4A).

**Keyword gaps:** "A/B audio comparison", "audio diff", "compare mp3 files", "are two audio files the same", "ABX test".

**Suggested**
- Title: `Compare Two Audio Files Online – Audio Similarity % | FreeDailyPro` (58)
- Meta: `Compare two audio files online and get a similarity score with the moments that differ. Works with MP3, WAV, FLAC and M4A. Files stay on your device.` (149)
- H1: keep `Compare Two Audio Files`
- H2s:
  - "How to compare two audio files"
  - "What the similarity percentage means"
  - "Why the same song can score low (offset, re-encoding)"
  - "Supported formats"
- FAQ:
  - "How can I tell if two audio files are the same?" → "Load both. 100% means identical audio; the timeline shows where they differ."
  - "Can I compare an MP3 with a WAV?" → "Yes. Both are decoded on your device before comparing."
  - "Why is the score low for the same recording?" → "One file may start later or be re-encoded. Align the start first." (keep this consistent with the B-0050 fix)
  - "Are my files uploaded?" → "No."
## Outcomes (ranked)
1. Title and meta as above.
2. A "what the % means" H2 with a table. Wording must match what the tool really does after B-0050/B-0122.
3. Translated /es metadata (B-0123).
4. FAQ JSON-LD equals the visible FAQ.
## Constraints
Never claim offset detection or A/B features until they ship (B-0119).
## Test cases
1. Title 60 or fewer chars, starts with "Compare Two Audio Files".
2. Meta 140–160.
3. /es title and H1 in Spanish.
4. The similarity H2 exists in `<main>`.
