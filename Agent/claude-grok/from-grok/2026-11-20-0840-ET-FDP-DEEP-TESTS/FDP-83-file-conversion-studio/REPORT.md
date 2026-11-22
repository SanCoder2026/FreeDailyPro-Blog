Sent: 2026-11-21 19:08 ET

# FDP-83 File Conversion Studio (file-conversion-studio): deep test report for Claude

- **Written:** 2026-11-21 19:07 EST (box `date`, ET). Testing ran 2026-11-21 18:55–19:06 EST.
- **Tool:** https://www.freedailypro.com/tool/file-conversion-studio
  - TEST-ORDER row 83: **Workflow Product**, PDF Tools, "category group: PDF Tools, cluster C05" (with universal-file-converter #22, convert-image #34, heic-to-jpg #102, webp-converter #103).
  - **Offer:** $29.99 a month, 7-day trial the first time, sign-in first. "No trial uses and no day pass." Files are processed in the browser.
  - **No video** (none on the page; none of the 511 channel videos is about it). **No /blog/file-conversion-studio** (404), but the guide "Convert Any File Without Switching Tools" (/blog/convert-any-file-without-switching-tools, 10 Nov 2026) is its post.
  - **GSC data is not available.** No API/MCP testing.
- **What a guest can test:** only the paywall. The Studio itself (`FileConversionStudio-DzZvPuK7.js`) renders only when the server's `workflowProduct.status` says `entitled`, so all conversion, recipe, queue, ZIP, CSV and run-log behaviour is **untested** and listed in SIGNIN-NEEDED. I checked the page's claims against the shipped Studio code instead (desk).
- **Testers:** desk (page, 5 FAQs, Details, JSON-LD, both guides, gate + Studio JS); Playwright guest in Chromium and Firefox (`live.json`: gate, Start trial target, `?checkout=success` as a guest, links, keyboard order, Workflow Products listing, Universal File Converter cross-link); matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. "Start 7-day trial" led to the /profile sign-in page; I stopped there and typed nothing. No card, email or ad clicks. No site or repo changes. Device ID and request inputs redacted.
- **Sign-in (untested):** Start 7-day trial → https://www.freedailypro.com/profile?returnTo=/tool/file-conversion-studio?autoBuy=workflow:file-conversion-studio, then Stripe; the whole Studio; Manage or cancel.
- **RERUN-AFTER-RESET:** none (no trial uses involved). I did not touch the existing RERUN rows.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to an office worker deciding whether to start a $29.99 trial.

**Owner context:** Workflow Products need sign-in and a paid plan or trial; without Santosh's go-ahead they are tested up to the sign-in or Stripe page. The gate is server-side (`workflowProduct.status`), so there is no gate gap to report as a guest.

**P0 / P1:** none found as a guest.

**P2 — where to look:**
- **Nothing shows the product before the trial.** For a $29.99/month product the page has no screenshot, video or sample output: "What you get before you pay" lists `converted-files.zip`, `results.csv`, `run-log.json` and a recipe pack but offers none to look at. Other Workflow Products (e.g. #43) have a video. A short video, a screenshot of the queue and a sample `results.csv` would let people judge it before signing in.
- **Locale pages are not translated.** All 10 hreflang pages (/es, /de, /ja…) show the English H1, intro, price card, FAQ and title. Only the nav and one badge change. hreflang tells search engines these are translations.
- **Meta description is cut mid-sentence:** "…with saved recipes, a quality panel, your own file." (the page text continues "file names, a ZIP and a results report").

**P3:**
- `?checkout=success` on the URL shows a guest "Thank you. We are confirming your payment with Stripe; this page opens by itself in a few seconds." It polls `workflowProduct.status` 20 times (about 60 s), then the message silently disappears. Show it only to a signed-in user who has just checked out, and say so if confirmation never arrives.
- The page sits in **PDF Tools** with "More from PDF Tools: Merge, Split, Compress PDF", although it converts pictures, Office, audio and video. The Workflow Products breadcrumb is right.
- The full Studio bundle (54 KB) is downloaded for guests who only see the paywall.
- iPhone SE 9 px overflow (header button); ja desktop 3 px; axe desktop label-content-name-mismatch + region (sitewide).

## Intent

Someone with a mixed weekly folder wants to know, before giving a card, that one recipe will turn it into a clean ZIP and report. The paywall is clear and honest: price, trial terms, cancel wording, "no trial uses and no day pass", files stay in the browser, and three single-step tools to try first. The page copy matches the shipped Studio code: the 5 starter recipes, {name}/{date}/{n}/{n:3}, the 200 MB audio/video limit, Pause/Stop/Retry, results CSV, run log, recipe packs, the first frame of animated GIFs, flat or by-type ZIP. What's missing is any way to *see* it.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | UNTESTED | Behind sign-in + trial. Code matches the claims. |
| 2 | Completeness | PASS (desk) | All listed features present in code. |
| 3 | Ease of use | PASS (gate) | CTA reached in 24 Tabs; clear terms. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | PASS (to sign-in) | Start trial → /profile sign-in with autoBuy return. Stopped. |
| 6 | Information correct | PASS | Terms, limits, formats match code. |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PARTIAL | Meta description cut mid-sentence; untranslated locale pages. |
| 9 | Blog | PASS | Guide accurate (recipes, patterns, 200 MB, trial). |
| 10 | YouTube video | FAIL | None exists. |
| 11 | FAQ / guide correct | PASS | Matches code. |
| 12 | Video shows current capability | N/A | No video. |
| 13 | Storage | PASS (desk) | Local; recipes hold settings only. |
| 14 | Sharing | PASS | Share/Create Shortcut present. |
| 15 | Downloads | UNTESTED | ZIP/CSV/log need entitlement. |
| 16 | Usage count | N/A | Subscription; no trial uses. Gate server-side. |
| 17 | Categorization in section | PARTIAL | PDF Tools for a mixed-format product. |
| 18 | Correct section of site | PASS | Workflow Products listing card present. |
| 19 | AI need and demand | PASS | "bulk convert files"; chat AIs can't batch-convert local files. |
| 20 | Merge better? | No | Distinct from Universal File Converter (one file vs whole job). |
| 21 | Remove? | No | — |
| 22 | Duplicates | C05 | Overlaps UFC/convert-image by design (single-step upsell). |

## After fixes, rerun

- `px83-live.js` (G01 sees a video/sample; G03 no message for guests), `run-matrix.js config.json` (locales translated), view-source meta description. With Santosh's go-ahead and a trial account: the SIGNIN rows.
