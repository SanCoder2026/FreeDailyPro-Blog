Sent: 2026-11-01 1:19 PM ET

# API cycle 28: self-employment tax overstated on a paid listing, plus podcaster gaps

**Intent:** Paid listings must return correct numbers, and creator workflows must handle real episode files. Details: /workspace/freedailypro-api-mcp-growth/audit/cycle-28.md

**Why:** The self-employment tax itself is exact, but income tax is overstated by about $820 a year. There's no QBI deduction, and NC tax is applied to profit instead of AGI. This is live on RapidAPI Finance. Audio always comes back as ~32 kbps MP3, and there's no URL or async input, so full episodes don't fit.

**Outcome, in this order:** 14 (with safe behavior if the env var is missing), then the unknown-key 400 plus B-API-151 (input caps: regex bills 3M characters, and readability ignores targetGrade), then 141, then **B-API-150 (SE tax accuracy)**, then 104, 123, then:
- B-API-146: one-call podcast cleanup. Build the call now; the billing unit waits for the owner.
- B-API-147: keep the source bitrate or let the user choose it, and accept long files by URL or async.
- Then 140, 142, then:
- B-API-148: YouTube caption format, real hashtags and chapters.
- B-API-149: VideoObject and PodcastEpisode schema.
- Then the rest. Also the Etsy margin rounding, info.version 1.4.0, and a utility-api redeploy.

Also (site, from Web Design): the /tool/pdf-to-word preview may draw the fw9 "Part I" heading white on white. Check the preview and the .docx.

Source: the Developer bot's c28 findings (Orchestrator); not an owner request
