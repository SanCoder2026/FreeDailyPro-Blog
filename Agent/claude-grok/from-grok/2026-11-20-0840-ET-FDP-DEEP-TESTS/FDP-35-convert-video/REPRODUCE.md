Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: reproduction steps (guest, https://www.freedailypro.com/tool/convert-video)

1. **P1 one use per page load** (context with uses left; `localStorage fdp-usage-v1.usageToday` < 10):
   1. Drop `V01_h264_aac.mp4`, Output MOV, Convert, Download → counter +1.
   2. New → `V09.3gp` → MP4 → Download → unchanged. New → `V11_h264_noaudio.mp4` → MOV → Download → unchanged.
   3. Reload → `V05_h264.mkv` → MP4 → Download → +1.
   4. Script: `scripts/cvv-gate.js` (part 1).
2. **P1 preview at 0:** in a context at 0 remaining, convert any video. The result player shows the converted video; open its ⋮ menu (Chrome) → Download, or right-click → Save video as. Compare with a paid Download: identical bytes (`cvv-gate.js` records both hashes). The page's Download opens "Today's trial uses are done".
3. **Size copy:** drop a 70 MB MP4 → "trial use supports up to 50.0 MB… Upgrade to Pro for up to 200.0 MB", Convert disabled; the drop zone says "Large files (over 5 GB) may take longer".
4. **Output count:** open Output Format → six entries; compare with FAQ "the four outputs" and Limitations "four formats in the menu".
5. **Bad file:** drop a text file renamed `.mp4`, Convert → after ~12 s, the "codec this tool doesn't support (some phone-recorded .mov files…)" toast.
6. **Video:** https://www.youtube.com/watch?v=zqpLPhmyj9E at ~0:28 (file dialog with personal folders) and ~0:45 (old "Format Converter" UI).
7. **Payment (stop before typing):** Quick Buy (day) → "Day Pass, $1" email prompt; Quick Buy (monthly) → Stripe Checkout.
