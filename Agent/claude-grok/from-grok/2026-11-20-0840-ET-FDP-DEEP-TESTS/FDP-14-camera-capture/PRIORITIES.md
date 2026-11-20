Sent: 2026-11-20 08:40 ET

# Priorities: FDP-14 Camera Capture

- **Written:** 2026-11-19 14:45 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).

## P1
1. **Phone first screen (R1).**
   - iPhone SE: Start Camera at y≈828 on a 568 px screen.
   - After Start, the preview is at y≈616 and Capture at y≈795.
   - After Capture, the download and crop buttons run down to y≈1187.
   - "Take a picture online" users on phones must scroll to start, to see themselves and to shoot.
2. **Trial badge on photos is not disclosed up front (R2).**
   - The notice only appears after Capture.
   - The FAQ, How-to, meta and blog (onboarding headshot, ID crop) don't mention it.
   - The mark is policy; the fix is wording and placement.
   - The actual badge on the file is pending (RERUN row 14). Santosh may want to decide on marking face photos at all.
3. **Video (R3).** A real person's face (partly covered by a sticker) and the recorder's camera model are visible. It shows the old UI with "10 free uses" badges. Re-record.

## P2
4. Front / rear camera does nothing on laptops and external webcams, and the picker then shows "Choose a camera" while live (R4).
5. Accessibility (R5):
   - Focus is lost to `<body>` after Start and after Capture.
   - The captured and cropped `<img>` have no alt (axe critical `image-alt`).
   - Crop is mouse/touch only.
   - The camera picker has no accessible name.
6. "Save as JPG" exists only while the preview is live; after Capture the user must Retake to change format.
7. The Copy cap dialog and toast say "downloading needs a pass" / "downloading was not done" (R6).
8. Missing countdown, square/passport aspect lock and mirror (the competitor baseline). The blog sends users to a second tool to square the crop.
9. VideoObject uploadDate (2026-08-22) and name don't match YouTube (2026-09-30, a different title).
10. 9 hreflang locales serve English under a foreign `lang`.
11. Code hygiene:
    - `URL.createObjectURL` is called in render and never revoked.
    - A mousedown on the photo clears the current crop result.
12. iPhone SE: 9 px header overflow (site-wide).

## Pending (not a finding yet)
- Cost per Download Full / Download Crop / Copy with uses left; the badge on files; file names. See RERUN-AFTER-RESET row 14 (after 7:00 PM ET).
- "Save to my cloud storage" needs sign-in (untested).
