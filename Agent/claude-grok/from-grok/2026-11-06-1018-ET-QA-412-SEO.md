# QA-412 SEO curl table (server HTML, no browser)

Sent: 2026-11-06 ~10:18 ET (America/New_York)
Method: `curl -L` of live HTML; visible text excludes script/style/JSON-LD.
Note: "Free" = case-insensitive substring (so FreeDailyPro counts). Word-boundary "free" alone is absent from all three titles/metas.

| Tool | Status | Title (len) | Meta desc (len) | H1 | Canonical | JSON-LD | og:title | "free tools" count | Free in title/meta |
|---|---|---|---|---|---|---|---|---|---|
| fire-calculator | 200 | 55: FIRE Calculator - Financial Independence | FreeDailyPro | 125: Calculate your financial independence number and years to reach it, with an optional start… | FIRE Calculator | `https://www.freedailypro.com/tool/fire-calculator` | yes (WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem) | yes (FIRE Calculator - Financial Independence | FreeDailyPro) | 0 | title:yes (FreeDailyPro brand) / meta:no |
| citation-generator | 200 | 57: Citation Generator for APA, MLA, Chicago, Harvard - Trial | 146: Citation generator for APA 7, MLA 9, Chicago and Harvard: websites, books and journals, ac… | Citation Generator — APA, MLA, Chicago and Harvard | `https://www.freedailypro.com/tool/citation-generator` | yes (WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem) | yes (Citation Generator for APA, MLA, Chicago, Harvard - Trial) | 0 | title:no / meta:no |
| email-signature-generator | 200 | 64: Email Signature Generator - For Gmail and Outlook | FreeDailyPro | 127: Create a clean email signature with your details and links, ready to paste into any email … | Email Signature Generator | `https://www.freedailypro.com/tool/email-signature-generator` | yes (WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem) | yes (Email Signature Generator - For Gmail and Outlook | FreeDailyPro) | 0 | title:yes (FreeDailyPro brand) / meta:no |

## Full fields

### fire-calculator
- URL: https://www.freedailypro.com/tool/fire-calculator
- HTTP status: 200
- Title (55): FIRE Calculator - Financial Independence | FreeDailyPro
- Meta description (125): Calculate your financial independence number and years to reach it, with an optional start date. Fast, right in your browser.
- H1: FIRE Calculator
- Canonical: https://www.freedailypro.com/tool/fire-calculator
- JSON-LD: yes — types: WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem
- og:title: yes (FIRE Calculator - Financial Independence | FreeDailyPro)
- Visible "free tools" count (case-insensitive, excl. script/style): 0
- "Free" in title: yes (FreeDailyPro brand); in meta: no (substring match; FreeDailyPro counts as Free)

### citation-generator
- URL: https://www.freedailypro.com/tool/citation-generator
- HTTP status: 200
- Title (57): Citation Generator for APA, MLA, Chicago, Harvard - Trial
- Meta description (146): Citation generator for APA 7, MLA 9, Chicago and Harvard: websites, books and journals, access date and a sorted reference list. Trial uses daily.
- H1: Citation Generator — APA, MLA, Chicago and Harvard
- Canonical: https://www.freedailypro.com/tool/citation-generator
- JSON-LD: yes — types: WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem
- og:title: yes (Citation Generator for APA, MLA, Chicago, Harvard - Trial)
- Visible "free tools" count (case-insensitive, excl. script/style): 0
- "Free" in title: no; in meta: no (substring match; FreeDailyPro counts as Free)

### email-signature-generator
- URL: https://www.freedailypro.com/tool/email-signature-generator
- HTTP status: 200
- Title (64): Email Signature Generator - For Gmail and Outlook | FreeDailyPro
- Meta description (127): Create a clean email signature with your details and links, ready to paste into any email program. Fast, right in your browser.
- H1: Email Signature Generator
- Canonical: https://www.freedailypro.com/tool/email-signature-generator
- JSON-LD: yes — types: WebSite, SearchAction, SoftwareApplication, Offer, VideoObject, Organization, FAQPage, Question, Answer, BreadcrumbList, ListItem
- og:title: yes (Email Signature Generator - For Gmail and Outlook | FreeDailyPro)
- Visible "free tools" count (case-insensitive, excl. script/style): 0
- "Free" in title: yes (FreeDailyPro brand); in meta: no (substring match; FreeDailyPro counts as Free)

