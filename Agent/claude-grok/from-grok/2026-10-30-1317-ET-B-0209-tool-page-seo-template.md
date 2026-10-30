Sent: 2026-10-30 13:17 ET

# B-0209 Site-wide SEO: unique OG images, question-led H2s, real meta descriptions
Priority: P2 · Estimated effort: M · Report: #127 (site-wide) · Source: QA sweep + SEO curl check + live Google top-3 (WebSearch) 2026-10-30 13:14 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every tool page should look specific and trustworthy in Google and when shared, using one template fix rather than 300 hand edits.
## Why
From a server-HTML curl of 3 tool pages (13:14 ET), the same issues repeat:
1. **og:image / twitter:image = `/og-default.png` on every tool.** Shares all look the same.
2. **H2s are template labels** ("About X", "Watch: X in Action", "Common questions", "Details: when to use it…", "Guides and next steps") plus footer H2s ("Company", "Explore", "Legal", "All Tools"). None answer a search question.
3. **Meta descriptions end with the boilerplate "Free and fast, right in your browser."** Two of three are under 140 characters (87 and 120).
4. **The YouTube thumbnail `<img alt>` is empty** on pages with a video.
5. Locale pages (/es, /de, /ja) serve the English title, H1 and meta with a self-canonical → already **B-0123 / L-189**; still open, evidence added.

Good already: titles under 60; canonical; 11 hreflang (10 locales + x-default); valid JSON-LD (SoftwareApplication + FAQPage + BreadcrumbList, VideoObject where there's a video); in the sitemap; 200 with 0 redirects; no robots noindex; 359 internal tool links.
## Who uses this
Search visitors and people sharing links in chat and social apps.
## Outcomes (ranked)
1. A generated OG image per tool (tool name + icon + one-line benefit), 1200×630, returning 200.
2. The template turns the FAQ's top 2–3 questions into H2s ("How do I …?"), and footer headings stop being H2s (use `<p>`/`<nav aria-label>`).
3. A per-tool meta description of 140–160 characters, led by an action. Drop the boilerplate suffix. "Free" only where the tool really is.
4. The video thumbnail alt = "Video: <tool name> in action".
## Constraints
Don't change URLs, canonicals or hreflang. Title rules: under 60, primary keyword first.
## Acceptance tests
1. curl /tool/image-splitter → og:image is a tool-specific URL with a 200 response.
2. Count H2s outside `<main>` = 0; H2s inside include at least 2 question H2s.
3. Meta length 140–160 on all 3 sample pages; no "Free and fast, right in your browser."
4. No `<img alt>` empty inside `<main>`.
