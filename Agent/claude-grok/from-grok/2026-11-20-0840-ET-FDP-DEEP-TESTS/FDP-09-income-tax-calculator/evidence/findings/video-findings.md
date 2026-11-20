Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: YouTube video findings

- **Video:** https://www.youtube.com/watch?v=UvcrEE6Swwc. Title "How to Use Income Tax Calculator – Free Step-by-Step Walkthrough", 141 s, uploaded 20260923, **0 views** (yt-dlp info.json, 2026-11-19 13:10 EST). It is embedded on the tool page and in the sitemap.
- **Evidence:** `video/v.info.json`, 47 frames (1 every 3 s, 960 px; a subset is packaged) and `video/contact.jpg`.

## Shows current capabilities? PARTIAL (P2, stale)
The recording shows an older UI (frame f008):
- The H1 is "Income Tax Calculator", the breadcrumb is "Tax Calculators", and the search says "Search 200+ tools".
- The inputs are only income, a **state tax rate in %** and an SE checkbox ("pay full FICA, not just employee half"). There is no filing status, state picker, pre-tax/401(k), per-period or age group.
- The note reads "based on current 2026 US federal brackets for a single filer".
- **Result at $85k, 5% state:** take-home $64,322, total tax $20,679, FICA $6,503. For the current UI with no state, `ref_federal.py` gives federal $9,870, so with 5% the total would be 9,870 + 6,503 + 4,250 = $20,623. The video's $20,679 implies federal $9,926, which suggests older figures.
- **Wording:**
  - The badge "10 free uses daily" and the intro card "FREE · PRIVATE · NO LOGIN" use "free" wording.
  - The outro says "200+ Free Productivity Tools", while the site now says 300+.
  - The description says "Try Income Tax Calculator free" and "Free daily uses". The owner rule is to say "trial uses", and copying costs a use.
- **Privacy (P2):** the frames show the recorder's personal browser bookmarks bar (Gmail, Netflix, Prime Video, Twitch, etc.) and the Windows taskbar. Re-record in a clean profile.
- **Not shown:** filing status, state picker, 401(k), SE QBI, per-period, and copy/save/print.
- **Recommendation:** re-record with the current UI. Show a state, HoH and an SE case, and say that copy/save/print use a trial use (or stop charging for them).
