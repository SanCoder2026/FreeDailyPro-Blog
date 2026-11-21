Sent: 2026-11-21 14:10 ET

# FDP-64: reproduce

All guest, fresh browser contexts. Times EST. Professional trial uses reset at midnight UTC (7:00 PM ET).

1. **Save at 0 (P1):** a context at 10/10 (`SUF=-capped TRIES=20 px64-live.js zero`). Drop `tone-12s.wav`, Convert → player appears. Download → cap dialog. In real Chrome: player ⋮ → Download, or right-click → Save audio as: the MP3 saves. Compare md5 with a Download from a context with uses left (`tone-12s.mp3`, 7e24a7ecf8ff).
2. **Per-load charging (P1):** `TRIES=40 px64-live.js left`. Download (POST, 0→1) → Convert again to OGG → Download (no POST) → New file → Download (no POST) → reload → Download (POST, 1→2).
3. **Size limit:** drop a ~60 MB WAV: "trial use supports up to 50.0 MB…", Convert off; drop zone says 500 MB.
4. **OGG→OGG:** drop `tone.ogg` (32 kbps), choose OGG, Convert → error toast.
5. **Batch:** Several files, add 6 WAVs → 5 kept; Convert all; row download (POST) + ZIP (no POST).
6. **Sign-in stops:** Open from Google Drive → Google sign-in; Save to my cloud storage → sign-in dialog; Quick Buy Day → email; Monthly → Stripe.
