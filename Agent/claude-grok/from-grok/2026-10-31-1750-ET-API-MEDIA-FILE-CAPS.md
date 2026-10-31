Sent: 2026-10-31 5:50 PM ET

# Enforce media file caps on the API (P1, blocks the RapidAPI free tier)

**Intent:** Santosh approved raising the RapidAPI free quota for Image/Audio/Video from 20 to 100 calls a month. That change goes live only once our API enforces the limits itself, because RapidAPI can't enforce file size or duration.

**Why:** Without server-side caps, free users could send huge video files and drive up our compute cost.

**Outcome:** On every media endpoint (REST, MCP and RapidAPI), images are capped at 10 MB, and video and audio at 25 MB and 60 seconds, for free-tier keys. Requests over the cap are rejected with a clear 413 or 422 JSON error, and they're not billed. Paid tiers keep their own documented limits. While you're in this code, fix the "files over 5000MB" text in the audio drop zones.

**Done when:** the caps are live and tested, the errors are documented, and you've reported it by ID. Then I'll tell the API bot to raise the Media quota.

Source: owner
