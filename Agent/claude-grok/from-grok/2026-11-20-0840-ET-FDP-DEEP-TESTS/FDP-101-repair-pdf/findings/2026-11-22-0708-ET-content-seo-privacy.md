Sent: 2026-11-22 07:08 ET

Sent: 2026-11-22 07:08 ET

# FDP-101 content, SEO, locales, video, privacy

- **SEO:**
  - title "Repair a Corrupted PDF Online - Recovery Tool | FreeDailyPro" (60); meta 102 chars (short); canonical self;
  - tool + blog in sitemap.xml; hreflang 10 + x-default;
  - JSON-LD: WebSite, SoftwareApplication (4.99 USD/MON), VideoObject, FAQPage (13), BreadcrumbList;
  - og:image og-default.png.
- **FAQ (13):**
  - true: privacy (verified), non-PDF naming, failure links exist, the "Recovered 4 of 9" wording exists in code;
  - not true on the lenient path: "The tool flags the file as cut off in that case", "rather than a broken or incomplete download that looks like it worked" (T01);
  - contradiction: "can't recover … a truncated download" vs "fixes … a file cut short by an interrupted download";
  - near-duplicate pairs: damage kinds ×2, "look exactly the same" / "match the original exactly".
- **Details:**
  - "a page survives only if every part it needs is present" (lenient path keeps blank pages, T01);
  - "Expect bookmarks and fillable fields to be missing after the fallback scan" (true for bookmarks; the widget value survived on P02);
  - "nothing is requested from any other server, no helper download happens" (two code chunks + auth.me are fetched on Attempt Repair).
- **Guide** /blog/repair-pdf (1,538 words):
  - structure vs cut-off ✓, password case ✓, privacy ✓;
  - "Recovered 9 of 14 pages" example (T01 gets 5 of 5);
  - salvage via PDF to JPG / Word (dead ends, P2 #6).
- **Video** T7f0XAhH6Oo:
  - "How to Use Repair PDF – Free Step-by-Step Walkthrough", 1:20, uploaded 30 Sep 2026, 15 views at test time;
  - JSON-LD says "How to Repair Corrupted PDF Online – Recover Broken Files | FreeDailyPro.com", 2026-08-22;
  - frames: intro thumbnail "REPAIR CORRUPTED PDF · FREE ONLINE TOOL · FREE · PRIVATE · NO LOGIN", walkthrough in an older layout, success result, subscribe card, end card "200+ Free Productivity Tools";
  - the description says "Try Repair PDF free" / "Free daily uses".
- **Locales:** es/pt/fr/de/ja/hi/zh/ko/id return 200 with translated H1s (Reparar PDF, Réparer PDF, PDF Reparieren, PDF修復, PDF रिपेयर करें, 修复PDF, PDF 복구, Perbaiki PDF). /ar 404 (sitewide).
- **Privacy** (PV01, privacy-pv.json):
  - 107 requests during drop → repair → preview; none had the file name or content in the URL or body;
  - GA collect only page_view (dl, dt);
  - hosts: freedailypro.com, googletagmanager, pagead2.googlesyndication, googleads.g.doubleclick, stats.g.doubleclick, analytics.google, fundingchoicesmessages, ep1/ep2.adtrafficquality, www.google.com, i.ytimg.com, api.producthunt.com;
  - storage: localStorage fdp-days-v1, fdp-usage-v1, fdp-device-id (value not recorded), freedailypro-recent-tools, google_*; sessionStorage fdp-v, fdp-i1; no IndexedDB.
- **Payment:** Quick Buy Day → "Day Pass, $1 · Enter your email and go straight to payment…" (stopped); Monthly → checkout.stripe.com/g/pay/cs_live_REDACTED (stopped).
- **Drive:** "Open from Google Drive" → accounts.google.com sign-in popup (closed). "Save to Google Drive" at 0 uses → cap dialog.
- **Share:** "Link copied to clipboard" → https://www.freedailypro.com/tool/repair-pdf.
- **Keyboard / a11y:**
  - 7 Tabs to the drop zone (Home, PDF Tools, favourite, share, Quick Buy ×2, drop zone);
  - the failure message is in a polite live region, and focus falls to BODY;
  - axe desktop: label-content-name-mismatch (serious, .right-2), region; Pixel 7 clean.
- **Matrix:** 10 devices 200; iPhone SE 329/320 px (button); others no overflow; desktop CLS 0.025–0.039.
