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
| L-092 | camera | full-photo download badged with no prior notice (crop path discloses) | #73 (B-0063) | open | 2026-10-29 |
| L-093 | camera | capture/JPG/crop/count work at 1280+390 (fake device) | #73 | verified | 2026-10-29 |
| L-094 | camera | no tool_completed on download | B-0060 | open (evidence added) | 2026-10-29 |
| L-095 | camera | mobile load CLS 0.173 | B-0041 | open (evidence added) | 2026-10-29 |
| L-096 | word-counter | abbreviations overcount sentences; CJK words; no speaking time/keyword density | #73 (B-0065) | open | 2026-10-29 |
| L-097 | word-counter | related-search ad block injected inside stats grid (390) | B-0041 | open (evidence added) | 2026-10-29 |
| L-098 | word-counter | no tool_completed on Copy stats | B-0060 | open (evidence added) | 2026-10-29 |
| L-099 | audio-normalizer | Spotify −14 / Podcast −16 split; ACX RMS copy (#45) | #45 | verified | 2026-10-29 |
| L-100 | audio-normalizer | MP3 out ~110k VBR, no bitrate choice; ACX MP3 non-compliant | #73 (B-0064) | open | 2026-10-29 |
| L-101 | audio-normalizer | 13×13 limit-peaks checkbox | #45 → B-0064 | open (still fails) | 2026-10-29 |
| L-102 | audio-normalizer | counter 6→0 mid-session | B-0055 | open (evidence added) | 2026-10-29 |

Mature: Income Tax federal engine (L-074). Mature candidates: Split PDF, QR Code Generator, Custom QR, Unit Converter (coverage only). Roman Numeral Converter becomes **mature** once B-0036 + B-0052 verify.
Batch 4 (#73): Audio Normalizer loudness engine verified (all presets ±0.05 LU); mature once B-0064 lands. Word Counter mature-candidate after B-0065.
| L-103 | video-to-gif | corrupt file silent fail + charge (batch-12) | — | verified fixed (#74) | 2026-10-29 |
| L-104 | video-to-gif | start past end (batch-12) | — | verified fixed (clamped) (#74) | 2026-10-29 |
| L-105 | video-to-gif | GIF size shown in MiB labelled MB | B-0067 | open | 2026-10-29 |
| L-106 | compress-video | limit copy 200 MB vs GIF 5 GB | B-0067 | open | 2026-10-29 |
| L-107 | compress-video | counter 10→0 after one run | B-0055 | open (evidence added) | 2026-10-29 |
| L-108 | compress-video | post-use CLS 0.10–0.138 desktop | B-0041 | open (evidence added) | 2026-10-29 |
| L-109 | sign-pdf | SIGN-01 download no-op | — | verified fixed (#74) | 2026-10-29 |
| L-110 | sign-pdf | SIGN-02 charge on drop | — | verified fixed (#74) | 2026-10-29 |
| L-111 | sign-pdf | SIGN-03 metadata overwritten | — | verified fixed (#74) | 2026-10-29 |
| L-112 | sign-pdf | SIGN-04 signature offset | — | verified fixed (#74) | 2026-10-29 |
| L-113 | sign-pdf | "Tap" hint on desktop | B-0067 | open | 2026-10-29 |
| L-114 | sign-pdf + video-to-gif | meta description 48/76 chars | B-0068 | open | 2026-10-29 |
| L-115 | compress-image | Don't change dimensions pre-ticked → target missed | B-0066 | open | 2026-10-29 |
| L-116 | compress-image + resize-crop | post-use CLS 0.166–0.203 / 0.119 | B-0041 | open (evidence added) | 2026-10-29 |
| L-117 | resize-crop | plan: fit mode ignored | — | UI pass all 5 modes; API untested (read-only) | 2026-10-29 |

Batch 5 (#74–75): Compress Video, Video to GIF, Sign PDF, Resize & Crop = mature-candidates. Compress Image mature after B-0066.
| L-118 | barcode-generator | 0.1% CTR pos 7.8; 1× default too small for print; GS1 note; filename | B-0069 | open | 2026-10-29 |
| L-119 | barcode-generator | validation (check digit, length) | — | verified pass (#77) | 2026-10-29 |
| L-120 | invoice-generator | payment terms missing on PDF | B-0071 | open | 2026-10-29 |
| L-121 | invoice-generator | PDF output + totals maths | — | verified pass (#77) | 2026-10-29 |
| L-122 | compress-image | default ticked (B-0066) – unticked path reaches 186 KB | B-0066 | open (evidence added) | 2026-10-29 |
| L-123 | word-to-pdf | theme font → Times | B-0070 | open | 2026-10-29 |
| L-124 | word-to-pdf | meta 75 chars | B-0070 | open | 2026-10-29 |
| L-125 | universal-file-converter | Original → Download shown/ungated after convert | B-0070 | open | 2026-10-29 |
| L-126 | pdf-to-word | tables/lists/links/page size/metadata | — | verified pass (#76) | 2026-10-29 |
| L-127 | multiple | pool 0 on desktop vs 10 on mobile; p2w 10→0 after 1 use | B-0055 | open (evidence added) | 2026-10-29 |
| L-128 | universal + barcode + compress-image | post-action CLS 0.12–0.28 | B-0041 | open (evidence added) | 2026-10-29 |

Batch 6 (#76–77): PDF to Word mature-candidate; Word to PDF after B-0070; Barcode after B-0069; Invoice after B-0071. Universal converted-download untested (pool), retest.
| L-129 | mortgage-calculator | mobile load CLS 0.32–0.48 (auto-placed ad + results block) | B-0072 | open | 2026-10-29 |
| L-130 | /tools | desktop load CLS 0.28–0.37 (tool-chip row) | B-0072 | open | 2026-10-29 |
| L-131 | bmi-calculator | snippet 0/504 at pos 6.8 | B-0073 | open | 2026-10-29 |
| L-132 | jwt / uuid / hash | meta descriptions 73–76 chars | B-0074 | open | 2026-10-29 |
| L-133 | hash-generator | file hashing missing (plan) | — | fixed, verified #79 | 2026-10-29 |
| L-134 | /developers | false claims / 404 use-cases | B-0020 | fixed, verified #80 | 2026-10-29 |
| L-135 | categories + sitemap | indexability (B-0035) | B-0035 | site-side clean, #80 | 2026-10-29 |
| L-136 | calculators | no tool-completion GA event | B-0060 | open (evidence added) | 2026-10-29 |
| L-137 | uuid mobile | pool 0 → limit dialog | B-0055 | open (evidence added) | 2026-10-29 |

Batch 7 (#78–80): BMI, Loan, JWT, UUID, Hash, /developers, category pages **mature**; Mortgage after B-0072. Carry-over: Barcode UPC-A/ITF-14, Universal converted download, Invoice desktop.
| L-138 | /tool/book-maker | HTTP 404 + noindex, JS redirect (106 views) | B-0075 | open | 2026-10-30 |
| L-139 | find-replace | .docx output stored uncompressed, 23× size | B-0076 | open | 2026-10-30 |
| L-140 | tip / magazine / book-writing-toolbox | mobile load CLS 0.19–0.55; shared container shift | B-0077 | open | 2026-10-30 |
| L-141 | tip-calculator | invalid input shows "—" without message | B-0078 | open | 2026-10-30 |
| L-142 | book-writing-toolbox | mobile icon buttons without accessible names | B-0078 | open | 2026-10-30 |
| L-143 | find-replace / universal | pool: mobile replaced at 0; 2→0 after one download | B-0055 | open (evidence added) | 2026-10-30 |
| L-144 | universal-file-converter | CSV→XLSX converted download (carry-over) | — | verified OK #81 | 2026-10-30 |

Batch 8 (#81–82): Percentage, Magazine (after B-0077) mature; Tip after B-0077/B-0078; Find & Replace after B-0076; Book toolbox export untested (Google sign-in wall). Carry-over: Barcode UPC-A/ITF-14 (pool 0), Invoice desktop.
| L-145 | citation-generator | snippet 0/2,448 at pos 8.6; meta 77 chars | B-0079 | open | 2026-10-30 |
| L-146 | citation-generator | Chicago website drops the year | B-0080 | open | 2026-10-30 |
| L-147 | random-number-generator | invalid min disables Generate with no reason | B-0080 | open | 2026-10-30 |
| L-148 | /multitool-apps | HTTP 404 (55 views) → /premium-apps | B-0075 | open (evidence added) | 2026-10-30 |
| L-149 | citation / password mobile | load CLS 0.24 / 0.23 | B-0077 | open (evidence added) | 2026-10-30 |
| L-150 | image-to-pdf / password / case-converter | outputs blocked (0 trial uses all run) | — | carry-over | 2026-10-30 |

Batch 9 (#83–85): /workflow-products mature; RNG mature after B-0080; Citation after B-0079/B-0080. Screenshot Tool needs a headed run. Carry-over: Image to PDF, Password, Case Converter outputs, Barcode UPC-A/ITF-14, Invoice desktop.

Batch 10 (#86–87, admin session, 30 Oct 07:55 ET carry-overs):
| L-151 | image-to-pdf | multi-image output verified (2p Letter, JPG passthrough) | — | verified; mature | 2026-10-30 |
| L-152 | password-generator | 20-char ±symbols + Copy | — | verified; mature | 2026-10-30 |
| L-153 | case-converter | chained modes garble; no download | B-0081 | open | 2026-10-30 |
| L-154 | barcode | UPC-A/ITF-14 check digits PNG+SVG | — | verified | 2026-10-30 |
| L-120 | invoice-generator | +evidence #87: Net 30 in dropdown, due date correct, still not printed on PDF | B-0071 | open (still fails) | 2026-10-30 |
| L-155 | universal-file-converter | JPG→PNG output real PNG | — | verified | 2026-10-30 |
| L-156 | universal-file-converter | blob: ERR_FILE_NOT_FOUND; scripted click no download | B-0082 | open | 2026-10-30 |
Evidence: B-0069 (filenames barcode.png / barcode (1).png). L-125 (B-0070 bypass) untestable in admin session, stays open. L-150 carry-over closed.

Batch 11 (#88, capability-gap sweep 1, owner rule 30 Oct: mature = works AND ≥ best competitor):
| L-157 | income-tax | capability gap: refund/owed, credits, itemised, other income, tax-year switch, API depth | B-0089 | open (P2) | 2026-10-30 |
| L-158 | tip-calculator | capability gap: multi-% compare, service/country presets, uneven split, reverse | B-0090 | open (P2) | 2026-10-30 |
| L-159 | bmi-calculator | capability gap: BMI Prime/PI, WHtR, target mode, CDC child percentile, API | B-0091 | open (P2) | 2026-10-30 |
| L-074 | income-tax | RE-LABEL: federal engine accurate (re-checked #88) but **not mature** under the new rule (B-0089) | B-0089 | re-labelled | 2026-10-30 |
| L-072 | income-tax | +evidence #88: 401(k) age groups (under 50 / 50+ / 60–63) now in the UI; limits not re-verified | B-0057 | open (evidence) | 2026-10-30 |
Re-label: BMI "mature" (batch 7, #78) → **not mature** (B-0091). Percentage and Loan "mature" labels are under review in the next capability batch.

Batch 12 (#89, capability-gap sweep 2):
| L-160 | mortgage-calculator | capability gap: chart, yearly view, biweekly, DTI 28/36, cost growth, API | B-0086 | open (P2) | 2026-10-30 |
| L-161 | percentage-calculator | capability gap: solve-any-two, steps, pp vs %, bps, history | B-0087 | open (P2) | 2026-10-30 |
| L-162 | loan-calculator | capability gap: frequencies, solve-for, APR, deferred/bond, compare | B-0088 | open (P2) | 2026-10-30 |
Re-labels (#89): Loan "mature" (batch 7) → not mature; Percentage "mature" (batch 8) → not mature (small gap); Unit Converter L-081 mature-candidate → under review (not benchmarked yet).

Batch 13 (#90, capability-gap sweep 3; batch-11 briefs renumbered B-0083/84/85 → B-0089/90/91 on Orchestrator request):
| L-163 | roth (none) | no Roth tool: /tool/roth-ira-calculator → 404, not in sitemap | B-0100 | open (P2) | 2026-10-30 |
| L-164 | 401k-calculator | capability gap: $72k total limit, tiered match, early withdrawal, drawdown, Roth 401k, vesting/fees | B-0101 | open (P2) | 2026-10-30 |
| L-165 | compound-interest | capability gap: chart, rate range, withdrawals, solve-for, continuous; merge API into loan service | B-0102 | open (P2) | 2026-10-30 |

Batch 14 (#91, capability-gap sweep 4; owner 08:16: book watermark intentional; ApyHub API handled directly by owner with Claude):
| L-166 | college-529-calculator | 4 inputs lack accessible names; no cost-based goal, tax comparison or table (2,029 impr, 0 clicks) | B-0103 | open (P2) | 2026-10-30 |
| L-167 | rmd-calculator | capability gap: Joint Life spouse table, projection, deadline/penalty, data year/owner, inherited | B-0104 | open (P2) | 2026-10-30 |
| L-168 | fire-calculator | capability gap: savings-rate framing, chart, Coast/Barista FIRE | B-0105 | open (P2) | 2026-10-30 |
