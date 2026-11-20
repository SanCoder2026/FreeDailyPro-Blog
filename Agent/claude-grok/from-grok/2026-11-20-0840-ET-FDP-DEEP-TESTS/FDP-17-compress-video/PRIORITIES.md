Sent: 2026-11-20 08:40 ET

# Priorities: FDP-17 Compress Video

- **Written:** 2026-11-19 15:55 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).

## P1
1. **Outdated platform presets (R1).**
   - "8 MB (Discord)": Discord's free limit is 20 MB (FAQ updated 2026-09-30).
   - "16 MB (WhatsApp)": WhatsApp's default video limit is 64/100 MB.
   - Users over-compress. Update the presets, the blog and the meta wording.
2. **Copy describes options and defaults that don't exist (R2).**
   - "Light" appears in the FAQ, blog, YouTube description and video.
   - The guide says "Manual Quality, which is selected when the tool opens" (Medium is).
   - The pass count is described three ways (code: up to 3).
   - "over 200 MB" vs the 50 MB trial cap.
3. **Targets above the source make bigger files labelled "Target reached" (R3):** 12.9 MB → 97 MB with the 100 MB preset. Skip or cap.

## P2
4. Small-target misses: audio fixed at 128 kbps, 100 kbps video floor; the advice "Try Strong or 720p" is wrong for a 720p source (R4).
5. Manual Quality 50% made a 10 Mbps 1080p file 4.4% larger despite the FAQ's "caps near 90%" (honest message shown).
6. "Get a Day Pass to download" shown under the free "Keep original (download)" button.
7. Non-video file error: phone-codec advice + "check the browser console (F12)".
8. Units: limit messages in MiB, results in decimal MB.
9. iPhone SE: drop zone top at y=615 against 584 (just below the fold). 320 px header overflows 9 px (site-wide).
10. Accessibility: no `aria-pressed` on modes; unnamed Manual Quality slider; result line not announced; focus to body after Compress.
11. Video j2eUOdBo3bk: old UI (Light, "guaranteed", Pro badge), never shows a result, 40 s outro, personal bookmarks and files, "Free" wording.
12. Blog: Light, 8 MB Discord, "25 MB is 26,214,400 bytes" (the tool uses 25,000,000), 16 MB preset missing, Trim Video detour (trim is built in).
13. Locales: English titles, meta and most UI; VideoObject name ≠ YouTube title.
14. No "Continue with" hand-off after the result (Video Converter / Trim would fit).
15. **WebKit/iOS processing unverified** (box harness limit). Check on a real device.
