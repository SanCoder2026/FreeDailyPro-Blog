Sent: 2026-10-30 11:49 ET

# QA Report 113 Addendum — admin-session results (11:42–11:44 ET, /profile confirmed)
Adds to #113 and does not change it. Downloads: batch-32/downloads/. I checked them with Python wave and numpy at 11:47 ET.

## 1. Paper checker + apa-good-v2.docx (L-217, L-225)
All 8 checks pass (admin session). This confirms that the #111 failures were caused by the test file → L-217 and L-225 verified.

## 2. audio-merger (L-224)
- a1 + a2 (44.1 + 44.1 kHz) → a1-merged_44k+44k.wav: 176,478 B, 44.1 kHz mono, 2.000 s ✓.
- a1 + a48 → a1-merged_44k+48k.wav: 44.1 kHz, 1.919 s. **My check:** my a48.wav fixture holds 44,100 samples at 48 kHz, which is 0.919 s (a fixture quirk, not 1 s). So 1 + 0.919 = 1.919 s is **correct**: the clip was resampled to 44.1 kHz with nothing lost. There is no warning about resampling (minor, B-0163 #2).
- The file list shows a48.wav as "86.2 KB · 0:00". The real size is 88,244 B = 86.2 KiB, so the **size is correct**. **"0:00" floors 0.919 s** → a display bug (minor, B-0163 #3; same family as L-213's 0:04→0:02 truncation).
- Both downloads are named "a1-merged.wav" (named after the first clip). Minor: a timestamp or count suffix would avoid overwrites (B-0163 #4).
- Ads and the sticky header cover the merge buttons; the admin run had to force-click → L-004 evidence. My headless overlap probe at 0 trial uses couldn't reach this state (the file list never rendered).
## 3. audio-trimmer (L-222)
- End before start → toast "Enter a valid end time", then the end **silently resets to 0:05**. Better: keep the typed value and highlight it (B-0157 test case already asks for an error; the reset is the new detail).
- 0:01→0:03 → trimmed_tone5s.wav: 176,478 B, 44.1 kHz, 2.000 s ✓.
## 4. silence-remover (L-223)
desilenced_sil.wav is 48 kHz mono, 2.300 s.
- Quiet-block scan (10 ms blocks, |x|<300): silence runs 1.00–1.30 s. That is **0.3 s of kept pause** between the tones, not edge padding.
  - It matches the "Shorten to about 0.3 s" pause option. The default mode in the admin run isn't recorded.
  - If "Remove them completely" was selected, this is a bug. If it was the default 0.3 s shorten, the output is right but the page label "0:04 → 0:02" understates 2.3 s.
- 44.1 kHz in → 48 kHz out was not requested (minor). The ledger grep for resampl/48 kHz/truncat found no existing row → **B-0163**.

## Ledger
L-217 and L-225 verified. L-222, L-223 and L-224 updated. New row L-229 (B-0163). L-004 has the new evidence.
