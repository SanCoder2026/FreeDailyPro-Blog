Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: reproduction steps (guest, https://www.freedailypro.com/tool/thumbnail-gen)

1. **P1 ZIP not charged:**
   1. In a fresh context with uses left (strip "N remaining today"; `localStorage fdp-usage-v1.usageToday` < 10), drop `testfiles/V3_720p.webm`.
   2. Press Capture Thumbnail twice (e.g. Original size, then YouTube 1280×720). Counter unchanged.
   3. Press Download on one image → counter +1 (badged PNG).
   4. Press "Download all as ZIP" → ZIP of both images, counter unchanged, no dialog; reload: unchanged.
   5. Script: `scripts/tg-gate.js`. At 0: `tg-drain.js` (Download and ZIP open the cap dialog; stop at the email prompt).
2. **4K upscaling:** drop the 720p WebM, choose "YouTube 4K 3840 x 2160 (recommended)", Capture → a 3840×2160 image from a 1280×720 source, no warning. Compare with the page's "There are four output sizes".
3. **Misleading error:** rename a text file to `x.mp4`, drop it → "Your browser can't play this video (often iPhone HEVC video)…"; type 0:01, Capture → "Could not read that frame from the video".
4. **Time clamp:** on a 5 s clip type `0:59` + Enter → frame at 5.00 s, box still shows 0:59.
5. **Video:** https://www.youtube.com/watch?v=wGXvbaUKqQI at ~0:14: old UI, bookmarks bar visible.
6. **Payment (stop before typing):** Quick Buy (day) → "Day Pass, $1" email prompt; Quick Buy (monthly) → Stripe Checkout.
