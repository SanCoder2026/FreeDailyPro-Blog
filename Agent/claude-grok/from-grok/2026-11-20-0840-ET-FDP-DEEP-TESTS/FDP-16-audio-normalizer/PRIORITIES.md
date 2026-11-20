Sent: 2026-11-20 08:40 ET

# Priorities: FDP-16 Audio Volume Normalizer

- **Written:** 2026-11-19 15:26 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).

## P1
1. **True-peak ceilings broken (R1).**
   - "Limit loud peaks…" on: a −16 LUFS result at **−0.51 dBTP** (ceiling −1.5).
   - Peak to −1 dB: **−0.07 dBTP**.
   - Use a true-peak (oversampled) limiter and true-peak measurement, and report dBTP.
2. **"Even out volume levels" contradicts the tool (R2).** The tagline, About and How to use promise evening out. The guide says the constant gain does not. Rewrite as loudness-to-target copy, or build a leveler.
3. **Dead-end errors and the Opus bug (R3).**
   - Silent, short, non-audio and stereo ~45 kbps Opus files show "Check the browser console (F12)".
   - Show the specific message.
   - Fix the Vorbis bitrate floor so Opus → OGG works as the page promises.
4. **Drop zone below the fold on iPhone SE (R4):** y=724 vs a 584 px viewport.

## P2
5. "Large files (over 500 MB)" vs the 50 MB trial / 200 MB Pro limits (R5).
6. 24-bit WAV saved as 16-bit; the FAQ says "a WAV stays lossless" (R6).
7. AAC: −15.67 with "couldn't reach −16", and TP −1.11 against a −1.5 ceiling (R7).
8. Target counts disagree: "first four" (FAQ), "five of six" (guide), "five" (blog).
9. Step 2 "Choose a target" never shown as done for the default Podcast target.
10. Target buttons lack `aria-pressed`; the summary isn't announced (not a live region); focus goes to `<body>` after Normalize.
11. Blog: "Podcast / Spotify is -16 LUFS", "five targets", "Each normalization counts" (normalizing isn't charged; Download is).
12. Video WG-hQcqm-as: old UI, "Upload the video" caption, personal Downloads list, "Free" title, description and outro.
13. Locales: English title, meta, subtitle, steps and drop zone on all 9; VideoObject name ≠ YouTube title.
14. iPhone SE 320 px: header "Open menu" overflows by 9 px (site-wide).
15. Merge Volume Booster in as a fixed-gain mode; cross-link the ACX Audiobook Checker from the Audiobook target.
16. **Policy note for Santosh:** the full result plays in the preview at 0 remaining; only Download and Drive are gated. Confirm this matches "results count".
17. **WebKit/iOS processing unverified** (box harness limit). Check on a real device.
