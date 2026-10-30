# FreeDailyPro retest ledger (cycle 2)
Rules: one row per tool+issue. Never re-report an open issue or an already verified fix. Claude's "done" ≠ verified: mark verified-fixed only after an own pass; if a claimed fix fails, re-report as "claimed fixed (report #N) — still fails". Dates ET.
Status values: verified-fixed | open | claimed-fixed-unverified | improvement-suggested | owner-decision | by-design | mature.

| ID | Tool | Issue | First report # | Status | Last checked |
|---|---|---|---|---|---|
| L-001 | homepage | H1 extracts "Task.One" (no space) | homepage-figures brief / B-0022 | verified-fixed | 2026-10-29 |
| L-002 | homepage | count claims inconsistent (title/footer 300+, cards 250+ tools / 100+ apps) | homepage-figures brief; SW-34 | owner-decision | 2026-10-29 |
| L-003 | homepage | search box below fold on desktop, no submit/hint/label, no no-results state, suggestions at 2 chars | #66 (B-0053) | open | 2026-10-29 |
| L-004 | site-wide | auto-ads keyword chips inside headings/labels/results | orch B-0041 (confirmed live in #66) | open | 2026-10-29 |
| L-005 | site-wide | GA site-search event missing | guidance pack | open (in B-0053) | 2026-10-29 |
| L-006 | homepage/site | privacy pop-up sticky (B-0002, claimed done "EEA/UK/CH only") | #46–65 (B-0002) | claimed-fixed-unverified (absent for US visitor; EEA not testable from US IP) | 2026-10-29 |
| L-010 | roman-numeral-converter | Date mode accepts 30 Feb / 31 Apr | #20 | verified-fixed | 2026-10-29 |
| L-011 | roman-numeral-converter | US date order option | #20 (improvement) | verified-fixed | 2026-10-29 |
| L-012 | roman-numeral-converter | vinculum >3999 (all 5 competitors have it) | #20 (improvement) | improvement-suggested (content part in B-0036) | 2026-10-29 |
| L-013 | roman-numeral-converter | CTR/title/meta/FAQ; /es Spanish content | B-0036 | open (not claimed) | 2026-10-29 |
| L-014 | roman-numeral-converter (/es + all tool pages) | /es hreflang → homepage set, html lang=en; hreflang + JSON-LD doubled after hydration | #66 (B-0052) | open | 2026-10-29 |
| L-015 | roman-numeral-converter | inputs <16px (iOS zoom) | #46–65 class (B-0016) | open | 2026-10-29 |
| L-016 | roman-numeral-converter | "Free" in title/meta | SW-26 | by-design (owner keeps free in SEO tags) | 2026-10-29 |
| L-020 | audio-comparer | identical/different scoring | #54 | verified (still PASS) | 2026-10-29 |
| L-021 | audio-comparer | "Free" in title | #54 / SW-26 | by-design (SEO tags); visible copy in B-0019 open | 2026-10-29 |
| L-022 | audio-comparer | 0% for same audio with offset or MP3 re-encode; sample-rate label 48 kHz for 44.1 kHz | #66 (B-0050) | open | 2026-10-29 |
| L-023 | audio-comparer | trial use counted on file select, inconsistent (9 vs 8) | #66 (B-0051) | open | 2026-10-29 |
| L-024 | audio-comparer | sample pair, A/B play, spectrogram, share link (competitors) | #66 | improvement-suggested | 2026-10-29 |
| L-025 | audio-comparer | trial tier 10/day $1/$4.99 | #54 SW-19 | by-design | 2026-10-29 |
| L-030 | pricing | Day Pass "Sign in to buy" label | Stripe audit / B-0027 | open (not claimed) | 2026-10-29 |
| L-031 | pricing | monthly needs email gate before Stripe | Stripe audit / B-0027 | open (not claimed) | 2026-10-29 |
| L-032 | pricing | /account, /workflows 404 | Stripe audit / B-0027 | open (not claimed) | 2026-10-29 |
| L-033 | pricing | API Upgrade → Google sign-in unexplained; mobile pop-ups over payment dialog | Stripe audit / B-0027 | open (not claimed; not retested) | 2026-10-29 |
| L-040 | merge-pdf | trial use only on download (not merge, not repeat DL) | B-0001 pattern | verified-fixed/PASS | 2026-10-29 |
| L-041 | merge-pdf | badge disclosed before download | SW-14 | by-design, disclosed | 2026-10-29 |
| L-042 | merge-pdf | result size label 1.7 KB vs 5,548 B file | #67 (B-0054) | open | 2026-10-29 |
| L-043 | merge-pdf | page thumbnails / per-page remove-rotate / ranges | #67 (B-0054) | improvement-suggested | 2026-10-29 |
| L-044 | merge-pdf | API ignores page selection | B-0040 | open (not claimed) | 2026-10-29 |
| L-045 | merge-pdf | guides link off-topic blogs | #17 | open (not retested) | 2026-10-29 |
| L-050 | camera-capture | capture/download PNG/JPG | #49 | verified (still PASS, pre-check) | 2026-10-29 |
| L-051 | camera-capture | "Free" in title | #49 SW-26 | by-design (SEO tags); visible copy B-0019 open | 2026-10-29 |
| L-052 | camera-capture | real iOS/Android permission flow | #49 | open (untested, needs device) | 2026-10-29 |

Mature: none yet. Roman Numeral Converter becomes **mature** once B-0036 + B-0052 verify.
