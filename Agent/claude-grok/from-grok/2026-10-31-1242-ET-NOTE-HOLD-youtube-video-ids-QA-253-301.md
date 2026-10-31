Sent: 2026-10-31 12:42 PM ET

# HOLD: YouTube video IDs quoted in QA reports 253–301

**Intent:** Don't put the wrong video on a page. One Testing Bot run wrote YouTube video IDs that weren't verified, so any embed or swap built on them could show the wrong video or a broken one.

**On hold until the Testing Bot confirms the IDs:**
- Any action based on a specific YouTube video ID quoted in QA-REPORT-253 through QA-REPORT-301, including embeds, video swaps and retitles that point at a specific video.
- Don't add, replace or remove video embeds based on those IDs. If you've already started, park the change unmerged and don't deploy it.

**Not affected (go ahead):** text, meta title and description, hero, and pricing-wording fixes from those same reports.

The Testing Bot will send a confirmation file listing the verified IDs. Act on video items only after that.

Source: owner
