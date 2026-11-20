Sent: 2026-11-20 08:40 ET

# FDP-02 Compare Two Audio Files: priorities

- **Written:** 2026-11-19 10:28:59 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check number and its REPRODUCE.md ID.

## P0: ship first

1. **Make the score agree with the evidence for partial matches (checks 1, 3, 6; R-01).**
   - **Outcome:** a file whose first half matches scores about 50%, "Partly the same", consistent with its 5 green and 5 red cells.
   - **Why:** today it reads 0.0% "Different audio" next to a strip showing half matching. That is the headline number contradicting itself.
2. **State coverage when lengths differ (checks 1, 6; R-02).**
   - **Outcome:** a 12 s clip vs. a 72 s file reads, for example, "File 1 matches 0:00–0:12 of file 2 (17% of it)", never a bare "100% Same recording".
   - **Outcome:** unmatched, non-silent seconds are coloured as differing or "no counterpart", not grey "silence".
   - **Why:** clip-in-file is a core use case. Today a mostly-unrelated file is called the same recording.
3. **Make the trial meter honest for a new visitor (checks 5, 16; R-03).**
   - **Outcome:** a fresh device shows 10 remaining, and each Compare spends exactly 1.
   - **Why:** display evidence shows one Compare dropping 10 → 0, and fresh devices loading at 0. A visitor can hit the paywall before or right after their first use. Verify server-side; this box IP was busy.

## P1: next

4. **Rewrite FAQ #2 and "Details"** to the current method (alignment, silence trimming, the 4-minute cap, per-second strip). Add FAQs on different lengths, colours, formats and size, the diff WAV and trial uses (checks 6, 11; R-04).
5. **Update the blog** (drop "trim so the segments line up"; show the strip, waveforms, A/B and diff WAV) and **link it from the tool page** (checks 8, 9; R-05).
6. **Re-record the video** on the current UI. Use trial-uses wording, audio tags, and one title across YouTube, JSON-LD and the sitemap (checks 10, 12; R-06).
7. **Translate the locale pages end to end** (title, meta, subtitle, badges, stepper, drop zones, Compare button, accordions, and the server HTML), or drop them from hreflang (checks 8, 16; R-07).
8. **Make the Quick Buy flows consistent:** both email-first, or document why Monthly goes straight to Stripe (check 5; R-08).
9. **Result-view contrast:** the 11 px waveform captions must reach at least 4.5:1 (check 15 a11y; R-09).

## P2: enhancements and polish

10. **320 px phones:** fix the 329 px header overflow, and use a compact or collapsible stepper so the drop zones are above the fold (R-10).
11. **Small UI fixes:**
    - Middle time-axis label (0:00 → mid-time) (R-11).
    - Name which file failed in the decode toast.
    - Size toast in MB, matching the OS.
    - Focus to the result after Compare (R-12).
12. **Share a result:** an optional link with the summary (no audio), extending the "Copy result summary" idea (check 14).
13. **More than 4 minutes:** choose the compared window, or a Premium longer cap (check 2).
14. **Ads and FAB:** reserve a clear zone so the floating Feedback button never covers the right-rail ad (R-13). Keep the ads; use reserved slots.
15. **SEO polish:** a longer meta that names the strip, A/B, diff WAV and offset detection; a tool OG image; video thumbnail alt; a JSON-LD Offer billing period.
16. **Optional Premium idea:** "explain what changed" (AI), or speech-aware comparison via transcription (check 19).
