Sent: 2026-11-20 08:40 ET

# FDP-02 Compare Two Audio Files: reproduce

- **Written:** 2026-11-19 10:28:59 EST (box `date`, ET).
- **Setup:** use a guest or fresh profile, with no sign-in and no ad clicks. Test files are in `evidence/testfiles/`, or run `scripts/make-testfiles.sh`.
- **Trial uses:** each Compare spends one. If the strip says "0 remaining today" on load, open another fresh context or wait for midnight UTC (7:00 PM ET).
- **Automation:** run the scripts from a folder with Playwright installed (`cd /workspace/deep/tools-env` on the box).

## R-01: half match scores 0.0%

1. Open https://www.freedailypro.com/tool/audio-comparer.
2. File 1 = `a440_10s.wav`, File 2 = `mix_440then880_10s.wav`. Press Compare Audio.
3. **Seen:** "0.0% Different audio", while the strip shows the first 5 cells green and "Differs at 0:05–0:10".
4. **Expected:** about 50% "Partly the same".
5. Script: `node scripts/ac-verify-pairs.js '[["a440_10s.wav","mix_440then880_10s.wav","r01"]]'`.

## R-02: clip vs. a mostly-different longer file scores 100%

1. `melody_12s.wav` vs `melody_then_noise_72s.wav`.
   - **Seen:** 100.0% "Same recording, possibly a different format or quality", plus the note "File 2 runs longer…".
2. `melody_12s.wav` vs `noise20_then_melody_32s.wav`.
   - **Seen:** 100.0% "Same recording; file 2 starts 20.03 s later".
3. Swap step 1 (the 72 s file as File 1).
   - **Seen at about 10:11 EST:** 100.0%, with 60 grey ("silence") cells over loud noise and no "Differs at".
   - Re-run when uncapped; that artefact was lost in a box restore.
4. **Expected:** a coverage statement and a proportional score.
5. Script: `node scripts/ac-verify-pairs.js '[["melody_12s.wav","melody_then_noise_72s.wav","r02a"],["melody_12s.wav","noise20_then_melody_32s.wav","r02b"],["melody_then_noise_72s.wav","melody_12s.wav","r02c"]]'`.

## R-03: trial meter

1. Run `node scripts/ac-pool-probe.js 5`. It opens 5 fresh contexts with no action, and records the strip, localStorage and the page's own `usage.check` responses.
   - **Seen (09:57 EST):** 4/4 "0 remaining today" with new `dev:` scopes.
2. Run `node scripts/ac-functional.js usage`. It does two fresh-context runs: add files → Compare → Play 1/2 → Match loudness → Download → Copy → Share → Another pair → reload. The strip is recorded after every step.
   - **Seen:** run 1 is correct (10 → 9, then flat).
   - **Seen:** run 2 went **10 → 0 on one Compare** (10:15:05 EST).
3. Also try from a residential IP. **Display-only evidence; confirm in code.**

## R-04: FAQ and Details describe the old method

Open "Common questions" (question 2) and "Details: when to use it…". They say "equal time segments… normalized time basis". Compare with "How to use it" on the same page, which describes alignment, silence trimming and the 4-minute cap.

## R-05: blog

1. Open https://www.freedailypro.com/blog/audio-comparer. It shows the segment method and the advice to trim leading silence with Audio Trimmer.
2. Search the tool page source for `/blog/audio-comparer`. It has 0 hits.

## R-06: video

Play the embedded video (KZVe2ILAUD4). It shows the old "Similarity 62.8%" card and "free" cards. Check: the title on YouTube vs. JSON-LD VideoObject.name vs. the sitemap `video:title`.

## R-07: locales

1. Open /es/tool/audio-comparer (and pt, fr, de, ja, hi, zh, ko, id).
2. Read `<title>`, the subtitle, the badges, the stepper, the drop zones, the Compare Audio button and the accordion headers. They are English, while the H1 and strip are translated.
3. Run `curl -s https://www.freedailypro.com/es/tool/audio-comparer | grep -o '<h1[^<]*<[^>]*>[^<]*'`. The server H1 is English.

## R-08: Quick Buy

1. Click the $1 Quick Buy. An email dialog opens. Stop.
2. Click the $4.99 Quick Buy. It goes straight to checkout.stripe.com. Stop. Type nothing.
3. Script: `node scripts/ac-capped-flow.js`.

## R-09: contrast

Run `node scripts/ac-a11y-result.js` (one Compare, then axe on the result view). **Seen:** color-contrast on 9 nodes, e.g. #155dfc on #0d1820 at 3.42:1, 11 px.

## R-10: 320 px

Run `node run-matrix.js scripts/config.json --only=devices "--devices=iPhone SE"`. **Seen:** scrollWidth 329, and drop zone 1 at y=632 with the fold at 568.

## R-11: time axis

Run any comparison. The labels under the waveforms read "0:00 · 0:00 · 0:12".

## R-12: focus

Keyboard-only: Tab to the drop zones, then Enter, then Compare. After the result, `document.activeElement` is \<body\>.

## R-13: Feedback FAB over the ad

Firefox at 1440×900, first screen: the floating "Feedback" button sits over the lower part of the right-rail ad, including its CTA (`evidence/screens/devices/desktop-1440x900-firefox-fold.png`). Do not click the ad.
