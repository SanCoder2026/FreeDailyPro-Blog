Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: video findings (check 10 and 12)

- **Embed on the page:** "Watch: BMI Calculator in Action". Play button "Play video: How to Calculate BMI & Daily Calories Online". JSON-LD VideoObject has the same name, uploadDate 2026-09-22.
- **YouTube** https://www.youtube.com/watch?v=SogofBA7ENk: title "How to Use BMI Calculator – Free Step-by-Step Walkthrough", 88 s, uploaded 2026-09-23, channel FreeDailyPro, **1 view** (yt-dlp 2026-11-20 22:47 EST). The description says "Try BMI Calculator free", "Free daily uses in your browser". Downloaded with yt-dlp and watched as 44 frames at 1 frame per 2 s (`evidence/video/sheet01-04.png`).

## What the video shows vs the live tool
| Video | Live tool (2026-11-20) |
|---|---|
| Intro card "CALCULATE BMI & DAILY CALORIES — FREE · PRIVATE · NO LOGIN" | No calorie output (that is the Calorie Calculator); "free" wording |
| Page title "BMI & Calorie Calculator", subtitle "Calculate BMI and daily calorie needs", badge "10 free uses daily" | H1 "BMI Calculator — Body Mass Index and Healthy Weight Range"; no trial badge |
| Only weight and height; result card shows the number and label | Age, sex, waist, Asian option, gauge, healthy range, Prime, Ponderal, WHO table, target, steps, exports |
| Typing 7 kg shows **BMI 2.4 Underweight**; empty weight shows **0.0**; height 17 cm shows **BMI 3114.2 Obese** (frame f026) | These inputs are now rejected with range messages (B16, B18, B21) |
| A browser tab "FreeDailyPro_All_Tools.xlsx" and "Ask Gemini" are visible | An internal sheet name is visible (P2) |
| End card "Your All-in-One Platform for 200+ Free Productivity Tools" | Site says 300+; "Free Productivity Tools" wording |

**Verdict:** FAIL (P1). The video shows an older, simpler "BMI & Calorie Calculator" and a 3114.2 BMI bug that has since been fixed. It promises daily calories and none of today's features. Re-record it and align the embed title, VideoObject name and YouTube title (no "free").
