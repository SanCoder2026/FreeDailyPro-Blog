# B-0023 Richer structured data on hub pages; decide blog hreflang
Priority: P3      Estimated effort: 40 min

## Goal / why
Tool pages have rich structured data (FAQ, SoftwareApplication) but the hub pages that should rank for broad searches (/developers, /corporate-safe-tools, /professional-tools) only have WebSite/SearchAction. Tool pages also carry about 11 hreflang alternates while blog posts often carry none, which is an inconsistent signal to search engines.

## What to change
- Add structured data that matches what is on each page: https://www.freedailypro.com/developers (e.g. SoftwareApplication or WebAPI plus FAQPage if the page has FAQs), https://www.freedailypro.com/corporate-safe-tools and https://www.freedailypro.com/professional-tools (e.g. CollectionPage with an ItemList of the tools shown). Keep the existing WebSite/SearchAction.
- Blog hreflang: if blog posts exist only in English, have them declare only their own language (plus x-default) and write the reason in the commit; if translated versions exist, give them the same alternate set as tool pages. No half-state.

## Acceptance criteria
- The three hub pages pass Google's Rich Results Test / schema validator without errors.
- One sample blog post has a deliberate, consistent hreflang set; the commit says which option was chosen.
- Any count shown in schema follows the owner's count rule (category's own number on category pages; "300+ professional tools, premium applications and workflow products" for the site in general).
- Verification `live and checked`.

## Not in scope / do not decide
Blog text. Tool page schema. Translating blog posts.

## Owner decisions needed
none

Source: SEO bot (technical SEO flags, Oct 28).
