Sent: 2026-11-20 08:40 ET

# Video findings: i01IkvYUEVo

- **Run:** 2026-11-19 14:02 EST. yt-dlp metadata and a 720p mp4 (not kept); 19 frames at 1 per 3 s, a contact sheet and crops in `video/`.
- **Metadata:** "How to Use Unit Converter – Free Step-by-Step Walkthrough", 57 s, uploaded 2026-09-23 (UTC date), 0 views at fetch time. It is embedded on the tool page and in the sitemap.

| Finding | Evidence | Severity |
|---|---|---|
| **Old UI.** It shows 4 category tabs (Length, Weight, Temperature, Area); live has 15 (Volume, Speed, Time, Data, Pressure, Energy, Power, Angle, Frequency, Fuel economy, Cooking). The old subtitle reads "Convert length, weight, temperature, and more", and the old breadcrumb reads "Converters & Calculators" (now "Unit, Date & Everyday Calculators"). There is no all-units list, swap, pair pages or export bar | `video/z22.png`, `video/z28.png`, `video/sheet01.png` | P2 |
| **The description lists 11 categories** (it omits angle, frequency and cooking, and says "data" not "data transfer") | `video/info.json` | P2 |
| **"Free" wording** in the title, the description ("Try Unit Converter free", "Free daily uses") and the end card ("200+ Free Productivity Tools") | `video/info.json`, `video/sheet01.png` | P2 (brand wording) |
| Only ~15 s of the 57 s is the tool; the rest is intro, logo, presenter and outro | `video/sheet01.png` | P2 |

The figures in the clip (34 km) are not wrong; the issue is coverage. Re-record the current UI in a clean profile with trial-use wording, or with "no trial use needed" for converters.
