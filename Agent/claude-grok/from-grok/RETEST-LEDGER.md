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
| L-053 | site-wide (compress/split/qr/bulk/income-tax) | trial counter differs between server instances (usage.check 0 vs 10 for same IP; fresh visitor sees 0; reload restores uses) | #68 (B-0055) | open | 2026-10-29 |
| L-054 | compress-pdf | B-0022 "Smallest" mode name in FAQ/help/meta | B-0022 | verified-fixed | 2026-10-29 |
| L-055 | compress-pdf / paywall | B-0021 Day Pass first + limit_hit/upgrade_cta_view events | B-0021 | verified-fixed (cta_click not triggered — gate rule) | 2026-10-29 |
| L-056 | compress-pdf | Aggressive = Extreme byte-identical; Extreme never grey/B&W; Balanced skips lossless level 2 | #68 (B-0056) | open | 2026-10-29 |
| L-057 | compress-pdf | counting: compress free, 1 use on download | B-0001 | verified-fixed | 2026-10-29 |
| L-058 | compress-pdf | target-size download, >50 MB file, iOS | #68 | open (untested — pool exhausted/B-0055) | 2026-10-29 |
| L-059 | split-pdf | multi-range → ZIP of all files (UI) | test-plan row 7 / B-0040 (API part stays open) | verified-fixed (UI) | 2026-10-29 |
| L-060 | split-pdf | range validation messages, overlap warning, combine order | #68 | mature-candidate (PASS) | 2026-10-29 |
| L-061 | split-pdf | desktop docW 1840 once (not reproducible, likely ad) | #68 | watch (orch B-0041) | 2026-10-29 |
| L-062 | split-pdf | visual page picker / split by bookmarks/size | #68 | improvement-suggested | 2026-10-29 |
| L-063 | qr-generator | all content types encode correctly, logo→H, contrast warning | #69 | mature-candidate (PASS) | 2026-10-29 |
| L-064 | qr group | PDF/EPS export, frames, scan check, CSV upload, custom-qr meta 54 chars, tel normalise | #69 (B-0058) | improvement-suggested | 2026-10-29 |
| L-065 | bulk-qr | ",no name" keeps comma (#43) | #43 | claimed-fixed-unverified (ZIP blocked by B-0055) | 2026-10-29 |
| L-066 | bulk-qr | 13×13 checkbox / inputs <16px mobile (#43) | #43 | verified-fixed | 2026-10-29 |
| L-067 | custom-qr | #47 PASS — no open items; functional rerun skipped (premium + selector) | #47 | open (rerun next) | 2026-10-29 |
| L-068 | income-tax | default state Custom 5% | #21 | verified-fixed | 2026-10-29 |
| L-069 | income-tax | pre-tax > income negative take-home | #21 | verified-fixed | 2026-10-29 |
| L-070 | income-tax | income -1 silent | #21 | claimed fixed (report #21) — still fails (B-0057) | 2026-10-29 |
| L-071 | income-tax | NY state uses 2025 rates under 2026 label ($4,952 vs $4,859.75 @100k) | #70 (B-0057) | open | 2026-10-29 |
| L-072 | income-tax | 401(k) limit check lacks 50+/60–63 catch-up | #70 (B-0057) | open | 2026-10-29 |
| L-073 | income-tax | CA $100k = $5,312 unconfirmed vs FTB 2026 | #70 (B-0057 audit) | open (verify) | 2026-10-29 |
| L-074 | income-tax | federal math + FICA + SE + counting (1/visit) | #70 | mature (federal) | 2026-10-29 |
| L-075 | site-wide | B-0055 recheck: 24/24 loads usageToday 0 at 22:28–22:30 ET; pool emptied with no day change (the UTC day had rolled over at 20:00 ET, yet usage was 10 at 22:05) | #71 (B-0055) | open — reset without a day change adds evidence; flapping not reproduced this run | 2026-10-29 |
| L-076 | compress-pdf | target size 2 MB → 1.49 MB, text + link kept, 1 use on download | #71 | verified (was untested) | 2026-10-29 |
| L-077 | qr-generator | 2000 px PNG download | #71 | verified (was blocked) | 2026-10-29 |
| L-078 | bulk-qr | ",no name" keeps comma (#43) | #43 | verified-fixed (was claimed-fixed-unverified L-065) | 2026-10-29 |
| L-079 | custom-qr | PNG download desktop+mobile, premium limit message | #47/#71 | verified; mature-candidate | 2026-10-29 |
| L-080 | bulk-qr (mobile) | CLS 0.153 | B-0041 | open (evidence added) | 2026-10-29 |
| L-081 | unit-converter | accuracy 11 categories, temp edge cases, swap, counting | #72 | mature-candidate (PASS) | 2026-10-29 |
| L-082 | unit-converter | missing power/angle/frequency/cooking; no inputmode decimal | #72 (B-0062) | improvement-suggested | 2026-10-29 |
| L-083 | unit-converter / grammar-checker | no tool_completed GA event on use | #72 (B-0060) | open | 2026-10-29 |
| L-084 | unit-converter | CLS desktop 0.185 / mobile 0.135 | B-0041 | open (evidence added) | 2026-10-29 |
| L-085 | grammar-checker | jumpd auto-fix; an banana; it's tail; you're message (#31) | #31 | verified-fixed | 2026-10-29 |
| L-086 | grammar-checker | "Me and him goes", "I seen" (#31 P3) | #31 | open (not re-briefed) | 2026-10-29 |
| L-087 | grammar-checker | valid UK spelling auto-changed to US | #72 (B-0059) | open | 2026-10-29 |
| L-088 | grammar-checker | then/than, effect/affect, less/fewer missed; 681-bullet list ungrouped | #72 (B-0059) | open | 2026-10-29 |
| L-089 | grammar-checker | CLS desktop 0.133 (video embed) | B-0041 | open (evidence added) | 2026-10-29 |
| L-090 | url-shortener | /s/* → 410 with explanation | owner removal fa78b7f | verified | 2026-10-29 |
| L-091 | url-shortener | /tool/url-shortener bare 404; slash URL 301→404 | #72 (B-0061) | open | 2026-10-29 |

Mature: Income Tax federal engine (L-074). Mature candidates: Split PDF, QR Code Generator, Custom QR, Unit Converter (coverage only). Roman Numeral Converter becomes **mature** once B-0036 + B-0052 verify.
