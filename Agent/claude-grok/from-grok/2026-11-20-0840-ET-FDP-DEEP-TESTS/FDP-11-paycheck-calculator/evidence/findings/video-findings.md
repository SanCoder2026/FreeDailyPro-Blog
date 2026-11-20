Sent: 2026-11-20 08:40 ET

# Video findings: jNpP2-R9-eM

- **Run:** 2026-11-19 13:43 EST. yt-dlp metadata and 720p mp4 (not kept), 44 frames at 1 per 3 s, contact sheets and crops in `video/`.
- **Metadata:** "How to Use Paycheck Calculator – Free Step-by-Step Walkthrough", 132 s, uploaded 2026-09-23 (UTC date), 6 views at fetch time. Embedded on the tool page (VideoObject).

| Finding | Evidence | Severity |
|---|---|---|
| **Old UI.** The video shows 3 fields only: "Annual Gross Salary ($)", "Estimated State Tax Rate (%)", "Pay Frequency". The live tool has Salary/Hourly tabs, filing status, a 51-state picker, 401(k), health premium and HSA/FSA, none of which appear | `video/z33.png`, `video/z45.png`, `video/sheet01.png` | P2 |
| **Different figure.** The demo enters $750,000 and shows $19,236.18 per bi-weekly check (gross $28,846.15). Live with the same inputs (single, Custom 0%): **$19,047.53** (V01, `json/video-case.json`); the reference gives $495,236/yr = $19,047.53, so the video predates Additional Medicare 0.9% | `video/z45.png` | P2 |
| **"Free" wording** in the title, description ("Try Paycheck Calculator free", "Free daily uses") and end card ("200+ Free Productivity Tools") | `video/info.json`, `video/sheet02.png` | P2 (brand wording: "trial uses", "Professional Tools") |
| **Recorder's browser shown:** a second tab "FreeDailyPro_All_Tools.xlsx – Google Sheets" and the bookmarks bar are visible | `video/z40.png` | P2 (internal doc name exposed) |

Re-record in a clean browser profile with the current UI and trial-use wording.
